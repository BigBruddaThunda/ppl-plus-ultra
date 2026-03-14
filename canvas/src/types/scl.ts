/**
 * SCL Primitive Types — The Ppl± Phonebook
 *
 * All 61 SCL emojis defined as const objects with reverse indexes.
 * Sourced from CLAUDE.md canonical tables. ONE consistent pattern throughout.
 *
 * This file contains NO priority, constraint, or hierarchy logic.
 * The constraint hierarchy (Order > Color > Axis > Type) lives in the resolver (Phase 3).
 * The experience hierarchy (Axis > Color > Order > Type) lives in the visual canvas (Session 3+).
 */

// ---------------------------------------------------------------------------
// Shape
// ---------------------------------------------------------------------------

export interface SclEntry {
  readonly emoji: string;
  readonly name: string;
  readonly slug: string;
}

export interface OperatorEntry extends SclEntry {
  readonly latin: string;
}

export interface BlockEntry extends SclEntry {
  readonly role: 'orientation' | 'access' | 'transformation' | 'retention' | 'modifier';
}

// ---------------------------------------------------------------------------
// Dials (26 emojis — the 4 zip code positions)
// ---------------------------------------------------------------------------

export const ORDERS = {
  1: { emoji: '🐂', name: 'Foundation', slug: 'foundation' },
  2: { emoji: '⛽', name: 'Strength', slug: 'strength' },
  3: { emoji: '🦋', name: 'Hypertrophy', slug: 'hypertrophy' },
  4: { emoji: '🏟', name: 'Performance', slug: 'performance' },
  5: { emoji: '🌾', name: 'Full Body', slug: 'full-body' },
  6: { emoji: '⚖', name: 'Balance', slug: 'balance' },
  7: { emoji: '🖼', name: 'Restoration', slug: 'restoration' },
} as const satisfies Record<number, SclEntry>;

export const AXES = {
  1: { emoji: '🏛', name: 'Basics', slug: 'basics' },
  2: { emoji: '🔨', name: 'Functional', slug: 'functional' },
  3: { emoji: '🌹', name: 'Aesthetic', slug: 'aesthetic' },
  4: { emoji: '🪐', name: 'Challenge', slug: 'challenge' },
  5: { emoji: '⌛', name: 'Time', slug: 'time' },
  6: { emoji: '🐬', name: 'Partner', slug: 'partner' },
} as const satisfies Record<number, SclEntry>;

export const TYPES = {
  1: { emoji: '🛒', name: 'Push', slug: 'push' },
  2: { emoji: '🪡', name: 'Pull', slug: 'pull' },
  3: { emoji: '🍗', name: 'Legs', slug: 'legs' },
  4: { emoji: '➕', name: 'Plus', slug: 'plus' },
  5: { emoji: '➖', name: 'Ultra', slug: 'ultra' },
} as const satisfies Record<number, SclEntry>;

export const COLORS = {
  1: { emoji: '⚫', name: 'Teaching', slug: 'teaching' },
  2: { emoji: '🟢', name: 'Bodyweight', slug: 'bodyweight' },
  3: { emoji: '🔵', name: 'Structured', slug: 'structured' },
  4: { emoji: '🟣', name: 'Technical', slug: 'technical' },
  5: { emoji: '🔴', name: 'Intense', slug: 'intense' },
  6: { emoji: '🟠', name: 'Circuit', slug: 'circuit' },
  7: { emoji: '🟡', name: 'Fun', slug: 'fun' },
  8: { emoji: '⚪', name: 'Mindful', slug: 'mindful' },
} as const satisfies Record<number, SclEntry>;

// ---------------------------------------------------------------------------
// Operators (12 emojis — CLAUDE.md canonical, NOT zip_converter.py)
// ---------------------------------------------------------------------------

export const OPERATORS = {
  1:  { emoji: '🧲', name: 'Capio',  slug: 'capio',  latin: 'capio' },
  2:  { emoji: '🐋', name: 'Duco',   slug: 'duco',   latin: 'duco' },
  3:  { emoji: '🤌', name: 'Facio',  slug: 'facio',  latin: 'facio' },
  4:  { emoji: '🧸', name: 'Fero',   slug: 'fero',   latin: 'fero' },
  5:  { emoji: '✒️', name: 'Grapho', slug: 'grapho', latin: 'grapho' },
  6:  { emoji: '🦉', name: 'Logos',  slug: 'logos',  latin: 'logos' },
  7:  { emoji: '🚀', name: 'Mitto',  slug: 'mitto',  latin: 'mitto' },
  8:  { emoji: '🦢', name: 'Plico',  slug: 'plico',  latin: 'plico' },
  9:  { emoji: '📍', name: 'Pono',   slug: 'pono',   latin: 'pono' },
  10: { emoji: '👀', name: 'Specio', slug: 'specio', latin: 'specio' },
  11: { emoji: '🥨', name: 'Tendo',  slug: 'tendo',  latin: 'tendo' },
  12: { emoji: '🪵', name: 'Teneo',  slug: 'teneo',  latin: 'teneo' },
} as const satisfies Record<number, OperatorEntry>;

// ---------------------------------------------------------------------------
// Blocks (22 emojis)
// ---------------------------------------------------------------------------

export const BLOCKS = {
  1:  { emoji: '♨️', name: 'Warm-Up',       slug: 'warm-up',       role: 'orientation' },
  2:  { emoji: '🎯', name: 'Intention',      slug: 'intention',     role: 'orientation' },
  3:  { emoji: '🔢', name: 'Fundamentals',   slug: 'fundamentals',  role: 'access' },
  4:  { emoji: '🧈', name: 'Bread & Butter', slug: 'bread-butter',  role: 'transformation' },
  5:  { emoji: '🫀', name: 'Circulation',    slug: 'circulation',   role: 'access' },
  6:  { emoji: '▶️', name: 'Primer',         slug: 'primer',        role: 'access' },
  7:  { emoji: '🎼', name: 'Composition',    slug: 'composition',   role: 'transformation' },
  8:  { emoji: '♟️', name: 'Gambit',         slug: 'gambit',        role: 'access' },
  9:  { emoji: '🪜', name: 'Progression',    slug: 'progression',   role: 'access' },
  10: { emoji: '🌎', name: 'Exposure',       slug: 'exposure',      role: 'transformation' },
  11: { emoji: '🎱', name: 'ARAM',           slug: 'aram',          role: 'transformation' },
  12: { emoji: '🌋', name: 'Gutter',         slug: 'gutter',        role: 'transformation' },
  13: { emoji: '🪞', name: 'Vanity',         slug: 'vanity',        role: 'transformation' },
  14: { emoji: '🗿', name: 'Sculpt',         slug: 'sculpt',        role: 'transformation' },
  15: { emoji: '🛠', name: 'Craft',          slug: 'craft',         role: 'transformation' },
  16: { emoji: '🧩', name: 'Supplemental',   slug: 'supplemental',  role: 'transformation' },
  17: { emoji: '🪫', name: 'Release',        slug: 'release',       role: 'retention' },
  18: { emoji: '🏖', name: 'Sandbox',        slug: 'sandbox',       role: 'transformation' },
  19: { emoji: '🏗', name: 'Reformance',     slug: 'reformance',    role: 'transformation' },
  20: { emoji: '🧬', name: 'Imprint',        slug: 'imprint',       role: 'retention' },
  21: { emoji: '🚂', name: 'Junction',       slug: 'junction',      role: 'retention' },
  22: { emoji: '🔠', name: 'Choice',         slug: 'choice',        role: 'modifier' },
} as const satisfies Record<number, BlockEntry>;

// ---------------------------------------------------------------------------
// System (1 emoji)
// ---------------------------------------------------------------------------

export const SYSTEM = {
  1: { emoji: '🧮', name: 'SAVE', slug: 'save' },
} as const satisfies Record<number, SclEntry>;

// ---------------------------------------------------------------------------
// Reverse Indexes (emoji → position)
// ---------------------------------------------------------------------------

function buildReverseIndex<T extends Record<number, { emoji: string }>>(
  table: T
): Record<string, number> {
  return Object.fromEntries(
    Object.entries(table).map(([pos, entry]) => [entry.emoji, Number(pos)])
  );
}

export const ORDER_BY_EMOJI = buildReverseIndex(ORDERS);
export const AXIS_BY_EMOJI = buildReverseIndex(AXES);
export const TYPE_BY_EMOJI = buildReverseIndex(TYPES);
export const COLOR_BY_EMOJI = buildReverseIndex(COLORS);
export const OPERATOR_BY_EMOJI = buildReverseIndex(OPERATORS);
export const BLOCK_BY_EMOJI = buildReverseIndex(BLOCKS);

// ---------------------------------------------------------------------------
// W Enum — Weight Vector Index (positions 1–61)
// ---------------------------------------------------------------------------

export const W = {
  // Orders (1–7)
  FOUNDATION:   1,
  STRENGTH:     2,
  HYPERTROPHY:  3,
  PERFORMANCE:  4,
  FULL_BODY:    5,
  BALANCE:      6,
  RESTORATION:  7,

  // Axes (8–13)
  BASICS:       8,
  FUNCTIONAL:   9,
  AESTHETIC:    10,
  CHALLENGE:    11,
  TIME:         12,
  PARTNER:      13,

  // Types (14–18)
  PUSH:         14,
  PULL:         15,
  LEGS:         16,
  PLUS:         17,
  ULTRA:        18,

  // Colors (19–26)
  TEACHING:     19,
  BODYWEIGHT:   20,
  STRUCTURED:   21,
  TECHNICAL:    22,
  INTENSE:      23,
  CIRCUIT:      24,
  FUN:          25,
  MINDFUL:      26,

  // Operators (27–38)
  CAPIO:        27,
  DUCO:         28,
  FACIO:        29,
  FERO:         30,
  GRAPHO:       31,
  LOGOS:        32,
  MITTO:        33,
  PLICO:        34,
  PONO:         35,
  SPECIO:       36,
  TENDO:        37,
  TENEO:        38,

  // Blocks (39–60)
  WARM_UP:      39,
  INTENTION:    40,
  FUNDAMENTALS: 41,
  BREAD_BUTTER: 42,
  CIRCULATION:  43,
  PRIMER:       44,
  COMPOSITION:  45,
  GAMBIT:       46,
  PROGRESSION:  47,
  EXPOSURE:     48,
  ARAM:         49,
  GUTTER:       50,
  VANITY:       51,
  SCULPT:       52,
  CRAFT:        53,
  SUPPLEMENTAL: 54,
  RELEASE:      55,
  SANDBOX:      56,
  REFORMANCE:   57,
  IMPRINT:      58,
  JUNCTION:     59,
  CHOICE:       60,

  // System (61)
  SAVE:         61,
} as const;

export const WEIGHT_VECTOR_LENGTH = 61;

// ---------------------------------------------------------------------------
// Operator Derivation Table (CLAUDE.md canonical)
// ---------------------------------------------------------------------------

export const OPERATOR_TABLE: Record<string, {
  preparatory: { emoji: string; latin: string };
  expressive:  { emoji: string; latin: string };
}> = {
  '🏛': { preparatory: { emoji: '📍', latin: 'pono' },  expressive: { emoji: '🤌', latin: 'facio' } },
  '🔨': { preparatory: { emoji: '🧸', latin: 'fero' },  expressive: { emoji: '🥨', latin: 'tendo' } },
  '🌹': { preparatory: { emoji: '👀', latin: 'specio' }, expressive: { emoji: '🦢', latin: 'plico' } },
  '🪐': { preparatory: { emoji: '🪵', latin: 'teneo' }, expressive: { emoji: '🚀', latin: 'mitto' } },
  '⌛': { preparatory: { emoji: '🐋', latin: 'duco' },  expressive: { emoji: '✒️', latin: 'grapho' } },
  '🐬': { preparatory: { emoji: '🧲', latin: 'capio' }, expressive: { emoji: '🦉', latin: 'logos' } },
};

// ---------------------------------------------------------------------------
// Polarity Sets
// ---------------------------------------------------------------------------

export const PREPARATORY_COLORS = new Set(['⚫', '🟢', '⚪', '🟡']);
export const EXPRESSIVE_COLORS = new Set(['🔵', '🟣', '🔴', '🟠']);

// ---------------------------------------------------------------------------
// Dial Range Constants
// ---------------------------------------------------------------------------

export const ORDER_COUNT = 7;
export const AXIS_COUNT = 6;
export const TYPE_COUNT = 5;
export const COLOR_COUNT = 8;
export const TOTAL_ZIPS = 1_680;
