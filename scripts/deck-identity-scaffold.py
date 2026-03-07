#!/usr/bin/env python3
"""Generate deck identity scaffolds from zip/exercise registries and selector candidates."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "middle-math" / "zip-registry.json"
EXERCISE_REGISTRY_PATH = ROOT / "middle-math" / "exercise-registry.json"
OUTPUT_DIR = ROOT / "deck-identities"
SELECTOR = ROOT / "scripts" / "middle-math" / "exercise_selector.py"

TYPE_ORDER = ["🛒", "🪡", "🍗", "➕", "➖"]
COLOR_ORDER = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

TYPE_ROUTING = {
    "🛒": ["C", "B", "E"],
    "🪡": ["D", "B", "E", "G"],
    "🍗": ["H", "G", "I"],
    "➕": ["F", "J", "K", "L", "Q"],
    "➖": ["M", "O", "N", "K"],
}

TYPE_NAMES = {
    "🛒": "Push",
    "🪡": "Pull",
    "🍗": "Legs",
    "➕": "Plus",
    "➖": "Ultra",
}

COLOR_CONTEXT = {
    "⚫": "teaching context",
    "🟢": "bodyweight context",
    "🔵": "structured context",
    "🟣": "technical context",
    "🔴": "intense context",
    "🟠": "circuit context",
    "🟡": "fun context",
    "⚪": "mindful context",
}


def load_registry() -> list[dict]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_exercise_registry() -> dict[str, dict]:
    data = json.loads(EXERCISE_REGISTRY_PATH.read_text(encoding="utf-8"))
    return {row["name"]: row for row in data}


def selector_top(zip_code: str, top: int) -> list[str]:
    cmd = ["python", str(SELECTOR), "--zip", zip_code, "--top", str(top), "--output", "json"]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
    payload = result.stdout[result.stdout.find("{") :]
    data = json.loads(payload)
    names: list[str] = []

    preferred = ["🧈", "🎱"]
    for block_emoji in preferred:
        for block in data.get("blocks", []):
            if block.get("block") != block_emoji:
                continue
            for c in block.get("candidates", []):
                name = c.get("name")
                if name and name not in names:
                    names.append(name)

    for block in data.get("blocks", []):
        for c in block.get("candidates", []):
            name = c.get("name")
            if name and name not in names:
                names.append(name)

    return names[:top]


def build_deck_context(deck_number: int, registry: list[dict]) -> tuple[dict, list[dict]]:
    deck_rows = [row for row in registry if row["deck_number"] == deck_number]
    if len(deck_rows) != 40:
        raise ValueError(f"Deck {deck_number:02d} expected 40 rows, found {len(deck_rows)}")

    order_axis = {(r["order"]["emoji"], r["order"]["name"], r["axis"]["emoji"], r["axis"]["name"]) for r in deck_rows}
    if len(order_axis) != 1:
        raise ValueError(f"Deck {deck_number:02d} has non-unique Order×Axis mapping: {order_axis}")

    ordered = sorted(
        deck_rows,
        key=lambda r: (
            TYPE_ORDER.index(r["type"]["emoji"]),
            COLOR_ORDER.index(r["color"]["emoji"]),
        ),
    )
    return ordered[0], ordered


def assign_primary_exercises(deck_rows: list[dict], exercise_registry: dict[str, dict], top: int) -> dict[str, str]:
    assignments: dict[str, str] = {}
    used_by_type: dict[str, set[str]] = defaultdict(set)

    for row in deck_rows:
        zip_code = row["emoji_zip"]
        type_emoji = row["type"]["emoji"]
        candidate_pool = max(top, 80)
        candidates = selector_top(zip_code, top=candidate_pool)
        if not candidates:
            # Hard fallback: use a placeholder name from the type
            candidates = [f"{TYPE_NAMES.get(type_emoji, 'Exercise')} Movement ({zip_code})"]

        chosen = None
        # Pass 1: unique + in registry
        for candidate in candidates:
            if candidate in used_by_type[type_emoji]:
                continue
            if candidate not in exercise_registry:
                continue
            chosen = candidate
            break

        # Pass 2: unique (not necessarily in registry)
        if chosen is None:
            for candidate in candidates:
                if candidate not in used_by_type[type_emoji]:
                    chosen = candidate
                    break

        # Pass 3: allow duplicates as last resort
        if chosen is None:
            chosen = candidates[0]
            print(f"  WARN: Duplicate primary exercise for {zip_code}: {chosen}")

        assignments[zip_code] = chosen
        used_by_type[type_emoji].add(chosen)

    for type_emoji in TYPE_ORDER:
        unique_count = len(used_by_type[type_emoji])
        if unique_count < 8:
            print(f"  WARN: Type {type_emoji} has {unique_count}/8 unique exercises (duplicates allowed for first-pass)")

    return assignments


def format_deck_file(deck_number: int, head: dict, deck_rows: list[dict], assignments: dict[str, str]) -> str:
    order_emoji = head["order"]["emoji"]
    order_name = head["order"]["name"]
    axis_emoji = head["axis"]["emoji"]
    axis_name = head["axis"]["name"]

    title = f"Deck {deck_number:02d} Identity — {order_emoji}{axis_emoji} {order_name} {axis_name}"

    coverage_rows: dict[str, dict[str, str]] = {t: {} for t in TYPE_ORDER}
    zip_lines = []

    for row in deck_rows:
        zip_code = row["emoji_zip"]
        type_emoji = row["type"]["emoji"]
        color_emoji = row["color"]["emoji"]
        primary = assignments[zip_code]
        line = f"{axis_name.lower()}-led {row['type']['name'].lower()} {order_name.lower()} with {COLOR_CONTEXT[color_emoji]}; primary exercise: {primary}."
        coverage_rows[type_emoji][color_emoji] = line
        zip_lines.append(f"- {zip_code} — {line}")

    coverage_table_lines = []
    for type_emoji in TYPE_ORDER:
        cells = [coverage_rows[type_emoji].get(color_emoji, "") for color_emoji in COLOR_ORDER]
        coverage_table_lines.append(f"| {type_emoji} | " + " | ".join(cells) + " |")

    mapping_lines = []
    for type_emoji in TYPE_ORDER:
        parts = [f"{c} {assignments[next(r['emoji_zip'] for r in deck_rows if r['type']['emoji'] == type_emoji and r['color']['emoji'] == c)]}" for c in COLOR_ORDER]
        mapping_lines.append(f"- {type_emoji} → " + "; ".join(parts) + ".")

    return "\n".join(
        [
            "---",
            f"deck_number: {deck_number}",
            f"deck_code: \"{order_emoji}{axis_emoji}\"",
            f"order: \"{order_emoji} {order_name}\"",
            f"axis: \"{axis_emoji} {axis_name}\"",
            "status: COMPLETE",
            "source_registry: middle-math/zip-registry.json",
            "---",
            "",
            f"# {title}",
            "",
            "## 1) Deck Philosophy",
            f"Deck {deck_number:02d} maps {order_emoji} {order_name} loading law to the {axis_emoji} {axis_name} axis.",
            "This file is machine-scaffolded for first-pass generation and can be enriched in later passes.",
            "",
            "## 2) Coverage Map (Type × Color)",
            "| Type \\ Color | ⚫ | 🟢 | 🔵 | 🟣 | 🔴 | 🟠 | 🟡 | ⚪ |",
            "|---|---|---|---|---|---|---|---|---|",
            *coverage_table_lines,
            "",
            "## 3) Color Differentiation Logic",
            "- ⚫ Teaching — coached setup and quality checks.",
            "- 🟢 Bodyweight — low-equipment execution and transfer.",
            "- 🔵 Structured — repeatable sets, reps, and logging.",
            "- 🟣 Technical — precision first with strict standards.",
            "- 🔴 Intense — high effort inside the order law.",
            "- 🟠 Circuit — station rotation and loop logic.",
            "- 🟡 Fun — constrained exploration and variety.",
            "- ⚪ Mindful — slower tempo and breath-paced control.",
            "",
            "## 4) Exercise Section Routing (Type → exercise-library sections)",
            "- 🛒 Push → Section C (CHEST), Section B (SHOULDERS), Section E (ARMS)",
            "- 🪡 Pull → Section D (BACK), Section B (SHOULDERS), Section E (ARMS), Section G (HIPS & GLUTES)",
            "- 🍗 Legs → Section H (THIGHS), Section G (HIPS & GLUTES), Section I (LOWER LEG & FOOT)",
            "- ➕ Plus → Section F (CORE), Section J (OLYMPIC LIFTS & DERIVATIVES), Section K (PLYOMETRICS), Section L (KETTLEBELL), Section Q (STRONGMAN)",
            "- ➖ Ultra → Section M (CARDIO & CONDITIONING), Section O (FOOTWORK & AGILITY), Section N (SPORT FOCUSED), Section K (PLYOMETRICS)",
            "",
            "### Exercise Mapping (Primary exercise in 🧈 / 🎱 by zip)",
            *mapping_lines,
            "",
            "## 5) Zip Identity Lines",
            *zip_lines,
            "",
        ]
    )


def missing_decks() -> list[int]:
    missing = []
    for deck in range(1, 43):
        if not (OUTPUT_DIR / f"deck-{deck:02d}-identity.md").exists():
            missing.append(deck)
    return missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deck identity scaffolds.")
    parser.add_argument("deck_numbers", nargs="*", type=int, help="Deck number(s) to scaffold")
    parser.add_argument("--missing", action="store_true", help="Scaffold only missing deck identity files")
    parser.add_argument("--top", type=int, default=3, help="Selector candidates to consider per zip")
    parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing identity files")
    args = parser.parse_args()

    targets = args.deck_numbers
    if args.missing:
        targets = sorted(set(targets + missing_decks()))
    if not targets:
        print("No deck targets provided.")
        return

    registry = load_registry()
    exercise_registry = load_exercise_registry()

    for deck_number in targets:
        out_path = OUTPUT_DIR / f"deck-{deck_number:02d}-identity.md"
        if out_path.exists() and not args.overwrite:
            print(f"Skip existing {out_path.relative_to(ROOT)} (use --overwrite)")
            continue

        head, deck_rows = build_deck_context(deck_number, registry)
        assignments = assign_primary_exercises(deck_rows, exercise_registry, top=args.top)
        output = format_deck_file(deck_number, head, deck_rows, assignments)
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
