---
phase: 02-core-data
plan: 01
subsystem: weights
tags: [weight-tables, scl, typescript, tdd]
dependency_graph:
  requires: [canvas/src/types/scl.ts]
  provides: [canvas/src/weights/index.ts, computeRawVector]
  affects: [exercise-selection, css-rendering, keyword-scoring]
tech_stack:
  added: []
  patterns: [DialWeightTable, WeightEntry, coarse-scale-enforcement, TDD-red-green]
key_files:
  created:
    - canvas/src/weights/types.ts
    - canvas/src/weights/orders.ts
    - canvas/src/weights/axes.ts
    - canvas/src/weights/type-weights.ts
    - canvas/src/weights/colors.ts
    - canvas/src/weights/blocks.ts
    - canvas/src/weights/operators.ts
    - canvas/src/weights/index.ts
    - canvas/tests/weight-tables.test.ts
  modified: []
decisions:
  - "Block and Operator weight tables exist but are NOT consumed by computeRawVector() — kept as standalone exports for downstream block/operator selection"
  - "computeRawVector() implements Steps 1-3 only (Primary, Affinity, Suppression cascade) with [-8,+8] clamp — Steps 4-5 reserved for Phase 3 resolver"
  - "Duplicate W.FUNDAMENTALS key in Foundation affinities was caught by tsc — removed in same task before commit"
metrics:
  duration: "~8 minutes"
  completed: "2026-03-14"
  tasks_completed: 2
  files_created: 9
---

# Phase 2 Plan 01: SCL Weight Tables Summary

**One-liner:** 6 typed weight tables with 60 dial entries and Float32Array computeRawVector() implementing Steps 1–3 of the SCL weight derivation formula.

## What Was Built

All 6 SCL weight tables authored as typed TypeScript modules, plus the `computeRawVector()` summation function. This is the core data layer that translates zip code semantics into numeric weight vectors — every downstream system (exercise selection, CSS rendering, keyword scoring) depends on these weights.

### Files Created

| File | Entries | Notes |
|------|---------|-------|
| `canvas/src/weights/types.ts` | — | WeightScale, WeightEntry, DialWeightTable interfaces |
| `canvas/src/weights/orders.ts` | 7 | Foundation–Restoration with block-sequence affinities |
| `canvas/src/weights/axes.ts` | 6 | Basics–Partner with operator pair affinities |
| `canvas/src/weights/type-weights.ts` | 5 | Push–Ultra with antagonist suppressions |
| `canvas/src/weights/colors.ts` | 8 | Teaching–Mindful with GOLD gate enforcement |
| `canvas/src/weights/blocks.ts` | 22 | All block types — NOT in computeRawVector |
| `canvas/src/weights/operators.ts` | 12 | All operators with polarity pair suppressions — NOT in computeRawVector |
| `canvas/src/weights/index.ts` | — | computeRawVector() + barrel re-exports |
| `canvas/tests/weight-tables.test.ts` | 26 | TDD tests: entry counts, hard rules, coarse scale, vector shape |

### computeRawVector() Contract

- Input: `(orderPos: number, axisPos: number, typePos: number, colorPos: number)`
- Output: `Float32Array(62)` — slot 0 unused, slots 1–61 for W positions 1–61
- Algorithm: Step 1 (primary +8) → Step 2 (affinity sum) → Step 3 (suppression sum) → clamp to [-8, +8]
- Only consumes the 4 dial tables (ORDERS, AXES, TYPES, COLORS)
- Blocks and Operators exported separately, not consumed here

## Key Hard Suppressions (CLAUDE.md Citations)

| Table | Position | Suppressed | Value | Rule |
|-------|----------|-----------|-------|------|
| ORDERS_WEIGHTS | 7 (Restoration) | W.GUTTER | -8 | "Never in 🖼 Restoration" |
| ORDERS_WEIGHTS | 7 (Restoration) | W.STRENGTH | -6 | Heavy loading contradicts <=55% ceiling |
| ORDERS_WEIGHTS | 7 (Restoration) | W.PERFORMANCE | -8 | Performance contradicts recovery intent |
| ORDERS_WEIGHTS | 4 (Performance) | W.VANITY | -8 | "No junk volume after the test" |
| ORDERS_WEIGHTS | 1 (Foundation) | W.GUTTER | -8 | "Never in 🐂" |
| COLORS_WEIGHTS | 5 (Intense) | W.MINDFUL | -6 | Opposite character |
| COLORS_WEIGHTS | 8 (Mindful) | W.GUTTER | -8 | "Never in ⚪ Mindful" |
| COLORS_WEIGHTS | 6 (Circuit) | W.STRENGTH | -8 | "No barbells in 🟠 Circuit" |
| TYPES_WEIGHTS | 1 (Push) | W.PULL | -6 | Direct antagonists |
| TYPES_WEIGHTS | 2 (Pull) | W.PUSH | -6 | Direct antagonists |

## Test Results

```
tests/weight-tables.test.ts — 26 tests PASSING
tests/zip-converter.test.ts — 6,762 tests PASSING (pre-existing, unaffected)
tests/exercise-dict.test.ts — 13 tests PASSING (pre-existing, unaffected)
tests/keyword-dict.test.ts  — 9 failing (pre-existing RED tests for next plan, out of scope)
```

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Duplicate W.FUNDAMENTALS key in Foundation affinities**
- **Found during:** Task 2 (tsc --noEmit)
- **Issue:** orders.ts[1].affinities had `[W.FUNDAMENTALS]` declared twice — `error TS1117: An object literal cannot have multiple properties with the same name`
- **Fix:** Removed the duplicate trailing entry (the comment-only duplicate added while writing)
- **Files modified:** canvas/src/weights/orders.ts
- **Commit:** Handled inline before Task 2 commit

## Self-Check

### Files exist
- canvas/src/weights/types.ts — FOUND
- canvas/src/weights/orders.ts — FOUND
- canvas/src/weights/axes.ts — FOUND
- canvas/src/weights/type-weights.ts — FOUND
- canvas/src/weights/colors.ts — FOUND
- canvas/src/weights/blocks.ts — FOUND
- canvas/src/weights/operators.ts — FOUND
- canvas/src/weights/index.ts — FOUND
- canvas/tests/weight-tables.test.ts — FOUND

### Commits exist
- 447d8087 — test(02-01): TDD RED phase
- 364696e3 — feat(02-01): all 6 weight tables + computeRawVector

## Self-Check: PASSED
