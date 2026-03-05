#!/usr/bin/env python3
"""Repository inventory and progress truth table report."""

from __future__ import annotations

import argparse
from pathlib import Path
from collections import Counter

CARD_GENERATED = {"GENERATED", "GENERATED-V2"}
CARD_REGEN = {"REGEN-NEEDED", "GENERATED-V2-REGEN-NEEDED", "GENERATED-REGEN-NEEDED"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)


def classify_weight_status(path: Path) -> str:
    body = path.read_text(encoding="utf-8", errors="ignore")
    for line in body.splitlines()[:20]:
        if "status" in line.lower():
            upper = line.upper()
            if "COMPLETE" in upper:
                return "COMPLETE"
            if "STUB" in upper:
                return "STUB"
            if "DRAFT" in upper:
                return "DRAFT"
    upper = body.upper()
    if "STUB" in upper:
        return "STUB"
    if "DRAFT" in upper:
        return "DRAFT"
    if "COMPLETE" in upper:
        return "COMPLETE"
    return "UNKNOWN"


def run(repo_root: Path) -> None:
    top_level_dirs = sorted([p for p in repo_root.iterdir() if p.is_dir() and p.name != ".git"], key=lambda p: p.name)

    dir_rows: list[list[str]] = []
    total_repo_files = 0
    for d in top_level_dirs:
        file_count = sum(1 for p in d.rglob("*") if p.is_file())
        total_repo_files += file_count
        dir_rows.append([d.name, str(file_count)])
    root_files = sum(1 for p in repo_root.iterdir() if p.is_file())
    total_repo_files += root_files

    cards_dir = repo_root / "cards"
    card_status = Counter()
    for card in cards_dir.rglob("*.md"):
        if card.name == "AGENTS.md":
            continue
        status = parse_frontmatter(card).get("status", "UNKNOWN")
        card_status[status] += 1

    seeds_total = sum(1 for _ in (repo_root / "seeds").rglob("*.md")) if (repo_root / "seeds").exists() else 0
    identities_total = sum(1 for p in (repo_root / "deck-identities").glob("deck-*-identity.md")) if (repo_root / "deck-identities").exists() else 0
    cosmograms_total = sum(1 for p in (repo_root / "deck-cosmograms").glob("deck-*-cosmogram.md")) if (repo_root / "deck-cosmograms").exists() else 0
    scripts_total = sum(1 for p in (repo_root / "scripts").rglob("*") if p.is_file()) if (repo_root / "scripts").exists() else 0

    weight_dir = repo_root / "middle-math" / "weights"
    weight_files = sorted([p for p in weight_dir.glob("*-weights.md") if p.is_file()]) if weight_dir.exists() else []
    weight_status = Counter(classify_weight_status(p) for p in weight_files)

    summary_rows = [
        ["Total repository files", str(total_repo_files)],
        ["Card stubs (EMPTY)", str(card_status.get("EMPTY", 0))],
        ["Card generated (GENERATED, GENERATED-V2)", str(sum(card_status[s] for s in CARD_GENERATED))],
        ["Card canonical (CANONICAL)", str(card_status.get("CANONICAL", 0))],
        ["Card regen-needed", str(sum(card_status[s] for s in CARD_REGEN))],
        ["Total seeds (.md)", str(seeds_total)],
        ["Total deck identities", str(identities_total)],
        ["Total cosmograms", str(cosmograms_total)],
        ["Total scripts (files)", str(scripts_total)],
        ["Weight declaration files", str(len(weight_files))],
        ["Weight status: DRAFT", str(weight_status.get("DRAFT", 0))],
        ["Weight status: STUB", str(weight_status.get("STUB", 0))],
        ["Weight status: COMPLETE", str(weight_status.get("COMPLETE", 0))],
    ]

    print("# Repository Inventory")
    print()
    print(markdown_table(["Directory", "File Count"], [[".", str(root_files)]] + dir_rows))
    print()
    print("# Progress Summary")
    print()
    print(markdown_table(["Metric", "Value"], summary_rows))


def main() -> None:
    ap = argparse.ArgumentParser(description="Scan repository inventory and progress totals.")
    ap.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    args = ap.parse_args()
    run(args.repo_root.resolve())


if __name__ == "__main__":
    main()
