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

Update this file whenever the project state changes.
The whiteboard is always the current truth of where things stand.

🧮