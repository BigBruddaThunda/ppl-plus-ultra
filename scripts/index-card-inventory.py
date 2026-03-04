#!/usr/bin/env python3
"""index-card-inventory.py

Input contract:
- `--cards-root <path>` required.
- Optional: `--out-json`, `--out-csv`, `--baseline`.

Output contract:
- Emits inventory rows: deck, zip, status, file.
- Optional JSON/CSV artifacts.
- Exit 1 on hard failures:
  - unreadable markdown file
  - missing or unknown status when `--strict-status` is enabled
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

VALID_STATUSES = {'EMPTY', 'GENERATED', 'GENERATED-V2', 'CANONICAL', 'REGEN-NEEDED', 'GENERATED-V2-REGEN-NEEDED'}


def parse_frontmatter(content: str):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            fm = {}
            for line in lines[1:i]:
                if ':' in line:
                    k, _, v = line.partition(':')
                    fm[k.strip()] = v.strip()
            return fm
    return None


def row_for_file(path: Path, cards_root: Path):
    rel = path.relative_to(cards_root)
    deck = '/'.join(rel.parts[:2]) if len(rel.parts) >= 2 else ''
    content = path.read_text(encoding='utf-8')
    fm = parse_frontmatter(content) or {}
    return {
        'deck': deck,
        'zip': fm.get('zip', ''),
        'status': fm.get('status', ''),
        'file': str(rel),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cards-root', required=True)
    ap.add_argument('--out-json')
    ap.add_argument('--out-csv')
    ap.add_argument('--baseline', help='Optional prior JSON inventory for delta report')
    ap.add_argument('--strict-status', action='store_true')
    args = ap.parse_args()

    root = Path(args.cards_root)
    rows = []
    hard_fail = False

    for p in sorted(root.rglob('*.md')):
        if p.name == 'AGENTS.md':
            continue
        try:
            row = row_for_file(p, root)
        except Exception as exc:
            print(f'❌ Failed to read {p}: {exc}')
            hard_fail = True
            continue

        if args.strict_status:
            if not row['status']:
                print(f"❌ missing status in {row['file']}")
                hard_fail = True
            elif row['status'] not in VALID_STATUSES:
                print(f"❌ unknown status '{row['status']}' in {row['file']}")
                hard_fail = True

        rows.append(row)

    status_counts = {}
    for r in rows:
        status_counts[r['status']] = status_counts.get(r['status'], 0) + 1

    payload = {'count': len(rows), 'status_counts': status_counts, 'cards': rows}

    if args.out_json:
        out = Path(args.out_json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')

    if args.out_csv:
        out = Path(args.out_csv)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['deck', 'zip', 'status', 'file'])
            writer.writeheader()
            writer.writerows(rows)

    if args.baseline:
        base = json.loads(Path(args.baseline).read_text(encoding='utf-8'))
        old_files = {r['file'] for r in base.get('cards', [])}
        new_files = {r['file'] for r in rows}
        print(f"Delta: +{len(new_files - old_files)} / -{len(old_files - new_files)} files")

    print(f"Indexed {len(rows)} card files. Status counts: {status_counts}")
    raise SystemExit(1 if hard_fail else 0)


if __name__ == '__main__':
    main()
