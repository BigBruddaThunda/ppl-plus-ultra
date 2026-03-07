#!/usr/bin/env python3
"""
build-exercise-card-index.py — Exercise Library v.1 Wave 2

Scans all 1,680 generated cards, extracts exercise names, fuzzy-matches
them to exercise-registry.json entries, and produces a cross-reference
index: exercise-card-index.json.

Outputs:
  - middle-math/exercise-card-index.json (EX-ID → cards + frequency)
  - Unmatched exercises report (exercises in cards not in registry)
  - Unused exercises report (registry entries never used in any card)

Usage:
  python scripts/build-exercise-card-index.py
  python scripts/build-exercise-card-index.py --stats
  python scripts/build-exercise-card-index.py --unmatched
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter

REPO_ROOT = Path(__file__).parent.parent
CARDS_DIR = REPO_ROOT / "cards"
REGISTRY_PATH = REPO_ROOT / "middle-math" / "exercise-registry.json"
LIBRARY_PATH = REPO_ROOT / "exercise-library.md"
OUTPUT_PATH = REPO_ROOT / "middle-math" / "exercise-card-index.json"

TYPE_EMOJIS = ['🛒', '🪡', '🍗', '➕', '➖']

EQUIPMENT_PREFIXES = [
    'barbell', 'dumbbell', 'kettlebell', 'cable', 'machine', 'band',
    'resistance band', 'plate', 'trap bar', 'smith machine', 'ez bar',
    'ez-bar', 'safety bar', 'swiss bar', 'landmine',
]


def extract_zip_from_path(filepath: Path) -> str:
    """Extract the 4-emoji zip code from a card filename."""
    name = filepath.name
    # Zip is the first 4 emojis before the ± symbol
    match = re.match(r'^(.+?)±', name)
    if match:
        return match.group(1)
    return ""


def extract_exercises_from_card(filepath: Path) -> list:
    """Extract exercise names from a card file. Returns list of strings."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            body = f.read()
    except Exception:
        return []

    exercises = []
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPE_EMOJIS) + ')'
    pattern = re.compile(
        r'^\s*[-*•├│]?\s*[-─]?\s*\d+\s+' + type_emoji_pattern + r'\s+(.+?)(?:\s*\(.*\))?\s*$'
    )

    for line in body.split('\n'):
        m = pattern.match(line)
        if m:
            name = m.group(1).strip()
            name = re.sub(r'\s*\(.*?\)\s*$', '', name).strip()
            name = re.sub(r'\s+at\s+\d+(?:\.\d+)?%\s*$', '', name, flags=re.IGNORECASE).strip()
            name = re.sub(r'\s+[×x]\s+\d+\s*$', '', name).strip()
            if name and len(name) > 2:
                exercises.append(name)

    return exercises


def normalize_name(name: str) -> str:
    """Normalize for matching: lowercase, strip punctuation, collapse whitespace."""
    s = name.lower().strip()
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def build_registry_lookup(registry: list) -> dict:
    """Build name → EX-ID lookup with multiple matching strategies."""
    lookup = {}

    for entry in registry:
        ex_id = entry["exercise_id"]
        name = entry["name"]
        norm = normalize_name(name)

        # Exact normalized name
        lookup[norm] = ex_id

        # Canonical name if different
        canonical = entry.get("canonical_name", "")
        if canonical and canonical != name:
            lookup[normalize_name(canonical)] = ex_id

        # Without equipment prefix
        for prefix in EQUIPMENT_PREFIXES:
            if norm.startswith(prefix + ' '):
                stripped = norm[len(prefix):].strip()
                if stripped and stripped not in lookup:
                    lookup[stripped] = ex_id

    return lookup


def match_exercise_to_registry(exercise_name: str, lookup: dict, registry_names_lower: list) -> str:
    """Try to match an exercise name to a registry entry. Returns EX-ID or None."""
    norm = normalize_name(exercise_name)

    # Strategy 1: Exact match
    if norm in lookup:
        return lookup[norm]

    # Strategy 2: First 3 words, then 2 words
    words = norm.split()
    if len(words) >= 3:
        three = ' '.join(words[:3])
        if three in lookup:
            return lookup[three]
    if len(words) >= 2:
        two = ' '.join(words[:2])
        if two in lookup:
            return lookup[two]

    # Strategy 3: Strip equipment prefix
    for prefix in EQUIPMENT_PREFIXES:
        if norm.startswith(prefix + ' '):
            stripped = norm[len(prefix):].strip()
            if stripped in lookup:
                return lookup[stripped]

    # Strategy 4: Substring match against all registry names
    for reg_name, ex_id in lookup.items():
        if len(reg_name) >= 6 and reg_name in norm:
            return ex_id
        if len(norm) >= 6 and norm in reg_name:
            return ex_id

    return None


def find_all_cards(cards_dir: Path) -> list:
    """Find all generated card files (not stubs)."""
    cards = []
    for root, dirs, files in os.walk(cards_dir):
        for f in files:
            if f.endswith('.md') and '±' in f and f != 'AGENTS.md':
                filepath = Path(root) / f
                # Check if it's generated (has content beyond stub)
                try:
                    with open(filepath, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                    if 'status: GENERATED' in content or 'status: CANONICAL' in content:
                        cards.append(filepath)
                except Exception:
                    pass
    return cards


def main():
    parser = argparse.ArgumentParser(description="Build exercise-to-card cross-reference index")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--unmatched", action="store_true", help="Show unmatched exercises")
    parser.add_argument("--dry-run", action="store_true", help="Don't write output file")
    args = parser.parse_args()

    # Load registry
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        registry = json.load(f)
    print(f"Loaded {len(registry)} exercises from registry")

    lookup = build_registry_lookup(registry)
    registry_names = {normalize_name(e["name"]): e["exercise_id"] for e in registry}

    # Initialize index
    index = {}
    for entry in registry:
        index[entry["exercise_id"]] = {
            "name": entry["name"],
            "movement_pattern": entry["movement_pattern"],
            "cards": [],
            "frequency": 0,
        }

    # Scan all cards
    cards = find_all_cards(CARDS_DIR)
    print(f"Found {len(cards)} generated cards")

    total_exercises = 0
    matched_exercises = 0
    unmatched_list = []
    card_count = 0

    for card_path in sorted(cards):
        zip_code = extract_zip_from_path(card_path)
        exercises = extract_exercises_from_card(card_path)
        card_count += 1

        for ex_name in exercises:
            total_exercises += 1
            ex_id = match_exercise_to_registry(ex_name, lookup, list(registry_names.keys()))

            if ex_id and ex_id in index:
                if zip_code not in index[ex_id]["cards"]:
                    index[ex_id]["cards"].append(zip_code)
                index[ex_id]["frequency"] += 1
                matched_exercises += 1
            else:
                unmatched_list.append({
                    "name": ex_name,
                    "card": zip_code,
                    "file": str(card_path.relative_to(REPO_ROOT)),
                })

    # Compute summary stats
    used = sum(1 for v in index.values() if v["frequency"] > 0)
    unused = sum(1 for v in index.values() if v["frequency"] == 0)
    match_rate = 100 * matched_exercises / total_exercises if total_exercises > 0 else 0

    print(f"\nResults:")
    print(f"  Cards scanned:     {card_count}")
    print(f"  Exercises found:   {total_exercises}")
    print(f"  Matched:           {matched_exercises} ({match_rate:.1f}%)")
    print(f"  Unmatched:         {len(unmatched_list)}")
    print(f"  Registry used:     {used} / {len(registry)}")
    print(f"  Registry unused:   {unused} / {len(registry)}")

    if args.unmatched and unmatched_list:
        print(f"\nUnmatched exercises ({len(unmatched_list)}):")
        # Deduplicate by name
        seen = set()
        for u in unmatched_list:
            key = normalize_name(u["name"])
            if key not in seen:
                print(f"  '{u['name']}' in {u['card']}")
                seen.add(key)
                if len(seen) >= 50:
                    remaining = len(set(normalize_name(x["name"]) for x in unmatched_list)) - len(seen)
                    if remaining > 0:
                        print(f"  ... and {remaining} more")
                    break

    if args.stats:
        # Top exercises by frequency
        sorted_by_freq = sorted(
            [(v["name"], v["frequency"], k) for k, v in index.items() if v["frequency"] > 0],
            key=lambda x: -x[1]
        )
        print(f"\nTop 20 exercises by frequency:")
        for name, freq, ex_id in sorted_by_freq[:20]:
            print(f"  {freq:4d}  {ex_id}  {name}")

        # Pattern distribution of used exercises
        pattern_usage = Counter()
        for v in index.values():
            if v["frequency"] > 0:
                pattern_usage[v["movement_pattern"]] += 1
        print(f"\nUsed exercises by movement pattern:")
        for p, c in pattern_usage.most_common():
            print(f"  {p:24} {c:5d}")

    # Build output (only used exercises, to keep file manageable)
    output = {
        "metadata": {
            "generated": "exercise-card-index",
            "cards_scanned": card_count,
            "exercises_extracted": total_exercises,
            "match_rate": round(match_rate, 1),
            "registry_used": used,
            "registry_unused": unused,
            "unmatched_count": len(unmatched_list),
        },
        "index": index,
        "unmatched": unmatched_list[:100],  # Cap at 100 for file size
    }

    if not args.dry_run:
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        size_kb = OUTPUT_PATH.stat().st_size // 1024
        print(f"\nWrote {OUTPUT_PATH} (~{size_kb} KB)")
    else:
        print("\nDry run — output not written.")


if __name__ == "__main__":
    main()
