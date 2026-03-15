# Phase 8: Tests and Card Templates - Context

**Gathered:** 2026-03-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Full Vitest suite validation (weight vector spot-checks across 10 representative zips, keyword scoring tests, full pipeline integration test). HTML/TSX card templates that render a .md workout card as an interactive web component consuming CSS custom properties from the weight pipeline. Intaglio art direction visible in the rendered output. This is the capstone phase — validates the entire pipeline end-to-end and produces the first visual card output.

</domain>

<decisions>
## Implementation Decisions

### Card Template Structure
- **Zoned layout** — Header zone (title with flanking emoji, subtitle, CODE line, intention), Block zone (scrollable uniform blocks with heavy border separators), Footer zone (junction + save). Each zone is a distinct visual region. The card feels like a physical card with sections, not a document.
- **Uniform blocks** — All 22 block types use the same container treatment. The emoji header and content inside distinguish them. No visual variation by operational role (Orientation/Access/Transformation/Retention). Content speaks, container is clean.
- **Bold emoji anchors** — Type emoji flanking the title are large, colorized, and serve as the card's visual identity. Like a coat of arms on a certificate. The first thing you see.

### Intaglio CSS Techniques
- **Full intaglio treatment** — Line-work borders (fine 1-2px, possibly double/engraved-style), hatching patterns via repeating-linear-gradient for block backgrounds, guilloche pattern accents, and vignette darkening at card edges. The complete banknote engraving aesthetic.
- **Hybrid pattern system** — Saturation from the weight system drives pattern DENSITY/BOLDNESS (⚫ Teaching = barely visible fine lines, 🔴 Intense = bold dense hatching). The Color identity determines the SHAPE of the pattern (crosshatch vs parallel vs diagonal vs radial). Weight-driven intensity + art-directed pattern type.
- **SVG-based guilloche** — Inline SVG or SVG background-image for guilloche patterns. More precise, scales perfectly, can be color-themed via CSS custom properties. The right approach for geometric patterns at phone resolution.

### Test Coverage
- **10 representative zips** — Start with 2123 (⛽🏛🪡🔵, already tested in rendering.test.ts) as the anchor. Researcher picks 9 more spanning all 7 Orders with varied Axis/Type/Color combinations, including edge cases (GOLD gate, hard suppressions).
- **Multiple pipeline inputs** — Integration test uses 3-4 different text inputs: a strength query, a bodyweight query, an ambiguous query, and a nonsense string. Tests the full pipeline: text → ParseResult → WeightVector → CSS custom properties.
- **Keyword scoring tests** — Known terms route to correct dimensions, collision-prone words handled correctly.

### Card Interactivity
- **Logging-ready scaffold** — The template has the HTML structure for full workout logging (input fields for weight/reps, timer slots, checkbox areas for set completion, block progress indicators) but the JavaScript logic is PLACEHOLDER/STUBBED. The visual template is complete; interactive logic ships in a future milestone.
- **Dual format: HTML preview + TSX production** — Self-contained HTML file that opens directly in a browser (CSS custom properties injected inline, no build step). Plus a TSX component in canvas/components/ for the production app. HTML is derived from or mirrors the TSX component.

### Claude's Discretion
- Which 9 additional zip codes to spot-check (must span all 7 Orders)
- Exact CSS techniques for each intaglio effect (line-work border widths, hatching angles, guilloche SVG complexity)
- TSX component architecture (number of sub-components, state management for logging scaffold)
- How to parse .md workout cards into template data (markdown parsing approach)
- Test organization (one big test file vs separate files per concern)

</decisions>

<specifics>
## Specific Ideas

- The card is a "room" in the elevator model — it should feel like entering a space, not reading a document
- Bold emoji anchors serve as the coat of arms — the visual identity of this workout's Type
- The intaglio patterns should feel like they belong on an engraved certificate, not a digital dashboard
- "Minutia" — Jake wants the small details right: hatching grain, border precision, pattern coherence across the 8 Color moods
- Logging-ready means the scaffold is visually complete — a user looking at the card sees where they WOULD log sets, even though the JS isn't wired yet

</specifics>

<code_context>
## Existing Code Insights

### Reusable Assets
- `canvas/src/rendering/weights-to-css-vars.ts` — weightsToCSSVars() produces 30 CSS custom properties from any resolved weight vector. The card template consumes these directly.
- `canvas/src/rendering/block-styles.ts` — BLOCK_CONTAINER_STYLES for all 22 blocks. Available for block-level CSS class generation.
- `canvas/src/rendering/saturation-map.ts` — COLOR_SATURATION lookup (0.05 to 0.90). Drives pattern density in the hybrid system.
- `canvas/src/tokens/design-tokens.css` — All OKLCH palettes, Order typography, Axis gradients as CSS custom properties. The card HTML imports this.
- `canvas/src/tokens/tokens.ts` — TypeScript token exports. COLOR_W_TO_TONAL bridge for token key lookup.
- `canvas/src/weights/resolver.ts` — resolveZip() and resolveVector(). Test setup for spot-checks.
- `canvas/src/parser/scorer.ts` — scoreText() for pipeline integration tests.
- `canvas/components/` — Write target for canvas-renderer subagent (Phase 6). Card templates go here.

### Established Patterns
- Vitest test suite (8 test files, 6,949 tests). New tests follow the same pattern.
- JSON data + TypeScript types (exercises.json, dial-keywords.json, design-tokens.json)
- Pure function pattern (weightsToCSSVars is pure — card rendering should also be pure)

### Integration Points
- Card template consumes design-tokens.css (link or inline)
- Card template consumes weightsToCSSVars() output as inline CSS custom properties
- .md workout card files in cards/ are the source data to render
- canvas-renderer subagent writes to canvas/components/ (Phase 6 governance)

</code_context>

<deferred>
## Deferred Ideas

- Full workout logging JavaScript (set completion, rest timers, weight/rep persistence) — future milestone
- Server-side rendering of cards — future platform architecture
- User history integration (logging writes back to exercise database) — downstream architecture
- Dark mode card variant — token structure supports it but not Phase 8 scope
- Card-to-card navigation (junction zip code links) — future milestone

</deferred>

---

*Phase: 08-tests-and-card-templates*
*Context gathered: 2026-03-15*
