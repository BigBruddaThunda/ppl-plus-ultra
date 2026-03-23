# Ppl± Architectural Reset — Direction Document

**Date:** 2026-03-23
**Author:** Jake Berry + Claude (audit session)
**Status:** DIRECTION — not yet executed

---

## The Core Insight

Ppl± is a workout program. Everything else is DLC.

The current repo treats Ppl± as a universe-building project with a workout system embedded in it. The reset flips that: Ppl± is a workout product that can grow into a universe over time, one layer at a time.

---

## What The Product Is

A personal trainer in your pocket.

- Opens to today's workout
- Shows exercises with sets, reps, rest, cues
- Logs your work
- Tracks progress over time
- Adapts based on your equipment, schedule, and goals
- Rotates through a structured program (the zip code engine)

That's the whole product. Ship this first. Everything else is DLC.

---

## Decisions Made

| Question | Answer |
|----------|--------|
| Workout model | Static cards (improved) + hybrid templates that personalize at render time |
| SCL visibility | Emojis are decoration. Users see them, never need to understand them. The icon does the talking. |
| Repo strategy | Monorepo with packages. One home, organized layers. |
| MVP scope | Full rotation + preferences: equipment, schedule, goals, logging, progress, exercise swaps |
| Vision layers | Archived in /vault as DLC. Nothing deleted. Everything organized. Domain-hop friendly. |
| Block system | All 22 blocks available to any zip code. Blocks are expressive icons, not structural rules. The workout decides its blocks. |
| Exercise data | Database from day one (SQLite/Postgres with structured fields) |

---

## The Architectural Shift

### What changes from the current system

**BEFORE (current):**
- SCL is a constraint language with rules that must be followed
- Blocks are hard-assigned to Orders ("🐂 uses 4-6 blocks: ♨️ 🔢/🛠 🧈 🧩 🧬 🚂")
- 1,680 static markdown files with embedded workout content
- 57 KB CLAUDE.md teaching an AI how to be a workout language compiler
- Exercise library is a 134 KB markdown file
- 73 seeds, cosmograms, Operis, and vision docs mixed with workout content
- The zip code is presented as something users need to learn

**AFTER (rebuild):**
- SCL is an internal engine that produces workouts. Users never see the rules.
- Blocks are a visual vocabulary — any block can appear anywhere based on what the workout needs
- Exercise library lives in a database with structured fields
- Workouts are templates that get personalized (equipment, history, preferences)
- Emojis appear as natural icons in the UI — intuitive, never explained
- Vision content lives in /vault, clearly separated as future DLC
- The zip code is the internal address. Users see "Heavy Pull Day" with icons.

### What stays the same

- The 4-dial system (Order × Axis × Type × Color = 1,680 addresses)
- The 61 emoji vocabulary
- The 22 block icons
- The exercise library content (2,085 exercises)
- The rotation engine concept
- The operator layer (internal logic)
- The tonal voice (direct, technical, human — no motivation filler)

---

## Monorepo Package Structure (proposed)

```
ppl-plus-ultra/
├── packages/
│   ├── workout-engine/        ← THE PRODUCT
│   │   ├── exercises.db       ← SQLite: 2,085 exercises with structured fields
│   │   ├── templates/         ← Workout templates (improved cards, hybrid format)
│   │   ├── rotation/          ← Zip rotation engine (equipment, schedule, goals → today's workout)
│   │   ├── selection/         ← Exercise selection algorithm
│   │   └── scl/               ← SCL rules as code (not markdown specs)
│   │
│   ├── web/                   ← NEXT.JS APP
│   │   ├── src/app/           ← Routes: home, workout, log, progress, settings
│   │   ├── src/components/    ← UI components (clean rebuild)
│   │   └── src/lib/           ← Supabase, auth, Stripe
│   │
│   └── shared/                ← SHARED TYPES & UTILS
│       ├── types/             ← TypeScript types for zip codes, exercises, workouts
│       └── constants/         ← Emoji maps, color palettes, block definitions
│
├── vault/                     ← DLC ARCHIVE (organized, not active)
│   ├── operis/                ← Operis editorial system (seeds + editions)
│   ├── cosmograms/            ← Deep research identity docs
│   ├── seeds/                 ← 73 architectural vision documents
│   ├── projects/              ← graph-parti, story-engine, civic-atlas
│   ├── scl-deep/              ← Deep specification layer
│   ├── voice/                 ← Wilson, automotive, voice parser
│   ├── platform-v2/           ← Platform architecture docs
│   └── INDEX.md               ← What's in the vault, when to reactivate
│
├── archive/                   ← HISTORICAL ARTIFACTS
│   ├── cards-v1/              ← Current 1,680 generated cards (reference)
│   ├── middle-math-v1/        ← Current computation layer
│   ├── exercise-content-v1/   ← Current exercise knowledge files
│   └── session-log.md         ← Development history
│
├── CLAUDE.md                  ← SIMPLIFIED (~5-10 KB, workout product only)
├── README.md                  ← Public face of the workout product
└── turbo.json                 ← Turborepo config
```

---

## Exercise Database Schema (first draft)

```sql
CREATE TABLE exercises (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  section CHAR(1) NOT NULL,           -- A-Q from exercise library

  -- SCL mappings
  types TEXT NOT NULL,                 -- JSON array: ["🛒","🪡"]
  equipment_tier INTEGER NOT NULL,     -- 0-5
  gold_gated BOOLEAN DEFAULT FALSE,

  -- Muscle targeting
  primary_muscles TEXT NOT NULL,       -- JSON array
  secondary_muscles TEXT,              -- JSON array

  -- Movement classification
  movement_pattern TEXT,               -- press, pull, hinge, squat, carry, etc.
  bilateral BOOLEAN DEFAULT TRUE,
  compound BOOLEAN DEFAULT TRUE,

  -- Axis affinities (0-1 float, how well it fits each axis)
  basics_affinity REAL DEFAULT 0.5,
  functional_affinity REAL DEFAULT 0.5,
  aesthetic_affinity REAL DEFAULT 0.5,
  challenge_affinity REAL DEFAULT 0.5,
  time_affinity REAL DEFAULT 0.5,
  partner_affinity REAL DEFAULT 0.5,

  -- Order relevance
  min_order_difficulty INTEGER DEFAULT 1,  -- 1=Foundation, 7=Restoration
  max_order_difficulty INTEGER DEFAULT 5,

  -- Coaching
  cue_short TEXT,                      -- 3-6 word cue
  cue_detail TEXT,                     -- Full coaching note
  common_mistakes TEXT                 -- JSON array
);
```

---

## Block Philosophy Reset

The 22 blocks are NOT:
- Hard-assigned to specific Orders
- Required in specific sequences
- Structural rules that constrain generation

The 22 blocks ARE:
- Visual markers (emoji icons) that give a workout section its character
- Available to any zip code based on what the workout needs
- Expressive punctuation — like colored bullet points with personality
- Self-explanatory through their icon (♨️ = warm up, 🧈 = the main thing, 🌋 = all out)

A workout picks its blocks the way a writer picks their words. The vocabulary is fixed (22 blocks). The composition is free.

---

## What The User Experience Looks Like

### Day One
1. Sign up
2. Tell Ppl± your equipment (home gym? full gym? bodyweight?)
3. Tell Ppl± your schedule (3 days? 5 days? which days?)
4. Tell Ppl± your goals (strength? muscle? general fitness?)
5. Get your first workout

### Every Day After
1. Open app → see today's workout
2. Workout has: title, blocks with exercises, sets/reps/rest, coaching cues
3. Emojis appear naturally as section icons — never explained
4. Log each set as you go (weight, reps, notes)
5. Finish → see session summary
6. Over time: see progress charts, PR tracking, workout history

### What Users Don't See
- Zip codes (internal addressing)
- SCL rules (engine logic)
- Axis names (selection algorithm)
- Operator layer (session intent derivation)
- Block assignment rules (there are none — the workout picks its blocks)
- Polarity tables, Latin verbs, cosmograms, Operis

---

## Migration Path

### Phase 1: Organize (in this repo)
- Create /vault and move vision content there
- Create /archive and snapshot current generated cards
- Restructure as monorepo with Turborepo
- Write simplified CLAUDE.md focused on workout product

### Phase 2: Foundation (workout engine)
- Build exercise database from exercise-library.md
- Build exercise selection engine (port from middle-math)
- Build rotation engine (equipment + schedule + goals → today's zip)
- Build workout template system (improved card format)

### Phase 3: Web App (clean rebuild)
- Next.js with Supabase auth and database
- Workout display with block icons
- Set logging interface
- Progress tracking
- Stripe for subscriptions

### Phase 4+: DLC Layers (from vault)
- Reactivate seeds as they become relevant
- Operis editorial layer
- Community features
- Voice/automotive
- Cosmogram depth content
- Whatever else the product grows into

---

## Key Principle

Build the workout program. Ship the workout program.
Everything else waits in the vault until the workout program is solid.

The universe grows from a strong foundation, not the other way around.
