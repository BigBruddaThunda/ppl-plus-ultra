---
planted: 2026-03-03
status: SEED
phase-relevance: Phase 4/5 (Operis rendering), Phase 6 (automation)
depends-on:
  - seeds/operis-prompt-pipeline.md
  - seeds/default-rotation-engine.md
  - seeds/operis-architecture.md
  - middle-math/rotation/reverse-weight-resolution.md
  - deck-identities/naming-convention.md
connects-to:
  - seeds/operis-educational-layer.md
  - seeds/operis-color-posture.md
  - middle-math/user-context/
  - exercise-library.md
---

# PPL± Operis — 13-Room Sandbox Structure

## One Sentence

Each daily Operis features exactly 13 workout rooms — 8 Color siblings derived deterministically from the rotation engine, and 5 Content Rooms derived editorially from the day's Operis content — producing a Sandbox that is both architecturally complete and editorially alive.

---

## The Two Sets

### Set A — The 8 Color Siblings (deterministic)

The rotation engine produces a daily default zip code: Order × Type × Axis. That zip code exists in 8 Color variants — the same workout DNA in 8 different equipment formats and session structures. All 8 appear in the Sandbox every day.

Example: If the rotation engine produces ⛽🔨🪡 (Strength × Functional × Pull) for today, the 8 Color siblings are:

| Zip | Color | Format |
|-----|-------|--------|
| ⛽🔨🪡⚫ | Teaching | Extended rest, coaching cues, comprehension focus |
| ⛽🔨🪡🟢 | Bodyweight | No gym required. Tier 0–2 equipment. |
| ⛽🔨🪡🔵 | Structured | Prescribed sets/reps/rest. Trackable. |
| ⛽🔨🪡🟣 | Technical | Precision. Lower volume, extended rest. |
| ⛽🔨🪡🔴 | Intense | Maximum effort. High volume. Reduced rest. |
| ⛽🔨🪡🟠 | Circuit | Station-based timed rotation. Loop logic. |
| ⛽🔨🪡🟡 | Fun | Exploration and variety. Structured play. |
| ⛽🔨🪡⚪ | Mindful | Slow tempo. Extended rest. Breath focus. |

One of these 8 carries the Color of the Day and becomes the featured room. It appears first, above the fold, with 150–250 words of description. The other 7 appear below with 60–100 words each, since they share the same Order × Type × Axis and their descriptions focus on what the Color changes about the session format.

The 8 Color siblings are fully deterministic. No editorial judgment is needed to select them. The rotation engine produces them. The editor writes them.

**Temporal threads.** Each Color variant carries its own week-over-week progressive arc. The 🟢 Bodyweight track from Monday to Tuesday to Wednesday is a progression independent of the 🔴 Intense track across the same days. A reader who consistently picks 🟢 has their own training lane that the system can eventually track via the user context layer (`middle-math/user-context/`). The 8 siblings are 8 parallel training programs running simultaneously, all derived from the same rotation engine, diverging only at Color.

---

### Set B — The 5 Content Rooms (editorial)

The 5 Content Rooms are the Operis editorial content made physical. Each room is a zip code derived from a specific piece of today's content — a historical event, an educational feature, a seasonal observation. The daily content becomes pattern learning expressed as movement.

The principle: The Operis publishes knowledge. The 5 Content Rooms translate that knowledge into physical practice. A historical event about bridge construction becomes a workout that trains the movement patterns of structural labor. An educational feature about seed starting becomes a workout that trains the postures and grip endurance of planting. A historical milestone about a rushing record becomes a workout that trains the way a running back prepares for volume carries — filtered through PPL± logic.

This is embodied cognitive learning. The reader who does the Content Room does not just read about the event — they train the physical reality of it. The knowledge enters through two channels: prose and practice. Dual coding. This is how adult learning sticks.

---

## Content Room Selection Rules

The 5 Content Rooms are selected by Prompt 3 (the Editor) during composition. The selection follows these constraints:

**Constraint 1 — All share today's Order.** The Order is the day of the week. It does not change. All 13 rooms in the Sandbox carry today's Order.

**Constraint 2 — 5 unique Types.** Each Content Room carries a different Type (🛒 Push, 🪡 Pull, 🍗 Legs, ➕ Plus, ➖ Ultra). One of each. No Type repeats within the 5.

**Constraint 3 — 5 unique Axes.** Each Content Room carries a different Axis. The main zip's monthly Axis is available for Content Rooms — the monthly Axis lock applies only to the 8 Color siblings. The 5 Content Rooms scatter across the Axis space. No Axis repeats within the 5.

**Constraint 4 — Colors are editorially selected.** Each Content Room's Color (position 4) is selected by the editor based on the content's character. A historical event about precision engineering maps to 🟣 Technical. An educational item about outdoor skills maps to 🟢 Bodyweight. A seasonal observation about urgent weather preparation maps to 🔴 Intense. The Color expresses how the content translates to a workout format.

**Constraint 5 — No duplication with Color siblings.** The 5 Content Rooms must not duplicate any of the 8 Color siblings' full 4-emoji zip codes. Since the Color siblings all share one Type and one Axis while the Content Rooms must have 5 different Types and 5 different Axes, this constraint is naturally satisfied in most cases. The editor checks for edge cases.

**Constraint 6 — Content sourcing.** Each Content Room must trace to a specific piece of Operis content — a named historical event, a named educational feature, or a named seasonal observation. The connection is documented in the edition's frontmatter under `sandbox-zips.content-rooms` with source content tags. The connection does not appear in the room's title or description (see Naming Convention below).

---

## Content-to-Zip Mapping

This is the editorial craft at the heart of the Content Room system. The editor reads a piece of Operis content, identifies the physical domain it implies, and maps that domain to PPL± parameters.

The mapping chain:
```
Operis content
    → Physical domain implied by the content
        → Type (what muscles / movement patterns)
            → Axis (what character of movement)
                → Color (what equipment format / session structure)
                    → Order (fixed — day of week)
                        = Zip code
```

**Mapping examples:**

Content: "1883 — Brooklyn Bridge opens. 14 years of construction. Workers handled cables overhead at height, riveted steel in sustained positions, carried materials across catwalks."
Physical domain: Overhead work, sustained grip, balance under load, carries.
Type: ➕ Plus (full body power, carries, core stability)
Axis: 🪐 Challenge (precision under demanding conditions)
Color: 🟣 Technical (serious, quality-focused, no room for error)
Result on a Tuesday (⛽): ⛽🪐➕🟣

Content: "Educational feature — seed starting in early March. Kneeling, hip hinging, fine motor grip, sustained low posture, ground-level work for extended periods."
Physical domain: Hip hinge endurance, grip, prolonged kneeling and bending.
Type: 🍗 Legs (hip hinge patterns, glute and hamstring endurance)
Axis: 🌹 Aesthetic (feel-based, intentional, body awareness)
Color: 🟢 Bodyweight (accessible, could be done in a garden)
Result on a Tuesday (⛽): ⛽🌹🍗🟢

Content: "1995 — Emmitt Smith breaks NFL rushing record. Volume carries, explosive hip extension, lateral cutting, sustained output across a career."
Physical domain: Lower body explosive power, conditioning, durability.
Type: 🍗 Legs — wait, already used. Remap: ➖ Ultra (cardiovascular endurance, sustained output, the conditioning that makes a career)
Axis: 🔨 Functional (athletic transfer, standing, ground-based)
Color: 🔴 Intense (maximum effort, high stakes)
Result on a Tuesday (⛽): ⛽🔨➖🔴

The editor must think through the full constraint space. If a natural Type mapping is already claimed by another Content Room, the editor finds the next-best Type that the content supports. Football is not only legs — it is also conditioning (➖ Ultra), power (➕ Plus), or upper body durability (🛒 Push, 🪡 Pull). The constraint forces creative interpretation. The constraint is the feature.

---

## Naming Convention

Content Room titles follow the same ExRx naming convention as all PPL± workout cards. Titles are exercise-descriptive, not editorial or narrative.

**Correct:**
- ⛽🪐➕🟣±🪵 Overhead Carry and Core Stability
- ⛽🌹🍗🟢±👀 Bodyweight Hip Hinge and Garden Posture
- ⛽🔨➖🔴±🥨 Lateral Conditioning and Sprint Intervals

**Incorrect:**
- ⛽🪐➕🟣±🪵 The Brooklyn Bridge Room
- ⛽🌹🍗🟢±👀 The Gardener's Row
- ⛽🔨➖🔴±🥨 The Emmitt Smith Room

The editorial connection between the Content Room and its source content lives in two places: (1) the Operis edition text, where the editor can describe the room's relationship to the day's content in prose, and (2) the edition frontmatter, where the source content tag is logged. The title and the card file itself are pure PPL± — exercise-descriptive, findable by any user at any time regardless of whether they read the original Operis edition.

A user who discovers ⛽🪐➕🟣 six months later finds a workout called "Overhead Carry and Core Stability." It stands on its own. The fact that it was first generated because the Operis featured the Brooklyn Bridge is archival context, not user-facing naming.

---

## The Complete Daily Sandbox

13 rooms. Fixed structure. Variable content.

```
Featured Room (★)
    [Color of the Day variant from the 8 siblings]
    150–250 words. Above the fold.

Color Siblings (7 remaining)
    [The other 7 Color variants of today's Order × Type × Axis]
    60–100 words each. Focus on what the Color changes.

Content Rooms (5)
    [5 zip codes derived from today's Operis content]
    100–150 words each. Exercise-descriptive titles.
    5 unique Types. 5 unique Axes. Colors editorially selected.
    Each traces to a named piece of today's content.
```

Total room description word count: 150–250 (featured) + 420–700 (7 siblings) + 500–750 (5 content rooms) = 1,070–1,700 words dedicated to rooms. This is a significant portion of the 2,800–5,000 word edition. The rooms are the product. They deserve the space.

---

## Generation Implications

The 13-room Sandbox is the Operis's primary card generation pressure mechanism.

The 8 Color siblings are always from one deck (one Order × Axis combination). If any of the 8 are EMPTY stubs, they must be generated before the edition publishes. This means every edition potentially forces up to 8 card generations from the same deck — and since the Type rotates daily, the edition hits a different Type row in that deck each day. Over 5 days, the edition touches all 5 Types in the deck. Over 8 days, it touches all 8 Colors in each Type. One deck's 40 cards can be fully generated by the Operis in approximately 40 days of editions.

The 5 Content Rooms scatter across decks (5 different Axes means potentially 5 different decks). Each Content Room that lands on an EMPTY stub forces a card generation in a different deck. This spreads the generation pressure across the library rather than concentrating it in one deck.

Combined generation rate: Up to 13 card generations per edition. Assuming 30–50% are already GENERATED on any given day, the net new generation is 6–9 cards per day. At 7 cards per day average, the remaining 1,600 cards complete in approximately 229 days — roughly 33 weeks of daily Operis production.

Deck identity document requirement: Prompt 4 (the Builder) checks for deck identity documents before generating cards. If a Content Room falls in a deck with no identity document, Prompt 4 builds the identity document first. This is the one permitted exception to the "do not freelance" rule — building a deck identity maps all 40 zip codes in the deck, not just the one the Operis featured. The identity document is generation infrastructure, not speculative work.

---

## Relationship to Reverse-Weight Resolution

The reverse-weight resolution algorithm (`middle-math/rotation/reverse-weight-resolution.md`) triangulates today's featured room between yesterday's fatigue and tomorrow's stimulus.

For the 8 Color siblings, the reverse-weight logic operates per-Color-track. Yesterday's 🔵 Structured room and tomorrow's 🔵 Structured room frame today's 🔵 Structured sibling. Each Color track has its own temporal thread.

For the 5 Content Rooms, the reverse-weight logic is secondary to the content mapping. The Content Room's zip code is determined by its source content, not by the temporal thread. However, the editor can use the reverse-weight resolution as a tiebreaker when two zip codes equally serve the content — prefer the one that better prepares tomorrow while respecting yesterday.

The featured room is always the reverse-weight resolution of the Color of the Day track. It is simultaneously the best room for today's cognitive posture AND the best room for the week's progressive arc. This dual purpose is why it gets the most real estate.

---

## Content Room Constraint Summary

All constraints in one place for Prompt 3 (the Editor):

1. All 5 Content Rooms share today's Order (fixed by day of week via Gear 1).
2. Each Content Room has a unique Type — all 5 Types appear exactly once across the 5 rooms (🛒🪡🍗➕➖ one each).
3. Each Content Room has a unique Axis. The sibling/monthly Axis is available to Content Rooms; the sibling-axis lock applies only to the 8 Color siblings. No Axis repeats within the 5 Content Rooms.
4. Color is editorial. Choose the Color that fits the content's character using the Color Context Vernacular. No full-zip duplication with any Color sibling.
5. Every Content Room title follows `deck-identities/naming-convention.md`. No editorial content in titles. The zip-code title describes the workout. The editorial connection lives in the Operis prose and front-matter, not in the title.
6. Every Content Room's source is recorded in the edition front-matter `source` and `source-beat` fields. These fields are for archival traceability, not for display.

---

## Content-to-Zip Mapping Chain

The mapping moves from content toward workout, not the other way:

```
Operis content
    → physical domain (what kind of movement or exertion does this content connect to?)
    → Type (which muscle group / movement domain? 🛒🪡🍗➕➖)
    → Axis (what is the exercise character? 🏛🔨🌹🪐⌛🐬 — unique across the 5 Content Rooms)
    → Color (what is the session format / editorial tone? ⚫🟢🔵🟣🔴🟠🟡⚪)
    → Order (fixed by today's day of week — already determined by Gear 1)
    = 4-emoji zip code
```

Content decides Type and Axis. The Editor chooses Color. Order is fixed. The mapping moves from content toward workout, not the other way.

Example chain: A historical event about a 19th-century laborer carrying iron across a bridge site → physical domain: load-bearing, carrying, grip endurance → Type: ➕ Plus (loaded carries, strongman patterns) → Axis: 🔨 Functional (unilateral, standing, athletic transfer) → Color: 🔵 Structured (trackable, prescriptive) → Order: from today's day of week (e.g., ⛽ on Tuesday) → zip: ⛽🔨➕🔵.

The sibling/monthly Axis is allowed for Content Rooms. The only Axis requirement is uniqueness across the 5 Content Rooms (no repeats).

---

## Naming Convention

All Content Room titles follow `deck-identities/naming-convention.md` exactly. The ExRx naming standard:

**Format:** [Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]

**Correct:** "Dumbbell Romanian Deadlift — Hamstring Strength Log"
**Incorrect:** "Bridge Builder's Hip Hinge" (editorial reference in title)
**Incorrect:** "The Carrier's Walk" (narrative, no ExRx content)

A user finding this zip code six months from now via search, community recommendation, or their own Almanac queue will see a workout title. They will not have today's editorial context. The zip-code title must be self-sufficient as a workout description.

The editorial connection between a Content Room and its source content lives in three places:
1. The Operis edition front-matter (`source` and `source-beat` fields)
2. The Operis edition prose (the Historical Desk or Educational Feature article that inspired the room, juxtaposed with the room listing through prose proximity)
3. The editor's contextual description of the room within the edition (which can allude through proximity without announcing)

It lives nowhere in the card file title. The card file title is a phone book listing.

Cross-reference: `seeds/operis-sandbox-structure.md` (this file) → `deck-identities/naming-convention.md` → `scl-deep/vocabulary-standard.md`.

---

## Open Questions

- Should the 5 Content Rooms maintain any week-over-week continuity? (e.g., if Monday's Content Rooms covered certain Axes, should Tuesday's Content Rooms prefer different Axes for weekly coverage?) Current design: no — each day's Content Rooms are determined solely by that day's content. Weekly coverage is a natural byproduct, not a constraint.

- Should Content Room descriptions reference their source content explicitly? Current design: the description is a lived-space workout description (ExRx naming, exercise-focused). The editorial connection is made in the Operis prose surrounding the room listing, not in the room description itself. The card file is pure PPL±.

- How does the Content Room system interact with the user's Almanac queue? If a user taps a Content Room from the Operis, does it enter their queue as a one-time room or as a recurring address? Current lean: one-time. The Content Room is an address in the 1,680-room library like any other. It persists. But the editorial connection to a specific date's content is archival.

🧮
