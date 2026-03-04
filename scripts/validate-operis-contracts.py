#!/usr/bin/env python3
"""Validate Operis pipeline contract artifacts for a test-results date folder."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - fallback parser handles this case
    yaml = None

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


def _parse_contract_c_frontmatter_constrained(fm: str, path: Path) -> dict[str, object]:
    """Parse only the Contract C frontmatter subset needed for validation.

    Supported shape:
    - root scalars
    - sandbox-zips.siblings[] (strings)
    - sandbox-zips.content-rooms[] (maps with scalar fields)
    """

    data: dict[str, object] = {}
    lines = fm.splitlines()
    i = 0

    while i < len(lines):
        raw = lines[i]
        if not raw.strip():
            i += 1
            continue

        root_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if not root_match:
            fail(f"{path}: Malformed frontmatter line: '{raw}'")

        key = root_match.group(1)
        value = root_match.group(2).strip()

        if key != "sandbox-zips":
            data[key] = value.strip('"\'')
            i += 1
            if value == "":
                while i < len(lines):
                    nested_raw = lines[i]
                    if not nested_raw.strip():
                        i += 1
                        continue
                    if not nested_raw.startswith("  "):
                        break
                    i += 1
            continue

        if value:
            fail(f"{path}: 'sandbox-zips' must be a nested mapping")

        i += 1
        sandbox: dict[str, object] = {}
        while i < len(lines):
            child_raw = lines[i]
            if not child_raw.strip():
                i += 1
                continue

            if not child_raw.startswith("  "):
                break

            child = child_raw[2:]
            child_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", child)
            if not child_match:
                fail(f"{path}: Malformed sandbox-zips entry: '{child_raw}'")

            child_key = child_match.group(1)
            child_value = child_match.group(2).strip()
            if child_value:
                fail(f"{path}: 'sandbox-zips.{child_key}' must be a list")

            if child_key == "siblings":
                siblings: list[str] = []
                i += 1
                while i < len(lines):
                    item_raw = lines[i]
                    if not item_raw.strip():
                        i += 1
                        continue
                    if not item_raw.startswith("    - "):
                        break
                    item_value = item_raw[6:].strip().strip('"\'')
                    if not item_value:
                        fail(f"{path}: Empty item found in sandbox-zips.siblings")
                    siblings.append(item_value)
                    i += 1
                sandbox[child_key] = siblings
                continue

            if child_key == "content-rooms":
                content_rooms: list[dict[str, str]] = []
                i += 1
                while i < len(lines):
                    item_raw = lines[i]
                    if not item_raw.strip():
                        i += 1
                        continue
                    if not item_raw.startswith("    - "):
                        break

                    rest = item_raw[6:].strip()
                    room: dict[str, str] = {}
                    if rest:
                        inline_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", rest)
                        if not inline_match:
                            fail(
                                f"{path}: Malformed content-room list item: '{item_raw.strip()}'"
                            )
                        room[inline_match.group(1)] = inline_match.group(2).strip().strip('"\'')

                    i += 1
                    while i < len(lines):
                        field_raw = lines[i]
                        if not field_raw.strip():
                            i += 1
                            continue
                        if field_raw.startswith("    - ") or not field_raw.startswith("      "):
                            break

                        field = field_raw[6:]
                        if ":" not in field:
                            fail(
                                f"{path}: Malformed content-room field: '{field_raw.strip()}'"
                            )
                        field_key, field_value = field.split(":", 1)
                        room[field_key.strip()] = field_value.strip().strip('"\'')
                        i += 1

                    content_rooms.append(room)

                sandbox[child_key] = content_rooms
                continue

            fail(f"{path}: Unsupported key under sandbox-zips: '{child_key}'")

        data[key] = sandbox

    return data


def parse_frontmatter(path: Path) -> dict[str, object]:
    fm = extract_frontmatter(path)

    if yaml is not None:
        try:
            parsed = yaml.safe_load(fm)
        except yaml.YAMLError as exc:
            fail(f"{path}: Invalid YAML frontmatter ({exc})")
        if not isinstance(parsed, dict):
            fail(f"{path}: Frontmatter must parse to a mapping")
        return parsed

    return _parse_contract_c_frontmatter_constrained(fm, path)


def validate_contract_c(path: Path) -> None:
    frontmatter = parse_frontmatter(path)

    if "rooms" in frontmatter:
        fail(f"{path}: Legacy key 'rooms' is not allowed; use 'sandbox-zips'")

    if "sandbox-zips" not in frontmatter:
        fail(f"{path}: Missing required frontmatter key 'sandbox-zips'")

    if "sandbox-total" not in frontmatter:
        fail(f"{path}: Missing required frontmatter key 'sandbox-total'")

    total_str = str(frontmatter["sandbox-total"]).strip('"\'')
    if total_str != "13":
        fail(f"{path}: 'sandbox-total' must equal 13 (found: {frontmatter['sandbox-total']})")

    sandbox = frontmatter["sandbox-zips"]
    if not isinstance(sandbox, dict):
        fail(f"{path}: 'sandbox-zips' must be a mapping")

    siblings = sandbox.get("siblings")
    if not isinstance(siblings, list):
        fail(f"{path}: sandbox-zips.siblings must be a list")
    if len(siblings) != 8:
        fail(f"{path}: sandbox-zips.siblings must contain exactly 8 zips (found: {len(siblings)})")
    for i, item in enumerate(siblings, start=1):
        if not str(item).strip():
            fail(f"{path}: sandbox-zips.siblings item {i} is empty")

    content_items = sandbox.get("content-rooms")
    if not isinstance(content_items, list):
        fail(f"{path}: sandbox-zips.content-rooms must be a list")
    if len(content_items) != 5:
        fail(
            f"{path}: sandbox-zips.content-rooms must contain exactly 5 rooms (found: {len(content_items)})"
        )

    required_fields = ("zip", "source", "source-beat")
    for i, item in enumerate(content_items, start=1):
        if not isinstance(item, dict):
            fail(f"{path}: sandbox-zips.content-rooms item {i} must be a mapping")
        for field in required_fields:
            if not str(item.get(field, "")).strip():
                fail(
                    f"{path}: sandbox-zips.content-rooms item {i} is missing required '{field}'"
                )

    if len(siblings) + len(content_items) != 13:
        fail(
            f"{path}: sandbox-zips contains {len(siblings) + len(content_items)} entries; expected 13"
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
