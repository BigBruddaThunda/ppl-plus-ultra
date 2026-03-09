#!/usr/bin/env python3
"""fix-card-format.py — Batch format fixes for Ppl± workout cards.

Applies non-destructive scripted patches to fix common format issues:
  A. Add inline operator call to first block header (if missing)
  B. Remove barbell exercises from 🟢 Bodyweight and 🟠 Circuit cards
  C. Rename 🧈 Bread & Butter → 🎱 ARAM in 🟠 Circuit cards (if missing)
  D. Add 🏖 Sandbox block to 🟡 Fun cards (if missing)
  E. Add tempo cues to ⚪ Mindful exercise lines (if missing)

Usage:
  python scripts/fix-card-format.py cards/ --dry-run    # preview
  python scripts/fix-card-format.py cards/               # apply
  python scripts/fix-card-format.py cards/ --fix operator # only fix A
  python scripts/fix-card-format.py cards/ --fix circuit  # only fix B+C
  python scripts/fix-card-format.py cards/ --fix fun      # only fix D
  python scripts/fix-card-format.py cards/ --fix mindful  # only fix E
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']

OPERATOR_EMOJIS = ['🧲', '🐋', '🤌', '🧸', '✒️', '🦉', '🥨', '🦢', '📍', '👀', '🪵', '🚀']

# Operator table: Axis × Color polarity → operator emoji
# Preparatory Colors: ⚫🟢⚪🟡 → first column
# Expressive Colors: 🔵🟣🔴🟠 → second column
OPERATOR_TABLE = {
    '🏛': {'prep': '📍', 'expr': '🤌'},
    '🔨': {'prep': '🧸', 'expr': '🥨'},
    '🌹': {'prep': '👀', 'expr': '🦢'},
    '🪐': {'prep': '🪵', 'expr': '🚀'},
    '⌛': {'prep': '🐋', 'expr': '✒️'},
    '🐬': {'prep': '🧲', 'expr': '🦉'},
}

PREP_COLORS = {'⚫', '🟢', '⚪', '🟡'}
EXPR_COLORS = {'🔵', '🟣', '🔴', '🟠'}

# Substitution map for barbell → dumbbell/kettlebell
BARBELL_SUBS = {
    'barbell': 'dumbbell',
    'Barbell': 'Dumbbell',
}

TYPE_NAMES = {'🛒': 'Push', '🪡': 'Pull', '🍗': 'Legs', '➕': 'Plus', '➖': 'Ultra'}


def parse_zip(zip_str: str):
    s = zip_str.strip()
    result = []
    for emoji_set in [ORDERS, AXES, TYPES, COLORS]:
        for emoji in emoji_set:
            if s.startswith(emoji):
                result.append(emoji)
                s = s[len(emoji):]
                break
        else:
            return None
    return tuple(result)


def parse_frontmatter(content: str):
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, content, 0
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    if end_idx is None:
        return None, content, 0
    fm = {}
    for line in lines[1:end_idx]:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    body = '\n'.join(lines[end_idx + 1:])
    return fm, body, end_idx


def get_operator_for_zip(axis: str, color: str) -> str | None:
    """Derive default operator emoji from Axis × Color polarity."""
    if axis not in OPERATOR_TABLE:
        return None
    polarity = 'prep' if color in PREP_COLORS else 'expr'
    return OPERATOR_TABLE[axis][polarity]


def has_operator_in_body(body: str) -> bool:
    """Check if any operator emoji appears in the body (not frontmatter)."""
    return any(op in body for op in OPERATOR_EMOJIS)


def fix_operator_call(content: str, fm: dict, body: str) -> tuple[str, bool]:
    """Fix A: Add inline operator call to first block header if missing."""
    if has_operator_in_body(body):
        return content, False

    zip_str = fm.get('zip', '')
    parsed = parse_zip(zip_str)
    if not parsed:
        return content, False

    _order, axis, _type, color = parsed
    op_emoji = get_operator_for_zip(axis, color)
    if not op_emoji:
        return content, False

    # Get operator name from frontmatter
    op_line = fm.get('operator', '')
    op_name = ''
    for op in OPERATOR_EMOJIS:
        if op in op_line:
            parts = op_line.split(op, 1)
            if len(parts) > 1:
                op_name = parts[1].strip()
            break

    # Find first block header: ## N) EMOJI Block Name
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if re.match(r'^##\s+\d+\)\s+', line.strip()):
            # Add operator after block header if not already there
            if op_emoji not in line:
                suffix = f" — {op_emoji} {op_name}" if op_name else f" — {op_emoji}"
                lines[i] = line.rstrip() + suffix
                return '\n'.join(lines), True
            break

    return content, False


def fix_circuit_barbell(content: str, fm: dict, body: str) -> tuple[str, bool]:
    """Fix B: Remove barbell references from 🟠 Circuit and 🟢 Bodyweight cards."""
    zip_str = fm.get('zip', '')
    parsed = parse_zip(zip_str)
    if not parsed:
        return content, False
    color = parsed[3]
    if color not in ('🟠', '🟢'):
        return content, False

    # Replace barbell → dumbbell in exercise lines
    lines = content.split('\n')
    changed = False
    for i, line in enumerate(lines):
        if 'barbell' in line.lower() and ('├─' in line or '│' in line or re.match(r'^\s*\d+\s+', line)):
            new_line = re.sub(r'\bBarbell\b', 'Dumbbell', line)
            new_line = re.sub(r'\bbarbell\b', 'dumbbell', new_line)
            if new_line != line:
                lines[i] = new_line
                changed = True

    return '\n'.join(lines), changed


def fix_circuit_aram(content: str, fm: dict, body: str) -> tuple[str, bool]:
    """Fix C: Rename 🧈 Bread & Butter → 🎱 ARAM in 🟠 Circuit cards if no ARAM exists."""
    zip_str = fm.get('zip', '')
    parsed = parse_zip(zip_str)
    if not parsed:
        return content, False
    color = parsed[3]
    if color != '🟠':
        return content, False

    if '🎱' in body:
        return content, False  # Already has ARAM

    if '🧈' not in body:
        return content, False  # No Bread & Butter to rename

    # Replace 🧈 Bread & Butter → 🎱 ARAM in block headers
    content = content.replace('🧈 Bread & Butter', '🎱 ARAM')
    content = content.replace('🧈 Bread/Butter', '🎱 ARAM')
    # Also update frontmatter blocks line
    content = content.replace('🧈', '🎱')

    return content, True


def fix_fun_sandbox(content: str, fm: dict, body: str) -> tuple[str, bool]:
    """Fix D: Add 🏖 Sandbox block to 🟡 Fun cards if missing."""
    zip_str = fm.get('zip', '')
    parsed = parse_zip(zip_str)
    if not parsed:
        return content, False
    color = parsed[3]
    if color != '🟡':
        return content, False

    if '🏖' in body:
        return content, False  # Already has Sandbox

    # Find the 🪫 Release block or 🚂 Junction to insert before
    lines = content.split('\n')
    insert_idx = None
    block_num = 0

    for i, line in enumerate(lines):
        if re.match(r'^##\s+(\d+)\)', line.strip()):
            m = re.match(r'^##\s+(\d+)\)', line.strip())
            block_num = int(m.group(1))
            if '🪫' in line or '🚂' in line:
                insert_idx = i
                break

    if insert_idx is None:
        return content, False

    # Get type emoji and name
    type_emoji = parsed[2]
    type_name = TYPE_NAMES.get(type_emoji, '')

    # Build Sandbox block
    sandbox = [
        '═══',
        f'## {block_num}) 🏖 Sandbox',
        f'Subcode: {fm.get("zip", "")} (Sandbox | {type_name} | Fun)',
        f'├─ Choose your adventure — pick one variation you have not tried before:',
        f'│  Option A: Explore a grip or stance variation',
        f'│  Option B: Try a tempo you normally avoid',
        f'│  Option C: Combine two movements creatively',
        f'Rest: 90s between attempts',
    ]

    # Insert before the Release/Junction block, renumber subsequent blocks
    lines[insert_idx:insert_idx] = sandbox

    # Renumber blocks after insertion
    new_num = block_num + 1
    for j in range(insert_idx + len(sandbox), len(lines)):
        m = re.match(r'^(##\s+)(\d+)(\)\s+.*)$', lines[j])
        if m:
            lines[j] = f'{m.group(1)}{new_num}{m.group(3)}'
            new_num += 1

    return '\n'.join(lines), True


def fix_mindful_tempo(content: str, fm: dict, body: str) -> tuple[str, bool]:
    """Fix E: Add tempo cues to ⚪ Mindful exercise lines if missing."""
    zip_str = fm.get('zip', '')
    parsed = parse_zip(zip_str)
    if not parsed:
        return content, False
    color = parsed[3]
    if color != '⚪':
        return content, False

    tempo_words = ['tempo', 'eccentric', 'breath', 'slow', '4s', '4-sec', 'inhale', 'exhale']
    lines = content.split('\n')
    changed = False

    for i, line in enumerate(lines):
        # Exercise lines: ├─ N TYPE Exercise Name
        if '├─' in line and any(t in line for t in TYPES):
            # Check if already has tempo cue
            if any(tw in line.lower() for tw in tempo_words):
                continue
            # Check if has a parenthetical cue
            if re.search(r'\([^)]+\)\s*$', line):
                # Replace existing cue with tempo cue
                line_new = re.sub(r'\([^)]+\)\s*$', '(4s eccentric, breath-paced)', line)
            else:
                # Add tempo cue
                line_new = line.rstrip() + ' (4s eccentric, breath-paced)'
            if line_new != line:
                lines[i] = line_new
                changed = True

    return '\n'.join(lines), changed


def process_card(card_path: str, fixes: set[str], dry_run: bool) -> dict:
    """Process a single card file. Returns stats dict."""
    with open(card_path, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body, _ = parse_frontmatter(content)
    if fm is None or fm.get('status', '') == 'EMPTY':
        return {'skipped': True}

    stats = {'path': card_path, 'fixes_applied': []}
    current = content

    if 'operator' in fixes or 'all' in fixes:
        current, changed = fix_operator_call(current, fm, body)
        if changed:
            stats['fixes_applied'].append('operator_call')

    if 'circuit' in fixes or 'all' in fixes:
        current, changed = fix_circuit_barbell(current, fm, body)
        if changed:
            stats['fixes_applied'].append('circuit_barbell')
        current, changed = fix_circuit_aram(current, fm, body)
        if changed:
            stats['fixes_applied'].append('circuit_aram')

    if 'fun' in fixes or 'all' in fixes:
        current, changed = fix_fun_sandbox(current, fm, body)
        if changed:
            stats['fixes_applied'].append('fun_sandbox')

    if 'mindful' in fixes or 'all' in fixes:
        current, changed = fix_mindful_tempo(current, fm, body)
        if changed:
            stats['fixes_applied'].append('mindful_tempo')

    if stats['fixes_applied'] and not dry_run:
        with open(card_path, 'w', encoding='utf-8') as f:
            f.write(current)

    return stats


def main():
    parser = argparse.ArgumentParser(description="Batch format fixes for Ppl± cards")
    parser.add_argument("path", help="Path to cards/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--fix", choices=['operator', 'circuit', 'fun', 'mindful', 'all'],
                       default='all', help="Which fix to apply (default: all)")
    args = parser.parse_args()

    fixes = {args.fix}
    cards_dir = Path(args.path)

    total = 0
    fixed = 0
    fix_counts = {}

    for dirpath, dirnames, filenames in os.walk(cards_dir):
        for fn in sorted(filenames):
            if not fn.endswith('.md') or '±' not in fn:
                continue
            fp = os.path.join(dirpath, fn)
            total += 1
            stats = process_card(fp, fixes, args.dry_run)
            if stats.get('skipped'):
                continue
            if stats['fixes_applied']:
                fixed += 1
                for fix_name in stats['fixes_applied']:
                    fix_counts[fix_name] = fix_counts.get(fix_name, 0) + 1

    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{prefix}Processed {total} cards, {fixed} modified:")
    for fix_name, count in sorted(fix_counts.items()):
        print(f"  {fix_name}: {count} cards")
    if not fix_counts:
        print("  No fixes needed.")


if __name__ == "__main__":
    main()
