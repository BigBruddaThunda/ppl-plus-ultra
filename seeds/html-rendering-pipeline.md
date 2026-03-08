---
title: HTML Rendering Pipeline
status: SEED
planted: 2026-03-08
category: experience-layer
depends-on: middle-math/weight-css-spec.md, middle-math/design-tokens.json
connects-to: seeds/experience-layer-blueprint.md, seeds/mobile-ui-architecture.md
---

# HTML Rendering Pipeline

How the SCL weight vector becomes a visual room.

---

## 1. Overview

One HTML template. 1,680 rooms. No per-room stylesheets.

The zip code IS the rendering instruction. A 4-emoji address resolves to a 61-dimensional weight vector, which resolves to a set of CSS custom properties, which the single room template consumes. Every visual decision — color, typography, spacing, density, saturation, gradient direction — derives from the weight vector. Nothing is hardcoded per room.

The pipeline:
- **Input:** zip code (4 emoji or 4 digit)
- **Resolution:** weight vector (61 floats on the octave scale, -8.0 to +8.0)
- **Normalization:** `(weight + 8.0) / 16.0` maps each dimension to 0.0–1.0
- **Derivation:** dominant dimensions select design tokens, normalized values interpolate properties
- **Output:** CSS custom properties on the room root element
- **Consumption:** the HTML template reads properties and renders

No component ever asks "which zip code am I?" It reads `--ppl-theme-*` and `--ppl-weight-*` variables and renders accordingly.

---

## 2. Color Palette per Color

The dominant Color dimension (indices 18–25 in the weight vector) selects one of 8 palettes. Each palette maps to 7 CSS custom properties on the room root.

### ⚫ Teaching (Order)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#1A1A1A` |
| Secondary | `--ppl-theme-secondary` | `#2D2D2D` |
| Background | `--ppl-theme-background` | `#F8F8F8` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#1A1A1A` |
| Accent | `--ppl-theme-accent` | `#3D3D3D` |
| Border | `--ppl-theme-border` | `#E0E0E0` |

### 🟢 Bodyweight (Growth)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#3A7D44` |
| Secondary | `--ppl-theme-secondary` | `#4A9154` |
| Background | `--ppl-theme-background` | `#F0F7F1` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#1A3D1E` |
| Accent | `--ppl-theme-accent` | `#2A5C32` |
| Border | `--ppl-theme-border` | `#C5DEC8` |

### 🔵 Structured (Planning)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#2E6BA6` |
| Secondary | `--ppl-theme-secondary` | `#3A7EC0` |
| Background | `--ppl-theme-background` | `#EDF4FB` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#143050` |
| Accent | `--ppl-theme-accent` | `#1E4F7D` |
| Border | `--ppl-theme-border` | `#B8D4EC` |

### 🟣 Technical (Magnificence)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#7B4FA2` |
| Secondary | `--ppl-theme-secondary` | `#8E62B2` |
| Background | `--ppl-theme-background` | `#F3EEF8` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#3A1F50` |
| Accent | `--ppl-theme-accent` | `#5E3C7D` |
| Border | `--ppl-theme-border` | `#D5C2E8` |

### 🔴 Intense (Passion)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#C0392B` |
| Secondary | `--ppl-theme-secondary` | `#D44433` |
| Background | `--ppl-theme-background` | `#FDF0EE` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#5C1A13` |
| Accent | `--ppl-theme-accent` | `#962D22` |
| Border | `--ppl-theme-border` | `#F0BCBA` |

### 🟠 Circuit (Connection)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#E07A3A` |
| Secondary | `--ppl-theme-secondary` | `#E88B50` |
| Background | `--ppl-theme-background` | `#FDF5EE` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#6B3418` |
| Accent | `--ppl-theme-accent` | `#C4612A` |
| Border | `--ppl-theme-border` | `#F0CEAD` |

### 🟡 Fun (Play)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#F2C744` |
| Secondary | `--ppl-theme-secondary` | `#F5D060` |
| Background | `--ppl-theme-background` | `#FDFBEE` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#5C4A12` |
| Accent | `--ppl-theme-accent` | `#D4A830` |
| Border | `--ppl-theme-border` | `#F0E3B0` |

### ⚪ Mindful (Eudaimonia)

| Property | Variable | Value |
|----------|----------|-------|
| Primary | `--ppl-theme-primary` | `#F5F0E8` |
| Secondary | `--ppl-theme-secondary` | `#E8E2D8` |
| Background | `--ppl-theme-background` | `#FBFAF8` |
| Surface | `--ppl-theme-surface` | `#FFFFFF` |
| Text | `--ppl-theme-text` | `#3D3530` |
| Accent | `--ppl-theme-accent` | `#D4C9B8` |
| Border | `--ppl-theme-border` | `#D4C9B8` |

**Selection logic:** The Color dimension with the highest weight in indices 18–25 selects the active palette. The full 7-property palette is applied to the room root element. Neutral fallback: 🔵 Structured.

---

## 3. Typography Scale per Order

The dominant Order dimension (indices 0–6) selects a typographic configuration. Each Order has a distinct visual density and weight that shapes how the room reads.

| Order | fontSizeBase | fontSizeDisplay | fontWeight | fontWeightDisplay | letterSpacing | lineHeight | Density |
|-------|-------------|-----------------|------------|-------------------|---------------|------------|---------|
| 🐂 Foundation | `1rem` | `1.75rem` | 400 | 600 | `0.02em` | 1.75 | spacious |
| ⛽ Strength | `1rem` | `2rem` | 700 | 900 | `0.005em` | 1.45 | compact |
| 🦋 Hypertrophy | `1rem` | `1.875rem` | 500 | 700 | `0.015em` | 1.6 | comfortable |
| 🏟 Performance | `1.125rem` | `2.5rem` | 800 | 900 | `0em` | 1.35 | sparse |
| 🌾 Full Body | `1rem` | `1.75rem` | 500 | 650 | `0.01em` | 1.65 | flowing |
| ⚖ Balance | `0.9375rem` | `1.625rem` | 500 | 600 | `0.02em` | 1.6 | precise |
| 🖼 Restoration | `1.0625rem` | `1.75rem` | 300 | 400 | `0.03em` | 1.85 | airy |

**Character notes:**

- **🐂 Foundation** — Spacious, patient. Large breathing room between elements. The learning posture. Wide letter-spacing, tall line-height, light font-weight. Nothing competes for attention.
- **⛽ Strength** — Compact, heavy. Dense information delivered without decoration. Tight line-height, bold weight, near-zero letter-spacing. The room feels loaded.
- **🦋 Hypertrophy** — Comfortable, moderate. Volume-forward layout with enough room to breathe. Medium weight, standard spacing. The pump is visible in how the content fills space.
- **🏟 Performance** — Sparse, maximum signal. Oversized display type, everything non-essential stripped. The testing environment. Numbers dominate. Zero letter-spacing.
- **🌾 Full Body** — Flowing. Movements visualized as a sequence, not a list. Moderate weight with generous line-height. The eye moves continuously.
- **⚖ Balance** — Precise. Smaller base font, deliberate spacing. A microscope on detail. Tight, corrective layout.
- **🖼 Restoration** — Airy, light. Maximum whitespace. The thinnest font-weight (300), widest letter-spacing (0.03em), tallest line-height (1.85). Breath-paced rhythm. You leave the room lighter than you entered.

**CSS mapping:**

```css
.ppl-room {
  font-size: var(--ppl-weight-font-size-base);
  font-weight: var(--ppl-weight-font-weight);
  letter-spacing: var(--ppl-weight-letter-spacing);
  line-height: var(--ppl-weight-lineheight);
}

.ppl-room .block-header {
  font-size: var(--ppl-weight-font-size-display);
  font-weight: var(--ppl-weight-font-weight-display);
}
```

---

## 4. Spacing Rhythm per Order

Order density values drive a spacing multiplier that scales all spacing tokens globally. The `--ppl-weight-spacing-multiplier` property acts as a coefficient on the base spacing scale (`2px` / `4px` / `8px` / `16px` / `24px` / `40px` / `64px` / `96px` / `128px`).

| Order | Density | Multiplier | Effect |
|-------|---------|------------|--------|
| 🐂 Foundation | spacious | 1.5 | Wide margins, generous padding. Room to learn. |
| ⛽ Strength | compact | 0.75 | Tight spacing. Dense, loaded feel. No wasted space. |
| 🦋 Hypertrophy | comfortable | 1.0 | Standard spacing. Balanced density. |
| 🏟 Performance | sparse | 1.25 | Generous spacing but not for comfort — for signal isolation. Less content, more emphasis per element. |
| 🌾 Full Body | flowing | 1.1 | Slightly expanded. Enough room for movement sequences to read as continuous flow. |
| ⚖ Balance | precise | 0.9 | Slightly tighter than standard. Corrective precision. |
| 🖼 Restoration | airy | 1.5 | Maximum breathing room. Matches Foundation's spaciousness but for a different reason — recovery, not learning. |

**Application:**

```css
.ppl-room {
  --computed-spacing-sm: calc(8px * var(--ppl-weight-spacing-multiplier));
  --computed-spacing-md: calc(16px * var(--ppl-weight-spacing-multiplier));
  --computed-spacing-lg: calc(24px * var(--ppl-weight-spacing-multiplier));
  --computed-spacing-xl: calc(40px * var(--ppl-weight-spacing-multiplier));
}

.block + .block {
  margin-top: var(--computed-spacing-xl);
}

.exercise-entry {
  padding: var(--computed-spacing-sm) var(--computed-spacing-md);
}
```

---

## 5. Block Container Styling

The 22 blocks are visual containers inside a room. Each block has a consistent structural treatment but subtle visual differentiation based on its operational function.

### Structural constants

- **Block separator:** 3px solid border using `--ppl-theme-border`, the CSS equivalent of the `═══` separator in markdown cards.
- **Block header:** emoji + name, rendered in display font size and weight. Flush left.
- **Block padding:** base spacing `md` (16px) scaled by `--ppl-weight-spacing-multiplier`.
- **Block border-radius:** `borderRadius.md` (8px).

### Visual treatment by function

Blocks fall into 4 operational categories. Each category gets a subtle background tint derived from the active Color palette.

**Orientation blocks** — Arriving, focusing, pointing intent.
Background: `--ppl-theme-background` with a warm shift (+2% toward `--ppl-theme-accent`). Subdued. The room is still waking up.

| Block | Emoji | Treatment |
|-------|-------|-----------|
| Warm-Up | ♨️ | Warm tint. Always first (unless 🎯 opens). |
| Intention | 🎯 | Centered text. Italic. Quoted. |
| Fundamentals | 🔢 | Numbered list emphasis. Teaching register. |

**Access/Preparation blocks** — Mobility, activation, priming.
Background: linear gradient from `--ppl-theme-background` to `--ppl-theme-surface` at 5% opacity of `--ppl-theme-secondary`. An activation ramp.

| Block | Emoji | Treatment |
|-------|-------|-----------|
| Circulation | 🫀 | Subtle pulse animation on header emoji (optional, respects `prefers-reduced-motion`). |
| Primer | ▶️ | Forward-arrow motif. Transition from warm-up to work. |
| Gambit | ♟️ | Darker surface tint. Deliberate sacrifice signaling. |
| Progression | 🪜 | Step indicators. Loading ramp visualization. |

**Transformation blocks** — Where capacity is built or tested.
Background: `--ppl-theme-surface` with full `--ppl-theme-primary` at 4% opacity. This is the main event. The room's Color is most visible here.

| Block | Emoji | Treatment |
|-------|-------|-----------|
| Bread & Butter | 🧈 | Largest block. Full theme color. Most visual weight. |
| Composition | 🎼 | Flow layout — exercises displayed as connected sequence. |
| Exposure | 🌎 | Expanded width. Exploration space. |
| ARAM | 🎱 | Station boxes. Loop visualization with rotation arrows. |
| Gutter | 🌋 | High-saturation background. Red-shifted tint regardless of Color. Warning register. |
| Vanity | 🪞 | Mirror motif. Slightly reflective surface treatment (subtle gradient). |
| Sculpt | 🗿 | Strong border. Chiseled edges (sharper border-radius, 4px). |
| Craft | 🛠 | Tool motif. Monospace font for precision cues. |
| Supplemental | 🧩 | Slightly recessed. Secondary to 🧈. Lighter background. |
| Sandbox | 🏖 | Dashed border. Exploratory zone indicator. |
| Reformance | 🏗 | Construction motif. Yellow-shifted accent regardless of Color. |

**Retention/Transfer blocks** — Locking in, cooling down, bridging forward.
Background: `--ppl-theme-background` desaturated by 30%. Cooling. The room is wrapping up.

| Block | Emoji | Treatment |
|-------|-------|-----------|
| Release | 🪫 | Fading opacity gradient toward block bottom. |
| Imprint | 🧬 | Subtle pattern texture. Neural memory visual cue. |
| Junction | 🚂 | Navigation element. Contains clickable zip code links to next-session rooms. |
| SAVE | 🧮 | Terminal block. Full-width border top. Closing principle in display weight. |

---

## 6. Gradient Direction per Axis

Each Axis has a characteristic gradient angle applied as a subtle directional element on the room's background. The gradient uses `--ppl-theme-background` to transparent `--ppl-theme-primary` at 3% opacity. The angle is the Axis's spatial signature.

| Axis | Angle | Direction | Rationale |
|------|-------|-----------|-----------|
| 🏛 Basics (Firmitas) | `0deg` | Bottom to top | Vertical. Classical. Stable. Columnar. |
| 🔨 Functional (Utilitas) | `45deg` | Bottom-left to top-right | Diagonal. Dynamic. Athletic transfer. |
| 🌹 Aesthetic (Venustas) | `90deg` | Left to right | Horizontal. Flowing. Sensory sweep. |
| 🪐 Challenge (Gravitas) | `135deg` | Top-left to bottom-right | Dramatic descending diagonal. Gravity. Weight. |
| ⌛ Time (Temporitas) | `180deg` | Top to bottom | Downward flow. Sand falling. Temporal direction. |
| 🐬 Partner (Sociatas) | `270deg` | Bottom to top (rightward lean) | Upward. Inclusive. Lifting together. |

**CSS variable:**

```css
.ppl-room {
  --ppl-axis-gradient-angle: 0deg; /* default, overridden per Axis */
  background: linear-gradient(
    var(--ppl-axis-gradient-angle),
    var(--ppl-theme-background) 0%,
    color-mix(in srgb, var(--ppl-theme-primary) 3%, transparent) 100%
  );
}
```

The gradient is environmental, not decorative. It should be barely perceptible — a spatial orientation cue, not a visual feature.

---

## 7. Opacity and Saturation per Color Temperament

Each Color has a characteristic saturation level that shapes the room's visual intensity. Saturation controls how much of the Color palette's chromatic range is expressed. Low saturation rooms are near-monochrome. High saturation rooms are vivid.

| Color | Saturation | Character | Visual Effect |
|-------|-----------|-----------|---------------|
| ⚫ Teaching | 0.05 | Near-monochrome | High contrast black/white. Content-first. Color is almost absent. The room is a blank page. |
| 🟢 Bodyweight | 0.50 | Natural, organic | Muted greens. Park-bench feel. Nothing artificial. |
| 🔵 Structured | 0.60 | Clean, methodical | Clear blue. Organized but not cold. The system default. |
| 🟣 Technical | 0.70 | Deep, rich | Saturated purple. Precision demands visual clarity. |
| 🔴 Intense | 0.90 | Vivid, high-energy | Maximum chromatic expression. The room pushes back. |
| 🟠 Circuit | 0.75 | Warm, connected | Strong orange. Station-to-station warmth. |
| 🟡 Fun | 0.80 | Bright, playful | Saturated yellow. The room invites exploration. |
| ⚪ Mindful | 0.15 | Near-transparent | Barely there. Warm neutrals. The room recedes. |

**CSS application:**

```css
.ppl-room {
  --ppl-weight-saturation: 0.60; /* set by weight vector derivation */
  filter: saturate(var(--ppl-weight-saturation));
}
```

Note: the `filter: saturate()` approach is a simplification. In production, saturation is baked into the palette selection itself — the hex values in `design-tokens.json` already encode each Color's saturation character. The CSS variable serves as a secondary modulation layer for blended states and transitions between rooms.

**Saturation interacts with Order.** The saturation value above is the Color's baseline. Order context modulates it:
- 🖼 Restoration reduces saturation by 20% (the recovery lane desaturates everything)
- 🏟 Performance increases contrast but not saturation (signal clarity, not chromatic intensity)
- ⛽ Strength preserves full saturation (heavy rooms stay vivid)

---

## 8. Pipeline Flow

The complete rendering pipeline from zip code to visual room:

```
Zip Code (4 emoji or 4 digit)
  │
  │  Example: ⛽🏛🪡🔵  or  2123
  │
  ↓ lookup (zip-metadata table, CHAR(4) numeric key)
  │
Weight Vector (61 dimensions, octave scale -8.0 to +8.0)
  │
  │  [0]:  -4.0  (🐂 suppressed)
  │  [1]:  +8.0  (⛽ dominant Order)
  │  [2]:  -2.0  (🦋 suppressed)
  │  ...
  │  [7]:  +8.0  (🏛 dominant Axis)
  │  ...
  │  [14]: +8.0  (🪡 dominant Type)
  │  ...
  │  [20]: +8.0  (🔵 dominant Color)
  │  ...
  │
  ↓ normalize: (weight + 8.0) / 16.0
  │
Normalized Vector (61 dimensions, 0.0 to 1.0)
  │
  │  [1]:  1.000  (⛽ max)
  │  [7]:  1.000  (🏛 max)
  │  [14]: 1.000  (🪡 max)
  │  [20]: 1.000  (🔵 max)
  │
  ↓ dominant dimension per category (argmax within index range)
  │
  │  Order:  index 1  → ⛽ Strength
  │  Axis:   index 7  → 🏛 Basics
  │  Type:   index 14 → 🪡 Pull
  │  Color:  index 20 → 🔵 Structured
  │
  ↓ map to design tokens (design-tokens.json)
  │
  │  Order tokens:  orders.strength → fontWeight: 700, lineHeight: 1.45, density: compact
  │  Color palette: colors.structured → primary: #2E6BA6, background: #EDF4FB, ...
  │
  ↓ generate CSS custom properties
  │
  │  --ppl-weight-font-weight: 700
  │  --ppl-weight-lineheight: 1.45
  │  --ppl-weight-spacing-multiplier: 0.75
  │  --ppl-weight-letter-spacing: 0.005em
  │  --ppl-theme-primary: #2E6BA6
  │  --ppl-theme-background: #EDF4FB
  │  --ppl-theme-text: #143050
  │  --ppl-axis-gradient-angle: 0deg
  │  --ppl-weight-saturation: 0.60
  │  ... (full property set)
  │
  ↓ apply to room root element (.ppl-room or :root)
  │
Single HTML Template
  │
  │  <div class="ppl-room" style="[generated properties]">
  │    <header>...</header>
  │    <section class="block orientation">...</section>
  │    <section class="block transformation">...</section>
  │    <section class="block retention">...</section>
  │  </div>
  │
  ↓ render
  │
Visual Room Experience
```

**Key principle:** The template never branches on zip code identity. It consumes CSS custom properties and renders. A 🖼⚪ room and a ⛽🔴 room use the same HTML. The weight vector makes them look and feel completely different.

---

## 9. CSS Custom Property Reference

Complete list of all properties, organized by derivation source.

### Group 1: Order-derived (indices 0–6)

| Property | Type | Range | Derivation |
|----------|------|-------|------------|
| `--ppl-weight-density` | float | 0.4–1.0 | Inverse of Order spaciousness |
| `--ppl-weight-lineheight` | float | 1.35–1.85 | Direct from `orders[name].lineHeight` |
| `--ppl-weight-font-weight` | integer | 300–900 | Direct from `orders[name].fontWeight` |
| `--ppl-weight-font-weight-display` | integer | 400–900 | Direct from `orders[name].fontWeightDisplay` |
| `--ppl-weight-font-size-base` | rem | 0.9375–1.125 | Direct from `orders[name].fontSizeBase` |
| `--ppl-weight-font-size-display` | rem | 1.625–2.5 | Direct from `orders[name].fontSizeDisplay` |
| `--ppl-weight-letter-spacing` | em | 0–0.03 | Direct from `orders[name].letterSpacing` |
| `--ppl-weight-spacing-multiplier` | float | 0.75–1.5 | Mapped from Order density character |

### Group 2: Axis-derived (indices 7–12)

| Property | Type | Range | Derivation |
|----------|------|-------|------------|
| `--ppl-weight-typography-bias` | float | 0.0–1.0 | Normalized dominant Axis weight |
| `--ppl-weight-visual-rhythm` | float | 0.0–1.0 | Normalized dominant Axis weight |
| `--ppl-axis-gradient-angle` | degree | 0–270 | Axis identity lookup (see Section 6) |

### Group 3: Type-derived (indices 13–17)

| Property | Type | Range | Derivation |
|----------|------|-------|------------|
| `--ppl-weight-emphasis-push` | float | 0.0–1.0 | Normalized weight at index 13 |
| `--ppl-weight-emphasis-pull` | float | 0.0–1.0 | Normalized weight at index 14 |
| `--ppl-weight-emphasis-legs` | float | 0.0–1.0 | Normalized weight at index 15 |
| `--ppl-weight-emphasis-plus` | float | 0.0–1.0 | Normalized weight at index 16 |
| `--ppl-weight-emphasis-ultra` | float | 0.0–1.0 | Normalized weight at index 17 |

### Group 4: Color-derived (indices 18–25)

| Property | Type | Range | Derivation |
|----------|------|-------|------------|
| `--ppl-theme-primary` | hex | — | `colors[active].primary` from design-tokens.json |
| `--ppl-theme-secondary` | hex | — | `colors[active].secondary` |
| `--ppl-theme-background` | hex | — | `colors[active].background` |
| `--ppl-theme-surface` | hex | — | `colors[active].surface` |
| `--ppl-theme-text` | hex | — | `colors[active].text` (on light bg) |
| `--ppl-theme-accent` | hex | — | `colors[active].accent` |
| `--ppl-theme-border` | hex | — | `colors[active].border` |
| `--ppl-weight-saturation` | float | 0.05–0.90 | Color identity saturation value |
| `--ppl-weight-contrast` | float | 0.0–1.0 | Normalized dominant Color weight |

### Group 5: Derived dimensions (indices 26–60)

| Property | Type | Range | Derivation |
|----------|------|-------|------------|
| `--ppl-weight-rest-emphasis` | float | 0.0–1.0 | Mean of temporal cluster [26–35], normalized |
| `--ppl-weight-rep-display` | float | 0.0–1.0 | Mean of exercise/operator cluster [36–50], normalized |
| `--ppl-weight-block-spacing` | float | 0.0–1.0 | Mean of full derived range [26–60], normalized |
| `--ppl-weight-cue-density` | float | 0.0–1.0 | Mean of interaction cluster [51–60], normalized |

**Total: 30 CSS custom properties** derived from the 61-dimensional weight vector and design token lookup.

---

## 10. Constraints

1. **No hardcoded hex values in components.** Every color reference passes through `--ppl-theme-*` variables. A component that contains a hex literal is a bug.

2. **Weight vector is the single source.** No component reads the zip code directly for styling decisions. The weight vector resolves, the CSS properties generate, the template consumes. That is the only path.

3. **WCAG AA contrast minimum.** The rendering layer clamps `--ppl-weight-contrast` to ensure no text/background combination falls below 4.5:1 contrast ratio. The `textOnLight` field in `design-tokens.json` provides pre-validated text colors for each palette.

4. **Smooth 250ms transitions between rooms.** When navigating between zip codes, all `--ppl-weight-*` and `--ppl-theme-*` properties transition using `animation.default` (250ms) with `easing.standard` (`cubic-bezier(0.4, 0, 0.2, 1)`). The room morphs — it does not jump-cut.

5. **Dark mode is derived, not defined.** The 8 palettes in `design-tokens.json` are light-mode specifications. Dark mode variants will be generated by hue rotation and lightness inversion at build time. Dark mode is Phase 4 scope. This pipeline supports it by using CSS custom properties exclusively — swapping the property values swaps the mode.

6. **Screenshot mode strips chrome.** A `.ppl-room--export` class removes navigation, interactive elements, and UI chrome, producing a clean static card suitable for image export. The weight vector still drives all visual properties.

7. **`prefers-reduced-motion` respected.** All animations (block header pulses, room transitions, gradient shifts) collapse to instant when the user has requested reduced motion. The 250ms transition becomes 0ms.

8. **Font stack consistency.** All rooms use the same font family declarations from `design-tokens.json`: body (`'Inter', 'Helvetica Neue', sans-serif`), display (same), mono (`'JetBrains Mono', 'Fira Code', monospace`). Order changes weight and spacing, never the typeface.

---

🧮
