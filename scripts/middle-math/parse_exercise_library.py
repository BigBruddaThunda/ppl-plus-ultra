#!/usr/bin/env python3
"""Parse exercise-library.md into structured JSON for middle-math tooling."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "exercise-library.md"
OUTPUT = ROOT / "middle-math" / "exercise-library.json"

TYPE_BY_EMOJI = {
    "🛒": "Push",
    "🪡": "Pull",
    "🍗": "Legs",
    "➕": "Plus",
    "➖": "Ultra",
}

ORDER_BY_EMOJI = {
    "🐂": "Foundation",
    "⛽": "Strength",
    "🦋": "Hypertrophy",
    "🏟": "Performance",
    "🌾": "Full Body",
    "⚖": "Balance",
    "🖼": "Restoration",
}

AXIS_BY_EMOJI = {
    "🏛": "Basics",
    "🔨": "Functional",
    "🌹": "Aesthetic",
    "🪐": "Challenge",
    "⌛": "Time",
    "🐬": "Partner",
}

UNILATERAL_TOKENS = (
    "single-arm",
    "single arm",
    "single-leg",
    "single leg",
    "one-arm",
    "one arm",
    "alternating",
    "split squat",
    "bulgarian",
    "pistol",
    "cossack",
    "archer",
    "half-kneeling",
)

ISOLATION_TOKENS = (
    "raise",
    "curl",
    "extension",
    "flexion",
    "rotation",
    "fly",
    "stretch",
    "mobilization",
    "release",
    "massage",
    "isometric",
    "activation",
    "cars",
    "wall slide",
    "external rotation",
    "internal rotation",
)

COMPOUND_TOKENS = (
    "press",
    "push-up",
    "push up",
    "row",
    "pull-up",
    "chin-up",
    "dip",
    "deadlift",
    "squat",
    "lunge",
    "carry",
    "snatch",
    "clean",
    "jerk",
    "thruster",
    "swing",
    "muscle-up",
    "step-up",
)

SECTION_PATTERN = re.compile(r"^SECTION ([A-Q]):\s+(.+?)\s*\((\d+) exercises\)", re.MULTILINE)
EXERCISE_PATTERN = re.compile(r"^(\d+)\.\s+(.+)$")


def _extract_emoji_values(text: str, emoji_map: dict[str, str]) -> list[str]:
    values: list[str] = []
    for emoji, label in emoji_map.items():
        if emoji in text and label not in values:
            values.append(label)
    return values


def _parse_gold_ids(section_block: str) -> set[int]:
    gold_line = ""
    for line in section_block.splitlines():
        if line.startswith("Equipment Tier:") and "GOLD:" in line:
            gold_line = line
            break
    ids: set[int] = set()
    for start, end in re.findall(r"#(\d+)(?:[–-](\d+))?", gold_line):
        s = int(start)
        e = int(end) if end else s
        ids.update(range(s, e + 1))
    return ids


def _extract_section_metadata(section_letter: str, block: str) -> dict[str, Any]:
    lines = [line.strip() for line in block.splitlines() if line.strip()]

    mapping_line = next((line for line in lines if line.startswith("SCL Mapping:")), "")
    orders_line = next((line for line in lines if line.startswith("Orders:")), "")
    axes_line = next((line for line in lines if line.startswith("Axes:")), "")
    tier_line = next((line for line in lines if line.startswith("Equipment Tier:")), "")

    scl_types = _extract_emoji_values(mapping_line, TYPE_BY_EMOJI)

    order_relevance = _extract_emoji_values(orders_line, ORDER_BY_EMOJI)
    if "Orders: All" in orders_line and not order_relevance:
        order_relevance = list(ORDER_BY_EMOJI.values())

    axis_emphasis = _extract_emoji_values(axes_line, AXIS_BY_EMOJI)
    if "Axes: All" in axes_line:
        axis_emphasis = list(AXIS_BY_EMOJI.values())

    tier_match = re.search(r"Equipment Tier:\s*(\d+)\s*[–-]\s*(\d+)", tier_line)
    if not tier_match:
        raise ValueError(f"Could not parse equipment tier for section {section_letter}")

    tier_min, tier_max = int(tier_match.group(1)), int(tier_match.group(2))

    section_gold = section_letter in {"J", "K", "Q"}
    explicit_gold_ids = _parse_gold_ids(block)

    return {
        "scl_types": scl_types,
        "order_relevance": order_relevance,
        "axis_emphasis": axis_emphasis,
        "equipment_tier": [tier_min, tier_max],
        "section_gold": section_gold,
        "explicit_gold_ids": explicit_gold_ids,
    }


def _is_bilateral(name: str) -> bool:
    lowered = name.lower()
    return not any(token in lowered for token in UNILATERAL_TOKENS)


def _is_compound(name: str, movement_pattern: str) -> bool:
    lowered = name.lower()
    pattern = movement_pattern.lower()

    if any(token in lowered for token in COMPOUND_TOKENS):
        return True
    if any(token in lowered for token in ISOLATION_TOKENS):
        return False
    if any(token in pattern for token in ("mobility", "corrective", "prehab", "isometric", "stretch")):
        return False
    return any(token in pattern for token in ("press", "row", "pull", "carry", "deadlift", "squat"))


def parse_exercise_library(text: str) -> list[dict[str, Any]]:
    sections = list(SECTION_PATTERN.finditer(text))
    parsed: list[dict[str, Any]] = []

    for i, match in enumerate(sections):
        section_letter = match.group(1)
        section_name = match.group(2).strip()
        start = match.end()
        end = sections[i + 1].start() if i + 1 < len(sections) else len(text)
        block = text[start:end]

        metadata = _extract_section_metadata(section_letter, block)

        current_pattern = section_name
        for raw_line in block.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            exercise_match = EXERCISE_PATTERN.match(line)
            if exercise_match:
                exercise_id = int(exercise_match.group(1))
                exercise_name = exercise_match.group(2).strip()

                if " - " in current_pattern:
                    muscle_groups, movement_pattern = [part.strip() for part in current_pattern.split(" - ", 1)]
                else:
                    muscle_groups, movement_pattern = section_name, current_pattern

                gold_gated = metadata["section_gold"] or exercise_id in metadata["explicit_gold_ids"]

                parsed.append(
                    {
                        "id": exercise_id,
                        "section": section_letter,
                        "name": exercise_name,
                        "scl_types": metadata["scl_types"],
                        "order_relevance": metadata["order_relevance"],
                        "axis_emphasis": metadata["axis_emphasis"],
                        "equipment_tier": metadata["equipment_tier"],
                        "gold_gated": gold_gated,
                        "movement_pattern": movement_pattern,
                        "muscle_groups": muscle_groups,
                        "bilateral": _is_bilateral(exercise_name),
                        "compound": _is_compound(exercise_name, movement_pattern),
                    }
                )
                continue

            # Track subsection headings for movement/muscle context.
            if line.startswith(("SCL Mapping:", "Orders:", "Axes:", "Equipment Tier:", "Operator Affinity:", "Notes:")):
                continue
            if line.startswith("GOLD GATE REFERENCE"):
                break
            current_pattern = line

    return parsed


def build_stats(exercises: list[dict[str, Any]]) -> dict[str, Any]:
    section_counts = Counter(item["section"] for item in exercises)
    type_counts = Counter()
    for item in exercises:
        for t in item["scl_types"]:
            type_counts[t] += 1
    gold_count = sum(1 for item in exercises if item["gold_gated"])
    tier_distribution = Counter()
    for item in exercises:
        lo, hi = item["equipment_tier"]
        tier_distribution[f"{lo}-{hi}"] += 1

    return {
        "total": len(exercises),
        "sections": dict(sorted(section_counts.items())),
        "types": dict(sorted(type_counts.items())),
        "gold_gated": gold_count,
        "tiers": dict(sorted(tier_distribution.items())),
    }


def print_stats(stats: dict[str, Any]) -> None:
    print(f"Total exercises: {stats['total']}")
    print("Exercises per section:")
    for section, count in stats["sections"].items():
        print(f"  {section}: {count}")
    print("Exercises per Type:")
    for type_name, count in stats["types"].items():
        print(f"  {type_name}: {count}")
    print(f"GOLD-gated count: {stats['gold_gated']}")
    print("Tier distribution:")
    for tier, count in stats["tiers"].items():
        print(f"  {tier}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse exercise-library.md into JSON")
    parser.add_argument("--stats", action="store_true", help="Print parser summary statistics")
    args = parser.parse_args()

    text = SOURCE.read_text(encoding="utf-8")
    exercises = parse_exercise_library(text)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(exercises, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.stats:
        print_stats(build_stats(exercises))


if __name__ == "__main__":
    main()
