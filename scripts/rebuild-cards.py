#!/usr/bin/env python3
"""rebuild-cards.py — PPL± Card Rebuild Orchestrator

Reads existing GENERATED cards, regenerates content using the upgraded
fallback template in batch-generate-deck.py, overwrites in-place (content only,
filenames preserved), validates, and reports before/after quality scores.

Usage:
  python scripts/rebuild-cards.py                       # rebuild all 1,680
  python scripts/rebuild-cards.py --deck 13             # one deck
  python scripts/rebuild-cards.py --color 🟠             # one Color across all decks
  python scripts/rebuild-cards.py --min-score 80        # only cards below 80
  python scripts/rebuild-cards.py --dry-run             # preview without writing
  python scripts/rebuild-cards.py --force               # rebuild all including high-scoring
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
                 lib_text: str, dry_run: bool) -> dict:
    """Rebuild a single card. Returns result dict."""
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

    # Get primary exercise from deck identity
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

    # Get supplemental candidates
    supplemental = selector_candidates(zip_code, top=5)

    # Filter for Type accuracy and barbell rules
    type_name = meta["type"]["name"]
    supplemental = batch_mod._filter_exercises_for_type(supplemental, type_name)
    if color_e in NO_BARBELL:
        supplemental = batch_mod._filter_no_barbell(supplemental)
        if batch_mod._has_barbell(primary):
            # Substitute primary with first non-barbell candidate
            if supplemental:
                primary = supplemental.pop(0)

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

    # Generate new body
    new_body = batch_mod.fallback_template(context)

    # Compose new card content (preserve original frontmatter keys)
    updated_fm = dict(fm)
    updated_fm["status"] = "GENERATED"
    fm_lines = ["---"] + [f"{k}: {v}" for k, v in updated_fm.items()] + ["---", ""]
    new_content = "\n".join(fm_lines) + new_body.strip() + "\n"

    if dry_run:
        return {
            "path": str(card_path),
            "zip": zip_code,
            "status": "would_rebuild",
            "primary": primary,
            "color": meta["color"]["name"],
        }

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

    return {
        "path": str(card_path),
        "zip": zip_code,
        "status": "rebuilt",
        "primary": primary,
        "color": meta["color"]["name"],
    }


def main():
    parser = argparse.ArgumentParser(description="PPL± Card Rebuild Orchestrator")
    parser.add_argument("--deck", type=int, help="Only rebuild cards in this deck number")
    parser.add_argument("--color", help="Only rebuild cards with this Color emoji (e.g., 🟠)")
    parser.add_argument("--min-score", type=int, default=100,
                        help="Only rebuild cards currently scoring below this threshold (default: 100 = all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--force", action="store_true", help="Rebuild all cards regardless of score")
    args = parser.parse_args()

    if args.force:
        args.min_score = 101  # Everything is below 101

    print("Loading infrastructure...")
    batch_mod = load_batch_gen_module()
    registry = load_zip_registry()
    lib_text = EXERCISE_LIBRARY.read_text(encoding="utf-8")

    # Load all deck identities
    identities = {}
    for deck_num in range(1, 43):
        identities[deck_num] = parse_deck_identity(deck_num)

    # Collect cards
    cards = collect_cards(args.deck, args.color)
    print(f"Found {len(cards)} cards to process")

    if not cards:
        print("No cards to rebuild.")
        return

    results = []
    rebuilt = 0
    skipped = 0
    reverted = 0

    for i, card_path in enumerate(cards):
        result = rebuild_card(card_path, batch_mod, registry, identities, lib_text, args.dry_run)
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
    print(f"{'DRY RUN ' if args.dry_run else ''}Rebuild complete:")
    print(f"  Processed: {len(cards)}")
    print(f"  Rebuilt:   {rebuilt}")
    print(f"  Skipped:   {skipped}")
    print(f"  Reverted:  {reverted}")

    # Write report
    report_dir = ROOT / "reports"
    report_dir.mkdir(exist_ok=True)
    report_path = report_dir / f"rebuild-{date.today().isoformat()}.json"
    report = {
        "date": date.today().isoformat(),
        "dry_run": args.dry_run,
        "cards_processed": len(cards),
        "cards_rebuilt": rebuilt,
        "cards_skipped": skipped,
        "cards_reverted": reverted,
        "filters": {
            "deck": args.deck,
            "color": args.color,
            "min_score": args.min_score,
        },
        "results": results,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nReport: {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
