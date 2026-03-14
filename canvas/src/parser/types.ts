/**
 * Parser Types — Exercise Dictionary and Keyword Entry Interfaces
 *
 * ExerciseEntry: Typed interface for exercises.json entries.
 * Sourced from middle-math/exercise-library.json with dropped fields
 * (order_relevance, axis_emphasis) and added alias layer.
 *
 * KeywordEntry will be added in Plan 02-03 (keyword dictionary).
 */

export interface ExerciseEntry {
  id: number;
  section: string;                  // "A"–"Q"
  name: string;                     // canonical: "Romanian Deadlift (RDL)"
  scl_types: string[];              // ["Pull", "Plus"] — valid values: Push Pull Legs Plus Ultra
  equipment_tier: [number, number]; // [min, max] inclusive tier range
  gold_gated: boolean;
  movement_pattern: string;
  muscle_groups: string;
  bilateral: boolean;
  compound: boolean;
  aliases: string[];                // auto-derived + manual entries
}
