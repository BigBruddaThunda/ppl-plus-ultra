#!/usr/bin/env python3
"""
CX-33 — Progress Dashboard Data Builder
Scans the PPL± repository state and outputs docs/dashboard/data/progress.json.

Run this script to regenerate the dashboard data before deploying to GitHub Pages.

Usage:
  python scripts/build-dashboard-data.py
  python scripts/build-dashboard-data.py --output path/to/progress.json
"""

import json
import re
import sys
import argparse
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CARDS_DIR = REPO_ROOT / "cards"
WHITEBOARD_PATH = REPO_ROOT / "whiteboard.md"
TASK_ARCH_PATH = REPO_ROOT / ".codex" / "TASK-ARCHITECTURE.md"
OUTPUT_PATH = REPO_ROOT / "docs" / "dashboard" / "data" / "progress.json"

# 7 Orders × 6 Axes = 42 decks
ORDERS = [
    {"pos": 1, "emoji": "🐂", "name": "Foundation"},
    {"pos": 2, "emoji": "⛽", "name": "Strength"},
    {"pos": 3, "emoji": "🦋", "name": "Hypertrophy"},
    {"pos": 4, "emoji": "🏟", "name": "Performance"},
    {"pos": 5, "emoji": "🌾", "name": "Full Body"},
    {"pos": 6, "emoji": "⚖",  "name": "Balance"},
    {"pos": 7, "emoji": "🖼", "name": "Restoration"},
]
AXES = [
    {"pos": 1, "emoji": "🏛", "name": "Basics"},
    {"pos": 2, "emoji": "🔨", "name": "Functional"},
    {"pos": 3, "emoji": "🌹", "name": "Aesthetic"},
    {"pos": 4, "emoji": "🪐", "name": "Challenge"},
    {"pos": 5, "emoji": "⌛", "name": "Time"},
    {"pos": 6, "emoji": "🐬", "name": "Partner"},
]
COLOR_SECTIONS = [
    {"color": "⚫", "name": "Ordo Operis",       "latin": "Order of the Work"},
    {"color": "🟢", "name": "Natura Operis",      "latin": "Nature of the Work"},
    {"color": "🔵", "name": "Architectura Operis","latin": "Architecture of the Work"},
    {"color": "🟣", "name": "Profundum Operis",   "latin": "The Deep Work"},
    {"color": "🔴", "name": "Fervor Operis",      "latin": "The Heat of the Work"},
    {"color": "🟠", "name": "Nuntius Operis",     "latin": "The Messenger of the Work"},
    {"color": "🟡", "name": "Lusus Operis",       "latin": "The Play of the Work"},
    {"color": "⚪", "name": "Eudaimonia Operis",  "latin": "The Flourishing of the Work"},
]


def deck_number(order_pos: int, axis_pos: int) -> int:
    return (order_pos - 1) * 6 + axis_pos


def scan_cards() -> dict:
    """
    Scan cards/ directory and count cards by status.
    Returns counts: EMPTY, GENERATED, CANONICAL, REGEN_NEEDED, total.
    Also builds a per-deck count dict keyed by deck_number.
    """
    counts = {"EMPTY": 0, "GENERATED": 0, "CANONICAL": 0, "REGEN_NEEDED": 0, "OTHER": 0}
    deck_counts = {}  # {deck_number: {"generated": int, "total": int}}

    if not CARDS_DIR.exists():
        return {"counts": counts, "deck_counts": deck_counts}

    status_re = re.compile(r'^status:\s*(\S+)', re.MULTILINE)
    deck_re = re.compile(r'^deck:\s*(\d+)', re.MULTILINE)

    for md_file in CARDS_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        # Extract status and normalize variants
        status_match = status_re.search(content)
        raw_status = status_match.group(1).upper() if status_match else "OTHER"

        # Normalize status variants:
        #   GENERATED-V2-REGEN-NEEDED → REGEN_NEEDED
        #   GENERATED-V2              → GENERATED
        #   REGEN-NEEDED              → REGEN_NEEDED
        if "REGEN" in raw_status:
            status = "REGEN_NEEDED"
        elif raw_status.startswith("GENERATED"):
            status = "GENERATED"
        elif raw_status in counts:
            status = raw_status
        else:
            status = "OTHER"

        if status in counts:
            counts[status] += 1
        else:
            counts["OTHER"] += 1

        # Extract deck number
        deck_match = deck_re.search(content)
        if deck_match:
            deck_num = int(deck_match.group(1))
            if deck_num not in deck_counts:
                deck_counts[deck_num] = {"generated": 0, "total": 0}
            deck_counts[deck_num]["total"] += 1
            if status in ("GENERATED", "CANONICAL", "REGEN_NEEDED"):
                deck_counts[deck_num]["generated"] += 1

    return {"counts": counts, "deck_counts": deck_counts}


def scan_whiteboard() -> list[dict]:
    """
    Parse whiteboard.md color sections and count DONE/OPEN tasks per section.
    Returns a list of section dicts with done/open counts.
    """
    if not WHITEBOARD_PATH.exists():
        return []

    text = WHITEBOARD_PATH.read_text(encoding="utf-8")
    results = []

    section_headers = {
        "⚫": "Ordo Operis",
        "🟢": "Natura Operis",
        "🔵": "Architectura Operis",
        "🟣": "Profundum Operis",
        "🔴": "Fervor Operis",
        "🟠": "Nuntius Operis",
        "🟡": "Lusus Operis",
        "⚪": "Eudaimonia Operis",
    }

    for color_emoji, section_name in section_headers.items():
        # Count DONE and OPEN rows in each section
        # Look for lines starting with | DONE or | OPEN in the section
        pattern = re.compile(
            rf'##\s+{re.escape(color_emoji)}.*?\n(.*?)(?=\n##|\Z)',
            re.DOTALL
        )
        match = pattern.search(text)
        done_count = 0
        open_count = 0
        if match:
            section_text = match.group(1)
            done_count = len(re.findall(r'^\|\s*DONE\s*\|', section_text, re.MULTILINE))
            open_count = len(re.findall(r'^\|\s*OPEN\s*\|', section_text, re.MULTILINE))

        results.append({
            "color": color_emoji,
            "name": section_name,
            "done": done_count,
            "open": open_count,
        })

    return results


def scan_task_architecture() -> dict:
    """
    Count DONE and PENDING containers in TASK-ARCHITECTURE.md.
    """
    if not TASK_ARCH_PATH.exists():
        return {"cx_total": 0, "cx_done": 0}

    text = TASK_ARCH_PATH.read_text(encoding="utf-8")
    done_count = len(re.findall(r'\|\s*DONE\s*\|', text))
    pending_count = len(re.findall(r'\|\s*PENDING\s*\|', text))
    in_progress_count = len(re.findall(r'\|\s*IN_PROGRESS\s*\|', text))

    return {
        "cx_total": done_count + pending_count + in_progress_count,
        "cx_done": done_count,
        "cx_pending": pending_count,
    }


def build_deck_grid(deck_counts: dict) -> list[dict]:
    """
    Build a 42-cell deck grid (7 orders × 6 axes).
    """
    grid = []
    for order in ORDERS:
        for axis in AXES:
            deck_num = deck_number(order["pos"], axis["pos"])
            deck_info = deck_counts.get(deck_num, {"generated": 0, "total": 0})
            # Ensure total is always 40 for valid decks (even if no cards scanned)
            total = max(deck_info["total"], 40) if deck_info["total"] > 0 else 40
            grid.append({
                "deck": deck_num,
                "order_pos": order["pos"],
                "order_emoji": order["emoji"],
                "order_name": order["name"],
                "axis_pos": axis["pos"],
                "axis_emoji": axis["emoji"],
                "axis_name": axis["name"],
                "generated": deck_info["generated"],
                "total": total,
            })
    return grid


def main():
    parser = argparse.ArgumentParser(description="Build PPL± progress dashboard data.")
    parser.add_argument(
        "--output", type=str, default=str(OUTPUT_PATH),
        help=f"Output path (default: {OUTPUT_PATH})"
    )
    args = parser.parse_args()
    output_path = Path(args.output)

    print("Scanning cards/...")
    card_data = scan_cards()
    counts = card_data["counts"]
    deck_counts = card_data["deck_counts"]

    print("Scanning whiteboard.md...")
    color_sections = scan_whiteboard()

    print("Scanning TASK-ARCHITECTURE.md...")
    cx_data = scan_task_architecture()

    total_cards = sum(counts.values())
    generated = counts["GENERATED"] + counts["CANONICAL"]

    deck_grid = build_deck_grid(deck_counts)

    output = {
        "card_total": 1680,
        "card_generated": generated,
        "card_canonical": counts["CANONICAL"],
        "card_empty": counts["EMPTY"],
        "card_regen_needed": counts["REGEN_NEEDED"],
        "card_other": counts["OTHER"],
        "deck_grid": deck_grid,
        "color_sections": color_sections,
        "cx_total": cx_data["cx_total"],
        "cx_done": cx_data["cx_done"],
        "cx_pending": cx_data.get("cx_pending", 0),
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Output written to {output_path}")
    print(f"  Cards generated: {generated}/1,680 ({generated/1680*100:.1f}%)")
    print(f"  CX containers:   {cx_data['cx_done']}/{cx_data['cx_total']} done")


if __name__ == "__main__":
    main()
