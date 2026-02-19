#!/usr/bin/env python3
"""
PPL± Repository Setup Script
Creates the complete folder structure and all 1,680 stub card files.
Run once from the root of the ppl-plus-ultra repository.
"""

import os

# ============================================================
# SCL DATA TABLES
# ============================================================

ORDERS = [
    ("🐂", "foundation"),
    ("⛽", "strength"),
    ("🦋", "hypertrophy"),
    ("🏟", "performance"),
    ("🌾", "fullbody"),
    ("⚖", "balance"),
    ("🖼", "restoration"),
]

AXES = [
    ("🏛", "basics"),
    ("🔨", "functional"),
    ("🌹", "aesthetic"),
    ("🪐", "challenge"),
    ("⌛", "time"),
    ("🐬", "partner"),
]

TYPES = [
    ("🛒", "push"),
    ("🪡", "pull"),
    ("🍗", "legs"),
    ("➕", "plus"),
    ("➖", "ultra"),
]

COLORS = [
    ("⚫", "teaching"),
    ("🟢", "bodyweight"),
    ("🔵", "structured"),
    ("🟣", "technical"),
    ("🔴", "intense"),
    ("🟠", "circuit"),
    ("🟡", "fun"),
    ("⚪", "mindful"),
]

# ============================================================
# OPERATOR DERIVATION
# Axis x Color polarity -> default operator
# Preparatory colors: ⚫ 🟢 ⚪ 🟡
# Expressive colors:  🔵 🟣 🔴 🟠
# ============================================================

PREPARATORY_COLORS = {"⚫", "🟢", "⚪", "🟡"}

OPERATOR_TABLE = {
    "🏛": {"prep": ("📍", "pono"),    "expr": ("🤌", "facio")},
    "🔨": {"prep": ("🧸", "fero"),    "expr": ("🥨", "tendo")},
    "🌹": {"prep": ("👀", "specio"),  "expr": ("🦢", "plico")},
    "🪐": {"prep": ("🪵", "teneo"),   "expr": ("🚀", "mitto")},
    "⌛": {"prep": ("🐋", "duco"),    "expr": ("✒️", "grapho")},
    "🐬": {"prep": ("🧲", "capio"),   "expr": ("🦉", "logos")},
}

def get_operator(axis_emoji, color_emoji):
    polarity = "prep" if color_emoji in PREPARATORY_COLORS else "expr"
    op_emoji, op_name = OPERATOR_TABLE[axis_emoji][polarity]
    return op_emoji, op_name

# ============================================================
# ORDER PARAMETERS
# Used to populate stub file content
# ============================================================

ORDER_PARAMS = {
    "🐂": {
        "name": "Foundation",
        "load": "<=65%",
        "reps": "8-15",
        "rest": "60-90s",
        "max_diff": "2/5",
        "cns": "Low",
        "duration": "45-60 min",
        "blocks": "♨️ 🔢/🛠 🧈 🧩 🧬 🚂",
        "session_count": "4-6",
    },
    "⛽": {
        "name": "Strength",
        "load": "75-85%",
        "reps": "4-6",
        "rest": "3-4 min",
        "max_diff": "4/5",
        "cns": "High",
        "duration": "55-75 min",
        "blocks": "♨️ ▶️ 🧈 🧩 🪫 🚂",
        "session_count": "5-6",
    },
    "🦋": {
        "name": "Hypertrophy",
        "load": "65-75%",
        "reps": "8-12",
        "rest": "60-90s",
        "max_diff": "3/5",
        "cns": "Moderate",
        "duration": "50-70 min",
        "blocks": "♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂",
        "session_count": "6-7",
    },
    "🏟": {
        "name": "Performance",
        "load": "85-100%+",
        "reps": "1-3",
        "rest": "Full recovery",
        "max_diff": "5/5",
        "cns": "High",
        "duration": "30-50 min",
        "blocks": "♨️ 🪜 🧈 🚂",
        "session_count": "3-4",
    },
    "🌾": {
        "name": "Full Body",
        "load": "~70%",
        "reps": "8-10",
        "rest": "30-90s",
        "max_diff": "3/5",
        "cns": "Moderate",
        "duration": "40-60 min",
        "blocks": "♨️ 🎼 🧈 🧩 🪫 🚂",
        "session_count": "5-6",
    },
    "⚖": {
        "name": "Balance",
        "load": "~70%",
        "reps": "10-12",
        "rest": "90s",
        "max_diff": "3/5",
        "cns": "Moderate",
        "duration": "45-60 min",
        "blocks": "♨️ 🏗 🧈 🧩 🪫 🚂",
        "session_count": "5-6",
    },
    "🖼": {
        "name": "Restoration",
        "load": "<=55%",
        "reps": "12-15",
        "rest": "60s",
        "max_diff": "2/5",
        "cns": "Low",
        "duration": "35-55 min",
        "blocks": "🎯 🪫 🧈 🧬 🚂",
        "session_count": "4-5",
    },
}

# ============================================================
# AXIS PARAMETERS
# ============================================================

AXIS_PARAMS = {
    "🏛": {
        "name": "Basics",
        "character": "Bilateral, stable, barbell-first classics. Compound over isolation.",
        "priority": "Barbell > dumbbell. Bilateral > unilateral. Classic > novel.",
    },
    "🔨": {
        "name": "Functional",
        "character": "Unilateral, standing, athletic-transfer movements.",
        "priority": "Unilateral > bilateral. Standing > seated. Free weight > machine.",
    },
    "🌹": {
        "name": "Aesthetic",
        "character": "Isolation, full ROM, mind-muscle connection. Feel over load.",
        "priority": "Isolation > compound. Cable/machine > barbell. Feeling > load.",
    },
    "🪐": {
        "name": "Challenge",
        "character": "Hardest variation at any level. Deficit, pause, tempo, bands.",
        "priority": "Hardest controllable variation always. Scales to individual.",
    },
    "⌛": {
        "name": "Time",
        "character": "Clock as training variable. EMOM, AMRAP, density, timed sets.",
        "priority": "Time-manipulable exercises first. Protocol from Order x Color.",
    },
    "🐬": {
        "name": "Partner",
        "character": "Social training context. Spottable, alternating, teachable.",
        "priority": "Partner-viable exercises first. Machine work deprioritized.",
    },
}

# ============================================================
# TYPE PARAMETERS
# ============================================================

TYPE_PARAMS = {
    "🛒": {
        "name": "Push",
        "muscles": "Chest, front delts, triceps",
        "patterns": "Horizontal press, vertical press",
    },
    "🪡": {
        "name": "Pull",
        "muscles": "Lats, rear delts, biceps, traps, erectors",
        "patterns": "Row, pulldown, hinge",
    },
    "🍗": {
        "name": "Legs",
        "muscles": "Quads, hamstrings, glutes, calves",
        "patterns": "Squat, lunge, hinge, isolation",
    },
    "➕": {
        "name": "Plus",
        "muscles": "Full body power, core",
        "patterns": "Olympic lifts, loaded carries, plyometrics, anti-rotation",
    },
    "➖": {
        "name": "Ultra",
        "muscles": "Cardiovascular system",
        "patterns": "Rowing, cycling, running, conditioning, mobility flows",
    },
}

# ============================================================
# COLOR PARAMETERS
# ============================================================

COLOR_PARAMS = {
    "⚫": {
        "name": "Teaching",
        "tier": "2-3",
        "gold": "No",
        "character": "Extra rest, coaching cues, comprehension over exertion.",
    },
    "🟢": {
        "name": "Bodyweight",
        "tier": "0-2",
        "gold": "No",
        "character": "No gym required. Park, hotel, living room.",
    },
    "🔵": {
        "name": "Structured",
        "tier": "2-3",
        "gold": "No",
        "character": "Prescribed sets/reps/rest. Trackable and repeatable.",
    },
    "🟣": {
        "name": "Technical",
        "tier": "2-5",
        "gold": "Yes",
        "character": "Precision. Lower volume, extended rest, quality focus.",
    },
    "🔴": {
        "name": "Intense",
        "tier": "2-4",
        "gold": "Yes",
        "character": "Maximum effort. High volume. Reduced rest. Supersets OK.",
    },
    "🟠": {
        "name": "Circuit",
        "tier": "0-3",
        "gold": "No",
        "character": "Station-based timed rotation. No barbells. Loop logic required.",
    },
    "🟡": {
        "name": "Fun",
        "tier": "0-5",
        "gold": "No",
        "character": "Exploration and variety. Structured play within constraints.",
    },
    "⚪": {
        "name": "Mindful",
        "tier": "0-3",
        "gold": "No",
        "character": "Slow tempo (4s eccentrics). Extended rest (2+ min). Breathing cues.",
    },
}

# ============================================================
# DECK NUMBER LOOKUP
# Order row x Axis column -> deck number (01-42)
# ============================================================

def get_deck_number(order_emoji, axis_emoji):
    order_index = [o[0] for o in ORDERS].index(order_emoji)
    axis_index = [a[0] for a in AXES].index(axis_emoji)
    return (order_index * 6) + axis_index + 1

# ============================================================
# STUB FILE CONTENT GENERATOR
# ============================================================

def generate_stub_content(order_e, axis_e, type_e, color_e):
    op_emoji, op_name = get_operator(axis_e, color_e)
    deck_num = get_deck_number(order_e, axis_e)

    order = ORDER_PARAMS[order_e]
    axis = AXIS_PARAMS[axis_e]
    type_ = TYPE_PARAMS[type_e]
    color = COLOR_PARAMS[color_e]

    zip_code = f"{order_e}{axis_e}{type_e}{color_e}"

    content = f"""---
zip: {zip_code}
operator: {op_emoji} {op_name}
status: EMPTY
deck: {deck_num:02d}
order: {order_e} {order['name']} | {order['load']} | {order['reps']} reps | {order['rest']} | CNS: {order['cns']}
axis: {axis_e} {axis['name']} | {axis['character']}
type: {type_e} {type_['name']} | {type_['muscles']}
color: {color_e} {color['name']} | Tier {color['tier']} | GOLD: {color['gold']} | {color['character']}
blocks: {order['blocks']}
---

This card is unfilled. Generate workout at this address using SCL rules in scl-directory.md.
"""
    return content

# ============================================================
# ROOT FILES
# ============================================================

def create_root_files():
    files = {
        "README.md": "# PPL±\n\nContent pending.\n",
        "whiteboard.md": "# Whiteboard\n\nActive decisions and current phase.\n",
        "scl-directory.md": "# SCL Directory\n\nFull SCL reference. Content pending.\n",
        "exercise-library.md": "# PPL± Exercise Library v.0\n\nContent pending.\n",
    }

    for filename, content in files.items():
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Created: {filename}")
        else:
            print(f"  Exists (skipped): {filename}")

# ============================================================
# MAIN BUILD FUNCTION
# ============================================================

def build_repository():
    print("\n PPL± Repository Setup")
    print("=" * 50)

    # Root files
    print("\n[ Root Files ]")
    create_root_files()

    # Card files
    print("\n[ Card Files ]")
    total_created = 0
    total_skipped = 0

    for order_e, order_slug in ORDERS:
        order_folder = f"cards/{order_e}-{order_slug}"

        for axis_e, axis_slug in AXES:
            axis_folder = f"{order_folder}/{axis_e}-{axis_slug}"

            for type_e, type_slug in TYPES:
                type_folder = f"{axis_folder}/{type_e}-{type_slug}"

                # Create folder path
                os.makedirs(type_folder, exist_ok=True)

                for color_e, color_slug in COLORS:
                    zip_code = f"{order_e}{axis_e}{type_e}{color_e}"
                    filename = f"{zip_code}\u00b1.md"
                    filepath = os.path.join(type_folder, filename)

                    if not os.path.exists(filepath):
                        content = generate_stub_content(
                            order_e, axis_e, type_e, color_e
                        )
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        total_created += 1
                    else:
                        total_skipped += 1

    print(f"\n  Files created: {total_created}")
    print(f"  Files skipped (already exist): {total_skipped}")
    print(f"  Total card files: {total_created + total_skipped}")

    # Summary
    print("\n[ Summary ]")
    print(f"  Orders:  {len(ORDERS)}")
    print(f"  Axes:    {len(AXES)}")
    print(f"  Types:   {len(TYPES)}")
    print(f"  Colors:  {len(COLORS)}")
    print(f"  Expected files: {len(ORDERS) * len(AXES) * len(TYPES) * len(COLORS)}")
    print(f"  Folders created: {len(ORDERS)} orders x {len(AXES)} axes x {len(TYPES)} types")
    print(f"  = {len(ORDERS) * len(AXES) * len(TYPES)} type-level folders")

    print("\n" + "=" * 50)
    print("  Repository structure complete.")
    print("  Populate CLAUDE.md, scl-directory.md, and exercise-library.md")
    print("  before beginning workout generation.")
    print("  Status: EMPTY across all 1,680 cards.")
    print("  🧮\n")

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    build_repository()
