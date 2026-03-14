/**
 * ParseResult — The contract type for all SCL parse output.
 *
 * ParseResult is the shape returned by the parser for any input string.
 * All downstream consumers (renderer, router, block selector, operator selector)
 * depend on this interface. It is defined here from day one to prevent
 * the breaking API change of retrofitting defaulted_dimensions later.
 *
 * DimensionGroup identifies which of the four zip code dials was defaulted
 * (not matched from user input) during parsing. An empty array means all four
 * dials were explicitly matched.
 */

export type DimensionGroup = 'order' | 'axis' | 'type' | 'color';

export interface ParseResult {
  /** The 4-emoji zip code string, e.g. '⛽🏛🪡🔵' */
  zip: string;

  /** The 4-digit numeric zip code string, e.g. '2123' */
  numericZip: string;

  /** Order dial position (1–7) */
  orderPos: number;

  /** Axis dial position (1–6) */
  axisPos: number;

  /** Type dial position (1–5) */
  typePos: number;

  /** Color dial position (1–8) */
  colorPos: number;

  /**
   * The resolved weight vector for this zip code.
   * Float32Array of length 62 (slot 0 unused, slots 1–61 for W positions).
   * Produced by resolveZip() — hard suppressions already applied.
   */
  weightVector: Float32Array;

  /**
   * Confidence score in [0, 1] for the parse.
   * 1.0 = all four dials explicitly matched.
   * Lower values indicate one or more dials were defaulted or inferred.
   */
  confidence: number;

  /**
   * Which dials were defaulted (not matched from user input).
   * Required — never optional. An empty array means no dimensions were defaulted.
   * Downstream consumers use this to surface "Did you mean...?" suggestions.
   */
  defaulted_dimensions: DimensionGroup[];

  /**
   * The raw terms from user input that were matched to produce this result.
   * Used for highlighting and debugging.
   */
  matchedTerms: string[];
}
