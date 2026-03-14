# Phase 4: Design Tokens - Research

**Researched:** 2026-03-14
**Domain:** Design token system (style-dictionary, OKLCH color science, CSS custom properties, TypeScript output)
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **Fresh color derivation using color theory math** — do NOT port the existing DRAFT values from middle-math/design-tokens.json. The old colors predate the intaglio art direction and need to be reworked from scratch.
- **Scalable property system** — do NOT hard-limit to 7 properties per palette. Design an extensible token structure where additional properties (textOnLight, shadow, glow, etc.) can be added without restructuring. Good architecture > fixed count.
- **Tonal names as semantic keys** — use Color Context Vernacular tonal names (order, growth, planning, magnificence, passion, connection, play, eudaimonia) NOT SCL emoji names (teaching, bodyweight, structured...) as the token namespace. CSS reads: `--ppl-color-passion--primary`.
- **3+1 dial ownership model:** Order = structural, Color = tonal, Axis = directional, Type = icon/illustration tokens. No property has two owners.
- **No property has two owners.** The arbitration spec must be exhaustive.
- **This spec MUST exist before any Phase 5 deriver code** — blocking dependency.
- **Nested CSS custom property naming** — double-hyphen nesting: `--ppl-color-passion--primary`, `--ppl-order-strength--fontWeight`.
- **Build produces both CSS and TypeScript** — design-tokens.css and tokens.ts, consumable by both canvas/ and web/.
- **The intaglio/banknote engraving aesthetic is the visual north star.**

### Claude's Discretion
- Color science methodology (OKLCH, HSL, or other) — researcher recommends, planner implements
- Exact base hue values per Color — derived from color theory + intaglio aesthetic
- Typographic scale values (fontWeight, lineHeight, spacingMultiplier per Order)
- style-dictionary configuration and transform setup
- Whether to use style-dictionary v3 or v4 API
- Typographic variation per Order (distinct vs. subtle)
- Typeface direction
- Axis gradient meaning (literal CSS gradients vs. visual flow parameters vs. both)
- Edge-case property assignment (animation speed, border radius, opacity, shadow depth)
- Source file location and output layout

### Deferred Ideas (OUT OF SCOPE)
- Per-exercise illustration tokens (Type owns the token slot but actual illustrations are content, not infrastructure)
- Dark mode / theme variants (token structure should support it but variants are not Phase 4 scope)
- Animation/motion tokens (token slots should exist but actual values may come from Phase 5 rendering work)
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| RNDR-01 | design-tokens.json encoding all 8 Color palettes (7 CSS props each: primary, secondary, background, surface, text, accent, border) | OKLCH-derived palette architecture; culori library; tonal name mapping from color-context-vernacular.md |
| RNDR-02 | design-tokens.json encoding all 7 Order typographies (fontWeight, lineHeight, spacingMultiplier) | DRAFT orders data in existing design-tokens.json provides valid starting shape; values need recalibration against intaglio aesthetic; weight-css-spec.md defines normalization bounds |
| RNDR-03 | design-tokens.json encoding all 6 Axis gradient directions | Research conclusion: Axis gradient = both a literal CSS gradient direction token AND a visual flow parameter (layout direction/hierarchy bias); 6 directional values derived from Axis character |
| RNDR-04 | CSS arbitration spec defining property ownership (structural: Order, tonal: Color, directional: Axis) | 3+1 model locked in CONTEXT.md; edge-case resolution research documented below |
</phase_requirements>

---

## Summary

Phase 4 produces three artifacts: (1) `design-tokens.json` — the single authoritative source for all static visual values, (2) `canvas/src/tokens/design-tokens.css` — CSS custom properties for use in web/, (3) `canvas/src/tokens/tokens.ts` — TypeScript object for use in canvas/ modules. A fourth artifact, the CSS Arbitration Spec (`04-CSS-ARBITRATION.md`), is a blocking document that must be finalized before Phase 5 writes any `weightsToCSSVars()` code.

The DRAFT `middle-math/design-tokens.json` file is a structural reference only. Its values (HSL-derived hex colors, DRAFT watermark) must be discarded and rederived. The structure (colors object, orders object, spacing, borderRadius, animation) is a sound template; the token nesting pattern shifts from flat key-value to double-hyphen CSS naming.

The critical research finding is that **OKLCH is the correct color space** for this project. It is perceptually uniform (equal numeric changes = equal perceived changes), browser-supported in all modern browsers (Chrome 111+, Firefox 113+, Safari 15.4+), and uniquely suited to algorithmic palette generation — which is exactly what fresh derivation requires. HSL produces inconsistent perceived lightness across hues, making it unsuitable for a mathematically derived system.

**Primary recommendation:** Use OKLCH for all color value storage. Use style-dictionary v4 (not v5) for the build pipeline because canvas/ is already ESM and v4 is battle-tested stable. Use `culori` (the canonical JavaScript OKLCH manipulation library) for color derivation scripts. Write the CSS Arbitration Spec as the first plan in this phase, before any token values are set.

---

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| style-dictionary | ^4.x (v4.3.x current stable in v4 branch; v5.3.3 is current overall) | Token compilation: JSON → CSS + TypeScript | Industry standard token build system; v4 is fully ESM (matches canvas/ tsconfig ESNext modules); v4 ships with `css/variables` and `typescript/esm-declarations` built-in formats |
| culori | ^4.x | OKLCH color manipulation, palette derivation | Canonical JS color library used by Evil Martians, Atmos, and the official CSS Color Level 4 tooling ecosystem; handles all OKLCH math without custom implementation |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Node.js script | built-in | Color derivation script: hue table → OKLCH values → design-tokens.json | Run once to generate token values; committed output is the artifact |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| OKLCH | HSL | HSL is perceptually non-uniform (blue at 50% lightness is visually darker than yellow at 50%); HSL cannot support algorithmic palette generation that looks consistent across all 8 hues |
| OKLCH | LCH | LCH uses different lightness model; OKLCH (Oklab-derived) is more uniform and is the W3C recommendation; both are viable but OKLCH is the current ecosystem standard |
| style-dictionary v4 | style-dictionary v5 | v5 is current but v4 is more documented with more community examples; canvas/ is already ESM so v4 works without friction; v4 → v5 migration path exists; use v4 for stability |
| style-dictionary | custom build script | Style-dictionary handles transforms, references, multiple output formats, file headers, and future extensibility; custom script would need to reimplement all this |

**Installation:**
```bash
# In canvas/ directory (where the build lives)
npm install --save-dev style-dictionary culori
```

---

## Architecture Patterns

### Recommended Project Structure
```
canvas/
├── src/
│   ├── tokens/
│   │   ├── design-tokens.json          # Master source (authored here, not in middle-math/)
│   │   ├── design-tokens.css           # Build artifact: CSS custom properties
│   │   └── tokens.ts                   # Build artifact: TypeScript object
│   ├── tokens/build/
│   │   └── build-tokens.mjs            # style-dictionary build script (ESM)
│   ├── types/
│   │   └── scl.ts                      # Existing
│   └── weights/                        # Existing
├── scripts/
│   └── derive-colors.mjs               # OKLCH derivation script (run once, produces token values)
└── tests/
    └── tokens.test.ts                  # Vitest tests: token shape validation
```

Note on source file location: The CONTEXT.md states `middle-math/design-tokens.json` is the existing DRAFT. Research finding: the canonical source should live in `canvas/src/tokens/design-tokens.json` because (1) canvas/ is the authoritative computation layer, (2) the style-dictionary build script lives in canvas/, (3) keeping tokens co-located with the TypeScript types they feed prevents drift. The middle-math/ copy becomes a read-only historical reference only.

### Pattern 1: style-dictionary v4 Build Config (ESM)

**What:** ESM build script that reads design-tokens.json and emits CSS and TypeScript.
**When to use:** Run in canvas/ as a build step; output artifacts are committed.

```javascript
// canvas/src/tokens/build/build-tokens.mjs
// Source: https://styledictionary.com/reference/config/
import StyleDictionary from 'style-dictionary';

const sd = new StyleDictionary({
  source: ['canvas/src/tokens/design-tokens.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      buildPath: 'canvas/src/tokens/',
      files: [
        {
          destination: 'design-tokens.css',
          format: 'css/variables',
          options: {
            selector: ':root',
            outputReferences: false,
          },
        },
      ],
    },
    typescript: {
      transformGroup: 'js',
      buildPath: 'canvas/src/tokens/',
      files: [
        {
          destination: 'tokens.ts',
          format: 'javascript/esm',
        },
      ],
    },
  },
});

await sd.hasInitialized;
await sd.buildAllPlatforms();
```

Note: style-dictionary v4 is async. Must await `sd.hasInitialized` before building.

### Pattern 2: OKLCH Palette Structure

**What:** How each Color entry is structured in design-tokens.json using OKLCH values.
**When to use:** All 8 Color palette entries follow this shape.

The intaglio aesthetic constraint shapes hue selection directly:
- Banknote colors are never saturated digital primaries. They are deep, ink-like, and hold contrast on cream/off-white backgrounds.
- High-chroma OKLCH values belong only to Passion (🔴) and Magnificence (🟣) — the GOLD Colors.
- Order (⚫) and Eudaimonia (⚪) should anchor near achromatic (chroma < 0.02).

OKLCH value format: `oklch(L C H)` where L ∈ [0,1], C ∈ [0,0.37] (practical max), H ∈ [0,360].

```json
// In design-tokens.json: colors section (OKLCH values stored as strings)
"colors": {
  "passion": {
    "emoji": "🔴",
    "scl_name": "Intense",
    "tonal_name": "Passion",
    "base_hue": 25,
    "base_chroma": 0.22,
    "tier": "2-4",
    "gold": true,
    "primary":    "oklch(0.42 0.22 25)",
    "secondary":  "oklch(0.52 0.18 25)",
    "background": "oklch(0.97 0.02 25)",
    "surface":    "oklch(1.0 0.0 0)",
    "text":       "oklch(0.28 0.14 25)",
    "accent":     "oklch(0.36 0.20 25)",
    "border":     "oklch(0.82 0.06 25)"
  }
}
```

CSS output via style-dictionary transform: `--ppl-color-passion--primary: oklch(0.42 0.22 25);`

Note: The `--ppl-color-passion--primary` naming uses double-hyphen per CONTEXT.md. Style-dictionary's name transforms use the JSON key path to build CSS variable names; a custom transform or naming convention in the JSON key structure achieves the `--ppl-[category]-[tone]--[property]` pattern.

### Pattern 3: CSS Arbitration Spec Structure

**What:** Flat table mapping every CSS custom property to exactly one dial owner.
**When to use:** Must exist as `04-CSS-ARBITRATION.md` before Phase 5 writes any rendering code.

```markdown
# CSS Property Arbitration Spec

| CSS Custom Property | Owner Dial | Value Source | Notes |
|---------------------|-----------|--------------|-------|
| --ppl-order-*--fontWeight | Order | design-tokens.json orders[name].fontWeight | 7 values |
| --ppl-order-*--lineHeight | Order | design-tokens.json orders[name].lineHeight | 7 values |
| --ppl-order-*--spacingMultiplier | Order | design-tokens.json orders[name].spacingMultiplier | 7 values |
| --ppl-order-*--density | Order | design-tokens.json orders[name].density | 7 values |
| --ppl-order-*--letterSpacing | Order | design-tokens.json orders[name].letterSpacing | 7 values |
| --ppl-color-*--primary | Color | design-tokens.json colors[name].primary | 8 values |
| --ppl-color-*--secondary | Color | design-tokens.json colors[name].secondary | 8 values |
| --ppl-color-*--background | Color | design-tokens.json colors[name].background | 8 values |
| --ppl-color-*--surface | Color | design-tokens.json colors[name].surface | 8 values |
| --ppl-color-*--text | Color | design-tokens.json colors[name].text | 8 values |
| --ppl-color-*--accent | Color | design-tokens.json colors[name].accent | 8 values |
| --ppl-color-*--border | Color | design-tokens.json colors[name].border | 8 values |
| --ppl-axis-*--gradientDirection | Axis | design-tokens.json axes[name].gradientDirection | 6 values |
| --ppl-axis-*--layoutFlow | Axis | design-tokens.json axes[name].layoutFlow | 6 values |
```

### Pattern 4: Axis Gradient Resolution

**Research finding:** "Axis gradient" should be both (1) a literal CSS `gradient-direction` token and (2) a visual flow parameter token. Each Axis has a directional character:

| Axis | Tonal Character | CSS Gradient Direction | Layout Flow |
|------|----------------|----------------------|-------------|
| 🏛 Basics | Stable, grounded | `to bottom` (vertical, classic) | `column` |
| 🔨 Functional | Athletic, forward-moving | `135deg` (diagonal, active) | `row` |
| 🌹 Aesthetic | Refined, sensory | `to bottom right` (soft diagonal) | `column-reverse` |
| 🪐 Challenge | Dramatic, upward | `to top` (vertical, ascending) | `column` |
| ⌛ Time | Precise, sequential | `to right` (horizontal, timeline) | `row` |
| 🐬 Partner | Warm, centripetal | `radial` (center-outward) | `row` |

Token shape:
```json
"axes": {
  "basics": {
    "emoji": "🏛",
    "gradientDirection": "to bottom",
    "layoutFlow": "column",
    "typographyBias": "classical"
  }
}
```

### Pattern 5: Order Typography Token Shape

**Research finding:** The DRAFT design-tokens.json `orders` section has the correct shape. Values need recalibration for the intaglio aesthetic. The recommended approach uses distinct variation per Order (not subtle), because each Order IS a different cognitive and physical state — the typography should encode that distinction.

Intaglio calibration principle: strong weight contrast (fontWeight 300 ↔ 900), controlled letter-spacing (0 ↔ 0.04em), and restrained line-height variation (1.35 ↔ 1.85). This matches the controlled precision of engraved letterforms.

```json
"orders": {
  "strength": {
    "emoji": "⛽",
    "fontWeight": 800,
    "fontWeightDisplay": 900,
    "lineHeight": 1.40,
    "spacingMultiplier": 0.85,
    "letterSpacing": "0.005em",
    "density": "compact"
  },
  "restoration": {
    "emoji": "🖼",
    "fontWeight": 300,
    "fontWeightDisplay": 400,
    "lineHeight": 1.85,
    "spacingMultiplier": 1.50,
    "letterSpacing": "0.04em",
    "density": "airy"
  }
}
```

### Pattern 6: Edge-Case CSS Property Assignments

**Research finding:** A consistent principle resolves all edge cases. Apply "what dimension does this property MOST express the character of?"

| Property | Owner | Principle |
|----------|-------|-----------|
| `border-radius` | Color | Roundness is a tonal quality: Order (⚫) = sharp corners; Eudaimonia (⚪) = softly rounded. It expresses Color character. |
| `shadow-depth` | Color | Shadow intensity tracks Color saturation and mood; dark Colors = deeper shadows. Tonal, not structural. |
| `opacity` (default states) | Order | Opacity affects information density; 🖼 Restoration uses lighter opacity elements. Structural. |
| `animation-duration` | Order | Animation speed is a structural rhythm property. 🏟 Performance = instant transitions; 🖼 Restoration = slow, deliberate. |
| `font-family` | Axis | Font family (not weight) expresses Axis character: ⌛ Time → monospace numeric emphasis; 🌹 Aesthetic → editorial serif; 🔨 Functional → condensed. |
| `gradient-direction` | Axis | Directional, locked. |
| `grid-gap / block-gap` | Order | Spacing density is Order's structural domain. |

**Summary principle:** If a property encodes intensity/mood → Color. If it encodes rhythm/density/weight → Order. If it encodes direction/character → Axis.

### Anti-Patterns to Avoid

- **Double-owning a property:** Any CSS property that appears in both Order and Color sections of the arbitration spec is a design error. The spec must be exhaustive and conflict-free before Phase 5 starts.
- **HSL hex values in OKLCH-based system:** Never mix hex color strings derived from HSL with OKLCH strings in the same token file. Pick one and use it throughout.
- **Hardcoded hex in components:** The weight-css-spec.md states this explicitly. All colors via `--ppl-theme-*` variables.
- **Regenerating tokens on every render:** The build artifacts (design-tokens.css, tokens.ts) are static files committed to the repo. They are not runtime-generated. The weight vector renderer (Phase 5) reads token values from the static tokens.ts.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| OKLCH color math | Custom oklch() functions | `culori` library | OKLCH gamut mapping, clamping, interpolation, and conversion are non-trivial; culori is the ecosystem standard, used by official CSS Color Level 4 tools |
| Token compilation | Custom JSON-to-CSS script | `style-dictionary` v4 | References, transforms, multiple platform outputs, file headers, source maps — all handled; custom scripts break on edge cases and need ongoing maintenance |
| Color contrast checking | Manual ratio calculation | `culori` + WCAG formula | culori includes deltaE and contrast utilities; the weight-css-spec.md requires WCAG AA (4.5:1) floor |
| CSS variable naming | Manual string templates | style-dictionary name transforms | style-dictionary's `name/kebab` transform (v4) produces consistent kebab-case names from JSON key paths |

**Key insight:** OKLCH palette generation looks simple but requires gamut clamping (not all OKLCH values are displayable in sRGB), which culori handles correctly. Hand-rolled OKLCH math will produce out-of-gamut values that render as mud on some screens.

---

## Common Pitfalls

### Pitfall 1: style-dictionary v4 Requires Async Init
**What goes wrong:** Calling `sd.buildAllPlatforms()` immediately after `new StyleDictionary(config)` without awaiting `sd.hasInitialized` fails silently or with obscure errors.
**Why it happens:** v4 rewrote in ES Modules; initialization is async.
**How to avoid:** Always `await sd.hasInitialized` before any build/format calls.
**Warning signs:** Build completes with 0 output files; no error thrown.

### Pitfall 2: OKLCH Out-of-Gamut Values
**What goes wrong:** High-chroma OKLCH values (C > 0.20 for certain hues) fall outside the sRGB gamut and render as clipped/muddy colors in browsers that don't support wide-gamut displays.
**Why it happens:** OKLCH covers a larger color space than sRGB. Not all valid OKLCH values are representable in CSS on standard displays.
**How to avoid:** Use `culori`'s `toGamut()` function when deriving palette values. Target P3 as the maximum gamut; sRGB for the fallback. Verify on a standard display.
**Warning signs:** Colors look desaturated or shifted on phone screens vs. design tools.

### Pitfall 3: Double-Hyphen CSS Variable Naming Conflict
**What goes wrong:** The locked naming convention `--ppl-color-passion--primary` uses double-hyphen to separate category from property. Style-dictionary's built-in name transforms use single hyphens everywhere. Without a custom transform, output becomes `--ppl-color-passion-primary`.
**Why it happens:** style-dictionary's `name/kebab` transform joins all JSON path segments with single hyphens.
**How to avoid:** Use a custom style-dictionary name transform that preserves the structural separator. OR structure the JSON with a nested key that encodes the double-hyphen boundary: e.g., the token key path `colors.passion.primary` maps to `--ppl-color-passion--primary` via a registered custom transform.
**Warning signs:** Generated CSS variables don't match the naming pattern in weight-css-spec.md.

### Pitfall 4: W Enum Index Offset Mismatch
**What goes wrong:** Phase 5's `weightsToCSSVars()` will reference W enum positions to find the dominant dial. The existing weight-css-spec.md uses 0-indexed positions (dims 0–6 for Orders) while the W enum in scl.ts uses 1-indexed positions (W.FOUNDATION = 1). If Phase 4's tokens.ts exports named access by W position, the off-by-one mismatch causes wrong token lookups.
**Why it happens:** weight-css-spec.md was written before the W enum was formalized in scl.ts.
**How to avoid:** The CSS Arbitration Spec (RNDR-04) must explicitly state which index convention the rendering layer uses. tokens.ts should export by semantic name (`tokens.colors.passion`), not by numeric index.
**Warning signs:** Wrong color themes applied to certain zip codes.

### Pitfall 5: Anchoring at tonal_name vs. scl_name
**What goes wrong:** The existing DRAFT design-tokens.json has both `tonal_name` and `scl_name` fields, and uses `scl_name` slugs as top-level keys (e.g., `"teaching"`, `"bodyweight"`). CONTEXT.md locks tonal names as the token namespace. Using the wrong key name cascades through CSS variable names.
**Why it happens:** Historical naming from before the tonal layer was formalized.
**How to avoid:** Top-level keys in the `colors` object MUST use tonal names: `order`, `growth`, `planning`, `magnificence`, `passion`, `connection`, `play`, `eudaimonia`. The `scl_name` field stays as metadata inside each entry.
**Warning signs:** CSS output reads `--ppl-color-teaching--primary` instead of `--ppl-color-order--primary`.

---

## Code Examples

### OKLCH Palette Derivation with culori

```javascript
// canvas/scripts/derive-colors.mjs
// Source: https://culorijs.org/
import { oklch, toGamut, formatCss } from 'culori';

// Base hue table — derived from intaglio aesthetic research
// Intaglio principle: deep, ink-like, not digital-primary
const BASE_HUES = {
  order:        { h: 0,   c: 0.00, lPrimary: 0.20 },  // ⚫ Near-achromatic black
  growth:       { h: 145, c: 0.12, lPrimary: 0.42 },  // 🟢 Forest green, not neon
  planning:     { h: 230, c: 0.14, lPrimary: 0.40 },  // 🔵 Deep Prussian blue
  magnificence: { h: 285, c: 0.18, lPrimary: 0.38 },  // 🟣 Deep violet, GOLD
  passion:      { h: 25,  c: 0.22, lPrimary: 0.42 },  // 🔴 Vermillion ink, GOLD
  connection:   { h: 45,  c: 0.18, lPrimary: 0.55 },  // 🟠 Warm amber
  play:         { h: 85,  c: 0.16, lPrimary: 0.72 },  // 🟡 Brass yellow
  eudaimonia:   { h: 60,  c: 0.02, lPrimary: 0.92 },  // ⚪ Cream white, near-achromatic
};

function deriveColorPalette(tonalName, { h, c, lPrimary }) {
  const gamutTarget = 'p3';  // Target P3 gamut; sRGB is automatic fallback

  const primary    = toGamut(oklch(lPrimary, c, h), gamutTarget);
  const secondary  = toGamut(oklch(lPrimary + 0.10, c * 0.80, h), gamutTarget);
  const background = toGamut(oklch(0.97, c * 0.10, h), gamutTarget);
  const surface    = toGamut(oklch(1.00, 0, 0), gamutTarget);
  const text       = toGamut(oklch(lPrimary - 0.14, c * 0.65, h), gamutTarget);
  const accent     = toGamut(oklch(lPrimary - 0.06, c * 0.90, h), gamutTarget);
  const border     = toGamut(oklch(0.82, c * 0.30, h), gamutTarget);

  return {
    primary:    formatCss(primary),
    secondary:  formatCss(secondary),
    background: formatCss(background),
    surface:    formatCss(surface),
    text:       formatCss(text),
    accent:     formatCss(accent),
    border:     formatCss(border),
  };
}
```

### style-dictionary v4 Custom Name Transform (double-hyphen)

```javascript
// Registers a custom transform to produce --ppl-color-passion--primary naming
// Source: https://styledictionary.com/versions/v4/migration/
import StyleDictionary from 'style-dictionary';

StyleDictionary.registerTransform({
  name: 'name/ppl/css-var',
  type: 'name',
  transform(token) {
    // token.path = ['colors', 'passion', 'primary']
    // target:      --ppl-color-passion--primary
    const [category, group, property] = token.path;
    // 'colors' → 'color', strip trailing 's'
    const categorySlug = category.replace(/s$/, '');
    return `ppl-${categorySlug}-${group}--${property}`;
  },
});
```

### tokens.ts Output Shape

```typescript
// Generated artifact: canvas/src/tokens/tokens.ts
// Consumed by Phase 5's weightsToCSSVars()

export const tokens = {
  colors: {
    order: {
      primary: 'oklch(0.20 0.00 0)',
      secondary: 'oklch(0.32 0.00 0)',
      background: 'oklch(0.97 0.00 0)',
      surface: 'oklch(1.00 0.00 0)',
      text: 'oklch(0.06 0.00 0)',
      accent: 'oklch(0.14 0.00 0)',
      border: 'oklch(0.82 0.00 0)',
    },
    passion: {
      primary: 'oklch(0.42 0.22 25)',
      // ...
    },
    // 8 tonal names total
  },
  orders: {
    foundation: { fontWeight: 400, lineHeight: 1.75, spacingMultiplier: 1.25, letterSpacing: '0.02em', density: 'spacious' },
    strength:   { fontWeight: 800, lineHeight: 1.40, spacingMultiplier: 0.85, letterSpacing: '0.005em', density: 'compact' },
    // ...7 orders
  },
  axes: {
    basics:     { gradientDirection: 'to bottom', layoutFlow: 'column' },
    functional: { gradientDirection: '135deg', layoutFlow: 'row' },
    // ...6 axes
  },
} as const;

export type Tokens = typeof tokens;
export type TonalColorName = keyof typeof tokens.colors;
export type OrderName = keyof typeof tokens.orders;
export type AxisName = keyof typeof tokens.axes;
```

### Color Name Mapping (tonal → scl → W enum position)

```typescript
// Bridge table needed by Phase 5 to map W enum positions to token keys
// W.TEACHING=19, W.BODYWEIGHT=20, ... but tokens use tonal names

export const COLOR_W_TO_TONAL: Record<number, TonalColorName> = {
  19: 'order',         // W.TEACHING
  20: 'growth',        // W.BODYWEIGHT
  21: 'planning',      // W.STRUCTURED
  22: 'magnificence',  // W.TECHNICAL
  23: 'passion',       // W.INTENSE
  24: 'connection',    // W.CIRCUIT
  25: 'play',          // W.FUN
  26: 'eudaimonia',    // W.MINDFUL
};
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| HSL hex values for design tokens | OKLCH oklch() values | CSS Color Level 4, browser support 2023+ | Perceptually uniform palettes; algorithmic generation works correctly |
| style-dictionary CommonJS config | style-dictionary v4 ESM config | 2024 (v4 release) | Async init required; hooks API restructured; must await sd.hasInitialized |
| CTI-based transform names (name/cti/kebab) | Simplified names (name/kebab) | style-dictionary v4 | Old transform names still work in v4 for compatibility but are deprecated |
| Static hex design tokens | OKLCH with gamut-mapped fallbacks | 2024-2025 | Wide-gamut P3 support on modern phones; sRGB fallback automatic in CSS |

**Deprecated/outdated:**
- `style-dictionary v3 CommonJS `extend()` pattern`: Still works but v4's class instantiation is the current pattern
- `hex colors in design-token files`: Functional but loses the OKLCH perceptual uniformity advantage; the existing DRAFT values are in hex and should not be ported

---

## Open Questions

1. **Exact base hue values per Color**
   - What we know: The intaglio aesthetic requires deep, ink-like colors; OKLCH hue values can be derived from the Color Context Vernacular tonal character descriptions
   - What's unclear: The exact hue, chroma, and lightness that best represents each Color's tonal identity on a phone screen while evoking banknote aesthetics
   - Recommendation: The planner should include a task for deriving and visually reviewing hue values (this cannot be validated without rendering); start with the hue table in the code examples above as an initial pass, plan for iteration

2. **Typeface selection**
   - What we know: Intaglio aesthetic points toward engraved letterforms: high-contrast transitional serifs, slab serifs, or condensed sans-serifs; Playfair Display (Google Fonts) is a high-contrast transitional serif matching late 18th-century aesthetics; Spectral is an editorial serif with 7 weights; Bitter is a screen-optimized slab serif
   - What's unclear: Whether typeface tokens belong in Phase 4 (design-tokens.json) or Phase 5 (rendering layer); whether multiple typefaces are used per Axis or a single typeface serves all Axes with weight/style variation
   - Recommendation: Phase 4 should define `fontFamily` tokens per Axis as strings in design-tokens.json; the actual font loading (CSS @import / next/font) is Phase 5. Candidate families: Playfair Display (display/Axis 🏛 🌹), Spectral (editorial), IBM Plex Mono (⌛ Time).

3. **style-dictionary version: v4 vs v5**
   - What we know: v5.3.3 is current (as of March 2026); v4.3.x is the stable v4 branch; canvas/ is ESM-compatible with both
   - What's unclear: Whether any v5 features are needed for this phase
   - Recommendation: Use v4 (specifically the latest v4.x, `npm install style-dictionary@4`). The v4 API is well-documented, battle-tested, and the migration path to v5 exists if needed. V5 does not offer features required by Phase 4.

---

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Vitest ^3.0.0 |
| Config file | `canvas/vite.config.ts` (Vitest configured via vite) |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| RNDR-01 | design-tokens.json has 8 Color entries, each with required palette keys | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-02 | design-tokens.json has 7 Order entries, each with fontWeight/lineHeight/spacingMultiplier | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-03 | design-tokens.json has 6 Axis entries, each with gradientDirection and layoutFlow | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-04 | CSS arbitration spec document exists at expected path | unit (file existence) | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-01 | Build script produces design-tokens.css with all CSS custom properties | integration | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-01 | tokens.ts exports are importable TypeScript with expected shape | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-01 | Color tonal keys are tonal names (not scl names) | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |
| RNDR-01 | COLOR_W_TO_TONAL bridge covers all 8 W positions (19-26) | unit | `cd canvas && npm test -- tokens.test.ts` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `cd canvas && npm test -- tokens.test.ts`
- **Per wave merge:** `cd canvas && npm test`
- **Phase gate:** Full suite green before `/gsd:verify-work`

### Wave 0 Gaps
- [ ] `canvas/tests/tokens.test.ts` — covers RNDR-01 through RNDR-04
- [ ] `canvas/src/tokens/` directory — does not exist yet
- [ ] `canvas/src/tokens/build/build-tokens.mjs` — style-dictionary build script
- [ ] style-dictionary and culori install: `cd canvas && npm install --save-dev style-dictionary@4 culori`

---

## Sources

### Primary (HIGH confidence)
- [styledictionary.com/reference/config/](https://styledictionary.com/reference/config/) — style-dictionary v4 configuration format, platform definitions
- [styledictionary.com/versions/v4/migration/](https://styledictionary.com/versions/v4/migration/) — v3→v4 breaking changes, async API, hooks restructure
- [styledictionary.com/reference/api/](https://styledictionary.com/reference/api/) — v4/v5 programmatic API (confirmed current version is v5.3.3, v4 branch still maintained)
- [culorijs.org/](https://culorijs.org/) — culori library canonical docs; OKLCH support verified
- [evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl) — OKLCH vs HSL perceptual uniformity, design token applications
- [developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch) — OKLCH browser support (Chrome 111+, Firefox 113+, Safari 15.4+)
- `middle-math/weight-css-spec.md` — weight-to-CSS derivation spec, dimension indices, normalization formula
- `middle-math/design-tokens.json` — DRAFT structure reference (values discarded, shape referenced)
- `scl-deep/color-context-vernacular.md` — tonal names, Color character descriptions (source of truth for hue selection rationale)
- `canvas/src/types/scl.ts` — W enum positions (19-26 for Colors), confirms 1-indexed offset
- `canvas/tsconfig.json` — ESNext + ESM modules, confirms v4 ESM compatibility

### Secondary (MEDIUM confidence)
- [medium.com/@alexdev82/oklch-the-modern-css-color-space-you-should-be-using-in-2025](https://medium.com/@alexdev82/oklch-the-modern-css-color-space-you-should-be-using-in-2025) — OKLCH adoption in design systems, TailwindCSS v4 uses OKLCH
- [typewolf.com/google-fonts](https://www.typewolf.com/google-fonts) — curated Google Fonts guidance, Playfair Display and Spectral verified as engraving-aesthetic options

### Tertiary (LOW confidence)
- Base hue values in the code examples above — derived from Color Context Vernacular character descriptions combined with intaglio aesthetic research; these are first-pass values for iteration, not final

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — style-dictionary v4 and culori are verified current ecosystem standards
- Architecture: HIGH — patterns derived from official docs + existing project code (W enum, weight-css-spec.md)
- Pitfalls: HIGH — async init, out-of-gamut, and naming pitfalls verified from official migration docs
- Base hue values: LOW — initial estimates pending visual validation

**Research date:** 2026-03-14
**Valid until:** 2026-06-14 (style-dictionary and culori APIs are stable; OKLCH support is fixed)
