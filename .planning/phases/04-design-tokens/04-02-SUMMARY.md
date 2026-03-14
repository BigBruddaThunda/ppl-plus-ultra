---
phase: 04-design-tokens
plan: 02
subsystem: canvas/tokens
tags: [design-tokens, oklch, style-dictionary, culori, css-variables, typescript]
dependency_graph:
  requires: [04-01]
  provides: [design-tokens.json, design-tokens.css, tokens.ts]
  affects: [phase-05-rendering]
tech_stack:
  added: [culori@4, style-dictionary@4, @types/node]
  patterns: [OKLCH color space, gamut clamping, double-hyphen CSS naming, typed token bridge]
key_files:
  created:
    - canvas/scripts/derive-colors.mjs
    - canvas/src/tokens/design-tokens.json
    - canvas/src/tokens/build/build-tokens.mjs
    - canvas/src/tokens/design-tokens.css
    - canvas/src/tokens/tokens.ts
  modified:
    - canvas/tests/tokens.test.ts
    - canvas/package.json
decisions:
  - "build-tokens.mjs uses direct CSS/TS generation (not style-dictionary platform API) for exact double-hyphen naming control"
  - "derive-colors.mjs uses clampChroma() not toGamut() — clampChroma preserves oklch mode while toGamut converts to display-p3"
  - "tokens.test.ts rewritten to ESM (import.meta.url, readFileSync) — Plan 01 authored with CJS require/__dirname which breaks without @types/node"
  - "@types/node installed as dev dependency for tsc --noEmit compliance"
metrics:
  duration: ~15 min
  completed: 2026-03-14
  tasks_completed: 2
  files_created: 5
  files_modified: 2
  tests_activated: 22
  tests_total: 6907
---

# Phase 4 Plan 02: Design Token Pipeline Summary

OKLCH Color palettes derived via culori with p3 gamut clamping, assembled into design-tokens.json with 8 Color entries (tonal names), 7 Order typographies, and 6 Axis gradient specs; style-dictionary-adjacent build script compiles to CSS custom properties with double-hyphen naming and a typed TypeScript export with COLOR_W_TO_TONAL bridge.

## What Was Built

### Task 1: OKLCH Color Derivation + design-tokens.json

`canvas/scripts/derive-colors.mjs` — ESM script using culori's `clampChroma()` to derive 7-property OKLCH palettes for all 8 Colors from base hue parameters. The script writes the `colors` section to `design-tokens.json` while preserving the `orders` and `axes` sections.

`canvas/src/tokens/design-tokens.json` — Master token source with three sections:
- `colors`: 8 palettes keyed by tonal name (order, growth, planning, magnificence, passion, connection, play, eudaimonia) — each with primary, secondary, background, surface, text, accent, border as `oklch(...)` strings
- `orders`: 7 typographies with distinct fontWeight, fontWeightDisplay, lineHeight, spacingMultiplier, letterSpacing, density per Order
- `axes`: 6 entries with gradientDirection, layoutFlow, typographyBias per Axis

### Task 2: Build Pipeline + Test Activation

`canvas/src/tokens/build/build-tokens.mjs` — Build script that reads design-tokens.json and writes:
- `design-tokens.css`: `:root {}` block with `--ppl-color-{tonal}--{prop}` CSS custom properties using double-hyphen separator
- `tokens.ts`: typed `const tokens = {...} as const` export + `TonalColorName`, `OrderName`, `AxisName` type aliases + `COLOR_W_TO_TONAL` bridge table mapping W positions 19-26 to tonal names

All 22 previously-skipped token tests activated. Full suite: 6907 tests, 0 failures.

## Verification

```
colors: 8  (order, growth, planning, magnificence, passion, connection, play, eudaimonia)
orders: 7  (foundation, strength, hypertrophy, performance, full-body, balance, restoration)
axes:   6  (basics, functional, aesthetic, challenge, time, partner)

grep 'oklch' design-tokens.json | head -1
  "primary": "oklch(0.2 0 0)"   ✓

grep '--ppl-color-passion--primary' design-tokens.css
  --ppl-color-passion--primary: oklch(0.42 0.1919091796875 25);   ✓

tsc --noEmit   → clean   ✓
npm test       → 6907 passed   ✓
```

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] toGamut() converts mode from oklch to display-p3**
- **Found during:** Task 1 — testing culori API
- **Issue:** `toGamut('p3')` returns a `display-p3` formatted string, not an oklch string. All palette values would have been `color(display-p3 ...)` instead of `oklch(...)`, breaking the "all palette values are oklch() strings" test.
- **Fix:** Used `clampChroma(obj, 'oklch', 'p3')` which clamps chroma to p3 gamut while preserving `oklch` mode.
- **Files modified:** canvas/scripts/derive-colors.mjs
- **Commit:** fed6c9aa

**2. [Rule 3 - Blocking] style-dictionary platform API not used for CSS output**
- **Found during:** Task 2 — exploring style-dictionary v4 platform configuration
- **Issue:** Getting exact double-hyphen naming (`--ppl-color-passion--primary`) via style-dictionary's transform pipeline would require a multi-step custom transform, format registration, and token path manipulation. Direct generation in build-tokens.mjs is deterministic and produces the exact naming required.
- **Fix:** Implemented `buildCSS()` and `buildTypeScript()` functions that loop over the source JSON directly, no style-dictionary platform needed.
- **Files modified:** canvas/src/tokens/build/build-tokens.mjs
- **Commit:** 9169f6d9

**3. [Rule 1 - Bug] tokens.test.ts used CJS patterns in ESM project**
- **Found during:** Task 2 — removing .skip markers
- **Issue:** Test file authored in Plan 01 used `require()`, `__dirname`, CJS-style filesystem access. These don't work in vitest ESM mode and would cause `__dirname is not defined` errors at runtime.
- **Fix:** Rewrote test file with `import.meta.url` based path resolution, ESM `readFileSync` import.
- **Files modified:** canvas/tests/tokens.test.ts
- **Commit:** 9169f6d9

**4. [Rule 3 - Blocking] @types/node missing for tsc --noEmit**
- **Found during:** Task 2 — running `tsc --noEmit`
- **Issue:** TypeScript couldn't resolve `fs`, `path`, `url` module types. Project had no `@types/node`.
- **Fix:** `npm install --save-dev @types/node`
- **Files modified:** canvas/package.json, canvas/package-lock.json
- **Commit:** 9169f6d9

## Commits

| Hash | Message |
|------|---------|
| fed6c9aa | feat(04-02): derive OKLCH color palettes and author design-tokens.json |
| 9169f6d9 | feat(04-02): build pipeline, CSS/TS outputs, activate token tests |

## Self-Check: PASSED

- canvas/scripts/derive-colors.mjs — FOUND
- canvas/src/tokens/design-tokens.json — FOUND (8 colors, 7 orders, 6 axes)
- canvas/src/tokens/build/build-tokens.mjs — FOUND
- canvas/src/tokens/design-tokens.css — FOUND (--ppl-color-passion--primary confirmed)
- canvas/src/tokens/tokens.ts — FOUND (COLOR_W_TO_TONAL exported)
- Commits fed6c9aa, 9169f6d9 — FOUND in git log
- npm test: 6907 passed — CONFIRMED
- tsc --noEmit: clean — CONFIRMED
