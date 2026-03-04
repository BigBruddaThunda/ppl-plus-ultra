#!/usr/bin/env python3
"""check-card-schema.py

Input contract:
- Either `--card <path>` or `--deck <path>`.
- Accepts markdown card files with frontmatter.

Output contract:
- Human summary to stdout.
- Optional JSON summary via `--json`.
- Exit 0 if all checked cards satisfy schema guardrails.
- Exit 1 on hard failures (missing frontmatter, missing zip, malformed zip,
  missing required blocks for generated cards, missing/invalid sub-block zip markers).

Canonical status allow-list:
- EMPTY
- GENERATED
- GENERATED-V2
- CANONICAL
- REGEN-NEEDED
- GENERATED-V2-REGEN-NEEDED
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']
VALID_STATUSES = {'EMPTY', 'GENERATED', 'GENERATED-V2', 'CANONICAL', 'REGEN-NEEDED', 'GENERATED-V2-REGEN-NEEDED'}

SUB_BLOCK_PATTERN = re.compile(r'(?:^|\s)([♨️🎯🔢🧈🫀▶️🎼♟️🪜🌎🎱🌋🪞🗿🛠🧩🪫🏖🏗🧬🚂🔠][🛒🪡🍗➕➖][🏛🔨🌹🪐⌛🐬][⚫🟢🔵🟣🔴🟠🟡⚪])(?:\s|$)')


def parse_frontmatter(content: str):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None, content
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break
    if end is None:
        return None, content
    fm = {}
    for line in lines[1:end]:
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip()
    return fm, '\n'.join(lines[end + 1:])


def parse_zip(zip_str: str):
    s = zip_str.strip()
    out = []
    for emoji_set in [ORDERS, AXES, TYPES, COLORS]:
        for e in emoji_set:
            if s.startswith(e):
                out.append(e)
                s = s[len(e):]
                break
        else:
            return None
    return tuple(out) if not s.strip() else None


def validate_card(path: Path):
    failures = []
    content = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    if fm is None:
        return ['missing frontmatter'], []

    status = fm.get('status', '').strip()
    if status not in VALID_STATUSES:
        failures.append(f"invalid status: {status or '(missing)'}")

    zip_raw = fm.get('zip', '').strip()
    parsed = parse_zip(zip_raw) if zip_raw else None
    if not zip_raw:
        failures.append('missing zip field')
    elif parsed is None:
        failures.append(f'malformed zip: {zip_raw}')

    if status != 'EMPTY':
        if '🧈' not in body and '🎱' not in body:
            failures.append('missing transformation anchor (🧈 or 🎱)')
        if '🚂' not in body:
            failures.append('missing 🚂 junction block')
        if '🧮' not in body:
            failures.append('missing 🧮 save section')
        if not SUB_BLOCK_PATTERN.search(body):
            failures.append('missing sub-block zip marker (BLOCK+TYPE+AXIS+COLOR)')

    notes = []
    if status != 'EMPTY' and '├─' not in body and '│' not in body:
        failures.append('tree notation not detected')
    return failures, notes


def collect_cards(card: str | None, deck: str | None):
    if card:
        p = Path(card)
        if not p.exists():
            raise FileNotFoundError(f'Card not found: {card}')
        return [p]
    deck_path = Path(deck)
    if not deck_path.exists():
        raise FileNotFoundError(f'Deck path not found: {deck}')
    return sorted(p for p in deck_path.rglob('*.md') if p.name != 'AGENTS.md')


def main():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument('--card')
    g.add_argument('--deck')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()

    try:
        cards = collect_cards(args.card, args.deck)
    except FileNotFoundError as exc:
        print(f'❌ {exc}')
        raise SystemExit(1)
    results = []
    hard_fail_count = 0
    for c in cards:
        fails, notes = validate_card(c)
        if fails:
            hard_fail_count += 1
        results.append({'card': str(c), 'failures': fails, 'notes': notes})

    if args.json:
        print(json.dumps({'checked': len(cards), 'hard_fail_cards': hard_fail_count, 'results': results}, ensure_ascii=False, indent=2))
    else:
        print(f'Checked {len(cards)} card(s).')
        for r in results:
            marker = '❌' if r['failures'] else '✅'
            print(f"{marker} {r['card']}")
            for f in r['failures']:
                print(f'   - {f}')
            for n in r['notes']:
                print(f'   - ⚠️ {n}')

    raise SystemExit(1 if hard_fail_count else 0)


if __name__ == '__main__':
    main()
