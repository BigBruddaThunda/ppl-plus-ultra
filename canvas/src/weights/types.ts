/**
 * Weight System Type Interfaces
 *
 * Core types for the SCL weight table system.
 * All weight values use coarse scale only: 0, +/-2, +/-4, +/-6, +/-8.
 * The full scale (-8 to +8) is defined in middle-math/weights/weight-system-spec.md
 * but only coarse values are used in the static tables.
 */

/**
 * Coarse weight scale — only these values are valid in static weight tables.
 * -8: Hard exclusion (rule says never)
 * -6: Contradicts the address (undermines zip code integrity)
 * -4: Suppressed (won't surface naturally)
 * -2: Noticeably absent / deprioritized
 *  0: Neutral
 * +2: Noticeable background presence
 * +4: Equal presence / balanced contributor
 * +6: Strong presence / shapes most decisions
 * +8: Defining / primary identity
 */
export type WeightScale = -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8;

/**
 * A single entry in a dial weight table.
 * - self: always +8 (primary dial identity)
 * - affinities: positive weight boosts for related W positions
 * - suppressions: negative weight penalties for conflicting W positions
 */
export interface WeightEntry {
  readonly self: 8;
  readonly affinities: Partial<Record<number, WeightScale>>;
  readonly suppressions: Partial<Record<number, WeightScale>>;
}

/**
 * A complete weight table for one dial category (keyed by dial position number).
 */
export interface DialWeightTable {
  [position: number]: WeightEntry;
}
