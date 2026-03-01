---
title: Reverse-Weight Resolution Algorithm
category: middle-math/rotation
status: SEED
planted: 2026-02-28
phase-relevance: Phase 2.5 (architecture) + Phase 4/5 (Operis)
depends-on:
  - middle-math/rotation/engine-spec.md
  - middle-math/weights/
  - zip-web/zip-web-signatures.md
  - middle-math/rotation/fatigue-model.md
connects-to:
  - seeds/operis-architecture.md
  - seeds/default-rotation-engine.md
---

# Reverse-Weight Resolution Algorithm

The rotation engine produces a default zip code for any given date using three deterministic gears: Order by weekday, Type by rolling 5-day calendar, Axis by month. The Color is user-chosen.

The default zip code is the starting point, not the final answer.

The Reverse-Weight Resolution layer triangulates today's optimal room by looking backward at yesterday's session and forward at tomorrow's highest-weighted candidate. Today sits at the hinge between what was done and what is coming. The algorithm finds the room that best honors that position.

---

## The Temporal Triangle

```
Yesterday's zip
     |
     | (fatigue signature)
     ↓
TODAY'S ADJUSTED ZIP  ←────  Tomorrow's zip
     ↑                        (stimulus requirements)
     |
  Rotation engine default
```

Yesterday tells you what tissue is loaded and what CNS demand was placed. Tomorrow tells you what the week is building toward. Today's resolution maximizes preparation for tomorrow while minimizing conflict with yesterday.

The resolution never overrides the Order. The weekday Order is fixed. The resolution operates within the Type, Axis, and Color space — the three dials that can flex.

---

## Phase 1 — Read Yesterday's Fatigue Signature

**Input**: Yesterday's zip code (4-emoji address).

**Process**:

1. Look up yesterday's zip in `zip-web/zip-web-signatures.md`. Each zip carries a fatigue signature: which muscle groups are loaded, CNS demand level (Low/Moderate/High), and mechanical stress patterns (compressive, tensile, rotational).

2. If the fatigue model in `middle-math/rotation/fatigue-model.md` has user RPE data logged, use it to weight the signature. High RPE on yesterday's session amplifies the suppression signal. Low RPE attenuates it.

3. Derive a suppression vector: which Types, Axes, and exercise families should be downweighted today. This is not a prohibition — it is a penalty. The system prefers rooms that don't compound yesterday's load on the same tissue under the same mechanical pattern.

**Example**:

Yesterday: ⛽🏛🛒🔴 (Strength, Basics, Push, Intense)
- Primary loaded tissue: chest, anterior deltoid, triceps
- CNS demand: High
- Mechanical pattern: horizontal press, heavy bilateral
- Suppression signal: 🛒 Push suppressed, 🔴 Intense suppressed under horizontal pressing, bilateral barbell push patterns suppressed

---

## Phase 2 — Read Tomorrow's Stimulus Requirements

**Input**: Tomorrow's default zip code from the rotation engine.

**Process**:

1. Run the rotation engine forward one day to derive tomorrow's default zip.

2. Identify tomorrow's primary stimulus requirements: which tissue needs to be fresh, which movement patterns need to be primed, which CNS state tomorrow's session demands.

3. Derive a preparation vector: which Types, Axes, and exercise families should be upweighted today because they serve tomorrow's session without fatiguing it.

**Example**:

Tomorrow: 🏟🏛🛒🟣 (Performance, Basics, Push, Technical)
- Primary stimulus: maximal horizontal press output
- Tissue requirement: chest and anterior deltoid fresh and primed
- CNS requirement: recovered, not depleted
- Preparation vector: avoid compounding pressing fatigue; light pulling work and leg work are neutral-to-positive for tomorrow's test

---

## Phase 3 — Compute the Adjusted Zip

**Input**: Today's rotation engine default, yesterday's suppression vector, tomorrow's preparation vector.

**Process**:

1. Start with today's default zip from the rotation engine.

2. Apply the suppression vector from Phase 1. Any zip that overlaps with yesterday's loaded tissue and mechanical pattern receives a penalty.

3. Apply the preparation vector from Phase 2. Any zip that primes tomorrow's primary stimulus without compressing it receives a bonus.

4. Among all valid zips sharing today's Order, rank by net score (bonuses minus penalties). Select the highest-ranked zip that does not violate any hard constraint (GOLD gate, barbell exclusion, equipment tier).

5. The adjusted zip is the today's room.

**Example — Full Triangulation**:

Yesterday: ⛽🏛🛒🔴 (heavy intense pressing, High CNS)
Tomorrow: 🏟🏛🛒🟣 (technical bench press test)
Today's Order: ⛽ Strength (weekday fixed)

Resolution logic:
- ⛽🏛🛒 combinations suppressed (pressing chain loaded yesterday AND needed fresh tomorrow)
- ⛽🏛🪡🔵 (Strength, Basics, Pull, Structured) scores high — heavy rowing primes posterior chain, does not compete with pressing tissue, leaves anterior deltoid recovered for tomorrow
- ⛽🔨🍗🟢 (Strength, Functional, Legs, Bodyweight) scores high — leg work is neutral to the pressing chain entirely
- Result: system selects ⛽🏛🪡🔵 — pulling addresses a complementary stimulus while the pressing chain recovers for tomorrow's test

---

## Phase 3b — When the Default is Already Optimal

If the rotation engine default zip scores within one standard deviation of the highest-ranked adjusted zip, the default stands. The resolution algorithm does not override the default unless the benefit is material.

This prevents unnecessary variation from the rotation engine's coprime design, which already handles long-horizon non-repetition across the 35-day super-cycle.

---

## Operis Editorial Implication

The reverse-weight resolution algorithm is the editorial intelligence behind the Operis's featured room selection. It is never explained in the edition text.

**What the reader sees**:
- The featured Sandbox room appears first, above the fold
- The Intention department frames today as the hinge between yesterday and tomorrow in human terms ("Thursday is the day you find out what Wednesday built")
- The room selection feels editorially coherent without the reader knowing why

**What the system is doing**:
- The selection logic ran Phase 1–3 before the edition was composed
- The featured room is the highest-ranked adjusted zip
- The Intention text is written to honor the temporal position — not to explain the algorithm

The selection logic shapes the edition from behind. It never appears on the newspaper's front page.

---

## Relationship to Existing Documents

- `middle-math/rotation/rotation-engine-spec.md` — provides the default zip; reverse-weight resolution adjusts it
- `middle-math/rotation/fatigue-model.md` — provides RPE heuristics that weight the Phase 1 suppression signal
- `zip-web/zip-web-signatures.md` — provides the fatigue signature lookup table for Phase 1
- `middle-math/weights/` — the weight tables provide the penalty/bonus scoring for Phase 3
- `seeds/operis-architecture.md` — documents the editorial application of this algorithm

---

## Implementation Notes

This document is SEED-level. The algorithm is specified but not yet implemented. Current card generation (Phase 2, fully-specified workout cards) continues without this layer.

When the Operis is built (Phase 4/5), this algorithm should be implemented as a pure function:

```
resolve(date) → zip_code
  inputs: date, yesterday's zip, tomorrow's default zip
  outputs: today's adjusted zip
  side effects: none
  deterministic: yes (same inputs → same output, always)
```

The function is deterministic. Given the same date and the same logged history, the same room is selected every time. The algorithm does not introduce randomness — it introduces informed adjustment within the deterministic rotation framework.

---

🧮
