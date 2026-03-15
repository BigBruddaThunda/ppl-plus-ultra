/**
 * card-template.test.ts — Smoke tests for WorkoutCard renderer (CARD-01)
 *
 * Verifies:
 *   1. renderWorkoutCard() returns a string containing .ppl-card root container
 *   2. Output contains at least one .ppl-block container
 *   3. Output does NOT contain hardcoded hex color values (#xxx or #xxxxxx)
 *   4. Function does not throw on a minimal CardData fixture
 */

import { describe, it, expect } from 'vitest';
import { renderWorkoutCard } from '../components/WorkoutCard.js';
import type { CardData } from '../components/types.js';

// ─── Minimal CardData fixture ─────────────────────────────────────────────

const minimalCard: CardData = {
  zip: '⛽🏛🪡🔵',
  numericZip: '2123',
  operator: '🤌 facio',
  title: 'Bent-Over Barbell Row — Back Strength Log',
  subtitle: 'Strength · 🪡 Pull | Lats · 🔵 Structured · ~50 min',
  intention: 'Load the pull and feel the weight in your hands before it leaves the floor.',
  typeEmoji: '🪡',
  blocks: [
    {
      number: 1,
      emoji: '♨️',
      name: 'Warm-Up',
      content: '5 min easy movement prep',
      contentHtml: '<p>5 min easy movement prep</p>',
      slug: 'warm-up',
      role: 'orientation',
    },
    {
      number: 2,
      emoji: '🧈',
      name: 'Bread & Butter',
      content: 'Bent-Over Barbell Row: 5×5 @ 80%',
      contentHtml: '<p>Bent-Over Barbell Row: 5×5 @ 80%</p>',
      slug: 'bread-butter',
      role: 'transformation',
    },
    {
      number: 3,
      emoji: '🚂',
      name: 'Junction',
      content: 'Next → ⛽🏛🛒🔵 — horizontal push to balance pull volume',
      contentHtml: '<p>Next → ⛽🏛🛒🔵 — horizontal push to balance pull volume</p>',
      slug: 'junction',
      role: 'retention',
    },
  ],
  cssVars: {
    '--ppl-theme-primary': 'oklch(0.4 0.105 230)',
    '--ppl-theme-secondary': 'oklch(0.5 0.112 230)',
    '--ppl-theme-background': 'oklch(0.97 0.014 230)',
    '--ppl-theme-surface': 'oklch(1 0 0)',
    '--ppl-theme-text': 'oklch(0.26 0.068 230)',
    '--ppl-theme-accent': 'oklch(0.34 0.089 230)',
    '--ppl-theme-border': 'oklch(0.82 0.042 230)',
    '--ppl-weight-font-weight': '800',
    '--ppl-weight-saturation': '0.50',
    '--ppl-weight-lineheight': '1.4',
  },
  colorSlug: 'structured',
  orderSlug: 'strength',
  axisSlug: 'basics',
};

// ─── Tests ────────────────────────────────────────────────────────────────

describe('renderWorkoutCard', () => {
  it('does not throw on minimal CardData fixture', () => {
    expect(() => renderWorkoutCard(minimalCard)).not.toThrow();
  });

  it('returns a string', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(typeof result).toBe('string');
    expect(result.length).toBeGreaterThan(0);
  });

  it('output contains ppl-card root container class', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain('ppl-card');
  });

  it('output contains ppl-block container class', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain('ppl-block');
  });

  it('output does NOT contain hardcoded hex color values', () => {
    const result = renderWorkoutCard(minimalCard);
    // Match #xxx or #xxxxxx hex colors (not inside SVG data URIs or hex entities)
    // We allow #000 inside SVG data URIs (guilloche pattern) — those are in CSS files, not here
    const hexColorPattern = /#[0-9a-fA-F]{3,8}(?![0-9a-fA-F])/g;
    const hexMatches = result.match(hexColorPattern);
    expect(hexMatches).toBeNull();
  });

  it('output contains data-color attribute matching colorSlug', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain(`data-color="${minimalCard.colorSlug}"`);
  });

  it('output contains data-zip attribute matching numericZip', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain(`data-zip="${minimalCard.numericZip}"`);
  });

  it('output contains the workout title', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain(minimalCard.title);
  });

  it('output contains the intention text', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain(minimalCard.intention);
  });

  it('CSS vars are present in the style attribute', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain('--ppl-theme-primary');
    expect(result).toContain('--ppl-weight-saturation');
  });

  it('renders all provided blocks', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain('data-block="warm-up"');
    expect(result).toContain('data-block="bread-butter"');
    expect(result).toContain('data-block="junction"');
  });

  it('junction block appears in footer zone', () => {
    const result = renderWorkoutCard(minimalCard);
    // Footer should contain junction
    const footerMatch = /<footer[^>]*>([\s\S]*?)<\/footer>/i.exec(result);
    expect(footerMatch).not.toBeNull();
    expect(footerMatch?.[1]).toContain('junction');
  });

  it('contains logging scaffold elements', () => {
    const result = renderWorkoutCard(minimalCard);
    expect(result).toContain('ppl-log-scaffold');
    expect(result).toContain('ppl-timer-slot');
    expect(result).toContain('ppl-log-checkbox');
    expect(result).toContain('type="text"');
    expect(result).toContain('type="checkbox"');
  });
});
