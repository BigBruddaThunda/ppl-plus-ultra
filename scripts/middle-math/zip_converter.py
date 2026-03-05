#!/usr/bin/env python3
"""Utilities for converting between emoji and numeric PPL± zip codes."""

from __future__ import annotations

import argparse
from typing import Dict, Tuple

ORDERS: Dict[int, Tuple[str, str, str]] = {
    1: ("🐂", "Foundation", "foundation"),
    2: ("⛽", "Strength", "strength"),
    3: ("🦋", "Hypertrophy", "hypertrophy"),
    4: ("🏟", "Performance", "performance"),
    5: ("🌾", "Full Body", "full-body"),
    6: ("⚖", "Balance", "balance"),
    7: ("🖼", "Restoration", "restoration"),
}

AXES: Dict[int, Tuple[str, str, str]] = {
    1: ("🏛", "Basics", "basics"),
    2: ("🔨", "Functional", "functional"),
    3: ("🌹", "Aesthetic", "aesthetic"),
    4: ("🪐", "Challenge", "challenge"),
    5: ("⌛", "Time", "time"),
    6: ("🐬", "Partner", "partner"),
}

TYPES: Dict[int, Tuple[str, str, str]] = {
    1: ("🛒", "Push", "push"),
    2: ("🪡", "Pull", "pull"),
    3: ("🍗", "Legs", "legs"),
    4: ("➕", "Plus", "plus"),
    5: ("➖", "Ultra", "ultra"),
}

COLORS: Dict[int, Tuple[str, str, str]] = {
    1: ("⚫", "Teaching", "teaching"),
    2: ("🟢", "Bodyweight", "bodyweight"),
    3: ("🔵", "Structured", "structured"),
    4: ("🟣", "Technical", "technical"),
    5: ("🔴", "Intense", "intense"),
    6: ("🟠", "Circuit", "circuit"),
    7: ("🟡", "Fun", "fun"),
    8: ("⚪", "Mindful", "mindful"),
}

PREPARATORY_COLORS = {"⚫", "🟢", "⚪", "🟡"}
EXPRESSIVE_COLORS = {"🔵", "🟣", "🔴", "🟠"}

OPERATOR_TABLE: Dict[str, Tuple[Tuple[str, str], Tuple[str, str]]] = {
    "🏛": (("📍", "pono"), ("🤌", "facio")),
    "🔨": (("🧸", "fero"), ("🥨", "tendo")),
    "🌹": (("👀", "specio"), ("🪢", "plico")),
    "🪐": (("🪵", "teneo"), ("🏹", "mitto")),
    "⌛": (("🎻", "duco"), ("✍️", "grapho")),
    "🐬": (("🫴", "capio"), ("🧿", "logos")),
}


def _emoji_to_position(table: Dict[int, Tuple[str, str, str]]) -> Dict[str, int]:
    return {emoji: position for position, (emoji, _, _) in table.items()}


ORDER_BY_EMOJI = _emoji_to_position(ORDERS)
AXIS_BY_EMOJI = _emoji_to_position(AXES)
TYPE_BY_EMOJI = _emoji_to_position(TYPES)
COLOR_BY_EMOJI = _emoji_to_position(COLORS)


def emoji_to_numeric(emoji_zip: str) -> str:
    chars = list(emoji_zip)
    if len(chars) != 4:
        raise ValueError("emoji zip must contain exactly 4 emojis")

    try:
        order = ORDER_BY_EMOJI[chars[0]]
    except KeyError as exc:
        raise ValueError(f"invalid order emoji: {chars[0]}") from exc
    try:
        axis = AXIS_BY_EMOJI[chars[1]]
    except KeyError as exc:
        raise ValueError(f"invalid axis emoji: {chars[1]}") from exc
    try:
        type_position = TYPE_BY_EMOJI[chars[2]]
    except KeyError as exc:
        raise ValueError(f"invalid type emoji: {chars[2]}") from exc
    try:
        color = COLOR_BY_EMOJI[chars[3]]
    except KeyError as exc:
        raise ValueError(f"invalid color emoji: {chars[3]}") from exc

    return f"{order}{axis}{type_position}{color}"


def _validate_numeric_or_raise(numeric_zip: str) -> None:
    if len(numeric_zip) != 4 or not numeric_zip.isdigit():
        raise ValueError("numeric zip must be exactly 4 digits")
    ranges = ((1, 7), (1, 6), (1, 5), (1, 8))
    labels = ("order", "axis", "type", "color")
    for idx, (label, (low, high)) in enumerate(zip(labels, ranges)):
        digit = int(numeric_zip[idx])
        if not low <= digit <= high:
            raise ValueError(f"{label} {digit} out of range {low}-{high}")


def numeric_to_emoji(numeric_zip: str) -> str:
    _validate_numeric_or_raise(numeric_zip)
    order, axis, type_position, color = (int(ch) for ch in numeric_zip)
    return (
        f"{ORDERS[order][0]}{AXES[axis][0]}"
        f"{TYPES[type_position][0]}{COLORS[color][0]}"
    )


def validate_zip(zip_str: str) -> bool:
    try:
        if zip_str.isdigit():
            _validate_numeric_or_raise(zip_str)
        else:
            emoji_to_numeric(zip_str)
    except ValueError:
        return False
    return True


def zip_to_deck(zip_str: str) -> int:
    numeric = zip_str if zip_str.isdigit() else emoji_to_numeric(zip_str)
    _validate_numeric_or_raise(numeric)
    order = int(numeric[0])
    axis = int(numeric[1])
    return (order - 1) * 6 + axis


def zip_to_path(emoji_zip: str) -> str:
    numeric = emoji_to_numeric(emoji_zip)
    order, axis, type_position = (int(numeric[0]), int(numeric[1]), int(numeric[2]))
    order_emoji, _, order_slug = ORDERS[order]
    axis_emoji, _, axis_slug = AXES[axis]
    type_emoji, _, type_slug = TYPES[type_position]
    return f"cards/{order_emoji}-{order_slug}/{axis_emoji}-{axis_slug}/{type_emoji}-{type_slug}/"


def derive_operator(emoji_zip: str) -> tuple[str, str]:
    chars = list(emoji_zip)
    if len(chars) != 4:
        raise ValueError("emoji zip must contain exactly 4 emojis")
    axis_emoji = chars[1]
    color_emoji = chars[3]

    if axis_emoji not in OPERATOR_TABLE:
        raise ValueError(f"invalid axis emoji: {axis_emoji}")
    if color_emoji not in COLOR_BY_EMOJI:
        raise ValueError(f"invalid color emoji: {color_emoji}")

    preparatory, expressive = OPERATOR_TABLE[axis_emoji]
    if color_emoji in PREPARATORY_COLORS:
        return preparatory
    if color_emoji in EXPRESSIVE_COLORS:
        return expressive
    raise ValueError(f"unable to derive polarity for color: {color_emoji}")


def _invalid_reason(zip_str: str) -> str:
    try:
        if zip_str.isdigit():
            _validate_numeric_or_raise(zip_str)
        else:
            emoji_to_numeric(zip_str)
    except ValueError as exc:
        return str(exc)
    return ""


def _run_convert(value: str) -> None:
    if value.isdigit():
        numeric = value
        emoji = numeric_to_emoji(numeric)
        print(f"emoji={emoji}", end=", ")
    else:
        emoji = value
        numeric = emoji_to_numeric(emoji)
        print(f"numeric={numeric}", end=", ")

    deck = zip_to_deck(numeric)
    operator_emoji, operator_name = derive_operator(emoji)
    path = zip_to_path(emoji)
    print(f"deck={deck:02d}, operator={operator_emoji} {operator_name}, path={path}")


def _run_validate(value: str) -> None:
    if validate_zip(value):
        print("VALID")
    else:
        print(f"INVALID ({_invalid_reason(value)})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert and validate PPL± zip codes")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--convert", help="Convert an emoji or numeric zip code")
    group.add_argument("--validate", help="Validate an emoji or numeric zip code")
    args = parser.parse_args()

    if args.convert:
        _run_convert(args.convert)
    if args.validate:
        _run_validate(args.validate)


if __name__ == "__main__":
    main()
