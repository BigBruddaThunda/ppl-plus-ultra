# Phase 5: Rendering Pipeline - Research

**Researched:** 2026-03-14
**Domain:** CSS custom property derivation from weight vectors; block container styling; pure function architecture
**Confidence:** HIGH

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| RNDR-05 | weightsToCSSVars() pure function deriving 30+ CSS custom properties from weight vector + design tokens | Full derivation architecture specified in weight-css-spec.md; all input types exist from Phases 2–4; W enum, tokens object, COLOR_W_TO_TONAL bridge all available |
| RNDR-06 | Block container styling for 22 blocks grouped by operational function (Orientation, Access, Transformation, Retention) | BLOCKS const in scl.ts carries role field for all 22 blocks; 4 operational groups: orientation (2), access (6), transformation (11), retention (3), modifier (1) |
| RNDR-07 | Color saturation derivation per Color temperament (⚫: 0.05 → 🔴: 0.90) | Saturation values are per-Color constants, not computed from weight vector; they are tonal properties of the Color identity; mapping table fully derivable from CLAUDE.md character descriptions |
| TEST-04 | Unit tests for CSS derivation (weight vector → expected CSS custom properties) | Vitest infrastructure in place; test file location: canvas/tests/rendering.test.ts; known zip 2123 (⛽🏛🪡🔵) provides concrete expected-value anchor |
</phase_requirements>

---

## Summary

Phase 5 builds the rendering pipeline on top of Phase 4's completed token infrastructure. Three artifacts are required: (1) `weightsToCSSVars()` — a pure TypeScript function that accepts a `Float32Array` weight vector and the `tokens` object, then returns a `Record<string, string>` of CSS custom property name/value pairs; (2) `blockContainerStyles` — a typed map of all 22 block slugs to their CSS class descriptors, grouped by the four operational functions already encoded in `BLOCKS` const; and (3) `rendering.test.ts` — a Vitest suite that validates the pipeline against the known zip code 2123 (⛽🏛🪡🔵, Strength/Basics/Pull/Structured).

The primary specification for this phase already exists in `middle-math/weight-css-spec.md`. This document defines the normalization formula `(weight + 8.0) / 16.0`, the dimension index map (0-indexed for the spec, 1-indexed in the W enum — bridge required), the per-group derivation logic, and a complete TypeScript reference implementation. Phase 5's job is to port this specification faithfully into `canvas/src/rendering/` using the token infrastructure and types that Phases 1–4 built.

The most important non-obvious constraint is the **index bridge**: `weight-css-spec.md` is 0-indexed (dimension 0 = Foundation through dimension 25 = Mindful) while the W enum in `scl.ts` is 1-indexed (W.FOUNDATION=1 through W.MINDFUL=26). The `resolveZip()` function returns a `Float32Array` of length 62 where position 0 is unused and positions 1–61 match W enum values. Every `vector[i]` access in `weightsToCSSVars()` must use the W enum constants (1-indexed), not the 0-indexed spec positions. The spec's `vector[0]` = W.FOUNDATION = `vector[1]` in practice.

**Primary recommendation:** Implement `weightsToCSSVars()` in `canvas/src/rendering/weights-to-css-vars.ts` as a single pure export. Use W enum constants for all vector index access. Use `COLOR_W_TO_TONAL` bridge from `tokens.ts` for dominant Color lookup. Implement block container styles as a typed constant object in `canvas/src/rendering/block-styles.ts`. Wire both into a test file before implementation using TDD.

---

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| TypeScript (project) | ^5.7.0 | Pure function implementation | Already in canvas/; strict mode enabled |
| Vitest | ^3.0.0 | Test suite for CSS derivation | Already in canvas/; existing test patterns established |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| (none new) | — | No new dependencies needed | All Phase 5 logic derives from existing canvas/ infrastructure |

Phase 5 requires zero new package installations. The rendering pipeline is a pure computation layer over data already present in canvas/src/.

**Installation:**
```bash
# No new packages. Verify existing canvas/ dependencies are installed:
cd canvas && npm install
```

---

## Architecture Patterns

### Recommended Project Structure
```
canvas/src/rendering/
├── weights-to-css-vars.ts   # weightsToCSSVars() pure function (RNDR-05)
├── block-styles.ts          # blockContainerStyles map — 22 blocks (RNDR-06)
├── saturation-map.ts        # COLOR_SATURATION constant (RNDR-07)
└── index.ts                 # Re-exports all rendering API
canvas/tests/
└── rendering.test.ts        # TEST-04 — CSS derivation tests
```

### Pattern 1: Pure Function with Token Injection

`weightsToCSSVars()` must be a pure function. This means:
- No module-level state reads
- No side effects
- Tokens passed as a parameter, not imported inside the function body
- Same inputs always produce same outputs

**What:** Accept `(vector: Float32Array, tokens: typeof import('../tokens/tokens').tokens)` and return `Record<string, string>`.

**When to use:** Every time a zip code must be rendered — the output is applied to a CSS root element.

**Example (correct pattern):**
```typescript
// Source: middle-math/weight-css-spec.md + canvas/src/types/scl.ts W enum
import { W } from '../types/scl.js';
import type { tokens as TokensType } from '../tokens/tokens.js';
import { COLOR_W_TO_TONAL } from '../tokens/tokens.js';

export function weightsToCSSVars(
  vector: Float32Array,
  tokens: typeof TokensType
): Record<string, string> {
  const props: Record<string, string> = {};
  // ... derive all CSS custom properties
  return props;
}
```

### Pattern 2: W Enum Index Bridge

The spec document `weight-css-spec.md` uses 0-indexed dimension positions (matching the conceptual layout). The W enum and `resolveZip()` output are 1-indexed. The bridge is:

```
spec_index = W_constant - 1
vector[W.FOUNDATION] = vector[1]   // spec index 0
vector[W.STRENGTH]   = vector[2]   // spec index 1
...
vector[W.INTENSE]    = vector[23]  // spec index 22 (Color dim 4 in spec)
vector[W.MINDFUL]    = vector[26]  // spec index 25 (Color dim 7 in spec)
```

**Rule for implementation:** Always use `vector[W.CONSTANT]` — never use bare integer indices. The W enum is the authoritative dimension key.

**Dominant dimension helper (0-indexed in spec → 1-indexed in W enum):**
```typescript
// Source: middle-math/weight-css-spec.md dominantDim pattern
function dominantDim(vector: Float32Array, wStart: number, wEnd: number): number {
  let maxIdx = wStart;
  let maxVal = vector[wStart];
  for (let i = wStart + 1; i <= wEnd; i++) {
    if (vector[i] > maxVal) { maxVal = vector[i]; maxIdx = i; }
  }
  return maxIdx; // returns the W enum position (1-indexed)
}
```

Call sites:
```typescript
const dominantOrderW  = dominantDim(vector, W.FOUNDATION, W.RESTORATION); // 1–7
const dominantAxisW   = dominantDim(vector, W.BASICS, W.PARTNER);         // 8–13
const dominantColorW  = dominantDim(vector, W.TEACHING, W.MINDFUL);       // 19–26
```

### Pattern 3: Token Lookup from Dominant Dial

Phase 4 established the `COLOR_W_TO_TONAL` bridge. Phase 5 must use it:

```typescript
// Source: canvas/src/tokens/tokens.ts COLOR_W_TO_TONAL
import { COLOR_W_TO_TONAL, tokens } from '../tokens/tokens.js';

const dominantColorW = dominantDim(vector, W.TEACHING, W.MINDFUL);
const tonalName = COLOR_W_TO_TONAL[dominantColorW];   // e.g. 'planning'
const colorTokens = tokens.colors[tonalName];          // full palette object

props['--ppl-theme-primary']    = colorTokens.primary;
props['--ppl-theme-background'] = colorTokens.background;
// ... etc
```

Similarly for Order:
```typescript
const ORDER_W_TO_SLUG: Record<number, string> = {
  [W.FOUNDATION]:  'foundation',
  [W.STRENGTH]:    'strength',
  [W.HYPERTROPHY]: 'hypertrophy',
  [W.PERFORMANCE]: 'performance',
  [W.FULL_BODY]:   'full-body',
  [W.BALANCE]:     'balance',
  [W.RESTORATION]: 'restoration',
};

const dominantOrderW = dominantDim(vector, W.FOUNDATION, W.RESTORATION);
const orderSlug = ORDER_W_TO_SLUG[dominantOrderW];
const orderTokens = tokens.orders[orderSlug];

props['--ppl-weight-font-weight']        = String(orderTokens.fontWeight);
props['--ppl-weight-lineheight']         = String(orderTokens.lineHeight);
props['--ppl-weight-spacing-multiplier'] = String(orderTokens.spacingMultiplier);
props['--ppl-weight-letter-spacing']     = orderTokens.letterSpacing;
```

### Pattern 4: Saturation Derivation (RNDR-07)

Saturation is a **per-Color constant**, not derived from the weight formula. Each Color has a fixed temperament-based saturation level. The derivation is: look up the dominant Color's saturation from a constant table.

```typescript
// Source: CLAUDE.md Color character descriptions + weight-css-spec.md saturation mapping
const COLOR_SATURATION: Record<number, number> = {
  [W.TEACHING]:   0.05,  // ⚫ Order — desaturated, focus on content
  [W.BODYWEIGHT]: 0.40,  // 🟢 Growth — natural, present but not vivid
  [W.STRUCTURED]: 0.50,  // 🔵 Planning — neutral, clean, trackable
  [W.TECHNICAL]:  0.65,  // 🟣 Magnificence — precise, quality-focused
  [W.INTENSE]:    0.90,  // 🔴 Passion — maximum effort, vivid
  [W.CIRCUIT]:    0.70,  // 🟠 Connection — station energy, engaged
  [W.FUN]:        0.75,  // 🟡 Play — bright, exploratory
  [W.MINDFUL]:    0.10,  // ⚪ Eudaimonia — near-monochrome, calm
};

props['--ppl-weight-saturation'] = COLOR_SATURATION[dominantColorW].toFixed(2);
```

**Why a constant, not a formula:** The saturation mapping is derived from Color *character* (tonal identity), not from how strongly the Color dimension scores in the weight vector. A zip that heavily activates 🔴 Intense is just as saturated as one that barely activates it — because the Color itself is the saturation instruction. The weight vector tells you WHICH Color is active; the constant table tells you WHAT that Color's saturation is.

### Pattern 5: Block Container Styles (RNDR-06)

Block container styles are grouped by the `role` property already present on every `BlockEntry` in `BLOCKS`. No new categorization needed — iterate BLOCKS and group by role.

```typescript
// Source: canvas/src/types/scl.ts BLOCKS const
import { BLOCKS } from '../types/scl.js';

type BlockRole = 'orientation' | 'access' | 'transformation' | 'retention' | 'modifier';

interface BlockContainerStyle {
  role: BlockRole;
  cssClass: string;
  borderAccent: string;   // CSS color token reference
  paddingMultiplier: number;
  emphasisLevel: 'low' | 'medium' | 'high';
}

export const BLOCK_CONTAINER_STYLES: Record<string, BlockContainerStyle> = {
  // Orientation blocks — framing, arriving, pointing intent
  'warm-up':    { role: 'orientation', cssClass: 'ppl-block--orientation', borderAccent: 'var(--ppl-theme-accent)', paddingMultiplier: 1.0, emphasisLevel: 'low' },
  'intention':  { role: 'orientation', cssClass: 'ppl-block--orientation', borderAccent: 'var(--ppl-theme-accent)', paddingMultiplier: 1.0, emphasisLevel: 'medium' },
  // Access blocks — mobility, activation, priming
  'fundamentals': { role: 'access', cssClass: 'ppl-block--access', borderAccent: 'var(--ppl-theme-secondary)', paddingMultiplier: 0.9, emphasisLevel: 'low' },
  // ... all 22 blocks
};
```

The 22 blocks by role (from `BLOCKS` in `scl.ts`):
- **orientation** (2): warm-up, intention
- **access** (6): fundamentals, circulation, primer, gambit, progression, (no 6th — see note below)
- **transformation** (11): bread-butter, composition, exposure, aram, gutter, vanity, sculpt, craft, supplemental, sandbox, reformance
- **retention** (3): release, imprint, junction
- **modifier** (1): choice

Note: Checking `scl.ts` BLOCKS carefully — role counts from the file:
- orientation: warm-up, intention → 2
- access: fundamentals, circulation, primer, gambit, progression → 5 (not 6)
- transformation: bread-butter, composition, exposure, aram, gutter, vanity, sculpt, craft, supplemental, sandbox, reformance → 11
- retention: release, imprint, junction → 3
- modifier: choice → 1
- Total: 2+5+11+3+1 = 22 ✓

### Pattern 6: CSS Property Count — Meeting the 30+ Requirement

RNDR-05 requires 30+ CSS custom properties. Inventory from weight-css-spec.md groups:

| Group | Properties | Count |
|-------|-----------|-------|
| Order — structural | --ppl-weight-density, --ppl-weight-lineheight, --ppl-weight-font-weight, --ppl-weight-letter-spacing, --ppl-weight-spacing-multiplier | 5 |
| Axis — typography character | --ppl-weight-typography-bias, --ppl-weight-visual-rhythm | 2 |
| Type — content emphasis | --ppl-weight-emphasis-push, -pull, -legs, -plus, -ultra | 5 |
| Color — theme palette (from tokens) | --ppl-theme-primary, --ppl-theme-secondary, --ppl-theme-background, --ppl-theme-surface, --ppl-theme-text, --ppl-theme-accent, --ppl-theme-border | 7 |
| Color — tonal meta | --ppl-weight-saturation, --ppl-weight-contrast | 2 |
| Axis — directional (from tokens) | --ppl-weight-gradient-direction, --ppl-weight-layout-flow, --ppl-weight-typography-family | 3 |
| Derived dims — structural | --ppl-weight-rest-emphasis, --ppl-weight-rep-display, --ppl-weight-block-spacing, --ppl-weight-cue-density | 4 |
| Order — additional structural (from tokens) | --ppl-weight-density-descriptor, --ppl-weight-font-weight-display | 2 |

**Total: 30** — exactly meets the floor. Adding the Axis typography-bias descriptor string and block-level tonal Color (active tonal name) pushes the count over 30 with room to spare.

### Anti-Patterns to Avoid

- **Bare integer vector indices:** `vector[22]` is wrong. Use `vector[W.INTENSE]`. The W enum is the spec.
- **Accessing tokens.colors by W number:** `tokens.colors[23]` will be undefined. Use `COLOR_W_TO_TONAL[23]` → `'passion'` → `tokens.colors['passion']`.
- **Hardcoding Color saturation:** The saturation spec (`⚫: 0.05, 🔴: 0.90`) is a constant per Color identity, not derived from the weight value.
- **Mutating the vector:** `weightsToCSSVars()` must never modify its `Float32Array` input. It is read-only.
- **Side effects inside the function:** No `document.documentElement.style.setProperty()` inside `weightsToCSSVars()`. The function returns a plain object. Callers apply the CSS.
- **Using spec 0-indexed positions directly:** `weight-css-spec.md` shows `vector[0]` through `vector[25]` for dials. In code, these are `vector[W.FOUNDATION]` through `vector[W.MINDFUL]`.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Dominant dimension finding | Custom max-loop | dominantDim helper (pattern from weight-css-spec.md) | Already specified; trivial 5-line function |
| Color name resolution from W position | Custom mapping object | `COLOR_W_TO_TONAL` from tokens.ts | Already built in Phase 4; use the authoritative bridge |
| Order name resolution from W position | Ad-hoc string switch | `ORDER_W_TO_SLUG` constant (6-entry record) | Mirror pattern of COLOR_W_TO_TONAL; define once in rendering module |
| Linear interpolation | Inline math everywhere | `lerp(min, max, t)` helper | Named function makes derivation intent readable |
| Normalization | Inline `(w + 8) / 16` everywhere | `normalize(weight)` helper | Testable; mirrors spec notation |
| Block role grouping | New categorization system | Iterate `BLOCKS` from scl.ts, group by `.role` | Role is already on every BlockEntry; no new data |

**Key insight:** Phase 5 is almost entirely an integration problem — mapping existing typed data through a specified algorithm. The temptation to add complexity (blended states, Order/Color interaction multipliers, derived dimension CSS) should be resisted until the clean single-dial derivation works end-to-end and passes TEST-04.

---

## Common Pitfalls

### Pitfall 1: The Index Bridge (0-indexed spec vs 1-indexed W enum)
**What goes wrong:** `vector[0]` is always unused in the resolver output (Float32Array of length 62, positions 1–61 are valid). Writing `vector[orderDim - 1]` instead of `vector[orderDim]` silently shifts the entire Order group by one position.
**Why it happens:** `weight-css-spec.md` describes the dimension map starting from index 0 (conceptual layout matching the 61-element logical space), while `resolveZip()` returns a 62-element Float32Array with position 0 empty.
**How to avoid:** Always reference dimensions via W enum constants. Never subtract 1 from a W constant. Never add 1 to a W constant. The W enum *is* the vector index.
**Warning signs:** Tests fail for exactly one Order; STRENGTH produces FOUNDATION values; MINDFUL produces CIRCUIT values.

### Pitfall 2: Saturation Treated as Weight-Derived
**What goes wrong:** Implementing `saturation = normalize(vector[W.INTENSE])` instead of using the constant table. For zip 2123 (Structured/🔵), the STRUCTURED dimension scores at +8 but saturation should be 0.50 (planning character), not 1.0 (weight-derived).
**Why it happens:** The weight-css-spec.md shows a "Color × Order interaction" saturation table that looks formula-driven. The specified values are actually per-Color constants — the Order mention describes which Order that Color pairs with to produce that saturation level, not a multiplication.
**How to avoid:** Implement `COLOR_SATURATION` as a static lookup keyed by W enum position. The test for zip 2123 must verify `--ppl-weight-saturation: 0.50`.
**Warning signs:** TEACHING saturation > 0.1; INTENSE saturation < 0.8.

### Pitfall 3: Non-pure weightsToCSSVars
**What goes wrong:** Importing `tokens` at module scope and closing over it inside `weightsToCSSVars()` instead of receiving it as a parameter.
**Why it happens:** Feels simpler and tokens is a static object anyway. But it breaks the pure function contract — the function can no longer be unit-tested with mock tokens.
**How to avoid:** `tokens` is a required parameter. The test passes a known token subset. Callers in production import and pass `tokens` from `tokens.ts`.
**Warning signs:** Cannot test with custom token values; RNDR-05 success criterion ("no side effects") is not verifiable.

### Pitfall 4: Block Styles as a Render Decision Instead of a Static Map
**What goes wrong:** Generating block styles dynamically per zip code (applying Color palette to each block container).
**Why it happens:** The phase description says "block container styles" and the system is CSS-variable driven — it's tempting to make blocks react to the weight vector.
**How to avoid:** RNDR-06 asks for *grouped container styles* — a static mapping of all 22 block slugs to CSS class metadata. Dynamic theming already happens through `--ppl-theme-*` variables set by `weightsToCSSVars()`. Block styles describe the structural/functional character of each block container (padding, border treatment, emphasis level) not the color theme.
**Warning signs:** `blockContainerStyles` accepts a vector parameter; different zips produce different block style objects.

### Pitfall 5: Properties Missing the 30+ Count
**What goes wrong:** Implementing only the 7 color theme properties + 5 Order properties = 12, missing the requirement.
**Why it happens:** The "theme" group is obvious; the derived-dim group (rest-emphasis, rep-display, block-spacing, cue-density) and Axis directional group are easy to forget.
**How to avoid:** Build the property inventory table (Pattern 6 above) before coding. Tests should count keys in the returned object: `expect(Object.keys(result).length).toBeGreaterThanOrEqual(30)`.
**Warning signs:** TEST-04 property count assertion fails.

---

## Code Examples

Verified patterns from official sources (weight-css-spec.md + existing canvas/ code):

### Complete weightsToCSSVars skeleton
```typescript
// Source: middle-math/weight-css-spec.md § CSS Custom Property Generation
// Adapted for W enum (1-indexed) from spec (0-indexed)
import { W } from '../types/scl.js';
import { tokens as DesignTokens, COLOR_W_TO_TONAL } from '../tokens/tokens.js';

function normalize(weight: number): number {
  return (weight + 8.0) / 16.0;
}

function dominantDim(vector: Float32Array, wStart: number, wEnd: number): number {
  let maxIdx = wStart;
  let maxVal = vector[wStart];
  for (let i = wStart + 1; i <= wEnd; i++) {
    if (vector[i] > maxVal) { maxVal = vector[i]; maxIdx = i; }
  }
  return maxIdx;
}

function lerp(min: number, max: number, t: number): number {
  return min + (max - min) * t;
}

export function weightsToCSSVars(
  vector: Float32Array,
  tokens: typeof DesignTokens
): Record<string, string> {
  const props: Record<string, string> = {};

  // --- Order group (W.FOUNDATION=1 .. W.RESTORATION=7) ---
  const orderW = dominantDim(vector, W.FOUNDATION, W.RESTORATION);
  const orderSlug = ORDER_W_TO_SLUG[orderW];
  const orderTokens = tokens.orders[orderSlug as keyof typeof tokens.orders];

  props['--ppl-weight-font-weight']        = String(orderTokens.fontWeight);
  props['--ppl-weight-font-weight-display'] = String(orderTokens.fontWeightDisplay);
  props['--ppl-weight-lineheight']         = String(orderTokens.lineHeight);
  props['--ppl-weight-spacing-multiplier'] = String(orderTokens.spacingMultiplier);
  props['--ppl-weight-letter-spacing']     = orderTokens.letterSpacing;
  props['--ppl-weight-density']            = orderTokens.density;

  // --- Color group (W.TEACHING=19 .. W.MINDFUL=26) ---
  const colorW = dominantDim(vector, W.TEACHING, W.MINDFUL);
  const tonalName = COLOR_W_TO_TONAL[colorW];
  const colorTokens = tokens.colors[tonalName];

  props['--ppl-theme-primary']    = colorTokens.primary;
  props['--ppl-theme-secondary']  = colorTokens.secondary;
  props['--ppl-theme-background'] = colorTokens.background;
  props['--ppl-theme-surface']    = colorTokens.surface;
  props['--ppl-theme-text']       = colorTokens.text;
  props['--ppl-theme-accent']     = colorTokens.accent;
  props['--ppl-theme-border']     = colorTokens.border;
  props['--ppl-weight-saturation'] = COLOR_SATURATION[colorW].toFixed(2);

  // --- Axis group (W.BASICS=8 .. W.PARTNER=13) ---
  const axisW = dominantDim(vector, W.BASICS, W.PARTNER);
  const axisSlug = AXIS_W_TO_SLUG[axisW];
  const axisTokens = tokens.axes[axisSlug as keyof typeof tokens.axes];

  props['--ppl-weight-gradient-direction'] = axisTokens.gradientDirection;
  props['--ppl-weight-layout-flow']        = axisTokens.layoutFlow;
  props['--ppl-weight-typography-bias']    = axisTokens.typographyBias;

  // --- Type group (W.PUSH=14 .. W.ULTRA=18): content emphasis ---
  const TYPE_NAMES = ['push', 'pull', 'legs', 'plus', 'ultra'] as const;
  const TYPE_W_START = W.PUSH; // 14
  for (let i = 0; i < 5; i++) {
    props[`--ppl-weight-emphasis-${TYPE_NAMES[i]}`] = normalize(vector[TYPE_W_START + i]).toFixed(3);
  }

  // --- Derived dims (W.CAPIO=27 .. W.SAVE=61): structural modifiers ---
  // Operator cluster (27–38): rep display prominence
  const repSlice = Array.from({ length: 12 }, (_, i) => vector[27 + i]);
  const repMean = repSlice.reduce((a, b) => a + b, 0) / 12;
  props['--ppl-weight-rep-display'] = normalize(repMean).toFixed(3);

  // Block cluster (39–60): block spacing
  const blockSlice = Array.from({ length: 22 }, (_, i) => vector[39 + i]);
  const blockMean = blockSlice.reduce((a, b) => a + b, 0) / 22;
  props['--ppl-weight-block-spacing'] = normalize(blockMean).toFixed(3);
  props['--ppl-weight-cue-density']   = normalize(blockMean).toFixed(3);

  // Rest emphasis: derived from Order character (airy Orders show rest prominently)
  const orderNorm = normalize(vector[orderW]);
  props['--ppl-weight-rest-emphasis'] = lerp(0.3, 0.9, orderNorm).toFixed(3);

  return props;
}
```

### Known zip 2123 expected values (anchor for TEST-04)
```
Zip: 2123 = ⛽ Strength (order 2) / 🏛 Basics (axis 1) / 🪡 Pull (type 2) / 🔵 Structured (color 3)

Expected weightsToCSSVars output (key properties):
--ppl-weight-font-weight:        800   (tokens.orders.strength.fontWeight)
--ppl-weight-lineheight:         1.4   (tokens.orders.strength.lineHeight)
--ppl-weight-spacing-multiplier: 0.85  (tokens.orders.strength.spacingMultiplier)
--ppl-theme-primary:             oklch(0.4 0.10496... 230)  (tokens.colors.planning.primary)
--ppl-weight-saturation:         0.50  (COLOR_SATURATION[W.STRUCTURED])
--ppl-weight-gradient-direction: to bottom  (tokens.axes.basics.gradientDirection)
--ppl-weight-layout-flow:        column    (tokens.axes.basics.layoutFlow)
--ppl-weight-typography-bias:    classical  (tokens.axes.basics.typographyBias)
--ppl-weight-emphasis-pull:      (normalize of vector[W.PULL] for 2123 — high, near 1.0)
--ppl-weight-emphasis-push:      (normalize of vector[W.PUSH] for 2123 — suppressed, near 0)
```

Compute the exact expected values by calling `resolveZip(2, 1, 2, 3)` from `canvas/src/weights/resolver.ts` during test setup.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Separate style config per zip | weight vector = visual instruction | weight-css-spec.md (2026-03-06) | No per-zip style management; deterministic |
| HSL color values | OKLCH color values | Phase 4 (2026-03-14) | Perceptually uniform; gamut-safe |
| style-dictionary for all token output | Direct CSS/TS generation for double-hyphen naming | Phase 4 plan 02 | Full control of `--ppl-color-passion--primary` naming pattern |
| Saturation from weight formula | Saturation as per-Color constant | weight-css-spec.md § Group 4 | Reflects Color temperament, not numeric weight score |

**Deprecated/outdated:**
- `--ppl-theme-*` prefix in spec doc: weight-css-spec.md uses `--ppl-theme-primary` for the 7 color values; this is correct and intentional (not `--ppl-color-passion--primary` — those are the full token catalog; `--ppl-theme-*` are the active-zip resolved vars)
- `weight-css-spec.md § Applying Properties in Next.js`: ignore Next.js-specific TSX code — canvas/ is not Next.js; the core `generateWeightCSS` function logic is what matters
- 0-indexed positions in spec: all spec pseudocode uses 0-indexed arrays; canvas/ uses 1-indexed W enum; always translate via W constants

---

## Open Questions

1. **Derived dimensions 27–61 (operators and blocks) — spec vs. actual populated values**
   - What we know: weight-css-spec.md specifies "derived cluster" at indices 26–60 for block/temporal/operator data, split into three sub-clusters
   - What's unclear: `resolveZip()` returns a 62-element Float32Array but only positions 1–26 are populated by `computeRawVector()` (dial dimensions only). Positions 27–61 may be zeros.
   - Recommendation: Verify by calling `resolveZip(2, 1, 2, 3)` and logging positions 27–61. If all zero, the derived-dim CSS properties (`--ppl-weight-rep-display`, etc.) will always normalize to 0.5 (neutral). This is acceptable for Phase 5 — spec the behavior and document that derived-dim CSS requires block/operator table population (Phase 8+). Do not block Phase 5 on this.

2. **`fontFamily` from Axis tokens — not in current design-tokens.json**
   - What we know: CSS arbitration spec assigns `fontFamily` to Axis; `design-tokens.json` has `typographyBias` (a descriptor string) but not a `fontFamily` value
   - What's unclear: Phase 4 deferred actual font selection; `typographyBias` is a semantic descriptor, not a CSS font-family value
   - Recommendation: Emit `--ppl-weight-typography-bias` (the descriptor string) not `--ppl-weight-font-family`. Leave the font-family CSS property for Phase 8 card templates to map the descriptor to an actual web font. Do not block Phase 5.

3. **`--ppl-weight-contrast` property — WCAG accessibility floor**
   - What we know: weight-css-spec.md specifies a contrast property with WCAG AA floor (4.5:1 minimum)
   - What's unclear: Computing a contrast ratio from a single normalized saturation score is not directly related to WCAG contrast (which compares two specific colors). The spec value may be a UI emphasis signal, not a literal contrast ratio.
   - Recommendation: Emit `--ppl-weight-contrast` as `colorNorm.toFixed(3)` (normalized dominant color weight) with the understanding that the rendering layer maps it to actual luminance differential in Phase 8. Document the limitation in the function's JSDoc.

---

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Vitest ^3.0.0 |
| Config file | canvas/vite.config.ts (implicit) or vitest config in package.json |
| Quick run command | `cd canvas && npm test -- --testPathPattern rendering` |
| Full suite command | `cd canvas && npm test` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| RNDR-05 | weightsToCSSVars() returns Record<string, string> with 30+ keys | unit | `cd canvas && npm test -- --testPathPattern rendering` | ❌ Wave 0 |
| RNDR-05 | Same WeightVector + same tokens → same output (pure function property) | unit | same | ❌ Wave 0 |
| RNDR-05 | zip 2123 produces expected CSS property values (font-weight, saturation, theme colors) | unit | same | ❌ Wave 0 |
| RNDR-06 | blockContainerStyles has exactly 22 entries | unit | same | ❌ Wave 0 |
| RNDR-06 | All 4 operational roles are represented (orientation, access, transformation, retention) | unit | same | ❌ Wave 0 |
| RNDR-06 | Each block slug from BLOCKS const is present in blockContainerStyles | unit | same | ❌ Wave 0 |
| RNDR-07 | ⚫ Teaching zip produces saturation ≤ 0.10 | unit | same | ❌ Wave 0 |
| RNDR-07 | 🔴 Intense zip produces saturation ≥ 0.85 | unit | same | ❌ Wave 0 |
| RNDR-07 | All 8 Color saturation values are in range [0.0, 1.0] | unit | same | ❌ Wave 0 |
| TEST-04 | CSS derivation test file exists and all tests pass | unit | `cd canvas && npm test` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `cd canvas && npm test -- --testPathPattern rendering`
- **Per wave merge:** `cd canvas && npm test`
- **Phase gate:** Full suite green (`cd canvas && npm test`) before `/gsd:verify-work`

### Wave 0 Gaps
- [ ] `canvas/tests/rendering.test.ts` — covers RNDR-05, RNDR-06, RNDR-07, TEST-04
- [ ] `canvas/src/rendering/index.ts` — re-exports for rendering module
- [ ] `canvas/src/rendering/weights-to-css-vars.ts` — the primary Phase 5 artifact
- [ ] `canvas/src/rendering/block-styles.ts` — 22-block container style map
- [ ] `canvas/src/rendering/saturation-map.ts` — COLOR_SATURATION constant

No new framework install needed — Vitest ^3.0.0 is already a devDependency.

---

## Sources

### Primary (HIGH confidence)
- `middle-math/weight-css-spec.md` — complete CSS derivation spec, normalization formula, TypeScript reference implementation, all 5 property groups
- `canvas/src/types/scl.ts` — W enum (authoritative 1-indexed vector positions), BLOCKS const (22 blocks with role field), all SCL primitives
- `canvas/src/tokens/tokens.ts` — `tokens` object shape, `COLOR_W_TO_TONAL` bridge table (W positions 19–26 → tonal names)
- `canvas/src/tokens/design-tokens.json` — authoritative token values (OKLCH colors, Order typography, Axis direction)
- `.planning/phases/04-design-tokens/04-CSS-ARBITRATION.md` — property ownership spec, naming conventions, W enum bridge table
- `canvas/src/weights/resolver.ts` — `resolveZip()` and `resolveVector()` API; output is Float32Array of length 62 (position 0 unused)

### Secondary (MEDIUM confidence)
- `canvas/tests/tokens.test.ts` — existing test patterns for Vitest in this codebase; file/import path conventions verified
- `canvas/src/weights/types.ts` — `WeightEntry`, `DialWeightTable` shapes; confirms weight scale is -8 to +8

### Tertiary (LOW confidence)
- Color saturation values (0.05 for ⚫ Teaching, 0.90 for 🔴 Intense) come from `weight-css-spec.md § Group 4` examples; intermediate values (🟢 0.40, 🔵 0.50, etc.) are extrapolated from CLAUDE.md character descriptions and not explicitly stated in any single spec document. These values are reasonable starting points but may need calibration after visual testing.

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — no new dependencies; all infrastructure in place from Phases 1–4
- Architecture: HIGH — complete derivation spec exists in weight-css-spec.md; exact function signatures derivable from existing types
- Pitfalls: HIGH — W enum index bridge is a verified concrete trap (0-indexed spec vs 1-indexed W enum); saturation-as-constant is explicitly stated in spec
- Block styling: HIGH — BLOCKS const with role field already exists; grouping logic is mechanical
- Saturation intermediate values: MEDIUM — ⚫ Teaching (0.05) and 🔴 Intense (0.90) are spec-stated; intermediate values extrapolated from character descriptions

**Research date:** 2026-03-14
**Valid until:** 2026-06-14 (stable — no external library dependencies; all sources are first-party project documents)
