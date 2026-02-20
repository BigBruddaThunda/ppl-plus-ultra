---
planted: 2026-02-20
status: SEED
phase-relevance: Phase 6 (User Accounts / Almanac)
blocks: nothing in Phase 2-5
depends-on: seeds/almanac-macro-operators.md, seeds/almanac-8day-rotation.md
connects-to: seeds/default-almanac-preset.md, seeds/almanac-room-bloom.md
---

# The Default Rotation Engine — Three Gears, Zero Decisions

## One Sentence

Three interlocking cycles at different speeds — Order by weekday (7), Type by rolling calendar (5), Axis by monthly Operator (12) — produce a complete daily zip code requiring zero user input, with the Color as the single human-facing choice layer.

## The Three Gears

### Gear 1: Order → Day of Week (7-day cycle, fixed)

The Order is pinned to the day of the week. It never moves. It resets every Monday.

| Day | Order | Architectural Name | Character |
|-----|-------|--------------------|-----------|
| Monday | 🐂 | Tuscan | Foundation. Pattern learning. The weekly reset. |
| Tuesday | ⛽ | Doric | Strength. Heavy loads. The week's structural work. |
| Wednesday | 🦋 | Ionic | Hypertrophy. Volume accumulation. The grind. |
| Thursday | 🏟 | Corinthian | Performance. Testing. Show what you built. |
| Friday | 🌾 | Composite | Full Body. Integration. Make it all fit together. |
| Saturday | ⚖ | Vitruvian | Balance. Correction. Fix what's off. |
| Sunday | 🖼 | Palladian | Restoration. Recovery. The long view. |

Why this sequence holds:
- Monday is the re-grounding after rest. 🐂 honors the reset without wasting it.
- Tuesday is when weekly energy peaks. ⛽ puts the heavy work where the body is ready.
- Wednesday is the hump. 🦋 volume carries momentum through midweek.
- Thursday is the performance window — enough stimulus in the tank, enough recovery from Tuesday.
- Friday loosens naturally. 🌾 integration matches the end-of-week energy shift.
- Saturday is the workshop day. ⚖ correction and tinkering.
- Sunday is rest. 🖼 recovery without training debt.

Planetary correspondence (from Order Parameters v2.0):
Monday/Moon (cycles, beginnings), Tuesday/Mars (force, action), Wednesday/Mercury (flow, adaptation), Thursday/Jupiter (expansion, expression), Friday/Venus (beauty, harvest), Saturday/Saturn (discipline, measurement), Sunday/Sun (wholeness, rest).

### Gear 2: Type → Rolling Calendar (5-day cycle, never resets for the week)

The Type rolls forward from January 1st across the entire calendar year. It does not reset on Monday. It does not align to the week. It just keeps rolling.

| Day | Type |
|-----|------|
| Jan 1 | 🛒 Push |
| Jan 2 | 🪡 Pull |
| Jan 3 | 🍗 Legs |
| Jan 4 | ➕ Plus |
| Jan 5 | ➖ Ultra |
| Jan 6 | 🛒 Push |
| Jan 7 | 🪡 Pull |
| ... | ... continues forever |

Because 5 and 7 share no common factor (coprime), the Type-Order combination on any given weekday shifts every week. Monday is always Foundation, but Monday is Push one week, Legs the next, Ultra after that. The same Order-Type pairing on the same weekday doesn't repeat for 35 days (5 × 7 = 35).

365 days ÷ 5 Types = 73 full Type rotations per year.
365 ÷ 35 day super-cycle = ~10.4 super-cycles per year.
Because 35 doesn't divide evenly into 365, Year 2 starts on a different Type than Year 1. Multi-year drift built in.

### Gear 3: Axis → Monthly Operator (12 shifts per year)

The monthly Operator implies a parent Axis. That Axis becomes the default for the month.

| Month | Operator | Parent Axis | Default Axis |
|-------|----------|-------------|--------------|
| January | 📍 pono | 🏛 Basics | 🏛 Firmitas |
| February | 🧲 capio | 🐬 Partner | 🐬 Sociatas |
| March | 🧸 fero | 🔨 Functional | 🔨 Utilitas |
| April | 👀 specio | 🌹 Aesthetic | 🌹 Venustas |
| May | 🥨 tendo | 🔨 Functional | 🔨 Utilitas |
| June | 🤌 facio | 🏛 Basics | 🏛 Firmitas |
| July | 🚀 mitto | 🪐 Challenge | 🪐 Gravitas |
| August | 🦢 plico | 🌹 Aesthetic | 🌹 Venustas |
| September | 🪵 teneo | 🪐 Challenge | 🪐 Gravitas |
| October | 🐋 duco | ⌛ Time | ⌛ Temporitas |
| November | ✒️ grapho | ⌛ Time | ⌛ Temporitas |
| December | 🦉 logos | 🐬 Partner | 🐬 Sociatas |

Note: Some Axes appear twice (Basics in Jan+Jun, Functional in Mar+May, Aesthetic in Apr+Aug, Challenge in Jul+Sep, Time in Oct+Nov, Partner in Feb+Dec). This is natural — each Axis gets a preparatory month and an expressive month. The Axis is the same floor, but the Operator tone on that floor shifts between inhale and exhale.

### The Color: The Human Dial

The Color is the user's choice. The system can default it (rotating through the 8 Colors on an 8-day sub-cycle, or starting at 🔵 Structured as baseline), but the Color is the dial that asks: "What experience do you want today?" Tired → ⚪ Mindful. Fired up → 🔴 Intense. No gym → 🟢 Bodyweight. Learning → ⚫ Teaching.

8 Colors means 8 workout options behind every daily Order-Type-Axis combination. The daily content stream is 8 deep.

## The Complete Default Zip Code

On any given day, with zero user input:
- **Order** = what day of the week is it?
- **Type** = what position in the rolling 5-day cycle?
- **Axis** = what month is it? (via Operator parent)
- **Color** = system default or user selection

Example: Wednesday, March 12th, Year 1.
- Order: 🦋 Hypertrophy (Wednesday)
- Type: Day 71 of the year. 71 mod 5 = 1. Types index: Push(0), Pull(1), Legs(2), Plus(3), Ultra(4). Day 71 → 🪡 Pull.
- Axis: March → 🧸 fero → 🔨 Functional
- Color: User picks or system defaults to 🔵 Structured.
- Default zip: **🦋🔨🪡🔵** — Hypertrophy, Functional, Pull, Structured.

The user who wants to just show up and train has a workout waiting. The user who wants depth spins the Color dial. The user who wants full control overrides everything.

## RAG and Automation Implications

The three fixed cycles create patterned data across three temporal dimensions:
- **Weekly pattern**: How does this user perform on Tuesday Strength days vs. Thursday Performance days?
- **Rolling Type pattern**: How does their Pull work trend across the year regardless of Order?
- **Monthly Axis pattern**: Do they favor Intense in summer (Gravitas months) and Mindful in winter?

Patterned data is what makes recommendation engines work. Without fixed cycles, every session is an island. With them, the system can see trends, predict performance windows, and recommend zip codes that fit the user's actual behavioral patterns.

The Almanac queue (seeds/almanac-8day-rotation.md) sits on TOP of the rotation engine. The engine provides defaults. The Almanac provides overrides. When the user queues a specific zip from a Junction recommendation or community suggestion, it overrides whatever the engine would have served. The engine is the floor. The Almanac is the furniture the user arranges on it.

## Open Questions

- Does the Type rolling cycle start on Jan 1 for ALL users, or does it start on the user's account creation date? (Global sync vs. personal offset)
  - If global sync: everyone is on the same Type on the same day, which creates a shared daily rhythm. Community boards could be typed by day.
  - If personal offset: each user has their own cycle, which prevents staleness but loses the shared rhythm.
- Should the Color default cycle (if automated) be 8-day or align to something else?
- How does a rest day interact with the rolling Type cycle? Does it pause the cycle (so you don't skip Legs day) or does the cycle keep rolling (so missing a day means missing that Type this rotation)?
- Edge case: the Type cycle produces ➖ Ultra on Sunday (🖼 Restoration). Ultra cardio + Restoration recovery is a valid zip (🖼⌛➖⚪ exists in the system), but is it the best default pairing? Or should certain Order-Type collisions get special handling?
