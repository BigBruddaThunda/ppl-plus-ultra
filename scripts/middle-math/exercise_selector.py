#!/usr/bin/env python3
"""
scripts/middle-math/exercise_selector.py
CX-43: Exercise Selector V2 (registry-aware)

V2 default behavior:
- Uses middle-math/exercise-registry.json
- Uses octave-scale axis_affinity/order_affinity directly
- Applies family diversity penalty across prior blocks (x0.3)
- Supports optional substitution chains via --show-subs
- Fixes catch-all movement_pattern="core-stability" using family_id overrides

Backward compatibility:
- --v1 reverts to CX-15 behavior (exercise-library.json + binary affinity + no family penalty)
"""

import argparse
import copy
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ZIP_REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
VECTORS_PATH = REPO_ROOT / "middle-math" / "weight-vectors.json"
EXERCISE_LIBRARY_PATH = REPO_ROOT / "middle-math" / "exercise-library.json"
EXERCISE_REGISTRY_PATH = REPO_ROOT / "middle-math" / "exercise-registry.json"
SUBSTITUTION_MAP_PATH = REPO_ROOT / "middle-math" / "exercise-engine" / "substitution-map.json"

# ---------------------------------------------------------------------------
# 61-emoji position map (weight vector dimensional index)
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
VECTOR_SIZE = 61

# ---------------------------------------------------------------------------
# Name maps
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
TYPE_EMOJI_TO_NAME = {v: k for k, v in TYPE_NAME_TO_EMOJI.items()}

# Registry affinity key maps
ORDER_AFFINITY_KEY_TO_EMOJI = {
    "foundation": "🐂", "strength": "⛽", "hypertrophy": "🦋",
    "performance": "🏟", "full_body": "🌾", "balance": "⚖", "restoration": "🖼",
}
AXIS_AFFINITY_KEY_TO_EMOJI = {
    "classic": "🏛", "functional": "🔨", "aesthetic": "🌹",
    "challenge": "🪐", "time": "⌛", "partner": "🐬",
}

COLOR_TIER_RANGES = {
    "⚫": (2, 3), "🟢": (0, 2), "🔵": (2, 3), "🟣": (2, 5),
    "🔴": (2, 4), "🟠": (0, 3), "🟡": (0, 5), "⚪": (0, 3),
}
GOLD_ELIGIBLE_COLORS = {"🟣", "🔴"}

BLOCK_SEQUENCES = {
    "🐂": ["♨️", "🔢", "🧈", "🧩", "🧬", "🚂"],
    "⛽": ["♨️", "▶️", "🧈", "🧩", "🪫", "🚂"],
    "🦋": ["♨️", "▶️", "🧈", "🗿", "🪞", "🧩", "🪫", "🚂"],
    "🏟": ["♨️", "🪜", "🧈", "🚂"],
    "🌾": ["♨️", "🎼", "🧈", "🧩", "🪫", "🚂"],
    "⚖": ["♨️", "🏗", "🧈", "🧩", "🪫", "🚂"],
    "🖼": ["🎯", "🪫", "🧈", "🧬", "🚂"],
}
STRUCTURAL_BLOCKS = {"♨️", "🚂", "🧮", "🎯"}
BLOCK_NAMES = {
    "♨️": "Warm-Up", "🎯": "Intention", "🔢": "Fundamentals", "🧈": "Bread/Butter",
    "🫀": "Circulation", "▶️": "Primer", "🎼": "Composition", "♟️": "Gambit",
    "🪜": "Progression", "🌎": "Exposure", "🎱": "ARAM", "🌋": "Gutter",
    "🪞": "Vanity", "🗿": "Sculpt", "🛠": "Craft", "🧩": "Supplemental",
    "🪫": "Release", "🏖": "Sandbox", "🏗": "Reformance", "🧬": "Imprint",
    "🚂": "Junction", "🔠": "Choice", "🧮": "SAVE",
}

MAJOR_PATTERN_FAMILIES = {
    "hip-hinge", "squat", "horizontal-press", "vertical-press", "horizontal-pull",
    "vertical-pull", "isolation-curl", "isolation-extension", "lunge", "carry",
    "anti-rotation", "conditioning", "olympic", "plyometric", "leg-isolation",
}


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_registry_lookup(registry: list) -> dict:
    by_numeric = {}
    by_emoji = {}
    for entry in registry:
        by_numeric[entry["numeric_zip"]] = entry
        by_emoji[entry["emoji_zip"]] = entry
    return {"numeric": by_numeric, "emoji": by_emoji}


def preprocess_registry_exercises(exercises: list) -> tuple[list, int]:
    """Override catch-all movement_pattern where family_id is a known major pattern."""
    overrides = 0
    processed = copy.deepcopy(exercises)
    for ex in processed:
        if ex.get("movement_pattern") == "core-stability" and ex.get("family_id") in MAJOR_PATTERN_FAMILIES:
            ex["movement_pattern"] = ex["family_id"]
            overrides += 1
    return processed, overrides


# ---------------------------------------------------------------------------
# Affinity/scoring
# ---------------------------------------------------------------------------
def build_exercise_affinity_v1(exercise: dict) -> list:
    vec = [0.0] * VECTOR_SIZE
    for type_name in exercise.get("scl_types", []):
        type_emoji = TYPE_NAME_TO_EMOJI.get(type_name)
        if type_emoji:
            vec[EMOJI_POSITIONS[type_emoji]] += 2.0
    for order_name in exercise.get("order_relevance", []):
        order_emoji = ORDER_NAME_TO_EMOJI.get(order_name)
        if order_emoji:
            vec[EMOJI_POSITIONS[order_emoji]] += 1.0
    for axis_name in exercise.get("axis_emphasis", []):
        axis_emoji = AXIS_NAME_TO_EMOJI.get(axis_name)
        if axis_emoji:
            vec[EMOJI_POSITIONS[axis_emoji]] += 1.0
    return vec


def build_exercise_affinity_v2(exercise: dict) -> list:
    """Octave-scale affinity: direct axis/order weights + Type +2; all else zero."""
    vec = [0.0] * VECTOR_SIZE

    for type_name in exercise.get("scl_types", []):
        type_emoji = TYPE_NAME_TO_EMOJI.get(type_name)
        if type_emoji:
            vec[EMOJI_POSITIONS[type_emoji]] += 2.0

    for axis_key, weight in exercise.get("axis_affinity", {}).items():
        axis_emoji = AXIS_AFFINITY_KEY_TO_EMOJI.get(axis_key)
        if axis_emoji is not None:
            vec[EMOJI_POSITIONS[axis_emoji]] = float(weight)

    for order_key, weight in exercise.get("order_affinity", {}).items():
        order_emoji = ORDER_AFFINITY_KEY_TO_EMOJI.get(order_key)
        if order_emoji is not None:
            vec[EMOJI_POSITIONS[order_emoji]] = float(weight)

    return vec


def dot_product(a: list, b: list) -> float:
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Filters
# ---------------------------------------------------------------------------
def exercise_identifier(exercise: dict) -> str:
    return exercise.get("exercise_id") or exercise.get("id") or "UNKNOWN"


def passes_type_filter(exercise: dict, type_name: str) -> bool:
    return type_name in exercise.get("scl_types", [])


def passes_equipment_tier_filter(exercise: dict, color_emoji: str) -> bool:
    color_min, color_max = COLOR_TIER_RANGES.get(color_emoji, (0, 5))
    ex_min, ex_max = exercise.get("equipment_tier", [0, 5])
    return max(color_min, ex_min) <= min(color_max, ex_max)


def passes_gold_gate(exercise: dict, color_emoji: str) -> bool:
    return (not exercise.get("gold_gated", False)) or (color_emoji in GOLD_ELIGIBLE_COLORS)


def passes_order_relevance(exercise: dict, order_name: str) -> bool:
    return order_name in exercise.get("order_relevance", [])


def passes_no_barbell_constraint(exercise: dict, color_emoji: str) -> bool:
    if color_emoji in {"🟢", "🟠"}:
        ex_min = exercise.get("equipment_tier", [0, 5])[0]
        if ex_min >= 3:
            return False
    return True


# ---------------------------------------------------------------------------
# Core selection
# ---------------------------------------------------------------------------
def select_for_block(
    block_emoji: str,
    zip_entry: dict,
    zip_vector: list,
    exercises: list,
    already_selected: set,
    prior_families: set,
    top_n: int,
    v1_mode: bool,
    substitution_map: dict,
    show_subs: bool,
) -> dict:
    order_emoji = zip_entry["order"]["emoji"]
    type_emoji = zip_entry["type"]["emoji"]
    color_emoji = zip_entry["color"]["emoji"]
    order_name = ORDER_EMOJI_TO_NAME.get(order_emoji, "")
    type_name = TYPE_EMOJI_TO_NAME.get(type_emoji, "")

    stats = {
        "considered": 0,
        "filtered_type": 0,
        "filtered_tier": 0,
        "filtered_gold": 0,
        "filtered_order": 0,
        "filtered_barbell": 0,
        "filtered_duplicate": 0,
        "scored": 0,
        "family_penalized": 0,
        "filtered_same_family_block": 0,
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

        ex_id = exercise_identifier(ex)
        if ex_id in already_selected:
            stats["filtered_duplicate"] += 1
            continue

        affinity = build_exercise_affinity_v1(ex) if v1_mode else build_exercise_affinity_v2(ex)
        score = dot_product(zip_vector, affinity)

        family_id = ex.get("family_id")
        family_penalty_applied = False
        if (not v1_mode) and family_id and family_id in prior_families:
            score *= 0.3
            family_penalty_applied = True
            stats["family_penalized"] += 1

        stats["scored"] += 1
        scored.append((score, ex, family_penalty_applied))

    scored.sort(key=lambda x: x[0], reverse=True)

    top = []
    block_families = set()
    for score, ex, family_penalty_applied in scored:
        family_id = ex.get("family_id")
        if family_id and family_id in block_families:
            stats["filtered_same_family_block"] += 1
            continue
        top.append((score, ex, family_penalty_applied))
        if family_id:
            block_families.add(family_id)
        if len(top) >= top_n:
            break

    candidates = []
    for score, ex, family_penalty_applied in top:
        ex_id = exercise_identifier(ex)
        candidate = {
            "id": ex_id,
            "name": ex.get("name", ""),
            "score": round(score, 2),
            "section": ex.get("source_section") or ex.get("section", "?"),
            "muscle_groups": ex.get("muscle_groups", ""),
            "movement_pattern": ex.get("movement_pattern", ""),
            "equipment_tier": ex.get("equipment_tier", [0, 5]),
            "gold_gated": ex.get("gold_gated", False),
            "family_id": ex.get("family_id"),
            "family_penalty_applied": family_penalty_applied,
        }

        if show_subs:
            subs = substitution_map.get(ex_id, {})
            candidate["substitutions"] = {
                "tier_down": subs.get("tier_down", []),
                "tier_up": subs.get("tier_up", []),
                "cross_family": subs.get("cross_family", []),
            }

        candidates.append(candidate)

    return {
        "block": block_emoji,
        "block_name": BLOCK_NAMES.get(block_emoji, block_emoji),
        "candidates": candidates,
        "stats": stats,
    }


def select_for_zip(
    zip_entry: dict,
    zip_vector: list,
    exercises: list,
    top_n: int,
    v1_mode: bool,
    substitution_map: dict,
    show_subs: bool,
) -> dict:
    block_sequence = BLOCK_SEQUENCES.get(zip_entry["order"]["emoji"], ["♨️", "🧈", "🚂"])
    selection_blocks = [b for b in block_sequence if b not in STRUCTURAL_BLOCKS]

    already_selected = set()
    prior_families = set()
    block_results = []
    total_stats = {
        "considered": 0,
        "filtered_type": 0,
        "filtered_tier": 0,
        "filtered_gold": 0,
        "filtered_order": 0,
        "filtered_barbell": 0,
        "filtered_duplicate": 0,
        "scored": 0,
        "family_penalized": 0,
    }

    for block_emoji in selection_blocks:
        result = select_for_block(
            block_emoji=block_emoji,
            zip_entry=zip_entry,
            zip_vector=zip_vector,
            exercises=exercises,
            already_selected=already_selected,
            prior_families=prior_families,
            top_n=top_n,
            v1_mode=v1_mode,
            substitution_map=substitution_map,
            show_subs=show_subs,
        )
        block_results.append(result)

        for candidate in result["candidates"]:
            already_selected.add(candidate["id"])
            family_id = candidate.get("family_id")
            if family_id:
                prior_families.add(family_id)

        for k in total_stats:
            total_stats[k] += result["stats"].get(k, 0)

    coverage_gaps = [
        {"block": r["block"], "block_name": r["block_name"], "candidates_found": len(r["candidates"])}
        for r in block_results
        if len(r["candidates"]) < 3
    ]

    return {
        "zip": zip_entry["numeric_zip"],
        "emoji_zip": zip_entry["emoji_zip"],
        "order": {"emoji": zip_entry["order"]["emoji"], "name": zip_entry["order"]["name"]},
        "axis": {"emoji": zip_entry["axis"]["emoji"], "name": zip_entry["axis"]["name"]},
        "type": {"emoji": zip_entry["type"]["emoji"], "name": zip_entry["type"]["name"]},
        "color": {"emoji": zip_entry["color"]["emoji"], "name": zip_entry["color"]["name"]},
        "gold_eligible": zip_entry.get("gold_eligible", False),
        "mode": "v1" if v1_mode else "v2",
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
    violations = []
    zip_code = manifest["zip"]
    emoji_zip = manifest["emoji_zip"]
    color_e = manifest["color"]["emoji"]
    is_gold = color_e in GOLD_ELIGIBLE_COLORS

    seen_exercise_ids = {}

    for block_result in manifest["blocks"]:
        block_e = block_result["block"]
        block_name = block_result["block_name"]
        seen_families_in_block = {}

        for cand in block_result["candidates"]:
            ex_id = cand["id"]
            ex_name = cand["name"]
            family_id = cand.get("family_id")

            if cand.get("gold_gated", False) and not is_gold:
                violations.append(
                    f"[{zip_code} {emoji_zip}] GOLD exercise in non-GOLD color {color_e}: "
                    f"'{ex_name}' (id={ex_id}) in block {block_e} {block_name}"
                )

            if ex_id in seen_exercise_ids:
                prev_block = seen_exercise_ids[ex_id]
                violations.append(
                    f"[{zip_code} {emoji_zip}] Duplicate exercise '{ex_name}' (id={ex_id}) "
                    f"in blocks {prev_block} and {block_e} {block_name}"
                )
            else:
                seen_exercise_ids[ex_id] = f"{block_e} {block_name}"

            if family_id:
                if family_id in seen_families_in_block:
                    prev_ex = seen_families_in_block[family_id]
                    violations.append(
                        f"[{zip_code} {emoji_zip}] Same-family candidates in block {block_e} {block_name}: "
                        f"{prev_ex} and {ex_name} share family_id={family_id}"
                    )
                else:
                    seen_families_in_block[family_id] = ex_name

    return violations


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def format_text(manifest: dict, show_subs: bool = False) -> str:
    lines = []
    z = manifest
    lines.append(f"\n{'═' * 60}")
    lines.append(f"  {z['emoji_zip']}  ({z['zip']})")
    lines.append(
        f"  {z['order']['emoji']} {z['order']['name']} | "
        f"{z['axis']['emoji']} {z['axis']['name']} | "
        f"{z['type']['emoji']} {z['type']['name']} | "
        f"{z['color']['emoji']} {z['color']['name']}"
    )
    lines.append(f"  Mode: {z['mode'].upper()}")
    lines.append(f"  GOLD eligible: {'YES' if z['gold_eligible'] else 'no'}")
    lines.append(f"{'─' * 60}")

    for block in z["blocks"]:
        lines.append(f"\n  {block['block']} {block['block_name']}")
        if not block["candidates"]:
            lines.append("    (no candidates found)")
        for i, c in enumerate(block["candidates"], 1):
            tier = f"T{c['equipment_tier'][0]}-{c['equipment_tier'][1]}"
            gold = " [GOLD]" if c.get("gold_gated") else ""
            fam = f" family={c.get('family_id', 'n/a')}"
            penalized = " [family-penalty]" if c.get("family_penalty_applied") else ""
            lines.append(f"    {i}. {c['name']}{gold}{penalized}")
            lines.append(f"       id={c['id']} score={c['score']:+.2f} {tier}{fam}")
            if show_subs and "substitutions" in c:
                subs = c["substitutions"]
                lines.append(f"       subs: ↓{subs['tier_down']} ↑{subs['tier_up']} ↔{subs['cross_family']}")

    gaps = z["summary"]["coverage_gaps"]
    if gaps:
        lines.append("\n  ⚠ Coverage gaps (<3 candidates):")
        for g in gaps:
            lines.append(f"    {g['block']} {g['block_name']}: {g['candidates_found']} found")

    return "\n".join(lines)


def format_stats(manifest: dict) -> str:
    z = manifest
    s = z["summary"]["total_stats"]
    lines = [
        f"\n  {z['emoji_zip']} ({z['zip']}) stats:",
        f"    Considered:         {s['considered']}",
        f"    Filtered by type:   {s['filtered_type']}",
        f"    Filtered by tier:   {s['filtered_tier']}",
        f"    Filtered by GOLD:   {s['filtered_gold']}",
        f"    Filtered by order:  {s['filtered_order']}",
        f"    Filtered barbell:   {s['filtered_barbell']}",
        f"    Filtered duplicate: {s['filtered_duplicate']}",
        f"    Family penalized:   {s['family_penalized']}",
        f"    Scored:             {s['scored']}",
    ]
    gaps = z["summary"]["coverage_gaps"]
    if gaps:
        lines.append(f"    ⚠ Coverage gaps: {len(gaps)} block(s)")
    else:
        lines.append("    ✓ All blocks have 3+ candidates")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_deck_zips(registry: list, deck_number: int) -> list:
    return [e for e in registry if e.get("deck_number") == deck_number]


def resolve_zip_entries(args, lookup, registry):
    if args.zip:
        entry = lookup["numeric"].get(args.zip) or lookup["emoji"].get(args.zip)
        if not entry:
            raise ValueError(f"zip code not found: {args.zip}")
        return [entry]
    if args.deck:
        deck_num = int(args.deck)
        zips = get_deck_zips(registry, deck_num)
        if not zips:
            raise ValueError(f"no zip codes found for deck {deck_num}")
        return zips
    return registry


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="CX-43: PPL± Exercise Selector V2 (registry-aware)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--zip", type=str, help="Single zip (emoji or numeric)")
    group.add_argument("--deck", type=str, help="All zips in deck (e.g., 07)")
    group.add_argument("--all", action="store_true", help="Run all 1,680 zips")

    parser.add_argument("--validate", action="store_true", help="Validate manifests")
    parser.add_argument("--stats", action="store_true", help="Print filter stats")
    parser.add_argument("--output", choices=["json", "text"], default="text")
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--v1", action="store_true", help="Use CX-15 behavior (library + binary affinity)")
    parser.add_argument("--show-subs", action="store_true", help="Include substitution chains in output")
    args = parser.parse_args()

    print("Loading data...", end=" ", flush=True)
    zip_registry = load_json(ZIP_REGISTRY_PATH)
    vectors = load_json(VECTORS_PATH)

    if args.v1:
        exercises = load_json(EXERCISE_LIBRARY_PATH)
        substitution_map = {}
        print(f"done. {len(zip_registry)} zips, {len(exercises)} exercises (V1 mode).")
    else:
        raw_exercises = load_json(EXERCISE_REGISTRY_PATH)
        exercises, overrides = preprocess_registry_exercises(raw_exercises)
        substitution_map = load_json(SUBSTITUTION_MAP_PATH)
        print(f"done. {len(zip_registry)} zips, {len(exercises)} exercises (V2 mode).")
        print(f"movement_pattern overrides applied: {overrides}", file=sys.stderr)

    lookup = build_registry_lookup(zip_registry)

    try:
        zip_entries = resolve_zip_entries(args, lookup, zip_registry)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.deck:
        print(f"Deck {int(args.deck)}: {len(zip_entries)} zip codes.")
    if args.all:
        print(f"All mode: {len(zip_entries)} zip codes.")

    manifests = []
    for zip_entry in zip_entries:
        numeric_zip = zip_entry["numeric_zip"]
        zip_vector = vectors.get(numeric_zip, {}).get("vector", [0.0] * VECTOR_SIZE)
        manifests.append(
            select_for_zip(
                zip_entry=zip_entry,
                zip_vector=zip_vector,
                exercises=exercises,
                top_n=args.top,
                v1_mode=args.v1,
                substitution_map=substitution_map,
                show_subs=args.show_subs,
            )
        )

    if args.validate:
        all_violations = []
        manifest_failures = 0
        for m in manifests:
            violations = validate_manifest(m)
            if violations:
                manifest_failures += 1
                all_violations.extend(violations)

        manifest_passes = len(manifests) - manifest_failures
        print("\n--- VALIDATION SUMMARY ---")
        print(f"  Zips checked: {len(manifests)}")
        print(f"  Pass: {manifest_passes}")
        print(f"  Fail: {manifest_failures}")

        if all_violations:
            print(f"\n--- VALIDATION FAILED: {len(all_violations)} violation(s) ---")
            for v in all_violations[:200]:
                print(f"  ✗ {v}")
            if len(all_violations) > 200:
                print(f"  ... {len(all_violations) - 200} additional violations omitted")
            sys.exit(1)

        print("  ✓ No GOLD exercises outside 🔴/🟣 colors")
        print("  ✓ No duplicate exercises across blocks within any zip")
        print("  ✓ No same-family candidates within any block")

    if args.output == "json":
        output = manifests[0] if len(manifests) == 1 else manifests
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        for m in manifests:
            print(format_text(m, show_subs=args.show_subs))
            if args.stats:
                print(format_stats(m))


if __name__ == "__main__":
    main()
