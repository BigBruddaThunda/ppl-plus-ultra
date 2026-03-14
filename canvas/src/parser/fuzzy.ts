/**
 * Fuzzy Matcher — Edit-distance and phrase-based fuzzy matching for the SCL parser
 *
 * Two matching strategies:
 *
 * 1. expandToken() — Single-token typo correction using fastest-levenshtein.
 *    Built from the flat corpus of all keyword terms + exercise aliases.
 *    Corrects typos like "benchh press" → "bench press" (edit distance 1).
 *
 * 2. expandPhrase() — Multi-word / short-form alias matching using fuse.js.
 *    Built from the exercise library (name + aliases fields).
 *    Expands abbreviations like "RDL" → "Romanian Deadlift (RDL)".
 *
 * Both use module-level singletons built once at import time.
 */

import { closest, distance } from 'fastest-levenshtein';
import Fuse from 'fuse.js';
import type { ExerciseEntry } from './types.js';

import KEYWORDS_RAW from '../../data/dial-keywords.json' assert { type: 'json' };
import EXERCISES_RAW from '../../data/exercises.json' assert { type: 'json' };

const KEYWORDS = KEYWORDS_RAW as Array<{ term: string; dimension: number; affinity_score: number; collision_prone: boolean; source: string }>;
const EXERCISES = EXERCISES_RAW as ExerciseEntry[];

// ---------------------------------------------------------------------------
// Module-level singletons (built once at import time, never rebuilt per-call)
// ---------------------------------------------------------------------------

/**
 * ALL_TERMS: flat corpus for edit-distance matching.
 * Contains all keyword terms + all exercise names + all exercise aliases.
 * Deduplicated to avoid redundant closest() candidates.
 */
const ALL_TERMS: string[] = (() => {
  const seen = new Set<string>();
  const terms: string[] = [];

  for (const kw of KEYWORDS) {
    if (!seen.has(kw.term)) {
      seen.add(kw.term);
      terms.push(kw.term);
    }
  }

  for (const ex of EXERCISES) {
    if (!seen.has(ex.name)) {
      seen.add(ex.name);
      terms.push(ex.name);
    }
    for (const alias of ex.aliases) {
      if (!seen.has(alias)) {
        seen.add(alias);
        terms.push(alias);
      }
    }
  }

  return terms;
})();

/**
 * FUSE_INSTANCE: fuse.js index over exercise name and aliases.
 * Config: threshold 0.4, minMatchCharLength 3, keys: name + aliases.
 * Built once at module load.
 */
const FUSE_INSTANCE = new Fuse(EXERCISES, {
  threshold: 0.4,
  minMatchCharLength: 3,
  keys: ['name', 'aliases'],
  includeScore: false,
});

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Expand a single token using edit-distance typo correction.
 *
 * Uses fastest-levenshtein to find the closest term in ALL_TERMS.
 * If the closest term is within maxDistance (default 2), returns [closestTerm].
 * Otherwise returns [token] unchanged.
 *
 * @param token        The input token to correct
 * @param maxDistance  Maximum edit distance to accept (default 2)
 * @returns            Array with either the corrected term or the original token
 */
export function expandToken(token: string, maxDistance = 2): string[] {
  if (!token) return [token];

  // Fast path: if the token exactly exists in ALL_TERMS, return immediately
  // This avoids the closest() scan overhead for known-good terms
  if (ALL_TERMS.includes(token)) {
    return [token];
  }

  const best = closest(token, ALL_TERMS);
  const dist = distance(token, best);

  if (dist <= maxDistance) {
    return [best];
  }

  return [token];
}

/**
 * Expand a phrase using fuse.js exercise alias matching.
 *
 * Searches for the phrase in exercise names and aliases using fuse.js
 * fuzzy matching. Returns the canonical exercise names for matches found.
 *
 * Used for abbreviations and short-form aliases like "RDL" → "Romanian Deadlift (RDL)".
 *
 * @param phrase  The phrase to search for in exercise aliases
 * @returns       Array of matched exercise names (may be empty if no match)
 */
export function expandPhrase(phrase: string): string[] {
  if (!phrase || phrase.length < 2) return [];

  const results = FUSE_INSTANCE.search(phrase);
  return results.map(r => r.item.name);
}
