#!/usr/bin/env python3
"""Deck readiness matrix across the 5-lane campaign model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from collections import Counter, defaultdict

NON_EMPTY_COSMO_STATUSES = {"GENERATED", "GENERATED-V2", "CANONICAL", "COMPLETE", "PUBLISHED"}
GENERATED_STATUSES = {"GENERATED", "GENERATED-V2", "CANONICAL", "GENERATED-V2-REGEN-NEEDED", "REGEN-NEEDED", "GENERATED-REGEN-NEEDED"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    txt = path.read_text(encoding="utf-8", errors="ignore")
    lines = txt.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def bool_icon(v: bool) -> str:
    return "✅" if v else "❌"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def run(repo_root: Path, registry_path: Path, audit_dir: Path) -> None:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    by_deck = defaultdict(list)
    for row in registry:
        by_deck[int(row["deck_number"])].append(row)

    cards_by_zip = {}
    for card in (repo_root / "cards").rglob("*.md"):
        if card.name == "AGENTS.md":
            continue
        fm = parse_frontmatter(card)
        zip_code = fm.get("zip", "")
        if zip_code:
            cards_by_zip[zip_code] = fm

    rows = []
    for deck in range(1, 43):
        zips = by_deck.get(deck, [])
        if not zips:
            rows.append([f"{deck:02d}", "0", "❌", "❌", "0", "0", "0", "0", "❌", "❌"])
            continue

        # Cosmogram lane
        cosmogram = repo_root / "deck-cosmograms" / f"deck-{deck:02d}-cosmogram.md"
        has_cosmogram = cosmogram.exists()
        cosmo_non_stub = False
        if has_cosmogram:
            status = parse_frontmatter(cosmogram).get("status", "").upper()
            if status in NON_EMPTY_COSMO_STATUSES:
                cosmo_non_stub = True
            elif status and "STUB" not in status:
                cosmo_non_stub = True

        # Identity lane
        identity = repo_root / "deck-identities" / f"deck-{deck:02d}-identity.md"
        has_identity = identity.exists()

        # Cards lane
        status_counts = Counter()
        for z in zips:
            fm = cards_by_zip.get(z["emoji_zip"], {})
            status_counts[fm.get("status", "MISSING")] += 1

        generated = sum(status_counts[s] for s in GENERATED_STATUSES)
        empty = status_counts.get("EMPTY", 0)
        canonical = status_counts.get("CANONICAL", 0)
        regen = status_counts.get("REGEN-NEEDED", 0) + status_counts.get("GENERATED-V2-REGEN-NEEDED", 0) + status_counts.get("GENERATED-REGEN-NEEDED", 0)

        # Audit lane
        audit_candidates = [
            audit_dir / f"deck-{deck:02d}-audit.md",
            audit_dir / f"deck-{deck:02d}.md",
            repo_root / "scripts" / "audits" / f"deck-{deck:02d}-audit.md",
            repo_root / "scripts" / "audits" / f"deck-{deck:02d}.md",
        ]
        has_audit = any(p.exists() for p in audit_candidates)

        canonical_lane = canonical == len(zips) and len(zips) > 0

        rows.append([
            f"{deck:02d}",
            str(len(zips)),
            f"{bool_icon(has_cosmogram)} / {bool_icon(cosmo_non_stub)}",
            bool_icon(has_identity),
            str(generated),
            str(empty),
            str(canonical),
            str(regen),
            bool_icon(has_audit),
            bool_icon(canonical_lane),
        ])

    print("# Deck Readiness Matrix")
    print()
    print("Cosmogram column format: `exists / non-stub`.")
    print()
    print(markdown_table(
        ["Deck", "Zips", "Cosmogram", "Identity", "Generated", "Empty", "Canonical", "Regen", "Audit", "Canonical Lane"],
        rows,
    ))


def main() -> None:
    ap = argparse.ArgumentParser(description="Check all 42 decks across campaign readiness lanes.")
    default_root = Path(__file__).resolve().parents[1]
    ap.add_argument("--repo-root", type=Path, default=default_root)
    ap.add_argument("--zip-registry", type=Path, default=default_root / "middle-math" / "zip-registry.json")
    ap.add_argument("--audit-dir", type=Path, default=default_root / "audits")
    args = ap.parse_args()
    run(args.repo_root.resolve(), args.zip_registry.resolve(), args.audit_dir.resolve())


if __name__ == "__main__":
    main()
