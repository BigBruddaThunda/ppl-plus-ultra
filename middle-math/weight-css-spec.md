# PPL± WeightCSS Specification
**CX-18 — Formalized 2026-03-06 (Session 037)**

This document specifies how the 61-dimensional SCL weight vector maps to CSS custom properties for the PPL± experience layer. The weight vector is not just a retrieval signal — it is a complete rendering instruction.

Reference: `middle-math/ARCHITECTURE.md` (Section 5 — Rendering Layer), `seeds/experience-layer-blueprint.md`

---

## Overview

Every PPL± room has a 61-dimensional weight vector. That vector encodes the room's complete SCL identity: which Order governs it, which Axis biases it, what Type it trains, what Color formats it, and how all the blocks and operators interact. The rendering layer reads this vector and derives CSS custom properties that shape the room's visual appearance, information density, typography, and tonal register.

**The zip code is a complete rendering instruction.** You do not need to pass separate style parameters. You pass a zip code, resolve its weight vector, and derive all visual properties from that vector.

---

## Octave Scale → Normalized Value

All 61 dimensions use the octave scale: `-8.0` to `+8.0`.

Normalization formula:

```
normalized = (weight + 8.0) / 16.0
```

This maps:
- `-8.0` → `0.0` (minimum, suppressed/excluded)
- `0.0`  → `0.5` (neutral)
- `+8.0` → `1.0` (maximum, defining character)

The normalized value drives CSS custom property values via linear interpolation between min and max bounds defined per property.

---

## Dimension Index Map

```
Indices 0–6:   ORDER dimensions
  [0] 🐂 Foundation
  [1] ⛽ Strength
  [2] 🦋 Hypertrophy
  [3] 🏟 Performance
  [4] 🌾 Full Body
  [5] ⚖ Balance
  [6] 🖼 Restoration

Indices 7–12:  AXIS dimensions
  [7]  🏛 Basics
  [8]  🔨 Functional
  [9]  🌹 Aesthetic
  [10] 🪐 Challenge
  [11] ⌛ Time
  [12] 🐬 Partner

Indices 13–17: TYPE dimensions
  [13] 🛒 Push
  [14] 🪡 Pull
  [15] 🍗 Legs
  [16] ➕ Plus
  [17] ➖ Ultra

Indices 18–25: COLOR dimensions
  [18] ⚫ Teaching
  [19] 🟢 Bodyweight
  [20] 🔵 Structured
  [21] 🟣 Technical
  [22] 🔴 Intense
  [23] 🟠 Circuit
  [24] 🟡 Fun
  [25] ⚪ Mindful

Indices 26–60: DERIVED dimensions
  [26–35] Block-level / temporal context (seasonal, rest period ratios)
  [36–50] Exercise family / operator affinity clusters
  [51–60] Interaction rules (suppression cascades, pairing matrices)
```

---

## CSS Custom Properties

All properties use the prefix `--ppl-weight-`. They are set on the room's root element (`.ppl-room` or `:root` when a single room is active) from the computed weight vector.

### Group 1: Order → Information Density

The active Order dimension (the one with the highest weight) drives the room's information density: font size, line height, spacing multiplier, and content compactness.

```css
--ppl-weight-density            /* float 0–1 → compactness of layout */
--ppl-weight-lineheight         /* float 0–1 → 1.35 (dense) to 1.85 (airy) */
--ppl-weight-font-weight        /* float 0–1 → 300 (light) to 900 (black) */
--ppl-weight-letter-spacing     /* float 0–1 → 0em to 0.05em */
--ppl-weight-spacing-multiplier /* float 0–1 → 0.75 (compact) to 1.5 (spacious) */
```

**Derivation:** Find the max-weighted Order dimension (index 0–6). Normalize that weight. Map to bounds:

| Property | At 0.0 (dim_min) | At 0.5 (neutral) | At 1.0 (dim_max) |
|----------|-----------------|-----------------|-----------------|
| density | 1.0 (most compact) | 0.7 | 0.4 (most spacious) |
| lineHeight | 1.35 | 1.6 | 1.85 |
| fontWeight | 700 | 500 | 300 |
| letterSpacing | 0em | 0.015em | 0.04em |
| spacingMultiplier | 0.75 | 1.0 | 1.5 |

Note: ⛽ Strength (+8, normalized 1.0) maps to density=0.4 (compact), fontWeight=300? — No: Strength is **heavy**. Density and font-weight move in opposite directions depending on the Order character. Use the `orders` block in `design-tokens.json` as the authoritative per-Order override. The formula above is the fallback for derived/blended states.

**Practical implementation:** For clean rendering, look up the active Order from the zip code and apply the corresponding `orders[name]` token from `design-tokens.json` directly. Use the weight-derived formula only for blended states where two Orders have competing weights.

---

### Group 2: Axis → Typography Character

The dominant Axis dimension drives typography style: font weight bias, letter spacing register, and visual rhythm.

```css
--ppl-weight-typography-bias    /* float 0–1 → typographic character */
--ppl-weight-visual-rhythm      /* float 0–1 → spacing regularity */
```

| Axis | Bias | Character |
|------|------|-----------|
| 🏛 Basics | Classical, structured | High contrast, geometric |
| 🔨 Functional | Athletic, utilitarian | Condensed, tracking-tight |
| 🌹 Aesthetic | Refined, sensory | Light weight, generous spacing |
| 🪐 Challenge | Intense, dramatic | Heavy, display-weight |
| ⌛ Time | Precise, technical | Monospace registers, numeric emphasis |
| 🐬 Partner | Warm, approachable | Rounded, open letterforms |

These map to typographic decisions in the rendering layer — e.g., ⌛ Time increases `font-variant-numeric: tabular-nums` emphasis, 🌹 Aesthetic increases `font-weight: 300` preference.

---

### Group 3: Type → Content Emphasis

The active Type dimension drives which muscle groups and movement patterns are visually emphasized in the workout display.

```css
--ppl-weight-emphasis-push   /* float 0–1 → visual prominence of push movements */
--ppl-weight-emphasis-pull   /* float 0–1 → visual prominence of pull movements */
--ppl-weight-emphasis-legs   /* float 0–1 → visual prominence of leg movements */
--ppl-weight-emphasis-plus   /* float 0–1 → visual prominence of power movements */
--ppl-weight-emphasis-ultra  /* float 0–1 → visual prominence of conditioning */
```

Derived from dim indices 13–17. High weight → that Type's movement label, muscle group callout, and exercise entries receive higher visual priority (larger text, more spacing, earlier in visual hierarchy).

---

### Group 4: Color → Theme and Saturation

The active Color dimension drives the room's color theme, saturation level, and format cues.

```css
--ppl-theme-primary     /* hex — primary color from design-tokens.json colors[active_color] */
--ppl-theme-secondary   /* hex */
--ppl-theme-background  /* hex */
--ppl-theme-surface     /* hex */
--ppl-theme-text        /* hex */
--ppl-theme-accent      /* hex */
--ppl-theme-border      /* hex */

--ppl-weight-saturation /* float 0–1 → color intensity */
--ppl-weight-contrast   /* float 0–1 → light/dark contrast ratio */
```

**Saturation mapping (from Color × Order interaction):**
- 🔴 Intense + ⛽ Strength → saturation 0.9 (vivid, high energy)
- ⚪ Mindful + 🖼 Restoration → saturation 0.2 (near-monochrome, calm)
- 🟡 Fun + 🦋 Hypertrophy → saturation 0.75 (bright, playful)
- ⚫ Teaching + any Order → saturation 0.05 (desaturated, focus on content)

Active color theme is determined by the highest-weighted Color dimension (index 18–25). Look up the color entry in `design-tokens.json` and apply its full palette.

---

### Group 5: Derived Dims → Structural Modifiers

The derived dimensions (26–60) encode block sequencing, operator affinities, and interaction rules. These drive structural UI decisions.

```css
--ppl-weight-rest-emphasis   /* float 0–1 → how prominently rest periods display */
--ppl-weight-rep-display     /* float 0–1 → rep scheme prominence vs exercise name */
--ppl-weight-block-spacing   /* float 0–1 → spacing between workout blocks */
--ppl-weight-cue-density     /* float 0–1 → how many coaching cues display by default */
```

| Derived cluster | Dims | Maps to |
|-----------------|------|---------|
| Block-level/temporal | 26–35 | Rest period display prominence, session rhythm indicators |
| Exercise family/operator | 36–50 | Exercise entry density, rep scheme layout, operator verb display |
| Interaction rules | 51–60 | Suppression signals (e.g., GOLD gate indicator), pairing brackets |

---

## CSS Custom Property Generation (TypeScript)

```typescript
// Normalize a single weight dimension to [0, 1]
function normalize(weight: number): number {
  return (weight + 8.0) / 16.0;
}

// Find index of maximum weight in a slice
function dominantDim(vector: number[], start: number, end: number): number {
  let maxIdx = start;
  let maxVal = vector[start];
  for (let i = start + 1; i <= end; i++) {
    if (vector[i] > maxVal) {
      maxVal = vector[i];
      maxIdx = i;
    }
  }
  return maxIdx;
}

// Interpolate between min and max by normalized value
function lerp(min: number, max: number, t: number): number {
  return min + (max - min) * t;
}

// Generate all CSS custom properties from a 61-float weight vector
function generateWeightCSS(vector: number[]): Record<string, string> {
  const props: Record<string, string> = {};

  // Order dims [0–6]: density, lineHeight, fontWeight, letterSpacing, spacingMult
  const orderDim = dominantDim(vector, 0, 6);
  const orderNorm = normalize(vector[orderDim]);
  props['--ppl-weight-density']            = lerp(1.0, 0.4, orderNorm).toFixed(3);
  props['--ppl-weight-lineheight']         = lerp(1.35, 1.85, orderNorm).toFixed(2);
  props['--ppl-weight-font-weight']        = Math.round(lerp(700, 300, orderNorm)).toString();
  props['--ppl-weight-letter-spacing']     = lerp(0, 0.04, orderNorm).toFixed(3) + 'em';
  props['--ppl-weight-spacing-multiplier'] = lerp(0.75, 1.5, orderNorm).toFixed(2);

  // Axis dims [7–12]: typography bias
  const axisDim = dominantDim(vector, 7, 12);
  const axisNorm = normalize(vector[axisDim]);
  props['--ppl-weight-typography-bias']  = axisNorm.toFixed(3);
  props['--ppl-weight-visual-rhythm']    = axisNorm.toFixed(3);

  // Type dims [13–17]: content emphasis per type
  const TYPE_NAMES = ['push', 'pull', 'legs', 'plus', 'ultra'];
  for (let i = 0; i < 5; i++) {
    props[`--ppl-weight-emphasis-${TYPE_NAMES[i]}`] = normalize(vector[13 + i]).toFixed(3);
  }

  // Color dims [18–25]: saturation and contrast
  const colorDim = dominantDim(vector, 18, 25);
  const colorNorm = normalize(vector[colorDim]);
  props['--ppl-weight-saturation'] = colorNorm.toFixed(3);
  props['--ppl-weight-contrast']   = colorNorm.toFixed(3);

  // Derived dims [26–60]: structural modifiers
  // Rest emphasis: mean of temporal cluster [26–35]
  const restMean = vector.slice(26, 36).reduce((a, b) => a + b, 0) / 10;
  props['--ppl-weight-rest-emphasis'] = normalize(restMean).toFixed(3);

  // Rep display: mean of exercise/operator cluster [36–50]
  const repMean = vector.slice(36, 51).reduce((a, b) => a + b, 0) / 15;
  props['--ppl-weight-rep-display'] = normalize(repMean).toFixed(3);

  // Block spacing: mean of derived cluster normalized
  const blockMean = vector.slice(26, 61).reduce((a, b) => a + b, 0) / 35;
  props['--ppl-weight-block-spacing'] = normalize(blockMean).toFixed(3);

  // Cue density: interaction rule cluster [51–60]
  const cueMean = vector.slice(51, 61).reduce((a, b) => a + b, 0) / 10;
  props['--ppl-weight-cue-density'] = normalize(cueMean).toFixed(3);

  return props;
}
```

---

## Applying Properties in Next.js (App Router)

```tsx
// app/zip/[zipcode]/room-styles.tsx
import { generateWeightCSS } from '@/lib/weight-css';
import { getWeightVector }   from '@/lib/weight-vectors';

export async function RoomStyles({ zipcode }: { zipcode: string }) {
  const vector = await getWeightVector(zipcode);
  const props  = generateWeightCSS(vector);

  // Convert to inline style string
  const styleStr = Object.entries(props)
    .map(([k, v]) => `${k}: ${v}`)
    .join('; ');

  return (
    <style>{`:root { ${styleStr} }`}</style>
  );
}
```

The color theme is applied separately by looking up the active color from `design-tokens.json`:

```tsx
// Find dominant Color dim (18–25), map to color name, apply full palette
const COLOR_KEYS = ['teaching','bodyweight','structured','technical','intense','circuit','fun','mindful'];
const colorIdx   = dominantDim(vector, 18, 25) - 18;  // 0–7
const activeColor = tokens.colors[COLOR_KEYS[colorIdx]];

// Set theme CSS variables
root.style.setProperty('--ppl-theme-primary',    activeColor.primary);
root.style.setProperty('--ppl-theme-background', activeColor.background);
// ... etc
```

---

## Fallback Values

When the weight vector is neutral (all values near 0, normalized near 0.5), apply these fallback tokens:

```css
:root {
  --ppl-weight-density:            0.7;
  --ppl-weight-lineheight:         1.6;
  --ppl-weight-font-weight:        500;
  --ppl-weight-letter-spacing:     0.015em;
  --ppl-weight-spacing-multiplier: 1.0;
  --ppl-weight-saturation:         0.6;
  --ppl-weight-contrast:           0.6;
  --ppl-weight-rest-emphasis:      0.5;
  --ppl-weight-rep-display:        0.5;
  --ppl-weight-block-spacing:      0.5;
  --ppl-weight-cue-density:        0.5;
}
```

Neutral fallback theme: `design-tokens.json → colors.structured` (🔵 Structured — the canonical neutral color for the PPL± system).

---

## Design Constraints

1. **No hardcoded hex values in components.** All colors come from `--ppl-theme-*` variables derived from the active zip's Color dim.
2. **No separate style configuration per zip code.** The weight vector is the single source of visual truth.
3. **Accessibility floor.** `--ppl-weight-contrast` must never produce a contrast ratio below 4.5:1 (WCAG AA). The rendering layer clamps contrast values before applying them.
4. **Smooth transitions.** When navigating between rooms, CSS transitions on `--ppl-weight-*` properties use `animation.default` (250ms) with `easing.standard`.
5. **Dark mode.** The 8 Color palettes have a single light-mode specification in `design-tokens.json`. Dark mode variants are derived by rotating hue and adjusting lightness — not defined here, planned for Phase 4 build.

---

*See also: `middle-math/design-tokens.json` · `seeds/experience-layer-blueprint.md` · `middle-math/ARCHITECTURE.md` (Section 5)*
