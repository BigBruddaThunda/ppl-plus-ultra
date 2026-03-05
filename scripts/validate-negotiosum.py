#!/usr/bin/env python3
"""validate-negotiosum.py

Validate Negotiosum consistency across:
- whiteboard.md
- .codex/TASK-ARCHITECTURE.md
- seeds/codex-container-directory-v3.md
- middle-math/zip-registry.json
- cards/ frontmatter status scan

Usage:
  python scripts/validate-negotiosum.py
  python scripts/validate-negotiosum.py --json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

WHITEBOARD_PATH = Path('whiteboard.md')
TASK_ARCH_PATH = Path('.codex/TASK-ARCHITECTURE.md')
CONTAINER_DIR_PATH = Path('seeds/codex-container-directory-v3.md')
ZIP_REGISTRY_PATH = Path('middle-math/zip-registry.json')
CARDS_PATH = Path('cards')

EXPECTED_CORE_CONTAINERS = {'CX-00A', 'CX-00B'} | {f'CX-{i:02d}' for i in range(1, 32)}
GENERATED_STATUSES = {'GENERATED', 'GENERATED-V2', 'CANONICAL'}

CX_PATTERN = re.compile(r'CX-(?:00[AB]|\d{2})')


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def parse_frontmatter(content: str) -> dict[str, str] | None:
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end = i
            break

    if end is None:
        return None

    frontmatter: dict[str, str] = {}
    for line in lines[1:end]:
        if ':' in line:
            key, _, value = line.partition(':')
            frontmatter[key.strip()] = value.strip()
    return frontmatter


def parse_whiteboard(text: str) -> dict[str, Any]:
    header = {
        'cards_generated': None,
        'cards_total': None,
        'seeds': None,
        'scripts': None,
        'cx_defined': None,
        'cx_complete': None,
        'cx_open': None,
    }

    cards_match = re.search(r'^Cards:\s*([\d,]+)\s*/\s*([\d,]+)', text, re.MULTILINE)
    if cards_match:
        header['cards_generated'] = int(cards_match.group(1).replace(',', ''))
        header['cards_total'] = int(cards_match.group(2).replace(',', ''))

    seeds_match = re.search(r'^Seeds:\s*(\d+)\s*\|\s*Scripts:\s*(\d+)', text, re.MULTILINE)
    if seeds_match:
        header['seeds'] = int(seeds_match.group(1))
        header['scripts'] = int(seeds_match.group(2))

    cx_match = re.search(r'^CX Containers:\s*(\d+)\s+defined,\s*(\d+)\s+complete,\s*(\d+)\s+open', text, re.MULTILINE)
    if cx_match:
        header['cx_defined'] = int(cx_match.group(1))
        header['cx_complete'] = int(cx_match.group(2))
        header['cx_open'] = int(cx_match.group(3))

    task_rows = []
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith('| Status | ID | Task | Blocker | Note |'):
            in_table = True
            continue
        if in_table and stripped.startswith('|--------|'):
            continue
        if in_table and stripped.startswith('|'):
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if len(cells) >= 5:
                row = {
                    'status': cells[0],
                    'id': cells[1],
                    'task': cells[2],
                    'blocker': cells[3],
                    'note': cells[4],
                    'raw': stripped,
                }
                task_rows.append(row)
            continue

        if in_table and stripped and not stripped.startswith('|'):
            in_table = False

    all_cx_mentions = sorted(set(CX_PATTERN.findall(text)))

    # convenient ID->status map for rows where ID is explicit
    row_status_by_id: dict[str, str] = {}
    for row in task_rows:
        cid = row['id']
        if CX_PATTERN.fullmatch(cid):
            row_status_by_id[cid] = row['status'].upper()

    return {
        'header': header,
        'task_rows': task_rows,
        'cx_mentions': all_cx_mentions,
        'row_status_by_id': row_status_by_id,
    }


def parse_task_architecture(text: str) -> dict[str, str]:
    statuses: dict[str, str] = {}

    in_index = False
    for line in text.splitlines():
        if line.strip().startswith('| Container |'):
            in_index = True
            continue
        if in_index and line.strip().startswith('|---'):
            continue
        if in_index:
            stripped = line.strip()
            if not stripped.startswith('|'):
                break
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if len(cells) < 5:
                continue
            container_cell = cells[0]
            status_cell = cells[4].upper()
            ids = CX_PATTERN.findall(container_cell)
            for cid in ids:
                statuses[cid] = status_cell

    return statuses


def parse_seed_container_ids(text: str) -> set[str]:
    return set(CX_PATTERN.findall(text))


def scan_card_status_counts(cards_root: Path) -> dict[str, int]:
    counts = {
        'generated_like': 0,
        'total_md_files': 0,
        'frontmatter_missing': 0,
    }

    for path in sorted(cards_root.rglob('*.md')):
        if path.name == 'AGENTS.md':
            continue

        counts['total_md_files'] += 1
        content = path.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)
        if fm is None:
            counts['frontmatter_missing'] += 1
            continue

        status = fm.get('status', '').strip()
        if status in GENERATED_STATUSES:
            counts['generated_like'] += 1

    return counts


def blocker_mentions(blocker_text: str) -> list[tuple[str, bool]]:
    if blocker_text.strip() in {'—', '-', ''}:
        return []

    mentions: list[tuple[str, bool]] = []
    for match in CX_PATTERN.finditer(blocker_text):
        cid = match.group(0)
        tail = blocker_text[match.end():match.end() + 3]
        marked_done = '✓' in tail
        mentions.append((cid, marked_done))
    return mentions


def evaluate() -> dict[str, Any]:
    whiteboard_text = read_text(WHITEBOARD_PATH)
    task_arch_text = read_text(TASK_ARCH_PATH)
    seed_text = read_text(CONTAINER_DIR_PATH)

    # Explicit read to satisfy dependency on this artifact.
    zip_registry = json.loads(read_text(ZIP_REGISTRY_PATH))

    whiteboard = parse_whiteboard(whiteboard_text)
    task_arch = parse_task_architecture(task_arch_text)
    seed_ids = parse_seed_container_ids(seed_text)
    card_counts = scan_card_status_counts(CARDS_PATH)

    optional_32_35 = {cid for cid in seed_ids if re.fullmatch(r'CX-(3[2-5])', cid)}
    expected = sorted(EXPECTED_CORE_CONTAINERS | optional_32_35)

    in_task_arch = set(task_arch.keys())
    in_whiteboard_rows = {row['id'] for row in whiteboard['task_rows'] if CX_PATTERN.fullmatch(row['id'])}
    in_whiteboard_mentions = set(whiteboard['cx_mentions'])

    # Coverage is based on structured indices only. Free-form mention text can
    # include speculative or historical references and should not satisfy the
    # container presence requirement.
    present_in_structured_sources = in_task_arch | in_whiteboard_rows
    missing_containers = [cid for cid in expected if cid not in present_in_structured_sources]

    status_mismatches = []
    ids_with_structured_status = sorted(set(task_arch) | set(whiteboard['row_status_by_id']))
    for cid in ids_with_structured_status:
        arch_status = task_arch.get(cid)
        wb_status = whiteboard['row_status_by_id'].get(cid)

        arch_is_done = arch_status == 'DONE'
        wb_is_done = wb_status == 'DONE'

        if arch_is_done != wb_is_done:
            status_mismatches.append({
                'id': cid,
                'task_arch_status': arch_status,
                'whiteboard_status': wb_status,
                'reason': 'done_state_mismatch',
            })

    header_card = whiteboard['header']['cards_generated']
    actual_card = card_counts['generated_like']
    stale_header_numbers = []
    if header_card is None:
        stale_header_numbers.append({
            'field': 'cards_generated',
            'reason': 'missing_header_value',
            'expected': actual_card,
            'actual': None,
            'delta': None,
        })
    else:
        delta = abs(header_card - actual_card)
        if delta > 2:
            stale_header_numbers.append({
                'field': 'cards_generated',
                'header_value': header_card,
                'actual_value': actual_card,
                'delta': delta,
            })

    blocker_issues = []
    for row in whiteboard['task_rows']:
        blockers = blocker_mentions(row['blocker'])
        if not blockers:
            continue

        for blocker_id, marked_done in blockers:
            status = task_arch.get(blocker_id)
            if status is None:
                status = whiteboard['row_status_by_id'].get(blocker_id)

            is_done = status == 'DONE'
            if marked_done and not is_done:
                blocker_issues.append({
                    'task_id': row['id'],
                    'task': row['task'],
                    'blocker': blocker_id,
                    'blocker_status': status,
                    'reason': 'marked_resolved_but_not_done',
                })

    checks = {
        'container_coverage': len(missing_containers) == 0,
        'status_consistency_done_sync': len(status_mismatches) == 0,
        'header_card_count': len(stale_header_numbers) == 0,
        'blocker_consistency': len(blocker_issues) == 0,
        'zip_registry_readable': isinstance(zip_registry, list) and len(zip_registry) > 0,
    }

    passed = sum(1 for ok in checks.values() if ok)
    total = len(checks)

    return {
        'checks': checks,
        'missing_containers': missing_containers,
        'status_mismatches': status_mismatches,
        'stale_header_numbers': stale_header_numbers,
        'blocker_inconsistencies': blocker_issues,
        'summary': f'Negotiosum health: {passed}/{total} checks passed',
        'details': {
            'whiteboard_header': whiteboard['header'],
            'whiteboard_task_row_count': len(whiteboard['task_rows']),
            'whiteboard_cx_mentions': whiteboard['cx_mentions'],
            'task_arch_count': len(task_arch),
            'expected_container_count': len(expected),
            'card_counts': card_counts,
        },
    }


def print_human(result: dict[str, Any]) -> None:
    print('Negotiosum Validator')
    print('════════════════════════════════')

    for name, ok in result['checks'].items():
        status = 'PASS' if ok else 'FAIL'
        print(f'- {name}: {status}')

    print('\nMissing containers:')
    if result['missing_containers']:
        for cid in result['missing_containers']:
            print(f'  - {cid}')
    else:
        print('  - none')

    print('\nStatus mismatches:')
    if result['status_mismatches']:
        for item in result['status_mismatches']:
            print(
                f"  - {item['id']}: TASK-ARCH={item['task_arch_status']} vs "
                f"whiteboard={item['whiteboard_status']} ({item['reason']})"
            )
    else:
        print('  - none')

    print('\nStale header numbers:')
    if result['stale_header_numbers']:
        for item in result['stale_header_numbers']:
            if item.get('field') == 'cards_generated' and 'header_value' in item:
                print(
                    f"  - cards_generated header={item['header_value']} actual={item['actual_value']} "
                    f"(delta={item['delta']})"
                )
            else:
                print(f"  - {item}")
    else:
        print('  - none')

    print('\nBlocker inconsistencies:')
    if result['blocker_inconsistencies']:
        for item in result['blocker_inconsistencies']:
            print(
                f"  - task {item['task_id']} ({item['task']}): blocker {item['blocker']} "
                f"status={item['blocker_status']} ({item['reason']})"
            )
    else:
        print('  - none')

    print()
    print(result['summary'])


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate Negotiosum consistency.')
    parser.add_argument('--json', action='store_true', help='Emit machine-readable JSON output')
    args = parser.parse_args()

    result = evaluate()

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_human(result)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
