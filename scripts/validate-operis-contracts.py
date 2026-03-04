#!/usr/bin/env python3
"""Validate Operis pipeline contract artifacts for a test-results date folder."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s)>\]]+")
TIME_RE = re.compile(r"\b\d{1,2}:\d{2}(?:\s?[APap][Mm])?\b")


class ContractViolation(Exception):
    pass


def fail(message: str) -> None:
    raise ContractViolation(message)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"Missing required artifact: {path}")
    return path.read_text(encoding="utf-8")


def section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        fail(f"Missing required section: '## {heading}'")
    start = match.end()
    next_heading = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def split_numbered_entries(block: str) -> list[str]:
    matches = list(re.finditer(r"^\d+\.\s+", block, re.MULTILINE))
    if not matches:
        return []
    entries: list[str] = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(block)
        entries.append(block[start:end].strip())
    return entries


def validate_contract_a(path: Path) -> None:
    text = read_text(path)

    beat1 = section(text, "Beat 1 — Historical Events")
    events = split_numbered_entries(beat1)
    if not events:
        fail(f"{path}: Beat 1 contains no numbered historical events")

    for idx, event in enumerate(events, start=1):
        if not URL_RE.search(event):
            fail(
                f"{path}: Beat 1 event {idx} is missing an explicit source URL"
            )

    beat2 = section(text, "Beat 2 — The Sky")
    required_fields = ["Sunrise", "Sunset", "Moonrise", "Moonset"]
    for field in required_fields:
        m = re.search(rf"^-\s*{field}\s*:\s*(.+)$", beat2, re.MULTILINE | re.IGNORECASE)
        if not m:
            fail(f"{path}: Beat 2 is missing required sky-time field '{field}'")
        value = m.group(1).strip()
        if not value:
            fail(f"{path}: Beat 2 field '{field}' is empty")
        if not TIME_RE.search(value):
            fail(
                f"{path}: Beat 2 field '{field}' must include an exact time (found: '{value}')"
            )


def validate_contract_b(path: Path) -> None:
    text = read_text(path)
    lanes_block = section(text, "Content Lanes")
    lanes = split_numbered_entries(lanes_block)
    if not lanes:
        fail(f"{path}: Content Lanes contains no numbered lanes")

    for idx, lane in enumerate(lanes, start=1):
        if not re.search(r"^\s*Sources?\s*:", lane, re.IGNORECASE | re.MULTILINE):
            fail(f"{path}: Content lane {idx} is missing an explicit source URL list")
        if not URL_RE.search(lane):
            fail(f"{path}: Content lane {idx} has a source list but no explicit URL")


def extract_frontmatter(path: Path) -> str:
    text = read_text(path)
    if not text.startswith("---\n"):
        fail(f"{path}: Missing YAML frontmatter opening delimiter '---'")
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path}: Missing YAML frontmatter closing delimiter '---'")
    return text[4:end]


def validate_contract_c(path: Path) -> None:
    fm = extract_frontmatter(path)
    lines = fm.splitlines()

    root_keys: dict[str, str] = {}
    for raw in lines:
        if raw.startswith(" ") or raw.startswith("\t"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
        if m:
            root_keys[m.group(1)] = m.group(2).strip()

    if "rooms" in root_keys:
        fail(f"{path}: Legacy key 'rooms' is not allowed; use 'sandbox-zips'")

    if "sandbox-zips" not in root_keys:
        fail(f"{path}: Missing required frontmatter key 'sandbox-zips'")

    if "sandbox-total" not in root_keys:
        fail(f"{path}: Missing required frontmatter key 'sandbox-total'")
    total_str = root_keys["sandbox-total"].strip('"\'')
    if total_str != "13":
        fail(f"{path}: 'sandbox-total' must equal 13 (found: {root_keys['sandbox-total']})")

    sibling_count = 0
    content_items: list[dict[str, str]] = []
    in_sandbox = False
    mode = None

    for raw in lines:
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()

        if indent == 0 and stripped.startswith("sandbox-zips:"):
            in_sandbox = True
            mode = None
            continue

        if indent == 0 and in_sandbox:
            break

        if not in_sandbox or not stripped:
            continue

        if indent == 2 and stripped.startswith("siblings:"):
            mode = "siblings"
            continue

        if indent == 2 and stripped.startswith("content-rooms:"):
            mode = "content"
            continue

        if mode == "siblings" and indent >= 4 and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"\'')
            if not item:
                fail(f"{path}: Empty item found in sandbox-zips.siblings")
            sibling_count += 1
            continue

        if mode == "content" and indent >= 4 and stripped.startswith("- "):
            item: dict[str, str] = {}
            rest = stripped[2:].strip()
            if rest:
                inline = re.match(r"([A-Za-z0-9_-]+)\s*:\s*(.*)$", rest)
                if inline:
                    item[inline.group(1)] = inline.group(2).strip().strip('"\'')
            content_items.append(item)
            continue

        if mode == "content" and indent >= 6 and ":" in stripped and content_items:
            key, value = stripped.split(":", 1)
            content_items[-1][key.strip()] = value.strip().strip('"\'')

    if sibling_count == 0:
        fail(f"{path}: sandbox-zips.siblings must contain at least one zip")

    if not content_items:
        fail(f"{path}: sandbox-zips.content-rooms must contain at least one room")

    for i, item in enumerate(content_items, start=1):
        zip_value = item.get("zip", "").strip()
        if not zip_value:
            fail(f"{path}: sandbox-zips.content-rooms item {i} is missing required 'zip'")

    if sibling_count + len(content_items) != 13:
        fail(
            f"{path}: sandbox-zips contains {sibling_count + len(content_items)} entries; expected 13"
        )


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Validate Operis contracts A/B/C under operis-editions/test-results/<date>/"
    )
    ap.add_argument(
        "artifacts_dir",
        help="Path to a date folder containing contract-a-research-brief.md, contract-b-content-brief.md, contract-c-operis-edition.md",
    )
    args = ap.parse_args()

    artifacts_dir = Path(args.artifacts_dir)
    if not artifacts_dir.is_dir():
        print(f"ERROR: Not a directory: {artifacts_dir}")
        return 1

    try:
        validate_contract_a(artifacts_dir / "contract-a-research-brief.md")
        validate_contract_b(artifacts_dir / "contract-b-content-brief.md")
        validate_contract_c(artifacts_dir / "contract-c-operis-edition.md")
    except ContractViolation as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"PASS: All Operis contracts validated for {artifacts_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
