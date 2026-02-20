# Whiteboard — PPL± Active Working Memory

This file is the project's short-term memory.
Update it at the start and end of every working session.
It is not documentation. It is a living scratchpad.

Current Phase

Phase 2 — Workout Generation

Phase 1 complete. All infrastructure is in place.
1,680 stub files ready. Workout generation begins now.
Deck priority and generation order to be confirmed before first card is written.

What Is Done — Phase 1 (COMPLETE)

- [x] Project architecture planned
- [x] CLAUDE.md drafted and complete
- [x] README.md drafted and complete
- [x] whiteboard.md drafted (this file)
- [x] scl-directory.md populated (106k chars, full SCL spec)
- [x] exercise-library.md populated (~128k chars, ~2,800 exercises, sections A–Q)
- [x] setup.py written, debugged, and executed
- [x] GitHub repository created
- [x] Claude Code linked to repository
- [x] setup.py executed — 1,680 stubs generated across 210 folders
- [x] All root files committed and pushed to GitHub

What Is Next — Phase 2

1. ✅ Deck confirmed: Deck 07 — ⛽🏛 Strength Basics (40 cards)
2. ✅ Batch size confirmed: Full deck in one session
3. Generate all 40 cards: ⛽🏛[TYPE][COLOR] × 5 Types × 8 Colors
4. For each card: parse zip → validate → generate → rename stub → log here
5. Status: GENERATED after write. CANONICAL after Jake's review.

Session 002 — Phase 2 begins
Date: 2026-02-18
Target: Deck 07 — ⛽🏛 Strength Basics — 40 cards
Generation order: 🛒 Push → 🪡 Pull → 🍗 Legs → ➕ Plus → ➖ Ultra

Generated this session — Deck 07 COMPLETE (40/40):

🛒 Push (8/8):
- ⛽🏛🛒⚫±📍 Coached Press — Teaching the Bench
- ⛽🏛🛒🟢±📍 The Transfer Test — Bodyweight Strength Push
- ⛽🏛🛒🔵±🤌 Heavy Classic Presses — Structured Push
- ⛽🏛🛒🟣±🤌 Bar Path Precision — Technical Press
- ⛽🏛🛒🔴±🤌 Max Effort Push — Intense Barbell Day
- ⛽🏛🛒🟠±🤌 Push Circuit — Rotational Strength Loop
- ⛽🏛🛒🟡±📍 Press Variety — Exploration Push Day
- ⛽🏛🛒⚪±📍 Heavy Slow Press — Mindful Barbell Push

🪡 Pull (8/8):
- ⛽🏛🪡⚫±📍 Coached Pull — Read the Lift
- ⛽🏛🪡🟢±📍 Bar Strength — No Barbell Required
- ⛽🏛🪡🔵±🤌 Heavy Classic Pulls
- ⛽🏛🪡🟣±🤌 Precision Pull — Mechanics Under Load
- ⛽🏛🪡🔴±🤌 Full Send Pull — Every Muscle Accounted For
- ⛽🏛🪡🟠±🤌 Pull Circuit — Full Back, Full Loop
- ⛽🏛🪡🟡±📍 The Pull Playground — Same Pattern, New Angles
- ⛽🏛🪡⚪±📍 Slow Pull — Deliberate Heavy Descent

🍗 Legs (8/8):
- ⛽🏛🍗⚫±📍 The Squat Lesson
- ⛽🏛🍗🟢±📍 The Transfer Test
- ⛽🏛🍗🔵±🤌 Standard Leg Day
- ⛽🏛🍗🟣±🤌 Mechanics Under Load
- ⛽🏛🍗🔴±🤌 Heavy Leg Day
- ⛽🏛🍗🟠±🤌 Leg Station Loop
- ⛽🏛🍗🟡±📍 Leg Day Variations
- ⛽🏛🍗⚪±📍 Slow Leg Day

➕ Plus (8/8):
- ⛽🏛➕⚫±📍 Classic Power Mechanics
- ⛽🏛➕🟢±📍 Barless Power Standard
- ⛽🏛➕🔵±🤌 The Power Ledger
- ⛽🏛➕🟣±🤌 Clean Precision
- ⛽🏛➕🔴±🤌 Maximum Power Output
- ⛽🏛➕🟠±🤌 Power Station Loop
- ⛽🏛➕🟡±📍 Complex Play
- ⛽🏛➕⚪±📍 Weight in Space

➖ Ultra (8/8):
- ⛽🏛➖⚫±📍 The Mechanics of Hard Effort
- ⛽🏛➖🟢±📍 Outside the Gym
- ⛽🏛➖🔵±🤌 The 500m Prescription
- ⛽🏛➖🟣±🤌 Precision at Output
- ⛽🏛➖🔴±🤌 Maximum Engine
- ⛽🏛➖🟠±🤌 The Classic Engine Loop
- ⛽🏛➖🟡±📍 The Modality Shuffle
- ⛽🏛➖⚪±📍 The Breath as Anchor

Architectural Seeds — Decisions Logged 2026-02-20

## Rotation Engine & Calendar Architecture — Decided 2026-02-20

Three major architectural patterns crystallized from ideation session:

### The Default Rotation Engine (seeds/default-rotation-engine.md)
Three interlocking cycles produce a daily zip code with zero user input:
- ORDER pinned to day of week (7-day cycle, fixed, never moves)
  Monday=🐂, Tuesday=⛽, Wednesday=🦋, Thursday=🏟, Friday=🌾, Saturday=⚖, Sunday=🖼
- TYPE rolls forward from Jan 1 (5-day cycle, never resets for week)
  Jan 1=🛒, Jan 2=🪡, Jan 3=🍗, Jan 4=➕, Jan 5=➖, Jan 6=🛒...
- AXIS derives from monthly Operator's parent Axis (12 shifts/year)
- COLOR is the user's choice layer (8 options per day)

5 and 7 are coprime → same Order-Type pairing doesn't repeat for 35 days.
365 days = ~10.4 super-cycles. Year 2 starts on different combination than Year 1.

This is the clock mechanism underneath the Almanac, the daily content stream, the Workout of the Day, and the RAG recommendation layer.

### The 12-Month Operator Calendar (seeds/almanac-macro-operators.md — UPDATED)
Finalized monthly mapping with full agricultural rationale:
Jan=📍pono, Feb=🧲capio, Mar=🧸fero, Apr=👀specio, May=🥨tendo, Jun=🤌facio, Jul=🚀mitto, Aug=🦢plico, Sep=🪵teneo, Oct=🐋duco, Nov=✒️grapho, Dec=🦉logos

Annual breath: 4-month inhale (Jan-Apr) → 4-month exhale (May-Aug) → 2-month catch-breath (Sep-Oct) → 2-month close (Nov-Dec).

### Axis-as-App-Floors (seeds/axis-as-app-floors.md — NEW)
The 6 Axes serve dual function — in-workout exercise bias AND app-level content spaces:
- 🏛 Firmitas = Front page, navigation hub, system map
- 🔨 Utilitas = Tools, calculators, settings, utility
- 🌹 Venustas = Personal library, trophy case, private space
- 🪐 Gravitas = Challenge board, benchmarks, competition
- ⌛ Temporitas = Almanac, calendar, seasonal content
- 🐬 Sociatas = Community, social layer, discussion

Same workout card, six different presentations depending on which floor you're on. This is the app's primary navigation architecture.

scl-deep/axis-specifications.md updated from stub to dual-layer working draft.

None of these block Phase 2-3 card generation work.

Open Questions

- Deck priority order for workout generation — which decks get filled first?
  Candidates: Deck 07 (⛽🏛 Strength Basics) as the anchor deck,
  or start with a full color sweep across one Order.

- Canonical workout approval process — who reviews GENERATED → CANONICAL?
  Currently Jake Berry has final editorial approval on all cards.

- Exercise library versioning — when does v.0 become v.1?
  Trigger: first exercise addition or correction after generation begins.

- HTML rendering timeline — this is Phase 5 and does not block Phases 2–4.
  No decisions needed yet.

Active Decisions

File naming confirmed:
Stubs use [zip]±.md
Complete files use [zip]±[operator emoji] [Workout Title].md
Example: ⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md

Exercise library stays as one file for now.
Will be split or indexed later if needed. Not a Phase 1 or 2 concern.

Folder naming convention confirmed:
[emoji]-[slug] format throughout.
Example: ⛽-strength, 🏛-basics, 🪡-pull

CLAUDE.md is the agent instruction set.
It lives in the repo root. Claude Code reads it automatically.
It is not pasted into the chat. It is a file.

All workout exercises must come from exercise-library.md.
No invented exercises. No exceptions.

The .md files are the master source of truth.
They are never replaced. They are rendered downstream into HTML.
User data never touches the master files.

Context Notes

PPL± is a 61-emoji semantic training language (SCL) that produces
1,680 unique workout addresses called zip codes.

Each zip code is a 4-dial address: ORDER + AXIS + TYPE + COLOR.

The language is polysemic — the same emoji holds multiple valid meanings
depending on context.

The language is polymorphic — the same structural pattern produces
different outputs depending on which emojis fill the positions.

This is a year of solo ideation by Jake Berry that converged on semantic
compression as the solution to context management across AI agent sessions.

The SCL is the context control layer. Four emojis carry enough structured
meaning to prevent hallucination drift across agent sessions.

The downstream vision:
.md card → HTML workout card → user interactive session →
user history → personal exercise database

Session Log

Session 001
Date: Project start
Work: Architecture planning, all root documents drafted in planning chat
Output: CLAUDE.md, README.md, whiteboard.md, setup.py — ready to deploy
Next: scl-directory.md, exercise-library.md, then Claude Code execution

Session 003
Date: 2026-02-20
Work: Documentation sync, 7 seeds planted, HTML scaffold created, Claude Code skills installed
Output: CLAUDE.md updated to Phase 2, README.md status updated, 7 new seeds in seeds/, html/ scaffold with design-system + floors + components + assets, 5 skills in .claude/skills/
Next: Continue deck generation — next deck TBD by Jake

Notes and Fragments

Parking lot for ideas that don't have a home yet.

- Each of the 61 emojis has natural color palettes and font theming.
  The block emojis will make experience layers visually distinct in HTML.
  Design system comes in Phase 4.

- The 🚂 Junction block suggests follow-up zip codes at end of session.
  This is the seed of a recommendation and programming logic layer.
  Low priority now. High value later.

- User workout history creates a personal version of the exercise library —
  only the exercises they actually use get logged data attached.
  This is the preference and personalization engine. Phase 6 concern.

- The emojis are never required learning for users.
  They are present. They become shorthand through use.
  Pattern recognition develops naturally over time.

- Considered and set aside: moon phases, astrological elements,
  seasonal eating, Trivium and Quadrivium mapped to the 7 Orders,
  8-week program decks. All viable future layers. Not Phase 1–3 concerns.

- The day-of-week Order mapping is both the simplest possible user on-ramp
  (what day is it? here's your workout) AND the deepest automation infrastructure
  decision (temporal patterning as a first-class RAG data dimension).

- The rolling Type cycle (5-day, never resets for the week) means Monday isn't
  always Push. The coprime relationship between 5 and 7 guarantees variety
  without any programming logic beyond counting days from Jan 1.

- The 8 Colors are the depth layer on any given day. Each day has one Order-Type
  pairing with 8 Color expressions. The daily content stream is 8 deep.

- The Axes are not just exercise selectors — they are the six floors of the app.
  This is the most significant architectural insight since the zip code system itself.
  The in-workout behavior and the app-level behavior are the same principle at
  different zoom levels.

- Firmitas is always the ground floor. The elevator starts there. The 4-dial lock
  lives on Firmitas. Spinning the Axis dial takes you to a different floor.

Update this file whenever the project state changes.
The whiteboard is always the current truth of where things stand.

Session 004
Date: 2026-02-20
Work: Codex integration — built complete Codex agent infrastructure
Output: AGENTS.md (root), cards/AGENTS.md (nested), .codex/config.toml, .codex/agents/generator.toml, .codex/agents/validator.toml, .codex/agents/explorer.toml, .codex/agents/reviewer.toml
Next: Install Codex CLI (npm i -g @openai/codex), authenticate, test with exploratory session, then begin parallel deck generation

🧮
Session 005
Date: 2026-02-20
Work: Deck 07 junction-system redraw and recommendation-logic rewrite across all 40 cards
Output: Replaced all Deck 07 🚂 Junction sections with cross-layout navigation (current zip centered, 4 type-based directional suggestions with rationale) and refreshed follow-up zip routing logic to include progressive/holistic/downshift pathways across SCL context.
Next: Validate Deck 07 junction suggestions for coaching preference tuning.
