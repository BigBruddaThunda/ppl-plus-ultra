---
phase: 02-core-data
plan: 03
subsystem: canvas/parser
tags: [keyword-dictionary, scl-vocabulary, fitness-terms, dimension-mapping]
requirements: [PARS-02]

dependency_graph:
  requires:
    - canvas/src/types/scl.ts (W enum positions 1-26)
  provides:
    - canvas/src/parser/keywords.ts (KeywordEntry interface, DimensionId type)
    - canvas/data/dial-keywords.json (2,005 fitness term entries)
  affects:
    - Phase 3 text scorer (consumes this dictionary)
    - Voice parser (vocabulary layer bridge)

tech_stack:
  added: []
  patterns:
    - TDD RED/GREEN cycle for data artifact
    - Generator script pattern (build-keywords.mjs) for reproducible JSON data

key_files:
  created:
    - canvas/src/parser/keywords.ts
    - canvas/data/dial-keywords.json
    - canvas/tests/keyword-dict.test.ts
    - canvas/scripts/build-keywords.mjs
  modified: []

decisions:
  - "DimensionId covers positions 1-26 only (4 zip dials); Blocks/Operators not in keyword space"
  - "barbell maps to dim 21 (Structured) as primary color dimension — tier 3 equipment"
  - "Generator script (build-keywords.mjs) kept in canvas/scripts/ for reproducibility"
  - "Collision-prone words retain single primary dimension mapping; compound forms provide specificity"

metrics:
  duration_seconds: 1603
  completed_date: "2026-03-14"
  tasks_completed: 2
  files_created: 4
  files_modified: 0
---

# Phase 2 Plan 03: Keyword Dictionary Summary

**One-liner:** SCL fitness vocabulary dictionary with 2,005 terms mapped to 26 zip-code dimensions using first-party source mining and compound keyword expansion.

## What Was Built

A typed keyword dictionary bridging natural language fitness terms to SCL zip code dimensions (W positions 1–26). When a user says "heavy barbell back work," the dictionary maps:
- "heavy" → dimension 2 (Strength), affinity 4, collision_prone: true
- "barbell" → dimension 21 (Structured), affinity 7
- "back" → dimension 15 (Pull), affinity 7

### Artifacts

**`canvas/src/parser/keywords.ts`** — TypeScript interface layer:
- `DimensionId` type union (1–26)
- `KeywordEntry` interface (term, dimension, affinity_score 1–8, collision_prone, source)
- `VALID_DIMENSIONS` and `VALID_SOURCES` export arrays for guard use

**`canvas/data/dial-keywords.json`** — 2,005 entries:
- All 26 dimensions covered (min 51 per dimension, max 149)
- 21 collision-prone single words flagged
- Source attribution: `first-party` (mined from CLAUDE.md, scl-directory.md) and `voice-seed` (from voice-parser-architecture.md Layer 1)
- Compound keywords preferred over ambiguous singles
- Sorted by dimension then term

**`canvas/tests/keyword-dict.test.ts`** — 14 tests covering:
- Size constraint (>= 2,000 entries)
- Full schema validation (all 5 required fields)
- Dimension validity (1–26 only)
- Affinity score range (1–8)
- Source validity
- Specific term routing (strength→2, chest→14, lats→15, barbell→19–26, bodyweight→20, HIIT→18)
- Collision flagging (>= 5 flagged)
- Coverage (every dimension >= 10 entries)
- Deduplication (no duplicate terms)

**`canvas/scripts/build-keywords.mjs`** — Generator script that produces dial-keywords.json from inline vocabulary arrays. Reproducible, auditable, extensible.

## Test Results

```
14/14 tests pass
6,815 total canvas tests pass (0 regressions)
TypeScript exits 0
```

## Deviations from Plan

None — plan executed exactly as written.

The generator script (`build-keywords.mjs`) is an implementation detail, not a deviation. The plan called for a data authoring task; the script is the authoring mechanism and produces the required artifact.

## Self-Check: PASSED

- canvas/src/parser/keywords.ts — FOUND
- canvas/data/dial-keywords.json — FOUND
- canvas/tests/keyword-dict.test.ts — FOUND
- canvas/scripts/build-keywords.mjs — FOUND
- Commit a389c991 (RED) — FOUND
- Commit 767fe125 (GREEN) — FOUND
