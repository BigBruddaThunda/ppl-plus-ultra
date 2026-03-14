/**
 * Weight Tables — Spot-check tests
 *
 * RED phase: these tests are written before the weight tables exist.
 * They will fail until Task 2 populates all 6 weight tables.
 *
 * Test coverage:
 * - Entry counts per dial table
 * - Hard suppression rules cited from CLAUDE.md
 * - Coarse-scale enforcement across all values
 * - computeRawVector() correctness and output shape
 */

import { describe, it, expect } from 'vitest';
import {
  computeRawVector,
  ORDERS_WEIGHTS,
  AXES_WEIGHTS,
  TYPES_WEIGHTS,
  COLORS_WEIGHTS,
  BLOCKS_WEIGHTS,
  OPERATORS_WEIGHTS,
} from '../src/weights/index.js';
import { W } from '../src/types/scl.js';
import type { WeightScale } from '../src/weights/types.js';

// ---------------------------------------------------------------------------
// Coarse scale enforcement
// ---------------------------------------------------------------------------

const COARSE_VALUES = new Set<number>([-8, -6, -4, -2, 0, 2, 4, 6, 8]);

function assertCoarseScale(tableName: string, table: Record<number, { self: 8; affinities: Partial<Record<number, WeightScale>>; suppressions: Partial<Record<number, WeightScale>> }>) {
  for (const [pos, entry] of Object.entries(table)) {
    // self is always 8 — valid
    expect(COARSE_VALUES.has(entry.self), `${tableName}[${pos}].self must be coarse scale`).toBe(true);

    for (const [wPos, val] of Object.entries(entry.affinities)) {
      expect(
        COARSE_VALUES.has(val as number),
        `${tableName}[${pos}].affinities[${wPos}] = ${val} — not a coarse scale value`
      ).toBe(true);
    }

    for (const [wPos, val] of Object.entries(entry.suppressions)) {
      expect(
        COARSE_VALUES.has(val as number),
        `${tableName}[${pos}].suppressions[${wPos}] = ${val} — not a coarse scale value`
      ).toBe(true);
    }
  }
}

describe('All weight tables use coarse scale only', () => {
  it('ORDERS_WEIGHTS all values coarse', () => {
    assertCoarseScale('ORDERS_WEIGHTS', ORDERS_WEIGHTS);
  });

  it('AXES_WEIGHTS all values coarse', () => {
    assertCoarseScale('AXES_WEIGHTS', AXES_WEIGHTS);
  });

  it('TYPES_WEIGHTS all values coarse', () => {
    assertCoarseScale('TYPES_WEIGHTS', TYPES_WEIGHTS);
  });

  it('COLORS_WEIGHTS all values coarse', () => {
    assertCoarseScale('COLORS_WEIGHTS', COLORS_WEIGHTS);
  });

  it('BLOCKS_WEIGHTS all values coarse', () => {
    assertCoarseScale('BLOCKS_WEIGHTS', BLOCKS_WEIGHTS);
  });

  it('OPERATORS_WEIGHTS all values coarse', () => {
    assertCoarseScale('OPERATORS_WEIGHTS', OPERATORS_WEIGHTS);
  });
});

// ---------------------------------------------------------------------------
// Entry counts
// ---------------------------------------------------------------------------

describe('Weight table entry counts', () => {
  it('ORDERS_WEIGHTS has exactly 7 entries', () => {
    expect(Object.keys(ORDERS_WEIGHTS).length).toBe(7);
  });

  it('AXES_WEIGHTS has exactly 6 entries', () => {
    expect(Object.keys(AXES_WEIGHTS).length).toBe(6);
  });

  it('TYPES_WEIGHTS has exactly 5 entries', () => {
    expect(Object.keys(TYPES_WEIGHTS).length).toBe(5);
  });

  it('COLORS_WEIGHTS has exactly 8 entries', () => {
    expect(Object.keys(COLORS_WEIGHTS).length).toBe(8);
  });

  it('BLOCKS_WEIGHTS has exactly 22 entries', () => {
    expect(Object.keys(BLOCKS_WEIGHTS).length).toBe(22);
  });

  it('OPERATORS_WEIGHTS has exactly 12 entries', () => {
    expect(Object.keys(OPERATORS_WEIGHTS).length).toBe(12);
  });
});

// ---------------------------------------------------------------------------
// Self = +8 for all primary dials (Orders 1–7)
// ---------------------------------------------------------------------------

describe('Each entry has self === 8', () => {
  it('All ORDERS_WEIGHTS entries have self === 8', () => {
    for (let i = 1; i <= 7; i++) {
      expect(ORDERS_WEIGHTS[i]?.self).toBe(8);
    }
  });

  it('All AXES_WEIGHTS entries have self === 8', () => {
    for (let i = 1; i <= 6; i++) {
      expect(AXES_WEIGHTS[i]?.self).toBe(8);
    }
  });
});

// ---------------------------------------------------------------------------
// Hard suppression rules (CLAUDE.md citations)
// ---------------------------------------------------------------------------

describe('ORDERS_WEIGHTS[7] — Restoration hard suppressions', () => {
  it('ORDERS_WEIGHTS[7] suppresses W.GUTTER at -8 (CLAUDE.md: "Never in Restoration")', () => {
    expect(ORDERS_WEIGHTS[7]?.suppressions[W.GUTTER]).toBe(-8);
  });

  it('ORDERS_WEIGHTS[7] suppresses W.STRENGTH at -6 (heavy loading contradicts <=55% ceiling)', () => {
    expect(ORDERS_WEIGHTS[7]?.suppressions[W.STRENGTH]).toBe(-6);
  });
});

describe('COLORS_WEIGHTS[5] — Intense hard suppression', () => {
  it('COLORS_WEIGHTS[5] (Intense) suppresses W.MINDFUL at -6 (opposite character)', () => {
    expect(COLORS_WEIGHTS[5]?.suppressions[W.MINDFUL]).toBe(-6);
  });
});

describe('TYPES_WEIGHTS[1] — Push hard suppression', () => {
  it('TYPES_WEIGHTS[1] (Push) suppresses W.PULL at -6 (direct antagonists)', () => {
    expect(TYPES_WEIGHTS[1]?.suppressions[W.PULL]).toBe(-6);
  });
});

// ---------------------------------------------------------------------------
// computeRawVector() — output shape and primary weights
// ---------------------------------------------------------------------------

describe('computeRawVector() output shape', () => {
  it('returns a Float32Array', () => {
    const vec = computeRawVector(2, 1, 2, 3);
    expect(vec).toBeInstanceOf(Float32Array);
  });

  it('returns length 62 (slot 0 unused, slots 1-61 for W positions)', () => {
    const vec = computeRawVector(2, 1, 2, 3);
    expect(vec.length).toBe(62);
  });

  it('slot 0 is unused (value 0)', () => {
    const vec = computeRawVector(2, 1, 2, 3);
    expect(vec[0]).toBe(0);
  });
});

describe('computeRawVector(2,1,2,3) primary dial weights', () => {
  // zip 2-1-2-3 = ⛽ Strength (W.STRENGTH=2) + 🏛 Basics (W.BASICS=8) + 🪡 Pull (W.PULL=15) + 🔵 Structured (W.STRUCTURED=21)
  let vec: Float32Array;

  it('sets ⛽ Strength primary +8 at W.STRENGTH (slot 2)', () => {
    vec = computeRawVector(2, 1, 2, 3);
    expect(vec[W.STRENGTH]).toBe(8);
  });

  it('sets 🏛 Basics primary +8 at W.BASICS (slot 8)', () => {
    vec = computeRawVector(2, 1, 2, 3);
    expect(vec[W.BASICS]).toBe(8);
  });

  it('sets 🪡 Pull primary +8 at W.PULL (slot 15)', () => {
    vec = computeRawVector(2, 1, 2, 3);
    expect(vec[W.PULL]).toBe(8);
  });

  it('sets 🔵 Structured primary +8 at W.STRUCTURED (slot 21)', () => {
    vec = computeRawVector(2, 1, 2, 3);
    expect(vec[W.STRUCTURED]).toBe(8);
  });
});

describe('computeRawVector() clamping', () => {
  it('all output values are clamped to [-8, +8]', () => {
    // Test multiple zip codes
    const zips: [number, number, number, number][] = [
      [1, 1, 1, 1],
      [2, 1, 2, 3],
      [3, 2, 1, 5],
      [7, 3, 3, 8],
      [4, 4, 4, 4],
    ];

    for (const [o, a, t, c] of zips) {
      const vec = computeRawVector(o, a, t, c);
      for (let i = 1; i < 62; i++) {
        const val = vec[i] as number;
        expect(
          val >= -8 && val <= 8,
          `computeRawVector(${o},${a},${t},${c})[${i}] = ${val} — outside [-8, 8]`
        ).toBe(true);
      }
    }
  });
});
