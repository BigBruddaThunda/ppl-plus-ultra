# CLAUDE.md — PPL± Project Operating Instructions

You are working inside the PPL± repository.
This file is your operating context. Read it before touching anything else.

---

## CURRENT PROJECT PHASE

**Phase: 2 — Workout Generation**
Status: Deck 08 (⛽🔨 Strength Functional) complete — 80/80 cards generated across 2 decks. 1,600 cards remaining across 40 decks.
Priority: Continue deck generation when instructed.
Active task: See `whiteboard.md` for current session instructions.

**Do not freelance. Read `whiteboard.md` before acting.**

---

## WHAT THIS PROJECT IS

PPL± is a semantic training language and workout generation system built by Jake Berry.
It uses 61 emojis across 7 categories to produce 1,680 unique workout addresses called
zip codes. Each zip code is a 4-emoji address that fully specifies a workout's loading
protocol, muscle group, exercise character, and equipment format.

The system is called SCL — Semantic Compression Language.

This repository is the master source of truth for all 1,680 workouts.

**Your role in this repository:**
- Parse zip codes and generate workouts that honor every constraint
- Write generated workouts into the correct card files
- Rename stub files to their full semantic filenames upon generation
- Never hallucinate parameters. If a constraint is unclear, re-read this file.
- Never exceed Order ceilings. The Order is the law.

---

## DOWNSTREAM ARCHITECTURE

The `.md` card files are the master blueprints for a web application.
Each card file will be ported to an interactive HTML workout card.
Each HTML card becomes a loggable, interactive room for users.
User workout history writes back to their personal exercise database.

A hallucinated exercise in a `.md` file propagates through:
`.md → HTML render → user workout session → user history → preference data.`

**Content accuracy is the highest priority constraint in this repository.**
When in doubt about an exercise or parameter, do not guess. Flag it.

---

## REPOSITORY STRUCTURE

```
ppl-plus-ultra/
├── README.md              — Public face. What this is and how to navigate it.
├── CLAUDE.md              — This file. Your operating instructions.
├── whiteboard.md          — Active decisions, current phase, open questions.
├── scl-directory.md       — Complete SCL reference. Every rule lives here.
├── exercise-library.md    — All valid exercises mapped to SCL types. v.0
├── scl-deep/              — Full uncompressed SCL specifications (source layer).
├── seeds/                 — Architectural ideas for future phases (planted, not active).
├── html/                  — HTML experience layer scaffold (Phase 4/5).
└── cards/
    └── [order]/[axis]/[type]/
        └── [zip]±.md                        — Stub. Awaiting generation.
        └── [zip]±[op] [Title].md            — Complete. Workout generated.
```

Card files live at:
`cards/[order-folder]/[axis-folder]/[type-folder]/[filename].md`

Example:
`cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`

---

## ADDITIONAL DIRECTORIES

### scl-deep/ — Deep Specification Layer

This directory holds the full uncompressed specifications behind the SCL. `scl-directory.md` (root) is the compiled operational reference you use during generation. `scl-deep/` holds the source specifications that `scl-directory.md` compresses.

You do not need to read scl-deep/ for card generation. It is reference material for design system work, validation logic, and future features.

Contents:
- `color-context-vernacular.md` — 8 Colors as tonal communication system (beyond equipment/format). Imported from v1.0, needs vocabulary update from 25 to 61 emoji system.
- `order-parameters.md` — Full periodization science, exercise attributes, conflict rules, volume landmarks, pairing matrices, micro-periodization, contraindication logic. Imported from v2.0, needs vocabulary update.
- `axis-specifications.md` — Dual-layer Axis framework: Layer 1 (in-workout exercise character) + Layer 2 (app-level content floors). Working draft.
- `vocabulary-standard.md` — Language standard. Banned/approved word lists. ExRx factual register. Operator verb preference. Companion to publication-standard.md.
- Stub files for blocks, operators, types — to be written.

### seeds/ — Architectural Seeds

Planted ideas for future phases. Seeds don't block current work. See `seeds/README.md` for the full index.

Do not build from seeds unless whiteboard.md promotes a seed to active work.

Key architectural decisions planted:
- **Default Rotation Engine** — 3-gear daily zip system (Order by weekday, Type by rolling 5-day calendar, Axis by monthly operator). The automation clock underneath the entire user experience.
- **Axis-as-App-Floors** — The 6 Axes serve dual function: in-workout exercise bias AND app-level content spaces (6 floors of the building). The most significant architectural insight since the zip code system.
- **Macro Almanac** — 12 operators mapped to 12 months with agricultural rationale and annual breath rhythm (4-month inhale → 4-month exhale → 2-month catch-breath → 2-month close).
- `daily-architecture.md` — SUPERSEDED by operis-architecture.md (Feb 26, 2026). Historical record: The Daily as content type, standing departments, five input layers, automation pathway.
- `operis-architecture.md` — PPL± Operis: complete specification. Weekly editorial cadence (7 Orders × Trivium/Quadrivium), 17 standing departments with activation-by-Order matrix, Operis↔Cosmogram feedback loop, construction vehicle pipeline (8–12 zip codes forced per edition). Supersedes daily-architecture.md.
- `content-types-architecture.md` — 109 content types mapped to 6 Axes with cross-floor appearance rule, 12-operator engagement model, and Order-as-curriculum (Trivium/Quadrivium depth levels).
- `operis-naming-rationale.md` — "Operis" etymology: Latin genitive ("of the work"). Phonetically approximates "off the press." Associative field: opera, opus, operate. PPL± brand name readings documented.
- `elevator-architecture.md` — The 4-dial elevator model: Order=building, Axis=floor, Type=wing, Color=room. Piano nobile floor stack (🔨 ground → 🏛 noble → ⌛ 2nd → 🐬 3rd → 🌹 4th → 🪐 5th). Dual axis function. Horizontal (zip web) and vertical (floor stack) navigation.
- `platform-architecture-v2.md` — Complete platform architecture refactored from Feb 11 "PPL± ITSELF." Business model (Tier 1 $10, Tier 2 $25–30), UX flows (card/deck/room metaphor, onboarding sequence), tech stack (Next.js/Supabase/Vercel/Stripe), zip-code-centric database schema, automation as deterministic pipeline. Supersedes platform-architecture-v1-archive.md.
- `seeds/operis-prompt-pipeline.md` — 4-prompt Operis generation pipeline: handoff contracts, Color flow (3 Color identities), department activation matrix, rotation engine V1.0 reference, automation pathway.
- `seeds/operis-educational-layer.md` — 8-lane educational content system mapped to Color Context Vernacular tonal registers, seasonal content architecture, SCL emoji content lattice.
- `seeds/operis-color-posture.md` — Color of the Day as cognitive posture: three Color identities (workout/publication/Operis), eight postures, determination inputs, automation scoring pathway.
- `seeds/operis-sandbox-structure.md` — 13-room Sandbox: 8 deterministic Color siblings + 5 editorially-derived Content Rooms, content-to-zip mapping, ExRx naming convention, generation implications.
- `seeds/operis-researcher-prompt.md` — Operis Prompt 1: Researcher. Takes a date, produces Research Brief (Contract A). V4.0.
- `seeds/operis-content-architect-prompt.md` — Operis Prompt 2: Content Architect. Takes Research Brief, produces Enriched Content Brief (Contract B) including Color of the Day. V4.0.
- `seeds/operis-editor-prompt.md` — Operis Prompt 3: Editor. Takes both briefs, writes the full Operis edition (Contract C) with 13-room sandbox (8 siblings + 5 Content Rooms). V4.0.
- `seeds/operis-builder-prompt.md` — Operis Prompt 4: Builder. Proofs edition, generates cards for empty zip codes, commits to repository. V4.0.

### operis-editions/ — Operis Editorial Record

Daily Operis editions filed by date (YYYY/MM/YYYY-MM-DD.md). Subdirectories:
- `operis-editions/historical-events/` — Date-indexed historical events database (366 files planned, MM-DD.md format, currently empty). Prompt 1 checks this path before web research.

### html/ — Experience Layer Scaffold

Directory skeleton for the HTML rendering layer (Phase 4/5). Currently scaffold only — no functional HTML.

Do not generate HTML content unless whiteboard.md indicates Phase 4/5 is active.

---

## FILE NAMING CONVENTION

**Stub (awaiting generation):**
`[zip]±.md`
Example: `⛽🏛🪡🔵±.md`

**Complete (workout generated):**
`[zip]±[operator emoji] [Workout Title].md`
Example: `⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`

The ± is the hinge point.
- Left of ± — machine-readable zip code address
- Right of ± — operator emoji + human-readable workout title

The operator emoji bridges the address and the title.
The full filename is the complete semantic identity of the workout.

When you generate a workout, you rename the stub file to the complete filename
as part of the same commit.

---

## CARD STUB TEMPLATE

When creating stub files, use this exact format:

```
---
zip: ORDERAXISTYPECOLOR
operator: [derived operator emoji] [latin name]
status: EMPTY
deck: [deck number]
order: [emoji] [Name] | [load%] | [rep range] | [rest] | CNS: [level]
axis: [emoji] [Name] | [character description]
type: [emoji] [Name] | [muscle groups]
color: [emoji] [Name] | Tier [X–X] | GOLD: [Yes/No] | [format description]
blocks: [derived block sequence using block emojis]
---

This card is unfilled. Generate workout at this address using SCL rules in scl-directory.md.
```

Example stub for ⛽🏛🪡🔵:

```
---
zip: ⛽🏛🪡🔵
operator: 🤌 facio
status: EMPTY
deck: 07
order: ⛽ Strength | 75–85% | 4–6 reps | 3–4 min rest | CNS: High
axis: 🏛 Basics | Bilateral, barbell-first, proven classics
type: 🪡 Pull | Lats, rear delts, biceps, traps, erectors
color: 🔵 Structured | Tier 2–3 | GOLD: No | Prescribed sets/reps/rest
blocks: ♨️ → ▶️ → 🧈 → 🧩 → 🪫 → 🚂 → 🧮
---

This card is unfilled. Generate workout at this address using SCL rules in scl-directory.md.
```

---

## GENERATION SEQUENCE (per card)

When instructed to generate a workout for a zip code:

1. Locate the stub file at the correct path in `cards/`
2. Read the stub frontmatter to confirm zip code and parameters
3. Run the full validation checklist mentally before writing anything
4. Generate the complete workout in SCL markdown format
5. Replace stub content with generated workout
6. Update frontmatter: `status: EMPTY` → `status: GENERATED`
7. Rename the file from `[zip]±.md` to `[zip]±[op] [Title].md`
8. Update `whiteboard.md`: log the zip code as generated
9. Do not move to the next card until the current card passes validation

---

## THE 4-DIAL ZIP CODE

Every workout is a 4-emoji address. Format: ORDER AXIS TYPE COLOR

```
Position 1: ORDER  (7)  — Load ceiling. Training phase. The law.
Position 2: AXIS   (6)  — Exercise character. Selection bias.
Position 3: TYPE   (5)  — Muscle groups. Movement domain.
Position 4: COLOR  (8)  — Equipment tier. Session format.
```

Total combinations: 7 × 6 × 5 × 8 = **1,680 zip codes**.

**Constraint hierarchy when dials conflict:**
1. ORDER — Hard ceiling. Nothing exceeds it. Ever.
2. COLOR — Hard filter. Equipment is binary.
3. AXIS  — Soft bias. Ranks exercises, does not exclude.
4. Equipment — Practical filter. What is actually available.

---

## THE 61 SCL EMOJI DICTIONARY

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

**Order character notes:**

🐂 Foundation — Pattern learning at sub-maximal load. The on-ramp for any new
skill at any level. Not beginner-only. A 20-year lifter learning Olympic lifts
uses 🐂. The ceiling: if load exceeds 65%, reps drop below 8, or difficulty
exceeds 2 — it is not 🐂 regardless of what else the code says. Order is the ceiling. The ceiling does not bend.

⛽ Strength — Neural adaptation. Heavy loads, low reps, full recovery. Force
production. Not bodybuilding. The pump is irrelevant here.

🦋 Hypertrophy — Muscle growth through volume and metabolic stress. Load is a
tool for tension, not the goal. The pump matters.

🏟 Performance — Testing, not training. You test, record, and leave. No junk
volume after the test. 🏟 blocks hypertrophy-style accumulation by default.
Scope: strength benchmarks, conditioning benchmarks, movement assessments,
sport-specific tests.

🌾 Full Body — Integration. Movements must flow into each other as one unified
pattern. **Flow and Unity Test is mandatory:** (1) Does one movement flow into the
next without a reset? (2) Is the result a single unified pattern? Both must be
yes. Thrusters pass. Squat-then-row-as-separate-movements fails.

⚖ Balance — Correction. Microscope on weak links and asymmetries.
⚖🛒 = triceps, side delts, front delts. ⚖🪡 = biceps, rear delts, forearms,
grip. ⚖🍗 = calves, adductors, tibialis. ⚖➕ = rotational stability,
anti-rotation. ⚖➖ = energy system gaps, aerobic base.

🖼 Restoration — Recovery without training debt. You leave fresher than you
entered. Extended scope: somatic movement, TRE, pelvic floor, deep hip work,
diaphragmatic breathing, nervous system regulation.
🖼 + 🌹 + ⚪ = the deepest recovery lane in the system.

### TYPES (5) — The Muscle Groups

| Emoji | Name | Muscles | Primary Patterns |
|-------|------|---------|-----------------|
| 🛒 | Push | Chest, front delts, triceps | Horizontal press, vertical press |
| 🪡 | Pull | Lats, rear delts, biceps, traps, erectors | Row, pulldown, hinge |
| 🍗 | Legs | Quads, hamstrings, glutes, calves | Squat, lunge, hinge, isolation |
| ➕ | Plus | Full body power, core | Olympic lifts, carries, plyometrics, anti-rot |
| ➖ | Ultra | Cardiovascular system | Rowing, cycling, running, conditioning, flows |

### AXES (6) — Exercise Character and Selection Bias

**🏛 Basics (Firmitas) — Ranking axis**
Bilateral, stable, time-tested fundamentals. Barbell classics first.
Priority: Barbell > dumbbell. Bilateral > unilateral. Compound > isolation.
Classic > novel. Would someone feel this axis without being told? Yes,
if the exercises are the barbell staples that have anchored training for decades.

**🔨 Functional (Utilitas) — Ranking axis**
Unilateral, standing, athletic-transfer movements.
Priority: Unilateral > bilateral. Standing > seated. Free weight > machine.
Ground-based > bench-based.

**🌹 Aesthetic (Venustas) — Ranking axis**
Isolation, full ROM, mind-muscle connection. Feel over load.
Priority: Isolation > compound. Cable/machine > barbell. Feeling > load.
In 🖼 Restoration context: lens turns inward — pelvic floor, psoas,
diaphragm, deep hip structures. The aesthetic lens becomes somatic.

**🪐 Challenge (Gravitas) — Ranking axis**
Hardest variation at any level. Deficit, pause, tempo, bands, chains,
unstable surfaces, stricter execution. Scales to the individual — always
the hardest version they can control.

**⌛ Time (Temporitas) — Context axis**
Enables: EMOM, AMRAP, density blocks, timed sets, time trials, TUT,
steady state, zone work. The specific protocol comes from Order × Color:
⌛🔴 = density/AMRAP. ⌛⚪ = meditative holds. ⌛🏟 = time trials.
⌛🔵 = EMOM.

**🐬 Partner (Sociatas) — Context axis**
Enables: Spottable, alternating, synchronized, competitive, assisted,
station rotation, scalable load, teachable. Machine work deprioritized.
Surfaces exercises that work with another person present.

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
| 🟠 | Circuit | 0–3 | No | Station-based timed rotation. No barbells. Loop logic req. |
| 🟡 | Fun | 0–5 | No | Exploration and variety. Structured play within constraints. |
| ⚪ | Mindful | 0–3 | No | Slow tempo (4s eccentrics). Extended rest (2+ min). Breath. |

🟠 Circuit loop logic rule: Every station must change which tissue is
working. No two adjacent stations target the same muscle group. A circuit
is not a list of exercises done quickly — it is a deliberate tissue-rotation
loop where each station recovers while others work.

---

## THE ± OPERATOR LAYER

After the zip code, the ± bridges to an operator — a Latin-derived verb
that sets session intent. The operator is derived from Axis × Color polarity.

Polarity split:
- **Preparatory Colors (inhale):** ⚫ Teaching, 🟢 Bodyweight, ⚪ Mindful, 🟡 Fun
- **Expressive Colors (exhale):**  🔵 Structured, 🟣 Technical, 🔴 Intense, 🟠 Circuit

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

## BLOCKS (22) — Session Containers

Blocks are rooms inside a workout. The name is fixed. The content is
context-dependent based on the zip code. Same block name, completely
different content depending on Order, Axis, Type, and Color.

**Four operational functions:**
- Orientation        — Arriving, focusing, pointing intent
- Access/Preparation — Mobility, activation, priming
- Transformation     — Where capacity is built or tested
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

**Block sequence guidelines by Order:**

```
🐂 Foundation:   4–6 blocks  ♨️ 🔢/🛠 🧈 🧩 🧬 🚂
⛽ Strength:     5–6 blocks  ♨️ ▶️ 🧈 🧩 🪫 🚂
🦋 Hypertrophy:  6–7 blocks  ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂
🏟 Performance:  3–4 blocks  ♨️ 🪜 🧈 🚂  (no junk volume)
🌾 Full Body:    5–6 blocks  ♨️ 🎼 🧈 🧩 🪫 🚂
⚖ Balance:      5–6 blocks  ♨️ 🏗 🧈 🧩 🪫 🚂
🖼 Restoration:  4–5 blocks  🎯 🪫 🧈 🧬 🚂
```

**Color modifiers on block structure:**
- ⚫ Teaching:  +extended rest, +🛠 Craft emphasis
- 🟢 Bodyweight: equipment collapses to tier 0–2
- 🔵 Structured: +🪜 Progression prominent
- 🟣 Technical:  fewer blocks, extended rest, quality focus
- 🔴 Intense:    🧩 may superset, 🌋 Gutter possible
- 🟠 Circuit:    🧈/🧩/🪞 merge into 🎱 ARAM
- 🟡 Fun:        +🏖 Sandbox and 🌎 Exposure permitted
- ⚪ Mindful:    extended ♨️ and 🪫, slow tempo throughout

---

## OPERATORS (12) — Training Action Verbs

| Emoji | Name | Meaning |
|-------|------|---------|
| 🧲 | capio | Receive, assess, intake. The catching phase. Absorbing eccentric. |
| 🐋 | duco | Orchestrate, lead, conduct. Session architecture and tempo flow. |
| 🤌 | facio | Execute, perform, produce. The concentric. The doing. |
| 🧸 | fero | Carry, transfer, channel. Loaded carries. Transfers across sessions. |
| ✒️ | grapho | Write, program, prescribe, document. Record the set. Log the PR. |
| 🦉 | logos | Reason, assess, analyze, interpret. Movement quality. Load calc. |
| 🚀 | mitto | Dispatch, deploy, launch, commit. Explosive intent. Max attempt. |
| 🦢 | plico | Fold, superset, compress, layer. Two exercises interwoven. |
| 📍 | pono | Set, position, assign. Stance, grip, body placement. The approach. |
| 👀 | specio | Inspect, observe, assess form, monitor. Video. Power leakage. |
| 🥨 | tendo | Stretch, lengthen, push limits. Extend ROM. Reach lockout. |
| 🪵 | teneo | Hold, anchor, persist. Isometrics. Sustained tension. Duration. |

## SYSTEM (1)

| Emoji | Name | Meaning |
|-------|------|---------|
| 🧮 | SAVE | Session complete. Log data. Archive. Closing ritual. Every workout ends here. |

---

## GENERATION RULES

When given a zip code, execute these steps in order. Do not skip steps.

**Step 1 — Parse the Zip Code**
Extract all four dials. Load all parameter ceilings and constraints.
- Order → load ceiling, rep range, rest periods, max difficulty, CNS demand
- Axis  → exercise selection bias, paired operators, exercise character
- Type  → muscle groups, movement patterns
- Color → equipment tier, GOLD access, session format, structural rules

**Step 2 — Derive the Default Operator**
Read the Axis (position 2) and the Color (position 4).
Check the polarity table above. Preparatory Colors → first operator.
Expressive Colors → second operator.
If the coach overrides the operator, honor the override.

**Step 3 — Derive the Block Sequence**
Use the Order × Color guidelines above.
Select the appropriate blocks. Count must match Order guidelines.
Apply Color modifiers on top.

**Step 4 — Select Exercises**
Every exercise must satisfy ALL FOUR dials simultaneously:
- Within Order's load ceiling and difficulty cap
- Matching Axis bias (rank accordingly, do not exclude)
- Training the Type's muscle groups and movement patterns
- Using only equipment within the Color's tier range
- GOLD exercises only if Color is 🔴 or 🟣
- All exercises must exist in `exercise-library.md`

**Step 5 — Format the Workout**
Use the SCL markdown format. All 15 required elements must be present.

---

## REQUIRED FORMAT ELEMENTS (all 15 must be present)

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
14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with brief rationale. Format: `Next → [zip] — [one-line reason]`
15. 🧮 SAVE with closing principle (1–2 sentences)

---

## TONAL RULES

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

## COMMON GENERATION ERRORS — READ BEFORE GENERATING

**🪫 Release is not always a cool-down.** Direction depends entirely on context.
  - 🔴 context = cathartic discharge, stress OUT
  - ⚪ context = parasympathetic downregulation, tension DOWN
  - 🖼 context = somatic return to baseline

**🌹 Aesthetic is not always isolation work.** In 🖼 Restoration context,
  the lens turns inward: pelvic floor, psoas, diaphragm, deep hip structures.
  The aesthetic lens becomes somatic. Do not assign cable curls to 🖼🌹.

**🧈 Bread & Butter is not always a heavy lift.**
  - In 🏟 it is the test itself.
  - In 🖼 it is the main mobility or somatic sequence.
  - In ⚖ it is targeted accessory compounds addressing the specific gap.
  The block name is fixed. The content shifts entirely by Order.

**⛽🟢 Bodyweight Strength is not a rest day and not a beginner workout.**
  It is the check valve — does your gym strength transfer outside the gym?
  Advanced calisthenics apply: muscle-ups, pistol squats, planche progressions,
  L-sits, archer push-ups. The Order ceiling still applies to difficulty.

**🏟 Performance has 3–4 blocks only. No exceptions. No junk volume.**
  The urge to add supplemental work after a test is wrong. Resist it.
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

## VALIDATION CHECKLIST

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

## EXERCISE LIBRARY

All exercises used in generated workouts must come from `exercise-library.md`.

The library contains ~2,185 exercises across 17 sections (A–Q).
Each section declares its SCL Type mapping, Order relevance, Axis emphasis,
Equipment Tier range, GOLD gate status, and Operator affinity.

**Type routing:**
- 🛒 Push  → Sections C (Chest), B (Shoulders anterior/lateral), E (Arms — triceps #51–95)
- 🪡 Pull  → Sections D (Back), B (Shoulders posterior/rotator cuff), E (Arms — biceps #1–50), G (Hips — hip hinge patterns)
- 🍗 Legs  → Sections H (Thighs), G (Hips & Glutes), I (Lower Leg & Foot)
- ➕ Plus  → Sections F (Core), J (Olympic Lifts), K (Plyometrics), L (Kettlebell), Q (Strongman)
- ➖ Ultra → Sections M (Cardio & Conditioning), O (Footwork & Agility), N (Sport Focused), K (Plyometrics — conditioning use)

**GOLD-gated sections (require 🔴 or 🟣):**
- Section J: All 85 Olympic lift exercises
- Section K: All 65 plyometric exercises
- Section Q: All 55 strongman exercises
- Section B: #9 Push Jerk, #14 Log Press, #137–140 Barbell/Hang/Power/Muscle Snatch, #141–144 Sandbag/Keg/Atlas shoulder work
- Section C: #121–125 Bamboo bar, earthquake bar, board press, sling shot
- Section D: #264 Yoke Walk, #265 Zercher Carry, #270 Keg Carry, #319 Atlas Stone Lift, #320 Tire Flip

---

## DECK REFERENCE

42 decks total (7 Orders × 6 Axes). 40 cards per deck (5 Types × 8 Colors).

| | 🏛 | 🔨 | 🌹 | 🪐 | ⌛ | 🐬 |
|----|-----|-----|-----|-----|-----|-----|
| 🐂 | 01 | 02 | 03 | 04 | 05 | 06 |
| ⛽ | 07 | 08 | 09 | 10 | 11 | 12 |
| 🦋 | 13 | 14 | 15 | 16 | 17 | 18 |
| 🏟 | 19 | 20 | 21 | 22 | 23 | 24 |
| 🌾 | 25 | 26 | 27 | 28 | 29 | 30 |
| ⚖ | 31 | 32 | 33 | 34 | 35 | 36 |
| 🖼 | 37 | 38 | 39 | 40 | 41 | 42 |

---

## STATUS CONVENTION

Card files carry a status marker in their frontmatter.

```
status: EMPTY      — Stub file. Awaiting workout generation.
status: GENERATED  — Workout written. Pending review.
status: CANONICAL  — Reviewed and approved. This is the master version.
```

Scan for empty rooms:
```bash
grep -r "status: EMPTY" cards/
```

---

## WHAT YOU DO NOT DO

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
- Do not freelance between sessions. Read `whiteboard.md` first.

---

61 emojis. Seven categories. 1,680 rooms.

Read the zip code. Honor the constraints. Fill the room.

---

## INFRASTRUCTURE LAYER — Tools, Skills, Hooks, Subagents

This section documents the automation infrastructure built during the infrastructure sprint.
These tools are available in every session. They are not optional — they are part of the workflow.

### Scripts (deterministic tools — run with bash)

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/validate-card.py` | Validate a single card against SCL rules | `python scripts/validate-card.py [card-path]` |
| `scripts/progress-report.py` | Dashboard of generation progress | `python scripts/progress-report.py` |
| `scripts/validate-deck.sh` | Validate all cards in a deck folder | `bash scripts/validate-deck.sh [deck-folder-path]` |
| `scripts/audit-exercise-coverage.py` | Check for duplicate primary exercises within a deck | `python scripts/audit-exercise-coverage.py [deck-folder-path]` |

### Skills (invoke with / commands)

| Skill | Purpose | Invoke |
|-------|---------|--------|
| generate-card | Full single-card generation pipeline | `/generate-card ⛽🌹🛒🔵` |
| build-deck-identity | Create deck identity document with exercise mapping | `/build-deck-identity 09` |
| progress-report | Run progress dashboard | `/progress-report` |
| retrofit-deck | Upgrade pre-V2 deck to current standards | `/retrofit-deck 07` |

### Subagents (isolated workers)

| Agent | Model | Purpose |
|-------|-------|---------|
| card-generator | Opus | Generate cards in isolated context |
| deck-auditor | Sonnet | Read-only compliance audit of completed decks |
| progress-tracker | Haiku | Lightweight repo state scan |

### Hooks (automatic)

| Trigger | What it does |
|---------|-------------|
| PostToolUse (Edit/Write on cards/) | Auto-runs validate-card.py on the edited file |
| SessionStart (startup) | Runs progress-report.py and displays dashboard |
| SessionStart (compact) | Re-injects phase context after compaction |

### Session startup sequence

Every session should follow this sequence:
1. CLAUDE.md is read automatically (ground floor context)
2. SessionStart hook fires → progress dashboard displays
3. Read whiteboard.md for current task and session state
4. If generating cards: use /generate-card or delegate to card-generator subagent
5. If auditing: delegate to deck-auditor subagent
6. After any card write: PostToolUse hook auto-validates
7. End of session: update whiteboard.md with results

### When to use what

- **Script** = deterministic check that runs the same way every time. Use for validation.
- **Skill** = multi-step workflow with judgment calls. Use for generation and identity building.
- **Subagent** = isolated context worker. Use when you don't want to fill the main context.
- **Hook** = automatic trigger. Use for things that must happen every time without being asked.

---

## TEMP PPL± ARCHITECT PATTERN

PPL± uses external AI environments (Genspark, Claude.ai web) as
read-only architect workspaces. These sessions cannot write to the
repo. They produce blueprint documents that Claude Code executes.

**How It Works**

1. Jake opens a Genspark or Claude.ai chat with task context
2. Pastes relevant sections from CLAUDE.md, whiteboard.md, and task
3. External AI does research, planning, drafting (unlimited usage)
4. Output: a Claude Code handoff document — the blueprint
5. Jake pastes blueprint into Claude Code session for execution
6. Claude Code reads whiteboard.md, executes, logs results

**Key Principle**

The temp architect READS and DRAFTS. It never touches the repo.
Claude Code READS and EXECUTES. It never freelances.
The handoff document is the contract between them.

**When You Receive a Handoff**

If a session starts with "Source: Genspark temp architect session"
or similar, the task list in that handoff is pre-researched and
pre-planned. Execute in order. Flag conflicts with whiteboard.md
state if found — the handoff may reference outdated state.

---

## DECK COSMOGRAM LAYER

Deck cosmograms live at `deck-cosmograms/deck-[NUMBER]-cosmogram.md`.
They are deep research identity documents — NOT workout cards.

**When generating cards for a deck:**
1. Read CLAUDE.md (this file) — ground floor
2. Read scl-directory.md — full SCL spec
3. Read the deck's cosmogram (if populated) — deep context
4. Read the deck identity doc (if exists) — exercise mapping
5. Generate the card

If a cosmogram's status is STUB or the file doesn't exist yet,
generate cards using scl-directory.md and deck identity alone.
The cosmogram is supplemental context, not a generation blocker.

Status: Research prompt and publication standard committed.
No cosmograms populated yet. Generation can begin.
- Research prompt: `seeds/cosmogram-research-prompt.md`
- Publication standard: `scl-deep/publication-standard.md`
- Output target: `deck-cosmograms/deck-[NUMBER]-cosmogram.md`
See `deck-cosmograms/README.md` for the full plan.

---

## LINTING LAYER

Status: PLANNED — directory structure planted, no tools built yet.

Three-tier validation pipeline (planned):
1. markdownlint-cli2 — structural markdown compliance
2. Frontmatter schema validator — YAML shape validation
3. SCL validator — PPL±-specific rules (`scripts/validate-card.py`)

The existing PostToolUse hook (validate-card.py) is Tier 3's
foundation. GitHub Actions CI will be the gate before merge.

Config directory: `.github/linters/`
Workflow directory: `.github/workflows/`
Seed document: `seeds/linters-architecture.md`

Do not build linting infrastructure unless whiteboard.md promotes it
to active work. The seed has the full architecture.

---

## PROJECT ARCHITECTURE — WORK STREAMS

The project has grown beyond the original 7-phase plan. Multiple
parallel work streams now exist. They are tracked here so nothing
gets lost. Each stream has a current status and a blocking/non-blocking
relationship to card generation.

**Active Streams**

| Stream | Status | Blocks Generation? |
|--------|--------|--------------------|
| Card Generation (Phase 2) | ACTIVE — 80/1,680 done | N/A — this IS the work |
| Deck Identities | ACTIVE — Deck 08 done, Deck 07 pending retrofit | Yes for new decks |
| Zip-Web Pods | BUILT — Deck 07 populated, 41 stubs ready | No |
| Infrastructure (scripts/skills/hooks) | BUILT — Session 18 | No |
| Deck Cosmograms | READY — prompt + standard committed, awaiting first generation | No |
| Linters Pipeline | PLANNED — seed planted | No |
| SCL Emoji Macros | DRAFTED — in external notes | No |
| Cosmogram Research Prompt | DRAFTED — in external notes | No |
| Git-Worktree Pattern | PLANNED — seed planted | No |
| HTML Experience Layer | Phase 4/5 — scaffold only | No |
| Codex Agent Infrastructure | BUILT — Session 4 | No |
| PPL± Operis Build-Out | ACTIVE — pipeline architecture planted Session 028 | No |
| Elevator/Floor Model | SEED — planted Session 022 | No |
| Platform Architecture V2 | SEED — planted Session 022 | No |
| Middle-Math Engine | PLANTED — architecture seeded Session 024 | No |

**Blocked Queue (waiting on dependencies)**

| Task | Blocked By | Unblocks |
|------|-----------|----------|
| Retrofit Deck 07 to V2 | Jake review of Deck 08 V2 pattern | Deck 07 → CANONICAL |
| Build Deck 09 identity | Deck 07 retrofit (confirms V2 pattern) | Deck 09 generation |
| Ralph Loop (41 remaining pod decks) | Deck 07 pod review | Full zip-web navigation |
| First cosmogram population | Session time (prompt + standard committed) | Deep content layer |
| Linters CI pipeline | Seed promoted to active + configs written | Merge-to-main policy |

---

## MIDDLE-MATH LAYER

The `middle-math/` directory is the computation engine between the SCL
specification and the rendered user experience. It contains weight system
declarations, exercise selection algorithms, user context specifications,
rotation engine formalization, rendering derivation logic, and the preserved
math primitives from the Hero's Almanac system.

Status: Architecture planted. Weight declarations in first-draft for Orders.
Remaining categories (Axes, Types, Colors, Blocks, Operators) are stubbed.

The middle-math layer does not block card generation. It is infrastructure
for the procedural workout engine that will eventually render workouts
from templates + user context instead of static card content.

Current card generation (fully-specified workout cards) continues. The
template-based format is an evolution, not a replacement. Both formats
will coexist — existing cards remain valid, new cards can use either format.

See `middle-math/ARCHITECTURE.md` for the complete system overview.

---

## SCL-61 EMOJI MACROS

A deep reference document covering cultural, historical, symbolic,
and cross-domain macro meanings for all 61 SCL emojis is drafted.

Target location: `scl-deep/emoji-macros.md`
Current status: STUB in `seeds/scl-emoji-macros-draft.md` (awaiting full document paste)
Relationship: Tier 0 reference alongside `color-context-vernacular.md`,
`order-parameters.md`, `axis-specifications.md` in `scl-deep/`

This does not change generation rules. It deepens understanding of
the design intent — why each emoji was chosen for its role.

---

## SCL-DEEP EXPANSION — SESSION 027

Two new documents added to the SCL-deep and middle-math layers:

- `scl-deep/vocabulary-standard.md` — Language standard. Banned/approved word lists. ExRx factual register. Operator verb preference. Covers all PPL± content surfaces: cards, Operis, README, cosmograms, whiteboard prose. Companion to publication-standard.md.

- `middle-math/rotation/reverse-weight-resolution.md` — Temporal zip-code resolution algorithm. Yesterday→today→tomorrow triangulation. Adjusts the rotation engine's default zip by looking backward at yesterday's fatigue signature and forward at tomorrow's stimulus requirements. Operis editorial implication: featured Sandbox room is the reverse-weight resolution room.

---

## NUMERIC ZIP NOTATION

Every SCL emoji has a numeric position on its dial. The 4-digit numeric zip code is the system-layer addressing key for URLs, databases, APIs, and every context where emojis cannot operate.

```
ORDER: 🐂=1  ⛽=2  🦋=3  🏟=4  🌾=5  ⚖=6  🖼=7
AXIS:  🏛=1  🔨=2  🌹=3  🪐=4  ⌛=5  🐬=6
TYPE:  🛒=1  🪡=2  🍗=3  ➕=4  ➖=5
COLOR: ⚫=1  🟢=2  🔵=3  🟣=4  🔴=5  🟠=6  🟡=7  ⚪=8
```

Example: ⛽🏛🪡🔵 = 2123. URL: /zip/2123. Database key: '2123'.

The emoji is the display layer. The number is the system layer. Both always present. Conversion is a single array lookup. See `seeds/numeric-zip-system.md`.

Deck derivation: `deck = (order - 1) * 6 + axis`. Zip 2123 → Deck 7. Zip 2223 → Deck 8.

---

## EXPERIENCE LAYER ARCHITECTURE

The experience layer is specified in seed documents planted February 26, 2026. These define the complete technical architecture for rendering .md cards as interactive room experiences, handling user accounts, processing payments, and delivering the mobile UI.

**Core documents:**
- `seeds/experience-layer-blueprint.md` — Master technical architecture (tech stack, routing, rendering, weight→CSS)
- `seeds/numeric-zip-system.md` — 4-digit numeric addressing standard
- `seeds/mobile-ui-architecture.md` — 4-dial UI, tool drawer, pinch-zoom canvas, 4 interaction states
- `seeds/data-ethics-architecture.md` — Data collection, privacy, export, deletion
- `seeds/stripe-integration-pipeline.md` — Subscription products, checkout, webhooks, RLS gating
- `seeds/claude-code-build-sequence.md` — 20-session build plan (Sessions A-N launch + V-Z automotive)

**Voice and audio layer:**
- `seeds/voice-parser-architecture.md` — Universal building navigation: natural language to zip + floor + content type. 3-layer keyword scoring. ~13,000 entries. No AI model. Handles workouts, info queries, personal data, almanac, education, community, multi-intent.
- `seeds/wilson-voice-identity.md` — Wilson: the PPL± voice. TTS identity, floor-specific register, response patterns. Not a chatbot.
- `seeds/automotive-layer-architecture.md` — Android Auto / CarPlay. Operis read aloud, voice zip nav, playlists, free-tier audio funnel.
- `seeds/regional-filter-architecture.md` — Opt-in region, seasonal content, no GPS/no tracking.

**Schema:**
- `middle-math/schemas/zip-metadata-schema.md` — Revised zip_metadata table with CHAR(4) numeric primary key

These documents do not block Phase 2-3 card generation. They become active when Phase 4 begins.

---

## DATA ETHICS POSITION

PPL± collects only what the user explicitly provides through their own action. No analytics fingerprinting. No third-party tracking. No selling data. Full data export on request. Full data deletion on command. The business model is subscriptions — the user is the customer, not the product.

This is a technical architecture decision, not a political statement. PPL± is not affiliated with any party or faction. Jake Berry, the creator, is not PPL± itself. The system's position on data matches the character of the system.

See `seeds/data-ethics-architecture.md` for the complete specification.

---

## PPL± OPERIS BUILD-OUT — SESSION 028

- Seed planted: `seeds/operis-architecture.md` (supersedes `seeds/daily-architecture.md`)
- Architecture complete: weekly editorial cadence, 109 content types, generation pipeline spec, front page card layout, depth standard, age-neutral register (Session 027)
- Pipeline architecture planted: `seeds/operis-prompt-pipeline.md` — 4-prompt pipeline with handoff contracts and Color flow (Session 028)
- Educational layer planted: `seeds/operis-educational-layer.md` — 8-lane content system mapped to Color Context Vernacular (Session 028)
- Color of the Day architecture planted: `seeds/operis-color-posture.md` — cognitive posture system, three Color identities, automation pathway (Session 028)
- Sandbox structure planted: `seeds/operis-sandbox-structure.md` — 13-room architecture (8 Color siblings + 5 Content Rooms), content-to-zip mapping (Session 028)
- Historical events database directory planted: `operis-editions/historical-events/` (Session 028)
- Reverse-weight resolution seeded: `middle-math/rotation/reverse-weight-resolution.md`
- Vocabulary standard seeded: `scl-deep/vocabulary-standard.md`
- Color weight derivation updated: `middle-math/rendering/operis-weight-derivation.md` — Color of the Day scoring mechanism planned (Session 028)
- Publication standard updated: `scl-deep/publication-standard.md` — Color as Cognitive Posture extension added (Session 028)
- ✅ COMPLETE (Session 029): Stored four Operis V4 prompts as seeds (seeds/operis-researcher-prompt.md, seeds/operis-content-architect-prompt.md, seeds/operis-editor-prompt.md, seeds/operis-builder-prompt.md). Pipeline updated with version tags, department alignment, prompt file reference. Sandbox and architecture docs updated.
- NEXT: Test full Operis V4 pipeline on a real date (run P1→P2→P3→P4 in sequence). Then continue Deck 09 identity and generation.
- Requires: historical events database (366 files, one-time build ~180 hours research, builds incrementally)
- Requires: cosmogram population (provides deep substrate for featured zip descriptions)
- Requires: HTML experience layer (Phase 4/5)
- Automation target: fully automated Operis generation from deterministic inputs + Color scoring mechanism
- Does not block card generation

---

🧮
