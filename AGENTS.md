# AGENTS.md — Ppl± Codex Operating Instructions

You are working inside the Ppl± repository.
Read this file before touching anything else.
Active task is always in `whiteboard.md` — read it before acting.

---

## What This Project Is

Ppl± is a semantic training language (SCL — Semantic Compression Language) built by Jake Berry.
It uses 61 emojis across 7 categories to produce 1,680 unique workout addresses called zip codes.
Each zip code is a 4-emoji address that fully specifies a workout's loading protocol, exercise
character, muscle groups, and equipment format.

This repository is the master source of truth for all 1,680 workouts.

**Current phase:** Phase 2 — Workout Generation
**Status:** Deck 07 (⛽🏛 Strength Basics) complete — 40/1,680 cards generated. 1,640 remaining.
**Active task:** See `whiteboard.md`.

**Do not freelance. Read `whiteboard.md` before acting.**

### Downstream architecture

The `.md` card files are master blueprints for a web application.

`.md card → HTML workout card → user interactive session → user history → personal exercise database`

A hallucinated exercise in a `.md` file propagates through the entire downstream pipeline.
**Content accuracy is the highest priority constraint in this repository.**
When in doubt about an exercise or parameter, do not guess. Flag it.

---

## Repository Structure

```
ppl-plus-ultra/
├── README.md              — Public-facing description and navigation guide
├── CLAUDE.md              — Claude Code operating instructions (also read by Codex as fallback)
├── AGENTS.md              — This file. Codex operating instructions.
├── whiteboard.md          — Active session state. Current phase. Open questions. Session log.
├── scl-directory.md       — Complete SCL reference (~106k chars). All rules live here.
├── exercise-library.md    — All valid exercises (~128k chars, ~2,800 exercises, sections A–Q)
├── card-template-v2.md    — Generation template for card format
├── .codex/
│   ├── config.toml        — Project-level Codex configuration
│   └── agents/
│       ├── generator.toml — Card generation agent config
│       ├── validator.toml — Constraint validation agent config
│       ├── explorer.toml  — Read-only codebase explorer config
│       └── reviewer.toml  — PR review agent config
├── .claude/               — Claude Code skills and configuration (do not modify)
├── scl-deep/              — Full uncompressed SCL specifications (reference only)
├── seeds/                 — Architectural ideas for future phases (do not build from unless promoted)
├── html/                  — HTML experience layer scaffold (Phase 4/5 — do not populate now)
└── cards/
    └── [order-folder]/[axis-folder]/[type-folder]/
        └── [zip]±.md                        — Stub. Awaiting generation.
        └── [zip]±[op] [Title].md            — Complete. Workout generated.
```

Card files live at: `cards/[order-folder]/[axis-folder]/[type-folder]/[filename].md`

Example:
`cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`

Folder naming: `[emoji]-[slug]` format (e.g., `⛽-strength`, `🏛-basics`, `🪡-pull`).

---

## The 4-Dial Zip Code System

Every workout is a 4-emoji address. Format: **ORDER AXIS TYPE COLOR**

```
Position 1: ORDER  (7)  — Load ceiling. Training phase. The law.
Position 2: AXIS   (6)  — Exercise character. Selection bias.
Position 3: TYPE   (5)  — Muscle groups. Movement domain.
Position 4: COLOR  (8)  — Equipment tier. Session format.
```

Total combinations: 7 × 6 × 5 × 8 = **1,680 zip codes**

**Constraint hierarchy when dials conflict:**
1. ORDER — Hard ceiling. Nothing exceeds it. Ever.
2. COLOR — Hard filter. Equipment is binary.
3. AXIS — Soft bias. Ranks exercises, does not exclude.
4. Equipment — Practical filter. What is actually available.

### ORDERS (7) — The Loading Protocol

| Emoji | Name | Load | Reps | Rest | Max Difficulty | CNS |
|-------|------|------|------|------|----------------|-----|
| 🐂 | Foundation | ≤65% | 8–15 | 60–90s | 2/5 | Low |
| ⛽ | Strength | 75–85% | 4–6 | 3–4 min | 4/5 | High |
| 🦋 | Hypertrophy | 65–75% | 8–12 | 60–90s | 3/5 | Moderate |
| 🏟 | Performance | 85–100%+ | 1–3 | Full | 5/5 | High |
| 🌾 | Full Body | ~70% | 8–10 | 30–90s | 3/5 | Moderate |
| ⚖ | Balance | ~70% | 10–12 | 90s | 3/5 | Moderate |
| 🖼 | Restoration | ≤55% | 12–15 | 60s | 2/5 | Low |

**Order notes:**
- 🐂 Foundation: Pattern learning at sub-maximal load. Not beginner-only. Ceiling: if load >65%, reps <8, or difficulty >2, it is not 🐂.
- ⛽ Strength: Neural adaptation. Heavy loads, low reps, full recovery. Force production. Not bodybuilding.
- 🦋 Hypertrophy: Muscle growth through volume and metabolic stress. The pump matters.
- 🏟 Performance: Testing, not training. Test, record, leave. No junk volume. 3–4 blocks only.
- 🌾 Full Body: Integration. Flow and Unity Test is mandatory — each movement flows into the next, forming a single unified pattern.
- ⚖ Balance: Correction. Microscope on weak links and asymmetries.
- 🖼 Restoration: Recovery without training debt. You leave fresher than you entered. Extended scope: somatic movement, TRE, pelvic floor, diaphragmatic breathing, nervous system regulation.

### TYPES (5) — The Muscle Groups

| Emoji | Name | Muscles | Primary Patterns |
|-------|------|---------|-----------------|
| 🛒 | Push | Chest, front delts, triceps | Horizontal press, vertical press |
| 🪡 | Pull | Lats, rear delts, biceps, traps, erectors | Row, pulldown, hinge |
| 🍗 | Legs | Quads, hamstrings, glutes, calves | Squat, lunge, hinge, isolation |
| ➕ | Plus | Full body power, core | Olympic lifts, carries, plyometrics, anti-rot |
| ➖ | Ultra | Cardiovascular system | Rowing, cycling, running, conditioning, flows |

### AXES (6) — Exercise Character and Selection Bias

| Emoji | Name | Character |
|-------|------|-----------|
| 🏛 | Basics (Firmitas) | Bilateral, stable, time-tested fundamentals. Barbell classics first. Priority: Barbell > dumbbell. Bilateral > unilateral. Compound > isolation. |
| 🔨 | Functional (Utilitas) | Unilateral, standing, athletic-transfer. Priority: Unilateral > bilateral. Standing > seated. Free weight > machine. |
| 🌹 | Aesthetic (Venustas) | Isolation, full ROM, mind-muscle connection. Feel over load. In 🖼: somatic lens — pelvic floor, psoas, diaphragm, deep hip. |
| 🪐 | Challenge (Gravitas) | Hardest variation at any level. Deficit, pause, tempo, bands, chains, unstable surfaces. Always the hardest version they can control. |
| ⌛ | Time (Temporitas) | Context axis enabling EMOM, AMRAP, density blocks, timed sets, time trials, TUT, steady state. Specific protocol from Order × Color. |
| 🐬 | Partner (Sociatas) | Context axis enabling spottable, alternating, synchronized, competitive, assisted, station rotation. Machine work deprioritized. |

Full character specifications for each Axis are in `scl-directory.md`.

### COLORS (8) — Equipment and Session Format

Equipment Tiers:
- Tier 0: Bodyweight only
- Tier 1: Bands, sliders, rollers
- Tier 2: Dumbbells, kettlebells, plates
- Tier 3: Barbell, rack, bench
- Tier 4: Machines, cables
- Tier 5: Specialty (stones, sleds, GHD, competition equipment)

**THE GOLD RULE:** Only 🔴 Intense and 🟣 Technical unlock GOLD exercises.
GOLD = Olympic lifts, advanced plyometrics, spinal-loaded ballistics.
All other colors block GOLD regardless of Order.

| Emoji | Name | Tier | GOLD | Character |
|-------|------|------|------|-----------|
| ⚫ | Teaching | 2–3 | No | Extra rest, coaching cues, comprehension over exertion |
| 🟢 | Bodyweight | 0–2 | No | No gym required. Park, hotel, living room. |
| 🔵 | Structured | 2–3 | No | Prescribed sets/reps/rest. Trackable. Repeatable. |
| 🟣 | Technical | 2–5 | Yes | Precision. Lower volume, extended rest, quality focus. |
| 🔴 | Intense | 2–4 | Yes | Maximum effort. High volume. Reduced rest. Supersets OK. |
| 🟠 | Circuit | 0–3 | No | Station-based timed rotation. No barbells. Loop logic required. |
| 🟡 | Fun | 0–5 | No | Exploration and variety. Structured play within constraints. |
| ⚪ | Mindful | 0–3 | No | Slow tempo (4s eccentrics). Extended rest (2+ min). Breath. |

🟠 Circuit loop logic: Every station must change which tissue is working. No two adjacent stations target the same muscle group.

---

## The ± Operator Layer

After the zip code, the ± bridges to an operator — a Latin-derived verb setting session intent.
The operator derives from Axis × Color polarity.

Polarity split:
- **Preparatory Colors (inhale):** ⚫ Teaching, 🟢 Bodyweight, ⚪ Mindful, 🟡 Fun
- **Expressive Colors (exhale):** 🔵 Structured, 🟣 Technical, 🔴 Intense, 🟠 Circuit

**Default Operator Table:**

| Axis | Preparatory (⚫🟢⚪🟡) | Expressive (🔵🟣🔴🟠) |
|------|--------------------------|--------------------------|
| 🏛 Basics | 📍 pono (place/position) | 🤌 facio (execute/perform) |
| 🔨 Funct. | 🧸 fero (carry/transfer) | 🥨 tendo (extend/push limits) |
| 🌹 Aesth. | 👀 specio (inspect/observe) | 🦢 plico (fold/superset/layer) |
| 🪐 Chall. | 🪵 teneo (hold/anchor/persist) | 🚀 mitto (dispatch/deploy/launch) |
| ⌛ Time | 🐋 duco (orchestrate/conduct) | ✒️ grapho (write/prescribe/document) |
| 🐬 Partner | 🧲 capio (receive/assess/intake) | 🦉 logos (reason/analyze/interpret) |

The coach can override the default operator. Honor the override.

---

## Blocks (22 Session Containers)

Blocks are rooms inside a workout. The name is fixed. The content shifts by zip code.

**Four operational functions:**
- Orientation — Arriving, focusing, pointing intent
- Access/Preparation — Mobility, activation, priming
- Transformation — Where capacity is built or tested
- Retention/Transfer — Locking in, cooling down, bridging forward

| Emoji | Name | Role | Notes |
|-------|------|------|-------|
| ♨️ | Warm-Up | Orientation/Access | Always present. Always first (unless 🎯 opens). Content shifts by Order. |
| 🎯 | Intention | Orientation | One sentence. Quoted. Active voice. Frame the work, don't hype it. |
| 🔢 | Fundamentals | Access | Re-grounding in basics. Post-injury, post-layoff, teaching contexts. |
| 🧈 | Bread/Butter | Transformation | The main thing. Always present. Most volume. Most stimulus. |
| 🫀 | Circulation | Access | Blood flow, tissue prep. Early or mid-session. |
| ▶️ | Primer | Access | CNS activation. Bridges warm-up to main work. Neural potentiation. |
| 🎼 | Composition | Transformation | Movement arrangement. Strong in 🌾 Full Body. Composite header block. |
| ♟️ | Gambit | Access | Deliberate sacrifice for positional advantage. Pre-fatigue with purpose. |
| 🪜 | Progression | Access/Transform | Loading ramps. Ladders. In 🏟: the ramp to the test. |
| 🌎 | Exposure | Transformation | Reveal weaknesses under controlled stress. Expand movement vocabulary. |
| 🎱 | ARAM | Transformation | Station-based loops. Loop logic required. Box notation in markdown. |
| 🌋 | Gutter | Transformation | All-out effort. Rare. Only in 🔴 and 🪐. Never in 🖼, 🐂, or ⚪. |
| 🪞 | Vanity | Transformation | Appearance-driven. Pump work. Mirror muscles. Honest. Stigma-free. |
| 🗿 | Sculpt | Transformation | Hypertrophy shaping. Angles, tension, volume. Carving not admiring. |
| 🛠 | Craft | Transformation | Skill acquisition. Quality over load. Filters toward ⚫ and 🟣. |
| 🧩 | Supplemental | Transformation | Secondary work. Supports 🧈. Must be non-redundant. Different angles. |
| 🪫 | Release | Retention | Context-dependent: 🔴 = stress OUT. ⚪ = tension DOWN. 🖼 = return to baseline. |
| 🏖 | Sandbox | Transformation | Constrained exploration. 🟡 = play. ⚫ = safe learning. 🟣 = skill testing. |
| 🏗 | Reformance | Transformation | Corrective construction. Prehab, postural correction. Prominent in ⚖. |
| 🧬 | Imprint | Retention | Locking in patterns. High rep, low load, late session. Neural memory. |
| 🚂 | Junction | Retention | Bridge to next session. 1–3 follow-up zip codes with rationale. Logging space. |
| 🔠 | Choice | Modifier | Bounded autonomy. Applies to other blocks. Options must be valid for the code. |

System block:
| 🧮 | SAVE | Closing | Session complete. Log data. Archive. Every workout ends here. |

### Block sequence guidelines by Order

```
🐂 Foundation:   4–6 blocks  ♨️ 🔢/🛠 🧈 🧩 🧬 🚂
⛽ Strength:     5–6 blocks  ♨️ ▶️ 🧈 🧩 🪫 🚂
🦋 Hypertrophy:  6–7 blocks  ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂
🏟 Performance:  3–4 blocks  ♨️ 🪜 🧈 🚂  (no junk volume)
🌾 Full Body:    5–6 blocks  ♨️ 🎼 🧈 🧩 🪫 🚂
⚖ Balance:      5–6 blocks  ♨️ 🏗 🧈 🧩 🪫 🚂
🖼 Restoration:  4–5 blocks  🎯 🪫 🧈 🧬 🚂
```

### Color modifiers on block structure

- ⚫ Teaching: +extended rest, +🛠 Craft emphasis
- 🟢 Bodyweight: equipment collapses to tier 0–2
- 🔵 Structured: +🪜 Progression prominent
- 🟣 Technical: fewer blocks, extended rest, quality focus
- 🔴 Intense: 🧩 may superset, 🌋 Gutter possible
- 🟠 Circuit: 🧈/🧩/🪞 merge into 🎱 ARAM
- 🟡 Fun: +🏖 Sandbox and 🌎 Exposure permitted
- ⚪ Mindful: extended ♨️ and 🪫, slow tempo throughout

---

## Generation Rules

### Deck Identity Layer — Required Pre-Generation Context

Before generating any card, check if a deck identity document exists at `deck-identities/deck-[XX]-identity.md`. If it exists:

1. Read the full deck identity document before generating
2. Read the specific zip identity line for the zip code being generated
3. Use the zip identity line as the generation seed — it replaces guessing with direction
4. Follow the naming convention at `deck-identities/naming-convention.md` for the card title
5. Honor the coverage map — each card's primary exercise must match what the map specifies
6. Each Color variant of a Type MUST use a different primary exercise in 🧈 Bread & Butter

If no deck identity document exists for the target deck, generate using SCL rules alone (current behavior). The identity layer is additive, not blocking.


Execute these steps in order. Do not skip steps.

**Step 1 — Parse the Zip Code**
Extract all four dials. Load all parameter ceilings and constraints.
- Order → load ceiling, rep range, rest periods, max difficulty, CNS demand
- Axis → exercise selection bias, paired operators, exercise character
- Type → muscle groups, movement patterns
- Color → equipment tier, GOLD access, session format, structural rules

**Step 2 — Derive the Default Operator**
Read the Axis (position 2) and the Color (position 4).
Check the polarity table above. Preparatory Colors → first operator. Expressive Colors → second operator.
If the coach overrides the operator, honor the override.

**Step 3 — Derive the Block Sequence**
Use the Order × Color guidelines. Select the appropriate blocks. Count must match Order guidelines.
Apply Color modifiers on top.

**Step 4 — Select Exercises**
Every exercise must satisfy ALL FOUR dials simultaneously:
- Within Order's load ceiling and difficulty cap
- Matching Axis bias (rank accordingly, do not exclude)
- Training the Type's muscle groups and movement patterns
- Using only equipment within the Color's tier range
- GOLD exercises only if Color is 🔴 or 🟣
- **All exercises must exist in `exercise-library.md` — no exceptions**

**Step 5 — Format the Workout**
Use the SCL markdown format. All 15 required elements must be present.

---

## Required Format Elements

All 15 must be present in every generated card:

1. Title with flanking Type emojis
2. Subtitle: training modality, targets, honest time estimate
3. CODE line: the 4-dial zip code
4. 🎯 INTENTION: quoted, one sentence, active voice, direct
5. Numbered BLOCKS with emoji names and heavy border separators (═══)
6. At least one Operator call inline after a block header
7. Sub-block zip codes: BLOCK+TYPE+AXIS+COLOR format with parenthetical expansion: (Block | Muscle | Bias | Equipment)
8. Tree notation: ├─ for containment, │ for continuation
9. Reps before exercise name: "10 🍗 Squat" not "🍗 Squat × 10"
10. Type emoji before exercise name: "🪡 Deadlift"
11. Cues in parentheses, 3–6 words, conversational: "(slow, feel the stretch)"
12. Sets on individual lines with Order emoji: "Set 1: ⛽ 80% × 5 (context)"
13. Rest specified for every block
14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with rationale. Format: `Next → [zip] — [one-line reason]`
15. 🧮 SAVE with closing principle (1–2 sentences)

---

## Tonal Rules

These are not suggestions. They are constraints.

- Direct, not flowery
- Technical but human
- Conversational cues, not clinical jargon
- No motivational filler. No "You got this!" No "Crush it today!"
- No clinical language. No "optimize neuromuscular recruitment"
- Yes to "Hips back, not down." Yes to "Hold the weight in the bottom."
- 🎯 Intention: frame the work, do not hype it
- 🧮 SAVE closing principle: transfer the work, do not praise the user
- The workout speaks to a competent adult who does not need to be managed

---

## Common Generation Errors

**🪫 Release is not always a cool-down.** Direction depends entirely on context.
- 🔴 context = cathartic discharge, stress OUT
- ⚪ context = parasympathetic downregulation, tension DOWN
- 🖼 context = somatic return to baseline

**🌹 Aesthetic is not always isolation work.** In 🖼 Restoration context, the lens turns inward:
pelvic floor, psoas, diaphragm, deep hip structures. The aesthetic lens becomes somatic.
Do not assign cable curls to 🖼🌹.

**🧈 Bread & Butter is not always a heavy lift.**
- In 🏟 it is the test itself.
- In 🖼 it is the main mobility or somatic sequence.
- In ⚖ it is targeted accessory compounds addressing the specific gap.
The block name is fixed. The content shifts entirely by Order.

**⛽🟢 Bodyweight Strength is not a rest day and not a beginner workout.**
It is the check valve — does your gym strength transfer outside the gym?
Advanced calisthenics apply: muscle-ups, pistol squats, planche progressions, L-sits, archer push-ups.
The Order ceiling still applies to difficulty.

**🏟 Performance has 3–4 blocks only. No exceptions. No junk volume.**
Test. Record. Leave. That is the complete session.

**🌾 Full Body is not a superset. It is integration.**
Each movement must flow into the next without a reset.
The result must be a single unified pattern, not a sequence of movements.
If you would call it a superset, it does not belong in 🌾.

---


Card titles must follow naming convention. No titles starting with "The."
No Protocol, Prescription, Playground, Full Send, or vibe-speak. The title is
a phone book listing: [Movement/Equipment] — [Muscle/Focus, Context].
See deck-identities/naming-convention.md.

8 Colors = 8 different workouts, not 8 formats. If two Color variants of
the same Type use the same primary exercise, one of them is wrong. The Color
should change WHICH exercises appear, not just rest times and cue density.

## Validation Checklist

Before writing any workout to a file, verify all of the following.
If any check fails, revise before writing.

**Order compliance:**
- [ ] Load stays at or below Order ceiling
- [ ] Rep ranges match Order parameters
- [ ] Rest periods match Order parameters
- [ ] Difficulty stays at or below Order maximum
- [ ] Block count matches Order guidelines

**Type accuracy:**
- [ ] Exercises train the correct muscle groups
- [ ] Movement patterns match the Type

**Axis character:**
- [ ] Exercise selection reflects the Axis bias
- [ ] Would someone feel the Axis without being told?

**Color constraints:**
- [ ] All equipment within Color's tier range
- [ ] No barbells in 🟢 or 🟠
- [ ] GOLD exercises only in 🔴 or 🟣
- [ ] Loop logic applied in 🟠 Circuit

**Full Body integrity (🌾 only):**
- [ ] Flow test: Does each movement flow into the next without a reset?
- [ ] Unity test: Is the result a single unified pattern, not a sequence?
- [ ] Both must pass.

**Block structure:**
- [ ] 🧈 Bread & Butter is present and carries most volume
- [ ] Session flows Orient → Access → Transform → Retain
- [ ] Ends with 🚂 Junction and 🧮 SAVE

**Format:**
- [ ] All 15 required elements present
- [ ] Sub-block zip codes formatted correctly
- [ ] Tree notation used
- [ ] Tonal rules followed throughout

---

## File Naming Convention

**Stub (awaiting generation):**
`[zip]±.md`
Example: `⛽🏛🪡🔵±.md`

**Complete (workout generated):**
`[zip]±[operator emoji] [Workout Title].md`
Example: `⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`

The ± is the hinge point.
- Left of ± — machine-readable zip code address
- Right of ± — operator emoji + human-readable workout title

**Status markers in frontmatter:**
- `status: EMPTY` — stub file, awaiting workout generation
- `status: GENERATED` — workout written, pending review
- `status: CANONICAL` — reviewed and approved by Jake Berry

When you generate a workout, rename the stub file to the complete filename as part of the same commit.
Update frontmatter: `status: EMPTY` → `status: GENERATED`.

---

## What You Do Not Do

- Do not invent exercises that are not in `exercise-library.md`
- Do not exceed Order load ceilings under any circumstances
- Do not use GOLD exercises in non-GOLD colors
- Do not use barbells in 🟢 Bodyweight or 🟠 Circuit workouts
- Do not add motivational language or praise the user
- Do not generate junk volume in 🏟 Performance workouts
- Do not place 🌋 Gutter in 🖼 Restoration, 🐂 Foundation, or ⚪ Mindful workouts
- Do not treat supersets as valid in non-🔴 contexts unless specified
- Do not generate a workout without running the full validation checklist
- Do not generate a card without reading its deck identity document first (if one exists)
- Do not name a card without following deck-identities/naming-convention.md
- Do not use the same primary exercise in two Color variants of the same Type
- Do not modify files outside the scope of the current task
- Do not freelance between sessions. Read `whiteboard.md` first.

---

## Review guidelines

When reviewing PRs for SCL compliance (triggered with `@codex review`):

**Verify all of the following:**
- All exercises exist in `exercise-library.md`
- Order load ceilings are not exceeded
- GOLD exercises only appear with 🔴 or 🟣 colors
- No barbells in 🟢 Bodyweight or 🟠 Circuit
- No motivational filler or clinical jargon in tone
- All 15 required format elements are present
- Block count matches Order guidelines
- 🟠 Circuit cards have proper loop logic (no adjacent stations targeting same muscle group)
- 🏟 Performance cards have 3–4 blocks only with no junk volume
- 🌾 Full Body cards pass the Flow test and Unity test

**Flag only:**
- P0 — Hard constraint violations (exercise not in library, load ceiling exceeded, GOLD in wrong color, barbell in 🟢/🟠, 🏟 with >4 blocks)
- P1 — Exercise/format accuracy issues (missing required elements, tonal rule violations, block count out of range)

Do not flag style preferences. Do not flag P2 or lower.

---

Read the zip code. Honor the constraints. Fill the room.
🧮
