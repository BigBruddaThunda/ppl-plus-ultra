/**
 * Type Weight Tables
 *
 * 5 entries (positions 1–5): Push through Ultra.
 * All affinities/suppressions derived from CLAUDE.md canonical rules.
 * Every hard suppression (-6 or -8) cites the specific CLAUDE.md rule.
 */

import { W } from '../types/scl.js';
import type { DialWeightTable } from './types.js';

export const TYPES_WEIGHTS: DialWeightTable = {

  // -------------------------------------------------------------------------
  // 1 — 🛒 Push
  // Muscles: Chest, front delts, triceps
  // Primary patterns: Horizontal press, vertical press
  // -------------------------------------------------------------------------
  [1]: {
    self: 8,
    affinities: {
      [W.BREAD_BUTTER]: 6, // 🧈 Main pressing volume
      [W.SUPPLEMENTAL]: 4, // 🧩 Accessory tricep/delt work
      [W.SCULPT]:       4, // 🗿 Chest shaping common in Push
      [W.VANITY]:       4, // 🪞 Mirror muscles — chest, front delt
      [W.PRIMER]:       4, // ▶️ Upper body activation before pressing
    },
    suppressions: {
      // CLAUDE.md: "Direct antagonists" — Push and Pull oppose each other
      [W.PULL]:         -6,
      // Legs is a completely different body region
      [W.LEGS]:         -4,
      // Ultra (cardio) contradicts upper-body pressing
      [W.ULTRA]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 2 — 🪡 Pull
  // Muscles: Lats, rear delts, biceps, traps, erectors
  // Primary patterns: Row, pulldown, hinge
  // -------------------------------------------------------------------------
  [2]: {
    self: 8,
    affinities: {
      [W.BREAD_BUTTER]: 6, // 🧈 Main pulling volume
      [W.SUPPLEMENTAL]: 4, // 🧩 Accessory bicep/rear delt work
      [W.SCULPT]:       4, // 🗿 Back and bicep shaping
      [W.VANITY]:       2, // 🪞 Rear delts, back definition
      [W.PRIMER]:       4, // ▶️ Scapular activation before pulling
      [W.BALANCE]:      4, // ⚖ Pull patterns address posterior chain
    },
    suppressions: {
      // CLAUDE.md: "Direct antagonists" — Pull and Push oppose each other
      [W.PUSH]:         -6,
      // Legs is a completely different body region
      [W.LEGS]:         -4,
      // Ultra (cardio) contradicts upper-body pulling
      [W.ULTRA]:        -4,
    },
  },

  // -------------------------------------------------------------------------
  // 3 — 🍗 Legs
  // Muscles: Quads, hamstrings, glutes, calves
  // Primary patterns: Squat, lunge, hinge, isolation
  // -------------------------------------------------------------------------
  [3]: {
    self: 8,
    affinities: {
      [W.BREAD_BUTTER]: 6, // 🧈 Main leg compound work
      [W.SUPPLEMENTAL]: 4, // 🧩 Isolation accessory (leg extension, curl)
      [W.SCULPT]:       4, // 🗿 Leg shaping (hack squat, leg press angles)
      [W.PRIMER]:       4, // ▶️ Hip/glute activation before legs
      [W.REFORMANCE]:   4, // 🏗 Corrective work common in legs
      [W.BALANCE]:      4, // ⚖ Leg imbalances (adductors, calves)
    },
    suppressions: {
      // Push (upper body) is a different region from Legs
      [W.PUSH]:         -4,
      // Pull (upper body) is a different region from Legs
      [W.PULL]:         -4,
    },
  },

  // -------------------------------------------------------------------------
  // 4 — ➕ Plus
  // Muscles: Full body power, core
  // Primary patterns: Olympic lifts, carries, plyometrics, anti-rotation
  // -------------------------------------------------------------------------
  [4]: {
    self: 8,
    affinities: {
      [W.BREAD_BUTTER]: 6, // 🧈 Main power/core work
      [W.COMPOSITION]:  6, // 🎼 Movement composition — full-body flows
      [W.EXPOSURE]:     6, // 🌎 Reveals full-body capacity
      [W.ARAM]:         4, // 🎱 Power circuits integrate well with Plus
      [W.FULL_BODY]:    4, // 🌾 Full Body order matches Plus well
      [W.PERFORMANCE]:  4, // 🏟 Power testing at 🏟 order
      [W.PLUS]:         8, // Self reference (own W slot)
    },
    suppressions: {
      // Isolation/vanity work contradicts full-body power
      [W.VANITY]:       -4,
    },
  },

  // -------------------------------------------------------------------------
  // 5 — ➖ Ultra
  // Muscles: Cardiovascular system
  // Primary patterns: Rowing, cycling, running, conditioning, flows
  // -------------------------------------------------------------------------
  [5]: {
    self: 8,
    affinities: {
      [W.BREAD_BUTTER]: 6, // 🧈 Main conditioning work
      [W.ARAM]:         6, // 🎱 Conditioning circuits suit Ultra
      [W.CIRCUIT]:      6, // 🟠 Circuit format suits conditioning
      [W.INTENSE]:      4, // 🔴 High-output conditioning
      [W.EXPOSURE]:     4, // 🌎 Exposing cardiovascular capacity
      [W.IMPRINT]:      2, // 🧬 Movement patterns under fatigue
    },
    suppressions: {
      // CLAUDE.md: "cardiovascular vs neural" — Strength loading contradicts conditioning
      [W.STRENGTH]:     -4,
      // Heavy barbell work contradicts cardiovascular focus
      [W.PERFORMANCE]:  -2,
      // Isolation work contradicts systemic conditioning
      [W.VANITY]:       -4,
      [W.SCULPT]:       -4,
    },
  },

};
