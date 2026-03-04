# Codex Audit Checklist Matrix (Agents-Friendly Expansion)

Source: `seeds/codex-audit-agents-friendly-expansion.md`.

## Legend
- **Status**
  - `covered` = already automated in current scripts.
  - `partial` = some automation exists, but not full check depth from proposal.
  - `new-entrypoint` = newly defined script entry point in this patch.
- **Hard fail** = check should return non-zero when violated.

## Matrix

| ID | Proposed check | Existing automation mapping | Status | New/target entry point | Hard fail condition |
|---|---|---|---|---|---|
| A1.1 | Deck identity exists for target deck | none | new-entrypoint | `scripts/lint-scl-rules.py --deck-identity deck-identities/deck-XX-identity.md` | Missing required identity file |
| A1.2 | Primary exercise uniqueness across 8 colors per Type | `scripts/audit-exercise-coverage.py` | covered | n/a | Duplicate primary exercise in same Type |
| A1.3 | Naming pass against naming convention | none | new-entrypoint | `scripts/lint-scl-rules.py --deck <path>` (filename guardrail checks) | Title/filename convention violations |
| A1.4 | Exercise availability verification against library | `scripts/validate-card.py` (library match) | covered | n/a | Exercise not found in `exercise-library.md` |
| A2.1 | Per-card SCL constraints in generation batches | `scripts/validate-card.py` | covered | n/a | Any P0/P1 violation already checked by validator |
| A2.2 | Per-deck batch validation gate | `scripts/validate-deck.sh` | covered | n/a | One or more cards fail validation |
| A3.1 | Regen queue post-fix validation clear | `scripts/validate-deck.sh` + `scripts/audit-exercise-coverage.py` | partial | `scripts/run-full-audit.sh` | Any validator/coverage failure |
| A3.2 | Format-15 completeness | `scripts/validate-card.py` (subset only) | partial | `scripts/lint-scl-rules.py --card/--deck` | Missing required format elements |
| B1.1 | Card schema parseability | none | new-entrypoint | `scripts/check-card-schema.py --card/--deck` | Malformed frontmatter/zip/required structural fields |
| B1.2 | Tree notation + sub-block zip extraction parse | none | new-entrypoint | `scripts/check-card-schema.py --card/--deck` | Missing/invalid sub-block zip or tree notation |
| B2.1 | P0/P1 linter output in machine-readable form | partial (`validate-card.py` human output) | new-entrypoint | `scripts/lint-scl-rules.py --format json` | Any P0 violation (and optional P1 via strict mode) |
| B2.2 | Circuit adjacency logic for 🟠 | none | new-entrypoint | `scripts/lint-scl-rules.py --card/--deck` | Adjacent stations target same Type in circuit blocks |
| B2.3 | Performance block ceiling for 🏟 | `scripts/validate-card.py` | covered | n/a | Block count exceeds order ceiling |
| B3.1 | One-command local audit bundle | none | new-entrypoint | `scripts/run-full-audit.sh` | Any invoked step fails |
| C1.1 | Missing middle-math weight nodes | none | new-entrypoint | `scripts/check-weight-declarations.py --path middle-math` | Missing required weight tokens in selected files |
| C2.1 | Exercise family tree structural completeness | none | new-entrypoint | `scripts/check-exercise-family-tree.py --path middle-math` | Required family metadata fields missing |
| C3.1 | Selector executable presence/contract | none | new-entrypoint | `scripts/run-selector-prototype.py --zip <code>` | Missing selector contract outputs |
| D1.1 | Junction Next-line format + valid zip | none | new-entrypoint | `scripts/validate-junction-bridges.py --card/--deck` | Invalid `Next ->` syntax or invalid zip |
| D1.2 | Junction rationale non-empty quality floor | none | new-entrypoint | `scripts/validate-junction-bridges.py --card/--deck` | Missing rationale text after dash |
| D2.1 | Fatigue heuristic executable contract | none | new-entrypoint | `scripts/check-fatigue-model.py --input <json>` | Missing required model output fields |
| E1.1 | Card inventory truth table generation | none | new-entrypoint | `scripts/index-card-inventory.py --cards-root cards --out-json <file>` | Unknown statuses when strict flag enabled |
| E1.2 | Inventory delta by commit support | none | new-entrypoint | `scripts/index-card-inventory.py --baseline <json>` | Delta generation error |
| E2.1 | Coverage audit by primary frequency | `scripts/audit-exercise-coverage.py` (duplicate check only) | partial | `scripts/audit-exercise-coverage.py` + future freq mode | Duplicate threshold failures |
| E3.1 | Deck-level review packet assembly | none | new-entrypoint | `scripts/build-canonicalization-pack.py --deck <path>` | Missing required pack sections/artifacts |
| F1.1 | Agent handoff contract file presence/shape | none | new-entrypoint | `scripts/validate-agent-handoffs.py --path .codex/agents` | Missing required contract keys |
| F2.1 | Prompt fixture suite pass/fail runner | none | new-entrypoint | `scripts/run-agent-fixtures.py --fixtures <dir>` | Any fixture mismatch |
| F3.1 | Session protocol template presence checks | none | new-entrypoint | `scripts/validate-session-templates.py --path seeds` | Missing required templates |

## Current practical “full audit” baseline

Today, the executable baseline in this repo is:
1. `scripts/validate-deck.sh`
2. `scripts/audit-exercise-coverage.py`
3. `scripts/index-card-inventory.py`
4. `scripts/check-card-schema.py`
5. `scripts/validate-junction-bridges.py`

The remaining new entry points are created as explicit contracts so they can be incrementally implemented without changing CLI shape.
