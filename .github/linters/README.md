# PPL± Linting Configuration

Three-tier validation pipeline for the PPL± repository.

---

## Tiers

**Tier 1: Markdown Structure (markdownlint-cli2)**
- Config: `.markdownlint.jsonc` (when written)
- Scope: `cards/**/*.md`, root `*.md` files
- Checks: heading style, code blocks, consistent formatting
- Note: Must allow emojis in headings, long lines, multiple H1s

**Tier 2: Frontmatter Schema (custom script)**
- Config: `card-frontmatter-schema.json` (when written)
- Scope: `cards/**/*.md`
- Checks: zip format (4 valid emojis), status enum, deck range,
  required fields present (zip, operator, status, deck, order,
  axis, type, color, blocks)

**Tier 3: SCL Compliance (scripts/validate-card.py extended)**
- Config: `scl-lint-config.json` (when written)
- Scope: `cards/**/*.md` with `status != EMPTY`
- Checks: Order ceiling compliance, GOLD gate, barbell constraints,
  exercise library membership, operator derivation, block sequence,
  duplicate primary exercise detection, 🧈/🚂/🧮 presence

---

## Pipeline

GitHub Actions workflow (`.github/workflows/lint.yml` when written)
runs all three tiers on push/PR against the `cards/` directory.

Local: `scripts/validate-card.py` already runs via PostToolUse hook.
CI: GitHub Actions is the gate before merge.

---

## Status: PLANNED

Directory planted. No configs written yet. The existing
`scripts/validate-card.py` is Tier 3's foundation — the linter
layer wraps it in CI and adds Tier 1 and Tier 2 around it.

See `seeds/linters-architecture.md` for the full architecture plan.

🧮
