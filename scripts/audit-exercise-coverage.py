#!/usr/bin/env python3
"""
audit-exercise-coverage.py — PPL± Duplicate Primary Exercise Detector
Usage: python scripts/audit-exercise-coverage.py cards/⛽-strength/🔨-functional/

For a given deck folder (one Order×Axis combination), checks that no two
Color variants of the same Type share the same primary exercise in 🧈 Bread & Butter.
"""

import sys
import os
import re
from collections import defaultdict

# ── SCL Emoji Sets ──────────────────────────────────────────────────────────
TYPES = ['🛒', '🪡', '🍗', '➕', '➖']
TYPE_NAMES = {
    '🛒': 'Push',
    '🪡': 'Pull',
    '🍗': 'Legs',
    '➕': 'Plus',
    '➖': 'Ultra',
}
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']
COLOR_NAMES = {
    '⚫': 'Teaching',
    '🟢': 'Bodyweight',
    '🔵': 'Structured',
    '🟣': 'Technical',
    '🔴': 'Intense',
    '🟠': 'Circuit',
    '🟡': 'Fun',
    '⚪': 'Mindful',
}


# ── Frontmatter parser ────────────────────────────────────────────────────────
def parse_frontmatter(content):
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, content

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None, content

    fm = {}
    for line in lines[1:end_idx]:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()

    body = '\n'.join(lines[end_idx + 1:])
    return fm, body


def parse_zip_type_color(zip_str):
    """Extract type (position 3) and color (position 4) from zip."""
    ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
    AXES   = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']

    s = zip_str.strip()

    # Consume order
    for o in ORDERS:
        if s.startswith(o):
            s = s[len(o):]
            break

    # Consume axis
    for a in AXES:
        if s.startswith(a):
            s = s[len(a):]
            break

    # Extract type
    type_emoji = None
    for t in TYPES:
        if s.startswith(t):
            type_emoji = t
            s = s[len(t):]
            break

    # Extract color
    color_emoji = None
    for c in COLORS:
        if s.startswith(c):
            color_emoji = c
            break

    return type_emoji, color_emoji


def extract_bread_butter_block(body):
    """
    Extract the content of the 🧈 Bread & Butter block from the card body.
    Returns the lines of the block until the next block header.
    """
    lines = body.split('\n')
    in_bb = False
    bb_lines = []

    for line in lines:
        stripped = line.strip()

        # Check if this is a block header
        is_header = stripped.startswith('#')

        if is_header and '🧈' in stripped:
            in_bb = True
            continue

        if in_bb:
            # Stop at next block header
            if is_header and any(
                e in stripped for e in [
                    '♨️', '🎯', '🔢', '🫀', '▶️', '🎼', '♟️', '🪜',
                    '🌎', '🎱', '🌋', '🪞', '🗿', '🛠', '🧩', '🪫',
                    '🏖', '🏗', '🧬', '🚂', '🔠'
                ]
            ):
                break
            bb_lines.append(line)

    return '\n'.join(bb_lines)


def extract_primary_exercise(bb_content):
    """
    Extract the first exercise name from 🧈 block content.
    Looks for:
    1. Lines matching "[number] [type-emoji] [exercise name]" pattern
    2. Lines starting with "**A." or "**1." bold headers (exercise names in table format)
    3. Barbell/exercise names in bold
    """
    if not bb_content.strip():
        return None

    type_emoji_pattern = '(?:🛒|🪡|🍗|➕|➖)'

    # Pattern 1: "10 🍗 Squat"
    p1 = re.compile(
        r'^\s*[-*•]?\s*\d+\s+' + type_emoji_pattern + r'\s+(.+?)(?:\s*\(.*\))?\s*$'
    )

    # Pattern 2: "**A. Exercise Name**" or "**Exercise Name**"
    p2 = re.compile(r'^\*\*[A-Z][\.\)]\s+(.+?)\*\*')

    # Pattern 3: Bold header "**Exercise Name**" on its own line
    p3 = re.compile(r'^\*\*([^*]+)\*\*\s*$')

    # Pattern 4: Table row that has an exercise name as first cell after |
    p4 = re.compile(r'^\|\s*\d+\s*\|\s*(.+?)\s*\|')

    for line in bb_content.split('\n'):
        stripped = line.strip()

        m = p1.match(stripped)
        if m:
            name = re.sub(r'\s*\(.*?\)\s*$', '', m.group(1)).strip()
            if name and len(name) > 2:
                return name

        m = p2.match(stripped)
        if m:
            name = m.group(1).strip()
            if name and len(name) > 2:
                return name

    # Second pass: look for first bold name or first markdown header that's an exercise
    for line in bb_content.split('\n'):
        stripped = line.strip()

        m = p3.match(stripped)
        if m:
            name = m.group(1).strip()
            # Filter out block-level names like "Bread & Butter"
            if name and len(name) > 5 and 'bread' not in name.lower() and 'butter' not in name.lower():
                return name

    # Third pass: any line with a type emoji
    type_emojis = ['🛒', '🪡', '🍗', '➕', '➖']
    for line in bb_content.split('\n'):
        stripped = line.strip()
        for te in type_emojis:
            if te in stripped:
                # Extract name after emoji
                idx = stripped.find(te)
                after = stripped[idx + len(te):].strip()
                # Clean up
                name = re.sub(r'^\s*[-×x]\s*\d+.*$', '', after).strip()
                name = re.sub(r'\s*\(.*?\)\s*$', '', name).strip()
                if name and len(name) > 3:
                    return name

    return None


# ── Main ─────────────────────────────────────────────────────────────────────
def audit(deck_path):
    if not os.path.exists(deck_path):
        print(f"ERROR: Directory not found: {deck_path}")
        sys.exit(1)

    print(f"Auditing exercise coverage: {deck_path}")
    print("════════════════════════════════════════")

    # Group cards by type
    # type_emoji -> list of (color_emoji, filename, primary_exercise)
    by_type = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(deck_path):
        for fname in sorted(filenames):
            if not fname.endswith('.md'):
                continue
            if fname == 'AGENTS.md':
                continue

            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"  ⚠️  Could not read {fname}: {e}")
                continue

            fm, body = parse_frontmatter(content)
            if fm is None:
                continue

            status = fm.get('status', '').strip()
            if status == 'EMPTY':
                continue  # Skip stubs

            zip_str = fm.get('zip', '').strip()
            if not zip_str:
                continue

            type_emoji, color_emoji = parse_zip_type_color(zip_str)
            if not type_emoji or not color_emoji:
                continue

            bb_content = extract_bread_butter_block(body)
            primary = extract_primary_exercise(bb_content)

            by_type[type_emoji].append((color_emoji, fname, primary))

    if not by_type:
        print("No generated cards found in this deck folder.")
        sys.exit(0)

    # Check for duplicates within each type
    all_ok = True

    for type_emoji in TYPES:
        cards = by_type.get(type_emoji, [])
        if not cards:
            continue

        type_name = TYPE_NAMES.get(type_emoji, type_emoji)
        print(f"\n{type_emoji} {type_name}:")

        # Map primary exercise -> list of colors that use it
        exercise_to_colors = defaultdict(list)
        for color_emoji, fname, primary in cards:
            color_name = COLOR_NAMES.get(color_emoji, color_emoji)
            print(f"  {color_emoji} {color_name:<12} — {primary or '(could not extract)'}")
            if primary:
                exercise_to_colors[primary.lower()].append((color_emoji, color_name))

        # Find duplicates
        for exercise, colors in exercise_to_colors.items():
            if len(colors) > 1:
                color_list = ' and '.join(f"{c[0]} {c[1]}" for c in colors)
                print(f"\n  ❌ DUPLICATE: '{exercise}' used in both {color_list}")
                all_ok = False

    print()
    if all_ok:
        print(f"✅ No duplicate primary exercises in {deck_path}")
        sys.exit(0)
    else:
        print(f"❌ Duplicate primary exercises found — see details above")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/audit-exercise-coverage.py <deck-folder-path>")
        sys.exit(1)

    audit(sys.argv[1])
