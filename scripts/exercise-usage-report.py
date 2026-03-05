#!/usr/bin/env python3
"""Exercise usage report from generated card content."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from collections import Counter, defaultdict

GENERATED_STATUSES = {
    "GENERATED",
    "GENERATED-V2",
    "CANONICAL",
    "REGEN-NEEDED",
    "GENERATED-V2-REGEN-NEEDED",
    "GENERATED-REGEN-NEEDED",
}
TYPE_EMOJIS = "🛒🪡🍗➕➖"


def parse_frontmatter_and_body(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    fm: dict[str, str] = {}
    end = 0
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, "\n".join(lines[end + 1 :])


def normalize_name(name: str) -> str:
    name = re.sub(r"\([^)]*\)", "", name)
    name = name.replace("—", " ").replace("-", " ").replace("/", " ")
    name = re.sub(r"\s+", " ", name).strip().lower()
    name = re.sub(r"[^a-z0-9 ]", "", name)
    return name


def parse_library(library_path: Path) -> tuple[dict[str, str], set[str]]:
    alias_to_canonical: dict[str, str] = {}
    canonical_set: set[str] = set()
    for line in library_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = re.match(r"^\s*\d+\.\s+(.+?)\s*$", line)
        if not m:
            continue
        name = m.group(1).strip()
        low = name.lower()
        if len(name) > 64 or ':' in name or '"' in name:
            continue
        if any(ch in name for ch in ["🐂","⛽","🦋","🏟","🌾","⚖","🖼","🛒","🪡","🍗","➕","➖"]):
            continue
        if low.startswith(("order ", "axis ", "type ", "color ", "position ", "set ")):
            continue
        if any(token in low for token in ["operator call", "block header", "frontmatter", "zip code"]):
            continue
        canonical_set.add(name)
        aliases = {name, re.sub(r"\([^)]*\)", "", name).strip()}
        for a in aliases:
            n = normalize_name(a)
            if n and n not in alias_to_canonical:
                alias_to_canonical[n] = name
    return alias_to_canonical, canonical_set


def extract_candidates(body: str) -> list[str]:
    out: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("```"):
            continue

        # Match type-emoji-formatted exercise fragments.
        for m in re.finditer(rf"[{TYPE_EMOJIS}]\s+([A-Za-z][A-Za-z0-9'’\-/ ]+)", line):
            chunk = m.group(1)
            chunk = re.split(r"\s+(?:at|x|×)\s+", chunk, maxsplit=1)[0]
            chunk = re.split(r"\s*\(|\s*—", chunk, maxsplit=1)[0]
            out.append(chunk.strip())

        # Match generic bullet exercise lines (warm-up style lines).
        m2 = re.match(r"^[-*]\s*(?:\d+(?:/side)?\s*(?:sec|min)?\s+)?([A-Za-z][A-Za-z0-9'’\-/ ]+)", line)
        if m2:
            chunk = re.split(r"\s*\(|\s*—|\s+-\s+", m2.group(1), maxsplit=1)[0]
            out.append(chunk.strip())

        # Match bold standalone exercise headings.
        m3 = re.match(rf"^\*\*[{TYPE_EMOJIS}]\s+(.+?)\*\*$", line)
        if m3:
            chunk = re.split(r"\s*\(|\s*—", m3.group(1), maxsplit=1)[0]
            out.append(chunk.strip())

    return out


def resolve_candidate(candidate: str, aliases: dict[str, str]) -> str | None:
    norm = normalize_name(candidate)
    if not norm:
        return None
    if norm in aliases:
        return aliases[norm]

    return None


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def run(repo_root: Path, library_path: Path, top_n: int) -> None:
    aliases, library_exercises = parse_library(library_path)
    frequency = Counter()
    exercise_colors: dict[str, set[str]] = defaultdict(set)

    for card in (repo_root / "cards").rglob("*.md"):
        if card.name == "AGENTS.md":
            continue
        fm, body = parse_frontmatter_and_body(card)
        status = fm.get("status", "")
        if status not in GENERATED_STATUSES:
            continue

        zip_code = fm.get("zip", "")
        color = zip_code[-1] if zip_code else "?"

        for candidate in extract_candidates(body):
            resolved = resolve_candidate(candidate, aliases)
            if resolved is None:
                continue
            frequency[resolved] += 1
            exercise_colors[resolved].add(color)

    never_used = sorted(library_exercises - set(frequency.keys()))
    gt_10 = sorted([(e, c) for e, c in frequency.items() if c > 10], key=lambda x: (-x[1], x[0]))
    one_color = sorted([(e, sorted(cs)[0], frequency[e]) for e, cs in exercise_colors.items() if len(cs) == 1], key=lambda x: (-x[2], x[0]))

    top_rows = [[name, str(count)] for name, count in frequency.most_common(top_n)]
    gt10_rows = [[name, str(count)] for name, count in gt_10] or [["(none)", "0"]]
    one_color_rows = [[name, color, str(count)] for name, color, count in one_color[:top_n]] or [["(none)", "-", "0"]]

    print("# Exercise Usage Report")
    print()
    print(markdown_table(["Metric", "Value"], [
        ["Generated cards scanned", str(sum(1 for _ in (repo_root / 'cards').rglob('*.md') if _.name != 'AGENTS.md' and parse_frontmatter_and_body(_)[0].get('status', '') in GENERATED_STATUSES))],
        ["Unique exercises used", str(len(frequency))],
        ["Exercises never used", str(len(never_used))],
        ["Exercises used > 10 times", str(len(gt_10))],
        ["Exercises used in only one color", str(len(one_color))],
    ]))
    print()
    print("## Top Exercise Frequency")
    print(markdown_table(["Exercise", "Count"], top_rows or [["(none)", "0"]]))
    print()
    print("## Exercises Used More Than 10 Times")
    print(markdown_table(["Exercise", "Count"], gt10_rows))
    print()
    print("## Exercises Used in Only One Color Variant")
    print(markdown_table(["Exercise", "Color", "Count"], one_color_rows))
    print()
    print("## Exercises Never Used (First 100)")
    never_rows = [[name] for name in never_used[:100]] or [["(none)"]]
    print(markdown_table(["Exercise"], never_rows))


def main() -> None:
    ap = argparse.ArgumentParser(description="Report exercise usage against exercise-library.md")
    root = Path(__file__).resolve().parents[1]
    ap.add_argument("--repo-root", type=Path, default=root)
    ap.add_argument("--exercise-library", type=Path, default=root / "exercise-library.md")
    ap.add_argument("--top-n", type=int, default=25)
    args = ap.parse_args()
    run(args.repo_root.resolve(), args.exercise_library.resolve(), args.top_n)


if __name__ == "__main__":
    main()
