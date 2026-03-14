/**
 * Zip Converter — Bidirectional emoji <-> numeric zip code conversion
 *
 * Converts between the 4-emoji SCL zip codes (e.g., '⛽🏛🪡🔵') and their
 * 4-digit numeric equivalents (e.g., '2123'). Also derives deck number
 * and default operator from any zip code.
 *
 * All emoji mappings sourced from CLAUDE.md canonical tables via scl.ts.
 * Zero runtime imports from middle-math/ — zip-registry.json is test-only.
 */

import {
  ORDERS,
  AXES,
  TYPES,
  COLORS,
  ORDER_BY_EMOJI,
  AXIS_BY_EMOJI,
  TYPE_BY_EMOJI,
  COLOR_BY_EMOJI,
  OPERATOR_TABLE,
  PREPARATORY_COLORS,
  EXPRESSIVE_COLORS,
  ORDER_COUNT,
  AXIS_COUNT,
  TYPE_COUNT,
  COLOR_COUNT,
} from '../types/scl';

// ---------------------------------------------------------------------------
// Internal helpers
// ---------------------------------------------------------------------------

/** Digit ranges for each zip position: [label, min, max] */
const RANGES: readonly [string, number, number][] = [
  ['order', 1, ORDER_COUNT],
  ['axis', 1, AXIS_COUNT],
  ['type', 1, TYPE_COUNT],
  ['color', 1, COLOR_COUNT],
];

/**
 * Validates a 4-digit numeric zip string. Throws descriptive errors.
 */
function validateNumericZip(numericZip: string): void {
  if (numericZip.length !== 4 || !/^\d{4}$/.test(numericZip)) {
    throw new Error(`numeric zip must be exactly 4 digits, got '${numericZip}'`);
  }

  for (let i = 0; i < 4; i++) {
    const digit = Number(numericZip[i]);
    const [label, min, max] = RANGES[i]!;
    if (digit < min || digit > max) {
      throw new Error(`${label} ${digit} out of range ${min}-${max}`);
    }
  }
}

/**
 * Detect whether a string looks numeric (all digits).
 */
function isNumeric(s: string): boolean {
  return /^\d+$/.test(s);
}

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

/**
 * Convert an emoji zip code to its numeric equivalent.
 *
 * @example emojiToZip('⛽🏛🪡🔵') // '2123'
 */
export function emojiToZip(emojiZip: string): string {
  const chars = [...emojiZip];
  if (chars.length !== 4) {
    throw new Error(
      `emoji zip must contain exactly 4 emojis, got ${chars.length}: '${emojiZip}'`
    );
  }

  const order = ORDER_BY_EMOJI[chars[0]!];
  if (order === undefined) throw new Error(`invalid order emoji: ${chars[0]}`);

  const axis = AXIS_BY_EMOJI[chars[1]!];
  if (axis === undefined) throw new Error(`invalid axis emoji: ${chars[1]}`);

  const type = TYPE_BY_EMOJI[chars[2]!];
  if (type === undefined) throw new Error(`invalid type emoji: ${chars[2]}`);

  const color = COLOR_BY_EMOJI[chars[3]!];
  if (color === undefined) throw new Error(`invalid color emoji: ${chars[3]}`);

  return `${order}${axis}${type}${color}`;
}

/**
 * Convert a numeric zip code to its emoji equivalent.
 *
 * @example zipToEmoji('2123') // '⛽🏛🪡🔵'
 */
export function zipToEmoji(numericZip: string): string {
  validateNumericZip(numericZip);

  const order = Number(numericZip[0]) as keyof typeof ORDERS;
  const axis = Number(numericZip[1]) as keyof typeof AXES;
  const type = Number(numericZip[2]) as keyof typeof TYPES;
  const color = Number(numericZip[3]) as keyof typeof COLORS;

  return `${ORDERS[order].emoji}${AXES[axis].emoji}${TYPES[type].emoji}${COLORS[color].emoji}`;
}

/**
 * Check whether a 4-digit numeric zip string addresses a valid zip code.
 *
 * @example isValidZip('2123') // true
 * @example isValidZip('2193') // false (type 9 out of range 1-5)
 */
export function isValidZip(zip: string): boolean {
  try {
    validateNumericZip(zip);
    return true;
  } catch {
    return false;
  }
}

/**
 * Derive the deck number (1-42) from a zip code.
 * Accepts both emoji and numeric input.
 *
 * Formula: (order - 1) * 6 + axis
 *
 * @example zipToDeck('2123') // 7
 * @example zipToDeck('⛽🏛🪡🔵') // 7
 */
export function zipToDeck(zip: string): number {
  const numeric = isNumeric(zip) ? zip : emojiToZip(zip);
  validateNumericZip(numeric);

  const order = Number(numeric[0]);
  const axis = Number(numeric[1]);

  return (order - 1) * AXIS_COUNT + axis;
}

/**
 * Derive the default operator for an emoji zip code.
 * Uses axis (position 2) and color polarity (position 4).
 *
 * @example deriveOperator('⛽🏛🪡🔵') // { emoji: '🤌', name: 'facio' }
 */
export function deriveOperator(emojiZip: string): { emoji: string; name: string } {
  const chars = [...emojiZip];
  if (chars.length !== 4) {
    throw new Error(
      `emoji zip must contain exactly 4 emojis, got ${chars.length}`
    );
  }

  const axisEmoji = chars[1]!;
  const colorEmoji = chars[3]!;

  const axisEntry = OPERATOR_TABLE[axisEmoji];
  if (!axisEntry) {
    throw new Error(`invalid axis emoji for operator derivation: ${axisEmoji}`);
  }

  if (COLOR_BY_EMOJI[colorEmoji] === undefined) {
    throw new Error(`invalid color emoji: ${colorEmoji}`);
  }

  if (PREPARATORY_COLORS.has(colorEmoji)) {
    return { emoji: axisEntry.preparatory.emoji, name: axisEntry.preparatory.latin };
  }

  if (EXPRESSIVE_COLORS.has(colorEmoji)) {
    return { emoji: axisEntry.expressive.emoji, name: axisEntry.expressive.latin };
  }

  throw new Error(`unable to derive polarity for color: ${colorEmoji}`);
}
