/**
 * rendering.test.ts — Phase 5 CSS Rendering Pipeline Tests (TEST-04)
 *
 * Requirements: RNDR-05, RNDR-06, RNDR-07, TEST-04
 *
 * All tests are anchored on zip 2123 (⛽🏛🪡🔵 — Strength/Basics/Pull/Structured)
 * as the known-value anchor for expected CSS output.
 *
 * TDD: RED phase — tests written before implementations exist.
 */

import { describe, it, expect, beforeAll } from 'vitest';
import { resolveZip } from '../src/weights/resolver.js';
import { tokens } from '../src/tokens/tokens.js';
import { W, BLOCKS } from '../src/types/scl.js';
import {
  weightsToCSSVars,
  COLOR_SATURATION,
  BLOCK_CONTAINER_STYLES,
} from '../src/rendering/index.js';

// ---------------------------------------------------------------------------
// Test setup — resolve known zip 2123 once
// ---------------------------------------------------------------------------

let vector2123: Float32Array;

beforeAll(() => {
  // zip 2123 = Order 2 (Strength), Axis 1 (Basics), Type 2 (Pull), Color 3 (Structured)
  vector2123 = resolveZip(2, 1, 2, 3);
});

// ---------------------------------------------------------------------------
// RNDR-05: weightsToCSSVars() — pure function contract
// ---------------------------------------------------------------------------

describe('RNDR-05: weightsToCSSVars() — pure function contract', () => {
  it('returns a Record<string, string> (not undefined, not empty)', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result).toBeDefined();
    expect(typeof result).toBe('object');
    expect(Object.keys(result).length).toBeGreaterThan(0);
  });

  it('returns 30+ CSS custom property keys', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(Object.keys(result).length).toBeGreaterThanOrEqual(30);
  });

  it('is a pure function — same vector + same tokens = identical output', () => {
    const result1 = weightsToCSSVars(vector2123, tokens);
    const result2 = weightsToCSSVars(vector2123, tokens);
    expect(result1).toEqual(result2);
  });

  it('does not mutate the input Float32Array', () => {
    const snapshot = Array.from(vector2123);
    weightsToCSSVars(vector2123, tokens);
    expect(Array.from(vector2123)).toEqual(snapshot);
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — expected Order token values (Strength)
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — Order token values (Strength)', () => {
  it('--ppl-weight-font-weight === "800"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-font-weight']).toBe('800');
  });

  it('--ppl-weight-lineheight === "1.4"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-lineheight']).toBe('1.4');
  });

  it('--ppl-weight-spacing-multiplier === "0.85"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-spacing-multiplier']).toBe('0.85');
  });

  it('--ppl-weight-letter-spacing === "0.005em"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-letter-spacing']).toBe('0.005em');
  });

  it('--ppl-weight-density === "compact"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-density']).toBe('compact');
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — expected Color theme values (Structured → planning tonal)
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — Color theme values (Structured = planning tonal)', () => {
  it('--ppl-theme-primary matches tokens.colors.planning.primary', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-primary']).toBe(tokens.colors.planning.primary);
  });

  it('--ppl-theme-secondary matches tokens.colors.planning.secondary', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-secondary']).toBe(tokens.colors.planning.secondary);
  });

  it('--ppl-theme-background matches tokens.colors.planning.background', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-background']).toBe(tokens.colors.planning.background);
  });

  it('--ppl-theme-surface matches tokens.colors.planning.surface', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-surface']).toBe(tokens.colors.planning.surface);
  });

  it('--ppl-theme-text matches tokens.colors.planning.text', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-text']).toBe(tokens.colors.planning.text);
  });

  it('--ppl-theme-accent matches tokens.colors.planning.accent', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-accent']).toBe(tokens.colors.planning.accent);
  });

  it('--ppl-theme-border matches tokens.colors.planning.border', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-theme-border']).toBe(tokens.colors.planning.border);
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — expected saturation (Structured = 0.50)
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — saturation and contrast', () => {
  it('--ppl-weight-saturation === "0.50" (Structured Color)', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-saturation']).toBe('0.50');
  });

  it('--ppl-weight-contrast exists as a string number', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-contrast']).toBeDefined();
    expect(isNaN(parseFloat(result['--ppl-weight-contrast']!))).toBe(false);
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — Axis directional values (Basics)
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — Axis directional values (Basics)', () => {
  it('--ppl-weight-gradient-direction === "to bottom"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-gradient-direction']).toBe('to bottom');
  });

  it('--ppl-weight-layout-flow === "column"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-layout-flow']).toBe('column');
  });

  it('--ppl-weight-typography-bias === "classical"', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-typography-bias']).toBe('classical');
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — Type emphasis (Pull type dominant, Push suppressed)
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — Type emphasis properties', () => {
  it('all --ppl-weight-emphasis-* keys exist', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-emphasis-push']).toBeDefined();
    expect(result['--ppl-weight-emphasis-pull']).toBeDefined();
    expect(result['--ppl-weight-emphasis-legs']).toBeDefined();
    expect(result['--ppl-weight-emphasis-plus']).toBeDefined();
    expect(result['--ppl-weight-emphasis-ultra']).toBeDefined();
  });

  it('--ppl-weight-emphasis-pull is near 1.0 (dominant type for Pull zip)', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    const pull = parseFloat(result['--ppl-weight-emphasis-pull']!);
    expect(pull).toBeGreaterThan(0.6);
  });

  it('--ppl-weight-emphasis-push is near 0.0 (suppressed type for Pull zip)', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    const push = parseFloat(result['--ppl-weight-emphasis-push']!);
    expect(push).toBeLessThan(0.5);
  });
});

// ---------------------------------------------------------------------------
// RNDR-05: zip 2123 — Derived dimension properties
// ---------------------------------------------------------------------------

describe('RNDR-05: zip 2123 — Derived dimension properties', () => {
  it('--ppl-weight-rep-display exists as string number', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-rep-display']).toBeDefined();
    expect(isNaN(parseFloat(result['--ppl-weight-rep-display']!))).toBe(false);
  });

  it('--ppl-weight-block-spacing exists as string number', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-block-spacing']).toBeDefined();
    expect(isNaN(parseFloat(result['--ppl-weight-block-spacing']!))).toBe(false);
  });

  it('--ppl-weight-cue-density exists as string number', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-cue-density']).toBeDefined();
    expect(isNaN(parseFloat(result['--ppl-weight-cue-density']!))).toBe(false);
  });

  it('--ppl-weight-rest-emphasis exists as string number', () => {
    const result = weightsToCSSVars(vector2123, tokens);
    expect(result['--ppl-weight-rest-emphasis']).toBeDefined();
    expect(isNaN(parseFloat(result['--ppl-weight-rest-emphasis']!))).toBe(false);
  });
});

// ---------------------------------------------------------------------------
// RNDR-07: COLOR_SATURATION — per-Color constants
// ---------------------------------------------------------------------------

describe('RNDR-07: COLOR_SATURATION constant', () => {
  it('Teaching (W.TEACHING=19) saturation <= 0.10', () => {
    const vec = resolveZip(2, 1, 2, 1); // Color pos 1 = Teaching
    const result = weightsToCSSVars(vec, tokens);
    expect(parseFloat(result['--ppl-weight-saturation']!)).toBeLessThanOrEqual(0.10);
  });

  it('Intense (W.INTENSE=23) saturation >= 0.85', () => {
    const vec = resolveZip(2, 1, 2, 5); // Color pos 5 = Intense
    const result = weightsToCSSVars(vec, tokens);
    expect(parseFloat(result['--ppl-weight-saturation']!)).toBeGreaterThanOrEqual(0.85);
  });

  it('Mindful (W.MINDFUL=26) saturation <= 0.15', () => {
    const vec = resolveZip(2, 1, 2, 8); // Color pos 8 = Mindful
    const result = weightsToCSSVars(vec, tokens);
    expect(parseFloat(result['--ppl-weight-saturation']!)).toBeLessThanOrEqual(0.15);
  });

  it('COLOR_SATURATION constant has exactly 8 entries (W positions 19-26)', () => {
    expect(Object.keys(COLOR_SATURATION)).toHaveLength(8);
  });

  it('all 8 saturation values are in range [0.0, 1.0]', () => {
    for (const [wPos, sat] of Object.entries(COLOR_SATURATION)) {
      expect(sat).toBeGreaterThanOrEqual(0.0);
      expect(sat).toBeLessThanOrEqual(1.0);
      // wPos should be in range 19-26
      expect(Number(wPos)).toBeGreaterThanOrEqual(19);
      expect(Number(wPos)).toBeLessThanOrEqual(26);
    }
  });
});

// ---------------------------------------------------------------------------
// RNDR-06: BLOCK_CONTAINER_STYLES — 22-entry static map
// ---------------------------------------------------------------------------

describe('RNDR-06: BLOCK_CONTAINER_STYLES — 22-entry static map', () => {
  it('has exactly 22 keys', () => {
    expect(Object.keys(BLOCK_CONTAINER_STYLES)).toHaveLength(22);
  });

  it('every slug from BLOCKS const is present as a key', () => {
    const blockSlugs = Object.values(BLOCKS).map((b) => b.slug);
    for (const slug of blockSlugs) {
      expect(BLOCK_CONTAINER_STYLES).toHaveProperty(slug);
    }
  });

  it('all 5 roles are represented: orientation, access, transformation, retention, modifier', () => {
    const roles = new Set(Object.values(BLOCK_CONTAINER_STYLES).map((s) => s.role));
    expect(roles.has('orientation')).toBe(true);
    expect(roles.has('access')).toBe(true);
    expect(roles.has('transformation')).toBe(true);
    expect(roles.has('retention')).toBe(true);
    expect(roles.has('modifier')).toBe(true);
  });

  it('every entry has required fields: role, cssClass, borderAccent, paddingMultiplier, emphasisLevel', () => {
    for (const [slug, style] of Object.entries(BLOCK_CONTAINER_STYLES)) {
      expect(style, `${slug} missing role`).toHaveProperty('role');
      expect(style, `${slug} missing cssClass`).toHaveProperty('cssClass');
      expect(style, `${slug} missing borderAccent`).toHaveProperty('borderAccent');
      expect(style, `${slug} missing paddingMultiplier`).toHaveProperty('paddingMultiplier');
      expect(style, `${slug} missing emphasisLevel`).toHaveProperty('emphasisLevel');
    }
  });

  it('bread-butter has emphasisLevel "high" (main work block)', () => {
    expect(BLOCK_CONTAINER_STYLES['bread-butter']!.emphasisLevel).toBe('high');
  });

  it('intention has emphasisLevel "medium" (framing block)', () => {
    expect(BLOCK_CONTAINER_STYLES['intention']!.emphasisLevel).toBe('medium');
  });

  it('choice has role "modifier"', () => {
    expect(BLOCK_CONTAINER_STYLES['choice']!.role).toBe('modifier');
  });

  it('paddingMultiplier values are numeric', () => {
    for (const [slug, style] of Object.entries(BLOCK_CONTAINER_STYLES)) {
      expect(typeof style.paddingMultiplier, `${slug}.paddingMultiplier not a number`).toBe('number');
    }
  });

  it('emphasisLevel values are "low" | "medium" | "high"', () => {
    const validLevels = new Set(['low', 'medium', 'high']);
    for (const [slug, style] of Object.entries(BLOCK_CONTAINER_STYLES)) {
      expect(validLevels.has(style.emphasisLevel), `${slug}.emphasisLevel invalid: ${style.emphasisLevel}`).toBe(true);
    }
  });
});
