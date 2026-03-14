/**
 * Keyword Dictionary Types — Vocabulary Bridge Layer
 *
 * Maps natural language fitness terms to SCL zip code dimensions (W positions 1-26).
 * Dimensions 1-7  = Orders
 * Dimensions 8-13 = Axes
 * Dimensions 14-18 = Types
 * Dimensions 19-26 = Colors
 *
 * Blocks (27-60) and Operators (27-38 in W enum) are NOT keyword dimensions.
 */

// ---------------------------------------------------------------------------
// DimensionId — valid W positions for the 4 zip dials only
// ---------------------------------------------------------------------------

export type DimensionId =
  | 1 | 2 | 3 | 4 | 5 | 6 | 7       // Orders: Foundation, Strength, Hypertrophy, Performance, Full Body, Balance, Restoration
  | 8 | 9 | 10 | 11 | 12 | 13       // Axes:   Basics, Functional, Aesthetic, Challenge, Time, Partner
  | 14 | 15 | 16 | 17 | 18          // Types:  Push, Pull, Legs, Plus, Ultra
  | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26;  // Colors: Teaching, Bodyweight, Structured, Technical, Intense, Circuit, Fun, Mindful

// ---------------------------------------------------------------------------
// KeywordEntry — single dictionary entry
// ---------------------------------------------------------------------------

export interface KeywordEntry {
  term: string;
  dimension: DimensionId;
  affinity_score: number;   // 1-8 positive only; 8 = unambiguous, 1 = weak/contextual
  collision_prone: boolean; // true if this single word is ambiguous across multiple dimensions
  source: 'first-party' | 'voice-seed';
}

// ---------------------------------------------------------------------------
// Valid dimension range for guard use
// ---------------------------------------------------------------------------

export const VALID_DIMENSIONS: readonly DimensionId[] = [
  1, 2, 3, 4, 5, 6, 7,
  8, 9, 10, 11, 12, 13,
  14, 15, 16, 17, 18,
  19, 20, 21, 22, 23, 24, 25, 26,
] as const;

export const VALID_SOURCES: readonly string[] = ['first-party', 'voice-seed'] as const;
