#!/usr/bin/env python3
"""Generate and report on the static zip registry."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from zip_converter import (
    AXES,
    COLORS,
    ORDERS,
    TYPES,
    derive_operator,
    emoji_to_numeric,
    numeric_to_emoji,
    zip_to_deck,
    zip_to_path,
)

OUTPUT_PATH = Path("middle-math/zip-registry.json")


def build_registry() -> list[dict]:
    entries: list[dict] = []
    for order in range(1, 8):
        for axis in range(1, 7):
            for type_position in range(1, 6):
                for color in range(1, 9):
                    numeric_zip = f"{order}{axis}{type_position}{color}"
                    emoji_zip = numeric_to_emoji(numeric_zip)
                    operator_emoji, operator_name = derive_operator(emoji_zip)
                    polarity = "preparatory" if emoji_zip[3] in {"⚫", "🟢", "⚪", "🟡"} else "expressive"
                    entry = {
                        "numeric_zip": numeric_zip,
                        "emoji_zip": emoji_zip,
                        "order": {"position": order, "emoji": ORDERS[order][0], "name": ORDERS[order][1]},
                        "axis": {"position": axis, "emoji": AXES[axis][0], "name": AXES[axis][1]},
                        "type": {
                            "position": type_position,
                            "emoji": TYPES[type_position][0],
                            "name": TYPES[type_position][1],
                        },
                        "color": {"position": color, "emoji": COLORS[color][0], "name": COLORS[color][1]},
                        "deck_number": zip_to_deck(numeric_zip),
                        "operator": {"emoji": operator_emoji, "name": operator_name},
                        "polarity": polarity,
                        "card_path": zip_to_path(emoji_zip),
                        "gold_eligible": COLORS[color][0] in {"🟣", "🔴"},
                    }
                    entries.append(entry)
    return sorted(entries, key=lambda item: item["numeric_zip"])


def write_registry(entries: list[dict]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_registry() -> list[dict]:
    return json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))


def print_stats(entries: list[dict]) -> None:
    total = len(entries)
    by_order = Counter(item["order"]["name"] for item in entries)
    by_axis = Counter(item["axis"]["name"] for item in entries)
    by_type = Counter(item["type"]["name"] for item in entries)
    by_color = Counter(item["color"]["name"] for item in entries)
    by_deck = Counter(item["deck_number"] for item in entries)
    gold_count = sum(1 for item in entries if item["gold_eligible"])
    gold_pct = (gold_count / total) * 100 if total else 0

    print(f"Total zips: {total}")
    print("Zips per Order:")
    for name, count in sorted(by_order.items()):
        print(f"  - {name}: {count}")
    print("Zips per Axis:")
    for name, count in sorted(by_axis.items()):
        print(f"  - {name}: {count}")
    print("Zips per Type:")
    for name, count in sorted(by_type.items()):
        print(f"  - {name}: {count}")
    print("Zips per Color:")
    for name, count in sorted(by_color.items()):
        print(f"  - {name}: {count}")
    print("Zips per Deck:")
    for deck, count in sorted(by_deck.items()):
        print(f"  - Deck {deck:02d}: {count}")
    print(f"GOLD-eligible count: {gold_count}")
    print(f"GOLD-eligible percentage: {gold_pct:.2f}%")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate static registry of all 1,680 zip codes")
    parser.add_argument("--stats", action="store_true", help="Print distribution stats")
    args = parser.parse_args()

    if args.stats:
        entries = load_registry() if OUTPUT_PATH.exists() else build_registry()
        print_stats(entries)
        return

    entries = build_registry()
    write_registry(entries)
    gold_count = sum(1 for item in entries if item["gold_eligible"])
    deck_count = len({item["deck_number"] for item in entries})
    print(f"Generated {len(entries):,} zip codes across {deck_count} decks. {gold_count} GOLD-eligible.")


if __name__ == "__main__":
    main()
