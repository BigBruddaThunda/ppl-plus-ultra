#!/usr/bin/env python3
"""
progress-report.py — PPL± Generation Progress Dashboard
Usage: python scripts/progress-report.py

Scans the cards/ directory and reports generation progress by status,
order, axis, and deck number.
"""

import os
import sys
import re
from datetime import date

# ── SCL Emoji Metadata ───────────────────────────────────────────────────────
ORDER_NAMES = {
    '🐂': 'Foundation',
    '⛽': 'Strength',
    '🦋': 'Hypertrophy',
    '🏟': 'Performance',
    '🌾': 'Full Body',
    '⚖': 'Balance',
    '🖼': 'Restoration',
}
ORDER_LIST = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']

AXIS_LIST = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
AXIS_NAMES = {
    '🏛': 'Basics',
    '🔨': 'Functional',
    '🌹': 'Aesthetic',
    '🪐': 'Challenge',
    '⌛': 'Time',
    '🐬': 'Partner',
}

# Deck grid: order (row) × axis (col) = deck number
DECK_GRID = {
    ('🐂', '🏛'): '01', ('🐂', '🔨'): '02', ('🐂', '🌹'): '03',
    ('🐂', '🪐'): '04', ('🐂', '⌛'): '05', ('🐂', '🐬'): '06',
    ('⛽', '🏛'): '07', ('⛽', '🔨'): '08', ('⛽', '🌹'): '09',
    ('⛽', '🪐'): '10', ('⛽', '⌛'): '11', ('⛽', '🐬'): '12',
    ('🦋', '🏛'): '13', ('🦋', '🔨'): '14', ('🦋', '🌹'): '15',
    ('🦋', '🪐'): '16', ('🦋', '⌛'): '17', ('🦋', '🐬'): '18',
    ('🏟', '🏛'): '19', ('🏟', '🔨'): '20', ('🏟', '🌹'): '21',
    ('🏟', '🪐'): '22', ('🏟', '⌛'): '23', ('🏟', '🐬'): '24',
    ('🌾', '🏛'): '25', ('🌾', '🔨'): '26', ('🌾', '🌹'): '27',
    ('🌾', '🪐'): '28', ('🌾', '⌛'): '29', ('🌾', '🐬'): '30',
    ('⚖', '🏛'): '31', ('⚖', '🔨'): '32', ('⚖', '🌹'): '33',
    ('⚖', '🪐'): '34', ('⚖', '⌛'): '35', ('⚖', '🐬'): '36',
    ('🖼', '🏛'): '37', ('🖼', '🔨'): '38', ('🖼', '🌹'): '39',
    ('🖼', '🪐'): '40', ('🖼', '⌛'): '41', ('🖼', '🐬'): '42',
}

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES   = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES  = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']

GENERATED_STATUSES = {'GENERATED', 'GENERATED-V2', 'CANONICAL'}

# ── Frontmatter parser ────────────────────────────────────────────────────────
def parse_frontmatter(content):
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None

    fm = {}
    for line in lines[1:end_idx]:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    return fm


def parse_zip_order_axis(zip_str):
    """Extract order and axis emoji from a zip string."""
    s = zip_str.strip()
    order = None
    for o in ORDERS:
        if s.startswith(o):
            order = o
            s = s[len(o):]
            break
    if order is None:
        return None, None

    axis = None
    for a in AXES:
        if s.startswith(a):
            axis = a
            break
    return order, axis


# ── Main scan ─────────────────────────────────────────────────────────────────
def run_report():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    cards_dir = os.path.join(repo_root, 'cards')

    if not os.path.exists(cards_dir):
        print("ERROR: cards/ directory not found")
        sys.exit(1)

    total_files = 0
    total_stubs = 0
    total_generated = 0

    # Counters
    by_order_generated = {o: 0 for o in ORDER_LIST}
    by_order_total = {o: 0 for o in ORDER_LIST}

    by_axis_generated = {a: 0 for a in AXIS_LIST}
    by_axis_total = {a: 0 for a in AXIS_LIST}

    # deck_number -> (generated, total)
    deck_counts = {}

    for dirpath, dirnames, filenames in os.walk(cards_dir):
        # Skip non-card directories
        for fname in filenames:
            if not fname.endswith('.md'):
                continue
            if fname == 'AGENTS.md':
                continue

            fpath = os.path.join(dirpath, fname)
            total_files += 1

            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            fm = parse_frontmatter(content)
            if fm is None:
                continue

            status = fm.get('status', '').strip()
            zip_str = fm.get('zip', '').strip()
            deck_num = fm.get('deck', '').strip()

            is_generated = status in GENERATED_STATUSES
            is_stub = status == 'EMPTY'

            if is_stub:
                total_stubs += 1
            elif is_generated:
                total_generated += 1

            # By order / axis
            if zip_str:
                order, axis = parse_zip_order_axis(zip_str)
                if order:
                    by_order_total[order] = by_order_total.get(order, 0) + 1
                    if is_generated:
                        by_order_generated[order] = by_order_generated.get(order, 0) + 1
                if axis:
                    by_axis_total[axis] = by_axis_total.get(axis, 0) + 1
                    if is_generated:
                        by_axis_generated[axis] = by_axis_generated.get(axis, 0) + 1

            # By deck
            if deck_num:
                # Normalize deck number to 2-digit string
                try:
                    deck_key = str(int(deck_num)).zfill(2)
                except ValueError:
                    deck_key = deck_num
                if deck_key not in deck_counts:
                    deck_counts[deck_key] = [0, 0]  # [generated, total]
                deck_counts[deck_key][1] += 1
                if is_generated:
                    deck_counts[deck_key][0] += 1

    # ── Output ────────────────────────────────────────────────────────────────
    today = date.today().strftime('%Y-%m-%d')
    total_system = 1680
    pct = (total_generated / total_system * 100) if total_system > 0 else 0

    print(f"PPL± Progress Report — {today}")
    print("══════════════════════════════════════")
    print(f"Total: {total_generated} / {total_system} ({pct:.1f}%)")
    print(f"Stubs remaining: {total_stubs}")
    print()

    print("By Order:")
    for order in ORDER_LIST:
        name = ORDER_NAMES[order]
        gen = by_order_generated.get(order, 0)
        total_order = 240  # 6 axes × 5 types × 8 colors = 240
        bar = '✅' if gen == total_order else ''
        print(f"  {order} {name:<14} {gen:>3} / {total_order} {bar}")
    print()

    print("By Axis:")
    for axis in AXIS_LIST:
        name = AXIS_NAMES[axis]
        gen = by_axis_generated.get(axis, 0)
        total_axis = 280  # 7 orders × 5 types × 8 colors = 280
        bar = '✅' if gen == total_axis else ''
        print(f"  {axis} {name:<14} {gen:>3} / {total_axis} {bar}")
    print()

    # Separate completed vs partial decks
    completed_decks = []
    partial_decks = []

    for deck_key in sorted(deck_counts.keys()):
        gen, total = deck_counts[deck_key]
        # Find order+axis for this deck
        deck_label = None
        for (o, a), d in DECK_GRID.items():
            if d == deck_key:
                deck_label = f"{o}{a}"
                break
        label = f"Deck {deck_key} {deck_label or ''}"
        if gen >= 40 and total >= 40:
            completed_decks.append(f"  {label}: 40/40 ✅")
        elif gen > 0:
            partial_decks.append(f"  {label}: {gen}/{total}")

    if completed_decks:
        print("By Deck (completed):")
        for line in completed_decks:
            print(line)
        print()

    if partial_decks:
        print("Decks with partial progress:")
        for line in partial_decks:
            print(line)
        print()

    # Anomaly detection
    anomalies = []
    for deck_key in sorted(deck_counts.keys()):
        gen, total = deck_counts[deck_key]
        if 0 < gen < 40:
            anomalies.append(f"  Deck {deck_key}: {gen}/{total} cards generated (partial)")
        if total > 40:
            anomalies.append(f"  Deck {deck_key}: {total} files found (expected 40)")

    if anomalies:
        print("⚠️  Anomalies:")
        for a in anomalies:
            print(a)
        print()


if __name__ == '__main__':
    run_report()
