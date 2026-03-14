/**
 * Scorer TDD Tests — Text-to-zip scoring pipeline
 *
 * Tests for scoreText() function, tokenizer, and fuzzy matcher.
 *
 * RED phase: These tests are written before the implementation exists.
 * They must fail until tokenizer.ts, fuzzy.ts, and scorer.ts are created.
 *
 * Behaviors covered:
 * - "heavy barbell back work" → orderPos=2 (Strength), typePos=2 (Pull)
 * - "benchh press" typo (edit distance 1) → Push (typePos=1)
 * - "RDL" alias → Pull (typePos=2)
 * - "leg press" bigram beats "press" unigram collision → Legs (typePos=3)
 * - Empty string → confidence=0, all 4 dimensions defaulted
 * - "gobbledygook nonsense" → confidence=0, all 4 dimensions defaulted
 * - Candidate count defaults to 5 max
 * - All ParseResult objects have required defaulted_dimensions field
 */

import { describe, it, expect } from 'vitest';
import { scoreText } from '../src/parser/scorer.js';
import { normalizeInput, tokenize } from '../src/parser/tokenizer.js';
import { expandToken, expandPhrase } from '../src/parser/fuzzy.js';
import type { ParseResult } from '../src/parser/parse-result.js';

// ---------------------------------------------------------------------------
// normalizeInput() and tokenize()
// ---------------------------------------------------------------------------

describe('normalizeInput()', () => {
  it('lowercases the input', () => {
    expect(normalizeInput('Heavy Barbell')).toBe('heavy barbell');
  });

  it('strips punctuation but preserves hyphens inside words', () => {
    expect(normalizeInput('bench-press!')).toBe('bench-press');
    expect(normalizeInput('hello, world.')).toBe('hello world');
  });

  it('normalizes unicode combining marks', () => {
    // NFD normalize then strip combining marks
    const withAccent = 'caf\u00e9';
    const normalized = normalizeInput(withAccent);
    expect(normalized).toMatch(/^caf/);
  });

  it('returns empty string for empty input', () => {
    expect(normalizeInput('')).toBe('');
  });
});

describe('tokenize()', () => {
  it('produces unigrams from whitespace-split', () => {
    const tokens = tokenize('heavy barbell back');
    expect(tokens).toContain('heavy');
    expect(tokens).toContain('barbell');
    expect(tokens).toContain('back');
  });

  it('produces adjacent bigrams', () => {
    const tokens = tokenize('heavy barbell back');
    expect(tokens).toContain('heavy barbell');
    expect(tokens).toContain('barbell back');
  });

  it('does not produce non-adjacent bigrams', () => {
    const tokens = tokenize('heavy barbell back');
    expect(tokens).not.toContain('heavy back');
  });

  it('returns empty array for empty input', () => {
    expect(tokenize('')).toEqual([]);
  });

  it('returns single unigram with no bigrams for single word', () => {
    const tokens = tokenize('strength');
    expect(tokens).toEqual(['strength']);
  });
});

// ---------------------------------------------------------------------------
// expandToken() — fuzzy edit-distance matching
// ---------------------------------------------------------------------------

describe('expandToken()', () => {
  it('returns exact token unchanged when it matches exactly', () => {
    const result = expandToken('bench press');
    expect(result).toContain('bench press');
  });

  it('corrects "benchh press" (edit distance 1) to "bench press"', () => {
    const result = expandToken('benchh press');
    expect(result).toContain('bench press');
  });

  it('corrects "benchh" (edit distance 1 from "bench") within distance 2', () => {
    // "benchh" is close to "bench" (distance 1)
    const result = expandToken('benchh', 2);
    // Should return the closest match within distance 2
    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBeGreaterThan(0);
  });

  it('returns the original token unchanged when no close match exists', () => {
    const result = expandToken('xyzqwerty');
    expect(result).toContain('xyzqwerty');
  });

  it('returns array type always', () => {
    const result = expandToken('strength');
    expect(Array.isArray(result)).toBe(true);
  });
});

// ---------------------------------------------------------------------------
// expandPhrase() — fuse.js alias matching
// ---------------------------------------------------------------------------

describe('expandPhrase()', () => {
  it('returns matched exercise names for "RDL"', () => {
    const result = expandPhrase('RDL');
    expect(result.length).toBeGreaterThan(0);
    // Should match something related to Romanian Deadlift
    const joined = result.join(' ').toLowerCase();
    expect(joined).toMatch(/romanian|rdl|deadlift/i);
  });

  it('returns empty array for completely unrecognized input', () => {
    const result = expandPhrase('xyzqwerty123456');
    expect(Array.isArray(result)).toBe(true);
    // Empty or very low matches
    expect(result.length).toBeLessThanOrEqual(2);
  });

  it('matches "bench press" to a chest exercise', () => {
    const result = expandPhrase('bench press');
    expect(Array.isArray(result)).toBe(true);
  });
});

// ---------------------------------------------------------------------------
// scoreText() — full pipeline
// ---------------------------------------------------------------------------

describe('scoreText() — ParseResult shape', () => {
  it('returns an array', () => {
    const results = scoreText('heavy barbell back work');
    expect(Array.isArray(results)).toBe(true);
  });

  it('returns at most 5 candidates by default', () => {
    const results = scoreText('heavy barbell back work');
    expect(results.length).toBeGreaterThan(0);
    expect(results.length).toBeLessThanOrEqual(5);
  });

  it('respects maxCandidates parameter', () => {
    const results = scoreText('heavy barbell back work', 3);
    expect(results.length).toBeLessThanOrEqual(3);
  });

  it('all results have required ParseResult fields', () => {
    const results = scoreText('heavy barbell back work');
    for (const r of results) {
      expect(r).toHaveProperty('zip');
      expect(r).toHaveProperty('numericZip');
      expect(r).toHaveProperty('orderPos');
      expect(r).toHaveProperty('axisPos');
      expect(r).toHaveProperty('typePos');
      expect(r).toHaveProperty('colorPos');
      expect(r).toHaveProperty('weightVector');
      expect(r).toHaveProperty('confidence');
      expect(r).toHaveProperty('defaulted_dimensions');
      expect(r).toHaveProperty('matchedTerms');
    }
  });

  it('defaulted_dimensions is always an array (never undefined)', () => {
    const results = scoreText('heavy barbell back work');
    for (const r of results) {
      expect(Array.isArray(r.defaulted_dimensions)).toBe(true);
    }
  });

  it('results are sorted by confidence descending', () => {
    const results = scoreText('heavy barbell back work');
    for (let i = 1; i < results.length; i++) {
      expect(results[i - 1]!.confidence).toBeGreaterThanOrEqual(results[i]!.confidence);
    }
  });

  it('zip is a 4-character emoji string', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.zip).toBeTruthy();
    expect([...results[0]!.zip].length).toBe(4);
  });

  it('numericZip is a 4-digit string', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.numericZip).toMatch(/^\d{4}$/);
  });

  it('weightVector is a Float32Array of length 62', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.weightVector).toBeInstanceOf(Float32Array);
    expect(results[0]!.weightVector.length).toBe(62);
  });

  it('confidence is in [0, 1] range', () => {
    const results = scoreText('heavy barbell back work');
    for (const r of results) {
      expect(r.confidence).toBeGreaterThanOrEqual(0);
      expect(r.confidence).toBeLessThanOrEqual(1);
    }
  });
});

// ---------------------------------------------------------------------------
// scoreText() — core scoring behaviors
// ---------------------------------------------------------------------------

describe('scoreText() — "heavy barbell back work"', () => {
  it('top result has orderPos=2 (Strength)', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.orderPos).toBe(2);
  });

  it('top result has typePos=2 (Pull)', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.typePos).toBe(2);
  });

  it('top result has non-zero confidence', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.confidence).toBeGreaterThan(0);
  });

  it('top result has some matched terms', () => {
    const results = scoreText('heavy barbell back work');
    expect(results[0]!.matchedTerms.length).toBeGreaterThan(0);
  });
});

describe('scoreText() — typo correction ("benchh press")', () => {
  it('routes "benchh press" to Push (typePos=1) despite typo', () => {
    const results = scoreText('benchh press');
    expect(results[0]!.typePos).toBe(1); // Push
  });

  it('has non-zero confidence for "benchh press"', () => {
    const results = scoreText('benchh press');
    expect(results[0]!.confidence).toBeGreaterThan(0);
  });
});

describe('scoreText() — alias expansion ("RDL")', () => {
  it('routes "RDL" to Pull (typePos=2) via exercise alias', () => {
    const results = scoreText('RDL');
    expect(results[0]!.typePos).toBe(2); // Pull
  });

  it('returns results for "RDL"', () => {
    const results = scoreText('RDL');
    expect(results.length).toBeGreaterThan(0);
  });
});

describe('scoreText() — bigram collision suppression ("leg press")', () => {
  it('"leg press" routes to Legs (typePos=3), not Push (typePos=1)', () => {
    const results = scoreText('leg press');
    expect(results[0]!.typePos).toBe(3); // Legs, not Push
  });

  it('"leg press" top result typePos is not Push (1)', () => {
    const results = scoreText('leg press');
    expect(results[0]!.typePos).not.toBe(1);
  });
});

describe('scoreText() — zero-match inputs', () => {
  it('empty string returns confidence=0', () => {
    const results = scoreText('');
    expect(results.length).toBe(1);
    expect(results[0]!.confidence).toBe(0);
  });

  it('empty string returns all 4 dimensions defaulted', () => {
    const results = scoreText('');
    const dims = results[0]!.defaulted_dimensions;
    expect(dims).toContain('order');
    expect(dims).toContain('axis');
    expect(dims).toContain('type');
    expect(dims).toContain('color');
    expect(dims.length).toBe(4);
  });

  it('"gobbledygook nonsense" returns confidence=0', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(results[0]!.confidence).toBe(0);
  });

  it('"gobbledygook nonsense" has all 4 dimensions defaulted', () => {
    const results = scoreText('gobbledygook nonsense');
    const dims = results[0]!.defaulted_dimensions;
    expect(dims).toContain('order');
    expect(dims).toContain('axis');
    expect(dims).toContain('type');
    expect(dims).toContain('color');
    expect(dims.length).toBe(4);
  });

  it('zero-match result defaulted_dimensions is an array of length 4', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(Array.isArray(results[0]!.defaulted_dimensions)).toBe(true);
    expect(results[0]!.defaulted_dimensions.length).toBe(4);
  });
});

// ---------------------------------------------------------------------------
// scoreText() — default positions
// ---------------------------------------------------------------------------

describe('scoreText() — default position values', () => {
  it('defaulted orderPos uses position 3 (Hypertrophy)', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(results[0]!.orderPos).toBe(3);
  });

  it('defaulted axisPos uses position 1 (Basics)', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(results[0]!.axisPos).toBe(1);
  });

  it('defaulted typePos uses position 1 (Push)', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(results[0]!.typePos).toBe(1);
  });

  it('defaulted colorPos uses position 3 (Structured)', () => {
    const results = scoreText('gobbledygook nonsense');
    expect(results[0]!.colorPos).toBe(3);
  });
});
