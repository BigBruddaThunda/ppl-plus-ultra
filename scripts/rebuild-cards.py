#!/usr/bin/env python3
"""rebuild-cards.py — PPL± Card Rebuild Orchestrator

Reads existing GENERATED cards, regenerates content using the upgraded
fallback template in batch-generate-deck.py, overwrites in-place (content only,
filenames preserved), validates, and reports before/after quality scores.

Supports abacus-aware rebuilding: each card is rebuilt using its primary
abacus context, constraining exercises to the archetype's scored pool.

Usage:
  python scripts/rebuild-cards.py                       # rebuild all 1,680
  python scripts/rebuild-cards.py --deck 13             # one deck
  python scripts/rebuild-cards.py --color 🟠             # one Color across all decks
  python scripts/rebuild-cards.py --min-score 80        # only cards below 80
  python scripts/rebuild-cards.py --dry-run             # preview without writing
  python scripts/rebuild-cards.py --force               # rebuild all including high-scoring
  python scripts/rebuild-cards.py --abacus general-strength  # rebuild one abacus (48 zips)
  python scripts/rebuild-cards.py --all-abaci           # rebuild all 1,680 via abacus context
  python scripts/rebuild-cards.py --dlc                 # rebuild 89 DLC free-agent zips
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# Import template infrastructure from batch-generate-deck
from pathlib import Path as _P

# We shell out to exercise_selector and import functions via direct exec
# to avoid circular import issues with batch-generate-deck.py's module name

VALIDATOR = ROOT / "scripts" / "validate-card.py"
AUDITOR = ROOT / "scripts" / "audit-deck-quality.py"
BATCH_GEN = ROOT / "scripts" / "batch-generate-deck.py"
SELECTOR = ROOT / "scripts" / "middle-math" / "exercise_selector.py"
ZIP_REGISTRY = ROOT / "middle-math" / "zip-registry.json"
EXERCISE_LIBRARY = ROOT / "exercise-library.md"
ABACUS_REGISTRY = ROOT / "middle-math" / "abacus-registry.json"
ABACUS_PROFILES_DIR = ROOT / "middle-math" / "abacus-profiles"
EXERCISE_REGISTRY = ROOT / "middle-math" / "exercise-registry.json"

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']
TYPE_EMOJI = {"Push": "🛒", "Pull": "🪡", "Legs": "🍗", "Plus": "➕", "Ultra": "➖"}
NO_BARBELL = {"🟢", "🟠"}


def parse_frontmatter(content: str) -> tuple[dict[str, str] | None, str]:
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, content
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    if end_idx is None:
        return None, content
    fm: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    body = '\n'.join(lines[end_idx + 1:])
    return fm, body


def parse_zip(zip_str: str) -> tuple[str, ...] | None:
    s = zip_str.strip()
    result = []
    for emoji_set in [ORDERS, AXES, TYPES, COLORS]:
        matched = False
        for emoji in emoji_set:
            if s.startswith(emoji):
                result.append(emoji)
                s = s[len(emoji):]
                matched = True
                break
        if not matched:
            return None
    return tuple(result) if not s.strip() else None


def load_zip_registry() -> dict[str, Any]:
    rows = json.loads(ZIP_REGISTRY.read_text(encoding="utf-8"))
    return {row["emoji_zip"]: row for row in rows}


def parse_deck_identity(deck: int) -> dict[str, dict]:
    path = ROOT / "deck-identities" / f"deck-{deck:02d}-identity.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    entries = {}
    line_re = re.compile(r"^-\s*(\S+)\s*—\s*(.+?);\s*primary exercise:\s*(.+?)\.?\s*$")
    for line in text.splitlines():
        m = line_re.match(line.strip())
        if m:
            zip_code, desc, exercise = m.groups()
            entries[zip_code] = {"description": desc.strip(), "primary_exercise": exercise.strip()}
    return entries


def selector_candidates(zip_code: str, top: int = 5) -> list[str]:
    cmd = ["python", str(SELECTOR), "--zip", zip_code, "--top", str(top), "--output", "json"]
    try:
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=30)
        if result.returncode != 0:
            return []
        text = result.stdout
        start = text.find("{")
        if start == -1:
            return []
        data = json.loads(text[start:])
        names = []
        for block in data.get("blocks", []):
            for candidate in block.get("candidates", []):
                name = candidate.get("name")
                if name and name not in names:
                    names.append(name)
                if len(names) >= top:
                    return names
        return names
    except Exception:
        return []


def audit_card_score(card_path: str) -> dict | None:
    """Run audit-deck-quality.py on a single card, return scores."""
    cmd = ["python", str(AUDITOR), card_path, "--format", "json"]
    try:
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=30)
        if result.returncode != 0:
            return None
        data = json.loads(result.stdout)
        cards = data.get("cards", [])
        if cards:
            return cards[0].get("scores", {})
    except Exception:
        pass
    return None


def load_batch_gen_module():
    """Load batch-generate-deck.py as a module for access to fallback_template."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("batch_gen", str(BATCH_GEN))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["batch_gen"] = mod
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Abacus infrastructure
# ---------------------------------------------------------------------------

# Numeric zip ↔ emoji zip conversion helpers
ORDER_EMOJIS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXIS_EMOJIS = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPE_EMOJIS_LIST = ['🛒', '🪡', '🍗', '➕', '➖']
COLOR_EMOJIS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']


def numeric_to_emoji(nzip: str) -> str:
    """Convert numeric zip like '2123' to emoji zip like '⛽🏛🪡🔵'."""
    if len(nzip) != 4:
        return ""
    try:
        o, a, t, c = int(nzip[0]), int(nzip[1]), int(nzip[2]), int(nzip[3])
        return ORDER_EMOJIS[o - 1] + AXIS_EMOJIS[a - 1] + TYPE_EMOJIS_LIST[t - 1] + COLOR_EMOJIS[c - 1]
    except (ValueError, IndexError):
        return ""


def load_abacus_registry() -> dict:
    """Load the abacus registry JSON."""
    if not ABACUS_REGISTRY.exists():
        return {"abaci": [], "dlc_packs": []}
    return json.loads(ABACUS_REGISTRY.read_text(encoding="utf-8"))


def load_abacus_profile(slug: str) -> dict | None:
    """Load a single abacus profile by slug."""
    path = ABACUS_PROFILES_DIR / f"{slug}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def load_exercise_registry() -> dict[str, dict]:
    """Load exercise registry keyed by exercise_id."""
    if not EXERCISE_REGISTRY.exists():
        return {}
    data = json.loads(EXERCISE_REGISTRY.read_text(encoding="utf-8"))
    return {ex["exercise_id"]: ex for ex in data}


def build_zip_to_abacus_map(abacus_reg: dict) -> dict[str, str]:
    """Build emoji_zip → primary abacus slug lookup.

    Priority: working slot in first abacus wins.
    If zip only appears as bonus, use first bonus appearance.
    """
    zip_map: dict[str, str] = {}

    # First pass: working slots (highest priority)
    for ab in abacus_reg.get("abaci", []):
        slug = ab["slug"]
        for nzip in ab.get("working_zips", []):
            ezip = numeric_to_emoji(nzip)
            if ezip and ezip not in zip_map:
                zip_map[ezip] = slug

    # Second pass: bonus slots (only if not already assigned)
    for ab in abacus_reg.get("abaci", []):
        slug = ab["slug"]
        for bonus in ab.get("bonus_zips", []):
            nzip = bonus["zip"]
            ezip = numeric_to_emoji(nzip)
            if ezip and ezip not in zip_map:
                zip_map[ezip] = slug

    return zip_map


def build_dlc_zip_map(abacus_reg: dict) -> dict[str, dict]:
    """Build emoji_zip → DLC pack info for free-agent zips."""
    dlc_map: dict[str, dict] = {}
    for pack in abacus_reg.get("dlc_packs", []):
        for nzip in pack.get("zips", []):
            ezip = numeric_to_emoji(nzip)
            if ezip:
                dlc_map[ezip] = {
                    "pack_id": pack["id"],
                    "pack_name": pack["name"],
                    "pack_slug": pack["slug"],
                    "theme": pack.get("theme", {}),
                }
    return dlc_map


def get_abacus_exercises(profile: dict, type_name: str, ex_registry: dict[str, dict],
                         top: int = 10) -> list[str]:
    """Get top exercises from abacus profile for a given Type, resolved to names."""
    pool = profile.get("exercise_pool", {})
    top_scored = pool.get("top_scored", {})

    # Use pre-scored top list if available
    scored = top_scored.get(type_name, [])
    if scored:
        return [e["name"] for e in scored[:top]]

    # Fallback to ID list
    ids = pool.get("by_type", {}).get(type_name, [])
    names = []
    for eid in ids[:top]:
        ex = ex_registry.get(eid)
        if ex:
            names.append(ex["name"])
    return names


def collect_abacus_cards(slug: str, abacus_reg: dict) -> list[Path]:
    """Collect card files for all zips in a specific abacus."""
    # Find the abacus
    abacus = None
    for ab in abacus_reg.get("abaci", []):
        if ab["slug"] == slug:
            abacus = ab
            break
    if not abacus:
        return []

    # Get all emoji zips
    target_zips = set()
    for nzip in abacus.get("working_zips", []):
        ezip = numeric_to_emoji(nzip)
        if ezip:
            target_zips.add(ezip)
    for bonus in abacus.get("bonus_zips", []):
        ezip = numeric_to_emoji(bonus["zip"])
        if ezip:
            target_zips.add(ezip)

    return _find_cards_by_zip(target_zips)


def collect_dlc_cards(abacus_reg: dict) -> list[Path]:
    """Collect card files for all DLC free-agent zips."""
    target_zips = set()
    for pack in abacus_reg.get("dlc_packs", []):
        for nzip in pack.get("zips", []):
            ezip = numeric_to_emoji(nzip)
            if ezip:
                target_zips.add(ezip)
    return _find_cards_by_zip(target_zips)


def _find_cards_by_zip(target_zips: set[str]) -> list[Path]:
    """Find card files matching a set of emoji zip codes."""
    cards = []
    for dirpath, _, filenames in os.walk(ROOT / "cards"):
        for fname in sorted(filenames):
            if not fname.endswith('.md') or fname in ('AGENTS.md', 'README.md'):
                continue
            path = Path(dirpath) / fname
            content = path.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(content)
            if fm is None:
                continue
            status = fm.get("status", "").strip()
            if status in ("EMPTY", "CANONICAL"):
                continue
            zip_code = fm.get("zip", "").strip()
            if zip_code in target_zips:
                cards.append(path)
    return cards


def collect_cards(deck: int | None, color: str | None) -> list[Path]:
    """Collect all .md card files, optionally filtered by deck or color."""
    cards = []
    for dirpath, _, filenames in os.walk(ROOT / "cards"):
        for fname in sorted(filenames):
            if not fname.endswith('.md') or fname in ('AGENTS.md', 'README.md'):
                continue
            path = Path(dirpath) / fname
            content = path.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(content)
            if fm is None:
                continue
            status = fm.get("status", "").strip()
            if status in ("EMPTY", "CANONICAL"):
                continue
            if deck is not None:
                card_deck = fm.get("deck", "").strip()
                try:
                    if int(card_deck) != deck:
                        continue
                except (ValueError, TypeError):
                    continue
            if color is not None:
                zip_str = fm.get("zip", "").strip()
                parsed = parse_zip(zip_str)
                if parsed and parsed[3] != color:
                    continue
            cards.append(path)
    return cards


def rebuild_card(card_path: Path, batch_mod: Any, registry: dict, identities: dict,
                 lib_text: str, dry_run: bool,
                 abacus_profile: dict | None = None,
                 ex_registry: dict[str, dict] | None = None) -> dict:
    """Rebuild a single card. Returns result dict.

    If abacus_profile is provided, exercises are selected from the abacus's
    scored pool instead of the generic exercise selector.
    """
    content = card_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    if fm is None:
        return {"path": str(card_path), "status": "skip", "reason": "no frontmatter"}

    zip_code = fm.get("zip", "").strip()
    parsed = parse_zip(zip_code)
    if parsed is None:
        return {"path": str(card_path), "status": "skip", "reason": "bad zip"}

    order_e, axis_e, type_e, color_e = parsed
    deck_str = fm.get("deck", "0").strip()
    try:
        deck_num = int(deck_str)
    except ValueError:
        deck_num = 0

    # Look up metadata
    meta = registry.get(zip_code)
    if not meta:
        return {"path": str(card_path), "status": "skip", "reason": "not in registry"}

    type_name = meta["type"]["name"]

    # --- Exercise selection: abacus-aware or legacy ---
    if abacus_profile and ex_registry:
        # Abacus-aware: use pre-scored pool from profile
        abacus_exercises = get_abacus_exercises(abacus_profile, type_name, ex_registry, top=10)

        # Filter for barbell and GOLD rules
        if color_e in NO_BARBELL:
            abacus_exercises = [e for e in abacus_exercises if not batch_mod._has_barbell(e)]

        # GOLD gate: if not 🔴/🟣, remove GOLD exercises
        if color_e not in batch_mod.GOLD_COLORS:
            gold_ids = set(abacus_profile.get("exercise_pool", {}).get("gold_exercises", []))
            gold_names = set()
            for eid in gold_ids:
                ex = ex_registry.get(eid)
                if ex:
                    gold_names.add(ex["name"])
            abacus_exercises = [e for e in abacus_exercises if e not in gold_names]

        # Type filter
        abacus_exercises = batch_mod._filter_exercises_for_type(abacus_exercises, type_name)

        primary = abacus_exercises[0] if abacus_exercises else None
        supplemental = abacus_exercises[1:6] if len(abacus_exercises) > 1 else []
    else:
        # Legacy path: deck identity + exercise selector
        primary = None
        supplemental = []

    # Fallback: get primary from deck identity if abacus didn't provide one
    if not primary:
        deck_ident = identities.get(deck_num, {})
        entry = deck_ident.get(zip_code, {})
        primary = entry.get("primary_exercise", "")

    if not primary:
        # Fallback: extract from existing card title
        for line in body.split('\n'):
            if line.strip().startswith('# '):
                parts = line.replace('#', '').strip().split('—')
                if parts:
                    for t_emoji in TYPES:
                        parts[0] = parts[0].replace(t_emoji, '')
                    primary = parts[0].strip()
                    break

    if not primary:
        return {"path": str(card_path), "status": "skip", "reason": "no primary exercise"}

    # Get supplemental candidates (if not already from abacus)
    if not supplemental:
        supplemental = selector_candidates(zip_code, top=5)
        supplemental = batch_mod._filter_exercises_for_type(supplemental, type_name)
        if color_e in NO_BARBELL:
            supplemental = batch_mod._filter_no_barbell(supplemental)

    # Final barbell check on primary
    if color_e in NO_BARBELL and batch_mod._has_barbell(primary):
        if supplemental:
            primary = supplemental.pop(0)

    # Get deck identity description
    deck_ident = identities.get(deck_num, {})
    entry = deck_ident.get(zip_code, {})

    # Build context
    context = {
        "zip": zip_code,
        "operator": fm.get("operator", meta["operator"]["emoji"] + " " + meta["operator"]["name"]),
        "identity_line": entry.get("description", ""),
        "primary_exercise": primary,
        "supplemental": supplemental,
        "order_emoji": meta["order"]["emoji"],
        "order_name": meta["order"]["name"],
        "axis_emoji": meta["axis"]["emoji"],
        "axis_name": meta["axis"]["name"],
        "type_emoji": TYPE_EMOJI.get(meta["type"]["name"], "🛒"),
        "type_name": meta["type"]["name"],
        "color_emoji": meta["color"]["emoji"],
        "color_name": meta["color"]["name"],
        "order_ceiling": batch_mod.ORDER_CEILINGS[meta["order"]["emoji"]],
        "color_tier": batch_mod.COLOR_TIERS[meta["color"]["emoji"]],
        "gold_allowed": meta["color"]["emoji"] in batch_mod.GOLD_COLORS,
        "no_barbell": meta["color"]["emoji"] in batch_mod.NO_BARBELL,
        "stub_file": card_path,
        "exercise_content": None,
    }

    # Inject abacus context if available
    if abacus_profile:
        color_postures = abacus_profile.get("color_postures", {})
        context["abacus_name"] = abacus_profile.get("name", "")
        context["abacus_domain"] = abacus_profile.get("domain", "")
        context["abacus_identity"] = abacus_profile.get("identity_statement", "")
        context["abacus_color_posture"] = color_postures.get(color_e, "")
        context["abacus_block_preferences"] = abacus_profile.get("block_preferences", {})

    # Generate new body
    new_body = batch_mod.fallback_template(context)

    # Compose new card content (preserve original frontmatter keys)
    updated_fm = dict(fm)
    updated_fm["status"] = "GENERATED"
    fm_lines = ["---"] + [f"{k}: {v}" for k, v in updated_fm.items()] + ["---", ""]
    new_content = "\n".join(fm_lines) + new_body.strip() + "\n"

    if dry_run:
        result = {
            "path": str(card_path),
            "zip": zip_code,
            "status": "would_rebuild",
            "primary": primary,
            "color": meta["color"]["name"],
        }
        if abacus_profile:
            result["abacus"] = abacus_profile.get("slug", "")
        return result

    # Save original for potential revert
    original_content = content

    # Write new content
    card_path.write_text(new_content, encoding="utf-8")

    # Validate
    val_result = subprocess.run(
        ["python", str(VALIDATOR), str(card_path)],
        cwd=ROOT, text=True, capture_output=True
    )
    if val_result.returncode != 0:
        # Revert on validation failure
        card_path.write_text(original_content, encoding="utf-8")
        return {
            "path": str(card_path),
            "zip": zip_code,
            "status": "revert",
            "reason": val_result.stdout.strip()[:200],
        }

    result = {
        "path": str(card_path),
        "zip": zip_code,
        "status": "rebuilt",
        "primary": primary,
        "color": meta["color"]["name"],
    }
    if abacus_profile:
        result["abacus"] = abacus_profile.get("slug", "")
    return result


def main():
    parser = argparse.ArgumentParser(description="PPL± Card Rebuild Orchestrator")
    parser.add_argument("--deck", type=int, help="Only rebuild cards in this deck number")
    parser.add_argument("--color", help="Only rebuild cards with this Color emoji (e.g., 🟠)")
    parser.add_argument("--min-score", type=int, default=100,
                        help="Only rebuild cards currently scoring below this threshold (default: 100 = all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--force", action="store_true", help="Rebuild all cards regardless of score")
    # Abacus modes
    parser.add_argument("--abacus", help="Rebuild all zips in one abacus (by slug, e.g., general-strength)")
    parser.add_argument("--all-abaci", action="store_true",
                        help="Rebuild all 1,680 zips using each zip's primary abacus context")
    parser.add_argument("--dlc", action="store_true",
                        help="Rebuild the 89 DLC free-agent zips")
    args = parser.parse_args()

    if args.force:
        args.min_score = 101  # Everything is below 101

    # Determine mode
    abacus_mode = args.abacus or args.all_abaci or args.dlc

    print("Loading infrastructure...")
    batch_mod = load_batch_gen_module()
    registry = load_zip_registry()
    lib_text = EXERCISE_LIBRARY.read_text(encoding="utf-8")

    # Load all deck identities
    identities = {}
    for deck_num in range(1, 43):
        identities[deck_num] = parse_deck_identity(deck_num)

    # Load abacus infrastructure if needed
    abacus_reg = None
    zip_to_abacus = None
    dlc_zip_map = None
    ex_registry = None

    if abacus_mode:
        print("Loading abacus infrastructure...")
        abacus_reg = load_abacus_registry()
        zip_to_abacus = build_zip_to_abacus_map(abacus_reg)
        dlc_zip_map = build_dlc_zip_map(abacus_reg)
        ex_registry = load_exercise_registry()
        print(f"  {len(zip_to_abacus)} zips mapped to abaci")
        print(f"  {len(dlc_zip_map)} DLC free-agent zips")

    # Collect cards based on mode
    if args.abacus:
        # Single abacus mode
        cards = collect_abacus_cards(args.abacus, abacus_reg)
        print(f"Found {len(cards)} cards in abacus '{args.abacus}'")
    elif args.all_abaci or args.dlc:
        # All abaci or DLC — collect everything
        if args.dlc:
            cards = collect_dlc_cards(abacus_reg)
            print(f"Found {len(cards)} DLC free-agent cards")
        else:
            cards = collect_cards(None, None)
            print(f"Found {len(cards)} cards for full abacus rebuild")
    else:
        cards = collect_cards(args.deck, args.color)
        print(f"Found {len(cards)} cards to process")

    if not cards:
        print("No cards to rebuild.")
        return

    # Profile cache for abacus mode
    profile_cache: dict[str, dict | None] = {}

    results = []
    rebuilt = 0
    skipped = 0
    reverted = 0

    for i, card_path in enumerate(cards):
        # Resolve abacus profile for this card
        abacus_profile = None
        if abacus_mode:
            # Read the card's zip to determine its abacus
            card_content = card_path.read_text(encoding="utf-8")
            card_fm, _ = parse_frontmatter(card_content)
            card_zip = card_fm.get("zip", "").strip() if card_fm else ""

            if args.abacus:
                slug = args.abacus
            elif args.dlc:
                # DLC zips: use DLC pack context (no profile, just legacy)
                slug = None
            else:
                slug = zip_to_abacus.get(card_zip)

            if slug:
                if slug not in profile_cache:
                    profile_cache[slug] = load_abacus_profile(slug)
                abacus_profile = profile_cache[slug]

        result = rebuild_card(
            card_path, batch_mod, registry, identities, lib_text, args.dry_run,
            abacus_profile=abacus_profile,
            ex_registry=ex_registry,
        )
        results.append(result)

        status = result["status"]
        if status in ("rebuilt", "would_rebuild"):
            rebuilt += 1
        elif status == "revert":
            reverted += 1
        else:
            skipped += 1

        # Progress every 100 cards
        if (i + 1) % 100 == 0 or i == len(cards) - 1:
            print(f"  [{i + 1}/{len(cards)}] rebuilt={rebuilt} skipped={skipped} reverted={reverted}")

    # Summary
    print()
    mode_label = ""
    if args.abacus:
        mode_label = f" [abacus: {args.abacus}]"
    elif args.all_abaci:
        mode_label = " [all-abaci]"
    elif args.dlc:
        mode_label = " [DLC]"

    print(f"{'DRY RUN ' if args.dry_run else ''}Rebuild{mode_label} complete:")
    print(f"  Processed: {len(cards)}")
    print(f"  Rebuilt:   {rebuilt}")
    print(f"  Skipped:   {skipped}")
    print(f"  Reverted:  {reverted}")

    # Write report
    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)
    suffix = ""
    if args.abacus:
        suffix = f"-abacus-{args.abacus}"
    elif args.all_abaci:
        suffix = "-all-abaci"
    elif args.dlc:
        suffix = "-dlc"
    report_path = report_dir / f"rebuild{suffix}-{date.today().isoformat()}.json"
    report = {
        "date": date.today().isoformat(),
        "dry_run": args.dry_run,
        "mode": "abacus" if abacus_mode else "legacy",
        "abacus_slug": args.abacus,
        "cards_processed": len(cards),
        "cards_rebuilt": rebuilt,
        "cards_skipped": skipped,
        "cards_reverted": reverted,
        "filters": {
            "deck": args.deck,
            "color": args.color,
            "min_score": args.min_score,
            "abacus": args.abacus,
            "all_abaci": args.all_abaci,
            "dlc": args.dlc,
        },
        "results": results,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nReport: {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
