# Ppl± Architectural Reset — Direction Document

**Date:** 2026-03-23
**Author:** Jake Berry + Claude (audit session)
**Status:** DIRECTION — not yet executed
**Revision:** 2 — corrected zip code visibility, living library model, rebalance engine

---

## The Core Insight

Ppl± is a living workout library of 1,680 zip codes that constantly rebalances itself around the user.

The zip code is the product. It's the user-facing identity — visible, shareable, sortable, loggable. "I did ⛽🏛🪡🔵 today." All 61 SCL emojis live inside every workout as a design vocabulary. All 1,680 addresses exist for every user, all the time.

Everything beyond the workout library is DLC — organized in the vault, never deleted, layered back in when ready.

---

## What The Product Is

A living library of 1,680 workouts that knows you.

- All 1,680 zip codes exist for every user from day one
- Any workout can be chosen at any moment, any day
- The system also programs for you — rotation, progression, the seesaw
- Toggle off equipment (barbells, bands, running) → all 1,680 zip codes instantly recompute
- Log a workout → the system learns your numbers and adjusts everything
- Turn off barbells after 6 months → your strength data persists and informs the new state
- Everything is constantly balancing itself — a perpetual seesaw of progression

The zip code is both the address AND the identity. It's how you find workouts, how you log them, how you share them, how the system tracks them.

---

## The Design Vocabulary

All 61 SCL emojis are available inside any workout at any zip code.

A 🐂 Foundation workout might show ⛽🦋🏟 emojis next to individual exercises or sets — because those emojis describe the character of that specific movement within the workout. The 4-dial zip code sets the root identity. The full 61-emoji vocabulary colors everything inside.

**Zip codes are user-facing:**
- Visible as workout titles/headers
- Shareable shorthand ("I did ⛽🏛🪡🔵 today")
- The sorting/filtering key for your library
- The logging address for your training history
- The language users learn naturally through use, not instruction

**Emojis are a design vocabulary, not a constraint language:**
- They appear next to exercises, sets, blocks, sections
- They communicate character through the icon itself
- Users absorb meaning through repeated exposure
- No glossary needed — the symbol does the talking
- But there ARE real constraints (Order ceilings, Color equipment tiers, GOLD gates) — these are engine rules, not UI rules

---

## Decisions Made

| Question | Answer |
|----------|--------|
| Zip code visibility | User-facing. Visible, shareable, loggable. The workout's identity. |
| All 61 emojis | Available inside any workout. Design vocabulary throughout. |
| 1,680 pool | Every user has all 1,680 from day one. Always accessible. |
| Workout model | Static on spawn → living after first interaction. Toggles and logs trigger recomputation. |
| Rebalance engine | Toggle off equipment/approaches → all 1,680 update. Log data persists across state changes. |
| SCL constraints | Real but internal. Order ceilings, Color tiers, GOLD gates are engine rules. Users feel them, don't read them. |
| Block system | All 22 blocks available to any zip code. Character emerges from the Order, not from a validator. A 🏟 test has 3-4 blocks because that's what a test IS. |
| Exercise data | Database from day one with structured fields. |
| Repo strategy | Monorepo with packages. One home, organized layers. |
| Vision layers | Archived in /vault as DLC. Nothing deleted. Everything organized. |

---

## The Living Library Model

### Static on Spawn
When a new user signs up, all 1,680 zip codes populate with default workouts based on their initial settings (equipment, goals, schedule). These are the "factory defaults."

### Living After First Interaction
The moment a user:
- **Logs one workout** → the system has real data (weights, reps, perceived effort)
- **Toggles off equipment** → all 1,680 recompute exercise selection
- **Changes a preference** → the seesaw rebalances

### The Rebalance Rules
- Turn off barbells → exercises swap to dumbbells/machines/bodyweight across all relevant zip codes
- Turn off running → ➖ Ultra zip codes swap to rowing/cycling/other modalities
- Turn off calisthenics → 🟢 Bodyweight zip codes adjust to band/minimal equipment alternatives
- Six months of barbell data doesn't vanish when you flip the switch — it informs the system's understanding of your strength, and the replacement exercises inherit that context
- Progression data travels with the user, not with the equipment

### The Seesaw
Every workout logged shifts the balance:
- Trained 🛒 Push three times this week? The system knows your 🪡 Pull is due.
- Hit a PR on squat? The system adjusts neighboring zip codes upward.
- Missed a week? The system de-loads gently, doesn't pretend nothing happened.
- The rotation engine, the progression engine, and the rebalance engine are three systems working as one continuous seesaw.

---

## The Architectural Shift

### What changes from the current system

**BEFORE (current):**
- 1,680 static markdown files with embedded workout content
- Zip codes treated as internal addressing that users don't need to see
- SCL emojis limited to the 4 dials in each workout's zip code
- 57 KB CLAUDE.md teaching an AI how to be a workout language compiler
- Exercise library is a 134 KB markdown file
- Blocks hard-assigned to Orders
- 73 seeds, cosmograms, Operis mixed with workout content

**AFTER (rebuild):**
- 1,680 zip codes as a living library that recomputes per user state
- Zip codes are the product identity — visible, shareable, loggable
- All 61 SCL emojis available inside any workout as design vocabulary
- Exercise library in a database with structured fields
- Workouts are templates that personalize at render time (equipment, history, preferences)
- Blocks are free — any block in any workout
- Vision content organized in /vault as DLC
- Rebalance engine: toggle → recompute → persist historical context

### What stays the same

- The 4-dial system (Order × Axis × Type × Color = 1,680 addresses)
- The 61 emoji vocabulary (now used MORE, not less)
- The 22 block icons
- The exercise library content (2,085 exercises)
- The rotation engine concept
- The operator layer
- The tonal voice (direct, technical, human — no motivation filler)
- The real constraints (Order ceilings, Color equipment tiers, GOLD gates)

---

## Monorepo Package Structure (proposed)

```
ppl-plus-ultra/
├── packages/
│   ├── engine/                  ← THE CORE
│   │   ├── exercises/           ← Exercise database + selection algorithm
│   │   ├── resolver/            ← Zip code → workout resolution (the renderer)
│   │   ├── rebalance/           ← Toggle/log → recompute all 1,680
│   │   ├── rotation/            ← Which zip code today? The daily seesaw.
│   │   ├── progression/         ← Weight/rep/set tracking + auto-progression
│   │   └── scl/                 ← SCL rules as code (constraints, not specs)
│   │
│   ├── web/                     ← NEXT.JS APP
│   │   ├── src/app/             ← Routes: library, workout, log, progress, settings
│   │   ├── src/components/      ← UI components
│   │   └── src/lib/             ← Supabase, auth, Stripe
│   │
│   └── shared/                  ← SHARED TYPES & UTILS
│       ├── types/               ← TypeScript types for zip codes, exercises, workouts
│       └── constants/           ← Emoji maps, color palettes, block definitions
│
├── vault/                       ← DLC ARCHIVE (organized, not active)
│   ├── operis/                  ← Operis editorial system
│   ├── cosmograms/              ← Deep research identity docs
│   ├── seeds/                   ← 73 architectural vision documents
│   ├── projects/                ← graph-parti, story-engine, civic-atlas
│   ├── scl-deep/                ← Deep specification layer
│   ├── voice/                   ← Wilson, automotive, voice parser
│   ├── platform-v2/             ← Platform architecture docs
│   └── INDEX.md                 ← What's in the vault, when to reactivate
│
├── archive/                     ← HISTORICAL ARTIFACTS
│   ├── cards-v1/                ← Current 1,680 generated cards (reference)
│   ├── middle-math-v1/          ← Current computation layer
│   └── session-log.md           ← Development history
│
├── CLAUDE.md                    ← SIMPLIFIED (~5-10 KB, workout product only)
├── README.md                    ← Public face
└── turbo.json                   ← Turborepo config
```

### Engine Architecture

The engine has five systems that work together:

```
User State (equipment, goals, schedule, history)
    │
    ├── Resolver: zip code + user state → rendered workout
    │     Uses: exercise DB, SCL constraints, user equipment, user history
    │
    ├── Rebalance: state change → recompute affected zip codes
    │     Triggers: equipment toggle, preference change, extended absence
    │     Preserves: all historical training data across state changes
    │
    ├── Rotation: user state + date + history → today's recommended zip
    │     The daily seesaw. Balances push/pull/legs, orders, recovery.
    │
    ├── Progression: workout log → updated training maxes + auto-adjustment
    │     Tracks: weight, reps, RPE per exercise per user
    │     Feeds: Resolver (next time this exercise appears, it's updated)
    │
    └── Selection: zip constraints + user state → exercise list
          The algorithm that picks exercises for a given zip code + user
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
  equipment_tier_min INTEGER NOT NULL, -- Minimum tier needed (0-5)
  equipment_tier_max INTEGER NOT NULL, -- Maximum tier it works in (0-5)
  equipment_tags TEXT,                 -- JSON array: ["barbell","rack","bench"]
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
  min_order_difficulty INTEGER DEFAULT 1,
  max_order_difficulty INTEGER DEFAULT 5,

  -- Coaching
  cue_short TEXT,                      -- 3-6 word cue
  cue_detail TEXT,                     -- Full coaching note
  common_mistakes TEXT                 -- JSON array
);

-- User's training history per exercise
CREATE TABLE user_exercise_log (
  id INTEGER PRIMARY KEY,
  user_id TEXT NOT NULL,
  exercise_id INTEGER NOT NULL REFERENCES exercises(id),
  zip_code CHAR(4) NOT NULL,          -- Which zip code this was logged under
  logged_at TIMESTAMP NOT NULL,
  weight REAL,
  reps INTEGER,
  sets INTEGER,
  rpe REAL,                           -- Rate of perceived exertion
  notes TEXT
);

-- User's current equipment/preference state
CREATE TABLE user_settings (
  user_id TEXT PRIMARY KEY,
  equipment_available TEXT NOT NULL,   -- JSON array of equipment tags
  goals TEXT,                          -- JSON array: ["strength","muscle","general"]
  schedule TEXT,                       -- JSON: days per week, which days
  disabled_modalities TEXT,            -- JSON: ["running","calisthenics"]
  updated_at TIMESTAMP NOT NULL
);

-- Derived: user's current estimated maxes per exercise
-- Recomputed from user_exercise_log whenever needed
CREATE TABLE user_exercise_state (
  user_id TEXT NOT NULL,
  exercise_id INTEGER NOT NULL REFERENCES exercises(id),
  estimated_1rm REAL,                 -- Calculated from log history
  last_weight REAL,
  last_reps INTEGER,
  last_logged TIMESTAMP,
  trend TEXT,                         -- "progressing", "plateau", "deloading"
  PRIMARY KEY (user_id, exercise_id)
);
```

---

## What The User Experience Looks Like

### Day One
1. Sign up
2. Tell Ppl± your equipment (what do you have access to?)
3. Tell Ppl± your goals (strength? muscle? general fitness? sport?)
4. Tell Ppl± your schedule (how many days? which days?)
5. All 1,680 zip codes populate with your defaults
6. The system recommends your first workout (or you browse the library)

### The Library
- Browse all 1,680 zip codes — filtered by your settings
- Each zip code shows: emoji address, title, what it trains, what equipment it uses
- Filter by Order (strength, hypertrophy, etc.), Type (push, pull, legs), equipment
- Zip codes you've disabled appear grayed/hidden (but never deleted)
- Your "active library" adjusts based on your toggles

### A Workout
- Title: the zip code + human-readable name
- All 61 emojis appear naturally throughout — next to blocks, exercises, sets
- Order emoji next to each set tells you the loading character
- Block emojis mark sections (♨️ Warm-Up, 🧈 Main Work, 🚂 Bridge)
- Exercise cues in conversational tone
- Log button on every set: weight, reps, done

### The Toggle
- Settings: turn equipment on/off, change modality preferences
- Flip a switch → the rebalance engine fires → all 1,680 zip codes update
- Your history doesn't vanish — the system remembers every weight you've ever lifted
- New exercises inherit context from your training history

### The Seesaw
- Log workouts → the system tracks your balance across push/pull/legs, orders, axes
- The rotation engine recommends what's next based on your history
- Miss a week → gentle deload. Hit PRs → progression nudge.
- It's not a fixed program — it's a living system that breathes with you

### Sharing
- "I did ⛽🏛🪡🔵 today" — the zip code IS the shorthand
- Other users know exactly what that means (or learn through exposure)
- Zip codes become the shared language of the community

---

## Migration Path

### Phase 1: Organize (in this repo)
- Create /vault and move vision content there
- Create /archive and snapshot current generated cards
- Restructure as monorepo with Turborepo
- Write simplified CLAUDE.md focused on workout product

### Phase 2: Engine Foundation
- Build exercise database from exercise-library.md (structured, queryable)
- Build the Resolver: zip code + user state → rendered workout
- Build the Selection algorithm: zip constraints + equipment → exercise list
- Build the Rebalance engine: state change → recompute affected zips

### Phase 3: Web App
- Next.js with Supabase auth and database
- The Library: browse/filter/search all 1,680 zip codes
- The Workout: display with all 61 emojis as design vocabulary
- The Log: per-set logging with weight/reps/RPE
- The Settings: equipment toggles that trigger rebalance
- The Seesaw: progression tracking, rotation recommendations

### Phase 4: The Living System
- Progression engine (auto-adjust weights/reps based on history)
- Full rotation engine (daily recommendations based on balance)
- Historical context preservation across equipment changes
- Community features (share zip codes, compare workouts)

### Phase 5+: DLC Layers (from vault)
- Operis editorial layer
- Voice/automotive
- Cosmogram depth content
- Platform features as the community grows

---

## Codex Bot Tension Log

These are friction points identified by the Codex connector bot reviewing this direction document against the existing CLAUDE.md architecture. They're documented here because they reveal exactly where the old system and the new direction collide — and what the rebuild needs to handle.

### Tension 1: Block Restrictions (P1 flag)

**What the bot said:** Marking blocks as "all 22 available to any zip code" conflicts with hard SCL rules that pin each Order to a narrow block count (e.g., 🏟 = 3-4 blocks only).

**Resolution:** The bot is defending validator rules that the reset dissolves. But the underlying wisdom is real — a Performance test SHOULD be 3-4 blocks. The difference is WHERE the constraint lives:
- **Old system:** A validator rule rejects a 5-block 🏟 card. The constraint is a rung in the scan cycle.
- **New system:** The resolver naturally produces 3-4 blocks for 🏟 because that's what a test session IS. The constraint is emergent from good workout design, not enforced by a linter.

The Order still sets the character. The engine still knows that 🏟 = test/record/leave. But it knows this as design intelligence, not as a line-count validator. A workout can break the "rule" if it has a good reason — the old system couldn't allow that.

### Tension 2: Equipment Tier Schema (P1 flag)

**What the bot said:** The schema uses a single `equipment_tier INTEGER` but exercises span tier ranges. The current selector uses min/max.

**Resolution:** The bot is correct. Fixed in this revision: `equipment_tier` → `equipment_tier_min` + `equipment_tier_max`. A barbell back squat needs tier 3 minimum but works in a tier 5 gym. The range is the right model.

### Pattern: What These Tensions Reveal

The Codex bot is defending the current CLAUDE.md as ground truth. Every tension point is a place where the new direction explicitly contradicts the old constraints. This is expected — the reset IS a contradiction of the old approach.

The tensions are useful because they map exactly which old rules need to be:
1. **Preserved as engine logic** (Order ceilings, Color tiers, GOLD gates, equipment ranges)
2. **Dissolved into design intelligence** (block counts, block sequences, block-to-Order assignments)
3. **Elevated to user-facing features** (zip code visibility, emoji vocabulary, the living library)

As the Codex bot flags more tensions, they get logged here. Each one is a design decision, not a bug.

---

## Key Principles

1. **The zip code is the product.** Not hidden infrastructure. The user-facing identity.
2. **All 1,680 exist, all the time.** Users can pick any workout at any moment. The system also recommends.
3. **All 61 emojis live everywhere.** The design vocabulary is the full set, not just the 4-dial address.
4. **Toggle → recompute → preserve.** Equipment changes trigger rebalance. History never vanishes.
5. **The seesaw never stops.** Every workout logged shifts the balance. The system breathes with the user.
6. **Constraints are real but invisible.** Order ceilings, Color tiers, GOLD gates — engine rules that users feel, never read.
7. **Vision content waits in the vault.** Ship the workout library. Layer everything else on top.
8. **Tensions are design decisions.** When the old system and new direction collide, log the tension, make the call, move on.
