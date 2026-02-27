---
title: Default Almanac Preset
category: seed
status: SEED
planted: 2026-02-27
phase-relevance: Phase 6 — User Accounts / Almanac
depends-on:
  - seeds/default-rotation-engine.md
  - seeds/almanac-8day-rotation.md
  - seeds/almanac-room-bloom.md
connects-to:
  - seeds/almanac-8day-rotation.md
  - middle-math/rotation/rotation-engine-spec.md
  - middle-math/user-context/exercise-profile-spec.md
  - seeds/platform-architecture-v2.md
---

# Default Almanac Preset

A new user has no history. No preferences. No logged sessions. The Almanac still works on day one.

This document specifies what the Almanac ships with before the user has done anything — the "seed packet" that makes the system functional immediately.

---

## What "Default" Means

Default means deterministic. Every new user gets the same Almanac on their registration day — not the same workout, but the same algorithmic posture. The three gears produce a unique daily address based on the calendar date. The Color sub-cycle begins at its global default position. The result: a real workout, fully specified, ready to go.

No setup required. No onboarding questionnaire. No "what are your goals?" The system shows the work. The user decides whether to do it.

---

## The Three Gears on Day One

**Gear 1 — Order (day of week):**
Fixed to the Gregorian calendar. The Order the user encounters on their registration day is determined by what day of the week it is. If they register on a Tuesday, they get ⛽ Strength. Wednesday: 🦋 Hypertrophy. No configuration required.

| Day | Order |
|-----|-------|
| Monday | 🐂 Foundation |
| Tuesday | ⛽ Strength |
| Wednesday | 🦋 Hypertrophy |
| Thursday | 🏟 Performance |
| Friday | 🌾 Full Body |
| Saturday | ⚖ Balance |
| Sunday | 🖼 Restoration |

**Gear 2 — Type (rolling 5-day perpetual calendar):**
The Type cycle began Jan 1 of the epoch year (Year 1 = 2026 in implementation). Day 1 of the epoch = 🛒 Push. Day 2 = 🪡 Pull. Day 3 = 🍗 Legs. Day 4 = ➕ Plus. Day 5 = ➖ Ultra. Day 6 = 🛒 Push again. This cycle rolls continuously.

New users enter the cycle at the current global position — the same Type that any other user would see on that calendar date. This is global sync: all users share the same Type on any given day (unless personally offset).

**Gear 3 — Axis (monthly):**
The monthly Axis assignment from `seeds/default-rotation-engine.md`:

| Month | Operator | → Axis |
|-------|----------|--------|
| January | 📍 pono | 🏛 Basics |
| February | 🧲 capio | 🐬 Partner |
| March | 🧸 fero | 🔨 Functional |
| April | 👀 specio | 🌹 Aesthetic |
| May | 🥨 tendo | 🔨 Functional |
| June | 🤌 facio | 🏛 Basics |
| July | 🚀 mitto | 🪐 Challenge |
| August | 🦢 plico | 🌹 Aesthetic |
| September | 🪵 teneo | 🪐 Challenge |
| October | 🐋 duco | ⌛ Time |
| November | ✒️ grapho | ⌛ Time |
| December | 🦉 logos | 🐬 Partner |

**Gear 4 — Color (default):**
Default Color is 🔵 Structured. Reasons: most neutral (doesn't assume strength or recovery intent), most teachable (prescribed sets/reps/rest are easy to follow on day one), most repeatable (trackable across sessions — the new user can immediately see progress metrics).

The 8-day Color cycle begins on registration date. Day 1 of the user's cycle = 🔵 Structured, regardless of global cycle position. The user's Color cycle is personally offset by registration date.

---

## Day One Experience

A user registers on Tuesday, March 12, 2026.

- Order: ⛽ Strength (Tuesday)
- Type: Day 71 of 2026 (March 12 = 71st day) → 71 mod 5 = 1 → 🪡 Pull
- Axis: March = 🔨 Functional
- Default Color: 🔵 Structured

**Default zip: ⛽🔨🪡🔵**

The Almanac presents all 8 Color variants of this address. The default is highlighted: ⛽🔨🪡🔵 Strength × Functional × Pull × Structured. The other 7 are visible. The user can tap any of them, or accept the default.

No decisions required. Just show up.

---

## The Initial 8 Options

On any given day, the user sees 8 valid workouts — one for each Color, all sharing the same Order × Axis × Type address:

```
[Address root for the day: Order × Axis × Type]
├── ⚫ Teaching     — extra rest, coaching cues, comprehension
├── 🟢 Bodyweight  — no gym required
├── 🔵 Structured  — [DEFAULT] prescribed sets/reps/rest
├── 🟣 Technical   — precision, GOLD possible, extended rest
├── 🔴 Intense     — max effort, GOLD possible, high volume
├── 🟠 Circuit     — station rotation, timed, no barbell
├── 🟡 Fun         — exploration, variety, play within constraints
└── ⚪ Mindful     — 4s eccentrics, breath, extended rest
```

The default (🔵 Structured) is not mandatory. It is simply the most universally appropriate starting point for a user whose preferences are unknown.

---

## Transition from Preset to Personalized

The preset retires gradually as the system accumulates data. Milestones:

**After 5 logged sessions:**
Color preference signals emerge. Which Color did the user choose each day? Start surface-ranking Colors accordingly. Soft adjustment only — all 8 remain available.

**After 20 logged sessions:**
Axis preference signals surface. Which Axis yields higher completion rates? (A session left unfinished or abandoned is a signal.) Axis ranking begins — not changing the monthly assignment, but adjusting which variant the system highlights within any given month's options.

**After 40 logged sessions:**
Type balance assessment begins. Is the user over-training one Type and under-training another? The system doesn't enforce balance — the three gears handle that — but can flag patterns. Example: a user who consistently overrides Pull days may be avoiding something worth addressing.

**After 90 days:**
Full personalization mode. The system knows enough to surface the right default on most days. The preset quietly retires. The user may not notice the transition — the algorithm just gets better at guessing what they actually want.

**Preset permanence:**
A user can always reset to the default preset from their profile settings. This wipes preference learning and restores the global-sync starting position. Useful after a long layoff or a major training goal change.

---

## The Almanac Seed Packet

What the system ships before the user interacts with it:

```
PRESET STATE:
  gear_1: day_of_week_mapping (fixed)
  gear_2: global_type_position (current day mod 5)
  gear_3: monthly_axis_assignment (current month)
  color_default: 🔵 Structured
  color_cycle_offset: registration_date (day 1 = 🔵)

USER STATE:
  session_count: 0
  color_selections: {}
  axis_completion_rates: {}
  type_balance: {}
  preference_mode: PRESET

ALMANAC STATE:
  queue: []  (empty — no zip codes queued)
  seasonal_layer: current_month_operator_content
  personalization_ready: false
```

The seed packet is deterministic. Two users registering on the same day get the same seed packet. Their Almanacs diverge as they log sessions and make different Color choices.

---

## Open Questions

- **Global Type sync:** Should new users enter the Type cycle at the global current position (all users share the same Type each day) or at a personal offset? Global sync creates shared daily experience. Personal offset means two users registering on the same day might not be doing the same Type.
- **Color cycle Day 1:** Fixed at 🔵 Structured for all new users, or derived from registration date in the global Color cycle?
- **Onboarding signal:** Should the system ask any questions at registration? Current answer is no — just show the work. But a single question ("Do you have gym access today?") could inform the first Color suggestion. Keep it optional.
- **Rest day detection:** Does the system assume every day is a training day, or does it detect patterns of non-use and adjust? The three gears roll regardless. The user simply doesn't log.
