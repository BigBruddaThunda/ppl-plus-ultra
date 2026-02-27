---
title: Almanac 8-Day Color Rotation
category: seed
status: SEED
planted: 2026-02-27
phase-relevance: Phase 6 — User Accounts / Almanac
depends-on:
  - seeds/default-rotation-engine.md
  - scl-directory.md
connects-to:
  - seeds/default-almanac-preset.md
  - seeds/default-rotation-engine.md
  - middle-math/rotation/rotation-engine-spec.md
---

# Almanac 8-Day Color Rotation

The Color dial is the only dial the user actively chooses. The other three — Order (day of week), Type (rolling 5-day), Axis (monthly) — are deterministic. Color is where the user's hand touches the system.

The default Color sub-cycle is an 8-day perpetual rotation, completely independent of the 7-day week. This independence is the point.

---

## The 8-Day Cycle

8 Colors rotate in a fixed perpetual sequence:

```
Day 1: 🔵 Structured
Day 2: 🟣 Technical
Day 3: 🔴 Intense
Day 4: 🟠 Circuit
Day 5: 🟡 Fun
Day 6: 🟢 Bodyweight
Day 7: ⚫ Teaching
Day 8: ⚪ Mindful
→ Day 9: 🔵 Structured (restart)
```

Sequence rationale: The cycle moves through Expressive Colors first (🔵🟣🔴🟠 — execute, test, perform, connect), then Preparatory Colors (🟡🟢⚫⚪ — explore, ground, learn, reset). It ends on ⚪ Mindful — the reset valve — before cycling back to 🔵 Structured.

This is not mandatory ordering. A new user could begin at any point in the cycle based on registration date, or the sequence could be shuffled by preference. The Almanac queue can override any position.

---

## Coprime Relationships and Super-Cycles

The 8-day Color cycle is coprime with the 7-day Order cycle (8 and 7 share no common factor other than 1). This means:

- Every Color-Order combination repeats every **56 days** (7 × 8)
- A user never sees ⛽ Strength + 🔴 Intense on the same day twice within a 56-day window
- The system feels non-repetitive even before the Type and Axis dials add their variation

Stack the Type cycle (5-day) on top:

- 5, 7, and 8 are mutually coprime
- Every Type-Order-Color combination repeats every **280 days** (5 × 7 × 8 = 280)
- Less than one full calendar year
- Multi-year drift: the same Type-Order-Color combination falls on different months each year

Add the Axis cycle (12-month, not coprime with the others but slow-moving):

- The full 4-dial combination repeats exactly — same zip code on the same date — every **3,360 days** (280 × 12 = 3,360) in theory, though the Axis is approximated monthly rather than daily
- For practical purposes: no user will see the full system cycle in their lifetime at the daily granularity

The system's non-repetition emerges from three coprime gears. No algorithm required after setup.

---

## The "8 Deep" Daily Options

On any given day, three dials are locked:
- Order: determined by day of week (e.g., Tuesday = ⛽ Strength)
- Type: determined by rolling calendar position (e.g., Day 73 = 🍗 Legs)
- Axis: determined by current month (e.g., March = 🔨 Functional)

The Color dial produces 8 options. Every day the user has access to 8 different workouts from the same address root:

```
Tuesday, March (Day 73 of year):
⛽🔨🍗⚫ — Teaching
⛽🔨🍗🟢 — Bodyweight
⛽🔨🍗🔵 — Structured
⛽🔨🍗🟣 — Technical
⛽🔨🍗🔴 — Intense
⛽🔨🍗🟠 — Circuit
⛽🔨🍗🟡 — Fun
⛽🔨🍗⚪ — Mindful
```

8 valid workouts. 8 entirely different experiences of the same training target. The user picks their color.

The default Color for that day (per the 8-day rotation) is shown first or highlighted. The user can override to any of the other 7.

---

## Almanac Queue Override

When a user queues a specific zip code — e.g., ⛽🔨🍗🟣 Technical because they want to go heavy with a precision focus — the queued Color overrides the default rotation for that day.

The rotation resumes the following day from wherever it left off. The queue does not skip positions — it temporarily overrides. Rest day behavior (whether the cycle pauses or continues rolling) is an open question.

---

## User Color Preference Learning

The Almanac tracks which Colors the user selects when given the 8-option spread. Over time:

- Colors chosen frequently: surface higher in the daily presentation
- Colors never chosen: deprioritized in the default suggestion (but always available)
- Colors with high completion rates: weighted heavier than selection alone

This is soft personalization — the 8 options always exist, but the system learns which one to highlight first.

See `seeds/default-almanac-preset.md` for the full preset-to-personalized transition timeline.

---

## Open Questions

- **Rest day behavior:** Does the Color cycle pause on rest days or keep rolling? If rolling: a user who takes Sundays off still advances through the Color cycle. If paused: the cycle reflects active training days only.
- **Explicit Color lock:** Can a user lock a favorite Color and ignore the rotation entirely? Probably yes — with a toggle.
- **Seasonal Color bias:** Should certain Colors be weighted higher in certain months? (🔴 Intense in summer, ⚪ Mindful in winter.) This would conflict with the mathematical purity of the rotation but might feel more natural.
- **Starting position:** Should new users begin at Day 1 (🔵 Structured) by default, or should the starting position be derived from registration date?
- **Global sync vs. personal offset:** Like the Type cycle, the Color cycle could be globally synced (all users on same day have same default Color) or individually offset by registration date. Global sync creates shared daily experience; personal offset reduces community-level clustering.
