/**
 * keyword-dict.test.ts
 *
 * Tests for dial-keywords.json — the vocabulary bridge layer.
 * All 26 dial dimensions (W positions 1-26) must be covered.
 * >= 2,000 total entries required.
 *
 * TDD RED: These tests fail until Task 2 populates the dictionary.
 */

import { describe, it, expect } from 'vitest';
import type { KeywordEntry, DimensionId } from '../src/parser/keywords';
import { VALID_DIMENSIONS, VALID_SOURCES } from '../src/parser/keywords';
import keywords from '../data/dial-keywords.json';

// Cast imported JSON to typed array
const dict = keywords as KeywordEntry[];

// ---------------------------------------------------------------------------
// Size constraints
// ---------------------------------------------------------------------------

describe('dial-keywords.json — size', () => {
  it('has >= 2,000 entries', () => {
    expect(dict.length).toBeGreaterThanOrEqual(2000);
  });
});

// ---------------------------------------------------------------------------
// Schema validation
// ---------------------------------------------------------------------------

describe('dial-keywords.json — schema', () => {
  it('every entry has required fields: term, dimension, affinity_score, collision_prone, source', () => {
    for (const entry of dict) {
      expect(entry).toHaveProperty('term');
      expect(entry).toHaveProperty('dimension');
      expect(entry).toHaveProperty('affinity_score');
      expect(entry).toHaveProperty('collision_prone');
      expect(entry).toHaveProperty('source');
    }
  });

  it('all dimension values are valid DimensionId (1-26 only)', () => {
    const validSet = new Set<number>(VALID_DIMENSIONS);
    for (const entry of dict) {
      expect(validSet.has(entry.dimension as number)).toBe(true);
    }
  });

  it('all affinity_score values are in range 1-8 (no zeros or negatives)', () => {
    for (const entry of dict) {
      expect(entry.affinity_score).toBeGreaterThanOrEqual(1);
      expect(entry.affinity_score).toBeLessThanOrEqual(8);
    }
  });

  it('source field is either "first-party" or "voice-seed" only', () => {
    const validSourceSet = new Set(VALID_SOURCES);
    for (const entry of dict) {
      expect(validSourceSet.has(entry.source)).toBe(true);
    }
  });
});

// ---------------------------------------------------------------------------
// Specific term routing
// ---------------------------------------------------------------------------

describe('dial-keywords.json — specific term routing', () => {
  it('"strength" maps to dimension 2 (W.STRENGTH) with affinity_score >= 6', () => {
    const entry = dict.find(e => e.term === 'strength');
    expect(entry).toBeDefined();
    expect(entry?.dimension).toBe(2);
    expect(entry?.affinity_score).toBeGreaterThanOrEqual(6);
  });

  it('"chest" maps to dimension 14 (W.PUSH)', () => {
    const entry = dict.find(e => e.term === 'chest');
    expect(entry).toBeDefined();
    expect(entry?.dimension).toBe(14);
  });

  it('"lats" or "latissimus" maps to dimension 15 (W.PULL)', () => {
    const lats = dict.find(e => e.term === 'lats');
    const latissimus = dict.find(e => e.term === 'latissimus');
    const found = lats ?? latissimus;
    expect(found).toBeDefined();
    expect(found?.dimension).toBe(15);
  });

  it('"barbell" maps to a Color dimension (19-26) representing tier 3 equipment', () => {
    const entry = dict.find(e => e.term === 'barbell');
    expect(entry).toBeDefined();
    const dim = entry?.dimension as number;
    expect(dim).toBeGreaterThanOrEqual(19);
    expect(dim).toBeLessThanOrEqual(26);
  });

  it('"bodyweight" or "calisthenics" maps to dimension 20 (W.BODYWEIGHT)', () => {
    const bw = dict.find(e => e.term === 'bodyweight');
    const cali = dict.find(e => e.term === 'calisthenics');
    const found = bw ?? cali;
    expect(found).toBeDefined();
    expect(found?.dimension).toBe(20);
  });

  it('"HIIT" or "intervals" maps to dimension 18 (W.ULTRA)', () => {
    const hiit = dict.find(e => e.term.toLowerCase() === 'hiit');
    const intervals = dict.find(e => e.term === 'intervals');
    const found = hiit ?? intervals;
    expect(found).toBeDefined();
    expect(found?.dimension).toBe(18);
  });
});

// ---------------------------------------------------------------------------
// Collision flagging
// ---------------------------------------------------------------------------

describe('dial-keywords.json — collision flagging', () => {
  const collisionWords = ['heavy', 'light', 'press', 'row', 'power', 'hard', 'easy', 'pump', 'strength'];

  it('at least 5 collision-prone words are flagged with collision_prone: true', () => {
    const flaggedCount = collisionWords.filter(word => {
      const entry = dict.find(e => e.term === word);
      return entry?.collision_prone === true;
    }).length;
    expect(flaggedCount).toBeGreaterThanOrEqual(5);
  });
});

// ---------------------------------------------------------------------------
// Coverage — every DimensionId has >= 10 entries
// ---------------------------------------------------------------------------

describe('dial-keywords.json — dimension coverage', () => {
  it('every DimensionId (1-26) has at least 10 keyword entries', () => {
    for (const dim of VALID_DIMENSIONS) {
      const count = dict.filter(e => e.dimension === dim).length;
      expect(count, `Dimension ${dim} has only ${count} entries (need >= 10)`).toBeGreaterThanOrEqual(10);
    }
  });
});

// ---------------------------------------------------------------------------
// Deduplication
// ---------------------------------------------------------------------------

describe('dial-keywords.json — deduplication', () => {
  it('no duplicate terms exist in the dictionary', () => {
    const terms = dict.map(e => e.term);
    const uniqueTerms = new Set(terms);
    expect(uniqueTerms.size).toBe(terms.length);
  });
});
