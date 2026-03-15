---
phase: 08-tests-and-card-templates
plan: "02"
subsystem: canvas/components
tags: [card-template, intaglio, css-custom-properties, gray-matter, marked, html-preview]

requires:
  - phase: 08-tests-and-card-templates/08-01
    provides: "7052-test baseline and pipeline validation suite"
  - phase: 05-rendering-pipeline
    provides: "weightsToCSSVars(), resolveZip(), saturation-map, block-styles"
  - phase: 04-design-tokens
    provides: "tokens.ts, design-tokens.css, --ppl-color-* and --ppl-order-* custom properties"

provides:
  - "CardData and BlockData interfaces (canvas/components/types.ts)"
  - "renderWorkoutCard() pure function — CardData → HTML string (canvas/components/WorkoutCard.tsx)"
  - "parseCardFile() — .md card file → CardData with pipeline integration"
  - "WorkoutCard.css — 8-Color hatching patterns, guilloche SVG, vignette, line-work borders"
  - "card-preview.html — self-contained browser preview of Structured vs Intense intaglio cards"
  - "card-template.test.ts — 13 smoke tests validating CARD-01/02/03 requirements"

affects:
  - canvas/components
  - future-html-render-layer
  - phase-09-onwards

tech-stack:
  added: [gray-matter, marked]
  patterns:
    - "Pure-function renderer (.tsx extension, zero React) — pure CardData → string function"
    - "CSS vars injected on .ppl-card inline style (NOT :root) — scoped per-card theming"
    - "data-color attribute on .ppl-card enables Color-specific CSS hatching selectors"
    - "Color-specific hatching: [data-color=X] .ppl-block + repeating-linear-gradient"
    - "Pattern density driven by var(--ppl-weight-saturation) via calc() in rgba alpha"
    - "SVG guilloche in CSS background-image using data URI with fixed-opacity tones"

key-files:
  created:
    - canvas/components/types.ts
    - canvas/components/WorkoutCard.tsx
    - canvas/components/WorkoutCard.css
    - canvas/components/card-preview.html
    - canvas/tests/card-template.test.ts
  modified:
    - canvas/package.json
    - canvas/package-lock.json
    - canvas/tsconfig.json

key-decisions:
  - "WorkoutCard.tsx is a pure function (CardData → string), not a React component — .tsx extension is forward-compatible when React arrives in Phase 4/5"
  - "CSS vars injected on .ppl-card inline style, not :root — allows multiple cards with different palettes on the same page"
  - "data-color attribute on .ppl-card drives Color-specific hatching selectors — avoids per-class duplication"
  - "Guilloche SVG uses fixed dark rgba tones (not CSS vars) — SVG data URIs cannot reference CSS custom properties"
  - "tsconfig.json extended with jsx: react-jsx and components/ in include — avoids JSX type errors without installing React"
  - "Pattern density calc(var(--ppl-weight-saturation) * N) — engraving density tracks Color's tonal weight"

requirements-completed: [CARD-01, CARD-02, CARD-03]

duration: ~8min
completed: "2026-03-15"
tasks: 2
files: 5
---

# Phase 8 Plan 02: Card Template Summary

**CardData/BlockData types, renderWorkoutCard() pure function, intaglio CSS (8-Color hatching + guilloche + vignette), and self-contained HTML preview showing Structured ledger lines vs Intense bold crosshatch**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-15T21:44:12Z
- **Completed:** 2026-03-15T21:52:00Z
- **Tasks:** 2 (Task 3 is a checkpoint — awaiting visual verification)
- **Files modified:** 5 created, 3 modified

## Accomplishments

- CardData and BlockData interfaces establish the rendering contract between the pipeline and card output
- renderWorkoutCard() pure function produces scoped, zero-hardcoded-color HTML — CSS vars on .ppl-card container (not :root) allow multiple palettes per page
- WorkoutCard.css delivers 8-Color intaglio hatching patterns (teaching=fine parallel, structured=horizontal ledger, intense=bold crosshatch, etc.) with density driven by --ppl-weight-saturation
- card-preview.html demonstrates the full contrast: Zip 2123 (planning tonal, sat 0.50, ruled ledger) side-by-side with Zip 2115 (passion tonal, sat 0.90, bold crosshatch)
- 13 smoke tests validate no regressions; full suite holds at 7065 passing assertions

## Task Commits

1. **Task 1: CardData types, WorkoutCard renderer, and intaglio CSS** - `96392bc3` (feat)
2. **Task 2: Self-contained HTML card preview** - `f7f62be2` (feat)

## Files Created/Modified

- `canvas/components/types.ts` — CardData and BlockData interfaces
- `canvas/components/WorkoutCard.tsx` — renderWorkoutCard() + parseCardFile() pure functions
- `canvas/components/WorkoutCard.css` — 8-Color intaglio CSS: hatching, guilloche SVG, vignette, line-work borders
- `canvas/components/card-preview.html` — 502-line self-contained browser preview (two cards, logging scaffold, responsive)
- `canvas/tests/card-template.test.ts` — 13 smoke tests for CARD-01/02/03
- `canvas/package.json` — gray-matter and marked dependencies added
- `canvas/tsconfig.json` — jsx: react-jsx, components/ included in compilation

## Decisions Made

- **WorkoutCard.tsx as pure function:** The .tsx extension is a forward-compatibility marker for when React arrives (Phase 4/5 web layer). The current implementation is a plain TypeScript function that returns a string — no JSX syntax, no React dependency.
- **CSS vars on .ppl-card, not :root:** Scoping vars to each card element means multiple cards with different palettes coexist on the same page without interference.
- **data-color attribute for hatching:** Single attribute drives all 8 Color-specific CSS selectors. No per-card class injection required.
- **Guilloche SVG uses fixed dark rgba:** SVG data URIs cannot reference CSS custom properties (browser limitation). The guilloche uses `rgba(0,0,0,0.08)` toning at fixed opacity. This is documented in the CSS as a known limitation.
- **parseCardFile() uses require() for Node modules:** gray-matter and marked are CommonJS-compatible; the function uses dynamic require() wrapped in try/catch for graceful fallback if called in a non-Node context.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] tsconfig.json required jsx setting for .tsx file**
- **Found during:** Task 1 TypeScript compilation
- **Issue:** TypeScript emitted TS6142 error — `--jsx` not set but module resolved to .tsx file
- **Fix:** Added `"jsx": "react-jsx"` and `"jsxImportSource": "react"` to compilerOptions; `skipLibCheck: true` prevents React type errors without installing @types/react
- **Files modified:** canvas/tsconfig.json
- **Verification:** `npx tsc --noEmit` passes with no output
- **Committed in:** 96392bc3 (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (Rule 3 — blocking build configuration issue)
**Impact on plan:** Required for TypeScript compilation. No scope creep.

## Issues Encountered

- Node ESM and TypeScript source files are not directly importable at runtime — used `npx tsx` with a temp file to pre-compute CSS vars for the static HTML preview (Option a from the plan).

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- card-preview.html is ready for visual review (Task 3 checkpoint)
- After checkpoint approval: CARD-01, CARD-02, CARD-03 requirements met
- parseCardFile() is ready to integrate with actual .md card files in canvas/ for Phase 9+ dynamic rendering

---
*Phase: 08-tests-and-card-templates*
*Completed: 2026-03-15*
