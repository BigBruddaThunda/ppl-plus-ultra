#!/usr/bin/env python3
"""
validate-card.py — PPL± Single Card SCL Validator
Usage: python scripts/validate-card.py <card-path>

Validates a single generated card file against SCL rules defined in CLAUDE.md.
Exits 0 if all checks pass (or card is a stub), exits 1 if any check fails.
"""

import sys
import os
import re

# ── SCL Emoji Sets ──────────────────────────────────────────────────────────
ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES   = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES  = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']

VALID_STATUSES = {'EMPTY', 'GENERATED', 'GENERATED-V2', 'CANONICAL'}

# ── Block Emojis (22) ────────────────────────────────────────────────────────
BLOCK_EMOJIS = [
    '♨️', '🎯', '🔢', '🧈', '🫀', '▶️', '🎼', '♟️', '🪜', '🌎',
    '🎱', '🌋', '🪞', '🗿', '🛠', '🧩', '🪫', '🏖', '🏗', '🧬',
    '🚂', '🔠'
]

# ── Order Block Count Guidelines ─────────────────────────────────────────────
ORDER_BLOCK_COUNTS = {
    '🐂': (4, 6),
    '⛽': (5, 6),
    '🦋': (6, 7),
    '🏟': (3, 4),
    '🌾': (5, 6),
    '⚖': (5, 6),
    '🖼': (4, 5),
}

# ── GOLD indicator keywords (exercise names that require 🔴 or 🟣) ──────────
GOLD_KEYWORDS = [
    'power clean', 'hang clean', 'hang power clean', 'muscle clean',
    'power snatch', 'hang snatch', 'hang power snatch', 'muscle snatch',
    'clean and jerk', 'clean & jerk', 'squat clean', 'split clean',
    'push jerk', 'split jerk', 'push press jerk',
    'log press',
    'box jump', 'depth jump', 'broad jump', 'tuck jump', 'hurdle jump',
    'drop jump', 'bounding', 'triple extension jump',
    'tire flip', 'atlas stone', 'yoke walk', 'zercher carry', 'keg carry',
    'sandbag shouldering', 'keg shouldering', 'atlas stone lift',
]

# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(content):
    """Extract YAML frontmatter from between --- markers."""
    lines = content.split('\n')
    if not lines[0].strip() == '---':
        return None, content

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None, content

    fm_lines = lines[1:end_idx]
    body = '\n'.join(lines[end_idx + 1:])

    fm = {}
    for line in fm_lines:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()

    return fm, body


def parse_zip(zip_str):
    """
    Parse a zip string into (order, axis, type, color).
    Returns None if parsing fails.
    Uses greedy prefix matching against known emoji sets.
    """
    s = zip_str.strip()
    result = []
    sets = [ORDERS, AXES, TYPES, COLORS]

    for emoji_set in sets:
        matched = None
        for emoji in emoji_set:
            if s.startswith(emoji):
                matched = emoji
                s = s[len(emoji):]
                break
        if matched is None:
            return None
        result.append(matched)

    # Should be nothing left
    if s.strip():
        return None

    return tuple(result)


def count_blocks(body):
    """Count block headers in the card body."""
    count = 0
    for line in body.split('\n'):
        line = line.strip()
        if not line.startswith('#'):
            continue
        for emoji in BLOCK_EMOJIS:
            if emoji in line:
                count += 1
                break
    return count


def has_block(body, emoji):
    """Check if a specific block emoji appears as a block header."""
    for line in body.split('\n'):
        line = line.strip()
        if line.startswith('#') and emoji in line:
            return True
    return False


def has_save(body):
    """Check if 🧮 SAVE appears anywhere in the body."""
    return '🧮' in body


def has_intention(body):
    """Check if a 🎯 INTENTION / quoted one-sentence frame appears."""
    # Either a 🎯 block header or a quoted line ("> ...")
    if '🎯' in body:
        return True
    # Also check for a blockquote that could be the intention
    for line in body.split('\n'):
        if line.strip().startswith('>') and len(line.strip()) > 5:
            return True
    return False


def extract_exercises(body):
    """
    Extract exercise names from lines matching the pattern:
    [number] [type-emoji] [exercise name]
    Returns list of exercise name strings.
    Strips load percentages (e.g., "at 60%") from names.
    """
    exercises = []
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    pattern = re.compile(
        r'^\s*[-*•]?\s*\d+\s+' + type_emoji_pattern + r'\s+(.+?)(?:\s*\(.*\))?\s*$'
    )
    for line in body.split('\n'):
        m = pattern.match(line)
        if m:
            name = m.group(1).strip()
            # Clean up trailing parentheticals
            name = re.sub(r'\s*\(.*?\)\s*$', '', name).strip()
            # Strip load references like "at 50%", "at 60%", "× 5", "x 5"
            name = re.sub(r'\s+at\s+\d+(?:\.\d+)?%\s*$', '', name, flags=re.IGNORECASE).strip()
            name = re.sub(r'\s+[×x]\s+\d+\s*$', '', name).strip()
            if name and len(name) > 2:
                exercises.append(name)
    return exercises


def check_against_library(exercises, library_path):
    """
    Check exercise names against exercise-library.md using fuzzy substring matching.
    Returns list of (exercise_name, found) tuples.

    Matching strategy:
    1. Exact substring: "Romanian Deadlift" in library
    2. First 3 words: "Romanian Deadlift (RDL)" matches "Romanian Deadlift"
    3. Strip equipment prefix: "Barbell Deadlift" → try "Deadlift"
    4. Strip variation suffix: "Deadlift (Conventional)" → try "Deadlift"
    """
    if not os.path.exists(library_path):
        return [(e, None) for e in exercises]  # None = library not found

    with open(library_path, 'r', encoding='utf-8') as f:
        library_content = f.read().lower()

    EQUIPMENT_PREFIXES = [
        'barbell', 'dumbbell', 'kettlebell', 'cable', 'machine', 'band',
        'resistance band', 'plate', 'trap bar', 'smith machine', 'ez bar',
        'ez-bar', 'safety bar', 'swiss bar', 'landmine',
    ]

    def fuzzy_match(name):
        name_lower = name.lower().strip()

        # 1. Exact substring
        if name_lower in library_content:
            return True

        # 2. First 3 words
        words = name_lower.split()
        if len(words) >= 3:
            if ' '.join(words[:3]) in library_content:
                return True
        if len(words) >= 2:
            if ' '.join(words[:2]) in library_content:
                return True

        # 3. Strip equipment prefix and try again
        for prefix in EQUIPMENT_PREFIXES:
            if name_lower.startswith(prefix + ' '):
                stripped = name_lower[len(prefix):].strip()
                if stripped in library_content:
                    return True
                # Also try first 2-3 words of stripped
                sw = stripped.split()
                if len(sw) >= 2 and ' '.join(sw[:2]) in library_content:
                    return True

        # 4. Strip parenthetical variation suffix
        clean = re.sub(r'\s*\(.*?\)\s*$', '', name_lower).strip()
        if clean != name_lower and clean in library_content:
            return True

        return False

    return [(exercise, fuzzy_match(exercise)) for exercise in exercises]


def check_gold_violations(body):
    """Check for GOLD exercise names in the body."""
    body_lower = body.lower()
    violations = []
    for keyword in GOLD_KEYWORDS:
        if keyword in body_lower:
            violations.append(keyword)
    return violations


def _get_prescription_lines(body):
    """
    Return lines that appear to be exercise prescriptions:
    - Numbered exercise lines: "10 🍗 Exercise Name"
    - Bold exercise headers: "**A. 🍗 Exercise**" or "**Exercise Name**"
    - Markdown headers that are exercise names (not block headers)
    """
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    numbered = re.compile(r'^\s*[-*•]?\s*\d+\s+' + type_emoji_pattern + r'\s+(.+)')
    bold_hdr = re.compile(r'^\*\*[A-Za-z0-9][\.\)]\s+(.+?)\*\*')
    bold_only = re.compile(r'^\*\*(.+?)\*\*\s*$')

    prescription_lines = []
    for line in body.split('\n'):
        stripped = line.strip()
        if numbered.match(stripped) or bold_hdr.match(stripped) or bold_only.match(stripped):
            prescription_lines.append(stripped.lower())
    return prescription_lines


def _find_barbell_exercises(body):
    """
    Find barbell exercises in prescriptive contexts only.
    Returns list of matched exercise names.
    """
    prescription_lines = _get_prescription_lines(body)
    found = []
    for line in prescription_lines:
        if re.search(r'\bbarbell\b', line):
            # Extract the exercise name portion
            found.append(line[:60].strip())
    return found


def _find_gold_exercises(body):
    """
    Find GOLD exercises in prescriptive contexts only.
    Returns list of matched keywords.
    """
    prescription_lines = _get_prescription_lines(body)
    found = []
    for keyword in GOLD_KEYWORDS:
        for line in prescription_lines:
            if keyword in line:
                found.append(keyword)
                break
    return found


# ── Main ─────────────────────────────────────────────────────────────────────

def validate(card_path):
    failures = []
    passes = []

    if not os.path.exists(card_path):
        print(f"❌ FILE NOT FOUND: {card_path}")
        sys.exit(1)

    with open(card_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # ── Frontmatter parsing ──────────────────────────────────────────────────
    fm, body = parse_frontmatter(content)

    if fm is None:
        failures.append("FRONTMATTER: No frontmatter found (missing --- markers)")

    if fm is not None:
        # ── Status check ────────────────────────────────────────────────────
        status = fm.get('status', '').strip()
        if not status:
            failures.append("STATUS: Missing status field in frontmatter")
        elif status not in VALID_STATUSES:
            failures.append(f"STATUS: '{status}' is not valid. Must be one of: {', '.join(VALID_STATUSES)}")

        # ── Zip check ───────────────────────────────────────────────────────
        zip_raw = fm.get('zip', '').strip()
        if not zip_raw:
            failures.append("ZIP: Missing zip field in frontmatter")
            zip_parsed = None
        else:
            zip_parsed = parse_zip(zip_raw)
            if zip_parsed is None:
                failures.append(f"ZIP: '{zip_raw}' could not be parsed as ORDER AXIS TYPE COLOR")
            else:
                passes.append(f"ZIP: {zip_raw} parsed as ORDER={zip_parsed[0]} AXIS={zip_parsed[1]} TYPE={zip_parsed[2]} COLOR={zip_parsed[3]}")
    else:
        status = 'UNKNOWN'
        zip_parsed = None

    # ── Print header ─────────────────────────────────────────────────────────
    filename = os.path.basename(card_path)
    zip_display = fm.get('zip', 'UNKNOWN') if fm else 'UNKNOWN'
    status_display = status if fm else 'UNKNOWN'

    print(f"Card: {filename}")
    print(f"Zip:  {zip_display}")
    print(f"Status: {status_display}")
    print()

    # ── Stub exit ────────────────────────────────────────────────────────────
    if status == 'EMPTY':
        print("ℹ️  STUB: Card is empty (status: EMPTY). Content checks skipped.")
        print()
        print("✅ PASS: Stub file is valid")
        sys.exit(0)

    if fm is None or zip_parsed is None:
        # Can't do content checks without valid frontmatter/zip
        for f_msg in failures:
            print(f"❌ {f_msg}")
        sys.exit(1)

    order, axis, type_, color = zip_parsed

    # ── Determine library path ───────────────────────────────────────────────
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    library_path = os.path.join(repo_root, 'exercise-library.md')

    # ── Content checks (GENERATED and above) ────────────────────────────────

    # a. Block count
    # Color modifiers adjust block count expectations:
    # 🔴 Intense: +1 to max (🌋 Gutter permitted)
    # 🟠 Circuit: -2 to min (🧈/🧩/🪞 merge into 🎱 ARAM)
    # 🟡 Fun: -1 to min (🏖 Sandbox may replace standard blocks)
    block_count = count_blocks(body)
    min_blocks, max_blocks = ORDER_BLOCK_COUNTS.get(order, (4, 7))
    effective_min = min_blocks
    effective_max = max_blocks
    if color == '🔴':
        effective_max = max_blocks + 1
    elif color == '🟠':
        effective_min = max(3, min_blocks - 2)
    elif color == '🟡':
        effective_min = max(3, min_blocks - 1)
    if effective_min <= block_count <= effective_max:
        passes.append(f"BLOCK COUNT: {block_count} blocks (expected {effective_min}–{effective_max} for {order}/{color})")
    else:
        failures.append(f"BLOCK COUNT: {block_count} blocks (expected {effective_min}–{effective_max} for {order}/{color})")

    # b. 🧈 Bread & Butter must be present
    # Exception: 🟠 Circuit merges 🧈 into 🎱 ARAM per SCL rules
    if color == '🟠':
        if has_block(body, '🎱'):
            passes.append("🎱 ARAM: Present (Circuit — replaces 🧈 per SCL rules)")
        else:
            failures.append("🎱 ARAM: Missing — Circuit cards require 🎱 ARAM block (replaces 🧈)")
    elif has_block(body, '🧈'):
        passes.append("🧈 BREAD & BUTTER: Present")
    else:
        failures.append("🧈 BREAD & BUTTER: Missing — required in all non-Circuit workouts")

    # c. 🚂 Junction must be present
    if has_block(body, '🚂'):
        passes.append("🚂 JUNCTION: Present")
    else:
        failures.append("🚂 JUNCTION: Missing — required in all workouts")

    # d. 🧮 SAVE must appear
    if has_save(body):
        passes.append("🧮 SAVE: Present")
    else:
        failures.append("🧮 SAVE: Missing — every workout must end with 🧮")

    # e. 🎯 INTENTION must appear
    if has_intention(body):
        passes.append("🎯 INTENTION: Present")
    else:
        failures.append("🎯 INTENTION: Missing — quoted one-sentence frame required")

    # f. Circuit color: no barbell exercises prescribed
    # Only check prescriptive exercise lines, not explanatory text
    if color == '🟠':
        barbell_exercises = _find_barbell_exercises(body)
        if barbell_exercises:
            failures.append(
                f"COLOR 🟠 CIRCUIT: Barbell exercise prescribed — not allowed in Circuit: "
                + ', '.join(barbell_exercises[:3])
            )
        else:
            passes.append("COLOR 🟠 CIRCUIT: No barbell exercises prescribed (correct)")

    # g. Bodyweight color: no barbell exercises prescribed
    if color == '🟢':
        barbell_exercises = _find_barbell_exercises(body)
        if barbell_exercises:
            failures.append(
                f"COLOR 🟢 BODYWEIGHT: Barbell exercise prescribed — not allowed in Bodyweight: "
                + ', '.join(barbell_exercises[:3])
            )
        else:
            passes.append("COLOR 🟢 BODYWEIGHT: No barbell exercises prescribed (correct)")

    # h. GOLD exercise check (only on prescriptive lines)
    if color not in ('🔴', '🟣'):
        gold_violations = _find_gold_exercises(body)
        if gold_violations:
            failures.append(
                f"GOLD GATE: GOLD exercises prescribed in non-GOLD color ({color}): "
                + ', '.join(gold_violations[:5])
            )
        else:
            passes.append(f"GOLD GATE: No GOLD exercises in non-GOLD color {color} (correct)")

    # i. Exercise library check
    exercises = extract_exercises(body)
    if exercises:
        lib_results = check_against_library(exercises, library_path)
        not_found = [(e, f) for e, f in lib_results if f is False]
        not_checked = [(e, f) for e, f in lib_results if f is None]

        if not_checked:
            print(f"⚠️  LIBRARY CHECK: exercise-library.md not found at {library_path} — skipping exercise validation")
        elif not_found:
            for ex, _ in not_found:
                failures.append(f"EXERCISE LIBRARY: '{ex}' not found in exercise-library.md")
        else:
            passes.append(f"EXERCISE LIBRARY: All {len(exercises)} exercises found in library")
    else:
        passes.append("EXERCISE LIBRARY: No numbered exercises found to check (check manually if unexpected)")

    # ── Report ───────────────────────────────────────────────────────────────
    for p in passes:
        print(f"✅ {p}")

    for fail in failures:
        print(f"❌ {fail}")

    print()
    if not failures:
        print(f"✅ PASS: {filename}")
        sys.exit(0)
    else:
        print(f"❌ FAIL: {filename} — {len(failures)} check(s) failed")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate-card.py <card-path>")
        sys.exit(1)

    validate(sys.argv[1])
