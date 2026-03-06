#!/usr/bin/env python3
"""
scripts/middle-math/exercise_selector.py
CX-15: Exercise Selection Prototype

Produces ranked exercise candidates per block for any zip code in the PPL±
1,680-room library. This is the core of the generation automation pipeline.

Algorithm:
  1. Parse input zip (emoji or numeric) → zip-registry.json
  2. Load zip's 61-dim weight vector from weight-vectors.json
  3. Determine block sequence from Order (per CLAUDE.md guidelines)
  4. For each block:
     a. Filter exercises by Type match
     b. Filter by Color equipment tier range
     c. Apply GOLD gate (only 🔴 pos=5, 🟣 pos=4 allow GOLD exercises)
     d. Apply Order relevance filter
     e. Score candidates via dot product against zip weight vector
     f. Rank top 3–5 candidates
  5. Deduplicate: no exercise appears in more than one block per zip
  6. Output JSON manifest

Usage:
    python scripts/middle-math/exercise_selector.py --zip ⛽🏛🪡🔵
    python scripts/middle-math/exercise_selector.py --zip 2123
    python scripts/middle-math/exercise_selector.py --deck 07
    python scripts/middle-math/exercise_selector.py --zip 2123 --validate
    python scripts/middle-math/exercise_selector.py --zip 2123 --stats
    python scripts/middle-math/exercise_selector.py --deck 07 --output json
    python scripts/middle-math/exercise_selector.py --deck 07 --output text
"""

import json
import sys
import argparse
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH    = REPO_ROOT / "middle-math" / "zip-registry.json"
VECTORS_PATH     = REPO_ROOT / "middle-math" / "weight-vectors.json"
EXERCISES_PATH   = REPO_ROOT / "middle-math" / "exercise-library.json"

# ---------------------------------------------------------------------------
# 61-emoji position map (mirrors weight_vector.py — the authoritative source)
# Positions 0–6:   Orders
# Positions 7–12:  Axes
# Positions 13–17: Types
# Positions 18–25: Colors
# Positions 26–48: Blocks (22 blocks + 🧮 SAVE = 23 slots)
# Positions 49–60: Operators (12 operators)
# ---------------------------------------------------------------------------
EMOJI_POSITIONS = {
    # Orders (7)
    "🐂": 0, "⛽": 1, "🦋": 2, "🏟": 3, "🌾": 4, "⚖": 5, "🖼": 6,
    # Axes (6)
    "🏛": 7, "🔨": 8, "🌹": 9, "🪐": 10, "⌛": 11, "🐬": 12,
    # Types (5)
    "🛒": 13, "🪡": 14, "🍗": 15, "➕": 16, "➖": 17,
    # Colors (8)
    "⚫": 18, "🟢": 19, "🔵": 20, "🟣": 21, "🔴": 22, "🟠": 23, "🟡": 24, "⚪": 25,
    # Blocks (22 + SAVE = 23)
    "♨️": 26, "🎯": 27, "🔢": 28, "🧈": 29, "🫀": 30, "▶️": 31, "🎼": 32,
    "♟️": 33, "🪜": 34, "🌎": 35, "🎱": 36, "🌋": 37, "🪞": 38, "🗿": 39,
    "🛠": 40, "🧩": 41, "🪫": 42, "🏖": 43, "🏗": 44, "🧬": 45, "🚂": 46,
    "🔠": 47, "🧮": 48,
    # Operators (12)
    "🧲": 49, "🐋": 50, "🤌": 51, "🧸": 52, "✒️": 53, "🦉": 54,
    "🥨": 55, "🦢": 56, "📍": 57, "👀": 58, "🪵": 59, "🚀": 60,
}

POSITION_EMOJIS = {v: k for k, v in EMOJI_POSITIONS.items()}
VECTOR_SIZE = 61

# Sort emojis by length descending so longer sequences match before shorter ones
EMOJIS_SORTED = sorted(EMOJI_POSITIONS.keys(), key=len, reverse=True)

# ---------------------------------------------------------------------------
# SCL name → emoji maps (for looking up exercise library strings)
# ---------------------------------------------------------------------------
ORDER_NAME_TO_EMOJI = {
    "Foundation": "🐂", "Strength": "⛽", "Hypertrophy": "🦋",
    "Performance": "🏟", "Full Body": "🌾", "Balance": "⚖", "Restoration": "🖼",
}
AXIS_NAME_TO_EMOJI = {
    "Basics": "🏛", "Functional": "🔨", "Aesthetic": "🌹",
    "Challenge": "🪐", "Time": "⌛", "Partner": "🐬",
}
TYPE_NAME_TO_EMOJI = {
    "Push": "🛒", "Pull": "🪡", "Legs": "🍗", "Plus": "➕", "Ultra": "➖",
}
ORDER_EMOJI_TO_NAME = {v: k for k, v in ORDER_NAME_TO_EMOJI.items()}
AXIS_EMOJI_TO_NAME  = {v: k for k, v in AXIS_NAME_TO_EMOJI.items()}
TYPE_EMOJI_TO_NAME  = {v: k for k, v in TYPE_NAME_TO_EMOJI.items()}

# ---------------------------------------------------------------------------
# Color equipment tier ranges (from CLAUDE.md / color-weights.md)
# ⚫ Teaching: 2–3 | 🟢 Bodyweight: 0–2 | 🔵 Structured: 2–3 | 🟣 Technical: 2–5
# 🔴 Intense: 2–4  | 🟠 Circuit: 0–3    | 🟡 Fun: 0–5        | ⚪ Mindful: 0–3
# ---------------------------------------------------------------------------
COLOR_TIER_RANGES = {
    "⚫": (2, 3),
    "🟢": (0, 2),
    "🔵": (2, 3),
    "🟣": (2, 5),
    "🔴": (2, 4),
    "🟠": (0, 3),
    "🟡": (0, 5),
    "⚪": (0, 3),
}

# Colors that unlock GOLD exercises (position 4 = 🟣, position 5 = 🔴)
GOLD_ELIGIBLE_COLORS = {"🟣", "🔴"}

# ---------------------------------------------------------------------------
# Block sequences per Order (from CLAUDE.md)
# Only blocks that need exercise candidates are included
# (♨️ Warm-Up, 🚂 Junction, 🧮 SAVE are structural — no exercise selection needed)
# ---------------------------------------------------------------------------
BLOCK_SEQUENCES = {
    # Order emoji → [blocks that need exercise candidates]
    "🐂": ["♨️", "🔢", "🧈", "🧩", "🧬", "🚂"],
    "⛽": ["♨️", "▶️", "🧈", "🧩", "🪫", "🚂"],
    "🦋": ["♨️", "▶️", "🧈", "🗿", "🪞", "🧩", "🪫", "🚂"],
    "🏟": ["♨️", "🪜", "🧈", "🚂"],
    "🌾": ["♨️", "🎼", "🧈", "🧩", "🪫", "🚂"],
    "⚖": ["♨️", "🏗", "🧈", "🧩", "🪫", "🚂"],
    "🖼": ["🎯", "🪫", "🧈", "🧬", "🚂"],
}

# Blocks that are structural / don't need direct exercise selection
STRUCTURAL_BLOCKS = {"♨️", "🚂", "🧮", "🎯"}

# Block names for display
BLOCK_NAMES = {
    "♨️": "Warm-Up", "🎯": "Intention", "🔢": "Fundamentals", "🧈": "Bread/Butter",
    "🫀": "Circulation", "▶️": "Primer", "🎼": "Composition", "♟️": "Gambit",
    "🪜": "Progression", "🌎": "Exposure", "🎱": "ARAM", "🌋": "Gutter",
    "🪞": "Vanity", "🗿": "Sculpt", "🛠": "Craft", "🧩": "Supplemental",
    "🪫": "Release", "🏖": "Sandbox", "🏗": "Reformance", "🧬": "Imprint",
    "🚂": "Junction", "🔠": "Choice", "🧮": "SAVE",
}

# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_registry() -> list:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_vectors() -> dict:
    return json.loads(VECTORS_PATH.read_text(encoding="utf-8"))


def load_exercises() -> list:
    return json.loads(EXERCISES_PATH.read_text(encoding="utf-8"))


def build_registry_lookup(registry: list) -> dict:
    """Build lookup dicts for fast zip resolution by both numeric and emoji key."""
    by_numeric = {}
    by_emoji   = {}
    for entry in registry:
        by_numeric[entry["numeric_zip"]] = entry
        by_emoji[entry["emoji_zip"]]     = entry
    return {"numeric": by_numeric, "emoji": by_emoji}


# ---------------------------------------------------------------------------
# Exercise affinity vector
# ---------------------------------------------------------------------------

def build_exercise_affinity(exercise: dict) -> list:
    """
    Build a 61-dim affinity vector for a single exercise.

    Positions get weight +2 if the exercise's type matches that Type emoji.
    Positions get weight +1 for each Order in order_relevance.
    Positions get weight +1 for each Axis in axis_emphasis.
    All other positions: 0.
    """
    vec = [0] * VECTOR_SIZE

    # Type affinity (strong signal, weight +2)
    for type_name in exercise.get("scl_types", []):
        type_emoji = TYPE_NAME_TO_EMOJI.get(type_name)
        if type_emoji and type_emoji in EMOJI_POSITIONS:
            vec[EMOJI_POSITIONS[type_emoji]] += 2

    # Order relevance (weight +1 each)
    for order_name in exercise.get("order_relevance", []):
        order_emoji = ORDER_NAME_TO_EMOJI.get(order_name)
        if order_emoji and order_emoji in EMOJI_POSITIONS:
            vec[EMOJI_POSITIONS[order_emoji]] += 1

    # Axis emphasis (weight +1 each)
    for axis_name in exercise.get("axis_emphasis", []):
        axis_emoji = AXIS_NAME_TO_EMOJI.get(axis_name)
        if axis_emoji and axis_emoji in EMOJI_POSITIONS:
            vec[EMOJI_POSITIONS[axis_emoji]] += 1

    return vec


def dot_product(a: list, b: list) -> float:
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Filtering logic
# ---------------------------------------------------------------------------

def passes_type_filter(exercise: dict, type_name: str) -> bool:
    return type_name in exercise.get("scl_types", [])


def passes_equipment_tier_filter(exercise: dict, color_emoji: str) -> bool:
    """Color tier range must overlap with exercise's equipment_tier [min, max]."""
    color_min, color_max = COLOR_TIER_RANGES.get(color_emoji, (0, 5))
    ex_min, ex_max = exercise.get("equipment_tier", [0, 5])
    # Overlap check: ranges intersect if max(mins) <= min(maxes)
    return max(color_min, ex_min) <= min(color_max, ex_max)


def passes_gold_gate(exercise: dict, color_emoji: str) -> bool:
    """GOLD-gated exercises only permitted when Color is 🔴 or 🟣."""
    if exercise.get("gold_gated", False):
        return color_emoji in GOLD_ELIGIBLE_COLORS
    return True


def passes_order_relevance(exercise: dict, order_name: str) -> bool:
    """Exercise must list this Order as relevant."""
    return order_name in exercise.get("order_relevance", [])


def passes_no_barbell_constraint(exercise: dict, color_emoji: str) -> bool:
    """🟢 Bodyweight and 🟠 Circuit: no barbell-only exercises (tier ≥ 3 minimum)."""
    if color_emoji in {"🟢", "🟠"}:
        ex_min = exercise.get("equipment_tier", [0, 5])[0]
        # If exercise requires tier ≥ 3 minimum, it needs barbell/rack — excluded
        if ex_min >= 3:
            return False
    return True


# ---------------------------------------------------------------------------
# Core selection for a single block
# ---------------------------------------------------------------------------

def select_for_block(
    block_emoji: str,
    zip_entry: dict,
    zip_vector: list,
    exercises: list,
    already_selected: set,
    top_n: int = 5,
) -> dict:
    """
    Select top_n exercise candidates for a given block within a zip code.

    Returns:
        {
          "block": block_emoji,
          "block_name": str,
          "candidates": [{"id", "name", "score", "section", "muscle_groups", "filters_passed"}],
          "stats": {"considered", "filtered_type", "filtered_tier", "filtered_gold",
                    "filtered_order", "filtered_barbell", "filtered_duplicate", "scored"}
        }
    """
    order_emoji = zip_entry["order"]["emoji"]
    type_emoji  = zip_entry["type"]["emoji"]
    color_emoji = zip_entry["color"]["emoji"]
    order_name  = ORDER_EMOJI_TO_NAME.get(order_emoji, "")
    type_name   = TYPE_EMOJI_TO_NAME.get(type_emoji, "")

    stats = {
        "considered": 0,
        "filtered_type": 0,
        "filtered_tier": 0,
        "filtered_gold": 0,
        "filtered_order": 0,
        "filtered_barbell": 0,
        "filtered_duplicate": 0,
        "scored": 0,
    }

    scored = []

    for ex in exercises:
        stats["considered"] += 1

        if not passes_type_filter(ex, type_name):
            stats["filtered_type"] += 1
            continue

        if not passes_equipment_tier_filter(ex, color_emoji):
            stats["filtered_tier"] += 1
            continue

        if not passes_gold_gate(ex, color_emoji):
            stats["filtered_gold"] += 1
            continue

        if not passes_order_relevance(ex, order_name):
            stats["filtered_order"] += 1
            continue

        if not passes_no_barbell_constraint(ex, color_emoji):
            stats["filtered_barbell"] += 1
            continue

        if ex["id"] in already_selected:
            stats["filtered_duplicate"] += 1
            continue

        # Score: dot product of zip vector × exercise affinity vector
        affinity = build_exercise_affinity(ex)
        score = dot_product(zip_vector, affinity)

        stats["scored"] += 1
        scored.append((score, ex))

    # Sort descending by score
    scored.sort(key=lambda x: x[0], reverse=True)
    top = scored[:top_n]

    candidates = [
        {
            "id": ex["id"],
            "name": ex["name"],
            "score": round(score, 1),
            "section": ex.get("section", "?"),
            "muscle_groups": ex.get("muscle_groups", ""),
            "movement_pattern": ex.get("movement_pattern", ""),
            "equipment_tier": ex.get("equipment_tier", [0, 5]),
            "gold_gated": ex.get("gold_gated", False),
        }
        for score, ex in top
    ]

    return {
        "block": block_emoji,
        "block_name": BLOCK_NAMES.get(block_emoji, block_emoji),
        "candidates": candidates,
        "stats": stats,
    }


# ---------------------------------------------------------------------------
# Full zip selection
# ---------------------------------------------------------------------------

def select_for_zip(
    zip_entry: dict,
    zip_vector: list,
    exercises: list,
    top_n: int = 5,
) -> dict:
    """
    Run exercise selection for all blocks in a zip code.

    Returns a manifest dict: {zip, emoji_zip, blocks: [...], summary}
    """
    numeric_zip = zip_entry["numeric_zip"]
    emoji_zip   = zip_entry["emoji_zip"]
    order_emoji = zip_entry["order"]["emoji"]
    axis_emoji  = zip_entry["axis"]["emoji"]
    type_emoji  = zip_entry["type"]["emoji"]
    color_emoji = zip_entry["color"]["emoji"]

    block_sequence = BLOCK_SEQUENCES.get(order_emoji, ["♨️", "🧈", "🚂"])
    # Only select exercises for non-structural blocks
    selection_blocks = [b for b in block_sequence if b not in STRUCTURAL_BLOCKS]

    already_selected = set()
    block_results = []
    total_stats = {
        "considered": 0, "filtered_type": 0, "filtered_tier": 0,
        "filtered_gold": 0, "filtered_order": 0, "filtered_barbell": 0,
        "filtered_duplicate": 0, "scored": 0,
    }

    for block_emoji in selection_blocks:
        result = select_for_block(
            block_emoji, zip_entry, zip_vector, exercises,
            already_selected, top_n=top_n
        )
        block_results.append(result)

        # Register selected exercises to prevent cross-block duplicates
        for candidate in result["candidates"]:
            already_selected.add(candidate["id"])

        for k in total_stats:
            total_stats[k] += result["stats"].get(k, 0)

    # Coverage gaps: blocks with fewer than 3 candidates
    coverage_gaps = [
        {"block": r["block"], "block_name": r["block_name"], "candidates_found": len(r["candidates"])}
        for r in block_results
        if len(r["candidates"]) < 3
    ]

    return {
        "zip": numeric_zip,
        "emoji_zip": emoji_zip,
        "order": {"emoji": order_emoji, "name": zip_entry["order"]["name"]},
        "axis":  {"emoji": axis_emoji,  "name": zip_entry["axis"]["name"]},
        "type":  {"emoji": type_emoji,  "name": zip_entry["type"]["name"]},
        "color": {"emoji": color_emoji, "name": zip_entry["color"]["name"]},
        "gold_eligible": zip_entry.get("gold_eligible", False),
        "block_sequence": block_sequence,
        "blocks": block_results,
        "summary": {
            "total_stats": total_stats,
            "coverage_gaps": coverage_gaps,
        },
    }


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_manifest(manifest: dict) -> list:
    """
    Validate a single zip manifest for GOLD leakage and cross-block duplicates.

    Returns list of violation strings (empty = clean).
    """
    violations = []
    zip_code  = manifest["zip"]
    emoji_zip = manifest["emoji_zip"]
    color_e   = manifest["color"]["emoji"]
    is_gold   = color_e in GOLD_ELIGIBLE_COLORS

    seen_exercise_ids = {}

    for block_result in manifest["blocks"]:
        block_e    = block_result["block"]
        block_name = block_result["block_name"]

        for cand in block_result["candidates"]:
            ex_id   = cand["id"]
            ex_name = cand["name"]

            # GOLD gate check
            if cand.get("gold_gated", False) and not is_gold:
                violations.append(
                    f"[{zip_code} {emoji_zip}] GOLD exercise in non-GOLD color "
                    f"{color_e}: '{ex_name}' (id={ex_id}) in block {block_e} {block_name}"
                )

            # Cross-block duplicate check
            if ex_id in seen_exercise_ids:
                prev_block = seen_exercise_ids[ex_id]
                violations.append(
                    f"[{zip_code} {emoji_zip}] Duplicate exercise '{ex_name}' (id={ex_id}) "
                    f"in blocks {prev_block} and {block_e} {block_name}"
                )
            else:
                seen_exercise_ids[ex_id] = f"{block_e} {block_name}"

    return violations


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_text(manifest: dict) -> str:
    """Human-readable text output for a single zip manifest."""
    lines = []
    z = manifest
    lines.append(f"\n{'═' * 60}")
    lines.append(f"  {z['emoji_zip']}  ({z['zip']})")
    lines.append(f"  {z['order']['emoji']} {z['order']['name']} | "
                 f"{z['axis']['emoji']} {z['axis']['name']} | "
                 f"{z['type']['emoji']} {z['type']['name']} | "
                 f"{z['color']['emoji']} {z['color']['name']}")
    lines.append(f"  GOLD eligible: {'YES' if z['gold_eligible'] else 'no'}")
    lines.append(f"{'─' * 60}")

    for block in z["blocks"]:
        lines.append(f"\n  {block['block']} {block['block_name']}")
        if not block["candidates"]:
            lines.append("    (no candidates found)")
        for i, c in enumerate(block["candidates"], 1):
            tier = f"T{c['equipment_tier'][0]}-{c['equipment_tier'][1]}"
            gold = " [GOLD]" if c.get("gold_gated") else ""
            lines.append(f"    {i}. {c['name']}{gold}")
            lines.append(f"       score={c['score']:+.0f}  {tier}  {c['muscle_groups']}")

    gaps = z["summary"]["coverage_gaps"]
    if gaps:
        lines.append(f"\n  ⚠ Coverage gaps (<3 candidates):")
        for g in gaps:
            lines.append(f"    {g['block']} {g['block_name']}: {g['candidates_found']} found")

    return "\n".join(lines)


def format_stats(manifest: dict) -> str:
    """Stats summary for a single zip manifest."""
    lines = []
    z = manifest
    s = z["summary"]["total_stats"]
    lines.append(f"\n  {z['emoji_zip']} ({z['zip']}) stats:")
    lines.append(f"    Considered:         {s['considered']}")
    lines.append(f"    Filtered by type:   {s['filtered_type']}")
    lines.append(f"    Filtered by tier:   {s['filtered_tier']}")
    lines.append(f"    Filtered by GOLD:   {s['filtered_gold']}")
    lines.append(f"    Filtered by order:  {s['filtered_order']}")
    lines.append(f"    Filtered barbell:   {s['filtered_barbell']}")
    lines.append(f"    Filtered duplicate: {s['filtered_duplicate']}")
    lines.append(f"    Scored:             {s['scored']}")
    gaps = z["summary"]["coverage_gaps"]
    if gaps:
        lines.append(f"    ⚠ Coverage gaps: {len(gaps)} block(s)")
        for g in gaps:
            lines.append(f"      {g['block']} {g['block_name']}: {g['candidates_found']} candidates")
    else:
        lines.append(f"    ✓ All blocks have 3+ candidates")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Deck helpers
# ---------------------------------------------------------------------------

def get_deck_zips(registry: list, deck_number: int) -> list:
    """Return all zip entries for a given deck number."""
    return [e for e in registry if e.get("deck_number") == deck_number]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CX-15: PPL± Exercise Selection Prototype"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--zip",  type=str,
                       help="Single zip code (emoji or numeric, e.g. '⛽🏛🪡🔵' or '2123')")
    group.add_argument("--deck", type=str,
                       help="All 40 zips in a deck (e.g. '07' or '7')")

    parser.add_argument("--validate", action="store_true",
                        help="Check for GOLD leakage and cross-block duplicates")
    parser.add_argument("--stats", action="store_true",
                        help="Print filter/selection statistics")
    parser.add_argument("--output", choices=["json", "text"], default="text",
                        help="Output format (default: text)")
    parser.add_argument("--top", type=int, default=5,
                        help="Candidates per block (default: 5)")

    args = parser.parse_args()

    # Load data
    print("Loading data...", end=" ", flush=True)
    registry  = load_registry()
    vectors   = load_vectors()
    exercises = load_exercises()
    lookup    = build_registry_lookup(registry)
    print(f"done. {len(registry)} zips, {len(exercises)} exercises.")

    # Resolve zip(s)
    if args.zip:
        entry = lookup["numeric"].get(args.zip) or lookup["emoji"].get(args.zip)
        if not entry:
            print(f"Error: zip code not found: {args.zip}", file=sys.stderr)
            sys.exit(1)
        zip_entries = [entry]
    else:
        deck_num = int(args.deck)
        zip_entries = get_deck_zips(registry, deck_num)
        if not zip_entries:
            print(f"Error: no zip codes found for deck {deck_num}", file=sys.stderr)
            sys.exit(1)
        print(f"Deck {deck_num}: {len(zip_entries)} zip codes.")

    # Run selection
    manifests = []
    for zip_entry in zip_entries:
        numeric_zip = zip_entry["numeric_zip"]
        zip_vector  = vectors.get(numeric_zip, {}).get("vector", [0] * VECTOR_SIZE)
        manifest    = select_for_zip(zip_entry, zip_vector, exercises, top_n=args.top)
        manifests.append(manifest)

    # Validate
    if args.validate:
        all_violations = []
        for m in manifests:
            all_violations.extend(validate_manifest(m))
        if all_violations:
            print(f"\n--- VALIDATION FAILED: {len(all_violations)} violation(s) ---")
            for v in all_violations:
                print(f"  ✗ {v}")
            sys.exit(1)
        else:
            total_blocks = sum(len(m["blocks"]) for m in manifests)
            print(f"\n--- VALIDATION PASSED ---")
            print(f"  ✓ {len(manifests)} zip(s), {total_blocks} block(s) checked")
            print(f"  ✓ No GOLD exercises outside 🔴/🟣 colors")
            print(f"  ✓ No duplicate exercises across blocks within any zip")

    # Output
    if args.output == "json":
        output = manifests[0] if len(manifests) == 1 else manifests
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        for m in manifests:
            print(format_text(m))
            if args.stats:
                print(format_stats(m))

    # Deck-level stats summary
    if args.deck and args.stats:
        total_gaps = sum(len(m["summary"]["coverage_gaps"]) for m in manifests)
        zips_with_gaps = sum(1 for m in manifests if m["summary"]["coverage_gaps"])
        print(f"\n{'═' * 60}")
        print(f"  DECK {args.deck} SUMMARY")
        print(f"  Zips processed:        {len(manifests)}")
        print(f"  Zips with gaps (<3):   {zips_with_gaps}")
        print(f"  Total coverage gaps:   {total_gaps}")
        if total_gaps == 0:
            print(f"  ✓ Full coverage across all blocks in this deck")


if __name__ == "__main__":
    main()
