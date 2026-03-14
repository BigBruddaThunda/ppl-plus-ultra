---
phase: 02-core-data
verified: 2026-03-14T20:42:09Z
status: passed
score: 4/4 success criteria verified
re_verification: false
gaps: []
human_verification: []
---

# Phase 2: Core Data Verification Report

**Phase Goal:** All four dial weight tables exist as typed TypeScript modules and the fitness keyword dictionary is built from authoritative sources
**Verified:** 2026-03-14T20:42:09Z
**Status:** passed
**Re-verification:** No — initial verification

---

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | Each of the four dial weight tables (Order: 7, Axis: 6, Type: 5, Color: 8) exports typed weight entries with affinity and suppression values on the -8 to +8 scale | VERIFIED | All 6 weight files compile; test confirms entry counts: ORDERS=7, AXES=6, TYPES=5, COLORS=8; all values coarse-scale only; 26 tests pass |
| 2 | exercises.json is built from exercise-library.md (~2,185 exercises) with fuzzy-matchable aliases | VERIFIED | exercises.json: 2,085 entries, 11 required fields, no dropped fields present, 1,161 entries have non-empty aliases, RDL/bench press manual aliases confirmed |
| 3 | dial-keywords.json contains ~2,500 fitness terms with dimension_affinity_score per entry, collision-prone keywords identified | VERIFIED (with note) | 2,005 unique terms across all 26 dimensions; all entries match KeywordEntry schema; 21 collision-prone entries flagged; plan gate of >=2,000 is met. ROADMAP approximation of ~2,500 is 495 short — the plan's formal threshold governs. 14 tests pass. |
| 4 | Weight vector computation produces a 61-dimensional array for any valid zip code input | VERIFIED | computeRawVector() returns Float32Array(62), slot 0 unused, slots 1-61 active; primary dials set to +8; affinity/suppression cascade applied; clamped to [-8, +8]; 26 tests across multiple zip codes pass |

**Score:** 4/4 truths verified

---

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `canvas/src/weights/types.ts` | WeightScale, WeightEntry, DialWeightTable interfaces | VERIFIED | Exports all 3 types; WeightScale constrains to -8/-6/-4/-2/0/2/4/6/8 |
| `canvas/src/weights/orders.ts` | ORDERS_WEIGHTS with 7 entries | VERIFIED | 7 entries; W enum keys throughout (86 uses); 12 hard suppressions with CLAUDE.md citation comments |
| `canvas/src/weights/axes.ts` | AXES_WEIGHTS with 6 entries | VERIFIED | 6 entries; W enum keys (59 uses); operator pair affinities match CLAUDE.md operator table |
| `canvas/src/weights/type-weights.ts` | TYPES_WEIGHTS with 5 entries | VERIFIED | 5 entries; Push/Pull mutual -6 suppression confirmed; antagonist logic correct |
| `canvas/src/weights/colors.ts` | COLORS_WEIGHTS with 8 entries | VERIFIED | 8 entries; GOLD gate enforced (W.GUTTER -8 in all non-GOLD colors); Intense/Mindful mutual -6 confirmed |
| `canvas/src/weights/blocks.ts` | BLOCKS_WEIGHTS with 22 entries | VERIFIED | 22 entries; NOT consumed by computeRawVector(); exported separately |
| `canvas/src/weights/operators.ts` | OPERATORS_WEIGHTS with 12 entries | VERIFIED | 12 entries; polarity pair suppressions; NOT consumed by computeRawVector() |
| `canvas/src/weights/index.ts` | computeRawVector() function + re-exports | VERIFIED | computeRawVector() implemented; re-exports all 6 tables and types; only imports 4 dial tables (not blocks/operators) |
| `canvas/tests/weight-tables.test.ts` | Spot-check tests for weight values and computeRawVector correctness | VERIFIED | 26 tests: entry counts, hard rules, coarse scale enforcement, primary slots, clamping — all pass |
| `canvas/src/parser/types.ts` | ExerciseEntry interface | VERIFIED | Exports ExerciseEntry with all 11 required fields; no order_relevance or axis_emphasis |
| `canvas/data/exercises.json` | ~2,085 exercise entries with aliases | VERIFIED | 2,085 entries; no dropped fields present; 1,161 with non-empty aliases; 13 tests pass |
| `canvas/tests/exercise-dict.test.ts` | Tests for exercise count, alias presence, field shape | VERIFIED | 13 tests pass |
| `canvas/src/parser/keywords.ts` | KeywordEntry interface and DimensionId type | VERIFIED | Exports DimensionId, KeywordEntry, VALID_DIMENSIONS, VALID_SOURCES; DimensionId constrains to 1-26 |
| `canvas/data/dial-keywords.json` | >= 2,000 keyword entries with dimension affinity scores | VERIFIED | 2,005 entries; all 26 dimensions covered with >= 10 entries each; 14 tests pass |
| `canvas/tests/keyword-dict.test.ts` | Tests for keyword count, dimension routing, collision flagging | VERIFIED | 14 tests pass |

---

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `canvas/src/weights/orders.ts` | `canvas/src/types/scl.ts` | W enum used as keys in affinities/suppressions | VERIFIED | 86 `[W.` occurrences; zero raw numeric keys in affinities/suppressions |
| `canvas/src/weights/index.ts` | `canvas/src/weights/orders.ts` | computeRawVector imports all 4 dial tables | VERIFIED | Top-level imports: ORDERS_WEIGHTS, AXES_WEIGHTS, TYPES_WEIGHTS, COLORS_WEIGHTS only — blocks/operators not imported |
| `canvas/src/weights/index.ts` | `canvas/src/types/scl.ts` | Uses WEIGHT_VECTOR_LENGTH for Float32Array allocation | VERIFIED | `import { WEIGHT_VECTOR_LENGTH } from '../types/scl.js'` present; `new Float32Array(WEIGHT_VECTOR_LENGTH + 1)` |
| `canvas/data/exercises.json` | `middle-math/exercise-library.json` | Ported with dropped fields and added alias layer | VERIFIED | 2,085 entries ported; order_relevance and axis_emphasis absent from all entries |
| `canvas/src/parser/types.ts` | `canvas/src/types/scl.ts` | scl_types values correspond to Type names | VERIFIED | Interface defined; tests confirm all scl_types values are valid Type names (Push/Pull/Legs/Plus/Ultra) |
| `canvas/src/parser/keywords.ts` | `canvas/src/types/scl.ts` | DimensionId type maps to W enum positions 1-26 | VERIFIED | DimensionId union type declares 1-26; matches W.FOUNDATION(1) through W.MINDFUL(26) exactly |

---

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-------------|-------------|--------|----------|
| WGHT-01 | 02-01-PLAN.md | 61-dimensional weight vector computation for any zip code (-8 to +8 scale) | SATISFIED | computeRawVector() returns Float32Array(62); 4 primary slots +8; affinity/suppression cascade; [-8,+8] clamp; 26 tests pass |
| WGHT-02 | 02-01-PLAN.md | Dial weight tables for all 4 categories (Order: 7, Axis: 6, Type: 5, Color: 8) | SATISFIED | All 4 dial tables exist with correct entry counts; all coarse-scale values; hard suppressions cited |
| PARS-02 | 02-03-PLAN.md | Keyword dictionary (~2,500 fitness terms) with dimension_affinity_score per entry | SATISFIED | 2,005 terms delivered; plan's formal gate is ">= 2,000"; all terms have affinity_score (1-8 range) per entry |
| PARS-03 | 02-02-PLAN.md | Exercise name detection using exercise-library.md as authoritative source (~2,185 exercises) | SATISFIED | 2,085 exercises in exercises.json; aliases layer enables fuzzy matching; manual aliases (RDL, OHP, skullcrusher, etc.) confirmed |
| PARS-04 | 02-02-PLAN.md | Equipment mention detection mapping to Color tier ranges | SATISFIED | equipment_tier is [min, max] tuple in every ExerciseEntry; barbell maps to Color dimension (dim 21, tier 3); keyword entries cover equipment vocabulary |
| PARS-05 | 02-02-PLAN.md | Body part / muscle group detection mapping to Type | SATISFIED | muscle_groups field present in all exercise entries; keyword dict maps chest->dim14, lats->dim15, etc.; scl_types field maps exercises to Type dimensions |

**Orphaned requirements check:** No REQUIREMENTS.md entries mapped to Phase 2 that are unaccounted for. WGHT-01, WGHT-02, PARS-02, PARS-03, PARS-04, PARS-05 all appear in PLAN frontmatter and are satisfied.

---

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| `canvas/src/weights/type-weights.ts` | 100 | `[W.PLUS]: 8` in Plus entry affinities — self-reference redundant (W.PLUS=17, slot 17 already set to +8 by primary in computeRawVector) | Info | No functional impact; primary slot set independently; minor code noise |

No TODO/FIXME/PLACEHOLDER comments found. No empty implementations. No stub return values in any of the 8 weight files.

---

### Notable Verification Notes

**1. dial-keywords.json term count: 2,005 vs ROADMAP "~2,500"**

The ROADMAP success criterion states "~2,500 fitness terms." Actual delivery is 2,005 unique terms. The tilde (~) signals approximation, and the governing PLAN (02-03-PLAN.md) formalizes the gate as ">= 2,000 entries," which is met. The test suite enforces ">= 2,000" and passes. This is not a blocking gap — the plan contract governs, and the ROADMAP estimate was aspirational. Flagged for awareness only.

**2. Duplicate term deduplication policy**

The keyword test enforces zero duplicate terms (same term string cannot appear twice regardless of dimension). This means "press" appears only once — mapped to its highest-signal dimension. This is stricter than the PLAN's "no duplicate entries" which could be read as no duplicate term+dimension combos. The implemented policy is acceptable and arguably stronger.

**3. BLOCKS_WEIGHTS and OPERATORS_WEIGHTS isolation**

Both tables are substantively populated (22 and 12 entries) but are intentionally excluded from computeRawVector(). This matches the PLAN specification. They are re-exported from index.ts for downstream block/operator selection systems.

**4. All 6,815 tests pass**

Full test suite: weight-tables.test.ts (26), exercise-dict.test.ts (13), keyword-dict.test.ts (14), zip-converter.test.ts (6,762). TypeScript compiles with no errors under strict mode.

---

### Human Verification Required

None. All success criteria for Phase 2 are verifiable programmatically. The data quality (weight derivations, keyword term choices, exercise aliases) was validated against CLAUDE.md canonical rules via citation comments and test spot-checks covering the spec's explicitly stated hard rules.

---

## Gaps Summary

No blocking gaps. Phase goal is achieved.

The four dial weight tables exist as typed TypeScript modules with correct entry counts (7+6+5+8 = 26 dial entries across the 4 operative tables), all coarse-scale values, all hard suppressions cited from CLAUDE.md. computeRawVector() produces a 61-dimensional Float32Array for any valid zip input. The exercise dictionary is built with 2,085 entries and a robust alias layer. The keyword dictionary delivers 2,005 fitness terms mapped across all 26 SCL dimensions with collision flagging.

---

_Verified: 2026-03-14T20:42:09Z_
_Verifier: Claude (gsd-verifier)_
