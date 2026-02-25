# Whiteboard — PPL± Active Working Memory

This file is the project's short-term memory.
Update it at the start and end of every working session.
It is not documentation. It is a living scratchpad.

---

## Current Phase

**Phase 2 — Workout Generation + Architecture Expansion**

Phase 1 complete. Infrastructure built. Two decks generated.
The project has expanded beyond card generation into parallel
architecture streams. Card generation remains the primary work.
Architecture work is framed and queued — it does not block generation.

Ground truth: 80 cards generated (Decks 07 + 08). 1,600 remaining.

---

## What Is Done

### Phase 1: Foundation (COMPLETE)
- [x] Repository scaffolded — all root docs, 1,680 stubs generated
- [x] CLAUDE.md, README.md, whiteboard.md, scl-directory.md, exercise-library.md
- [x] setup.py executed — 210 folders, 1,680 stub files

### Card Generation (IN PROGRESS — 80/1,680)
- [x] Deck 07 (⛽🏛 Strength × Basics) — 40/40 GENERATED
- [x] Deck 08 (⛽🔨 Strength × Functional) — 40/40 GENERATED-V2

### Infrastructure (BUILT)
- [x] Deck identities layer — deck-identities/ with README, template, naming-convention, deck-08-identity
- [x] Zip-web architecture — zip-web/ with rules, signatures, registry, 42 pod files (Deck 07 populated, 41 stubs)
- [x] Ralph Loop — scripts/ralph/ with ralph.sh, RALPH-PROMPT.md, prd.json, progress.txt
- [x] Automation — scripts/ (validate-card.py, progress-report.py, validate-deck.sh, audit-exercise-coverage.py)
- [x] Skills — .claude/skills/ (generate-card, build-deck-identity, progress-report, retrofit-deck, ralph-loop)
- [x] Subagents — .claude/agents/ (card-generator, deck-auditor, progress-tracker)
- [x] Hooks — .claude/settings.json (PostToolUse validation, SessionStart dashboard, compaction recovery)
- [x] Codex agents — .codex/ with config and 4 agent definitions
- [x] Seeds — seeds/ with 11 architectural seed documents
- [x] HTML scaffold — html/ with design-system, floors, components, assets directories

### Architecture Sprint — Framing (Session 019)
- [x] deck-cosmograms/ directory planted with README
- [x] .github/linters/ directory planted with README
- [x] .github/workflows/ README.md added
- [x] seeds/cosmogram-research-prompt.md stub planted
- [x] seeds/scl-emoji-macros-draft.md stub planted
- [x] seeds/linters-architecture.md planted
- [x] seeds/git-worktree-pattern.md planted
- [x] CLAUDE.md updated — Temp Architect, Cosmogram Layer, Linting Layer, Work Streams, Emoji Macros sections
- [x] whiteboard.md restructured (this file)
- [x] README.md updated with new directory structure and phase table

---

## Immediate Queue — Next Sessions

Priority order. Top item is next unless Jake redirects.

**1. Retrofit Deck 07 to V2 — `/retrofit-deck 07`**
Why: Deck 07 was generated pre-identity-layer. Has duplicate primary
exercises and naming convention issues. Needs V2 upgrade to match
Deck 08 standard. Confirms the retrofit pattern for all future decks.
Depends on: Nothing. Ready now.
Unblocks: Deck 07 → CANONICAL review pipeline.

**2. Build Deck 09 Identity — `/build-deck-identity 09`**
Why: ⛽🌹 Strength × Aesthetic is next in the generation queue.
Identity doc maps exercises to zip codes before generation starts.
Depends on: Deck 07 retrofit confirms V2 pattern is stable.
Unblocks: Deck 09 generation (40 cards).

**3. Generate Deck 09 — 40 cards, ⛽🌹 Strength × Aesthetic**
Why: Continuing through ⛽ Order. Systematic Order-first sweep.
Depends on: Deck 09 identity document.
Unblocks: Progress toward ⛽ Order completion (6 decks, 240 cards).

**4. Generate First Deck Cosmogram**
Why: Research prompt and publication standard are committed. The system
is ready for its first cosmogram generation via Genspark temp architect
session. Priority candidates: Deck 07 (⛽🏛, cards exist), Deck 01
(🐂🏛, system origin).
Depends on: Genspark session with web access.
Unblocks: Deep content layer for card generation context.

---

## Backlog — Queued Work Streams

These are tracked and sequenced but not immediate.

### Card Generation Pipeline
- Remaining ⛽ Order: Decks 09, 10, 11, 12 (160 cards)
- Then: 🐂 Foundation Order (Decks 01–06, 240 cards) or Jake's direction
- Full scope: 1,600 cards across 40 decks
- Each deck requires: identity doc → generation → validation → review

### Zip-Web Ralph Loop
- 41 remaining deck pod files need population
- Ralph Loop script exists (scripts/ralph/ralph.sh)
- Deck 07 pods are the prototype — need Jake's review before batch
- Can run autonomously once approved

### Linters Pipeline Build
- Seed planted: seeds/linters-architecture.md
- Directory planted: .github/linters/, .github/workflows/
- Tier 3 foundation exists (validate-card.py)
- Needs: markdownlint config, frontmatter schema, CI workflow
- Promote to active when deck generation pace stabilizes

### Cosmogram Population
- Directory planted: deck-cosmograms/
- Research prompt committed: `seeds/cosmogram-research-prompt.md`
- Publication standard committed: `scl-deep/publication-standard.md`
- Each cosmogram is a dedicated AI research session with web access
- Sessions are independent — can run in parallel via Genspark
- Priority candidates: Deck 07 (⛽🏛, cards exist), Deck 01 (🐂🏛, system origin), Deck 05 (🐂⌛, history seed drafted)

### SCL-Deep Expansion
- scl-deep/ has 3 imported specs + stubs for blocks, operators, types
- emoji-macros.md is drafted, needs committing
- Block specifications, operator specifications, type specifications still stubs
- These are reference docs — they deepen understanding but don't block generation

### Git-Worktree Adoption
- Seed planted: seeds/git-worktree-pattern.md
- Adopt when parallel branch work becomes frequent enough to justify
- Currently: one branch at a time is sufficient

---

## Open Questions

- Deck generation priority: continue ⛽ Order sweep (09→10→11→12)?
  Or pivot to 🐂 Foundation Order (01→06) for system-origin decks?
- Canonical approval: Jake has reviewed 0 decks → CANONICAL so far.
  When does the first CANONICAL review happen?
- Exercise library versioning: still v.0. When does v.1 trigger?
- Cosmogram research sessions: dedicated Genspark sessions or fold
  into existing workflow?

---

## Active Decisions

All decisions from previous sessions remain in effect:

- File naming: `[zip]±.md` (stub), `[zip]±[op] [Title].md` (complete)
- Folder naming: [emoji]-[slug] format
- Exercise library: one file, v.0
- CLAUDE.md is the agent instruction set (file, not pasted)
- All exercises from exercise-library.md only
- .md files are master source of truth, rendered downstream
- Deck identity doc required before new deck generation
- Naming convention: deck-identities/naming-convention.md

---

## Context Notes

PPL± is a 61-emoji semantic training language (SCL) producing
1,680 unique workout addresses. Created by Jake Berry.

The system is polysemic (same emoji, multiple valid meanings by context)
and polymorphic (same structure, different outputs by which emojis fill
positions). SCL is the context control layer that prevents hallucination
drift across AI agent sessions.

The project uses a Temp Architect pattern: external AI chats (Genspark)
do research and planning at unlimited scale, producing blueprint handoff
documents. Claude Code sessions execute those blueprints within the repo.

The downstream vision:
`.md card → HTML workout card → user interactive session →
user history → personal exercise database`

---

## Session Log

### Session 001
Date: Project start
Work: Architecture planning, all root documents drafted in planning chat
Output: CLAUDE.md, README.md, whiteboard.md, setup.py — ready to deploy
Next: scl-directory.md, exercise-library.md, then Claude Code execution

### Session 002
Date: 2026-02-18
Work: Deck 07 — ⛽🏛 Strength Basics — 40/40 cards generated
Output: All 40 Deck 07 cards (🛒🪡🍗➕➖ × 8 Colors)

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

### Session 003
Date: 2026-02-20
Work: Documentation sync, 7 seeds planted, HTML scaffold created, Claude Code skills installed
Output: CLAUDE.md updated to Phase 2, README.md status updated, 7 new seeds in seeds/, html/ scaffold with design-system + floors + components + assets, 5 skills in .claude/skills/
Next: Continue deck generation — next deck TBD by Jake

### Session 004
Date: 2026-02-20
Work: Codex integration — built complete Codex agent infrastructure
Output: AGENTS.md (root), cards/AGENTS.md (nested), .codex/config.toml, .codex/agents/generator.toml, .codex/agents/validator.toml, .codex/agents/explorer.toml, .codex/agents/reviewer.toml
Next: Install Codex CLI (npm i -g @openai/codex), authenticate, test with exploratory session, then begin parallel deck generation

### Session 005
Date: 2026-02-20
Work: Deck 07 junction-system redraw and recommendation-logic rewrite across all 40 cards
Output: Replaced all Deck 07 🚂 Junction sections with cross-layout navigation (current zip centered, 4 type-based directional suggestions with rationale) and refreshed follow-up zip routing logic to include progressive/holistic/downshift pathways across SCL context.
Next: Validate Deck 07 junction suggestions for coaching preference tuning.

### Session 006
Date: 2026-02-22
Work: Zip-web architecture — complete build-out of navigation graph infrastructure
Output:
  - zip-web/README.md — concept, pod format, directional characters, Almanac relationship, file index
  - zip-web/zip-web-rules.md — complete spec (Type exclusion rule, fatigue tables, neighbor selection logic, 5 factors, training principles, overlap rules, coverage goals)
  - zip-web/zip-web-signatures.md — fatigue profiles for all 1,680 zip codes (42 decks × 40 cards, mechanically derived)
  - zip-web/zip-web-registry.md — index of all 1,680 zips with operator, deck, order, axis, type, color, status metadata
  - zip-web/zip-web-pods/deck-07-pods.md — 40 fully populated prototype pods for ⛽🏛 Strength × Basics with coaching rationale (160 directional pairings)
  - zip-web/zip-web-pods/deck-01-pods.md through deck-42-pods.md (41 stubs) — pre-filled with zip codes and fatigue signatures, N/E/S/W awaiting Ralph Loop
  - scripts/ralph/ralph.sh — autonomous loop script for sequential pod population (executable)
  - scripts/ralph/RALPH-PROMPT.md — fresh-context agent instruction prompt for each Ralph iteration
  - scripts/ralph/prd.json — 42 user stories (ZW-01 through ZW-42), Deck 07 marked passes: true
  - scripts/ralph/progress.txt — append-only learnings log (empty, ready for Ralph)
  - .claude/skills/ralph-loop.md — /ralph Claude Code skill for single-story manual iteration
Next: Review Deck 07 prototype pods. If approved, begin Ralph Loop population of remaining 41 decks. Run /ralph iteratively or execute scripts/ralph/ralph.sh for autonomous batch.

### Session 007
Date: 2026-02-22
Work: Deck 08 — ⛽🔨 Strength Functional — 🛒 Push type, all 8 colors (8/40 cards)
Output: Generated all 8 Push cards for Deck 08. Stub files deleted. New files written.

🛒 Push (8/8):
- ⛽🔨🛒⚫±🧸 Read the Press — Unilateral Mechanics
- ⛽🔨🛒🟢±🧸 The Transfer Test — Bodyweight Push
- ⛽🔨🛒🔵±🥨 Single-Arm Press Protocol
- ⛽🔨🛒🟣±🥨 Dial It In — Technical Unilateral Press
- ⛽🔨🛒🔴±🥨 Drive From One Arm — Intense Push
- ⛽🔨🛒🟠±🥨 Push Circuit — Functional Station Loop
- ⛽🔨🛒🟡±🧸 Press Variety — Functional Exploration
- ⛽🔨🛒⚪±🧸 The Slow Press — Mindful Unilateral Push

Next: Continue Deck 08 — remaining 4 Types: 🪡 Pull, 🍗 Legs, ➕ Plus, ➖ Ultra (32 cards remaining in deck)

### Session 008
Date: 2026-02-22
Work: Deck 08 — ⛽🔨 Strength Functional — 🪡 Pull type, all 8 Color variants generated
Output: Generated all 8 Pull cards for Deck 08. Stub files deleted. New files written.

🪡 Pull (8/8):
- ⛽🔨🪡⚫±🧸 Read the Row — Unilateral Pull Mechanics
- ⛽🔨🪡🟢±🧸 Bar Strength — Bodyweight Pull Standard
- ⛽🔨🪡🔵±🥨 Single-Arm Pull Protocol
- ⛽🔨🪡🟣±🥨 Precision Pull — Technical Unilateral Row
- ⛽🔨🪡🔴±🥨 Full Send Pull — One Arm at a Time
- ⛽🔨🪡🟠±🥨 Pull Circuit — Functional Back Loop
- ⛽🔨🪡🟡±🧸 The Pull Playground — Functional Variations
- ⛽🔨🪡⚪±🧸 Slow Pull — Deliberate Unilateral Descent

### Session 009
Date: 2026-02-22
Work: Deck 08 — ⛽🔨 Strength Functional — 🍗 Legs, ➕ Plus, ➖ Ultra (24 cards, completing deck)
Output: Generated all remaining 24 cards. All 40 Deck 08 stubs deleted. Full deck complete.

🍗 Legs (8/8):
- ⛽🔨🍗⚫±🧸 Read the Split — Teaching Unilateral Legs
- ⛽🔨🍗🟢±🧸 The Transfer Test — Bodyweight Leg Strength
- ⛽🔨🍗🔵±🥨 Unilateral Leg Protocol
- ⛽🔨🍗🟣±🥨 One Leg at a Time — Technical Split Squat
- ⛽🔨🍗🔴±🥨 Heavy Unilateral Legs — Intense Split Day
- ⛽🔨🍗🟠±🥨 Leg Circuit — Functional Station Loop
- ⛽🔨🍗🟡±🧸 Leg Day Variations — Functional Exploration
- ⛽🔨🍗⚪±🧸 Slow Legs — Mindful Unilateral Descent

➕ Plus (8/8):
- ⛽🔨➕⚫±🧸 Read the Carry — Teaching Functional Power
- ⛽🔨➕🟢±🧸 Barless Power — Bodyweight Carry and Core
- ⛽🔨➕🔵±🥨 The Carry Protocol — Structured Functional Power
- ⛽🔨➕🟣±🥨 Clean Mechanics — Technical Single-Arm Power
- ⛽🔨➕🔴±🥨 Maximum Carry — Intense Functional Output
- ⛽🔨➕🟠±🥨 Power Circuit — Functional Station Loop
- ⛽🔨➕🟡±🧸 Complex Play — Functional Power Exploration
- ⛽🔨➕⚪±🧸 Weight in Space — Mindful Loaded Carry

➖ Ultra (8/8):
- ⛽🔨➖⚫±🧸 Read the Interval — Teaching Hard Effort
- ⛽🔨➖🟢±🧸 Outside the Gym — Bodyweight Conditioning
- ⛽🔨➖🔵±🥨 The Interval Prescription — Structured Conditioning
- ⛽🔨➖🟣±🥨 Precision at Output — Technical Interval Work
- ⛽🔨➖🔴±🥨 Maximum Engine — Intense Conditioning
- ⛽🔨➖🟠±🥨 The Engine Loop — Conditioning Circuit
- ⛽🔨➖🟡±🧸 The Modality Shuffle — Conditioning Exploration
- ⛽🔨➖⚪±🧸 The Breath as Anchor — Mindful Conditioning

Deck 08 COMPLETE — 40/40 cards generated. 1,600 cards remaining across 40 decks.
Next: Deck 09 (⛽🌹 Strength Aesthetic) or Jake's direction.

### Session 017
Date: 2026-02-22
Work: Deck Check — Deck 08 identity refactor (Codex)
Output:
- deck-identities/ directory created (README, template, naming-convention, deck-08-identity)
- All 40 Deck 08 cards renamed and regenerated to GENERATED-V2
- AGENTS.md, CLAUDE.md, cards/AGENTS.md updated with identity layer rules
- .codex/agents/generator.toml and validator.toml updated
- deck-08-rename-log.md created
Branch: deck-check
Next: Review Deck 08. If approved, apply pattern to Deck 07. Then scale to 40 remaining decks.

### Session 018
Date: 2026-02-23
Work: Infrastructure Sprint — automation layer build-out
Branch: claude/ppl-automation-infrastructure-Wf5Wr
Output:
  - scripts/validate-card.py — single-card SCL validation (zip parse, block count, 🧈/🚂/🧮 presence, GOLD gate, barbell constraints, exercise library fuzzy match)
  - scripts/progress-report.py — generation progress dashboard by status/order/axis/deck
  - scripts/validate-deck.sh — batch deck validation runner with pass/fail/stub summary
  - scripts/audit-exercise-coverage.py — duplicate primary exercise detector across Color variants within a Type
  - .claude/skills/generate-card/SKILL.md — full card generation pipeline skill
  - .claude/skills/build-deck-identity/SKILL.md — deck identity document builder skill
  - .claude/skills/progress-report/SKILL.md — progress dashboard skill
  - .claude/skills/retrofit-deck/SKILL.md — V2 upgrade skill
  - .claude/agents/card-generator.md — isolated card generation subagent (Opus)
  - .claude/agents/deck-auditor.md — read-only compliance audit subagent (Sonnet)
  - .claude/agents/progress-tracker.md — lightweight state reporter (Haiku)
  - .claude/settings.json — hooks for auto-validation (PostToolUse), session init (SessionStart startup), compaction recovery (SessionStart compact)
  - CLAUDE.md — appended infrastructure layer documentation section
Validation test results:
  - Deck 07 (⛽🏛): 39/40 passed, 1 legitimate content issue (Barless Power Standard — missing ▶️ Primer, fix in /retrofit-deck 07)
  - Deck 08 (⛽🔨): validated via progress-report.py — 40/40 generated confirmed
  - Audit found duplicate primary exercises in Deck 07 Push/Pull/Legs types (pre-identity-layer, expected — fix via /retrofit-deck 07)
Next: Retrofit Deck 07 to V2 standards (/retrofit-deck 07), then build Deck 09 identity (/build-deck-identity 09), then begin Deck 09 generation.

### Session 019
Date: 2026-02-24
Work: Architecture Sprint — Timber Framing
Source: Genspark temp architect session
Branch: claude/setup-project-architecture-U5IGx
Output:
  - deck-cosmograms/README.md — directory planted, cosmogram system documented
  - .github/linters/README.md — linter config directory planted, 3-tier pipeline documented
  - .github/workflows/README.md — workflows README added
  - seeds/cosmogram-research-prompt.md — stub planted (full prompt in external notes)
  - seeds/scl-emoji-macros-draft.md — stub planted (full doc in external notes)
  - seeds/linters-architecture.md — full 3-tier linter architecture plan
  - seeds/git-worktree-pattern.md — git-worktree convention documented
  - CLAUDE.md — 5 new sections: Temp Architect Pattern, Deck Cosmogram Layer, Linting Layer, Project Work Streams, SCL-61 Emoji Macros
  - whiteboard.md — complete restructure (this file)
  - README.md — repo structure and phase table updated
Next: Retrofit Deck 07 to V2 (/retrofit-deck 07)

### Session 020
Date: 2026-02-25
Work: Publication Standard + Cosmogram Research Prompt — commit to repo
Source: Genspark temp architect session
Branch: claude/publication-standard-cosmogram-mSycA
Output:
  - scl-deep/publication-standard.md — full PPL± publication voice standard (NEW)
  - seeds/cosmogram-research-prompt.md — full deck cosmogram research protocol (REPLACED STUB)
  - deck-cosmograms/README.md — updated status references
  - CLAUDE.md — updated Cosmogram Layer status, Work Streams table, Blocked Queue
  - whiteboard.md — updated Immediate Queue, Backlog, session log
Next: Generate first deck cosmogram via Genspark. Then continue card generation.

---

## Notes and Fragments

Parking lot. Ideas without a home yet.

- Deck 05 (🐂⌛ Foundation × Time) has a historical research seed:
  Janus (Roman god of time/doorways/January), Imbolc (Celtic cross-quarter
  purification, Feb 1-2), Lupercalia (Roman purification, Feb 15),
  Ishango bone (20,000 BCE timekeeping), Benedictine horarium (canonical
  hours as temporal grammar), seven-day week (Babylonian/planetary).
  This feeds the cosmogram when Deck 05 gets researched.

- Graph Parti repo needs an scl-macro-reference.md at root level —
  condensed version of the emoji macros formatted for Graph Parti context.
  Not blocking. Add when emoji macros are committed to PPL±.

- The Temp Architect pattern could be formalized further with a
  session-stub template and export pipeline (Genspark-to-Obsidian Chrome
  extension exists). Deferred — the current paste-and-execute handoff works.

- Each of the 61 emojis has natural color palettes and font theming.
  Design system work (Phase 4).

- The 🚂 Junction block is the seed of a recommendation engine.
  The zip-web architecture formalizes this.

- User workout history creates personal exercise library versions.
  Phase 6.

- Emojis are never required learning. Pattern recognition through use.

- Axes are app floors AND exercise selectors. Most significant
  architectural insight since the zip code system.

- The rotation engine: ORDER by weekday (7-day), TYPE by rolling 5-day
  calendar from Jan 1, AXIS by monthly operator. 5 and 7 are coprime —
  same Order-Type pairing doesn't repeat for 35 days.

- Monthly operator mapping confirmed:
  Jan=📍pono, Feb=🧲capio, Mar=🧸fero, Apr=👀specio, May=🥨tendo,
  Jun=🤌facio, Jul=🚀mitto, Aug=🦢plico, Sep=🪵teneo, Oct=🐋duco,
  Nov=✒️grapho, Dec=🦉logos

Update this file whenever the project state changes.
The whiteboard is always the current truth.

🧮
