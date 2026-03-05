#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ZIP_REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
WHITEBOARD_PATH = REPO_ROOT / "whiteboard.md"
TASK_ARCH_PATH = REPO_ROOT / ".codex" / "TASK-ARCHITECTURE.md"
CONTAINER_DIR_PATH = REPO_ROOT / "seeds" / "codex-container-directory-v3.md"
OUTPUT_PATH = REPO_ROOT / "docs" / "dashboard" / "data" / "progress.json"

GOOD_GENERATED_STATUSES = {"GENERATED", "GENERATED-V2", "CANONICAL"}


def parse_card_statuses() -> dict[str, str]:
    statuses: dict[str, str] = {}
    for card in (REPO_ROOT / "cards").rglob("*.md"):
        text = card.read_text(encoding="utf-8")
        zip_code = card.stem.split("±", 1)[0]
        match = re.search(r"^status:\s*([A-Z0-9-]+)\s*$", text, flags=re.MULTILINE)
        if match:
            statuses[zip_code] = match.group(1)
    return statuses


def parse_color_sections() -> list[dict[str, object]]:
    text = WHITEBOARD_PATH.read_text(encoding="utf-8")
    section_pattern = re.compile(
        r"^##\s+(?P<emoji>\S+)\s+(?P<name>[^\n—]+?)\s+—.*$", re.MULTILINE
    )
    matches = list(section_pattern.finditer(text))
    sections: list[dict[str, object]] = []

    for idx, match in enumerate(matches):
        section_name = match.group("name").strip()
        if not section_name.endswith("Operis"):
            continue

        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end]
        done = 0
        open_ = 0
        for line in block.splitlines():
            row = re.match(r"^\|\s*(DONE|OPEN|PENDING|IN_PROGRESS|BLOCKED)\s*\|", line)
            if not row:
                continue
            if row.group(1) == "DONE":
                done += 1
            else:
                open_ += 1

        sections.append(
            {
                "emoji": match.group("emoji"),
                "name": section_name,
                "done": done,
                "open": open_,
            }
        )

    return sections


def parse_cx_completion() -> tuple[int, int]:
    container_text = CONTAINER_DIR_PATH.read_text(encoding="utf-8")
    total_match = re.search(r"\|\s*Total containers\s*\|\s*(\d+)", container_text)
    cx_total = int(total_match.group(1)) if total_match else 0

    text = TASK_ARCH_PATH.read_text(encoding="utf-8")
    start = text.find("## Container Index")
    end = text.find("## Update Rule")
    block = text[start:end] if start != -1 and end != -1 else text

    cx_done = 0
    for line in block.splitlines():
        if not line.startswith("| CX-"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 5:
            continue

        id_col = cols[0]
        status_col = cols[4]
        ids = [part.strip() for part in id_col.split("/")]
        count = sum(1 for item in ids if item.startswith("CX-"))
        if status_col == "DONE":
            cx_done += count

    return cx_total, cx_done


def build() -> dict[str, object]:
    registry = json.loads(ZIP_REGISTRY_PATH.read_text(encoding="utf-8"))
    statuses = parse_card_statuses()

    totals = Counter()
    deck_totals = Counter()
    deck_generated = Counter()
    deck_identity: dict[int, dict[str, str]] = {}

    for item in registry:
        zip_code = item["emoji_zip"]
        deck_number = int(item["deck_number"])
        status = statuses.get(zip_code, "EMPTY")

        deck_totals[deck_number] += 1
        deck_identity.setdefault(
            deck_number,
            {
                "order": item["order"]["emoji"],
                "axis": item["axis"]["emoji"],
                "order_name": item["order"]["name"],
                "axis_name": item["axis"]["name"],
            },
        )

        if status in GOOD_GENERATED_STATUSES:
            totals["generated"] += 1
            deck_generated[deck_number] += 1
        elif "REGEN-NEEDED" in status:
            totals["regen"] += 1
        elif status == "EMPTY":
            totals["empty"] += 1

        if status == "CANONICAL":
            totals["canonical"] += 1

    deck_grid = []
    for deck_number in range(1, 43):
        info = deck_identity[deck_number]
        deck_grid.append(
            {
                "deck": deck_number,
                "order": info["order"],
                "axis": info["axis"],
                "order_name": info["order_name"],
                "axis_name": info["axis_name"],
                "generated": deck_generated[deck_number],
                "total": deck_totals[deck_number],
            }
        )

    cx_total, cx_done = parse_cx_completion()

    payload = {
        "card_total": len(registry),
        "card_generated": totals["generated"],
        "card_canonical": totals["canonical"],
        "card_empty": totals["empty"],
        "card_regen": totals["regen"],
        "deck_grid": deck_grid,
        "color_sections": parse_color_sections(),
        "cx_total": cx_total,
        "cx_done": cx_done,
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }
    return payload


def main() -> None:
    payload = build()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
