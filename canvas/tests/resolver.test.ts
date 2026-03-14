/**
 * Resolver TDD Tests
 *
 * Covers resolveVector() hard suppression hierarchy (Order > Color > Axis > Type)
 * and ParseResult interface shape validation.
 *
 * RED phase: These tests are written before the implementation exists.
 * They must fail until resolver.ts and parse-result.ts are created.
 */

import { describe, it, expect } from 'vitest';
import { computeRawVector } from '../src/weights/index.js';
import { W } from '../src/types/scl.js';
import { resolveVector, resolveZip } from '../src/weights/resolver.js';
import type { ParseResult, DimensionGroup } from '../src/parser/parse-result.js';

// ---------------------------------------------------------------------------
// resolveVector() — shape
// ---------------------------------------------------------------------------

describe('resolveVector() shape', () => {
  it('returns Float32Array of length 62 (slot 0 unused, slots 1–61)', () => {
    const raw = computeRawVector(2, 1, 2, 3);
    const resolved = resolveVector(raw, 2, 1, 2, 3);
    expect(resolved).toBeInstanceOf(Float32Array);
    expect(resolved.length).toBe(62);
  });

  it('does not mutate the input raw vector', () => {
    const raw = computeRawVector(2, 1, 2, 3);
    const rawCopy = new Float32Array(raw);
    resolveVector(raw, 2, 1, 2, 3);
    expect(raw).toEqual(rawCopy);
  });
});

// ---------------------------------------------------------------------------
// Order hard suppression: Restoration (pos 7) pins W.GUTTER to -8
//
// Zip 7-3-1-5 = Restoration / Aesthetic / Push / Intense
//   Order 7 suppressions: { W.GUTTER: -8 }
//   Color 5 (Intense) affinities: { W.GUTTER: +6 }
//   computeRawVector would sum these. After clamping, Gutter > -8.
//   resolveVector must override and pin W.GUTTER to -8.
// ---------------------------------------------------------------------------

describe('Order hard suppression — Restoration (pos 7)', () => {
  it('zip 7-3-1-5: W.GUTTER is pinned to -8 despite Intense Color +6 affinity', () => {
    const raw = computeRawVector(7, 3, 1, 5);
    const resolved = resolveVector(raw, 7, 3, 1, 5);

    // Confirm that the raw vector at W.GUTTER is NOT -8
    // (Intense adds +6 affinity, so raw will be > -8)
    expect(raw[W.GUTTER]).toBeGreaterThan(-8);

    // Resolver must pin it to -8
    expect(resolved[W.GUTTER]).toBe(-8);
  });

  it('zip 7-3-1-5: W.GUTTER is -8 regardless of Color contribution', () => {
    // Same Order (Restoration) with different colors — all should have W.GUTTER = -8
    const colors = [1, 2, 3, 4, 5, 6, 7, 8] as const;
    for (const colorPos of colors) {
      const raw = computeRawVector(7, 3, 1, colorPos);
      const resolved = resolveVector(raw, 7, 3, 1, colorPos);
      expect(resolved[W.GUTTER]).toBe(-8);
    }
  });

  it('zip 7-3-1-5: W.PERFORMANCE is pinned to -8 by Restoration Order', () => {
    // Order 7 suppressions: { W.PERFORMANCE: -8 }
    const raw = computeRawVector(7, 3, 1, 5);
    const resolved = resolveVector(raw, 7, 3, 1, 5);
    expect(resolved[W.PERFORMANCE]).toBe(-8);
  });
});

// ---------------------------------------------------------------------------
// Color hard suppression: Circuit (pos 6) pins W.STRENGTH to -8
//
// Zip 2-1-2-6 = Strength / Basics / Pull / Circuit
//   Order 2 (Strength) sets self = +8 at W.STRENGTH
//   Color 6 (Circuit) suppressions: { W.STRENGTH: -8 }
//   computeRawVector sums them → W.STRENGTH gets clamped but not at -8
//   resolveVector must pin W.STRENGTH to -8 because Color suppression <= -6
// ---------------------------------------------------------------------------

describe('Color hard suppression — Circuit (pos 6)', () => {
  it('zip 2-1-2-6: W.STRENGTH is pinned to -8 despite Strength Order self=+8', () => {
    const raw = computeRawVector(2, 1, 2, 6);
    const resolved = resolveVector(raw, 2, 1, 2, 6);

    // Raw at W.STRENGTH position is the self value (+8) + suppressions accumulated
    // Circuit suppresses at -8 but computeRawVector sums, so raw won't be -8
    // (it will be 8 + (-8) = 0 after steps, clamped to 0)
    // Note: W.STRENGTH = 2 (the Order slot) — suppression applies to that position
    // Actually confirm the raw isn't -8 (raw sums all contributions)
    // The resolved value must be -8
    expect(resolved[W.STRENGTH]).toBe(-8);
  });

  it('zip 2-1-2-6: W.GUTTER is -8 because Circuit also suppresses it at -8', () => {
    const raw = computeRawVector(2, 1, 2, 6);
    const resolved = resolveVector(raw, 2, 1, 2, 6);
    expect(resolved[W.GUTTER]).toBe(-8);
  });

  it('Color Circuit pins W.STRENGTH to -8 for Orders without a higher-priority W.STRENGTH suppression', () => {
    // Circuit (colorPos 6) suppresses W.STRENGTH at -8.
    // Exception: Order 7 (Restoration) has its own hard suppression on W.STRENGTH at -6,
    // which fires first (Order > Color hierarchy). So for Order 7 + Circuit, resolved
    // W.STRENGTH is -6 (Order wins) not -8 (Color loses).
    //
    // All other Orders (1–6) have no hard suppression on W.STRENGTH, so Circuit's -8 wins.
    const ordersWithNoStrengthHardSuppression = [1, 2, 3, 4, 5, 6] as const;
    for (const orderPos of ordersWithNoStrengthHardSuppression) {
      const raw = computeRawVector(orderPos, 1, 1, 6);
      const resolved = resolveVector(raw, orderPos, 1, 1, 6);
      expect(resolved[W.STRENGTH]).toBe(-8);
    }
  });

  it('Order 7 (Restoration) beats Circuit on W.STRENGTH: result is -6 not -8', () => {
    // Order 7 hard-suppresses W.STRENGTH at -6. Color 6 (Circuit) wants -8.
    // Since Order has higher priority, resolved value is -6.
    const raw = computeRawVector(7, 1, 1, 6);
    const resolved = resolveVector(raw, 7, 1, 1, 6);
    expect(resolved[W.STRENGTH]).toBe(-6);
  });
});

// ---------------------------------------------------------------------------
// Soft weight pass-through
//
// Zip 2-1-2-3 = Strength / Basics / Pull / Structured
// No hard suppressions active at most positions.
// resolveVector() must return identical values to computeRawVector() at
// non-hard-suppressed positions.
// ---------------------------------------------------------------------------

describe('Soft weight pass-through — zip 2-1-2-3', () => {
  it('non-suppressed positions equal computeRawVector() output', () => {
    const orderPos = 2;
    const axisPos  = 1;
    const typePos  = 2;
    const colorPos = 3;
    const raw      = computeRawVector(orderPos, axisPos, typePos, colorPos);
    const resolved = resolveVector(raw, orderPos, axisPos, typePos, colorPos);

    // Check a representative non-suppressed position
    // W.BREAD_BUTTER (42) — Strength has +8, Structured has +4, neither hard-suppresses it
    expect(resolved[W.BREAD_BUTTER]).toBe(raw[W.BREAD_BUTTER]);

    // W.WARM_UP (39) — no hard suppression
    expect(resolved[W.WARM_UP]).toBe(raw[W.WARM_UP]);

    // W.BASICS (8) — Strength affinities include Basics +2, no hard suppression
    expect(resolved[W.BASICS]).toBe(raw[W.BASICS]);

    // W.PULL (15) — no hard suppression from Order 2 or Color 3
    expect(resolved[W.PULL]).toBe(raw[W.PULL]);
  });

  it('resolver does not re-sum: output equals input at non-suppressed positions', () => {
    // resolveVector must NOT re-apply any affinity or suppression values
    // It only pins floors. So the output at non-suppressed positions IS the raw input.
    const raw = computeRawVector(2, 1, 2, 3);
    const resolved = resolveVector(raw, 2, 1, 2, 3);

    // Scan all positions; for non-hard-suppressed ones, values must match
    // Hard-suppressed ones in Structured (colorPos 3) suppressions: { W.GUTTER: -8 }
    // So W.GUTTER will differ (pinned to -8 by Color)
    for (let i = 1; i <= 61; i++) {
      const isHardSuppressed = (resolved[i] === -8 || resolved[i] === -6) &&
                               (raw[i] as number) > (resolved[i] as number);
      if (!isHardSuppressed) {
        expect(resolved[i]).toBe(raw[i]);
      }
    }
  });
});

// ---------------------------------------------------------------------------
// resolveZip() convenience wrapper
// ---------------------------------------------------------------------------

describe('resolveZip() convenience wrapper', () => {
  it('returns same result as resolveVector(computeRawVector(...))', () => {
    const orderPos = 2;
    const axisPos  = 1;
    const typePos  = 2;
    const colorPos = 3;

    const raw      = computeRawVector(orderPos, axisPos, typePos, colorPos);
    const expected = resolveVector(raw, orderPos, axisPos, typePos, colorPos);
    const actual   = resolveZip(orderPos, axisPos, typePos, colorPos);

    expect(actual).toEqual(expected);
  });

  it('resolveZip returns Float32Array of length 62', () => {
    const result = resolveZip(7, 3, 1, 5);
    expect(result).toBeInstanceOf(Float32Array);
    expect(result.length).toBe(62);
  });
});

// ---------------------------------------------------------------------------
// ParseResult interface — compile-time shape test
//
// This test verifies that a valid ParseResult literal can be constructed
// and that defaulted_dimensions is a required field (not optional).
// ---------------------------------------------------------------------------

describe('ParseResult interface', () => {
  it('can construct a valid ParseResult with all required fields', () => {
    const result: ParseResult = {
      zip: '⛽🏛🪡🔵',
      numericZip: '2123',
      orderPos: 2,
      axisPos: 1,
      typePos: 2,
      colorPos: 3,
      weightVector: resolveZip(2, 1, 2, 3),
      confidence: 1.0,
      defaulted_dimensions: [],
      matchedTerms: ['barbell', 'pull'],
    };

    expect(result.zip).toBe('⛽🏛🪡🔵');
    expect(result.numericZip).toBe('2123');
    expect(result.orderPos).toBe(2);
    expect(result.axisPos).toBe(1);
    expect(result.typePos).toBe(2);
    expect(result.colorPos).toBe(3);
    expect(result.weightVector).toBeInstanceOf(Float32Array);
    expect(result.confidence).toBe(1.0);
    expect(result.defaulted_dimensions).toEqual([]);
    expect(result.matchedTerms).toEqual(['barbell', 'pull']);
  });

  it('defaulted_dimensions accepts valid DimensionGroup values', () => {
    const dims: DimensionGroup[] = ['order', 'axis', 'type', 'color'];
    const result: ParseResult = {
      zip: '🐂🏛🛒⚫',
      numericZip: '1111',
      orderPos: 1,
      axisPos: 1,
      typePos: 1,
      colorPos: 1,
      weightVector: resolveZip(1, 1, 1, 1),
      confidence: 0.5,
      defaulted_dimensions: dims,
      matchedTerms: [],
    };

    expect(result.defaulted_dimensions).toHaveLength(4);
    expect(result.defaulted_dimensions[0]).toBe('order');
    expect(result.defaulted_dimensions[1]).toBe('axis');
    expect(result.defaulted_dimensions[2]).toBe('type');
    expect(result.defaulted_dimensions[3]).toBe('color');
  });

  it('defaulted_dimensions is a required field on ParseResult', () => {
    // This test verifies the type is valid TypeScript — no optional marker.
    // If defaulted_dimensions were optional (DimensionGroup[]?), the type
    // would accept undefined, but we always require the array.
    //
    // We verify this at runtime by checking it's always an array.
    const result: ParseResult = {
      zip: '⛽🏛🛒🔵',
      numericZip: '2113',
      orderPos: 2,
      axisPos: 1,
      typePos: 1,
      colorPos: 3,
      weightVector: resolveZip(2, 1, 1, 3),
      confidence: 0.8,
      defaulted_dimensions: ['axis'],
      matchedTerms: ['bench', 'press'],
    };

    expect(Array.isArray(result.defaulted_dimensions)).toBe(true);
    expect(result.defaulted_dimensions).toContain('axis');
  });
});
