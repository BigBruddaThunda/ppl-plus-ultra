/**
 * weights-to-css-vars.ts — Weight vector → CSS custom properties
 *
 * RNDR-05: The bridge between the weight engine (Phases 1–3) and the visual
 * experience. A resolved weight vector + design tokens go in; 30+ CSS custom
 * properties come out.
 *
 * weightsToCSSVars() is a PURE FUNCTION:
 *   - No module-level state reads
 *   - No side effects
 *   - tokens is a parameter, not imported inside the function body
 *   - Same inputs always produce the same outputs
 *   - Never mutates the input Float32Array
 *
 * Index convention: vector positions use W enum constants (1-indexed).
 * The W enum IS the authoritative vector index. Never use bare integers.
 * weight-css-spec.md is 0-indexed (conceptual layout); canvas/ is 1-indexed.
 *
 * Derived dimensions (W.CAPIO=27 .. W.SAVE=61): These positions are zero in the
 * current resolver output — computeRawVector() populates dial positions 1–26 only.
 * normalize(0) = 0.5 (neutral midpoint). Derived-dim CSS properties will be 0.500
 * until block/operator table population is implemented (Phase 8+). This is correct
 * and expected behavior. Documented here so callers are not surprised.
 */

import { W } from '../types/scl.js';
import { COLOR_W_TO_TONAL } from '../tokens/tokens.js';
import type { tokens as DesignTokens } from '../tokens/tokens.js';
import { COLOR_SATURATION } from './saturation-map.js';

// ---------------------------------------------------------------------------
// Bridge tables — Order and Axis W positions → token slug
// ---------------------------------------------------------------------------

/**
 * ORDER_W_TO_SLUG maps Order W enum positions (1–7) to token slugs used in
 * tokens.orders. Mirrors COLOR_W_TO_TONAL pattern from tokens.ts.
 */
export const ORDER_W_TO_SLUG: Record<number, string> = {
  [W.FOUNDATION]:  'foundation',
  [W.STRENGTH]:    'strength',
  [W.HYPERTROPHY]: 'hypertrophy',
  [W.PERFORMANCE]: 'performance',
  [W.FULL_BODY]:   'full-body',
  [W.BALANCE]:     'balance',
  [W.RESTORATION]: 'restoration',
} as const;

/**
 * AXIS_W_TO_SLUG maps Axis W enum positions (8–13) to token slugs used in
 * tokens.axes. Mirrors ORDER_W_TO_SLUG pattern.
 */
export const AXIS_W_TO_SLUG: Record<number, string> = {
  [W.BASICS]:     'basics',
  [W.FUNCTIONAL]: 'functional',
  [W.AESTHETIC]:  'aesthetic',
  [W.CHALLENGE]:  'challenge',
  [W.TIME]:       'time',
  [W.PARTNER]:    'partner',
} as const;

// ---------------------------------------------------------------------------
// Internal helpers
// ---------------------------------------------------------------------------

/**
 * vget — type-safe Float32Array element access.
 * noUncheckedIndexedAccess makes Float32Array[n] return number|undefined.
 * The W enum constants are compile-time valid indices (1-61) for a 62-slot vector,
 * so runtime access is always defined. This helper encodes that invariant.
 */
function vget(vector: Float32Array, index: number): number {
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  return vector[index]!;
}

/**
 * normalize — maps the [-8, +8] weight scale to [0.0, 1.0].
 * Source: weight-css-spec.md normalization formula.
 * normalize(0) = 0.5 (neutral midpoint — used for unpopulated derived dims)
 */
function normalize(weight: number): number {
  return (weight + 8.0) / 16.0;
}

/**
 * dominantDim — finds the W enum position with the highest value in [wStart, wEnd].
 * Returns the W enum position (1-indexed), not an array index.
 * Tie-breaking: returns the lowest index (first-wins).
 */
function dominantDim(vector: Float32Array, wStart: number, wEnd: number): number {
  let maxIdx = wStart;
  let maxVal = vget(vector, wStart);
  for (let i = wStart + 1; i <= wEnd; i++) {
    const val = vget(vector, i);
    if (val > maxVal) {
      maxVal = val;
      maxIdx = i;
    }
  }
  return maxIdx;
}

/**
 * detectDominantColorW — finds the active Color W position from the resolved vector.
 *
 * Cross-dial affinities can elevate non-active Color W positions to the same clamped
 * value (+8) as the active Color's self value. Generic argmax (first-wins) fails when
 * a lower-index Color (e.g. W.STRUCTURED=21) has equal cross-dial affinity accumulation
 * to the actual active Color (e.g. W.INTENSE=23).
 *
 * Resolution strategy:
 * 1. Find max value in Color range (W.TEACHING..W.MINDFUL, positions 19-26)
 * 2. If unique winner, return it
 * 3. If tied, use hard-suppression signatures in the Color range as tiebreakers:
 *    - Intense Color hard-suppresses Mindful (W.MINDFUL <= -6 → Intense is active)
 *    - Mindful Color hard-suppresses Intense (W.INTENSE <= -6 → Mindful is active)
 * 4. Default: first-wins (lowest index) for remaining ties
 *
 * This handles the known edge cases while preserving existing behavior for
 * zip 2123 (Structured) and all Teaching-type zips.
 */
function detectDominantColorW(vector: Float32Array): number {
  // Phase 1: find max value in Color range
  let maxVal = vget(vector, W.TEACHING);
  for (let cw = W.BODYWEIGHT; cw <= W.MINDFUL; cw++) {
    const val = vget(vector, cw);
    if (val > maxVal) maxVal = val;
  }

  // Phase 2: collect all candidates tied at max
  const candidates: number[] = [];
  for (let cw = W.TEACHING; cw <= W.MINDFUL; cw++) {
    if (vget(vector, cw) === maxVal) candidates.push(cw);
  }

  // Phase 3: unique winner — return immediately
  if (candidates.length === 1) {
    // candidates[0] is always defined here (length === 1 guard)
    return candidates[0] as number;
  }

  // Phase 4: tie-breaking via hard-suppression signatures in the Color range
  // Intense (W=23) is the ONLY Color that hard-suppresses W.MINDFUL at -6
  if (candidates.includes(W.INTENSE) && vget(vector, W.MINDFUL) <= -6) return W.INTENSE;
  // Mindful (W=26) is the ONLY Color that hard-suppresses W.INTENSE at -6
  if (candidates.includes(W.MINDFUL) && vget(vector, W.INTENSE) <= -6) return W.MINDFUL;

  // Phase 5: default — first-wins (lowest index)
  // candidates is non-empty (we always have W.TEACHING..W.MINDFUL = 8 entries)
  return candidates[0] as number;
}

/**
 * lerp — linear interpolation between min and max at position t ∈ [0, 1].
 */
function lerp(min: number, max: number, t: number): number {
  return min + (max - min) * t;
}

// ---------------------------------------------------------------------------
// weightsToCSSVars — main export
// ---------------------------------------------------------------------------

/**
 * weightsToCSSVars converts a resolved weight vector + design tokens into
 * a Record<string, string> of CSS custom property name/value pairs.
 *
 * Returns 30+ properties covering:
 *   - Order group: font-weight, font-weight-display, lineheight, spacing-multiplier,
 *                  letter-spacing, density, density-descriptor (7)
 *   - Color theme: primary, secondary, background, surface, text, accent, border (7)
 *   - Color tonal meta: saturation, contrast, tonal-name (3)
 *   - Axis directional: gradient-direction, layout-flow, typography-bias (3)
 *   - Axis structural: visual-rhythm (1)
 *   - Type emphasis: push, pull, legs, plus, ultra (5)
 *   - Derived dims: rep-display, block-spacing, cue-density, rest-emphasis (4)
 * Total: 7+7+3+3+1+5+4 = 30 minimum
 *
 * @param vector - Float32Array of length 62 from resolveZip() (position 0 unused)
 * @param tokens - Design token object (passed as parameter for pure function purity)
 * @returns Record<string, string> of CSS custom property name → value pairs
 */
export function weightsToCSSVars(
  vector: Float32Array,
  tokens: typeof DesignTokens
): Record<string, string> {
  const props: Record<string, string> = {};

  // ─── Order group (W.FOUNDATION=1 .. W.RESTORATION=7) ────────────────────
  const orderW = dominantDim(vector, W.FOUNDATION, W.RESTORATION);
  // ORDER_W_TO_SLUG is keyed by all valid Order W positions (1-7) — always defined
  const orderSlug = ORDER_W_TO_SLUG[orderW] as string;
  const orderTokens = tokens.orders[orderSlug as keyof typeof tokens.orders];

  props['--ppl-weight-font-weight']          = String(orderTokens.fontWeight);
  props['--ppl-weight-font-weight-display']  = String(orderTokens.fontWeightDisplay);
  props['--ppl-weight-lineheight']           = String(orderTokens.lineHeight);
  props['--ppl-weight-spacing-multiplier']   = String(orderTokens.spacingMultiplier);
  props['--ppl-weight-letter-spacing']       = orderTokens.letterSpacing;
  props['--ppl-weight-density']              = orderTokens.density;
  // Density descriptor: semantic alias for density — provides string descriptor to CSS consumers
  // that prefer the full --ppl-weight-density-descriptor key over the shorthand density key.
  props['--ppl-weight-density-descriptor']   = orderTokens.density;

  // ─── Color group (W.TEACHING=19 .. W.MINDFUL=26) ────────────────────────
  const colorW = detectDominantColorW(vector);
  // COLOR_W_TO_TONAL is keyed by all Color W positions (19-26) — always defined for valid input
  const tonalName = COLOR_W_TO_TONAL[colorW] as string & keyof typeof tokens.colors;
  const colorTokens = tokens.colors[tonalName];

  props['--ppl-theme-primary']    = colorTokens.primary;
  props['--ppl-theme-secondary']  = colorTokens.secondary;
  props['--ppl-theme-background'] = colorTokens.background;
  props['--ppl-theme-surface']    = colorTokens.surface;
  props['--ppl-theme-text']       = colorTokens.text;
  props['--ppl-theme-accent']     = colorTokens.accent;
  props['--ppl-theme-border']     = colorTokens.border;

  // ─── Color tonal meta ────────────────────────────────────────────────────
  // Saturation: constant per Color temperament (NOT weight-derived — see pitfall 2)
  // COLOR_SATURATION is keyed by all Color W positions (19-26) — always defined
  const saturation = COLOR_SATURATION[colorW] as number;
  props['--ppl-weight-saturation'] = saturation.toFixed(2);

  // Contrast: normalized dominant Color weight — a UI emphasis signal.
  // Maps to actual luminance differential in Phase 8 card templates.
  // WCAG AA contrast ratio (4.5:1 floor) is enforced at the template level, not here.
  const colorNorm = normalize(vget(vector, colorW));
  props['--ppl-weight-contrast'] = colorNorm.toFixed(3);

  // Tonal name descriptor — allows CSS consumers to know which tonal palette is active
  props['--ppl-weight-tonal-name'] = tonalName;

  // ─── Axis group (W.BASICS=8 .. W.PARTNER=13) ────────────────────────────
  const axisW = dominantDim(vector, W.BASICS, W.PARTNER);
  // AXIS_W_TO_SLUG is keyed by all valid Axis W positions (8-13) — always defined
  const axisSlug = AXIS_W_TO_SLUG[axisW] as string;
  const axisTokens = tokens.axes[axisSlug as keyof typeof tokens.axes];

  props['--ppl-weight-gradient-direction'] = axisTokens.gradientDirection;
  props['--ppl-weight-layout-flow']        = axisTokens.layoutFlow;
  props['--ppl-weight-typography-bias']    = axisTokens.typographyBias;

  // Visual rhythm: normalized dominant Axis weight — indicates session structural density.
  // Used by card templates to modulate spacing between movement cues.
  const axisNorm = normalize(vget(vector, axisW));
  props['--ppl-weight-visual-rhythm'] = axisNorm.toFixed(3);

  // ─── Type emphasis group (W.PUSH=14 .. W.ULTRA=18) ───────────────────────
  // normalize() maps [-8, +8] weight scale to [0.0, 1.0]
  // Suppressed types score -8 → normalize(-8) = 0.0
  // Dominant type scores +8 → normalize(+8) = 1.0
  const TYPE_NAMES = ['push', 'pull', 'legs', 'plus', 'ultra'] as const;
  for (let i = 0; i < 5; i++) {
    props[`--ppl-weight-emphasis-${TYPE_NAMES[i]}`] = normalize(vget(vector, W.PUSH + i)).toFixed(3);
  }

  // ─── Derived dimensions (W.CAPIO=27 .. W.SAVE=61) ────────────────────────
  // Note: resolveZip() populates positions 1–26 only. Positions 27–61 are zero.
  // normalize(0) = 0.5 (neutral midpoint). These CSS properties will be 0.500
  // until block/operator weight tables are populated (Phase 8+).

  // Operator cluster (W.CAPIO=27 .. W.TENEO=38): drives rep-display prominence
  let repSum = 0;
  for (let i = W.CAPIO; i <= W.TENEO; i++) {
    repSum += vget(vector, i);
  }
  const repMean = repSum / 12;
  props['--ppl-weight-rep-display'] = normalize(repMean).toFixed(3);

  // Block cluster (W.WARM_UP=39 .. W.CHOICE=60): drives block spacing
  let blockSum = 0;
  for (let i = W.WARM_UP; i <= W.CHOICE; i++) {
    blockSum += vget(vector, i);
  }
  const blockMean = blockSum / 22;
  props['--ppl-weight-block-spacing'] = normalize(blockMean).toFixed(3);
  props['--ppl-weight-cue-density']   = normalize(blockMean).toFixed(3);

  // Rest emphasis: airy Orders (low fontWeight, high lineHeight) show rest prominently.
  // Uses normalized Order weight (dominant Order position in the vector).
  const orderNorm = normalize(vget(vector, orderW));
  props['--ppl-weight-rest-emphasis'] = lerp(0.3, 0.9, orderNorm).toFixed(3);

  return props;
}
