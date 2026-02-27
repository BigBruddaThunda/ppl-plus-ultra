# PPL±

## Push Pull Legs Plus Ultra

A semantic training language. 61 emojis. 1,680 workouts.

PPL± is a workout generation and programming system built on SCL —
Semantic Compression Language. Four emojis produce a complete workout
address. Every parameter of that workout — load, reps, rest, equipment,
exercise character, and session structure — is encoded in those four
characters.

Created by Jake Berry.

---

## The Zip Code

Every workout in PPL± has a 4-emoji address called a zip code.

```
⛽ 🏛 🪡 🔵
│  │  │  └── COLOR  — Equipment and session format
│  │  └───── TYPE   — Muscle groups and movement domain
│  └──────── AXIS   — Exercise character and selection bias
└─────────── ORDER  — Load ceiling and training phase
```

This address is the complete specification. Every exercise, every set,
every rest period, every block in the session is determined by these
four dials working together.

The system produces 7 × 6 × 5 × 8 = **1,680 unique workout addresses**.

---

## The Language — 61 Emojis Across 7 Categories

### Orders (7) — The Loading Protocol

| Emoji | Name | Load | Reps | Character |
|-------|------|------|------|-----------|
| 🐂 | Foundation | ≤65% | 8–15 | Pattern learning. The on-ramp for any skill at any level. |
| ⛽ | Strength | 75–85% | 4–6 | Neural adaptation. Force production. Not bodybuilding. |
| 🦋 | Hypertrophy | 65–75% | 8–12 | Muscle growth. Volume and metabolic stress. |
| 🏟 | Performance | 85–100%+ | 1–3 | Testing, not training. Record and leave. |
| 🌾 | Full Body | ~70% | 8–10 | Integration. Movements that flow as one unified pattern. |
| ⚖ | Balance | ~70% | 10–12 | Correction. Microscope on weak links and asymmetries. |
| 🖼 | Restoration | ≤55% | 12–15 | Recovery without debt. Leave fresher than you arrived. |

### Types (5) — The Muscle Groups

| Emoji | Name | Muscles |
|-------|------|---------|
| 🛒 | Push | Chest, front delts, triceps |
| 🪡 | Pull | Lats, rear delts, biceps, traps, erectors |
| 🍗 | Legs | Quads, hamstrings, glutes, calves |
| ➕ | Plus | Full body power and core |
| ➖ | Ultra | Cardiovascular system and endurance |

### Axes (6) — Exercise Character

| Emoji | Name | Character |
|-------|------|-----------|
| 🏛 | Basics | Bilateral, stable, barbell-first classics |
| 🔨 | Functional | Unilateral, standing, athletic transfer |
| 🌹 | Aesthetic | Isolation, full ROM, mind-muscle connection |
| 🪐 | Challenge | Hardest variation at any level |
| ⌛ | Time | Clock as training variable |
| 🐬 | Partner | Social training context |

### Colors (8) — Equipment and Session Format

| Emoji | Name | Equipment Tier | GOLD |
|-------|------|---------------|------|
| ⚫ | Teaching | 2–3 | No |
| 🟢 | Bodyweight | 0–2 | No |
| 🔵 | Structured | 2–3 | No |
| 🟣 | Technical | 2–5 | Yes |
| 🔴 | Intense | 2–4 | Yes |
| 🟠 | Circuit | 0–3 | No |
| 🟡 | Fun | 0–5 | No |
| ⚪ | Mindful | 0–3 | No |

GOLD exercises — Olympic lifts, advanced plyometrics, spinal-loaded
ballistics — are only unlocked by 🟣 Technical and 🔴 Intense.

---

## The ± Operator

After the zip code, the ± symbol bridges to an operator — a Latin-derived
action verb that sets the session's intent.

```
⛽🏛🪡🔵 ± 🤌 Heavy Classic Pulls
```

The operator is derived from the Axis × Color polarity. Each Axis pairs
with two operators split by color type.

| Axis | Preparatory (⚫🟢⚪🟡) | Expressive (🔵🟣🔴🟠) |
|------|----------------------|----------------------|
| 🏛 Basics | 📍 pono | 🤌 facio |
| 🔨 Functional | 🧸 fero | 🥨 tendo |
| 🌹 Aesthetic | 👀 specio | 🦢 plico |
| 🪐 Challenge | 🪵 teneo | 🚀 mitto |
| ⌛ Time | 🐋 duco | ✒️ grapho |
| 🐬 Partner | 🧲 capio | 🦉 logos |

The operator becomes part of the file name. The full semantic address of
a workout is its complete filename:

```
⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md
```

Five emojis and a title. The entire scope of the workout in one filename.

---

## The 42 Decks

The 1,680 zip codes organize into 42 decks — one for each Order × Axis
combination. Each deck contains 40 cards (5 Types × 8 Colors).

| | 🏛 | 🔨 | 🌹 | 🪐 | ⌛ | 🐬 |
|---|---|---|---|---|---|---|
| 🐂 | 01 | 02 | 03 | 04 | 05 | 06 |
| ⛽ | 07 | 08 | 09 | 10 | 11 | 12 |
| 🦋 | 13 | 14 | 15 | 16 | 17 | 18 |
| 🏟 | 19 | 20 | 21 | 22 | 23 | 24 |
| 🌾 | 25 | 26 | 27 | 28 | 29 | 30 |
| ⚖ | 31 | 32 | 33 | 34 | 35 | 36 |
| 🖼 | 37 | 38 | 39 | 40 | 41 | 42 |

---

## Repository Structure

```
ppl-plus-ultra/
│
├── README.md              — This file
├── CLAUDE.md              — Agent operating instructions
├── whiteboard.md          — Active decisions and current phase
│
├── scl-directory.md       — Complete SCL language reference
├── exercise-library.md    — All valid exercises mapped to SCL (v.0)
│
├── scl-deep/              — Full uncompressed SCL specifications (source layer)
├── seeds/                 — Architectural ideas for future phases (planted, not active)
│   ├── experience-layer-blueprint.md   — Master technical architecture for Phases 4-7
│   ├── numeric-zip-system.md           — 4-digit numeric addressing standard
│   ├── data-ethics-architecture.md     — Data collection, privacy, export, deletion
│   ├── mobile-ui-architecture.md       — 4-dial UI, tool drawer, pinch-zoom canvas
│   ├── stripe-integration-pipeline.md  — Subscription products, checkout, webhooks
│   ├── claude-code-build-sequence.md   — 20-session build plan (A-N + V-Z)
│   ├── automotive-layer-architecture.md — Android Auto / CarPlay audio layer
│   ├── voice-parser-architecture.md    — Universal natural language building navigation
│   ├── wilson-voice-identity.md        — Wilson: the PPL± voice identity
│   └── regional-filter-architecture.md — Opt-in regional content filter
├── html/                  — HTML experience layer scaffold (Phase 4/5)
├── middle-math/           — Computation engine: weights, exercise selection, user context, rendering
├── deck-identities/       — Pre-generation exercise mapping per deck
├── deck-cosmograms/       — Deep research identity documents per deck (planned)
├── zip-web/               — Navigation graph: fatigue signatures, routing pods
│
├── scripts/               — Validation, progress, automation tools
├── .claude/               — Skills, agents, hooks, settings
├── .codex/                — Codex agent infrastructure
├── .github/               — CI pipeline configs (planned)
│
└── cards/
    └── [order]/[axis]/[type]/
        └── [zip]±.md                        — Stub. Awaiting generation.
        └── [zip]±[operator] [Title].md      — Complete. Workout generated.
```

### Card File Status

Every card file carries a status marker in its frontmatter.

```
status: EMPTY      — Stub file. Awaiting workout generation.
status: GENERATED  — Workout written. Pending review.
status: CANONICAL  — Reviewed and approved. Master version.
```

To see how many rooms are still waiting:

```bash
grep -r "status: EMPTY" cards/ | wc -l
```

---

## The Blocks — 22 Session Containers

Workouts are built from named blocks. The block name is fixed. The
content shifts completely based on the zip code.

| Emoji | Block | Role |
|-------|-------|------|
| ♨️ | Warm-Up | Always present. Always first. |
| 🎯 | Intention | One sentence framing the session. |
| 🔢 | Fundamentals | Re-grounding in basic patterns. |
| 🧈 | Bread & Butter | The main thing. Always present. |
| 🫀 | Circulation | Blood flow and tissue prep. |
| ▶️ | Primer | CNS activation before heavy work. |
| 🎼 | Composition | Movements arranged to cooperate. |
| ♟️ | Gambit | Deliberate sacrifice for advantage later. |
| 🪜 | Progression | Loading ramp toward peak. |
| 🌎 | Exposure | Revealing weaknesses under stress. |
| 🎱 | ARAM | Station-based loops with loop logic. |
| 🌋 | Gutter | All-out effort. Rare and deliberate. |
| 🪞 | Vanity | Appearance-driven pump work. Honest. |
| 🗿 | Sculpt | Hypertrophy shaping with angles and volume. |
| 🛠 | Craft | Skill acquisition. Quality over load. |
| 🧩 | Supplemental | Secondary work supporting Bread & Butter. |
| 🪫 | Release | Letting go. Direction depends on context. |
| 🏖 | Sandbox | Constrained exploration within boundaries. |
| 🏗 | Reformance | Corrective construction. Prehab. |
| 🧬 | Imprint | Locking in patterns. Neural memory. |
| 🚂 | Junction | Bridge to next session. Follow-up zip suggestions. |
| 🔠 | Choice | Bounded autonomy modifier. Pick from valid options. |

Every workout ends with 🧮 SAVE — the closing ritual and session archive.

---

## The Exercise Library

`exercise-library.md` contains the complete valid exercise pool for PPL±
generation. All exercises used in any workout must come from this library.

~2,185 exercises across 17 sections (A–Q), each mapped to SCL Types,
Orders, Axes, Equipment Tiers, and GOLD gate status.

This is v.0. The library grows as the system develops.

---

## What This Repository Is Building

The `.md` card files are the master source of truth — the architectural
blueprint for every workout. They are not replaced. They are rendered.

The downstream pipeline:

```
.md card (master blueprint)
    ↓
HTML workout card (experience layer)
    ↓
User interactive session (log, check, track)
    ↓
User history written back to account
    ↓
Personal exercise database grows with use
```

The HTML layer renders the `.md` structure as an interactive workout card.
SCL blocks become collapsible UI sections. Each block emoji carries its
own visual identity. Users log weights, check sets, track time — all
mapped back to the zip code address.

User data never touches the master `.md` files. The master stays clean.
User history lives in their account version. Many users, same master,
different histories.

---

## Project Status

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | Repository scaffolding and root documents | **Complete** |
| 2 | Workout generation — all 1,680 cards | **In Progress** — 80/1,680 (Decks 07, 08) |
| 2.5 | Architecture expansion (cosmograms, linters, zip-web, middle-math) | **Framed** |
| 3 | Validation and review | Pending |
| 4 | Design standards and UI system | **Blueprinted** — 11 architecture documents planted |
| 5 | HTML rendering layer | **Blueprinted** — 20-session build sequence specified |
| 6 | User account and logging system | **Blueprinted** — Supabase + Stripe pipeline specified |
| 7 | Launch | **Blueprinted** — Session N deployment spec written |

---

## Goal Mapping — Quick Reference

| Goal | Code Path |
|------|-----------|
| Learn the basics | 🐂 + Type + 🏛 + ⚫ |
| Get stronger | ⛽ + Type + any Axis + 🔵 |
| Build muscle | 🦋 + Type + 🌹 + 🔴 |
| Test your max | 🏟 + Type + 🏛 + 🟣 |
| Full body workout | 🌾 + Type + any Axis + any Color |
| Fix a weak link | ⚖ + Type + 🌹 + 🟡 |
| Active recovery | 🖼 + Type + 🌹 + ⚪ |
| No gym available | any + any + any + 🟢 |
| Quick session | any + ⌛ + any + 🟢 |
| Train with a partner | any + 🐬 + any + 🔵 |
| HIIT | any + ➖ + ⌛ + 🔴 |
| Zone 2 cardio | 🖼 + ➖ + 🏛 + ⚪ |
| Hard yoga / mobility | 🖼 + ➕ + 🪐 + 🔴 |
| Hip and psoas work | 🖼 + 🍗 + 🌹 + ⚪ |

---

61 emojis. Seven categories. 1,680 rooms.

Fill them.

🧮
