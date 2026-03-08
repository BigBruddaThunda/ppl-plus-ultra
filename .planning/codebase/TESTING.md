# Testing Patterns

**Analysis Date:** 2026-03-07

---

## Overview

Ppl± has no unit test framework (pytest, unittest, etc.). Validation is domain-specific: scripts validate cards against SCL rules. All validation is structural and content-based — checking format, zip codes, exercise names, block presence, and naming conventions against known good patterns.

---

## Validation Tools

### Primary Validator: `scripts/validate-card.py`

**Purpose:** Single-card validation against SCL rules.

**Usage:**
```bash
python scripts/validate-card.py <card-path>
```

**Exit codes:**
- `0` — All checks pass (or card is a stub with `status: EMPTY`)
- `1` — One or more checks failed

**What it checks (in order):**
1. Frontmatter present and parseable
2. `status` field valid (one of `EMPTY`, `GENERATED`, `GENERATED-V2`, `CANONICAL`)
3. `zip` field present and parses as ORDER AXIS TYPE COLOR
4. (Stubs exit here with pass)
5. Block count within Order × Color range
6. `🧈` Bread & Butter present (or `🎱` ARAM for Circuit)
7. `🚂` Junction present
8. `🧮` SAVE present
9. `🎯` Intention present (block or blockquote)
10. No barbell exercises in 🟠 Circuit or 🟢 Bodyweight cards
11. No GOLD exercises in non-GOLD colors (🔴 and 🟣 only allow GOLD)
12. All extracted exercises found in `exercise-library.md` (fuzzy substring match)

**Output style:**
```
Card: ⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md
Zip:  ⛽🏛🪡🔵
Status: GENERATED-V2

✅ ZIP: ⛽🏛🪡🔵 parsed as ORDER=⛽ AXIS=🏛 TYPE=🪡 COLOR=🔵
✅ BLOCK COUNT: 6 blocks (expected 5–6 for ⛽/🔵)
✅ 🧈 BREAD & BUTTER: Present
✅ 🚂 JUNCTION: Present
✅ 🧮 SAVE: Present
✅ 🎯 INTENTION: Present
✅ GOLD GATE: No GOLD exercises in non-GOLD color 🔵 (correct)
✅ EXERCISE LIBRARY: All 12 exercises found in library

✅ PASS: ⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md
```

---

### Deck Validator: `scripts/validate-deck.sh`

**Purpose:** Runs `validate-card.py` on every `.md` file in a deck folder recursively.

**Usage:**
```bash
bash scripts/validate-deck.sh cards/⛽-strength/🏛-basics/
```

**Exit codes:** `0` if all pass, `1` if any fail.

**Skips:** `AGENTS.md` files. Stub cards (`status: EMPTY`) counted separately, not as failures.

**Summary output:**
```
Summary: 22 passed, 0 failed, 18 stubs skipped
✅ All checks passed
```

---

### Schema Checker: `scripts/check-card-schema.py`

**Purpose:** Stricter frontmatter and structural schema enforcement. Supplements `validate-card.py`.

**Usage:**
```bash
python scripts/check-card-schema.py --card <path>
python scripts/check-card-schema.py --deck <path>
python scripts/check-card-schema.py --deck <path> --json
```

**What it checks beyond `validate-card.py`:**
- Sub-block zip markers present (regex: `BLOCK+TYPE+AXIS+COLOR` pattern)
- Tree notation complete: requires both `├─` and `│` markers
- Extended status allow-list: includes `REGEN-NEEDED`, `GENERATED-V2-REGEN-NEEDED`

**Hard failures** (exit 1): missing frontmatter, missing zip, malformed zip, missing transformation anchor, missing `🚂`, missing `🧮`, missing sub-block zip markers, incomplete tree notation.

---

### Junction Bridge Validator: `scripts/validate-junction-bridges.py`

**Purpose:** Validates `Next -> [zip] — rationale` lines in the `🚂` Junction block.

**Usage:**
```bash
python scripts/validate-junction-bridges.py --card <path>
python scripts/validate-junction-bridges.py --deck <path>
```

**Pattern it enforces:**
```python
NEXT_PATTERN = re.compile(r'^\s*Next\s*->\s*([^\s]+)\s*[—-]\s*(.+?)\s*$', re.IGNORECASE)
```

**Hard failures:**
- Malformed `Next ->` syntax
- Invalid zip code format in the bridge
- Rationale text shorter than 5 characters

---

### Exercise Coverage Auditor: `scripts/audit-exercise-coverage.py`

**Purpose:** Within a deck (one Order × Axis combination), checks that no two Color variants of the same Type share the same primary exercise in the `🧈` Bread & Butter block.

**Usage:**
```bash
python scripts/audit-exercise-coverage.py cards/⛽-strength/🔨-functional/
```

**What it reports:**
- Primary exercise extracted per generated card, grouped by Type
- Flags duplicates: same exercise used by two Colors in the same Type
- Stubs (status: EMPTY) are skipped

**Output:**
```
🪡 Pull:
  🔵 Structured     — Barbell Row
  🟣 Technical      — Barbell Row
  ❌ DUPLICATE: 'barbell row' used in both 🔵 Structured and 🟣 Technical
```

---

### SCL Lint Aggregator: `scripts/lint-scl-rules.py`

**Purpose:** Orchestrates existing validators and adds filename convention checking. Entry point for `--card` or `--deck` targets.

**Usage:**
```bash
python scripts/lint-scl-rules.py --card <path>
python scripts/lint-scl-rules.py --deck <path>
python scripts/lint-scl-rules.py --deck <path> --deck-identity <path>
python scripts/lint-scl-rules.py --card <path> --format json
```

**Filename convention rule:**
- `±` must be present in filename
- If not a stub (i.e., filename doesn't end at `±`), the segment after `±` must match `±\S+\s+.+` (operator + space + title)

**Exit:** `1` on any hard failure, `0` if clean.

---

### Full Audit Orchestrator: `scripts/run-full-audit.sh`

**Purpose:** One command runs the complete baseline validation sequence for a deck.

**Usage:**
```bash
bash scripts/run-full-audit.sh cards/⛽-strength/🏛-basics/
bash scripts/run-full-audit.sh --require-all-checks cards/⛽-strength/🏛-basics/
```

**Baseline sequence (6 steps, always runs):**
```
[1/6] scripts/lint-scl-rules.py --deck
[2/6] scripts/validate-deck.sh
[3/6] scripts/audit-exercise-coverage.py
[4/6] scripts/check-card-schema.py --deck
[5/6] scripts/validate-junction-bridges.py --deck
[6/6] scripts/index-card-inventory.py (writes artifacts to scripts/.artifacts/)
```

**Strict mode (`--require-all-checks`):** Invokes 8 additional contract-stub scripts with `--require-implementation`. These stubs exit `2` until implemented, so strict mode fails until all stubs are built out.

---

## Fixture Files

**Location:** `scripts/fixtures/schema/`

These are minimal valid/invalid card `.md` files used as known-good test cases:

| File | Purpose |
|------|---------|
| `generated-compliant-tree.md` | Minimal compliant generated card with correct tree notation |
| `generated-missing-tree.md` | Card missing tree notation — expected to fail schema check |
| `generated-regen-needed-compliant-tree.md` | REGEN-NEEDED status card with valid structure |
| `generated-tree-only-branch.md` | Card with `├─` but no `│` continuation — partial tree |
| `generated-tree-only-continuation.md` | Card with `│` but no `├─` branch — partial tree |

**Fixture frontmatter format:**
```yaml
---
status: GENERATED
zip: ⛽🏛🪡🔵
---
```

**Note:** `scripts/run-agent-fixtures.py` is scaffolded (CLI locked) but not yet implemented. Fixture-based automated testing is planned, not active.

---

## Automated Validation Hook

**PostToolUse hook** (configured in project automation layer): Automatically runs `scripts/validate-card.py` on any file modified under `cards/` after an Edit or Write tool call. This means every card generation triggers immediate validation without manual invocation.

**SessionStart hook**: Runs `scripts/progress-report.py` at session start and displays generation dashboard.

---

## Reporting Scripts

### Progress Dashboard: `scripts/progress-report.py`

```bash
python scripts/progress-report.py
```

Scans `cards/` and emits:
- Total generated / 1,680 with percentage
- By-Order breakdown (each Order = 240 cards)
- By-Axis breakdown (each Axis = 280 cards)
- Completed decks (40/40)
- Partial decks
- Anomalies (unexpected file counts)

### Deck Readiness Matrix: `scripts/deck-readiness.py`

```bash
python scripts/deck-readiness.py
```

Requires `middle-math/zip-registry.json`. Outputs a 42-deck matrix with columns: Cosmogram, Identity, Generated, Empty, Canonical, Regen, Audit, Canonical Lane.

### Repository Inventory: `scripts/inventory.py`

```bash
python scripts/inventory.py
```

Emits file counts by directory, card status counts, seed/identity/cosmogram totals, and weight declaration status.

### Exercise Usage Report: `scripts/exercise-usage-report.py`

```bash
python scripts/exercise-usage-report.py
```

Checks exercise coverage across all generated cards.

---

## Contract-Stub Scripts (Not Yet Implemented)

These scripts have locked CLI contracts but print `"Entry point defined. Implementation pending."` and exit cleanly unless `--require-implementation` is passed:

- `scripts/check-weight-declarations.py` — Validates middle-math weight declarations
- `scripts/check-exercise-family-tree.py` — Validates exercise family groupings
- `scripts/run-selector-prototype.py` — Tests the exercise selection algorithm
- `scripts/check-fatigue-model.py` — Validates fatigue model declarations
- `scripts/build-canonicalization-pack.py` — Builds canonicalization artifacts
- `scripts/validate-agent-handoffs.py` — Validates agent handoff contracts
- `scripts/run-agent-fixtures.py` — Runs fixture-based agent tests
- `scripts/validate-session-templates.py` — Validates session template format

---

## Operis Pipeline Validator: `scripts/validate-operis-contracts.py`

**Purpose:** Validates the 3-contract Operis pipeline output (Research Brief, Content Brief, Operis Edition).

**Usage:**
```bash
python scripts/validate-operis-contracts.py operis-editions/test-results/2024-07-26/
```

**What it enforces:**
- `contract-a-research-brief.md`: historical events have source URLs, sky-time fields present
- `contract-b-content-brief.md`: content lanes have source URL lists
- `contract-c-operis-edition.md`: `sandbox-zips` exists, `sandbox-total` equals 13, legacy `rooms` key rejected

---

## Validation Coverage Summary

| Check | Tool | Auto-triggered |
|-------|------|---------------|
| Frontmatter presence and zip validity | `validate-card.py` | Yes (PostToolUse hook) |
| Block count per Order × Color | `validate-card.py` | Yes |
| Required blocks (🧈, 🚂, 🧮, 🎯) | `validate-card.py` | Yes |
| Barbell in 🟢/🟠 | `validate-card.py` | Yes |
| GOLD gate violations | `validate-card.py` | Yes |
| Exercise library membership | `validate-card.py` | Yes |
| Sub-block zip markers | `check-card-schema.py` | Manual |
| Tree notation completeness | `check-card-schema.py` | Manual |
| Junction bridge format and zip validity | `validate-junction-bridges.py` | Manual |
| Duplicate primary exercises within type | `audit-exercise-coverage.py` | Manual |
| Filename convention | `lint-scl-rules.py` | Manual |
| Deck identity existence | `lint-scl-rules.py --deck-identity` | Manual |

---

*Testing analysis: 2026-03-07*
