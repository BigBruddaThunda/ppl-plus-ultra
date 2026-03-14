# Phase 4: Design Tokens - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

design-tokens.json as the single authoritative source for all visual values: 8 Color palettes, 7 Order typographies, 6 Axis gradient directions. Compiled to CSS custom properties and TypeScript via style-dictionary. CSS arbitration spec document mapping every CSS property to exactly one dial owner. No rendering code (Phase 5) — this phase produces the data and the spec.

</domain>

<decisions>
## Implementation Decisions

### Color Palette Values
- **Fresh derivation using color theory math** — do NOT port the existing DRAFT values from middle-math/design-tokens.json. The old colors predate the intaglio art direction and need to be reworked from scratch.
- **Color science approach: let the researcher decide.** Evaluate OKLCH vs HSL vs other perceptually uniform color spaces. Each Color gets a mathematically derived palette from a base hue + character parameters. The palette must serve the intaglio/banknote engraving aesthetic while remaining phone-readable.
- **Scalable property system** — do NOT hard-limit to 7 properties per palette. Design an extensible token structure where additional properties (textOnLight, shadow, glow, etc.) can be added without restructuring. Good architecture > fixed count.
- **Tonal names as semantic keys** — use Color Context Vernacular tonal names (order, growth, planning, magnificence, passion, connection, play, eudaimonia) NOT SCL emoji names (teaching, bodyweight, structured...) as the token namespace. CSS reads: `--ppl-color-passion--primary`.

### Typography & Spacing
- **Typographic variation per Order: let the researcher decide.** Research whether distinct fontWeight/lineHeight/spacing per Order or subtler variation best serves the intaglio aesthetic. Each Order should feel distinct but coherent.
- **Typeface direction: let the researcher decide.** Explore typefaces matching banknote engraving aesthetics (slab serif, geometric sans, engraved letterforms) that are web-safe and phone-readable. Present options — do not lock a typeface without research.
- **Axis gradient directions: let the researcher decide.** Research whether "gradient" means literal CSS gradients (background treatments), visual flow parameters (layout/alignment tokens), or both. Define what Axis gradient means in the rendering pipeline.

### CSS Property Ownership (Arbitration)
- **3+1 dial ownership model:**
  - **Order** = structural properties (fontWeight, lineHeight, spacingMultiplier, and tempo/rhythm-related properties)
  - **Color** = tonal properties (palette colors, mood, saturation, shadow depth)
  - **Axis** = directional properties (gradient direction, content flow, visual hierarchy direction)
  - **Type** = icon/illustration tokens (body-region illustrations, muscle group icons, movement pattern diagrams). NOT layout or color — purely visual content that represents the muscle groups.
- **No property has two owners.** The arbitration spec must be exhaustive — every CSS custom property mapped to exactly one dial.
- **Edge-case property assignment: let the researcher decide.** Research animation speed, border radius, opacity, shadow depth, etc. and propose assignments based on the rendering pipeline architecture. Apply a consistent principle, not ad-hoc mapping.
- **This spec MUST exist before any Phase 5 deriver code** — it is a blocking dependency (locked in STATE.md since pre-Phase 1).

### style-dictionary Build Pipeline
- **Source file location and output layout: let the researcher decide.** Research standard style-dictionary project layouts and recommend based on the existing canvas/ workspace and web/ directory structure.
- **Nested CSS custom property naming** — use double-hyphen nesting: `--ppl-color-passion--primary`, `--ppl-color-passion--surface`, `--ppl-order-strength--fontWeight`. BEM-like grouping for readability.
- **Build produces both CSS and TypeScript** — design-tokens.css and tokens.ts, consumable by both canvas/ and web/ as specified in the roadmap.

### Claude's Discretion
- Color science methodology (OKLCH, HSL, or other) — researcher recommends, planner implements
- Exact base hue values per Color — derived from color theory + intaglio aesthetic
- Typographic scale values (fontWeight, lineHeight, spacingMultiplier per Order)
- style-dictionary configuration and transform setup
- Whether to use style-dictionary v3 or v4 API

</decisions>

<specifics>
## Specific Ideas

- The intaglio/banknote engraving aesthetic is the visual north star — colors should feel like they belong on an engraved certificate, not a digital dashboard
- "Good architecture systems" — the token structure must scale to add new properties without restructuring
- Tonal names carry deeper cultural meaning from the Color Context Vernacular — this is intentional semantic layering, not just naming preference
- The code should speak the language of the system: `--ppl-color-passion--primary` tells you what Intense IS, not just what it's called

</specifics>

<code_context>
## Existing Code Insights

### Reusable Assets
- `middle-math/design-tokens.json` — DRAFT palettes with 8 Colors × 8 properties. Structure is useful reference but VALUES are stale and must be rederived. The tonal_name field maps Colors to their vernacular names.
- `middle-math/weight-css-spec.md` — Complete spec for how weight vectors map to CSS custom properties. Defines normalization formula: `(weight + 8.0) / 16.0`. This is the bridge between Phase 3's resolver output and Phase 5's rendering.
- `canvas/src/weights/` — Weight tables and computeRawVector()/resolveVector() from Phases 2-3. The rendering pipeline (Phase 5) will consume resolved weight vectors.
- `scl-deep/color-context-vernacular.md` — Deep Color identity document with tonal names, character descriptions, behavioral anchors.

### Established Patterns
- JSON data + TypeScript types pattern (exercises.json, dial-keywords.json) — design-tokens.json should follow the same pattern
- canvas/ workspace with its own package.json, Vitest test suite

### Integration Points
- design-tokens.json feeds Phase 5's weightsToCSSVars() function
- CSS arbitration spec constrains Phase 5's deriver functions (which dial produces which CSS property)
- tokens.ts output must be importable by canvas/src/ modules
- design-tokens.css output must be consumable by web/ (future HTML experience layer)

</code_context>

<deferred>
## Deferred Ideas

- Per-exercise illustration tokens (muscle group diagrams) — Type owns the token slot but actual illustrations are content, not infrastructure
- Dark mode / theme variants — the token structure should support it but variants are not Phase 4 scope
- Animation/motion tokens — token slots should exist but actual values may come from Phase 5 rendering work

</deferred>

---

*Phase: 04-design-tokens*
*Context gathered: 2026-03-14*
