# Roadmap: Ppl± Blank Canvas Infrastructure

## Overview

This roadmap builds a deterministic offline parser, weight-vector-to-CSS rendering pipeline, and Claude Code dev infrastructure across 8 phases in strict dependency order. Each phase produces a clean layer that the next phase stands on. The full pipeline — string input to rendered CSS custom properties — is only complete when all 8 phases are done, but each phase delivers independently testable, verifiable artifacts. Phases 1-7 cover the two-session infrastructure budget. Phase 8 closes the loop with tests and card templates.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Foundation** - Canvas workspace, TypeScript types, zip converter, and Claude Code path-gating infrastructure
- [ ] **Phase 2: Core Data** - Four dial weight tables and fitness keyword dictionary (parallel builds from first-party specs)
- [ ] **Phase 3: Integration** - Interaction resolver wiring weight tables into WeightVector; text scorer wiring vocab into ParseResult
- [ ] **Phase 4: Design Tokens** - design-tokens.json encoding all 8 Color palettes, 7 Order typographies, 6 Axis gradients; style-dictionary build
- [ ] **Phase 5: Rendering Pipeline** - weightsToCSSVars() and all deriver functions; CSS arbitration spec locked before code
- [ ] **Phase 6: Claude Code Infrastructure** - /blank-canvas skill, canvas-renderer subagent, PostToolUse hook, AGENT-BOUNDARIES.md
- [ ] **Phase 7: Scripts and State Persistence** - canvas-to-production.sh, batch-propagate.sh, canvas/.local/ state persistence
- [ ] **Phase 8: Tests and Card Templates** - Full Vitest suite, integration pipeline test, HTML/TSX card templates

## Phase Details

### Phase 1: Foundation
**Goal**: The canvas/ workspace exists with TypeScript types, bidirectional zip converter, and Claude Code infrastructure boundaries locked before any hooks are added
**Depends on**: Nothing (first phase)
**Requirements**: FOUND-01, FOUND-02, FOUND-03, FOUND-04, TEST-01
**Success Criteria** (what must be TRUE):
  1. `canvas/` directory exists at repo root with its own package.json, isolated from web/, middle-math/, cards/
  2. Any emoji zip code converts to its 4-digit numeric address and back without loss (all 1,680 round-trips pass)
  3. Deck number derives correctly from any zip code using (order - 1) * 6 + axis
  4. TypeScript types compile with strict mode for all SCL primitives (Order, Axis, Type, Color, Operator, Block)
  5. AGENT-BOUNDARIES.md exists documenting path-gating patterns before any canvas-specific hook is added
**Plans**: TBD

### Phase 2: Core Data
**Goal**: All four dial weight tables exist as typed TypeScript modules and the fitness keyword dictionary is built from authoritative sources
**Depends on**: Phase 1
**Requirements**: WGHT-01, WGHT-02, PARS-02, PARS-03, PARS-04, PARS-05
**Success Criteria** (what must be TRUE):
  1. Each of the four dial weight tables (Order: 7, Axis: 6, Type: 5, Color: 8) exports typed weight entries with affinity and suppression values on the -8 to +8 scale
  2. exercises.json is built from exercise-library.md (~2,185 exercises) with fuzzy-matchable aliases
  3. dial-keywords.json contains ~2,500 fitness terms with dimension_affinity_score per entry, collision-prone keywords identified
  4. Weight vector computation produces a 61-dimensional array for any valid zip code input
**Plans**: TBD

### Phase 3: Integration
**Goal**: The interaction resolver enforces the constraint hierarchy and the text scorer produces ranked ParseResult candidates from natural language
**Depends on**: Phase 2
**Requirements**: WGHT-03, WGHT-04, PARS-01, PARS-06, PARS-07, PARS-08
**Success Criteria** (what must be TRUE):
  1. Hard suppression fires correctly: any weight at or below -6 from a higher-priority dial cannot be overridden by a lower-priority dial
  2. The constraint hierarchy (Order > Color > Axis > Type) lives exclusively in the resolver — dial tables contain no hierarchy logic
  3. ParseResult includes defaulted_dimensions field from day one, populated whenever a dial scores zero and defaults
  4. Natural language input ("heavy barbell back work") returns ranked zip code candidates with confidence scores
  5. Fuzzy matching tolerates typos up to edit distance 2 and expands multi-word aliases
**Plans**: TBD

### Phase 4: Design Tokens
**Goal**: design-tokens.json is the single authoritative source for all visual values, built as semantic tokens and compiled to CSS and TypeScript via style-dictionary
**Depends on**: Phase 3
**Requirements**: RNDR-01, RNDR-02, RNDR-03, RNDR-04
**Success Criteria** (what must be TRUE):
  1. design-tokens.json encodes all 8 Color palettes (7 CSS properties each: primary, secondary, background, surface, text, accent, border) as semantic names, not primitive hex values
  2. design-tokens.json encodes all 7 Order typographies (fontWeight, lineHeight, spacingMultiplier) and all 6 Axis gradient directions
  3. style-dictionary build produces design-tokens.css and tokens.ts artifacts consumable by both canvas/ and web/
  4. CSS arbitration spec document exists mapping every CSS property to exactly one dial owner (structural: Order; tonal: Color; directional: Axis) before any deriver code is written
**Plans**: TBD

### Phase 5: Rendering Pipeline
**Goal**: weightsToCSSVars() takes a WeightVector and design tokens and produces 30+ CSS custom properties; block container styles cover all 22 blocks
**Depends on**: Phase 4
**Requirements**: RNDR-05, RNDR-06, RNDR-07, TEST-04
**Success Criteria** (what must be TRUE):
  1. weightsToCSSVars() is a pure function: same WeightVector + same tokens = same CSS output, no side effects
  2. Color saturation derivation spans the full temperament range (⚫ Teaching outputs ~0.05 saturation; 🔴 Intense outputs ~0.90)
  3. Block container styles exist for all 22 blocks grouped by operational function (Orientation, Access, Transformation, Retention)
  4. A known zip code (e.g., 2123 / ⛽🏛🪡🔵) produces the expected CSS custom property values when run through the full pipeline
**Plans**: TBD

### Phase 6: Claude Code Infrastructure
**Goal**: /blank-canvas skill, canvas-renderer subagent, and PostToolUse hook are live and correctly scoped so they operate only on canvas/ paths
**Depends on**: Phase 5
**Requirements**: CLCD-01, CLCD-02, CLCD-03
**Success Criteria** (what must be TRUE):
  1. /blank-canvas skill initializes the canvas workspace and loads current state when invoked
  2. canvas-renderer subagent is defined with explicit scope limited to canvas/components/ — it does not write to cards/, html/, or web/
  3. PostToolUse hook fires only on canvas/ file writes (path gate verified), applies art direction enforcement, and never uses exit code 2
  4. AGENT-BOUNDARIES.md documents which hooks own which paths and the "flush before delegate" rule
**Plans**: TBD

### Phase 7: Scripts and State Persistence
**Goal**: canvas-to-production.sh and batch-propagate.sh exist and run; canvas state persists locally in .local/ and snapshots commit on /canvas-save command
**Depends on**: Phase 6
**Requirements**: CLCD-04, CLCD-05, CLCD-06
**Success Criteria** (what must be TRUE):
  1. canvas-to-production.sh accepts a canvas artifact path and copies it to the correct destination in cards/, html/, or web/ without overwriting non-canvas files
  2. batch-propagate.sh accepts a design element and a count N, templates it across N zip codes, and reports which files were written
  3. canvas/.local/ holds working state that is git-ignored; /canvas-save commits a named snapshot to git
**Plans**: TBD

### Phase 8: Tests and Card Templates
**Goal**: The full pipeline is validated by a Vitest suite; HTML/TSX card templates render a .md workout card using CSS custom properties from the weight pipeline
**Depends on**: Phase 7
**Requirements**: TEST-02, TEST-03, TEST-05, CARD-01, CARD-02, CARD-03
**Success Criteria** (what must be TRUE):
  1. Vitest suite passes: weight vector spot-checks (10 representative zips), keyword scoring tests (known terms route to correct dimensions), CSS derivation tests (weight vector to expected CSS vars)
  2. Integration test runs the full pipeline from text input to ParseResult to WeightVector to CSS custom properties without error
  3. Card HTML/TSX template renders a .md workout card as an interactive web component consuming CSS custom properties (no hardcoded styles)
  4. Intaglio art direction is visible in the rendered card output (hatching, engraving aesthetic applied via publication standard CSS)
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in strict dependency order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation | 0/TBD | Not started | - |
| 2. Core Data | 0/TBD | Not started | - |
| 3. Integration | 0/TBD | Not started | - |
| 4. Design Tokens | 0/TBD | Not started | - |
| 5. Rendering Pipeline | 0/TBD | Not started | - |
| 6. Claude Code Infrastructure | 0/TBD | Not started | - |
| 7. Scripts and State Persistence | 0/TBD | Not started | - |
| 8. Tests and Card Templates | 0/TBD | Not started | - |
