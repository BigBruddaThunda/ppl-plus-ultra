/**
 * Zip Converter Tests — TDD RED phase
 *
 * Tests bidirectional emoji<->numeric zip conversion, deck derivation,
 * operator derivation, and error handling. Uses zip-registry.json as
 * the 1,680-entry ground truth corpus.
 */

import { describe, it, expect } from 'vitest';
import {
  emojiToZip,
  zipToEmoji,
  isValidZip,
  zipToDeck,
  deriveOperator,
} from '../src/parser/zip-converter';

// Test-only import: the 1,680-entry ground truth
import registry from '../../middle-math/zip-registry.json';

// ---------------------------------------------------------------------------
// Round-trip: all 1,680 zip codes
// ---------------------------------------------------------------------------

describe('round-trip conversions (1,680 entries)', () => {
  it('should have exactly 1,680 entries in the registry', () => {
    expect(registry.length).toBe(1_680);
  });

  for (const entry of registry) {
    const { numeric_zip, emoji_zip } = entry as {
      numeric_zip: string;
      emoji_zip: string;
    };

    it(`emojiToZip('${emoji_zip}') === '${numeric_zip}'`, () => {
      expect(emojiToZip(emoji_zip)).toBe(numeric_zip);
    });

    it(`zipToEmoji('${numeric_zip}') === '${emoji_zip}'`, () => {
      expect(zipToEmoji(numeric_zip)).toBe(emoji_zip);
    });
  }
});

// ---------------------------------------------------------------------------
// Specific conversions (smoke tests)
// ---------------------------------------------------------------------------

describe('specific conversions', () => {
  it("emojiToZip('⛽🏛🪡🔵') returns '2123'", () => {
    expect(emojiToZip('⛽🏛🪡🔵')).toBe('2123');
  });

  it("zipToEmoji('2123') returns '⛽🏛🪡🔵'", () => {
    expect(zipToEmoji('2123')).toBe('⛽🏛🪡🔵');
  });

  it("emojiToZip('🐂🏛🛒⚫') returns '1111'", () => {
    expect(emojiToZip('🐂🏛🛒⚫')).toBe('1111');
  });

  it("emojiToZip('🖼🐬➖⚪') returns '7658'", () => {
    expect(emojiToZip('🖼🐬➖⚪')).toBe('7658');
  });
});

// ---------------------------------------------------------------------------
// isValidZip
// ---------------------------------------------------------------------------

describe('isValidZip', () => {
  it('returns true for valid numeric zip', () => {
    expect(isValidZip('2123')).toBe(true);
  });

  it('returns true for boundary values', () => {
    expect(isValidZip('1111')).toBe(true);
    expect(isValidZip('7658')).toBe(true);
  });

  it('returns false for type 9 (out of range 1-5)', () => {
    expect(isValidZip('2193')).toBe(false);
  });

  it('returns false for order 0 (out of range 1-7)', () => {
    expect(isValidZip('0123')).toBe(false);
  });

  it('returns false for order 8 (out of range 1-7)', () => {
    expect(isValidZip('8123')).toBe(false);
  });

  it('returns false for axis 7 (out of range 1-6)', () => {
    expect(isValidZip('1713')).toBe(false);
  });

  it('returns false for color 9 (out of range 1-8)', () => {
    expect(isValidZip('2129')).toBe(false);
  });

  it('returns false for color 0', () => {
    expect(isValidZip('2120')).toBe(false);
  });

  it('returns false for non-4-digit string', () => {
    expect(isValidZip('212')).toBe(false);
    expect(isValidZip('21234')).toBe(false);
    expect(isValidZip('')).toBe(false);
  });

  it('returns false for non-numeric string', () => {
    expect(isValidZip('abcd')).toBe(false);
  });
});

// ---------------------------------------------------------------------------
// zipToDeck
// ---------------------------------------------------------------------------

describe('zipToDeck', () => {
  it("zipToDeck('2123') returns 7", () => {
    expect(zipToDeck('2123')).toBe(7);
  });

  it("zipToDeck('2223') returns 8", () => {
    expect(zipToDeck('2223')).toBe(8);
  });

  it("zipToDeck('7658') returns 42", () => {
    expect(zipToDeck('7658')).toBe(42);
  });

  it("zipToDeck('1111') returns 1", () => {
    expect(zipToDeck('1111')).toBe(1);
  });

  it('accepts emoji input', () => {
    expect(zipToDeck('⛽🏛🪡🔵')).toBe(7);
    expect(zipToDeck('🖼🐬➖⚪')).toBe(42);
  });

  // Verify all registry entries have correct deck
  for (const entry of registry) {
    const { numeric_zip, deck_number } = entry as {
      numeric_zip: string;
      deck_number: number;
    };

    it(`zipToDeck('${numeric_zip}') === ${deck_number}`, () => {
      expect(zipToDeck(numeric_zip)).toBe(deck_number);
    });
  }
});

// ---------------------------------------------------------------------------
// deriveOperator
// ---------------------------------------------------------------------------

describe('deriveOperator', () => {
  it("derives facio for 🏛 axis + 🔵 expressive color", () => {
    const op = deriveOperator('⛽🏛🪡🔵');
    expect(op).toEqual({ emoji: '🤌', name: 'facio' });
  });

  it("derives pono for 🏛 axis + 🟢 preparatory color", () => {
    const op = deriveOperator('⛽🏛🪡🟢');
    expect(op).toEqual({ emoji: '📍', name: 'pono' });
  });

  it("derives tendo for 🔨 axis + 🔴 expressive color", () => {
    const op = deriveOperator('🦋🔨🛒🔴');
    expect(op).toEqual({ emoji: '🥨', name: 'tendo' });
  });

  it("derives fero for 🔨 axis + ⚫ preparatory color", () => {
    const op = deriveOperator('🐂🔨🍗⚫');
    expect(op).toEqual({ emoji: '🧸', name: 'fero' });
  });

  it("derives plico for 🌹 axis + 🟠 expressive color", () => {
    const op = deriveOperator('🦋🌹🪡🟠');
    expect(op).toEqual({ emoji: '🦢', name: 'plico' });
  });

  it("derives specio for 🌹 axis + ⚪ preparatory color", () => {
    const op = deriveOperator('🖼🌹➖⚪');
    expect(op).toEqual({ emoji: '👀', name: 'specio' });
  });

  it("derives mitto for 🪐 axis + 🟣 expressive color", () => {
    const op = deriveOperator('⛽🪐🛒🟣');
    expect(op).toEqual({ emoji: '🚀', name: 'mitto' });
  });

  it("derives teneo for 🪐 axis + 🟡 preparatory color", () => {
    const op = deriveOperator('🐂🪐🍗🟡');
    expect(op).toEqual({ emoji: '🪵', name: 'teneo' });
  });

  it("derives grapho for ⌛ axis + 🔵 expressive color", () => {
    const op = deriveOperator('🦋⌛🛒🔵');
    expect(op).toEqual({ emoji: '✒️', name: 'grapho' });
  });

  it("derives duco for ⌛ axis + 🟢 preparatory color", () => {
    const op = deriveOperator('🐂⌛🪡🟢');
    expect(op).toEqual({ emoji: '🐋', name: 'duco' });
  });

  it("derives logos for 🐬 axis + 🔴 expressive color", () => {
    const op = deriveOperator('⛽🐬➕🔴');
    expect(op).toEqual({ emoji: '🦉', name: 'logos' });
  });

  it("derives capio for 🐬 axis + ⚪ preparatory color", () => {
    const op = deriveOperator('🖼🐬➖⚪');
    expect(op).toEqual({ emoji: '🧲', name: 'capio' });
  });

  // Verify all registry entries match
  for (const entry of registry) {
    const { emoji_zip, operator } = entry as {
      emoji_zip: string;
      operator: { emoji: string; name: string };
    };

    it(`deriveOperator('${emoji_zip}') matches registry`, () => {
      const derived = deriveOperator(emoji_zip);
      expect(derived.emoji).toBe(operator.emoji);
      expect(derived.name).toBe(operator.name);
    });
  }
});

// ---------------------------------------------------------------------------
// Error handling
// ---------------------------------------------------------------------------

describe('error handling', () => {
  it('emojiToZip throws on wrong emoji count (3)', () => {
    expect(() => emojiToZip('⛽🏛🪡')).toThrow();
  });

  it('emojiToZip throws on wrong emoji count (5)', () => {
    expect(() => emojiToZip('⛽🏛🪡🔵🔴')).toThrow();
  });

  it('emojiToZip throws on unrecognized emoji', () => {
    expect(() => emojiToZip('😀🏛🪡🔵')).toThrow();
  });

  it('emojiToZip throws on empty string', () => {
    expect(() => emojiToZip('')).toThrow();
  });

  it('zipToEmoji throws on out-of-range order digit', () => {
    expect(() => zipToEmoji('8123')).toThrow();
  });

  it('zipToEmoji throws on out-of-range type digit', () => {
    expect(() => zipToEmoji('2193')).toThrow();
  });

  it('zipToEmoji throws on out-of-range color digit', () => {
    expect(() => zipToEmoji('2129')).toThrow();
  });

  it('zipToEmoji throws on non-4-digit input', () => {
    expect(() => zipToEmoji('212')).toThrow();
    expect(() => zipToEmoji('21234')).toThrow();
  });

  it('zipToEmoji throws on non-numeric input', () => {
    expect(() => zipToEmoji('abcd')).toThrow();
  });

  it('deriveOperator throws on invalid emoji count', () => {
    expect(() => deriveOperator('⛽🏛')).toThrow();
  });
});
