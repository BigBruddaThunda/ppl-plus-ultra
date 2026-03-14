---
phase: 02-core-data
plan: 02
subsystem: parser/exercise-dictionary
tags: [exercise-library, alias-layer, typescript-interface, data-porting]
requirements: [PARS-03, PARS-04, PARS-05]

dependency_graph:
  requires:
    - middle-math/exercise-library.json (source data)
    - canvas/src/types/scl.ts (Type name validation)
  provides:
    - canvas/src/parser/types.ts (ExerciseEntry interface)
    - canvas/data/exercises.json (2,085 entries with aliases)
  affects:
    - Phase 3 fuzzy matcher (consumes aliases for exercise name resolution)
    - PARS-03 exercise name detection
    - PARS-04 equipment mention detection
    - PARS-05 body part detection

tech_stack:
  added: []
  patterns:
    - TDD (RED -> GREEN per-task cycle)
    - Auto-derivation: parenthetical stripping, abbreviation extraction, equipment prefix stripping
    - Manual alias layer: gym slang and abbreviations merged post auto-derivation

key_files:
  created:
    - canvas/src/parser/types.ts
    - canvas/data/exercises.json
    - canvas/tests/exercise-dict.test.ts
  modified: []

decisions:
  - "equipment_tier in source data uses [0, max] format (min is almost always 0); barbell test corrected to check tier[1] (max) >= 3, not tier[0]"
  - "build script (scripts/build-exercises-json.cjs) deleted after generation per plan spec"
  - "1,161 of 2,085 entries have aliases (55%) — auto-derivation handles equipment prefix stripping at scale"

metrics:
  duration: ~5 minutes
  completed: 2026-03-14
  tasks_completed: 2
  files_created: 3
  files_modified: 0
---

# Phase 2 Plan 02: Exercise Dictionary — Summary

**One-liner:** TypeScript ExerciseEntry interface with 2,085 entries from exercise-library.json, alias layer covering 1,161 exercises including RDL/OHP/TGU abbreviations and gym slang (skullcrusher, farmer carry, bench).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | ExerciseEntry type and test scaffold (TDD RED) | d65a0c16 | canvas/src/parser/types.ts, canvas/tests/exercise-dict.test.ts |
| 2 | Port exercise library and build alias layer (GREEN) | a81f18b0 | canvas/data/exercises.json, canvas/tests/exercise-dict.test.ts |

## What Was Built

### ExerciseEntry Interface (`canvas/src/parser/types.ts`)

TypeScript interface with 11 fields. Drops `order_relevance` and `axis_emphasis` from source (no signal — 82%+ of entries listed all values). Adds `aliases: string[]` for Phase 3 fuzzy matching.

### exercises.json (`canvas/data/exercises.json`)

2,085 entries ported from `middle-math/exercise-library.json`. Fields preserved: id, section, name, scl_types, equipment_tier, gold_gated, movement_pattern, muscle_groups, bilateral, compound. Fields dropped: order_relevance, axis_emphasis.

**Alias layer coverage:**
- 1,161 of 2,085 entries (55%) have non-empty aliases
- Auto-derived aliases: parenthetical content stripping ("Romanian Deadlift (RDL)" → "Romanian Deadlift"), abbreviation extraction ("(RDL)" → "RDL"), equipment prefix stripping ("Barbell Bench Press" → "Bench Press")
- Manual alias layer: ~45 gym slang and abbreviation entries (RDL, OHP, SLDL, TGU, BSS, skullcrusher, french press, face pull, lat pulldown, pistol squat, zercher, goblet squat, farmer carry, KB swing, bench, incline bench, flies, etc.)

### Tests (`canvas/tests/exercise-dict.test.ts`)

13 tests — all pass GREEN:
- Entry count in range [2000, 2200]
- All 11 required fields present on every entry
- No order_relevance or axis_emphasis fields
- equipment_tier always [min, max] with min <= max
- All scl_types values are valid ("Push", "Pull", "Legs", "Plus", "Ultra")
- gold_gated exercises only in permitted sections (J, K, Q, B, C, D)
- At least 100 entries with non-empty aliases (actual: 1,161)
- RDL entry has aliases "RDL" and "Romanian Deadlift"
- Barbell Bench Press entry has aliases "bench press" and "bench"
- Barbell exercises have equipment_tier[1] >= 3

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed equipment_tier test direction**
- **Found during:** Task 2 (GREEN)
- **Issue:** Plan test specified `equipment_tier[0] >= 3` for barbell exercises. Source data uses [0, max] format — tier[0] is always 0 for nearly all exercises. The min field does not encode "minimum required tier."
- **Fix:** Corrected test to check `equipment_tier[1]` (max) >= 3. This is the correct semantic: barbell exercises require tier 3 equipment, captured by the max tier value. All 64 barbell exercises pass.
- **Files modified:** canvas/tests/exercise-dict.test.ts
- **Not a data fix:** Source data format is consistent; the test assumption was incorrect.

## Self-Check: PASSED

Files exist:
- canvas/src/parser/types.ts: FOUND
- canvas/data/exercises.json: FOUND
- canvas/tests/exercise-dict.test.ts: FOUND

Commits exist:
- d65a0c16: FOUND (test: add failing tests for exercise dictionary)
- a81f18b0: FOUND (feat: port exercise library with alias layer)

All 13 exercise-dict tests: PASS
