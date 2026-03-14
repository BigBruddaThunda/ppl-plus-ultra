/**
 * Token system shape validation tests — Phase 4 design tokens
 *
 * RNDR-01: 8 Color palettes (tonal names, OKLCH values)
 * RNDR-02: 7 Order typographies (fontWeight, lineHeight, spacingMultiplier)
 * RNDR-03: 6 Axis gradient directions (gradientDirection, layoutFlow)
 * RNDR-04: CSS arbitration spec document exists
 */

import { describe, it, expect } from 'vitest';
import { existsSync, readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

// ─── Paths ───────────────────────────────────────────────────────────────────

// Resolve from canvas/ root (this test runs with cwd = canvas/)
const __dirname_ts = dirname(fileURLToPath(import.meta.url));
const TOKENS_DIR = join(__dirname_ts, '..', 'src', 'tokens');
const DESIGN_TOKENS_JSON = join(TOKENS_DIR, 'design-tokens.json');
const DESIGN_TOKENS_CSS = join(TOKENS_DIR, 'design-tokens.css');
const TOKENS_TS = join(TOKENS_DIR, 'tokens.ts');
const ARBITRATION_SPEC = join(
  __dirname_ts,
  '..', '..', '.planning', 'phases', '04-design-tokens', '04-CSS-ARBITRATION.md'
);

// ─── Expected shape constants ─────────────────────────────────────────────────

/** 8 tonal names — must match COLOR_W_TO_TONAL bridge table in arbitration spec */
const TONAL_NAMES = [
  'order',         // W.TEACHING = 19  (⚫ Teaching)
  'growth',        // W.BODYWEIGHT = 20 (🟢 Bodyweight)
  'planning',      // W.STRUCTURED = 21 (🔵 Structured)
  'magnificence',  // W.TECHNICAL = 22  (🟣 Technical)
  'passion',       // W.INTENSE = 23    (🔴 Intense)
  'connection',    // W.CIRCUIT = 24    (🟠 Circuit)
  'play',          // W.FUN = 25        (🟡 Fun)
  'eudaimonia',    // W.MINDFUL = 26    (⚪ Mindful)
] as const;

/** Required properties each Color palette entry must have */
const COLOR_REQUIRED_PROPS = [
  'primary', 'secondary', 'background', 'surface', 'text', 'accent', 'border',
] as const;

/** 7 Order slugs — SCL Order names in kebab-case */
const ORDER_SLUGS = [
  'foundation',  // 🐂
  'strength',    // ⛽
  'hypertrophy', // 🦋
  'performance', // 🏟
  'full-body',   // 🌾
  'balance',     // ⚖
  'restoration', // 🖼
] as const;

/** Required properties each Order typography entry must have */
const ORDER_REQUIRED_PROPS = [
  'fontWeight', 'lineHeight', 'spacingMultiplier',
] as const;

/** 6 Axis slugs — SCL Axis names in kebab-case */
const AXIS_SLUGS = [
  'basics',      // 🏛
  'functional',  // 🔨
  'aesthetic',   // 🌹
  'challenge',   // 🪐
  'time',        // ⌛
  'partner',     // 🐬
] as const;

/** Required properties each Axis entry must have */
const AXIS_REQUIRED_PROPS = [
  'gradientDirection', 'layoutFlow',
] as const;

/**
 * W enum positions for Colors (from canvas/src/types/scl.ts)
 * to tonal token key mapping — authoritative bridge table
 */
const COLOR_W_TO_TONAL: Record<number, typeof TONAL_NAMES[number]> = {
  19: 'order',        // W.TEACHING
  20: 'growth',       // W.BODYWEIGHT
  21: 'planning',     // W.STRUCTURED
  22: 'magnificence', // W.TECHNICAL
  23: 'passion',      // W.INTENSE
  24: 'connection',   // W.CIRCUIT
  25: 'play',         // W.FUN
  26: 'eudaimonia',   // W.MINDFUL
};

// ─── RNDR-04: CSS Arbitration Spec ───────────────────────────────────────────
// This test passes immediately — the spec is created in Plan 01.

describe('RNDR-04: CSS arbitration spec', () => {
  it('04-CSS-ARBITRATION.md exists at expected path', () => {
    expect(existsSync(ARBITRATION_SPEC)).toBe(true);
  });

  it('04-CSS-ARBITRATION.md contains Owner Dial table', () => {
    if (!existsSync(ARBITRATION_SPEC)) return;
    const content = readFileSync(ARBITRATION_SPEC, 'utf8');
    expect(content).toContain('Owner Dial');
  });

  it('04-CSS-ARBITRATION.md contains W enum bridge table (all 8 W positions)', () => {
    if (!existsSync(ARBITRATION_SPEC)) return;
    const content = readFileSync(ARBITRATION_SPEC, 'utf8');
    // All 8 W positions (19-26) must appear in the bridge table
    for (const pos of [19, 20, 21, 22, 23, 24, 25, 26]) {
      expect(content).toContain(String(pos));
    }
  });
});

// ─── RNDR-01: Color Palettes ─────────────────────────────────────────────────

describe('RNDR-01: Color palettes', () => {
  it('design-tokens.json exists', () => {
    expect(existsSync(DESIGN_TOKENS_JSON)).toBe(true);
  });

  it('design-tokens.json has exactly 8 Color entries', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    expect(tokens).toHaveProperty('colors');
    expect(Object.keys(tokens.colors)).toHaveLength(8);
  });

  it('Color entries use tonal names (not SCL emoji names)', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const tonalName of TONAL_NAMES) {
      expect(tokens.colors).toHaveProperty(tonalName);
    }
    // Must NOT have SCL names
    const sclNames = ['teaching', 'bodyweight', 'structured', 'technical', 'intense', 'circuit', 'fun', 'mindful'];
    for (const sclName of sclNames) {
      expect(tokens.colors).not.toHaveProperty(sclName);
    }
  });

  it('each Color entry has all required palette properties', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const tonalName of TONAL_NAMES) {
      const entry = tokens.colors[tonalName];
      for (const prop of COLOR_REQUIRED_PROPS) {
        expect(entry).toHaveProperty(prop);
      }
    }
  });

  it('all Color palette values are oklch() strings', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    const colorValueProps = ['primary', 'secondary', 'background', 'surface', 'text', 'accent', 'border'];
    for (const tonalName of TONAL_NAMES) {
      const entry = tokens.colors[tonalName];
      for (const prop of colorValueProps) {
        const value: string = entry[prop];
        expect(value).toMatch(/^oklch\(/);
      }
    }
  });
});

// ─── RNDR-02: Order Typographies ─────────────────────────────────────────────

describe('RNDR-02: Order typographies', () => {
  it('design-tokens.json has exactly 7 Order entries', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    expect(tokens).toHaveProperty('orders');
    expect(Object.keys(tokens.orders)).toHaveLength(7);
  });

  it('Order entries use correct slugs', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of ORDER_SLUGS) {
      expect(tokens.orders).toHaveProperty(slug);
    }
  });

  it('each Order entry has required typography properties', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of ORDER_SLUGS) {
      const entry = tokens.orders[slug];
      for (const prop of ORDER_REQUIRED_PROPS) {
        expect(entry).toHaveProperty(prop);
      }
    }
  });

  it('fontWeight is a number for all Orders', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of ORDER_SLUGS) {
      expect(typeof tokens.orders[slug].fontWeight).toBe('number');
    }
  });

  it('lineHeight is a number for all Orders', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of ORDER_SLUGS) {
      expect(typeof tokens.orders[slug].lineHeight).toBe('number');
    }
  });

  it('spacingMultiplier is a number for all Orders', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of ORDER_SLUGS) {
      expect(typeof tokens.orders[slug].spacingMultiplier).toBe('number');
    }
  });
});

// ─── RNDR-03: Axis Gradients ──────────────────────────────────────────────────

describe('RNDR-03: Axis gradients', () => {
  it('design-tokens.json has exactly 6 Axis entries', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    expect(tokens).toHaveProperty('axes');
    expect(Object.keys(tokens.axes)).toHaveLength(6);
  });

  it('Axis entries use correct slugs', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of AXIS_SLUGS) {
      expect(tokens.axes).toHaveProperty(slug);
    }
  });

  it('each Axis entry has gradientDirection (string)', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of AXIS_SLUGS) {
      const entry = tokens.axes[slug];
      expect(entry).toHaveProperty('gradientDirection');
      expect(typeof entry.gradientDirection).toBe('string');
    }
  });

  it('each Axis entry has layoutFlow (string)', () => {
    const tokens = JSON.parse(readFileSync(DESIGN_TOKENS_JSON, 'utf8'));
    for (const slug of AXIS_SLUGS) {
      const entry = tokens.axes[slug];
      expect(entry).toHaveProperty('layoutFlow');
      expect(typeof entry.layoutFlow).toBe('string');
    }
  });
});

// ─── Build Artifacts ──────────────────────────────────────────────────────────

describe('Build artifacts', () => {
  it('design-tokens.css exists after build', () => {
    expect(existsSync(DESIGN_TOKENS_CSS)).toBe(true);
  });

  it('design-tokens.css contains CSS custom properties with --ppl- prefix', () => {
    const css = readFileSync(DESIGN_TOKENS_CSS, 'utf8');
    expect(css).toContain('--ppl-');
    expect(css).toContain(':root');
  });

  it('design-tokens.css uses double-hyphen separator (--ppl-color-passion--primary)', () => {
    const css = readFileSync(DESIGN_TOKENS_CSS, 'utf8');
    // At least one double-hyphen property must exist
    expect(css).toMatch(/--ppl-color-\w+--\w+/);
  });

  it('tokens.ts exists after build', () => {
    expect(existsSync(TOKENS_TS)).toBe(true);
  });

  it('tokens.ts exports tokens object with colors, orders, axes', async () => {
    const mod = await import(TOKENS_TS);
    expect(mod).toHaveProperty('tokens');
    expect(mod.tokens).toHaveProperty('colors');
    expect(mod.tokens).toHaveProperty('orders');
    expect(mod.tokens).toHaveProperty('axes');
  });

  it('COLOR_W_TO_TONAL bridge covers all 8 W positions (19-26)', async () => {
    const mod = await import(TOKENS_TS);
    expect(mod).toHaveProperty('COLOR_W_TO_TONAL');
    const bridge: Record<number, string> = mod.COLOR_W_TO_TONAL;
    // Verify all 8 positions map to tonal names
    const expectedMappings = COLOR_W_TO_TONAL;
    for (const [wPos, tonalName] of Object.entries(expectedMappings)) {
      expect(bridge[Number(wPos)]).toBe(tonalName);
    }
  });

  it('tokens.ts Color keys are tonal names (order, growth, planning, magnificence, passion, connection, play, eudaimonia)', async () => {
    const mod = await import(TOKENS_TS);
    const colorKeys = Object.keys(mod.tokens.colors);
    for (const tonalName of TONAL_NAMES) {
      expect(colorKeys).toContain(tonalName);
    }
    expect(colorKeys).toHaveLength(8);
  });
});

// ─── W Enum Bridge ────────────────────────────────────────────────────────────

describe('COLOR_W_TO_TONAL bridge (test-level verification)', () => {
  it('covers all 8 W positions (19-26)', () => {
    const positions = Object.keys(COLOR_W_TO_TONAL).map(Number);
    expect(positions).toHaveLength(8);
    for (let pos = 19; pos <= 26; pos++) {
      expect(COLOR_W_TO_TONAL).toHaveProperty(String(pos));
    }
  });

  it('maps to all 8 tonal names', () => {
    const values = Object.values(COLOR_W_TO_TONAL);
    for (const tonalName of TONAL_NAMES) {
      expect(values).toContain(tonalName);
    }
    expect(values).toHaveLength(8);
  });

  it('W.TEACHING(19) maps to order', () => {
    expect(COLOR_W_TO_TONAL[19]).toBe('order');
  });

  it('W.INTENSE(23) maps to passion', () => {
    expect(COLOR_W_TO_TONAL[23]).toBe('passion');
  });

  it('W.MINDFUL(26) maps to eudaimonia', () => {
    expect(COLOR_W_TO_TONAL[26]).toBe('eudaimonia');
  });
});
