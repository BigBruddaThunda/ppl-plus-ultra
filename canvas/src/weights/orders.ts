/**
 * Order Weight Tables
 *
 * 7 entries (positions 1–7): Foundation through Restoration.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const ORDERS_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — 🐂 Foundation
  // "Pattern learning at sub-maximal load. The on-ramp for any new skill."
  // "If load exceeds 65%, reps drop below 8, or difficulty exceeds 2 — it is not 🐂"
  // Block sequence: ♨️ 🔢/🛠 🧈 🧩 🧬 🚂
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      6, // ♨️ Always first, extended in Foundation
      [W.FUNDAMENTALS]: 8, // 🔢 Core block for Foundation — re-grounding in basics
      [W.BREAD_BUTTER]: 6, // 🧈 Always present, carries main volume
      [W.SUPPLEMENTAL]: 4, // 🧩 Secondary work supports pattern learning
      [W.IMPRINT]:      6, // 🧬 Locking in patterns — high affinity for Foundation
      [W.JUNCTION]:     4, // 🚂 Bridge to next session
      [W.CRAFT]:        6, // 🛠 Skill acquisition — strongly relevant to Foundation
      [W.TEACHING]:     4, // ⚫ Teaching color fits Foundation character
      [W.BODYWEIGHT]:   2, // 🟢 Sub-maximal patterns work bodyweight-first
    },
    suppressions: {
      // CLAUDE.md: "Never in 🐂" — Gutter is all-out effort, contradicts Foundation ceiling
      [W.GUTTER]:       -8,
      // CLAUDE.md: "difficulty ceiling" — Challenge axis contradicts 2/5 max difficulty
      [W.CHALLENGE]:    -4,
      // CLAUDE.md: "Not 🏟 — testing, not training"
      [W.PERFORMANCE]:  -4,
      // CLAUDE.md: "🏟 blocks hypertrophy-style accumulation by default"
      [W.INTENSE]:      -4,
      // Foundation is sub-maximal — high-load Strength order contradicts
      [W.STRENGTH]:     -2,
    },
  },

  // -------------------------------------------------------------------------
  // 2 — ⛽ Strength
  // "Neural adaptation. Heavy loads, low reps, full recovery. Force production."
  // "The pump is irrelevant here."
  // Block sequence: ♨️ ▶️ 🧈 🧩 🪫 🚂
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Needed but not extended
      [W.PRIMER]:       6, // ▶️ CNS activation — essential for Strength
      [W.BREAD_BUTTER]: 8, // 🧈 Most volume, most stimulus
      [W.SUPPLEMENTAL]: 4, // 🧩 Secondary work supports main lift
      [W.RELEASE]:      4, // 🪫 Neural discharge after high CNS demand
      [W.JUNCTION]:     4, // 🚂 Session bridge
      [W.PROGRESSION]:  4, // 🪜 Loading ramps common in Strength
      [W.STRUCTURED]:   4, // 🔵 Structured format fits Strength well
      [W.TECHNICAL]:    4, // 🟣 Technical color fits precision loading
      [W.BASICS]:       2, // 🏛 Barbell classics align with Strength
    },
    suppressions: {
      // CLAUDE.md: "The pump is irrelevant here" — Vanity is pump work
      [W.VANITY]:       -4,
      // CLAUDE.md: "ARAM -4" cited in weight-system-spec.md example
      [W.ARAM]:         -4,
      // CLAUDE.md: Restoration contradicts heavy loading
      [W.RESTORATION]:  -4,
      // CLAUDE.md: Hypertrophy-style volume accumulation not the goal
      [W.SCULPT]:       -2,
      // Circuit format conflicts with 3–4 min rest requirement
      [W.CIRCUIT]:      -4,
    },
  },

  // -------------------------------------------------------------------------
  // 3 — 🦋 Hypertrophy
  // "Muscle growth through volume and metabolic stress. The pump matters."
  // Block sequence: ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Standard warm-up
      [W.PRIMER]:       4, // ▶️ CNS priming
      [W.BREAD_BUTTER]: 8, // 🧈 Main hypertrophy volume
      [W.SCULPT]:       6, // 🗿 Hypertrophy shaping — strong affinity
      [W.VANITY]:       4, // 🪞 Pump work — CLAUDE.md: "The pump matters"
      [W.SUPPLEMENTAL]: 6, // 🧩 Accessory volume high in Hypertrophy
      [W.RELEASE]:      4, // 🪫 Post-volume discharge
      [W.JUNCTION]:     4, // 🚂 Bridge
      [W.AESTHETIC]:    2, // 🌹 Aesthetic axis compatible
    },
    suppressions: {
      // CLAUDE.md: "Performance -4" — testing contradicts accumulation
      [W.PERFORMANCE]:  -4,
      // CLAUDE.md: Restoration contradicts moderate-high load accumulation
      [W.RESTORATION]:  -4,
      // Heavy strength loading contradicts 65–75% ceiling
      [W.STRENGTH]:     -2,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — 🏟 Performance
  // "Testing, not training. You test, record, and leave. No junk volume."
  // "🏟 blocks hypertrophy-style accumulation by default."
  // Block sequence: ♨️ 🪜 🧈 🚂 (3–4 blocks ONLY)
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Prepare for maximal effort
      [W.PROGRESSION]:  6, // 🪜 Loading ramp to test — essential
      [W.BREAD_BUTTER]: 8, // 🧈 The test itself
      [W.JUNCTION]:     6, // 🚂 Record and log — critical for Performance
      [W.TECHNICAL]:    4, // 🟣 Precision execution at max loads
    },
    suppressions: {
      // CLAUDE.md: "No junk volume after the test" — Vanity is junk volume
      [W.VANITY]:       -8,
      // CLAUDE.md: "No junk volume" — Sculpt is accumulation work
      [W.SCULPT]:       -8,
      // CLAUDE.md: "No junk volume" — Supplemental after test forbidden
      [W.SUPPLEMENTAL]: -6,
      // CLAUDE.md: "No exceptions. No junk volume" — ARAM is volume/circuit
      [W.ARAM]:         -6,
      // Restoration contradicts maximal effort testing
      [W.RESTORATION]:  -6,
      // Hypertrophy accumulation contradicts test-and-leave protocol
      [W.HYPERTROPHY]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 5 — 🌾 Full Body
  // "Integration. Movements must flow into each other as one unified pattern."
  // "Flow and Unity Test is mandatory"
  // Block sequence: ♨️ 🎼 🧈 🧩 🪫 🚂
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Standard
      [W.COMPOSITION]:  8, // 🎼 Movement arrangement — CLAUDE.md: "Strong in 🌾 Full Body"
      [W.BREAD_BUTTER]: 6, // 🧈 Main integration sequence
      [W.SUPPLEMENTAL]: 4, // 🧩 Secondary integration work
      [W.RELEASE]:      4, // 🪫 Post-integration
      [W.JUNCTION]:     4, // 🚂 Bridge
      [W.PLUS]:         4, // ➕ Full body power / core integrates well
    },
    suppressions: {
      // CLAUDE.md: "Full Body is not a superset. It is integration." — Circuit is list-not-integration
      [W.CIRCUIT]:      -4,
      // Performance's test-and-leave conflicts with integration flow
      [W.PERFORMANCE]:  -4,
      // Vanity (pump/isolation) contradicts flow requirement
      [W.VANITY]:       -4,
    },
  },

  // -------------------------------------------------------------------------
  // 6 — ⚖ Balance
  // "Correction. Microscope on weak links and asymmetries."
  // Block sequence: ♨️ 🏗 🧈 🧩 🪫 🚂
  // -------------------------------------------------------------------------
  [6]: {
    self: 8,
    affinities: {
      [W.WARM_UP]:      4, // ♨️ Standard
      [W.REFORMANCE]:   8, // 🏗 Corrective construction — CLAUDE.md: "+6 in Balance"
      [W.BREAD_BUTTER]: 6, // 🧈 Targeted accessory compounds
      [W.SUPPLEMENTAL]: 6, // 🧩 Correction-focused accessory work
      [W.RELEASE]:      4, // 🪫 Release after corrective work
      [W.JUNCTION]:     4, // 🚂 Bridge to continued correction
      [W.FUNCTIONAL]:   2, // 🔨 Unilateral work common in Balance
    },
    suppressions: {
      // Gutter contradicts correction work
      [W.GUTTER]:       -6,
      // Max performance testing contradicts microscopic correction
      [W.PERFORMANCE]:  -4,
      // High CNS demand of Strength contradicts corrective focus
      [W.STRENGTH]:     -2,
    },
  },

  // -------------------------------------------------------------------------
  // 7 — 🖼 Restoration
  // "Recovery without training debt. You leave fresher than you entered."
  // "Extended scope: somatic movement, TRE, pelvic floor, deep hip work, diaphragmatic breathing"
  // Block sequence: 🎯 🪫 🧈 🧬 🚂
  // -------------------------------------------------------------------------
  [7]: {
    self: 8,
    affinities: {
      [W.INTENTION]:    8, // 🎯 Restoration opens with Intention (block order: 🎯 first)
      [W.RELEASE]:      8, // 🪫 CLAUDE.md: "🪫 prominent in ⚪ and 🖼"
      [W.BREAD_BUTTER]: 6, // 🧈 Main mobility/somatic sequence
      [W.IMPRINT]:      6, // 🧬 Locking in body patterns
      [W.JUNCTION]:     4, // 🚂 Bridge
      [W.MINDFUL]:      6, // ⚪ Mindful color deeply compatible
      [W.AESTHETIC]:    4, // 🌹 Somatic/aesthetic lens — CLAUDE.md: "lens turns inward"
    },
    suppressions: {
      // CLAUDE.md: "Do not place 🌋 Gutter in 🖼 Restoration"
      [W.GUTTER]:       -8,
      // CLAUDE.md: "Heavy loading contradicts <=55% ceiling" — Strength is 75–85%
      [W.STRENGTH]:     -6,
      // CLAUDE.md: Performance contradicts recovery intent
      [W.PERFORMANCE]:  -8,
      // CLAUDE.md: Intense color contradicts restoration character
      [W.INTENSE]:      -6,
      // CLAUDE.md: Mitto -6 (dispatch/launch contradicts recovery)
      [W.MITTO]:        -6,
      // High CNS blocks
      [W.HYPERTROPHY]:  -4,
      [W.PRIMER]:       -4,
    },
  },

};
