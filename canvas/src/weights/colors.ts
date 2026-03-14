/**
 * Color Weight Tables
 *
 * 8 entries (positions 1–8): Teaching through Mindful.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const COLORS_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — ⚫ Teaching
  // Tier 2–3. GOLD: No.
  // "Extra rest, coaching cues, comprehension over exertion"
  // Color modifier: "+extended rest, +🛠 Craft emphasis"
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.CRAFT]:        8, // 🛠 CLAUDE.md: "+🛠 Craft emphasis" for Teaching
      [W.FUNDAMENTALS]: 6, // 🔢 Foundation/Teaching — re-grounding
      [W.WARM_UP]:      4, // ♨️ Extended warm-up in Teaching context
      [W.SANDBOX]:      4, // 🏖 CLAUDE.md: "⚫ = safe learning" in Sandbox
      [W.INTENTION]:    4, // 🎯 Framing the work is important in Teaching
    },
    suppressions: {
      // CLAUDE.md: GOLD gate — Teaching does not unlock GOLD exercises
      [W.GUTTER]:       -8,
      // Teaching is comprehension over exertion — maximum effort contradicts
      [W.INTENSE]:      -6,
      // Teaching is not performance testing
      [W.PERFORMANCE]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 2 — 🟢 Bodyweight
  // Tier 0–2. GOLD: No.
  // "No gym required. Park, hotel, living room."
  // "No barbells in 🟢 Bodyweight"
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Bodyweight warm-up
      [W.BREAD_BUTTER]: 4, // 🧈 Bodyweight main work
      [W.SANDBOX]:      4, // 🏖 Bodyweight exploration
      [W.FUN]:          4, // 🟡 Bodyweight workouts tend playful
      [W.FUNCTIONAL]:   4, // 🔨 Unilateral/standing bodyweight
    },
    suppressions: {
      // CLAUDE.md: "No barbells in 🟢 Bodyweight" — hard equipment exclusion
      [W.STRENGTH]:     -6,
      // CLAUDE.md: "No barbells" — Tier 3+ equipment excluded
      [W.TECHNICAL]:    -4,
      // CLAUDE.md: Tier 4+ machines excluded
      [W.VANITY]:       -2,
      // GOLD gate: Teaching does not unlock GOLD
      [W.GUTTER]:       -8,
    },
  },

  // -------------------------------------------------------------------------
  // 3 — 🔵 Structured
  // Tier 2–3. GOLD: No.
  // "Prescribed sets/reps/rest. Trackable. Repeatable."
  // Color modifier: "+🪜 Progression prominent"
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.PROGRESSION]:  6, // 🪜 CLAUDE.md: "+🪜 Progression prominent" for Structured
      [W.BREAD_BUTTER]: 4, // 🧈 Main prescribed work
      [W.JUNCTION]:     6, // 🚂 Structured logging for progress tracking
      [W.PRIMER]:       4, // ▶️ Structured protocols benefit from CNS priming
      [W.SUPPLEMENTAL]: 4, // 🧩 Structured accessory work
    },
    suppressions: {
      // CLAUDE.md: GOLD gate — Structured does not unlock GOLD
      [W.GUTTER]:       -8,
      // Structured format conflicts with free-form circuit rotation
      [W.ARAM]:         -2,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — 🟣 Technical
  // Tier 2–5. GOLD: Yes.
  // "Precision. Lower volume, extended rest, quality focus."
  // Color modifier: "fewer blocks, extended rest, quality focus"
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.CRAFT]:        6, // 🛠 Technical = skill acquisition and precision
      [W.BREAD_BUTTER]: 4, // 🧈 Technical main work (lower volume)
      [W.WARM_UP]:      4, // ♨️ Extended warm-up for technical preparation
      [W.SPECIO]:       4, // 👀 Observe/inspect — quality monitoring
      [W.LOGOS]:        4, // 🦉 Reason/analyze — technical assessment
    },
    suppressions: {
      // Technical precision contradicts circuit speed
      [W.CIRCUIT]:      -4,
      // Technical = lower volume, ARAM is high-volume rotation
      [W.ARAM]:         -4,
      // High-volume accumulation contradicts technical quality focus
      [W.SCULPT]:       -2,
    },
  },

  // -------------------------------------------------------------------------
  // 5 — 🔴 Intense
  // Tier 2–4. GOLD: Yes.
  // "Maximum effort. High volume. Reduced rest. Supersets OK."
  // Color modifier: "🧩 may superset, 🌋 Gutter possible"
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.GUTTER]:       6, // 🌋 CLAUDE.md: "only in 🔴 and 🪐" — Gutter unlocked
      [W.BREAD_BUTTER]: 6, // 🧈 High-volume main work
      [W.SUPPLEMENTAL]: 6, // 🧩 CLAUDE.md: "🧩 may superset" in Intense
      [W.SCULPT]:       4, // 🗿 High volume shaping
      [W.VANITY]:       4, // 🪞 Pump work in maximum effort context
      [W.ARAM]:         4, // 🎱 Supersets/density circuits
      [W.PLICO]:        4, // 🦢 Superset layering operator
      [W.RELEASE]:      4, // 🪫 Stress discharge after intense work
    },
    suppressions: {
      // CLAUDE.md: "opposite character" — Mindful and Intense are polar opposites
      [W.MINDFUL]:      -6,
      // CLAUDE.md: Restoration contradicts maximum effort
      [W.RESTORATION]:  -6,
      // Teaching (comprehension) contradicts maximum effort
      [W.TEACHING]:     -4,
    },
  },

  // -------------------------------------------------------------------------
  // 6 — 🟠 Circuit
  // Tier 0–3. GOLD: No.
  // "Station-based timed rotation. No barbells. Loop logic required."
  // "Every station must change which tissue is working."
  // -------------------------------------------------------------------------
  [6]: {
    self: 8,
    affinities: {
      [W.ARAM]:         8, // 🎱 CLAUDE.md: "🎱 ARAM" is the circuit block — strong affinity
      [W.WARM_UP]:      4, // ♨️ Standard
      [W.RELEASE]:      4, // 🪫 Recovery loop
      [W.JUNCTION]:     4, // 🚂 Post-circuit logging
      [W.ULTRA]:        6, // ➖ Conditioning type suits circuits
      [W.FUN]:          4, // 🟡 Circuit has playful energy
      [W.TIME]:         4, // ⌛ Timed rotation = Time axis
    },
    suppressions: {
      // CLAUDE.md: "No barbells in 🟠 Circuit" — hard equipment exclusion
      [W.STRENGTH]:     -8,
      // CLAUDE.md: GOLD gate — Circuit does not unlock GOLD
      [W.GUTTER]:       -8,
      // CLAUDE.md: Performance testing contradicts station rotation
      [W.PERFORMANCE]:  -6,
      // Technical precision contradicts circuit speed
      [W.TECHNICAL]:    -4,
      // Strength loading blocks contradict timed circuit
      [W.PROGRESSION]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 7 — 🟡 Fun
  // Tier 0–5. GOLD: No.
  // "Exploration and variety. Structured play within constraints."
  // Color modifier: "+🏖 Sandbox and 🌎 Exposure permitted"
  // -------------------------------------------------------------------------
  [7]: {
    self: 8,
    affinities: {
      [W.SANDBOX]:      8, // 🏖 CLAUDE.md: "+🏖 Sandbox" for Fun — primary Fun block
      [W.EXPOSURE]:     6, // 🌎 CLAUDE.md: "+🌎 Exposure permitted" for Fun
      [W.WARM_UP]:      4, // ♨️ Play starts with movement
      [W.BREAD_BUTTER]: 4, // 🧈 Fun has a main event too
      [W.JUNCTION]:     4, // 🚂 Log the play session
    },
    suppressions: {
      // CLAUDE.md: GOLD gate — Fun does not unlock GOLD
      [W.GUTTER]:       -8,
      // Fun contradicts strict technical precision
      [W.TECHNICAL]:    -2,
      // Fun contradicts maximum effort intensity
      [W.INTENSE]:      -2,
    },
  },

  // -------------------------------------------------------------------------
  // 8 — ⚪ Mindful
  // Tier 0–3. GOLD: No.
  // "Slow tempo (4s eccentrics). Extended rest (2+ min). Breath."
  // Color modifier: "extended ♨️ and 🪫, slow tempo throughout"
  // -------------------------------------------------------------------------
  [8]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      6, // ♨️ CLAUDE.md: "extended ♨️ in Mindful"
      [W.RELEASE]:      8, // 🪫 CLAUDE.md: "extended 🪫 in Mindful" — dominant block
      [W.INTENTION]:    6, // 🎯 Mindful framing — high affinity
      [W.IMPRINT]:      6, // 🧬 Slow tempo imprints movement patterns
      [W.BREAD_BUTTER]: 4, // 🧈 Mindful main work (slow tempo)
      [W.RESTORATION]:  6, // 🖼 Mindful aligns with Restoration character
      [W.TENEO]:        4, // 🪵 Hold/anchor — isometric work in Mindful
      [W.SPECIO]:       4, // 👀 Observe form at slow tempo
    },
    suppressions: {
      // CLAUDE.md: "Do not place 🌋 Gutter in ... ⚪ Mindful"
      [W.GUTTER]:       -8,
      // CLAUDE.md: "opposite character" — Intense and Mindful are polar opposites
      [W.INTENSE]:      -6,
      // CLAUDE.md: GOLD gate — Mindful does not unlock GOLD
      // (Gutter already suppressed above; no additional GOLD items relevant)
      // Maximum effort and Mindful are incompatible
      [W.PERFORMANCE]:  -6,
      // Circuit speed contradicts slow tempo
      [W.CIRCUIT]:      -4,
      // Challenge's max-variation push contradicts mindful slowness
      [W.CHALLENGE]:    -4,
    },
  },

};
