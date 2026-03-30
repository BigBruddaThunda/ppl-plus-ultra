---
planted: 2026-03-26
status: SEED
phase-relevance: Phase 4/5 (Design System + Interactive Cards), all future visual phases
blocks: html/assets/icons/, html/assets/fonts/
depends-on:
  - seeds/art-direction-intaglio.md
  - seeds/negentropy-thesis.md
  - middle-math/design-tokens.json
  - canvas/src/types/scl.ts
  - canvas/src/rendering/weights-to-css-vars.ts
  - middle-math/weight-css-spec.md
connects-to:
  - seeds/architectural-reset-direction.md
  - seeds/experience-layer-blueprint.md
  - seeds/mobile-ui-architecture.md
  - seeds/elevator-architecture.md
  - seeds/wiki-address-resolution-layer.md
  - html/design-system/theme.css
  - html/design-system/orders/
  - projects/graph-parti/
extends: seeds/art-direction-intaglio.md (first concrete implementation of the intaglio visual language at the atomic level)
supersedes: nothing (first specification)
---

# SCL Glyph Architecture — The 61 Design Atoms

⚫🟣 — foundational + precise

## One Sentence

Each of the 61 SCL emojis becomes an architecturally-specified design atom — a parameterized visual element with fixed identity, weight-responsive rendering, intaglio line work, and dual-layer behavior where the custom glyph renders in-app and the Unicode emoji survives copy-paste.

---

## Section 1 — What the Glyph Layer Is

The system currently has:
- The **address layer** — zip codes (4-emoji combinations, 1,680 addresses)
- The **topology layer** — D architecture, block sequences, constraint surfaces
- The **rendering layer** — weight vectors → CSS custom properties → visual output
- The **content layer** — exercises, cues, sets, the workout itself

What's missing: the **glyph layer** — the visual DNA of each individual emoji.

Right now, 🐂 looks different on every phone. Apple, Google, Samsung, Microsoft — each renders their own version. The system specifies materials, shadows, line weights, palettes, and D proportions deterministically through the weight vector pipeline. But the actual symbols that compose the language? Those are outsourced to phone manufacturers. That's entropy.

The glyph layer replaces 61 platform-dependent emoji renderings with 61 architecturally-specified design atoms. Each atom has:
- A fixed visual identity rooted in the intaglio art direction
- Parameterized rendering driven by the weight vector
- A dual-layer codec: custom glyph in-app, Unicode emoji outside

This is the same pattern that repeats across the system:
- Emoji zip / numeric zip (display layer / system layer)
- Wiki topology / app furniture (free layer / paid layer)
- Custom glyph / Unicode emoji (owned layer / universal layer)

Both layers always present. The system owns one, the world owns the other.

---

## Section 2 — The 7 Glyph Families

Each SCL category gets a distinct visual treatment rooted in its architectural role. The treatment encodes function, not decoration.

### Orders (7 glyphs) — Column Capitals

🐂 ⛽ 🦋 🏟 🌾 ⚖ 🖼

Each Order glyph is rendered as a classical column capital in its architectural style. The subject (ox, fuel, butterfly, stadium, wheat, scale, frame) appears within or atop the capital form.

- 🐂 Foundation = Tuscan capital. Simple, unadorned. Sparse parallel hatching. Line weight 0.8x.
- ⛽ Strength = Doric capital. Compact, bold. Dense cross-hatching. Line weight 1.3x.
- 🦋 Hypertrophy = Ionic capital. Scrolled volutes. Balanced hatching. Line weight 1.0x.
- 🏟 Performance = Corinthian capital. Ornate acanthus. Dense detail. Line weight 1.5x.
- 🌾 Full Body = Composite capital. Integrated elements. Flowing hatching. Line weight 1.1x.
- ⚖ Balance = Vitruvian proportions. Symmetrical, measured. Precise hatching. Line weight 1.0x.
- 🖼 Restoration = Palladian capital. Light, airy. Sparse stippling. Line weight 0.6x.

The column capital IS the category marker. You know it's an Order because it sits on a column. Complexity increases with Order index — Foundation is simplest, Performance is most ornate.

### Axes (6 glyphs) — Building Facades

🏛 🔨 🌹 🪐 ⌛ 🐬

Each Axis glyph is rendered as an architectural facade element — a face of the building that expresses the Axis's spatial character.

- 🏛 Basics = Classical temple front. Pediment, columns. Grand, symmetrical.
- 🔨 Functional = Workshop facade. Angled roofline, tool rack, open front.
- 🌹 Aesthetic = Arched window. Ornamental frame, decorative ironwork.
- 🪐 Challenge = Fortified entrance. Heavy lintel, deep threshold.
- ⌛ Time = Clock tower face. Dial, numerals, mechanical precision.
- 🐬 Partner = Double doorway. Two entrances, shared threshold.

The facade IS the category marker. You know it's an Axis because it's a face of the building.

### Types (5 glyphs) — Anatomical Engravings

🛒 🪡 🍗 ➕ ➖

Each Type glyph is rendered as a simplified anatomical region indicator in the intaglio style — like an engraving from a medical atlas.

- 🛒 Push = Anterior upper body. Chest, shoulders, triceps emphasized.
- 🪡 Pull = Posterior chain. Back, rear delts, biceps emphasized.
- 🍗 Legs = Lower body. Quads, hamstrings, glutes, calves emphasized.
- ➕ Plus = Full body with power vectors. Olympic lift silhouette.
- ➖ Ultra = Circulatory overlay. Heart, lungs, movement arrows.

The anatomical framing IS the category marker. You know it's a Type because it maps the body.

### Colors (8 glyphs) — Ink Wells

⚫ 🟢 🔵 🟣 🔴 🟠 🟡 ⚪

Each Color glyph is rendered as an ink well or vial in the intaglio style, filled with the Color's ink via graduated hatching. These are the only glyphs that use color — all others are monochrome line work. The vial form connects to the existing vial ornamentation from the intaglio seed.

- ⚫ Teaching = Charcoal ink well. Deep, dark, even fill.
- 🟢 Bodyweight = Forest green ink. Like the reverse of a US dollar.
- 🔵 Structured = Deep blue ink. Like an architectural blueprint.
- 🟣 Technical = Purple ink with guilloche border. GOLD-gated marker.
- 🔴 Intense = Deep red ink with guilloche border. GOLD-gated marker.
- 🟠 Circuit = Warm amber ink. Lithographic poster quality.
- 🟡 Fun = Golden ochre ink. Vintage map quality.
- ⚪ Mindful = Silver-gray ink. Pencil preliminary quality.

The ink well IS the category marker. You know it's a Color because it holds ink.

### Blocks (22 glyphs) — Architectural Room Plans

♨️ 🎯 🔢 🧈 🫀 ▶️ 🎼 ♟️ 🪜 🌎 🎱 🌋 🪞 🗿 🛠 🧩 🪫 🏖 🏗 🧬 🚂 🔠

Each Block glyph is rendered as a small architectural floor plan — a room viewed from above. The subject appears as furniture or features within the room. This connects to "blocks are rooms inside a workout."

- Orientation blocks (♨️ 🎯) — Entry rooms. Open plan, threshold markers.
- Access blocks (🔢 🫀 ▶️ 🎼 ♟️ 🪜 🌎) — Corridor rooms. Directional flow.
- Transformation blocks (🧈 🎱 🌋 🪞 🗿 🛠 🧩 🏖 🏗) — Main chambers. Largest footprint.
- Retention blocks (🪫 🧬 🚂) — Exit rooms. Narrowing path.
- Modifier (🔠) — Overlay room. Dotted walls indicating flexibility.

The plan-view room IS the category marker. You know it's a Block because you're looking down into it.

### Operators (12 glyphs) — Gesture Engravings

📍 🧸 👀 🥨 🤌 🚀 🦢 🪵 🐋 ✒️ 🧲 🦉

Each Operator glyph is rendered as a hand or body gesture in intaglio engraving — like an anatomical study of a specific movement. The Latin verb is inscribed beneath in copperplate lettering.

- Preparatory operators (📍 🧸 👀 🪵 🐋 🧲) — Lighter line weight. The inhale.
- Expressive operators (🤌 🥨 🦢 🚀 ✒️ 🦉) — Heavier line weight. The exhale.

The gesture IS the category marker. You know it's an Operator because a hand is performing an action.

### System (1 glyph) — The Seal

🧮

The SAVE glyph is rendered as an institutional seal — circular, abacus centered, guilloche border. Like a notary stamp or printer's mark. The only glyph that uses the full ornamental vocabulary because it represents closure and authority.

---

## Section 3 — Glyph Specification Format

Each glyph is defined as a structured entry:

```json
{
  "id": 1,
  "w_position": "W.FOUNDATION",
  "emoji": "🐂",
  "unicode": "U+1F402",
  "family": "order",
  "name": "Foundation",
  "slug": "foundation",
  "classical": "Tuscan",

  "geometry": {
    "viewbox": "0 0 256 256",
    "svg_path": "assets/glyphs/svg/orders/foundation.svg",
    "detail_tiers": ["full", "medium", "small", "pixel"]
  },

  "intaglio": {
    "stroke_style": "parallel",
    "hatching_angle": 0,
    "hatching_density_base": 0.4,
    "guilloche_complexity": 1,
    "line_weight_base": 0.8,
    "line_weight_range": [0.5, 1.2],
    "fill": "none"
  },

  "material": {
    "surface": "rough travertine",
    "warmth": 0.8,
    "texture": "visible fiber"
  },

  "color_default": {
    "source": "design-tokens.json",
    "ink": "#1A1A1A"
  },

  "weight_responsive": {
    "line_weight": "--ppl-line-multiplier",
    "shadow": "--ppl-shadow-depth",
    "ink_color": "--ppl-theme-primary",
    "hatching_density": "--ppl-weight-density",
    "saturation": "--ppl-weight-saturation"
  },

  "context_variants": {
    "header": "2D scale, full detail tier, primary ink",
    "inline": "1D scale, medium detail tier, muted ink",
    "minimap": "0.5D scale, small detail tier, silhouette",
    "pixel": "16px, pixel detail tier, single stroke"
  },

  "pencil_metadata": {
    "description": "An ox head viewed from the front, rendered in intaglio line work atop a Tuscan column capital. Simple, unadorned. Sparse parallel hatching for volume. No ornamental borders.",
    "family_coherence": "All 7 Order glyphs share the column capital base form. Complexity increases with Order index."
  }
}
```

The full registry lives at `middle-math/glyph-registry.json` — 61 entries, one per emoji. This mirrors the existing pattern where `middle-math/exercise-registry.json` holds exercise metadata.

---

## Section 4 — Weight-Driven Contextual Rendering

The same glyph renders differently depending on where it appears. The weight vector drives rendering through CSS custom properties that `weightsToCSSVars()` already generates.

**The bridge:**
```
resolveZip() -> Float32Array[62] -> weightsToCSSVars() -> CSS custom properties -> SVG glyph consumes properties
```

**What changes per context:**

| CSS Custom Property | Glyph Effect |
|---|---|
| `--ppl-line-multiplier` | Master stroke-width on all paths |
| `--ppl-shadow-depth` | Emboss depth on the glyph |
| `--ppl-theme-primary` | Primary ink color for strokes |
| `--ppl-theme-accent` | Secondary detail color |
| `--ppl-weight-density` | Hatching line count / spacing |
| `--ppl-weight-saturation` | Chroma intensity of color fills |
| `--ppl-material-hue` | Background tone behind the glyph |

**Example:** 🐂 at zip 1138 (🐂🏛🍗⚪):
- Weight[W.FOUNDATION] = 8 → maximum expression, full line weight, complete hatching
- Color is ⚪ Mindful → silver-gray ink, light touch
- Renders: Tuscan capital, warm travertine, silver lines, sparse hatching

Same 🐂 at zip 2111 (⛽🏛🛒⚫):
- Weight[W.FOUNDATION] = -4 → suppressed, thinner lines, simplified
- Color is ⚫ Teaching → charcoal ink
- Renders: same Tuscan capital but visually receded — it's not the active Order

The glyph's identity stays fixed. Its expression shifts with the weight context. Same as how a person looks different in different lighting but is always recognizably themselves.

---

## Section 5 — Technical Format: Dual-Layer System

### Layer 1: SVG Source Masters (the CAD blocks)

Each glyph is a parameterized SVG with:
- Stroke paths in intaglio line work (no fills — volume from hatching)
- CSS custom property hooks (`var(--ppl-line-multiplier)` etc.)
- 4 detail tiers via `<g>` groups: full / medium / small / pixel
- Normalized viewbox: 256x256 master, with 32x32 and 16x16 simplified variants

Location: `assets/glyphs/svg/[category]/[slug].svg`

### Layer 2: Icon Font (the copy-paste surface)

A custom WOFF2 font where each glyph maps to a Unicode Private Use Area (PUA) codepoint:
- 61 PUA codepoints (U+F0001 through U+F003D)
- CSS `@font-face` with `unicode-range` targeting PUA
- Fallback chain: Ppl± icon font → system emoji → text name

Location: `assets/glyphs/font/ppl-glyphs.woff2`

### Copy-Paste Behavior

```html
<span class="ppl-glyph" data-glyph="foundation" data-w="1">🐂</span>
```

- **In-app:** Font substitution renders the custom glyph
- **Copy:** Clipboard gets Unicode emoji 🐂
- **Paste into Ppl±:** Unicode maps back to custom glyph
- **Paste outside Ppl±:** Standard platform emoji renders

The text content IS the emoji. The visual IS the glyph. Same content, owned rendering.

---

## Section 6 — Pencil Integration

What Pencil needs from this system:

1. **Component library** — 61 glyphs as referenceable Pencil components with named props mapping to CSS custom properties and variants for 4 resolution tiers
2. **Design tokens** — Already exist in `design-tokens.json`. Extended with a `glyphs` section containing per-glyph intaglio parameters.
3. **Example compositions** — Glyphs in context: zip code labels, block sequences, dial interfaces, deck headers
4. **AI agent reference** — Each glyph entry includes a natural language description + intaglio constraints + contextual rules so any AI agent can compose consistently without guessing

Location: `assets/glyphs/pencil/` — packaged component library

**The negentropy application:** Instead of every Pencil session starting from scratch ("make me an icon for Strength"), the agent reads the glyph spec and knows exactly what ⛽ looks like, what proportions it uses, what line weights apply, what material it's made of. The specification eliminates guesswork. That's negentropy at the design-tool level.

---

## Section 7 — Relationship to Graph Parti / .parti Endgame

The glyph architecture is the base layer for the future .parti system:

- **Graph Parti** (`projects/graph-parti/`) = semantic canvas with SCL addressing
- **.parti file** = a drawing format that uses SCL glyphs as its vocabulary
- **The glyphs ARE the CAD blocks** — parameterized, reusable, weight-responsive
- **Current use:** Pencil component library for design work
- **Future use:** .parti file primitives for the Ppl± design tool

The 61 glyphs are to .parti what basic shapes are to AutoCAD — the atomic elements that everything else is composed from. When .parti exists, these glyphs are already specified, already parameterized, already weight-responsive. The foundation is laid before the building is designed.

---

## Section 8 — Build Sequence

1. **This seed** — Specification complete. Glyph registry JSON format defined.
2. **7 proof-of-concept glyphs** — One per category (🐂 🏛 🛒 ⚫ ♨️ 🤌 🧮). Validates all 7 treatments.
3. **Pencil test** — Load proof glyphs into Pencil, test composition and referenceability.
4. **Full 61-glyph SVG set** — Orders (7) → Colors (8) → Types (5) → Axes (6) → Operators (12) → Blocks (22) → System (1)
5. **Icon font compilation** — SVG masters → WOFF2 via build script. PUA codepoint mapping.
6. **Token integration** — Add `glyphs` section to `design-tokens.json`. Create `<PplGlyph>` React component.
7. **Weight integration** — Connect parameterized SVGs to the `weightsToCSSVars()` pipeline.

Start with the smallest provable unit. The 7 proof glyphs validate the entire system before scaling to 61.

---

## Section 9 — Directional Constraint Compliance

From `seeds/architectural-reset-direction.md`, Section 5:

1. **Operates on the zip code address space?** Yes — glyphs ARE the symbols that compose zip codes.
2. **Constraint hierarchy governs it?** Yes — Order glyphs inherit D proportions, Color glyphs inherit palettes, weight vector drives all contextual rendering.
3. **Absorbs entropy or creates it?** Absorbs — replaces 61 platform-dependent renderings with 61 deterministic specifications driven by the same weight system that drives everything else.
4. **Same principle at different timescale?** Yes — the intaglio art direction applied at the atomic level. The art direction seed is the macro; glyphs are the micro.
5. **Exercise library coverage?** N/A — visual layer, not content layer.

**The 100-year question:** Would architecturally-specified glyphs for a design language still make sense if the system runs for 100 years? Yes. Fonts outlive the platforms that render them. The intaglio style has been in continuous use since the 15th century. The glyphs are designed to age as well as the architecture they represent.

---

🧮
