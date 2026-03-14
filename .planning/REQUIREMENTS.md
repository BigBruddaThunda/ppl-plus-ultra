# Requirements: Ppl± Blank Canvas Infrastructure

**Defined:** 2026-03-13
**Core Value:** The SCL parser must deterministically convert any input into weight-vector-tagged, layer-sorted SCL addresses without requiring AI.

## v1 Requirements

Requirements for initial release (Sessions 1-2). Each maps to roadmap phases.

### Foundation

- [ ] **FOUND-01**: TypeScript type definitions for all SCL primitives (Order, Axis, Type, Color, Operator, Block) with emoji and numeric representations
- [x] **FOUND-02**: Emoji ↔ numeric zip conversion (bidirectional, all 1,680 addresses)
- [x] **FOUND-03**: Deck derivation from zip code ((order - 1) * 6 + axis)
- [ ] **FOUND-04**: canvas/ directory scaffold with clean separation from web/, middle-math/, cards/

### Weight Engine

- [x] **WGHT-01**: 61-dimensional weight vector computation for any zip code (-8 to +8 scale)
- [x] **WGHT-02**: Dial weight tables for all 4 categories (Order: 7, Axis: 6, Type: 5, Color: 8)
- [x] **WGHT-03**: Interaction resolver enforcing constraint hierarchy (Order > Color > Axis > Type)
- [x] **WGHT-04**: Hard suppression logic (weight ≤ -6 is absolute, cannot be overridden by lower-priority dial)

### Parser

- [x] **PARS-01**: ParseResult type with zip code, weight vector, confidence score, and defaulted_dimensions field
- [x] **PARS-02**: Keyword dictionary (~2,500 fitness terms) with dimension_affinity_score per entry
- [x] **PARS-03**: Exercise name detection using exercise-library.md as authoritative source (~2,185 exercises)
- [x] **PARS-04**: Equipment mention detection mapping to Color tier ranges
- [x] **PARS-05**: Body part / muscle group detection mapping to Type
- [x] **PARS-06**: Fuzzy matching with typo tolerance (edit distance ≤ 2) via fastest-levenshtein
- [x] **PARS-07**: Multi-word alias expansion via fuse.js
- [x] **PARS-08**: Text-to-zip scoring pipeline that produces ranked candidate addresses from natural language input

### Rendering

- [ ] **RNDR-01**: design-tokens.json encoding all 8 Color palettes (7 CSS props each: primary, secondary, background, surface, text, accent, border)
- [ ] **RNDR-02**: design-tokens.json encoding all 7 Order typographies (fontWeight, lineHeight, spacingMultiplier)
- [ ] **RNDR-03**: design-tokens.json encoding all 6 Axis gradient directions
- [x] **RNDR-04**: CSS arbitration spec defining property ownership (structural: Order, tonal: Color, directional: Axis)
- [ ] **RNDR-05**: weightsToCSSVars() pure function deriving 30+ CSS custom properties from weight vector + design tokens
- [ ] **RNDR-06**: Block container styling for 22 blocks grouped by operational function (Orientation, Access, Transformation, Retention)
- [ ] **RNDR-07**: Color saturation derivation per Color temperament (⚫: 0.05 → 🔴: 0.90)

### Claude Code Infrastructure

- [ ] **CLCD-01**: /blank-canvas skill (SKILL.md with auto-invocation description)
- [ ] **CLCD-02**: canvas-renderer subagent definition (fresh context for v0, resumable for iteration)
- [ ] **CLCD-03**: PostToolUse hook path-gated to canvas/ directory (informational, never blocking)
- [ ] **CLCD-04**: canvas-to-production.sh script porting canvas elements to cards/, html/, or web/
- [ ] **CLCD-05**: batch-propagate.sh script templating a design across N zip codes
- [ ] **CLCD-06**: Canvas state persistence — local working state in canvas/.local/ + git snapshots via /canvas-save command

### Testing

- [x] **TEST-01**: Unit tests for zip converter (all 1,680 round-trip conversions)
- [ ] **TEST-02**: Unit tests for weight vector computation (spot-check 10 representative zips across all Orders)
- [ ] **TEST-03**: Unit tests for keyword dictionary scoring (known terms → correct dimension routing)
- [ ] **TEST-04**: Unit tests for CSS derivation (weight vector → expected CSS custom properties)
- [ ] **TEST-05**: Integration test for full pipeline (text input → ParseResult → weight vector → CSS vars)

### Card Templates

- [ ] **CARD-01**: HTML/TSX template rendering a .md workout card as an interactive web component
- [ ] **CARD-02**: Template consumes CSS custom properties from weight vector (no hardcoded styles)
- [ ] **CARD-03**: Intaglio art direction applied via publication standard CSS (hatching, engraving aesthetic)

## v2 Requirements

Deferred to Session 3+ after infrastructure is solid.

### Visual Canvas

- **CANV-01**: React Flow or tldraw canvas on localhost:3000 with zip code nodes
- **CANV-02**: Paste-to-parse interaction (paste text → auto-sort to layers)
- **CANV-03**: Drag/connect/inspect interactions between nodes
- **CANV-04**: Zoom levels matching elevator model (city → building → floor → room)

### Diagram System

- **DIAG-01**: Weight vector radial (61-spoke radar diagram)
- **DIAG-02**: City navigator (7 buildings × 6 floors interactive map)
- **DIAG-03**: Block sequence timeline (horizontal workout block viewer)
- **DIAG-04**: Similarity constellation (force-directed zip cluster graph)

### Extended Parser

- **XPRS-01**: Full 13K keyword dictionary from voice-parser-architecture seed
- **XPRS-02**: Multi-intent parsing (text referencing multiple zip codes)
- **XPRS-03**: Context-aware parsing (user history affects scoring)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Visual canvas UI (React Flow/tldraw) | Infrastructure must exist before visual layer; deferred to Session 3+ |
| Graph Parti extraction | Ppl± is the pilot instance; extraction happens after patterns are proven |
| Mobile app | Web-first architecture; mobile is a future platform target |
| AI-dependent sorting | Core parser must be deterministic and offline; AI assists creation/refinement, not sorting |
| Operis generation pipeline | Separate work stream, does not block canvas infrastructure |
| User authentication | Not needed for local dev canvas; auth exists in web/ already |
| Real-time collaboration | Single-user dev tool; collaboration via git |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| FOUND-01 | Phase 1 | Pending |
| FOUND-02 | Phase 1 | Complete |
| FOUND-03 | Phase 1 | Complete |
| FOUND-04 | Phase 1 | Pending |
| TEST-01 | Phase 1 | Complete |
| WGHT-01 | Phase 2 | Complete |
| WGHT-02 | Phase 2 | Complete |
| PARS-02 | Phase 2 | Complete |
| PARS-03 | Phase 2 | Complete |
| PARS-04 | Phase 2 | Complete |
| PARS-05 | Phase 2 | Complete |
| WGHT-03 | Phase 3 | Complete |
| WGHT-04 | Phase 3 | Complete |
| PARS-01 | Phase 3 | Complete |
| PARS-06 | Phase 3 | Complete |
| PARS-07 | Phase 3 | Complete |
| PARS-08 | Phase 3 | Complete |
| RNDR-01 | Phase 4 | Pending |
| RNDR-02 | Phase 4 | Pending |
| RNDR-03 | Phase 4 | Pending |
| RNDR-04 | Phase 4 | Complete |
| RNDR-05 | Phase 5 | Pending |
| RNDR-06 | Phase 5 | Pending |
| RNDR-07 | Phase 5 | Pending |
| TEST-04 | Phase 5 | Pending |
| CLCD-01 | Phase 6 | Pending |
| CLCD-02 | Phase 6 | Pending |
| CLCD-03 | Phase 6 | Pending |
| CLCD-04 | Phase 7 | Pending |
| CLCD-05 | Phase 7 | Pending |
| CLCD-06 | Phase 7 | Pending |
| TEST-02 | Phase 8 | Pending |
| TEST-03 | Phase 8 | Pending |
| TEST-05 | Phase 8 | Pending |
| CARD-01 | Phase 8 | Pending |
| CARD-02 | Phase 8 | Pending |
| CARD-03 | Phase 8 | Pending |

**Coverage:**
- v1 requirements: 36 total
- Mapped to phases: 36
- Unmapped: 0 ✓

---
*Requirements defined: 2026-03-13*
*Last updated: 2026-03-13 — traceability updated to match ROADMAP.md phase assignments (TEST-02, TEST-03 moved from Phase 3 to Phase 8)*
