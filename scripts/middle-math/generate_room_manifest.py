#!/usr/bin/env python3
"""
scripts/middle-math/generate_room_manifest.py
CX-26: Operis Room Manifest Generator

Given a date, derives the 13-room Operis Sandbox:
  Set A — 8 Color siblings (deterministic from rotation engine)
  Set B — 5 Content Room placeholders (editorial, unique Type + Axis)

Rotation engine (from seeds/operis-sandbox-structure.md):
  Order  = weekday (Mon=🐂, Tue=⛽, Wed=🦋, Thu=🏟, Fri=🌾, Sat=⚖, Sun=🖼)
  Type   = 5-day rolling cycle from Jan 1 of the input date's year
           (🛒 → 🪡 → 🍗 → ➕ → ➖ → repeat)
  Axis   = monthly operator (month 1=🏛 cycling through 6 axes)

Output: JSON manifest with date, derived dials, 8 sibling zips, 5 content rooms.

Usage:
    python scripts/middle-math/generate_room_manifest.py --date 2026-03-06
    python scripts/middle-math/generate_room_manifest.py --week 2026-03-06
    python scripts/middle-math/generate_room_manifest.py --date 2026-03-06 --output text
"""

import json
import sys
import argparse
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT     = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"

# ---------------------------------------------------------------------------
# Rotation engine constants
# ---------------------------------------------------------------------------

# Weekday → Order emoji (Monday=0 in Python's weekday())
WEEKDAY_TO_ORDER = {
    0: "🐂",  # Monday    — Foundation
    1: "⛽",  # Tuesday   — Strength
    2: "🦋",  # Wednesday — Hypertrophy
    3: "🏟",  # Thursday  — Performance
    4: "🌾",  # Friday    — Full Body
    5: "⚖",  # Saturday  — Balance
    6: "🖼",  # Sunday    — Restoration
}

# 5-day rolling Type cycle starting from Jan 1 of each year
TYPE_CYCLE = ["🛒", "🪡", "🍗", "➕", "➖"]

# 6-month rolling Axis cycle (repeats: Jan=🏛, Feb=🔨, ..., Jul=🏛, ...)
MONTH_TO_AXIS = {
    1:  "🏛",   # January
    2:  "🔨",   # February
    3:  "🌹",   # March
    4:  "🪐",   # April
    5:  "⌛",   # May
    6:  "🐬",   # June
    7:  "🏛",   # July
    8:  "🔨",   # August
    9:  "🌹",   # September
    10: "🪐",   # October
    11: "⌛",   # November
    12: "🐬",   # December
}

# All 8 Color emojis in canonical order
COLORS_ALL = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

# Color names
COLOR_NAMES = {
    "⚫": "Teaching",
    "🟢": "Bodyweight",
    "🔵": "Structured",
    "🟣": "Technical",
    "🔴": "Intense",
    "🟠": "Circuit",
    "🟡": "Fun",
    "⚪": "Mindful",
}

# SCL name lookups
ORDER_NAMES = {
    "🐂": "Foundation", "⛽": "Strength", "🦋": "Hypertrophy",
    "🏟": "Performance", "🌾": "Full Body", "⚖": "Balance", "🖼": "Restoration",
}
AXIS_NAMES = {
    "🏛": "Basics", "🔨": "Functional", "🌹": "Aesthetic",
    "🪐": "Challenge", "⌛": "Time", "🐬": "Partner",
}
TYPE_NAMES = {
    "🛒": "Push", "🪡": "Pull", "🍗": "Legs", "➕": "Plus", "➖": "Ultra",
}

# Numeric position maps (for zip code construction)
ORDER_POS  = {"🐂": 1, "⛽": 2, "🦋": 3, "🏟": 4, "🌾": 5, "⚖": 6, "🖼": 7}
AXIS_POS   = {"🏛": 1, "🔨": 2, "🌹": 3, "🪐": 4, "⌛": 5, "🐬": 6}
TYPE_POS   = {"🛒": 1, "🪡": 2, "🍗": 3, "➕": 4, "➖": 5}
COLOR_POS  = {"⚫": 1, "🟢": 2, "🔵": 3, "🟣": 4, "🔴": 5, "🟠": 6, "🟡": 7, "⚪": 8}

# All 5 types in a list for content room derivation
ALL_TYPES = ["🛒", "🪡", "🍗", "➕", "➖"]
# All 6 axes in a list for content room derivation
ALL_AXES  = ["🏛", "🔨", "🌹", "🪐", "⌛", "🐬"]


# ---------------------------------------------------------------------------
# Rotation engine
# ---------------------------------------------------------------------------

def derive_order(d: date) -> str:
    """Derive Order emoji from weekday."""
    return WEEKDAY_TO_ORDER[d.weekday()]


def derive_type(d: date) -> str:
    """Derive Type emoji from 5-day rolling cycle anchored to Jan 1 of year."""
    jan1 = date(d.year, 1, 1)
    day_of_year = (d - jan1).days  # 0-indexed
    return TYPE_CYCLE[day_of_year % 5]


def derive_axis(d: date) -> str:
    """Derive Axis emoji from monthly operator cycle."""
    return MONTH_TO_AXIS[d.month]


def make_numeric_zip(order_e: str, axis_e: str, type_e: str, color_e: str) -> str:
    """Construct 4-digit numeric zip string."""
    return (
        f"{ORDER_POS[order_e]}"
        f"{AXIS_POS[axis_e]}"
        f"{TYPE_POS[type_e]}"
        f"{COLOR_POS[color_e]}"
    )


def make_emoji_zip(order_e: str, axis_e: str, type_e: str, color_e: str) -> str:
    return f"{order_e}{axis_e}{type_e}{color_e}"


# ---------------------------------------------------------------------------
# Manifest generation
# ---------------------------------------------------------------------------

def generate_manifest(d: date, registry_lookup: dict | None = None) -> dict:
    """
    Generate the 13-room Operis Sandbox manifest for a given date.

    Set A: 8 Color siblings — same Order × Axis × Type, one per Color.
    Set B: 5 Content Rooms — editorial placeholders with unique Types and Axes.

    Args:
        d:               The date to generate the manifest for.
        registry_lookup: Optional lookup dict for validating zips exist.

    Returns:
        A dict with the full manifest.
    """
    order_e = derive_order(d)
    axis_e  = derive_axis(d)
    type_e  = derive_type(d)

    # Set A: 8 Color siblings
    siblings = []
    for color_e in COLORS_ALL:
        numeric_zip = make_numeric_zip(order_e, axis_e, type_e, color_e)
        emoji_zip   = make_emoji_zip(order_e, axis_e, type_e, color_e)
        gold_eligible = color_e in {"🔴", "🟣"}

        # Validate zip exists in registry if provided
        exists = True
        if registry_lookup:
            exists = numeric_zip in registry_lookup

        siblings.append({
            "numeric_zip":    numeric_zip,
            "emoji_zip":      emoji_zip,
            "order":          {"emoji": order_e, "name": ORDER_NAMES.get(order_e, "")},
            "axis":           {"emoji": axis_e,  "name": AXIS_NAMES.get(axis_e,  "")},
            "type":           {"emoji": type_e,  "name": TYPE_NAMES.get(type_e,  "")},
            "color":          {"emoji": color_e, "name": COLOR_NAMES.get(color_e, "")},
            "gold_eligible":  gold_eligible,
            "registry_valid": exists,
        })

    # Set B: 5 Content Rooms
    # Use the 4 unused Types (the 4 not used by siblings)
    # and the 5 unused Axes (the 5 not used by siblings)
    unused_types = [t for t in ALL_TYPES if t != type_e]   # 4 types
    unused_axes  = [a for a in ALL_AXES  if a != axis_e]   # 5 axes

    content_rooms = []
    for i, unused_axis in enumerate(unused_axes):
        # Rotate through unused types; one axis gets repeated Type (cycling)
        content_type_e = unused_types[i % len(unused_types)]
        # Content room Color is editorially undefined — placeholder
        content_rooms.append({
            "slot":       i + 1,
            "type":       {"emoji": content_type_e, "name": TYPE_NAMES.get(content_type_e, "")},
            "axis":       {"emoji": unused_axis,    "name": AXIS_NAMES.get(unused_axis, "")},
            "color":      None,   # Editorially selected — not derived
            "note": (
                "Editorial Content Room. Color is assigned by the Operis Editor "
                "based on content character. Zip is finalized when Color is set."
            ),
        })

    return {
        "date":          d.isoformat(),
        "weekday":       d.strftime("%A"),
        "derived_dials": {
            "order": {"emoji": order_e, "name": ORDER_NAMES.get(order_e, "")},
            "axis":  {"emoji": axis_e,  "name": AXIS_NAMES.get(axis_e,  "")},
            "type":  {"emoji": type_e,  "name": TYPE_NAMES.get(type_e,  "")},
        },
        "sandbox": {
            "set_a_siblings":      siblings,
            "set_b_content_rooms": content_rooms,
            "total_rooms":         len(siblings) + len(content_rooms),
        },
    }


def generate_week_batch(start_date: date, registry_lookup: dict | None = None) -> list:
    """Generate manifests for 7 consecutive days starting from start_date."""
    return [
        generate_manifest(start_date + timedelta(days=i), registry_lookup)
        for i in range(7)
    ]


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_manifest_text(manifest: dict) -> str:
    """Human-readable text output for a manifest."""
    lines = []
    d = manifest["derived_dials"]
    sb = manifest["sandbox"]

    lines.append("\n" + "═" * 60)
    lines.append(f"  Operis Sandbox — {manifest['date']} ({manifest['weekday']})")
    lines.append(f"  Order: {d['order']['emoji']} {d['order']['name']}")
    lines.append(f"  Axis:  {d['axis']['emoji']} {d['axis']['name']}")
    lines.append(f"  Type:  {d['type']['emoji']} {d['type']['name']}")
    lines.append("─" * 60)

    lines.append(f"\n  Set A — 8 Color Siblings:")
    for s in sb["set_a_siblings"]:
        gold = " [GOLD]" if s["gold_eligible"] else ""
        valid = "" if s["registry_valid"] else " [NOT IN REGISTRY]"
        lines.append(
            f"    {s['emoji_zip']} ({s['numeric_zip']})  "
            f"{s['color']['emoji']} {s['color']['name']}{gold}{valid}"
        )

    lines.append(f"\n  Set B — 5 Content Rooms (editorial):")
    for r in sb["set_b_content_rooms"]:
        lines.append(
            f"    Slot {r['slot']}: {r['type']['emoji']} {r['type']['name']} "
            f"× {r['axis']['emoji']} {r['axis']['name']}  (Color: TBD)"
        )

    lines.append(f"\n  Total rooms: {sb['total_rooms']} (8 siblings + 5 content)")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CX-26: PPL± Operis Room Manifest Generator"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--date", type=str,
                       help="Single date (YYYY-MM-DD)")
    group.add_argument("--week", type=str,
                       help="7-day batch starting from date (YYYY-MM-DD)")

    parser.add_argument("--output", choices=["json", "text"], default="text",
                        help="Output format (default: text)")
    parser.add_argument("--no-validate", action="store_true",
                        help="Skip registry validation (faster)")

    args = parser.parse_args()

    # Load registry for validation
    registry_lookup = None
    if not args.no_validate and REGISTRY_PATH.exists():
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        registry_lookup = {e["numeric_zip"]: e for e in registry}

    try:
        if args.date:
            d = date.fromisoformat(args.date)
            manifest = generate_manifest(d, registry_lookup)
            if args.output == "json":
                print(json.dumps(manifest, ensure_ascii=False, indent=2))
            else:
                print(format_manifest_text(manifest))

        else:  # --week
            d = date.fromisoformat(args.week)
            manifests = generate_week_batch(d, registry_lookup)
            if args.output == "json":
                print(json.dumps(manifests, ensure_ascii=False, indent=2))
            else:
                for m in manifests:
                    print(format_manifest_text(m))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
