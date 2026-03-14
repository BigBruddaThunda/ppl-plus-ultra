/**
 * Operator Weight Tables
 *
 * 12 entries (positions 1–12): Capio through Teneo.
 * Operator weights express which Axes/Orders make each operator more or less natural.
 * NOT consumed by computeRawVector() — used by downstream operator-selection systems.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 *
 * Polarity pair mutual suppressions: each preparatory/expressive pair suppresses
 * the other at -4 (they serve opposite polarities of the same axis).
 *
 * CLAUDE.md Operator Table:
 * 🏛 Basics:    📍 pono (prep) / 🤌 facio (expr)
 * 🔨 Functional: 🧸 fero (prep) / 🥨 tendo (expr)
 * 🌹 Aesthetic:  👀 specio (prep) / 🦢 plico (expr)
 * 🪐 Challenge:  🪵 teneo (prep) / 🚀 mitto (expr)
 * ⌛ Time:       🐋 duco (prep) / ✒️ grapho (expr)
 * 🐬 Partner:    🧲 capio (prep) / 🦉 logos (expr)
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const OPERATORS_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — 🧲 Capio (Receive, assess, intake)
  // Home axis: 🐬 Partner (preparatory polarity)
  // "The catching phase. Absorbing eccentric."
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.PARTNER]:      8, // Home axis: 🐬 Partner preparatory
      [W.TEACHING]:     4, // Receiving/absorbing fits Teaching color
      [W.MINDFUL]:      4, // Intake/receive fits Mindful character
      [W.FOUNDATION]:   4, // Receiving new patterns in Foundation
    },
    suppressions: {
      // Polarity pair: Capio (prep) and Logos (expr) suppress each other
      [W.LOGOS]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 2 — 🐋 Duco (Orchestrate, lead, conduct)
  // Home axis: ⌛ Time (preparatory polarity)
  // "Session architecture and tempo flow."
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.TIME]:         8, // Home axis: ⌛ Time preparatory
      [W.MINDFUL]:      4, // Orchestrating slow tempo
      [W.FULL_BODY]:    4, // Conducting integrated flows
    },
    suppressions: {
      // Polarity pair: Duco (prep) and Grapho (expr) suppress each other
      [W.GRAPHO]:       -4,
    },
  },

  // -------------------------------------------------------------------------
  // 3 — 🤌 Facio (Execute, perform, produce)
  // Home axis: 🏛 Basics (expressive polarity)
  // "The concentric. The doing."
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.BASICS]:       8, // Home axis: 🏛 Basics expressive
      [W.STRENGTH]:     6, // Executing heavy loads
      [W.STRUCTURED]:   4, // Prescribed execution = Structured color
      [W.PERFORMANCE]:  4, // Performing the test
    },
    suppressions: {
      // Polarity pair: Facio (expr) and Pono (prep) suppress each other
      [W.PONO]:         -4,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — 🧸 Fero (Carry, transfer, channel)
  // Home axis: 🔨 Functional (preparatory polarity)
  // "Loaded carries. Transfers across sessions."
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.FUNCTIONAL]:   8, // Home axis: 🔨 Functional preparatory
      [W.BODYWEIGHT]:   4, // Carrying your own weight
      [W.PLUS]:         4, // Loaded carries = Plus type
      [W.BALANCE]:      4, // Transfer/carry work in Balance
    },
    suppressions: {
      // Polarity pair: Fero (prep) and Tendo (expr) suppress each other
      [W.TENDO]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 5 — ✒️ Grapho (Write, program, prescribe, document)
  // Home axis: ⌛ Time (expressive polarity)
  // "Record the set. Log the PR."
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.TIME]:         8, // Home axis: ⌛ Time expressive
      [W.PERFORMANCE]:  6, // Log the PR — critical in Performance
      [W.STRUCTURED]:   6, // Structured programming = Grapho
      [W.JUNCTION]:     4, // Junction logging aligns with Grapho
    },
    suppressions: {
      // Polarity pair: Grapho (expr) and Duco (prep) suppress each other
      [W.DUCO]:         -4,
    },
  },

  // -------------------------------------------------------------------------
  // 6 — 🦉 Logos (Reason, assess, analyze, interpret)
  // Home axis: 🐬 Partner (expressive polarity)
  // "Movement quality. Load calc."
  // -------------------------------------------------------------------------
  [6]: {
    self: 8,
    affinities: {
      [W.PARTNER]:      8, // Home axis: 🐬 Partner expressive
      [W.TECHNICAL]:    4, // Analytical assessment fits Technical
      [W.CRAFT]:        4, // Movement quality analysis
      [W.BALANCE]:      4, // Analyzing asymmetries
    },
    suppressions: {
      // Polarity pair: Logos (expr) and Capio (prep) suppress each other
      [W.CAPIO]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 7 — 🚀 Mitto (Dispatch, deploy, launch, commit)
  // Home axis: 🪐 Challenge (expressive polarity)
  // "Explosive intent. Max attempt."
  // -------------------------------------------------------------------------
  [7]: {
    self: 8,
    affinities: {
      [W.CHALLENGE]:    8, // Home axis: 🪐 Challenge expressive
      [W.PERFORMANCE]:  6, // Max attempt = Performance
      [W.INTENSE]:      6, // Maximum effort context
    },
    suppressions: {
      // Polarity pair: Mitto (expr) and Teneo (prep) suppress each other
      [W.TENEO]:        -4,
      // CLAUDE.md: "Mitto -6" for Restoration — launch contradicts recovery
      [W.RESTORATION]:  -6,
      // Mindful slowness contradicts explosive launch
      [W.MINDFUL]:      -4,
    },
  },

  // -------------------------------------------------------------------------
  // 8 — 🦢 Plico (Fold, superset, compress, layer)
  // Home axis: 🌹 Aesthetic (expressive polarity)
  // "Two exercises interwoven."
  // -------------------------------------------------------------------------
  [8]: {
    self: 8,
    affinities: {
      [W.AESTHETIC]:    8, // Home axis: 🌹 Aesthetic expressive
      [W.INTENSE]:      6, // CLAUDE.md: "🧩 may superset" in Intense → Plico
      [W.HYPERTROPHY]:  4, // Superset volume technique
    },
    suppressions: {
      // Polarity pair: Plico (expr) and Specio (prep) suppress each other
      [W.SPECIO]:       -4,
      // Strength's full recovery contradicts superset compression
      [W.STRENGTH]:     -4,
    },
  },

  // -------------------------------------------------------------------------
  // 9 — 📍 Pono (Set, position, assign)
  // Home axis: 🏛 Basics (preparatory polarity)
  // "Stance, grip, body placement. The approach."
  // -------------------------------------------------------------------------
  [9]: {
    self: 8,
    affinities: {
      [W.BASICS]:       8, // Home axis: 🏛 Basics preparatory
      [W.TEACHING]:     6, // Positioning instruction in Teaching
      [W.FOUNDATION]:   6, // Stance and approach in Foundation
      [W.CRAFT]:        4, // Placement precision in skill work
    },
    suppressions: {
      // Polarity pair: Pono (prep) and Facio (expr) suppress each other
      [W.FACIO]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 10 — 👀 Specio (Inspect, observe, assess form, monitor)
  // Home axis: 🌹 Aesthetic (preparatory polarity)
  // "Video. Power leakage."
  // -------------------------------------------------------------------------
  [10]: {
    self: 8,
    affinities: {
      [W.AESTHETIC]:    8, // Home axis: 🌹 Aesthetic preparatory
      [W.TEACHING]:     4, // Observation in teaching context
      [W.TECHNICAL]:    4, // Inspect form at slow/precise loads
      [W.MINDFUL]:      4, // Slow observation fits Mindful
    },
    suppressions: {
      // Polarity pair: Specio (prep) and Plico (expr) suppress each other
      [W.PLICO]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 11 — 🥨 Tendo (Stretch, lengthen, push limits)
  // Home axis: 🔨 Functional (expressive polarity)
  // "Extend ROM. Reach lockout."
  // -------------------------------------------------------------------------
  [11]: {
    self: 8,
    affinities: {
      [W.FUNCTIONAL]:   8, // Home axis: 🔨 Functional expressive
      [W.CHALLENGE]:    6, // Pushing limits — Challenge axis
      [W.RESTORATION]:  4, // Extending ROM in Restoration
    },
    suppressions: {
      // Polarity pair: Tendo (expr) and Fero (prep) suppress each other
      [W.FERO]:         -4,
    },
  },

  // -------------------------------------------------------------------------
  // 12 — 🪵 Teneo (Hold, anchor, persist)
  // Home axis: 🪐 Challenge (preparatory polarity)
  // "Isometrics. Sustained tension. Duration."
  // -------------------------------------------------------------------------
  [12]: {
    self: 8,
    affinities: {
      [W.CHALLENGE]:    8, // Home axis: 🪐 Challenge preparatory
      [W.MINDFUL]:      6, // Sustained holds in Mindful context
      [W.RESTORATION]:  4, // Sustained tension in somatic work
      [W.BALANCE]:      4, // Holding corrective positions
    },
    suppressions: {
      // Polarity pair: Teneo (prep) and Mitto (expr) suppress each other
      [W.MITTO]:        -4,
      // Sustained hold contradicts explosive dispatch
      [W.PERFORMANCE]:  -2,
    },
  },

};
