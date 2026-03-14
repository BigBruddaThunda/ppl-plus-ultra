/**
 * Scorer — Text-to-zip scoring pipeline for the SCL parser
 *
 * scoreText() is the primary entry point. It takes a natural language string
 * and returns ranked ParseResult candidates, with confidence scores and
 * fuzzy matching for typo tolerance and alias expansion.
 *
 * Pipeline stages:
 *   1. normalizeInput() — lowercase, unicode, strip punctuation
 *   2. tokenize() — unigrams + bigrams
 *   3. expandToken() — typo correction per token (edit distance)
 *   4. Keyword dict lookup — exact match on expanded tokens
 *   5. expandPhrase() — exercise alias matching on full input
 *   6. Accumulate dimension scores per DimensionId group
 *   7. Bigram override — bigrams win over unigrams for same dim group
 *   8. Collision suppression — collision_prone unigrams deferred when bigram exists
 *   9. Argmax per dimension group → best position for Order, Axis, Type, Color
 *  10. Default positions for unmatched groups → record defaulted_dimensions
 *  11. resolveZip() → weight vector
 *  12. Confidence = clamped score ratio
 *  13. Candidate generation for ambiguous dims → up to maxCandidates results
 */

import { normalizeInput, tokenize } from './tokenizer.js';
import { expandToken, expandPhrase } from './fuzzy.js';
import { resolveZip } from '../weights/resolver.js';
import { zipToEmoji } from './zip-converter.js';
import type { ParseResult, DimensionGroup } from './parse-result.js';
import type { KeywordEntry } from './keywords.js';
import type { ExerciseEntry } from './types.js';

import KEYWORDS_RAW from '../../data/dial-keywords.json' assert { type: 'json' };
import EXERCISES_RAW from '../../data/exercises.json' assert { type: 'json' };

const KEYWORDS = KEYWORDS_RAW as KeywordEntry[];
const EXERCISES = EXERCISES_RAW as ExerciseEntry[];

// ---------------------------------------------------------------------------
// Module-level singletons
// ---------------------------------------------------------------------------

/**
 * KEYWORD_MAP: term → KeywordEntry (exact-match lookup, built once)
 * When multiple entries exist for the same term, keep the highest affinity_score.
 */
const KEYWORD_MAP: Map<string, KeywordEntry> = (() => {
  const map = new Map<string, KeywordEntry>();
  for (const kw of KEYWORDS) {
    const existing = map.get(kw.term);
    if (!existing || kw.affinity_score > existing.affinity_score) {
      map.set(kw.term, kw);
    }
  }
  return map;
})();

/**
 * EXERCISE_TYPE_MAP: exercise name → scl_types[]
 * Built from exercises.json for alias-to-type mapping in expandPhrase() results.
 *
 * Uses first-write-wins so that when the same name appears multiple times
 * (e.g. "Romanian Deadlift (RDL)" appears as Pull+Plus, Pull+Legs, and Legs),
 * the first (most specific) entry is kept. This ensures RDL maps to Pull+Plus,
 * not the final Legs-only entry.
 */
const EXERCISE_TYPE_MAP: Map<string, string[]> = (() => {
  const map = new Map<string, string[]>();
  for (const ex of EXERCISES) {
    if (!map.has(ex.name)) {
      map.set(ex.name, ex.scl_types);
    }
    for (const alias of ex.aliases) {
      if (!map.has(alias)) {
        map.set(alias, ex.scl_types);
      }
    }
  }
  return map;
})();

// ---------------------------------------------------------------------------
// Dimension group constants
// ---------------------------------------------------------------------------

/** DimensionId ranges for each group (inclusive) */
const ORDER_DIMS = { min: 1, max: 7 };   // 7 Orders
const AXIS_DIMS  = { min: 8, max: 13 };  // 6 Axes
const TYPE_DIMS  = { min: 14, max: 18 }; // 5 Types
const COLOR_DIMS = { min: 19, max: 26 }; // 8 Colors

/** Default positions when a group has zero score */
const DEFAULTS = {
  order: 3, // Hypertrophy
  axis:  1, // Basics
  type:  1, // Push
  color: 3, // Structured
} as const;

/** SCL type name to dimension ID mapping */
const SCL_TYPE_TO_DIM: Record<string, number> = {
  'Push':  14,
  'Pull':  15,
  'Legs':  16,
  'Plus':  17,
  'Ultra': 18,
};

// ---------------------------------------------------------------------------
// Internal types
// ---------------------------------------------------------------------------

interface DimScores {
  order: Map<number, number>;
  axis:  Map<number, number>;
  type:  Map<number, number>;
  color: Map<number, number>;
}

/** Track which dimension groups have had a bigram match */
interface BigramFlags {
  order: boolean;
  axis:  boolean;
  type:  boolean;
  color: boolean;
}

// ---------------------------------------------------------------------------
// Helper functions
// ---------------------------------------------------------------------------

function getDimGroup(dim: number): DimensionGroup | null {
  if (dim >= ORDER_DIMS.min && dim <= ORDER_DIMS.max) return 'order';
  if (dim >= AXIS_DIMS.min  && dim <= AXIS_DIMS.max)  return 'axis';
  if (dim >= TYPE_DIMS.min  && dim <= TYPE_DIMS.max)  return 'type';
  if (dim >= COLOR_DIMS.min && dim <= COLOR_DIMS.max) return 'color';
  return null;
}

function getDimPosition(dim: number, group: DimensionGroup): number {
  switch (group) {
    case 'order': return dim - ORDER_DIMS.min + 1; // dim 1 → pos 1
    case 'axis':  return dim - AXIS_DIMS.min + 1;  // dim 8 → pos 1
    case 'type':  return dim - TYPE_DIMS.min + 1;  // dim 14 → pos 1
    case 'color': return dim - COLOR_DIMS.min + 1; // dim 19 → pos 1
  }
}

function argmax(scores: Map<number, number>): number | null {
  let bestPos: number | null = null;
  let bestScore = -Infinity;
  for (const [pos, score] of scores) {
    if (score > bestScore || (score === bestScore && bestPos !== null && pos < bestPos)) {
      bestScore = score;
      bestPos = pos;
    }
  }
  return bestPos;
}

function addScore(
  scores: DimScores,
  group: DimensionGroup,
  pos: number,
  value: number
): void {
  const map = scores[group];
  map.set(pos, (map.get(pos) ?? 0) + value);
}

// ---------------------------------------------------------------------------
// scoreText() — public API
// ---------------------------------------------------------------------------

/**
 * Convert natural language input to ranked ParseResult candidates.
 *
 * Returns up to maxCandidates results sorted by confidence descending.
 * Always returns at least one result (default positions when no match).
 *
 * @param input          Natural language query string
 * @param maxCandidates  Maximum number of candidates to return (default 5)
 * @returns              Ranked ParseResult[] sorted by confidence descending
 */
export function scoreText(input: string, maxCandidates = 5): ParseResult[] {
  // --- Stage 1–2: normalize and tokenize ---
  const normalized = normalizeInput(input);
  const tokens = tokenize(normalized);

  // --- Stage 3: expand tokens for typo correction ---
  // For each token, attempt fuzzy correction. Track both original and expanded.
  const expandedTokens: Array<{ original: string; expanded: string; isBigram: boolean }> = [];

  for (const token of tokens) {
    const isBigram = token.includes(' ');
    const expanded = expandToken(token);
    expandedTokens.push({
      original: token,
      expanded: expanded[0] ?? token,
      isBigram,
    });
  }

  // --- Stage 4–8: keyword scoring with bigram priority and collision suppression ---
  const scores: DimScores = {
    order: new Map(),
    axis:  new Map(),
    type:  new Map(),
    color: new Map(),
  };

  const bigramFlags: BigramFlags = {
    order: false,
    axis:  false,
    type:  false,
    color: false,
  };

  const matchedTerms: string[] = [];

  // Two-pass: first collect bigram matches, then unigrams with collision check

  // Pass 1: bigrams only
  for (const { expanded, isBigram } of expandedTokens) {
    if (!isBigram) continue;

    const kw = KEYWORD_MAP.get(expanded);
    if (!kw) continue;

    const group = getDimGroup(kw.dimension);
    if (!group) continue;

    const pos = getDimPosition(kw.dimension, group);
    addScore(scores, group, pos, kw.affinity_score);
    bigramFlags[group] = true;

    if (!matchedTerms.includes(expanded)) {
      matchedTerms.push(expanded);
    }
  }

  // Pass 2: unigrams — skip collision_prone tokens when bigram exists for that group
  for (const { expanded, isBigram } of expandedTokens) {
    if (isBigram) continue;

    const kw = KEYWORD_MAP.get(expanded);
    if (!kw) continue;

    const group = getDimGroup(kw.dimension);
    if (!group) continue;

    // Skip collision-prone unigram if bigram exists for this dimension group
    if (kw.collision_prone && bigramFlags[group]) continue;

    const pos = getDimPosition(kw.dimension, group);
    addScore(scores, group, pos, kw.affinity_score);

    if (!matchedTerms.includes(expanded)) {
      matchedTerms.push(expanded);
    }
  }

  // --- Stage 5: expandPhrase() for exercise alias matching ---
  // Only use top 3 phrase matches to avoid keyword-pollution from fuzzy matches.
  // For example, "leg press" fuse.js returns 96 exercises (many Push types from
  // "press" substring), which would overwhelm the bigram keyword match.
  // The keyword dict already handles multi-word terms with bigrams — expandPhrase()
  // is specifically for abbreviations and short-form aliases (RDL, OHP, etc.)
  // where no keyword dict entry exists.
  const phraseMatches = expandPhrase(input).slice(0, 3);

  for (const exerciseName of phraseMatches) {
    const sclTypes = EXERCISE_TYPE_MAP.get(exerciseName);
    if (!sclTypes) continue;

    for (const sclType of sclTypes) {
      const dim = SCL_TYPE_TO_DIM[sclType];
      if (dim === undefined) continue;

      const group = getDimGroup(dim);
      if (!group || group !== 'type') continue;

      const pos = getDimPosition(dim, group);
      // Use a moderate score for alias-derived type matching
      addScore(scores, group, pos, 5);
    }

    if (!matchedTerms.includes(exerciseName)) {
      matchedTerms.push(exerciseName);
    }
  }

  // --- Stage 9–10: select best position per group, track defaults ---
  const defaulted_dimensions: DimensionGroup[] = [];

  const selectPos = (group: DimensionGroup): number => {
    const best = argmax(scores[group]);
    if (best === null) {
      defaulted_dimensions.push(group);
      return DEFAULTS[group];
    }
    return best;
  };

  const orderPos = selectPos('order');
  const axisPos  = selectPos('axis');
  const typePos  = selectPos('type');
  const colorPos = selectPos('color');

  // --- Stage 11: resolveZip() for weight vector ---
  const weightVector = resolveZip(orderPos, axisPos, typePos, colorPos);

  // --- Stage 12: compute confidence ---
  const inputTokenCount = tokens.length || 1;
  const totalMatchedScore = matchedTerms.length > 0
    ? Array.from(scores.order.values()).reduce((a, b) => a + b, 0) +
      Array.from(scores.axis.values()).reduce((a, b) => a + b, 0) +
      Array.from(scores.type.values()).reduce((a, b) => a + b, 0) +
      Array.from(scores.color.values()).reduce((a, b) => a + b, 0)
    : 0;

  const rawConfidence = totalMatchedScore / (inputTokenCount * 8);
  const confidence = Math.min(1, Math.max(0, rawConfidence));

  // Zero match case: confidence exactly 0 when no keywords matched at all
  const hasAnyMatch = matchedTerms.length > 0;
  const finalConfidence = hasAnyMatch ? confidence : 0;

  // --- Stage 13: build primary ParseResult ---
  const numericZip = `${orderPos}${axisPos}${typePos}${colorPos}`;
  const zip = zipToEmoji(numericZip);

  const primary: ParseResult = {
    zip,
    numericZip,
    orderPos,
    axisPos,
    typePos,
    colorPos,
    weightVector,
    confidence: finalConfidence,
    defaulted_dimensions,
    matchedTerms,
  };

  // --- Stage 14: generate candidates for ambiguous inputs ---
  if (!hasAnyMatch || finalConfidence === 0) {
    // No matches — return only the default result
    return [primary];
  }

  // Build candidate set by varying top-2 positions for any ambiguous group
  const candidates: ParseResult[] = [primary];

  const tryAddCandidate = (
    oPos: number,
    aPos: number,
    tPos: number,
    cPos: number
  ): void => {
    if (candidates.length >= maxCandidates) return;

    const nz = `${oPos}${aPos}${tPos}${cPos}`;
    // Don't duplicate the primary
    if (nz === numericZip) return;
    // Don't duplicate any existing candidate
    if (candidates.some(c => c.numericZip === nz)) return;

    const wv = resolveZip(oPos, aPos, tPos, cPos);
    const z = zipToEmoji(nz);

    // Confidence for alternate candidates — slightly lower than primary
    const altConf = Math.max(0, finalConfidence * 0.8);

    candidates.push({
      zip: z,
      numericZip: nz,
      orderPos: oPos,
      axisPos: aPos,
      typePos: tPos,
      colorPos: cPos,
      weightVector: wv,
      confidence: altConf,
      defaulted_dimensions: defaulted_dimensions.slice(),
      matchedTerms,
    });
  };

  // Try top-2 positions for each group
  const top2 = (group: DimensionGroup): number[] => {
    const map = scores[group];
    if (map.size === 0) return [DEFAULTS[group]];

    const sorted = Array.from(map.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 2)
      .map(([pos]) => pos);

    return sorted;
  };

  const orderCandidates = top2('order');
  const axisCandidates  = top2('axis');
  const typeCandidates  = top2('type');
  const colorCandidates = top2('color');

  for (const o of orderCandidates) {
    for (const a of axisCandidates) {
      for (const t of typeCandidates) {
        for (const c of colorCandidates) {
          tryAddCandidate(o, a, t, c);
          if (candidates.length >= maxCandidates) break;
        }
        if (candidates.length >= maxCandidates) break;
      }
      if (candidates.length >= maxCandidates) break;
    }
    if (candidates.length >= maxCandidates) break;
  }

  // Sort by confidence descending
  candidates.sort((a, b) => b.confidence - a.confidence);

  return candidates.slice(0, maxCandidates);
}
