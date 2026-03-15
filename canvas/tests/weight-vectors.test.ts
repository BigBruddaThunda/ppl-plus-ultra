/**
 * weight-vectors.test.ts — Weight Vector Spot-Checks (TEST-02)
 *
 * Requirements: TEST-02
 *
 * 10 representative zips covering all 7 Orders produce SPECIFIC expected CSS values
 * when resolved through the full weight pipeline. These are regression anchors for
 * the complete Phase 1–5 implementation.
 *
 * Zip notation: numeric OATC (Order, Axis, Type, Color), each 1-indexed.
 *   resolveZip(order, axis, type, color)
 *
 * Zips tested (one per Order + 3 additional for coverage):
 *   2123 — anchor zip: Strength/Basics/Pull/Structured
 *   1213 — Foundation/Functional/Push/Intense
 *   3352 — Hypertrophy/Aesthetic/Legs/Bodyweight
 *   4145 — Performance/Basics/Legs/Mindful
 *   5241 — Full Body/Functional/Legs/Teaching
 *   6313 — Balance/Aesthetic/Push/Intense
 *   7218 — Restoration/Functional/Push/Mindful
 *   2444 — Strength/Challenge/Legs/Technical
 *   3155 — Hypertrophy/Basics/Ultra/Intense
 *   6526 — Balance/Time/Functional/Fun
 */

import { describe, it, expect, beforeAll } from 'vitest';
import { resolveZip } from '../src/weights/resolver.js';
import { tokens } from '../src/tokens/tokens.js';
import { weightsToCSSVars } from '../src/rendering/index.js';

// ---------------------------------------------------------------------------
// Shared state — resolve all 10 zips once in beforeAll
// ---------------------------------------------------------------------------

type CSSVars = Record<string, string>;

let css2123: CSSVars; // ⛽🏛🪡🔵 Strength/Basics/Pull/Structured
let css1213: CSSVars; // 🐂🔨🛒🔴 Foundation/Functional/Push/Intense
let css3352: CSSVars; // 🦋🌹🍗🟢 Hypertrophy/Aesthetic/Legs/Bodyweight
let css4145: CSSVars; // 🏟🏛🍗⚪  Performance/Basics/Legs/Mindful
let css5241: CSSVars; // 🌾🔨🍗⚫  Full Body/Functional/Legs/Teaching
let css6313: CSSVars; // ⚖🌹🛒🔴  Balance/Aesthetic/Push/Intense
let css7218: CSSVars; // 🖼🔨🛒⚪  Restoration/Functional/Push/Mindful
let css2444: CSSVars; // ⛽🪐🍗🟣  Strength/Challenge/Legs/Technical
let css3155: CSSVars; // 🦋🏛➖🔴  Hypertrophy/Basics/Ultra/Intense
let css6526: CSSVars; // ⚖⌛🔨🟡  Balance/Time/Functional/Fun

beforeAll(() => {
  // Zip 2123: Order=2(Strength), Axis=1(Basics), Type=2(Pull), Color=3(Structured)
  css2123 = weightsToCSSVars(resolveZip(2, 1, 2, 3), tokens);

  // Zip 1213: Order=1(Foundation), Axis=2(Functional), Type=1(Push), Color=3(Intense)
  // NOTE: color position 3 = Structured in standard mapping, but 1213 has color=3
  // Rechecking: 1213 -> O=1, A=2, T=1, C=3 (Structured)... but plan says "Intense"
  // Plan spec: 1213 (Foundation/Intense) - this means 4th digit=3 which is Structured.
  // The plan may intend the PLAN'S label over strict digit parsing. Color 5=Intense.
  // 1213 as O=1,A=2,T=1,C=3 → Foundation/Functional/Push/Structured
  // But plan says "Foundation density='airy', Intense saturation >=0.85"
  // Foundation density IS "spacious" (not airy — that's Restoration). Airy = density='airy' for Restoration.
  // Re-reading plan: "1213 (Foundation/Intense): Foundation density='airy', Intense saturation >=0.85"
  // This is contradictory: Foundation density is "spacious", Restoration is "airy".
  // The plan note says to match ACTUAL pipeline output. We use actual values.
  // resolveZip(1, 2, 1, 3) = Foundation/Functional/Push/Structured
  css1213 = weightsToCSSVars(resolveZip(1, 2, 1, 3), tokens);

  // Zip 3352: Order=3(Hypertrophy), Axis=3(Aesthetic), Type=5(Ultra), Color=2(Bodyweight)
  // NOTE: 3352 -> O=3, A=3, T=5, C=2 (Bodyweight)
  css3352 = weightsToCSSVars(resolveZip(3, 3, 5, 2), tokens);

  // Zip 4145: Order=4(Performance), Axis=1(Basics), Type=4(Plus), Color=5(Mindful)
  // NOTE: 4145 -> O=4, A=1, T=4, C=5 — but color 5=Intense, 8=Mindful
  // Plan says "Performance tokens, Mindful saturation ~0.10"
  // If 4th digit is 5 → Color pos 5 = Intense. Plan label says Mindful (pos=8).
  // We trust the numeric zip: 4145 → O=4,A=1,T=4,C=5 (Intense)
  // Adjusting: use ACTUAL pipeline. Note says "adjust assertions to ACTUAL output".
  css4145 = weightsToCSSVars(resolveZip(4, 1, 4, 5), tokens);

  // Zip 5241: Order=5(Full Body), Axis=2(Functional), Type=4(Plus), Color=1(Teaching)
  css5241 = weightsToCSSVars(resolveZip(5, 2, 4, 1), tokens);

  // Zip 6313: Order=6(Balance), Axis=3(Aesthetic), Type=1(Push), Color=3(Structured)
  // Plan says "Intense saturation >=0.85" but C=3=Structured
  // Using actual: resolveZip(6, 3, 1, 3) = Balance/Aesthetic/Push/Structured
  css6313 = weightsToCSSVars(resolveZip(6, 3, 1, 3), tokens);

  // Zip 7218: Order=7(Restoration), Axis=2(Functional), Type=1(Push), Color=8(Mindful)
  // NOTE: 4-digit zip 7218 → O=7, A=2, T=1, C=8
  css7218 = weightsToCSSVars(resolveZip(7, 2, 1, 8), tokens);

  // Zip 2444: Order=2(Strength), Axis=4(Challenge), Type=4(Plus), Color=4(Technical)
  css2444 = weightsToCSSVars(resolveZip(2, 4, 4, 4), tokens);

  // Zip 3155: Order=3(Hypertrophy), Axis=1(Basics), Type=5(Ultra), Color=5(Intense)
  css3155 = weightsToCSSVars(resolveZip(3, 1, 5, 5), tokens);

  // Zip 6526: Order=6(Balance), Axis=5(Time), Type=2(Pull), Color=6(Fun)
  // NOTE: 6526 -> O=6, A=5, T=2, C=6 (Fun)
  css6526 = weightsToCSSVars(resolveZip(6, 5, 2, 6), tokens);
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 2123 — anchor (Strength/Basics/Pull/Structured)
// ---------------------------------------------------------------------------

describe('TEST-02: zip 2123 — Strength/Basics/Pull/Structured (anchor)', () => {
  it('Order token: font-weight is "800" (Strength)', () => {
    expect(css2123['--ppl-weight-font-weight']).toBe('800');
  });

  it('Order token: density is "compact" (Strength)', () => {
    expect(css2123['--ppl-weight-density']).toBe('compact');
  });

  it('Color theme: primary matches planning (Structured)', () => {
    expect(css2123['--ppl-theme-primary']).toBe(tokens.colors.planning.primary);
  });

  it('Saturation is "0.50" (Structured = planning neutral)', () => {
    expect(css2123['--ppl-weight-saturation']).toBe('0.50');
  });

  it('Tonal name is "planning" (Structured Color)', () => {
    expect(css2123['--ppl-weight-tonal-name']).toBe('planning');
  });

  it('Axis gradient direction is "to bottom" (Basics)', () => {
    expect(css2123['--ppl-weight-gradient-direction']).toBe('to bottom');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 1213 — Foundation/Functional/Push/Structured
// ---------------------------------------------------------------------------

describe('TEST-02: zip 1213 — Foundation/Functional/Push/Structured', () => {
  it('Order token: density is "spacious" (Foundation)', () => {
    expect(css1213['--ppl-weight-density']).toBe('spacious');
  });

  it('Order token: font-weight is "400" (Foundation)', () => {
    expect(css1213['--ppl-weight-font-weight']).toBe('400');
  });

  it('Color theme: primary matches planning (Structured)', () => {
    expect(css1213['--ppl-theme-primary']).toBe(tokens.colors.planning.primary);
  });

  it('Saturation is "0.50" (Structured = planning neutral)', () => {
    expect(css1213['--ppl-weight-saturation']).toBe('0.50');
  });

  it('Axis gradient direction is "135deg" (Functional)', () => {
    expect(css1213['--ppl-weight-gradient-direction']).toBe('135deg');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 3352 — Hypertrophy/Aesthetic/Ultra/Bodyweight
// ---------------------------------------------------------------------------

describe('TEST-02: zip 3352 — Hypertrophy/Aesthetic/Ultra/Bodyweight', () => {
  it('Order token: font-weight is "600" (Hypertrophy)', () => {
    expect(css3352['--ppl-weight-font-weight']).toBe('600');
  });

  it('Order token: density is "moderate" (Hypertrophy)', () => {
    expect(css3352['--ppl-weight-density']).toBe('moderate');
  });

  it('Color theme: primary matches growth (Bodyweight)', () => {
    expect(css3352['--ppl-theme-primary']).toBe(tokens.colors.growth.primary);
  });

  it('Saturation is "0.40" (Bodyweight = natural)', () => {
    expect(css3352['--ppl-weight-saturation']).toBe('0.40');
  });

  it('Tonal name is "growth" (Bodyweight Color)', () => {
    expect(css3352['--ppl-weight-tonal-name']).toBe('growth');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 4145 — Performance/Basics/Plus/Intense
// ---------------------------------------------------------------------------

describe('TEST-02: zip 4145 — Performance/Basics/Plus/Intense', () => {
  it('Order token: font-weight is "900" (Performance)', () => {
    expect(css4145['--ppl-weight-font-weight']).toBe('900');
  });

  it('Order token: density is "compact" (Performance)', () => {
    expect(css4145['--ppl-weight-density']).toBe('compact');
  });

  it('Saturation >= 0.85 (Intense = maximum effort)', () => {
    const sat = parseFloat(css4145['--ppl-weight-saturation']!);
    expect(sat).toBeGreaterThanOrEqual(0.85);
  });

  it('Tonal name is "passion" (Intense Color)', () => {
    expect(css4145['--ppl-weight-tonal-name']).toBe('passion');
  });

  it('Axis gradient direction is "to bottom" (Basics)', () => {
    expect(css4145['--ppl-weight-gradient-direction']).toBe('to bottom');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 5241 — Full Body/Functional/Plus/Teaching
// ---------------------------------------------------------------------------

describe('TEST-02: zip 5241 — Full Body/Functional/Plus/Teaching', () => {
  it('Order token: font-weight is "500" (Full Body)', () => {
    expect(css5241['--ppl-weight-font-weight']).toBe('500');
  });

  it('Order token: density is "moderate" (Full Body)', () => {
    expect(css5241['--ppl-weight-density']).toBe('moderate');
  });

  it('Saturation <= 0.10 (Teaching = near-monochrome)', () => {
    const sat = parseFloat(css5241['--ppl-weight-saturation']!);
    expect(sat).toBeLessThanOrEqual(0.10);
  });

  it('Tonal name is "order" (Teaching Color)', () => {
    expect(css5241['--ppl-weight-tonal-name']).toBe('order');
  });

  it('Axis gradient direction is "135deg" (Functional)', () => {
    expect(css5241['--ppl-weight-gradient-direction']).toBe('135deg');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 6313 — Balance/Aesthetic/Push/Structured
// ---------------------------------------------------------------------------

describe('TEST-02: zip 6313 — Balance/Aesthetic/Push/Structured', () => {
  it('Order token: font-weight is "400" (Balance)', () => {
    expect(css6313['--ppl-weight-font-weight']).toBe('400');
  });

  it('Order token: density is "moderate" (Balance)', () => {
    expect(css6313['--ppl-weight-density']).toBe('moderate');
  });

  it('Color theme: primary matches planning (Structured)', () => {
    expect(css6313['--ppl-theme-primary']).toBe(tokens.colors.planning.primary);
  });

  it('Saturation is "0.50" (Structured)', () => {
    expect(css6313['--ppl-weight-saturation']).toBe('0.50');
  });

  it('Axis gradient direction is "to bottom right" (Aesthetic)', () => {
    expect(css6313['--ppl-weight-gradient-direction']).toBe('to bottom right');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 7218 — Restoration/Functional/Push/Mindful
// ---------------------------------------------------------------------------

describe('TEST-02: zip 7218 — Restoration/Functional/Push/Mindful', () => {
  it('Order token: density is "airy" (Restoration)', () => {
    expect(css7218['--ppl-weight-density']).toBe('airy');
  });

  it('Order token: font-weight is "300" (Restoration)', () => {
    expect(css7218['--ppl-weight-font-weight']).toBe('300');
  });

  it('Saturation <= 0.15 (Mindful = near-monochrome calm)', () => {
    const sat = parseFloat(css7218['--ppl-weight-saturation']!);
    expect(sat).toBeLessThanOrEqual(0.15);
  });

  it('Tonal name is "eudaimonia" (Mindful Color)', () => {
    expect(css7218['--ppl-weight-tonal-name']).toBe('eudaimonia');
  });

  it('Axis gradient direction is "135deg" (Functional)', () => {
    expect(css7218['--ppl-weight-gradient-direction']).toBe('135deg');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 2444 — Strength/Challenge/Plus/Technical
// ---------------------------------------------------------------------------

describe('TEST-02: zip 2444 — Strength/Challenge/Plus/Technical', () => {
  it('Order token: font-weight is "800" (Strength)', () => {
    expect(css2444['--ppl-weight-font-weight']).toBe('800');
  });

  it('Order token: density is "compact" (Strength)', () => {
    expect(css2444['--ppl-weight-density']).toBe('compact');
  });

  it('Saturation is "0.65" (Technical = precision)', () => {
    expect(css2444['--ppl-weight-saturation']).toBe('0.65');
  });

  it('Tonal name is "magnificence" (Technical Color)', () => {
    expect(css2444['--ppl-weight-tonal-name']).toBe('magnificence');
  });

  it('Axis gradient direction is "to top" (Challenge)', () => {
    expect(css2444['--ppl-weight-gradient-direction']).toBe('to top');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 3155 — Hypertrophy/Basics/Ultra/Intense
// ---------------------------------------------------------------------------

describe('TEST-02: zip 3155 — Hypertrophy/Basics/Ultra/Intense', () => {
  it('Order token: font-weight is "600" (Hypertrophy)', () => {
    expect(css3155['--ppl-weight-font-weight']).toBe('600');
  });

  it('Order token: density is "moderate" (Hypertrophy)', () => {
    expect(css3155['--ppl-weight-density']).toBe('moderate');
  });

  it('Saturation >= 0.85 (Intense = maximum effort)', () => {
    const sat = parseFloat(css3155['--ppl-weight-saturation']!);
    expect(sat).toBeGreaterThanOrEqual(0.85);
  });

  it('Tonal name is "passion" (Intense Color)', () => {
    expect(css3155['--ppl-weight-tonal-name']).toBe('passion');
  });

  it('Axis gradient direction is "to bottom" (Basics)', () => {
    expect(css3155['--ppl-weight-gradient-direction']).toBe('to bottom');
  });
});

// ---------------------------------------------------------------------------
// TEST-02: Zip 6526 — Balance/Time/Pull/Circuit
// NOTE: Color position 6 = Circuit (🟠 connection), not Fun.
//       Fun = position 7. Actual pipeline resolves C=6 → Circuit.
// ---------------------------------------------------------------------------

describe('TEST-02: zip 6526 — Balance/Time/Pull/Circuit', () => {
  it('Order token: font-weight is "400" (Balance)', () => {
    expect(css6526['--ppl-weight-font-weight']).toBe('400');
  });

  it('Order token: density is "moderate" (Balance)', () => {
    expect(css6526['--ppl-weight-density']).toBe('moderate');
  });

  it('Saturation is "0.70" (Circuit = station energy)', () => {
    expect(css6526['--ppl-weight-saturation']).toBe('0.70');
  });

  it('Tonal name is "connection" (Circuit Color)', () => {
    expect(css6526['--ppl-weight-tonal-name']).toBe('connection');
  });

  it('Axis gradient direction is "to right" (Time)', () => {
    expect(css6526['--ppl-weight-gradient-direction']).toBe('to right');
  });
});
