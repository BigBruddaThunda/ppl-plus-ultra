#!/usr/bin/env python3
"""generate-abacus-report.py — PPL± Abacus Full Sort Report Generator

Produces a comprehensive markdown document mapping every zip code to its
abacus, slot type, and context.

Usage:
    python scripts/generate-abacus-report.py
    python scripts/generate-abacus-report.py --output reports/custom-name.md
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ABACUS_REGISTRY = REPO_ROOT / "middle-math" / "abacus-registry.json"
ABACUS_PROFILES_DIR = REPO_ROOT / "middle-math" / "abacus-profiles"

ORDER_EMOJIS = ["🐂", "⛽", "🦋", "🏟", "🌾", "⚖", "🖼"]
AXIS_EMOJIS = ["🏛", "🔨", "🌹", "🪐", "⌛", "🐬"]
TYPE_EMOJIS = ["🛒", "🪡", "🍗", "➕", "➖"]
COLOR_EMOJIS = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

ORDER_NAMES = {
    "🐂": "Foundation", "⛽": "Strength", "🦋": "Hypertrophy",
    "🏟": "Performance", "🌾": "Full Body", "⚖": "Balance", "🖼": "Restoration",
}
AXIS_NAMES = {"🏛": "Basics", "🔨": "Functional", "🌹": "Aesthetic", "🪐": "Challenge", "⌛": "Time", "🐬": "Partner"}
TYPE_NAMES = {"🛒": "Push", "🪡": "Pull", "🍗": "Legs", "➕": "Plus", "➖": "Ultra"}
COLOR_NAMES = {
    "⚫": "Teaching", "🟢": "Bodyweight", "🔵": "Structured", "🟣": "Technical",
    "🔴": "Intense", "🟠": "Circuit", "🟡": "Fun", "⚪": "Mindful",
}


def numeric_to_emoji(nzip: str) -> str:
    if len(nzip) != 4:
        return nzip
    try:
        o, a, t, c = int(nzip[0]), int(nzip[1]), int(nzip[2]), int(nzip[3])
        return ORDER_EMOJIS[o - 1] + AXIS_EMOJIS[a - 1] + TYPE_EMOJIS[t - 1] + COLOR_EMOJIS[c - 1]
    except (ValueError, IndexError):
        return nzip


def zip_components(nzip: str) -> tuple[str, str, str, str]:
    """Return (order_name, axis_name, type_name, color_name) for a numeric zip."""
    try:
        o, a, t, c = int(nzip[0]), int(nzip[1]), int(nzip[2]), int(nzip[3])
        return (
            ORDER_NAMES.get(ORDER_EMOJIS[o - 1], "?"),
            AXIS_NAMES.get(AXIS_EMOJIS[a - 1], "?"),
            TYPE_NAMES.get(TYPE_EMOJIS[t - 1], "?"),
            COLOR_NAMES.get(COLOR_EMOJIS[c - 1], "?"),
        )
    except (ValueError, IndexError):
        return ("?", "?", "?", "?")


def main():
    parser = argparse.ArgumentParser(description="Generate PPL± Abacus Full Sort Report")
    parser.add_argument("--output", help="Output path (default: reports/abacus-full-sort-YYYY-MM-DD.md)")
    args = parser.parse_args()

    today = date.today().isoformat()
    output_path = Path(args.output) if args.output else REPO_ROOT / "reports" / f"abacus-full-sort-{today}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load registry
    reg = json.loads(ABACUS_REGISTRY.read_text(encoding="utf-8"))
    abaci = reg["abaci"]
    dlc_packs = reg.get("dlc_packs", [])
    coverage = reg.get("coverage", {})

    # Load profiles (for identity statements)
    profiles: dict[str, dict] = {}
    if ABACUS_PROFILES_DIR.exists():
        for p in ABACUS_PROFILES_DIR.glob("*.json"):
            if p.name == "index.json":
                continue
            data = json.loads(p.read_text(encoding="utf-8"))
            profiles[data["slug"]] = data

    # Build cross-reference: zip → list of (abacus_name, slot_type, role)
    zip_xref: dict[str, list[dict]] = defaultdict(list)
    for ab in abaci:
        for nzip in ab.get("working_zips", []):
            ezip = numeric_to_emoji(nzip)
            zip_xref[ezip].append({
                "abacus": ab["name"],
                "slug": ab["slug"],
                "slot": "working",
                "role": "working",
            })
        for bonus in ab.get("bonus_zips", []):
            ezip = numeric_to_emoji(bonus["zip"])
            zip_xref[ezip].append({
                "abacus": ab["name"],
                "slug": ab["slug"],
                "slot": "bonus",
                "role": bonus.get("role", "variety"),
            })

    for pack in dlc_packs:
        for nzip in pack.get("zips", []):
            ezip = numeric_to_emoji(nzip)
            zip_xref[ezip].append({
                "abacus": f"DLC: {pack['name']}",
                "slug": pack["slug"],
                "slot": "dlc",
                "role": "dlc",
            })

    # Build report
    lines = []
    lines.append(f"# PPL± Abacus Full Sort Report")
    lines.append(f"")
    lines.append(f"Generated: {today}")
    lines.append(f"")
    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"- **{len(abaci)} abaci** across 7 domains")
    lines.append(f"- **{len(dlc_packs)} DLC expansion packs** ({sum(len(p.get('zips', [])) for p in dlc_packs)} zips)")
    lines.append(f"- **1,680 total zip codes** — {coverage.get('covered', '?')} in abaci + {coverage.get('free_agents', '?')} in DLC = 100% coverage")
    lines.append(f"- Average overlap: {coverage.get('avg_overlap', '?')} abaci per zip")
    lines.append(f"- Max overlap: {coverage.get('max_overlap', '?')} abaci for a single zip")
    lines.append(f"")

    # Domain summary
    domains = Counter(ab.get("domain", "unknown") for ab in abaci)
    lines.append(f"### Domains")
    lines.append(f"")
    for domain, count in sorted(domains.items(), key=lambda x: -x[1]):
        lines.append(f"- **{domain.title()}**: {count} abaci")
    lines.append(f"")

    # --- Abacus Directory ---
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Abacus Directory")
    lines.append(f"")

    for ab in abaci:
        slug = ab["slug"]
        profile = profiles.get(slug, {})
        identity = profile.get("identity_statement", ab.get("description", ""))
        gold = profile.get("weights", {}).get("gold_affinity", False)
        pool_total = profile.get("exercise_pool", {}).get("total", "?")

        lines.append(f"### {ab['id']}. {ab['name']}")
        lines.append(f"")
        lines.append(f"- **Domain:** {ab.get('domain', '?')} | **Axis Bias:** {ab.get('axis_bias', '?')} | **Gold:** {'Yes' if gold else 'No'}")
        lines.append(f"- **Exercise Pool:** {pool_total}")
        lines.append(f"- **Identity:** {identity}")
        lines.append(f"")

        # Working slots table
        working = ab.get("working_zips", [])
        lines.append(f"**Working Slots ({len(working)}):**")
        lines.append(f"")
        lines.append(f"| # | Zip | Emoji | Order | Axis | Type | Color |")
        lines.append(f"|---|-----|-------|-------|------|------|-------|")
        for i, nzip in enumerate(working, 1):
            ezip = numeric_to_emoji(nzip)
            o, a, t, c = zip_components(nzip)
            lines.append(f"| {i} | {nzip} | {ezip} | {o} | {a} | {t} | {c} |")
        lines.append(f"")

        # Bonus slots table
        bonus = ab.get("bonus_zips", [])
        lines.append(f"**Bonus Slots ({len(bonus)}):**")
        lines.append(f"")
        lines.append(f"| # | Zip | Emoji | Role | Order | Type | Color |")
        lines.append(f"|---|-----|-------|------|-------|------|-------|")
        for i, b in enumerate(bonus, 1):
            nzip = b["zip"]
            ezip = numeric_to_emoji(nzip)
            o, a, t, c = zip_components(nzip)
            lines.append(f"| {i} | {nzip} | {ezip} | {b.get('role', '?')} | {o} | {t} | {c} |")
        lines.append(f"")

    # --- DLC Expansion Packs ---
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## DLC Expansion Packs")
    lines.append(f"")

    for pack in dlc_packs:
        zips = pack.get("zips", [])
        theme = pack.get("theme", {})
        lines.append(f"### {pack['id'].upper()}: {pack['name']}")
        lines.append(f"")
        lines.append(f"- **Theme:** {theme.get('primary_order', '?')} {theme.get('primary_axis', '?')}")
        lines.append(f"- **Size:** {len(zips)} zips")
        lines.append(f"- **Description:** {pack.get('description', '')}")
        lines.append(f"")
        lines.append(f"| # | Zip | Emoji | Order | Axis | Type | Color |")
        lines.append(f"|---|-----|-------|-------|------|------|-------|")
        for i, nzip in enumerate(zips, 1):
            ezip = numeric_to_emoji(nzip)
            o, a, t, c = zip_components(nzip)
            lines.append(f"| {i} | {nzip} | {ezip} | {o} | {a} | {t} | {c} |")
        lines.append(f"")

    # --- Cross-Reference ---
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Cross-Reference: Zip to Abacus")
    lines.append(f"")
    lines.append(f"| Zip | Emoji | Primary Abacus | Slot | Other Appearances |")
    lines.append(f"|-----|-------|----------------|------|-------------------|")

    # Sort by numeric zip
    all_numeric_zips = set()
    for ab in abaci:
        all_numeric_zips.update(ab.get("working_zips", []))
        all_numeric_zips.update(b["zip"] for b in ab.get("bonus_zips", []))
    for pack in dlc_packs:
        all_numeric_zips.update(pack.get("zips", []))

    for nzip in sorted(all_numeric_zips):
        ezip = numeric_to_emoji(nzip)
        refs = zip_xref.get(ezip, [])
        if not refs:
            lines.append(f"| {nzip} | {ezip} | *unassigned* | — | — |")
            continue

        primary = refs[0]
        others = refs[1:]
        other_str = ", ".join(f"{r['abacus']} ({r['role']})" for r in others) if others else "—"
        lines.append(f"| {nzip} | {ezip} | {primary['abacus']} | {primary['slot']} | {other_str} |")

    lines.append(f"")

    # Write
    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    print(f"Report written: {output_path}")
    print(f"  {len(abaci)} abaci, {len(dlc_packs)} DLC packs, {len(all_numeric_zips)} zips documented")


if __name__ == "__main__":
    main()
