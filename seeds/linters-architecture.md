# Linters Architecture

**status: PLANNED**

---

## Overview

Three-tier validation pipeline for PPL± card files.

---

## Tier 1: Markdown Structure

- Tool: `markdownlint-cli2`
- Config: `.github/linters/.markdownlint.jsonc`
- Must allow: emojis in headings, long lines, multiple H1, inline HTML
- Scope: `cards/**/*.md`

## Tier 2: Frontmatter Schema

- Tool: custom Python script (`scripts/validate-frontmatter.py`)
- Schema: `.github/linters/card-frontmatter-schema.json`
- Validates:
  - `zip` format (4 emojis from valid SCL sets)
  - `status` enum (`EMPTY` | `GENERATED` | `GENERATED-V2` | `CANONICAL`)
  - `deck` range (1–42)
  - Required fields present: `zip`, `operator`, `status`, `deck`, `order`, `axis`, `type`, `color`, `blocks`

## Tier 3: SCL Compliance

- Tool: `scripts/validate-card.py` (already exists from Session 18)
- Extended with `--all` flag for CI batch runs
- Validates:
  - Order ceiling compliance
  - GOLD gate (only 🔴 or 🟣 colors unlock GOLD exercises)
  - Barbell constraints (no barbells in 🟢 or 🟠)
  - Exercise library membership
  - Operator derivation (matches Axis × Color polarity table)
  - Block sequence (matches Order guidelines)
  - Duplicate primary exercise detection within a deck
  - Required blocks present (🧈, 🚂, 🧮)

---

## CI Pipeline

- `.github/workflows/lint.yml` — runs all 3 tiers on push/PR against `cards/`
- Local validation handled by PostToolUse hook (already active)

---

## Dependencies

- Tier 3 foundation exists (`validate-card.py` from Session 18)
- Tiers 1–2 need to be built (`validate-frontmatter.py`, markdownlint config)
- CI workflow (`lint.yml`) needs to be written

---

## Implementation Priority

- After current deck generation work stabilizes
- Does not block card generation
- Blocks merge-to-main policy (once implemented)

---

## File Locations When Built

```
.github/
├── linters/
│   ├── .markdownlint.jsonc      — Tier 1 config
│   └── card-frontmatter-schema.json  — Tier 2 schema
└── workflows/
    └── lint.yml                 — CI pipeline
scripts/
└── validate-frontmatter.py      — Tier 2 implementation
```

🧮
