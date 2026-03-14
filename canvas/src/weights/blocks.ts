/**
 * Block Weight Tables
 *
 * 22 entries (positions 1–22): Warm-Up through Choice.
 * Block weights express which Orders/Colors/Axes make each block more or less relevant.
 * NOT consumed by computeRawVector() — used by downstream block-selection systems.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const BLOCKS_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — ♨️ Warm-Up (Orientation/Access)
  // "Always present. Always first (unless 🎯 opens). Content shifts by Order."
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.RESTORATION]:  4, // Extended warm-up in Restoration
      [W.MINDFUL]:      6, // CLAUDE.md: "extended ♨️ in ⚪"
      [W.FOUNDATION]:   4, // Warm-up is prominent in Foundation
    },
    suppressions: {},
  },

  // -------------------------------------------------------------------------
  // 2 — 🎯 Intention (Orientation)
  // "One sentence. Quoted. Active voice."
  // "🖼 opens with 🎯"
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.RESTORATION]:  8, // CLAUDE.md: "🖼 Restoration: 🎯 opens the session"
      [W.MINDFUL]:      6, // Mindful framing benefits from explicit intention
      [W.TEACHING]:     4, // Teaching frames the work
    },
    suppressions: {},
  },

  // -------------------------------------------------------------------------
  // 3 — 🔢 Fundamentals (Access)
  // "Re-grounding in basics. Post-injury, post-layoff, teaching contexts."
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.FOUNDATION]:   8, // CLAUDE.md: Foundation block sequence includes 🔢
      [W.TEACHING]:     6, // Fundamentals = Teaching color affinity
      [W.CRAFT]:        4, // Skill contexts use Fundamentals
    },
    suppressions: {
      // Fundamentals is not relevant to high-performance testing
      [W.PERFORMANCE]:  -4,
      // Restoration uses different opening blocks
      [W.RESTORATION]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — 🧈 Bread & Butter (Transformation)
  // "The main thing. Always present. Most volume. Most stimulus."
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.FOUNDATION]:   6, // Always present in Foundation
      [W.STRENGTH]:     8, // Core Strength block
      [W.HYPERTROPHY]:  8, // Core Hypertrophy block
      [W.PERFORMANCE]:  8, // The test itself in Performance
      [W.FULL_BODY]:    8, // Integration sequence in Full Body
      [W.BALANCE]:      6, // Targeted correction work
      [W.RESTORATION]:  6, // Main mobility/somatic sequence
    },
    suppressions: {},
  },

  // -------------------------------------------------------------------------
  // 5 — 🫀 Circulation (Access)
  // "Blood flow, tissue prep. Early or mid-session."
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.ULTRA]:        4, // Cardiovascular type benefits from circulation
      [W.FULL_BODY]:    4, // Full Body flow benefits from circulation prep
    },
    suppressions: {},
  },

  // -------------------------------------------------------------------------
  // 6 — ▶️ Primer (Access)
  // "CNS activation. Bridges warm-up to main work. Neural potentiation."
  // -------------------------------------------------------------------------
  [6]: {
    self: 8,
    affinities: {
      [W.STRENGTH]:     6, // CLAUDE.md: Strength block sequence includes ▶️
      [W.HYPERTROPHY]:  4, // Hypertrophy benefits from CNS priming
      [W.PERFORMANCE]:  2, // Ramp to test includes primer
    },
    suppressions: {
      // CLAUDE.md: Restoration contradicts CNS activation
      [W.RESTORATION]:  -4,
      // Mindful slow entry contradicts neural potentiation
      [W.MINDFUL]:      -4,
    },
  },

  // -------------------------------------------------------------------------
  // 7 — 🎼 Composition (Transformation)
  // "Movement arrangement. Strong in 🌾 Full Body. Composite header block."
  // -------------------------------------------------------------------------
  [7]: {
    self: 8,
    affinities: {
      [W.FULL_BODY]:    8, // CLAUDE.md: "Strong in 🌾 Full Body"
      [W.PLUS]:         6, // Plus type = full body power flows
    },
    suppressions: {
      // Composition requires integration — contradicts isolation
      [W.AESTHETIC]:    -4,
      [W.VANITY]:       -4,
    },
  },

  // -------------------------------------------------------------------------
  // 8 — ♟️ Gambit (Access)
  // "Deliberate sacrifice for positional advantage. Pre-fatigue with purpose."
  // -------------------------------------------------------------------------
  [8]: {
    self: 8,
    affinities: {
      [W.CHALLENGE]:    4, // Challenge axis uses deliberate difficulty sacrifice
      [W.INTENSE]:      4, // Intense pre-fatigue context
      [W.HYPERTROPHY]:  4, // Pre-fatigue technique common in Hypertrophy
    },
    suppressions: {
      // Pre-fatigue contradicts performance testing integrity
      [W.PERFORMANCE]:  -6,
      // Gambit contradicts Foundation's clean pattern learning
      [W.FOUNDATION]:   -4,
    },
  },

  // -------------------------------------------------------------------------
  // 9 — 🪜 Progression (Access/Transform)
  // "Loading ramps. Ladders. In 🏟: the ramp to the test."
  // -------------------------------------------------------------------------
  [9]: {
    self: 8,
    affinities: {
      [W.PERFORMANCE]:  8, // CLAUDE.md: 🏟 block sequence includes 🪜 as ramp to test
      [W.STRENGTH]:     4, // Loading ramps suit Strength
      [W.STRUCTURED]:   6, // CLAUDE.md: "+🪜 Progression prominent" in Structured
    },
    suppressions: {
      // Time-based protocols don't use loading ramps
      [W.TIME]:         -2,
    },
  },

  // -------------------------------------------------------------------------
  // 10 — 🌎 Exposure (Transformation)
  // "Reveal weaknesses under controlled stress. Expand movement vocabulary."
  // -------------------------------------------------------------------------
  [10]: {
    self: 8,
    affinities: {
      [W.FUN]:          6, // CLAUDE.md: "+🌎 Exposure permitted" in Fun
      [W.BALANCE]:      4, // Exposing weaknesses is Balance's purpose
      [W.FUNCTIONAL]:   4, // Functional reveals real-world deficits
      [W.PARTNER]:      4, // Partner reveals weaknesses
    },
    suppressions: {
      // Performance testing is not exploration — it is measurement
      [W.PERFORMANCE]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 11 — 🎱 ARAM (Transformation)
  // "Station-based loops. Loop logic required. Box notation in markdown."
  // -------------------------------------------------------------------------
  [11]: {
    self: 8,
    affinities: {
      [W.CIRCUIT]:      8, // CLAUDE.md: Circuit color → ARAM is primary block
      [W.ULTRA]:        6, // Conditioning type suits station loops
      [W.TIME]:         6, // Timed rotation suits ARAM
      [W.INTENSE]:      4, // Dense circuits in Intense context
    },
    suppressions: {
      // CLAUDE.md: "🎱 ARAM -4" for Strength (cited in weight-system-spec example)
      [W.STRENGTH]:     -4,
      // CLAUDE.md: "no barbells in Circuit/ARAM"
      [W.TECHNICAL]:    -4,
      // Performance's 3-4 block limit contradicts ARAM addition
      [W.PERFORMANCE]:  -6,
    },
  },

  // -------------------------------------------------------------------------
  // 12 — 🌋 Gutter (Transformation)
  // "All-out effort. Rare. Only in 🔴 and 🪐."
  // -------------------------------------------------------------------------
  [12]: {
    self: 8,
    affinities: {
      [W.INTENSE]:      6, // CLAUDE.md: "only in 🔴 and 🪐" — Intense unlocks Gutter
      [W.CHALLENGE]:    4, // CLAUDE.md: "only in 🔴 and 🪐" — Challenge axis fits
    },
    suppressions: {
      // CLAUDE.md: "Never in 🖼 Restoration"
      [W.RESTORATION]:  -8,
      // CLAUDE.md: "Never in 🐂 Foundation"
      [W.FOUNDATION]:   -8,
      // CLAUDE.md: "Never in ⚪ Mindful"
      [W.MINDFUL]:      -8,
      // Bodyweight hard exclusion — all-out max effort needs resistance
      [W.BODYWEIGHT]:   -4,
      // Balance correction contradicts all-out effort
      [W.BALANCE]:      -6,
      // Teaching is comprehension, not all-out effort
      [W.TEACHING]:     -6,
    },
  },

  // -------------------------------------------------------------------------
  // 13 — 🪞 Vanity (Transformation)
  // "Appearance-driven. Pump work. Mirror muscles. Honest. Stigma-free."
  // -------------------------------------------------------------------------
  [13]: {
    self: 8,
    affinities: {
      [W.HYPERTROPHY]:  6, // Core Hypertrophy block (pump matters)
      [W.AESTHETIC]:    6, // Aesthetic axis = isolation/pump
      [W.INTENSE]:      4, // Pump work in Intense context
    },
    suppressions: {
      // CLAUDE.md: "Vanity -8 in Performance" (no junk volume)
      [W.PERFORMANCE]:  -8,
      // CLAUDE.md: "The pump is irrelevant" in Strength
      [W.STRENGTH]:     -6,
      // Restoration is not pump work
      [W.RESTORATION]:  -6,
    },
  },

  // -------------------------------------------------------------------------
  // 14 — 🗿 Sculpt (Transformation)
  // "Hypertrophy shaping. Angles, tension, volume. Carving not admiring."
  // -------------------------------------------------------------------------
  [14]: {
    self: 8,
    affinities: {
      [W.HYPERTROPHY]:  8, // CLAUDE.md: Hypertrophy block sequence includes 🗿
      [W.AESTHETIC]:    6, // Aesthetic axis = sculpting focus
      [W.INTENSE]:      4, // High volume sculpting in Intense
    },
    suppressions: {
      // CLAUDE.md: "Sculpt -8 in Performance" (no junk volume)
      [W.PERFORMANCE]:  -8,
      // Sculpt contradicts Restoration recovery
      [W.RESTORATION]:  -6,
      // Foundation is about pattern, not sculpting
      [W.FOUNDATION]:   -4,
    },
  },

  // -------------------------------------------------------------------------
  // 15 — 🛠 Craft (Transformation)
  // "Skill acquisition. Quality over load."
  // "Filters toward ⚫ and 🟣"
  // -------------------------------------------------------------------------
  [15]: {
    self: 8,
    affinities: {
      [W.TEACHING]:     8, // CLAUDE.md: "filters toward ⚫ Teaching"
      [W.TECHNICAL]:    6, // CLAUDE.md: "filters toward 🟣 Technical"
      [W.FOUNDATION]:   6, // Foundation is skill acquisition
      [W.CHALLENGE]:    4, // Learning hardest variation
    },
    suppressions: {
      // Maximum effort contradicts skill quality focus
      [W.INTENSE]:      -4,
      // Performance testing is not skill building
      [W.PERFORMANCE]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 16 — 🧩 Supplemental (Transformation)
  // "Secondary work. Supports 🧈. Must be non-redundant. Different angles."
  // -------------------------------------------------------------------------
  [16]: {
    self: 8,
    affinities: {
      [W.STRENGTH]:     4, // Strength includes supplemental accessory
      [W.HYPERTROPHY]:  6, // High supplemental volume in Hypertrophy
      [W.BALANCE]:      6, // Correction work is supplemental
      [W.RESTORATION]:  2, // Light supplemental mobility
    },
    suppressions: {
      // CLAUDE.md: "No junk volume" in Performance — supplemental = junk volume
      [W.PERFORMANCE]:  -6,
    },
  },

  // -------------------------------------------------------------------------
  // 17 — 🪫 Release (Retention)
  // "Context-dependent: 🔴 = stress OUT. ⚪ = tension DOWN. 🖼 = return to baseline."
  // -------------------------------------------------------------------------
  [17]: {
    self: 8,
    affinities: {
      [W.INTENSE]:      6, // Cathartic discharge after Intense
      [W.MINDFUL]:      8, // CLAUDE.md: "extended 🪫 in ⚪"
      [W.RESTORATION]:  8, // Core Restoration retention block
      [W.STRENGTH]:     4, // Neural discharge after CNS demand
    },
    suppressions: {
      // Performance is test-and-leave — no extended release
      [W.PERFORMANCE]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 18 — 🏖 Sandbox (Transformation)
  // "Constrained exploration."
  // "🟡 = play. ⚫ = safe learning. 🟣 = skill testing."
  // -------------------------------------------------------------------------
  [18]: {
    self: 8,
    affinities: {
      [W.FUN]:          8, // CLAUDE.md: "+🏖 Sandbox" for Fun — primary Fun block
      [W.TEACHING]:     4, // CLAUDE.md: "⚫ = safe learning"
      [W.TECHNICAL]:    4, // CLAUDE.md: "🟣 = skill testing"
      [W.PARTNER]:      4, // Sandbox exploration with partner
    },
    suppressions: {
      // Performance is not exploration — it is measurement
      [W.PERFORMANCE]:  -6,
      // Strength's strict protocol contradicts free exploration
      [W.STRENGTH]:     -4,
    },
  },

  // -------------------------------------------------------------------------
  // 19 — 🏗 Reformance (Transformation)
  // "Corrective construction. Prehab, postural correction. Prominent in ⚖."
  // -------------------------------------------------------------------------
  [19]: {
    self: 8,
    affinities: {
      [W.BALANCE]:      8, // CLAUDE.md: "+6 in ⚖ Balance" — dominant Balance block
      [W.RESTORATION]:  4, // Corrective work in Restoration
      [W.FOUNDATION]:   4, // Pattern correction in Foundation
      [W.TEACHING]:     4, // Reformance in teaching context
    },
    suppressions: {
      // Performance testing is not corrective work
      [W.PERFORMANCE]:  -4,
      // Maximum effort contradicts corrective precision
      [W.INTENSE]:      -4,
    },
  },

  // -------------------------------------------------------------------------
  // 20 — 🧬 Imprint (Retention)
  // "Locking in patterns. High rep, low load, late session. Neural memory."
  // -------------------------------------------------------------------------
  [20]: {
    self: 8,
    affinities: {
      [W.FOUNDATION]:   6, // CLAUDE.md: Foundation block sequence includes 🧬
      [W.RESTORATION]:  6, // CLAUDE.md: Restoration block sequence includes 🧬
      [W.MINDFUL]:      6, // Slow tempo imprints movement patterns
      [W.TEACHING]:     4, // Imprint follows teaching context
    },
    suppressions: {
      // Performance testing is not pattern locking
      [W.PERFORMANCE]:  -4,
      // Maximum effort contradicts high-rep low-load imprint
      [W.INTENSE]:      -4,
    },
  },

  // -------------------------------------------------------------------------
  // 21 — 🚂 Junction (Retention)
  // "Bridge to next session. 1–3 follow-up zip codes with rationale."
  // -------------------------------------------------------------------------
  [21]: {
    self: 8,
    affinities: {
      [W.FOUNDATION]:   4, // Always in Foundation
      [W.STRENGTH]:     4, // Always in Strength
      [W.HYPERTROPHY]:  4, // Always in Hypertrophy
      [W.PERFORMANCE]:  6, // CLAUDE.md: Junction critical in Performance (record PR)
      [W.FULL_BODY]:    4, // Always in Full Body
    },
    suppressions: {},
  },

  // -------------------------------------------------------------------------
  // 22 — 🔠 Choice (Modifier)
  // "Bounded autonomy. Applies to other blocks. Options must be valid."
  // -------------------------------------------------------------------------
  [22]: {
    self: 8,
    affinities: {
      [W.TEACHING]:     4, // Pedagogical choice
      [W.FUN]:          4, // Playful autonomy
      [W.BODYWEIGHT]:   2, // Equipment flexibility choices
    },
    suppressions: {
      // Technical precision is not a choice context
      [W.TECHNICAL]:    -2,
    },
  },

};
