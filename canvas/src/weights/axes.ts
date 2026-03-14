/**
 * Axis Weight Tables
 *
 * 6 entries (positions 1–6): Basics through Partner.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const AXES_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — 🏛 Basics (Firmitas)
  // "Bilateral, stable, time-tested fundamentals. Barbell classics first."
  // "Priority: Barbell > dumbbell. Bilateral > unilateral. Compound > isolation."
  // Operator pair: 📍 pono (preparatory) / 🤌 facio (expressive)
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.FACIO]:        6, // 🤌 Expressive operator for Basics — CLAUDE.md operator table
      [W.PONO]:         6, // 📍 Preparatory operator for Basics — CLAUDE.md operator table
      [W.STRUCTURED]:   4, // 🔵 Structured format matches barbell classics
      [W.TECHNICAL]:    4, // 🟣 Technical precision for barbell work
      [W.BREAD_BUTTER]: 6, // 🧈 Classics as main work
      [W.PRIMER]:       4, // ▶️ Barbell work benefits from CNS priming
      [W.PROGRESSION]:  4, // 🪜 Loading ramps common with barbell
      [W.STRENGTH]:     2, // ⛽ Strength aligns with barbell classics
    },
    suppressions: {
      // CLAUDE.md: "Basics/Aesthetic mutual suppression" — opposite character
      [W.AESTHETIC]:    -4,
      // CLAUDE.md: "Functional/Basics tension" — unilateral vs. bilateral bias
      [W.CHALLENGE]:    -2,
      // CLAUDE.md: Isolation work contradicts compound bias
      [W.VANITY]:       -2,
    },
  },

  // -------------------------------------------------------------------------
  // 2 — 🔨 Functional (Utilitas)
  // "Unilateral, standing, athletic-transfer movements."
  // "Priority: Unilateral > bilateral. Standing > seated. Free weight > machine."
  // Operator pair: 🧸 fero (preparatory) / 🥨 tendo (expressive)
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.FERO]:         6, // 🧸 Preparatory operator for Functional — CLAUDE.md operator table
      [W.TENDO]:        6, // 🥨 Expressive operator for Functional — CLAUDE.md operator table
      [W.BODYWEIGHT]:   4, // 🟢 Bodyweight supports unilateral/standing work
      [W.CHALLENGE]:    4, // 🪐 Challenge axis aligns — hardest variation
      [W.BREAD_BUTTER]: 6, // 🧈 Main functional compound work
      [W.EXPOSURE]:     4, // 🌎 Revealing weaknesses through movement
      [W.BALANCE]:      4, // ⚖ Balance order uses functional movements
    },
    suppressions: {
      // CLAUDE.md: "Functional/Aesthetic suppression -4" — opposite priorities
      [W.AESTHETIC]:    -4,
      // Machine/seated work contradicts Functional bias
      [W.VANITY]:       -2,
      // Bilateral barbell bias contradicts unilateral priority
      [W.BASICS]:       -2,
    },
  },

  // -------------------------------------------------------------------------
  // 3 — 🌹 Aesthetic (Venustas)
  // "Isolation, full ROM, mind-muscle connection. Feel over load."
  // "Priority: Isolation > compound. Cable/machine > barbell. Feeling > load."
  // "In 🖼 Restoration context: lens turns inward — pelvic floor, psoas, diaphragm."
  // Operator pair: 👀 specio (preparatory) / 🦢 plico (expressive)
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.SPECIO]:       6, // 👀 Preparatory operator for Aesthetic — CLAUDE.md operator table
      [W.PLICO]:        6, // 🦢 Expressive operator for Aesthetic — CLAUDE.md operator table
      [W.VANITY]:       8, // 🪞 Pump/mirror work — Aesthetic's home block
      [W.SCULPT]:       6, // 🗿 Carving with isolation — strong affinity
      [W.MINDFUL]:      4, // ⚪ Mindful format fits slow eccentric isolation
      [W.HYPERTROPHY]:  4, // 🦋 Hypertrophy uses isolation extensively
      [W.RESTORATION]:  4, // 🖼 Somatic/aesthetic lens in Restoration
      [W.IMPRINT]:      4, // 🧬 Mind-muscle → imprint patterns
    },
    suppressions: {
      // CLAUDE.md: "Basics/Aesthetic mutual suppression" — compound vs. isolation
      [W.BASICS]:       -4,
      // CLAUDE.md: "Functional/Aesthetic suppression" — unilateral vs. isolation
      [W.FUNCTIONAL]:   -4,
      // Heavy loading contradicts "Feel over load"
      [W.STRENGTH]:     -2,
      // Performance testing contradicts mind-muscle focus
      [W.PERFORMANCE]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — 🪐 Challenge (Gravitas)
  // "Hardest variation at any level. Deficit, pause, tempo, bands, chains."
  // "Always the hardest version they can control."
  // Operator pair: 🪵 teneo (preparatory) / 🚀 mitto (expressive)
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.TENEO]:        6, // 🪵 Preparatory operator for Challenge — CLAUDE.md operator table
      [W.MITTO]:        6, // 🚀 Expressive operator for Challenge — CLAUDE.md operator table
      [W.GUTTER]:       4, // 🌋 Gutter fits high-challenge contexts (only in 🔴 and 🪐)
      [W.TECHNICAL]:    4, // 🟣 Technical precision for hardest variations
      [W.GAMBIT]:       4, // ♟️ Deliberate sacrifice — fits Challenge character
      [W.PERFORMANCE]:  4, // 🏟 Testing at the edge aligns with Challenge
      [W.INTENSE]:      4, // 🔴 Maximum effort fits Challenge
      [W.CRAFT]:        4, // 🛠 Skill acquisition at hard variations
    },
    suppressions: {
      // CLAUDE.md: Foundation's difficulty ceiling (2/5) conflicts with Challenge
      [W.FOUNDATION]:   -4,
      // Mindful slow tempo contradicts hardest-variation bias
      [W.MINDFUL]:      -4,
      // Restoration contradicts pushing to limits
      [W.RESTORATION]:  -4,
    },
  },

  // -------------------------------------------------------------------------
  // 5 — ⌛ Time (Temporitas)
  // "Enables: EMOM, AMRAP, density blocks, timed sets, time trials, TUT."
  // "The specific protocol comes from Order × Color."
  // Operator pair: 🐋 duco (preparatory) / ✒️ grapho (expressive)
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.DUCO]:         6, // 🐋 Preparatory operator for Time — CLAUDE.md operator table
      [W.GRAPHO]:       6, // ✒️ Expressive operator for Time — CLAUDE.md operator table
      [W.ARAM]:         6, // 🎱 AMRAP/timed station loops — core Time expression
      [W.STRUCTURED]:   4, // 🔵 EMOM = structured time protocols
      [W.INTENSE]:      4, // 🔴 AMRAP/density = Intense time format
      [W.CIRCUIT]:      4, // 🟠 Timed circuits use Time axis
      [W.IMPRINT]:      2, // 🧬 TUT (time under tension) imprints patterns
    },
    suppressions: {
      // Standard rest-based protocols contradict time-based structure
      [W.PROGRESSION]:  -2,
    },
  },

  // -------------------------------------------------------------------------
  // 6 — 🐬 Partner (Sociatas)
  // "Enables: Spottable, alternating, synchronized, competitive, assisted."
  // "Machine work deprioritized. Surfaces exercises that work with another person."
  // Operator pair: 🧲 capio (preparatory) / 🦉 logos (expressive)
  // -------------------------------------------------------------------------
  [6]: {
    self: 8,
    affinities: {
      [W.CAPIO]:        6, // 🧲 Preparatory operator for Partner — CLAUDE.md operator table
      [W.LOGOS]:        6, // 🦉 Expressive operator for Partner — CLAUDE.md operator table
      [W.SANDBOX]:      4, // 🏖 Constrained exploration works well with partner
      [W.EXPOSURE]:     4, // 🌎 Partner reveals weaknesses
      [W.FUN]:          4, // 🟡 Partner workouts skew playful
      [W.CRAFT]:        4, // 🛠 Teaching a partner = skill context
    },
    suppressions: {
      // Machine work deprioritized — isolation machines don't partner well
      [W.VANITY]:       -2,
    },
  },

};
