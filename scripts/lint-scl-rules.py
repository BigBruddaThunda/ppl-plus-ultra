#!/usr/bin/env python3
"""lint-scl-rules.py

Input contract:
- One target: `--card <path>` or `--deck <path>`.
- Optional `--deck-identity <path>` existence check.
- Optional `--format json` for machine-readable output.

Output contract:
- Aggregates current validator checks and emits summary.
- Exit 1 on hard failures (validator failures, missing required deck identity, naming violations).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def run(cmd: list[str]):
    proc = subprocess.run(cmd, text=True, capture_output=True)
    return {'cmd': cmd, 'code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}


def filename_violation(path: Path):
    # Guardrail: completed files should include ± and operator emoji after it.
    # This is intentionally minimal and non-destructive.
    if path.name == 'AGENTS.md' or not path.name.endswith('.md'):
        return None
    if '±' not in path.stem:
        return 'missing ± in filename'
    if path.stem.endswith('±'):
        return None  # stub is acceptable
    if not re.search(r'±\S+\s+.+', path.stem):
        return 'generated filename missing operator+title segment'
    return None


def list_cards(card: str | None, deck: str | None):
    if card:
        return [Path(card)]
    return sorted(p for p in Path(deck).rglob('*.md') if p.name != 'AGENTS.md')


def main():
    ap = argparse.ArgumentParser()
    target = ap.add_mutually_exclusive_group(required=True)
    target.add_argument('--card')
    target.add_argument('--deck')
    ap.add_argument('--deck-identity')
    ap.add_argument('--format', choices=['text', 'json'], default='text')
    args = ap.parse_args()

    report = {'hard_failures': [], 'commands': []}

    if args.deck_identity and not Path(args.deck_identity).exists():
        report['hard_failures'].append(f'missing deck identity: {args.deck_identity}')

    # Reuse existing validators
    if args.card:
        report['commands'].append(run(['python', 'scripts/validate-card.py', args.card]))
    else:
        report['commands'].append(run(['bash', 'scripts/validate-deck.sh', args.deck]))

    # Filename convention guardrail
    for p in list_cards(args.card, args.deck):
        violation = filename_violation(p)
        if violation:
            report['hard_failures'].append(f'{p}: {violation}')

    for item in report['commands']:
        if item['code'] != 0:
            report['hard_failures'].append(f"command failed: {' '.join(item['cmd'])}")

    if args.format == 'json':
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for item in report['commands']:
            print(f"$ {' '.join(item['cmd'])}")
            if item['stdout']:
                print(item['stdout'].rstrip())
            if item['stderr']:
                print(item['stderr'].rstrip())
        if report['hard_failures']:
            print('Hard failures:')
            for h in report['hard_failures']:
                print(f'- {h}')
        else:
            print('No hard failures.')

    raise SystemExit(1 if report['hard_failures'] else 0)


if __name__ == '__main__':
    main()
