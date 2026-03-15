/**
 * pipeline-integration.test.ts — Full Pipeline Integration Tests (TEST-05)
 *
 * Requirements: TEST-05
 *
 * Validates the complete pipeline chain:
 *   scoreText() -> weightVector -> weightsToCSSVars() -> CSS vars
 *
 * Four test cases cover representative inputs:
 *   1. Strength query: "heavy barbell back work" (orderPos=2, typePos=2)
 *   2. Bodyweight query: "bodyweight squats at home" (colorPos=2)
 *   3. Ambiguous query: "tempo mindful stretching" (pipeline completes without error)
 *   4. Empty string: confidence=0, all 4 defaulted, CSS vars still valid
 *
 * Each stage of the pipeline is verified:
 *   - Stage 1: scoreText() returns ParseResult[] with correct shape
 *   - Stage 2: weightVector is Float32Array of length 62
 *   - Stage 3: weightsToCSSVars() returns 30+ non-empty CSS custom properties
 */

import { describe, it, expect, beforeAll } from 'vitest';
import { scoreText } from '../src/parser/scorer.js';
import { tokens } from '../src/tokens/tokens.js';
import { weightsToCSSVars } from '../src/rendering/index.js';
import type { ParseResult } from '../src/parser/parse-result.js';

// ---------------------------------------------------------------------------
// Helper: assert CSS vars output has 30+ valid non-empty entries
// ---------------------------------------------------------------------------

function assertValidCSSVars(vars: Record<string, string>, context: string): void {
  const keys = Object.keys(vars);
  expect(keys.length, `${context}: expected 30+ CSS vars`).toBeGreaterThanOrEqual(30);
  for (const key of keys) {
    const val = vars[key];
    expect(val, `${context}: CSS var ${key} must be defined`).toBeDefined();
    expect(val, `${context}: CSS var ${key} must not be empty string`).not.toBe('');
    expect(val, `${context}: CSS var ${key} must not be "undefined"`).not.toBe('undefined');
  }
}

// ---------------------------------------------------------------------------
// Stage 1: Test that scoreText() produces a well-formed ParseResult array
// ---------------------------------------------------------------------------

function assertParseResultShape(results: ParseResult[], context: string): void {
  expect(Array.isArray(results), `${context}: results must be array`).toBe(true);
  expect(results.length, `${context}: must have at least one result`).toBeGreaterThan(0);

  const top = results[0]!;
  expect(top, `${context}: orderPos`).toHaveProperty('orderPos');
  expect(top, `${context}: axisPos`).toHaveProperty('axisPos');
  expect(top, `${context}: typePos`).toHaveProperty('typePos');
  expect(top, `${context}: colorPos`).toHaveProperty('colorPos');
  expect(top, `${context}: weightVector`).toHaveProperty('weightVector');
  expect(top, `${context}: confidence`).toHaveProperty('confidence');
  expect(top, `${context}: defaulted_dimensions`).toHaveProperty('defaulted_dimensions');
  expect(top.weightVector, `${context}: weightVector is Float32Array`).toBeInstanceOf(Float32Array);
  expect(top.weightVector.length, `${context}: weightVector length is 62`).toBe(62);
}

// ---------------------------------------------------------------------------
// TEST-05: Integration Case 1 — Strength query
// ---------------------------------------------------------------------------

describe('TEST-05: integration — "heavy barbell back work"', () => {
  let results: ParseResult[];
  let cssVars: Record<string, string>;

  beforeAll(() => {
    results = scoreText('heavy barbell back work');
    cssVars = weightsToCSSVars(results[0]!.weightVector, tokens);
  });

  it('Stage 1: scoreText() returns ParseResult array', () => {
    assertParseResultShape(results, '"heavy barbell back work"');
  });

  it('Stage 1: top result has orderPos=2 (Strength)', () => {
    expect(results[0]!.orderPos).toBe(2);
  });

  it('Stage 1: top result has typePos=2 (Pull)', () => {
    expect(results[0]!.typePos).toBe(2);
  });

  it('Stage 1: confidence is > 0', () => {
    expect(results[0]!.confidence).toBeGreaterThan(0);
  });

  it('Stage 2: weightVector is Float32Array of length 62', () => {
    expect(results[0]!.weightVector).toBeInstanceOf(Float32Array);
    expect(results[0]!.weightVector.length).toBe(62);
  });

  it('Stage 3: weightsToCSSVars() returns 30+ CSS vars', () => {
    expect(Object.keys(cssVars).length).toBeGreaterThanOrEqual(30);
  });

  it('Stage 3: all CSS vars are non-empty strings', () => {
    assertValidCSSVars(cssVars, '"heavy barbell back work"');
  });

  it('Stage 3: Order CSS var reflects Strength token (font-weight "800")', () => {
    expect(cssVars['--ppl-weight-font-weight']).toBe('800');
  });

  it('Stage 3: Order density is "compact" (Strength)', () => {
    expect(cssVars['--ppl-weight-density']).toBe('compact');
  });
});

// ---------------------------------------------------------------------------
// TEST-05: Integration Case 2 — Bodyweight query
// ---------------------------------------------------------------------------

describe('TEST-05: integration — "bodyweight squats at home"', () => {
  let results: ParseResult[];
  let cssVars: Record<string, string>;

  beforeAll(() => {
    results = scoreText('bodyweight squats at home');
    cssVars = weightsToCSSVars(results[0]!.weightVector, tokens);
  });

  it('Stage 1: scoreText() returns ParseResult array', () => {
    assertParseResultShape(results, '"bodyweight squats at home"');
  });

  it('Stage 1: top result has colorPos=2 (Bodyweight)', () => {
    expect(results[0]!.colorPos).toBe(2);
  });

  it('Stage 1: confidence is > 0', () => {
    expect(results[0]!.confidence).toBeGreaterThan(0);
  });

  it('Stage 2: weightVector is Float32Array of length 62', () => {
    expect(results[0]!.weightVector).toBeInstanceOf(Float32Array);
    expect(results[0]!.weightVector.length).toBe(62);
  });

  it('Stage 3: weightsToCSSVars() returns 30+ CSS vars', () => {
    expect(Object.keys(cssVars).length).toBeGreaterThanOrEqual(30);
  });

  it('Stage 3: all CSS vars are non-empty strings', () => {
    assertValidCSSVars(cssVars, '"bodyweight squats at home"');
  });

  it('Stage 3: saturation is low (Bodyweight = natural, ~0.40)', () => {
    const sat = parseFloat(cssVars['--ppl-weight-saturation']!);
    expect(sat).toBeLessThanOrEqual(0.50);
  });

  it('Stage 3: tonal name is "growth" (Bodyweight Color)', () => {
    expect(cssVars['--ppl-weight-tonal-name']).toBe('growth');
  });
});

// ---------------------------------------------------------------------------
// TEST-05: Integration Case 3 — Ambiguous query
// ---------------------------------------------------------------------------

describe('TEST-05: integration — "tempo mindful stretching" (ambiguous)', () => {
  let results: ParseResult[];
  let cssVars: Record<string, string>;

  beforeAll(() => {
    results = scoreText('tempo mindful stretching');
    cssVars = weightsToCSSVars(results[0]!.weightVector, tokens);
  });

  it('Stage 1: scoreText() completes without throwing', () => {
    // Test passes if beforeAll ran without error
    expect(results).toBeDefined();
  });

  it('Stage 1: returns at least one ParseResult', () => {
    expect(results.length).toBeGreaterThanOrEqual(1);
  });

  it('Stage 2: weightVector is Float32Array of length 62', () => {
    expect(results[0]!.weightVector).toBeInstanceOf(Float32Array);
    expect(results[0]!.weightVector.length).toBe(62);
  });

  it('Stage 3: weightsToCSSVars() returns 30+ CSS vars without throwing', () => {
    expect(Object.keys(cssVars).length).toBeGreaterThanOrEqual(30);
  });

  it('Stage 3: all CSS vars are non-empty strings', () => {
    assertValidCSSVars(cssVars, '"tempo mindful stretching"');
  });

  it('Stage 3: pipeline produces a valid tonal name', () => {
    const validTonalNames = ['order', 'growth', 'planning', 'magnificence', 'passion', 'connection', 'play', 'eudaimonia'];
    expect(validTonalNames).toContain(cssVars['--ppl-weight-tonal-name']);
  });
});

// ---------------------------------------------------------------------------
// TEST-05: Integration Case 4 — Empty string input
// ---------------------------------------------------------------------------

describe('TEST-05: integration — "" (empty string)', () => {
  let results: ParseResult[];
  let cssVars: Record<string, string>;

  beforeAll(() => {
    results = scoreText('');
    // Empty string: scoreText returns 1 result with defaults + confidence=0
    cssVars = weightsToCSSVars(results[0]!.weightVector, tokens);
  });

  it('Stage 1: scoreText("") returns exactly 1 result (no candidates for zero-match)', () => {
    expect(results.length).toBe(1);
  });

  it('Stage 1: confidence is exactly 0 for empty input', () => {
    expect(results[0]!.confidence).toBe(0);
  });

  it('Stage 1: all 4 dimensions are in defaulted_dimensions', () => {
    const dims = results[0]!.defaulted_dimensions;
    expect(dims).toContain('order');
    expect(dims).toContain('axis');
    expect(dims).toContain('type');
    expect(dims).toContain('color');
    expect(dims.length).toBe(4);
  });

  it('Stage 1: default positions are used (order=3/Hypertrophy, axis=1/Basics, type=1/Push, color=3/Structured)', () => {
    expect(results[0]!.orderPos).toBe(3); // Hypertrophy
    expect(results[0]!.axisPos).toBe(1);  // Basics
    expect(results[0]!.typePos).toBe(1);  // Push
    expect(results[0]!.colorPos).toBe(3); // Structured
  });

  it('Stage 2: weightVector is Float32Array of length 62 (defaults are valid zips)', () => {
    expect(results[0]!.weightVector).toBeInstanceOf(Float32Array);
    expect(results[0]!.weightVector.length).toBe(62);
  });

  it('Stage 3: weightsToCSSVars() still produces 30+ CSS vars from defaulted zip', () => {
    expect(Object.keys(cssVars).length).toBeGreaterThanOrEqual(30);
  });

  it('Stage 3: all CSS vars are non-empty strings (defaults produce valid output)', () => {
    assertValidCSSVars(cssVars, 'empty string');
  });

  it('Stage 3: default zip 3113 produces Hypertrophy Order tokens (font-weight "600")', () => {
    // Default zip: order=3(Hypertrophy), axis=1(Basics), type=1(Push), color=3(Structured)
    expect(cssVars['--ppl-weight-font-weight']).toBe('600');
  });

  it('Stage 3: default zip produces "planning" tonal name (Structured Color)', () => {
    expect(cssVars['--ppl-weight-tonal-name']).toBe('planning');
  });
});
