#!/usr/bin/env python3
"""validate-junction-bridges.py

Input contract:
- Either `--card <path>` or `--deck <path>`.

Output contract:
- Validates `Next -> [zip] — rationale` lines in generated cards.
- Exit 1 on hard failures:
  - malformed Next-line syntax
  - invalid zip code format
  - missing rationale text
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']

NEXT_PATTERN = re.compile(r'^\s*Next\s*->\s*([^\s]+)\s*[—-]\s*(.+?)\s*$', re.IGNORECASE)


def parse_frontmatter(content: str):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None, content
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            fm = {}
            for line in lines[1:i]:
                if ':' in line:
                    k, _, v = line.partition(':')
                    fm[k.strip()] = v.strip()
            return fm, '\n'.join(lines[i + 1:])
    return None, content


def parse_zip(zip_str: str):
    s = zip_str.strip()
    for group in [ORDERS, AXES, TYPES, COLORS]:
        matched = False
        for e in group:
            if s.startswith(e):
                s = s[len(e):]
                matched = True
                break
        if not matched:
            return False
    return not s.strip()


def iter_cards(card: str | None, deck: str | None):
    if card:
        yield Path(card)
        return
    for p in sorted(Path(deck).rglob('*.md')):
        if p.name != 'AGENTS.md':
            yield p


def main():
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--card')
    group.add_argument('--deck')
    args = ap.parse_args()

    hard_fail = False
    checked = 0

    for card_path in iter_cards(args.card, args.deck):
        text = card_path.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        if not fm or fm.get('status') == 'EMPTY':
            continue
        checked += 1

        lines = body.splitlines()
        next_lines = [line for line in lines if 'Next' in line and '->' in line]
        for line in next_lines:
            m = NEXT_PATTERN.match(line)
            if not m:
                print(f"❌ {card_path}: malformed junction line: {line.strip()}")
                hard_fail = True
                continue
            zip_token, rationale = m.group(1).strip(), m.group(2).strip()
            zip_token = zip_token.strip('[]')
            if not parse_zip(zip_token):
                print(f"❌ {card_path}: invalid junction zip '{zip_token}'")
                hard_fail = True
            if len(rationale) < 5:
                print(f"❌ {card_path}: rationale too short in line '{line.strip()}'")
                hard_fail = True

    if not hard_fail:
        print(f"✅ Junction bridge validation passed ({checked} generated card(s) checked).")
    raise SystemExit(1 if hard_fail else 0)


if __name__ == '__main__':
    main()
