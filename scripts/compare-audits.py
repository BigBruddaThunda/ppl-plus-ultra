#!/usr/bin/env python3
"""compare-audits.py — Compare two Ppl± quality audit JSON reports.

Shows overall score change, per-dimension changes, per-deck changes,
flags resolved vs remaining, and top remaining issues.

Usage:
  python scripts/compare-audits.py reports/before.json reports/after.json
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def load_audit(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def delta(before: float, after: float) -> str:
    d = after - before
    sign = "+" if d > 0 else ""
    return f"{sign}{d:.1f}"


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/compare-audits.py <before.json> <after.json>")
        sys.exit(1)

    before = load_audit(sys.argv[1])
    after = load_audit(sys.argv[2])

    print("=" * 60)
    print("QUALITY AUDIT COMPARISON")
    print("=" * 60)

    # Overall
    b_overall = before["average_overall"]
    a_overall = after["average_overall"]
    print(f"\nOverall Score: {b_overall:.1f} → {a_overall:.1f} ({delta(b_overall, a_overall)})")

    # Per-dimension averages
    dims = ['color_compliance', 'exercise_type', 'parameter', 'block_sequence', 'content_depth', 'format']
    print(f"\n{'DIMENSION':<25} {'BEFORE':>8} {'AFTER':>8} {'DELTA':>8}")
    print("-" * 51)
    for dim in dims:
        b_vals = [c['scores'][dim] for c in before['cards'] if dim in c.get('scores', {})]
        a_vals = [c['scores'][dim] for c in after['cards'] if dim in c.get('scores', {})]
        b_avg = sum(b_vals) / len(b_vals) if b_vals else 0
        a_avg = sum(a_vals) / len(a_vals) if a_vals else 0
        print(f"  {dim:<23} {b_avg:>7.1f} {a_avg:>7.1f} {delta(b_avg, a_avg):>8}")

    # Flag counts
    b_flags = Counter()
    for c in before['cards']:
        for f in c.get('flags', []):
            b_flags[f.split(':')[0]] += 1

    a_flags = Counter()
    for c in after['cards']:
        for f in c.get('flags', []):
            a_flags[f.split(':')[0]] += 1

    all_flag_types = set(b_flags.keys()) | set(a_flags.keys())
    b_total = sum(b_flags.values())
    a_total = sum(a_flags.values())

    print(f"\n{'FLAG TYPE':<30} {'BEFORE':>8} {'AFTER':>8} {'DELTA':>8}")
    print("-" * 56)
    for ft in sorted(all_flag_types, key=lambda x: -(b_flags.get(x, 0))):
        b = b_flags.get(ft, 0)
        a = a_flags.get(ft, 0)
        d = a - b
        sign = "+" if d > 0 else ""
        marker = " ✅" if d < 0 else (" ⚠️" if d > 0 else "")
        print(f"  {ft:<28} {b:>7} {a:>7} {sign}{d:>7}{marker}")
    print(f"  {'TOTAL':<28} {b_total:>7} {a_total:>7} {delta(b_total, a_total):>8}")

    # Per-deck changes (show biggest movers)
    b_decks = {}
    for c in before['cards']:
        dk = c.get('deck', '?')
        if dk not in b_decks:
            b_decks[dk] = []
        b_decks[dk].append(c['scores']['overall'])

    a_decks = {}
    for c in after['cards']:
        dk = c.get('deck', '?')
        if dk not in a_decks:
            a_decks[dk] = []
        a_decks[dk].append(c['scores']['overall'])

    print(f"\n{'DECK':<10} {'BEFORE':>8} {'AFTER':>8} {'DELTA':>8}")
    print("-" * 36)
    deck_deltas = []
    for dk in sorted(b_decks.keys()):
        b_avg = sum(b_decks[dk]) / len(b_decks[dk])
        a_avg = sum(a_decks.get(dk, [0])) / max(len(a_decks.get(dk, [0])), 1)
        d = a_avg - b_avg
        deck_deltas.append((dk, b_avg, a_avg, d))

    # Show biggest positive movers first, then negatives
    for dk, b_avg, a_avg, d in sorted(deck_deltas, key=lambda x: -x[3]):
        if abs(d) >= 0.5:  # Only show significant changes
            sign = "+" if d > 0 else ""
            print(f"  Deck {dk:<5} {b_avg:>7.1f} {a_avg:>7.1f} {sign}{d:>7.1f}")

    # Remaining top issues
    print(f"\n{'='*60}")
    print("TOP REMAINING ISSUES")
    print("=" * 60)
    detail_counter = Counter()
    for c in after['cards']:
        for f in c.get('flags', []):
            detail_counter[f] += 1
    for issue, count in detail_counter.most_common(10):
        print(f"  {count:5d}  {issue}")

    print(f"\n{'='*60}")
    print(f"SUMMARY: {b_overall:.1f} → {a_overall:.1f} ({delta(b_overall, a_overall)})")
    print(f"  Flags: {b_total} → {a_total} ({delta(b_total, a_total)})")
    resolved = sum(max(0, b_flags.get(ft, 0) - a_flags.get(ft, 0)) for ft in all_flag_types)
    new_found = sum(max(0, a_flags.get(ft, 0) - b_flags.get(ft, 0)) for ft in all_flag_types)
    print(f"  Resolved: {resolved} flags")
    print(f"  New found: {new_found} flags (improved detection)")
    print("=" * 60)


if __name__ == "__main__":
    main()
