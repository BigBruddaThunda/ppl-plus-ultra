/**
 * saturation-map.ts — Color saturation constants for the rendering pipeline
 *
 * Each Color has a fixed temperament-based saturation level.
 * Saturation is a per-Color constant derived from SCL character descriptions,
 * NOT computed from the numeric weight value in the vector.
 *
 * A zip that activates 🔴 Intense strongly is exactly as saturated as one that
 * barely activates it — the Color identity IS the saturation instruction.
 *
 * Source: CLAUDE.md Color character + weight-css-spec.md § Group 4
 *
 * Keys are W enum positions (19–26) from canvas/src/types/scl.ts:
 *   W.TEACHING   = 19  (⚫ Teaching   — desaturated, focus on content)
 *   W.BODYWEIGHT = 20  (🟢 Bodyweight — natural, present but not vivid)
 *   W.STRUCTURED = 21  (🔵 Structured — neutral, clean, trackable)
 *   W.TECHNICAL  = 22  (🟣 Technical  — precise, quality-focused)
 *   W.INTENSE    = 23  (🔴 Intense    — maximum effort, vivid)
 *   W.CIRCUIT    = 24  (🟠 Circuit    — station energy, engaged)
 *   W.FUN        = 25  (🟡 Fun        — bright, exploratory)
 *   W.MINDFUL    = 26  (⚪ Mindful    — near-monochrome, calm)
 */

import { W } from '../types/scl.js';

/**
 * COLOR_SATURATION maps W enum Color positions (19–26) to saturation values
 * in the range [0.0, 1.0].
 *
 * These values are stable constants reflecting each Color's tonal identity.
 */
export const COLOR_SATURATION: Record<number, number> = {
  [W.TEACHING]:   0.05,  // ⚫ Teaching   — near-monochrome; content not color
  [W.BODYWEIGHT]: 0.40,  // 🟢 Bodyweight — natural; present but not vivid
  [W.STRUCTURED]: 0.50,  // 🔵 Structured — neutral planning blue; clean
  [W.TECHNICAL]:  0.65,  // 🟣 Technical  — precise magnificence; quality-focused
  [W.INTENSE]:    0.90,  // 🔴 Intense    — maximum effort; vivid passion
  [W.CIRCUIT]:    0.70,  // 🟠 Circuit    — station energy; connection engaged
  [W.FUN]:        0.75,  // 🟡 Fun        — play; bright and exploratory
  [W.MINDFUL]:    0.10,  // ⚪ Mindful    — eudaimonia; near-monochrome calm
} as const;
