# Phase 2: Core Data - Validation Architecture

**Extracted from:** 02-RESEARCH.md (Validation Architecture section)
**Status:** Ready

## Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest ^3.0.0 (configured in vite.config.ts) |
| Config file | `canvas/vite.config.ts` — test block with `include: ["tests/**/*.test.ts"]` |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` (same — all tests in one suite) |

## Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| WGHT-01 | computeRawVector('2123') returns 61-element array with ⛽=+8, 🏛=+8, 🪡=+8, 🔵=+8 | unit | `cd canvas && npm test` | Wave 0 |
| WGHT-01 | computeRawVector('2123') has 🌋 Gutter ≤ -6 (Order hard suppression propagates) | unit | `cd canvas && npm test` | Wave 0 |
| WGHT-01 | computeRawVector sums clamp correctly at ±8 boundary | unit | `cd canvas && npm test` | Wave 0 |
| WGHT-02 | ORDERS_WEIGHTS[2].self === 8 | unit | `cd canvas && npm test` | Wave 0 |
| WGHT-02 | ORDERS_WEIGHTS[7].suppressions has 🌋 at -8 (Restoration hard rule) | unit | `cd canvas && npm test` | Wave 0 |
| WGHT-02 | All 6 category tables have correct entry counts (7, 6, 5, 8, 22, 12) | unit | `cd canvas && npm test` | Wave 0 |
| PARS-02 | dial-keywords.json has >= 2,000 entries | unit | `cd canvas && npm test` | Wave 0 |
| PARS-02 | "strength" → dimension 2 (W.STRENGTH) with affinity_score >= 6 | unit | `cd canvas && npm test` | Wave 0 |
| PARS-02 | "chest" → dimension 14 (W.PUSH) | unit | `cd canvas && npm test` | Wave 0 |
| PARS-03 | exercises.json has ~2,085 entries | unit | `cd canvas && npm test` | Wave 0 |
| PARS-03 | Romanian Deadlift entry has aliases including "RDL" | unit | `cd canvas && npm test` | Wave 0 |
| PARS-04 | "barbell" keyword maps to Color tier 3 range | unit | `cd canvas && npm test` | Wave 0 |
| PARS-05 | "lats" keyword maps to Type W.PULL = 15 | unit | `cd canvas && npm test` | Wave 0 |

## Sampling Rate

- **Per task commit:** `cd canvas && npm test`
- **Per wave merge:** `cd canvas && npm test` (full suite)
- **Phase gate:** Full suite green before `/gsd:verify-work`

## Wave 0 Gaps

- [ ] `canvas/tests/weight-tables.test.ts` — covers WGHT-01, WGHT-02
- [ ] `canvas/tests/keyword-dict.test.ts` — covers PARS-02, PARS-03, PARS-04, PARS-05
- [ ] No new framework installs needed — Vitest already in package.json

---

*Phase: 02-core-data*
*Extracted: 2026-03-14*
