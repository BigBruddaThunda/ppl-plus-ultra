#!/usr/bin/env python3
"""Generate deck identity scaffolds from zip registry and exercise library."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "middle-math" / "zip-registry.json"
EXERCISE_LIBRARY_PATH = ROOT / "exercise-library.md"
OUTPUT_DIR = ROOT / "deck-identities"

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


def load_registry() -> list[dict]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def parse_exercise_sections() -> dict[str, str]:
    text = EXERCISE_LIBRARY_PATH.read_text(encoding="utf-8")
    sections: dict[str, str] = {}
    for match in re.finditer(r"^SECTION\s+([A-Q]):\s+(.+)$", text, flags=re.MULTILINE):
        letter, title = match.groups()
        sections[letter] = title.strip()
    return sections


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


def format_deck_file(deck_number: int, head: dict, deck_rows: list[dict], section_titles: dict[str, str]) -> str:
    order_emoji = head["order"]["emoji"]
    order_name = head["order"]["name"]
    axis_emoji = head["axis"]["emoji"]
    axis_name = head["axis"]["name"]

    title = f"Deck {deck_number:02d} Identity — {order_emoji}{axis_emoji} {order_name} {axis_name}"

    type_counts: dict[str, int] = defaultdict(int)
    zip_lines = []
    for row in deck_rows:
        emoji_zip = row["emoji_zip"]
        type_counts[row["type"]["emoji"]] += 1
        zip_lines.append(
            f"- {emoji_zip} — TODO — requires Claude Code /build-deck-identity session."
        )

    for type_emoji in TYPE_ORDER:
        if type_counts[type_emoji] != 8:
            raise ValueError(
                f"Deck {deck_number:02d} type {type_emoji} expected 8 zips, found {type_counts[type_emoji]}"
            )

    routing_lines = []
    for type_emoji in TYPE_ORDER:
        letters = TYPE_ROUTING[type_emoji]
        section_descriptions = [
            f"Section {letter} ({section_titles.get(letter, 'UNKNOWN')})" for letter in letters
        ]
        routing_lines.append(
            f"- {type_emoji} {TYPE_NAMES[type_emoji]} → {', '.join(section_descriptions)}"
        )

    return "\n".join(
        [
            "---",
            f"deck_number: {deck_number}",
            f"deck_code: \"{order_emoji}{axis_emoji}\"",
            f"order: \"{order_emoji} {order_name}\"",
            f"axis: \"{axis_emoji} {axis_name}\"",
            "status: SCAFFOLD",
            "source_registry: middle-math/zip-registry.json",
            "---",
            "",
            f"# {title}",
            "",
            "## 1) Deck Philosophy",
            "TODO — requires Claude Code /build-deck-identity session.",
            "",
            "## 2) Coverage Map (Type × Color)",
            "| Type \\ Color | ⚫ | 🟢 | 🔵 | 🟣 | 🔴 | 🟠 | 🟡 | ⚪ |",
            "|---|---|---|---|---|---|---|---|---|",
            "| 🛒 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |",
            "| 🪡 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |",
            "| 🍗 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |",
            "| ➕ | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |",
            "| ➖ | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |",
            "",
            "## 3) Color Differentiation Logic",
            "- ⚫ Teaching — TODO — requires Claude Code /build-deck-identity session.",
            "- 🟢 Bodyweight — TODO — requires Claude Code /build-deck-identity session.",
            "- 🔵 Structured — TODO — requires Claude Code /build-deck-identity session.",
            "- 🟣 Technical — TODO — requires Claude Code /build-deck-identity session.",
            "- 🔴 Intense — TODO — requires Claude Code /build-deck-identity session.",
            "- 🟠 Circuit — TODO — requires Claude Code /build-deck-identity session.",
            "- 🟡 Fun — TODO — requires Claude Code /build-deck-identity session.",
            "- ⚪ Mindful — TODO — requires Claude Code /build-deck-identity session.",
            "",
            "## 4) Exercise Section Routing (Type → exercise-library sections)",
            *routing_lines,
            "",
            "### Exercise Mapping Status",
            "TODO — requires Claude Code /build-deck-identity session.",
            "",
            "## 5) Zip Identity Lines",
            *zip_lines,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deck identity scaffolds.")
    parser.add_argument("deck_numbers", nargs="+", type=int, help="Deck number(s) to scaffold")
    args = parser.parse_args()

    registry = load_registry()
    section_titles = parse_exercise_sections()

    for deck_number in args.deck_numbers:
        head, deck_rows = build_deck_context(deck_number, registry)
        output = format_deck_file(deck_number, head, deck_rows, section_titles)
        out_path = OUTPUT_DIR / f"deck-{deck_number:02d}-identity.md"
        out_path.write_text(output, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
