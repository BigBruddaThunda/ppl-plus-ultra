---
phase: 04-design-tokens
plan: 01
subsystem: design-tokens
tags: [css-arbitration, style-dictionary, culori, oklch, test-scaffold]
dependency_graph:
  requires: []
  provides:
    - 04-CSS-ARBITRATION.md
    - canvas/src/tokens/ directory
    - canvas/tests/tokens.test.ts
    - style-dictionary@4 + culori installed
  affects:
    - 04-02-PLAN.md (design-tokens.json shape and build pipeline)
    - Phase 5 rendering (weightsToCSSVars() deriver functions)
tech_stack:
  added:
    - style-dictionary@4.4.0 (canvas/ devDependency)
    - culori@4.0.2 (canvas/ devDependency)
  patterns:
    - CSS arbitration spec pattern: Owner Dial table maps every property to exactly one dial
    - W enum → tonal name bridge: COLOR_W_TO_TONAL lookup table locks Phase 5 index convention
    - Vitest .skip pattern: failing tests pre-written, activated when Plan 02 artifacts arrive
key_files:
  created:
    - .planning/phases/04-design-tokens/04-CSS-ARBITRATION.md
    - canvas/src/tokens/.gitkeep
    - canvas/tests/tokens.test.ts
  modified:
    - canvas/package.json (added style-dictionary@4.4.0, culori@4.0.2 to devDependencies)
    - canvas/package-lock.json
decisions:
  - "Double-hyphen CSS naming convention locked: --ppl-color-passion--primary (not single hyphen)"
  - "W enum index convention locked: access tokens by semantic name (tokens.colors.passion), not numeric index"
  - "OKLCH as color space locked in arbitration spec; HSL permanently excluded per research"
  - "TYPE dial declared as illustration slot owner; actual content deferred to Phase 5+ (slot exists, no values)"
  - "24 CSS property pattern families mapped, 0 dual-owned properties"
metrics:
  duration: 20m
  completed: 2026-03-14
  tasks: 2
  files_modified: 5
---

# Phase 4 Plan 1: CSS Arbitration Spec, Dependencies, Test Scaffold Summary

CSS property ownership locked, style-dictionary@4 and culori installed, and 30-test token scaffold with W enum bridge verification live.

## What Was Built

**CSS Arbitration Spec** (`.planning/phases/04-design-tokens/04-CSS-ARBITRATION.md`): The blocking Phase 5 dependency that maps every CSS custom property to exactly one dial owner. 24 property pattern families across Order (structural), Color (tonal), Axis (directional), and Type (illustration slot). Zero dual-owned properties. Includes W enum → tonal name bridge table (19=order through 26=eudaimonia) with explicit index convention guidance for Phase 5.

**Dependencies** (`canvas/package.json`): style-dictionary@4.4.0 and culori@4.0.2 installed as devDependencies. Both verified importable via ESM. `canvas/src/tokens/` directory scaffolded with `.gitkeep`.

**Token test scaffold** (`canvas/tests/tokens.test.ts`): 30 tests across 6 describe blocks. RNDR-04 tests (arbitration spec existence, Owner Dial table, W bridge table) pass immediately. RNDR-01 (Color palettes), RNDR-02 (Order typographies), RNDR-03 (Axis gradients), and Build Artifacts tests are `.skip`-marked and activate when Plan 02 produces `design-tokens.json`, `design-tokens.css`, and `tokens.ts`.

**W enum bridge** (in `tokens.test.ts` and arbitration spec): COLOR_W_TO_TONAL maps W positions 19–26 to tonal names. Five immediate bridge tests pass, verifying the mapping is correct at the scaffold level.

## Test Results

```
RNDR-04: CSS arbitration spec   3/3 PASS
COLOR_W_TO_TONAL bridge         5/5 PASS
RNDR-01 Color palettes         8/8 SKIP (Plan 02)
RNDR-02 Order typographies     6/6 SKIP (Plan 02)
RNDR-03 Axis gradients         4/4 SKIP (Plan 02)
Build Artifacts                 7/7 SKIP (Plan 02)
Total: 8 pass, 22 skip
```

## Decisions Made

1. **Double-hyphen CSS naming**: `--ppl-color-passion--primary` uses double-hyphen to separate group from property. This requires a custom style-dictionary name transform in Plan 02. Locked here as the CSS naming authority.

2. **W enum index convention**: Phase 5 must use `COLOR_W_TO_TONAL[wPosition]` lookup → `tokens.colors['passion']`, never `tokens.colors[23]`. The bridge table is now documented in two places (arbitration spec + test file) with consistent values.

3. **OKLCH permanently locked**: HSL excluded by the arbitration spec. All color values will use `oklch()` format. Out-of-gamut handling via culori's `toGamut()`.

4. **TYPE dial = illustration slot only**: `--ppl-type-*--illustrationSlot` declared but deferred. Type does not own layout or color properties.

5. **24 property families, zero conflicts**: Every edge-case property (borderRadius, shadowDepth, opacity, animationDuration, fontFamily, gridGap, saturation) resolved with a single consistent principle.

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- FOUND: `.planning/phases/04-design-tokens/04-CSS-ARBITRATION.md`
- FOUND: `canvas/src/tokens/.gitkeep`
- FOUND: `canvas/tests/tokens.test.ts`
- FOUND: commit `1c22d0d7` (Task 1 — deps + token dir)
- FOUND: commit `3799d4a1` (Task 2 — arbitration spec + test scaffold)
