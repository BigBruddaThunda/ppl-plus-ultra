#!/usr/bin/env python3
"""Scaffold empty historical event files for all calendar days (including Feb 29)."""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "operis-editions" / "historical-events"

TEMPLATE = """---
date: {mm_dd}
status: EMPTY
events: []
envelope_version: 1
---

This date has no historical events recorded. Populate via Operis Prompt 1 (Researcher).
"""


def iter_dates_for_leap_year(year: int = 2024):
    """Yield every date in a leap year so Feb 29 is included."""
    current = date(year, 1, 1)
    end = date(year, 12, 31)
    while current <= end:
        yield current
        current += timedelta(days=1)


def scaffold_files() -> tuple[int, int]:
    """Create any missing historical-event files.

    Returns:
        (created_count, skipped_count)
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    created = 0
    skipped = 0

    for day in iter_dates_for_leap_year():
        mm_dd = day.strftime("%m-%d")
        path = OUTPUT_DIR / f"{mm_dd}.md"

        if path.exists():
            skipped += 1
            continue

        path.write_text(TEMPLATE.format(mm_dd=mm_dd), encoding="utf-8")
        created += 1

    return created, skipped


def main() -> None:
    created, skipped = scaffold_files()
    print(f"Created: {created}")
    print(f"Skipped: {skipped}")


if __name__ == "__main__":
    main()
