# Whiteboard — PPL± Active Working Memory

This file is the project's short-term memory.
Update it at the start and end of every working session.
It is not documentation. It is a living scratchpad.

Current Phase

Phase 1 — Repository Scaffolding

Getting the house in order before anything gets built.
All root documents created and populated.
All 1,680 stub files generated and in place.
No workout content yet. That comes later.

What Is Done

- [x] Project architecture planned
- [x] CLAUDE.md drafted and complete
- [x] README.md drafted and complete
- [x] whiteboard.md drafted (this file)
- [ ] scl-directory.md populated
- [ ] exercise-library.md populated
- [ ] setup.py written and ready
- [ ] GitHub repository created
- [ ] Claude Code linked to repository
- [ ] setup.py executed — all 1,680 stubs generated
- [ ] All root files committed to GitHub

What Is Next

1. Complete scl-directory.md
2. Complete exercise-library.md
3. Hand setup.py to Claude Code — run once
4. Verify folder structure and stub count (expect 1,680 files)
5. Commit everything to GitHub
6. Begin Phase 2

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