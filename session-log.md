# Session Log — PPL± Development History

This file is the archived record of all development sessions.
It is not active working memory. It is reference material.

For current tasks and project state, see `whiteboard.md` (the Negotiosum).

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
  - whiteboard.md — complete restructure
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

### Session 021
Date: 2026-02-25
Work: Deck 07 Retrofit to V2 — naming, identity, content fix, campaign architecture
Source: Session 020 branch merged to main ✅. Jake handoff with wave/campaign direction.
Branch: claude/compile-handoff-docs-lzeeO
Output:
  - deck-identities/deck-07-identity.md — V2 identity doc for ⛽🏛 Strength × Basics (40 zips mapped, primary exercise conflicts resolved, regen queue defined)
  - 25 card renames via git mv — all naming violations corrected across Push, Pull, Legs, Plus, Ultra types
  - 18 cards flagged GENERATED-V2-REGEN-NEEDED in frontmatter — duplicate primary exercises identified; content regeneration deferred to future session
  - ⛽🏛➕🟢 Barless Power Standard — missing ▶️ Primer block added (Explosive Tuck Jump + Hanging Scapular Pull)
  - seeds/deck-campaign-workflow.md — 5-lane campaign model planted (Cosmogram → Identity → Generation → Audit → CANONICAL)
  - whiteboard.md — Deck Campaign Table added, Immediate Queue updated, Session 021 logged

Deck 07 regen queue (18 cards):
  🛒: OHP (🔵), Incline Press (🔴), Push-Up Circuit (🟠), Decline Press (🟡), Floor Press (⚪)
  🪡: Bent-Over Row (🔵), Rack Pull (🟣), Sumo DL (🔴), Romanian DL (⚪)
  🍗: Front Squat (🔵), Romanian DL (🔴), Bulgarian Split Squat (🟡), Hip Thrust (⚪)
  ➕: Push Press (🔵), Dumbbell Thruster (🟡), Front Squat Slow (⚪)
  ➖: Assault Bike (🔵), Jump Rope (⚪)

Next: Build Deck 09 identity (/build-deck-identity 09), then generate Deck 09 (40 cards).

### Session 022
Date: 2026-02-25
Work: Architecture Sprint — Daily System, Elevator Model, Platform V2
Source: Genspark temp architect session
Branch: claude/add-daily-architecture-seed-z1Sqp
Output:
  - seeds/daily-architecture.md — The Daily as content type: 9 standing departments (♨️🎯🧈🧩🏖▶️🪫🚂🧮), 5 input layers (date/historical/cosmogram/forward/publication standard), automation pathway, circulation model, onboarding role
  - seeds/elevator-architecture.md — 4-dial elevator model (Order=building, Axis=floor, Type=wing, Color=room), piano nobile floor stack (🔨 ground → 🏛 noble → ⌛ 2nd → 🐬 3rd → 🌹 4th → 🪐 penthouse), dual axis function, horizontal/vertical navigation model, campus metaphor
  - seeds/platform-architecture-v2.md — Complete platform architecture refactored from Feb 11 document. Tiered business model preserved ($10/$25–30). Database schema refactored to zip-code-centric (daily_editions, zip_visits, room_threads tables added; program_sequence stores zip codes instead of workout IDs). Automation reframed as deterministic pipeline + constrained AI generation. Programs as zip code sequences. Onboarding as newspaper → room → building → navigator progression.
  - seeds/platform-architecture-v1-archive.md — Archive stub with frontmatter created. NOTE: Feb 11 "PPL± ITSELF" document body (~15,000 words) was not included in the handoff package. Frontmatter is in place; Jake needs to paste the full Feb 11 document body into this file.
  - CLAUDE.md — Work streams updated with 3 new seeds; seeds/ directory listing updated with 3 new descriptions
  - whiteboard.md — updated
Next: Continue card generation pipeline (Deck 09 identity or Deck 07 regen queue). Daily and platform seeds do not block generation.

### Session 023
Date: 2026-02-26
Work: PPL± Operis Architecture — naming, weekly cadence, 109 content types, generation pipeline
Source: Claude.ai temp architect session
Branch: claude/architecture-blueprint-handoff-k4lBH
Output:
  - seeds/operis-architecture.md — Complete Operis specification (supersedes daily-architecture.md). Weekly editorial cadence (7 Orders × Trivium/Quadrivium), 17 standing departments with activation-by-Order matrix, Operis↔Cosmogram feedback loop, construction vehicle pipeline (8–12 zips forced per edition)
  - seeds/content-types-architecture.md — 109 content types mapped to 6 Axes with cross-floor appearance rule, 12-operator engagement model, Order-as-curriculum (Trivium/Quadrivium depth levels)
  - seeds/operis-naming-rationale.md — "Operis" etymology and naming decision. Latin genitive ("of the work"), phonetic approximation "off the press," associative field (opera/opus/operate), PPL± brand name readings documented
  - seeds/daily-architecture.md — frontmatter updated: SUPERSEDED (body unchanged as historical record)
  - CLAUDE.md — updated: seeds listing (4 new lines), work streams table (Daily Architecture → PPL± Operis Build-Out)
  - whiteboard.md — updated: backlog section renamed, session log appended, naming note added
  - scl-deep/publication-standard.md — Operis content type added to tendo section
  - seeds/elevator-architecture.md — "the Daily" → "the Operis" throughout (8 replacements), frontmatter connects-to updated
  - seeds/platform-architecture-v2.md — "the Daily" → "the Operis" throughout (14 replacements), frontmatter depends-on updated
  - operis-editions/ — directory scaffold created with README.md and 2026/02/ path
Next: Generate first formal Operis edition (prototype). Then continue card generation pipeline (Deck 09 identity → Deck 09 generation).

### Session 024
Date: 2026-02-26
Work: Middle-Math Architecture — weight system, exercise engine, user context, rendering, Almanac roots
Source: Claude.ai temp architect session
Branch: claude/ppl-middle-math-architecture-RqfAa
Output:
  - middle-math/ directory created with complete 7-subdirectory structure (42 new files)
  - middle-math/ARCHITECTURE.md — 7-section system overview
  - middle-math/weights/ — octave scale spec, Order weight declarations (DRAFT), 5 category stubs, interaction rules
  - middle-math/exercise-engine/ — selection algorithm (pseudocode), family trees (DRAFT, 8 families), transfer ratios, substitution rules, template spec
  - middle-math/user-context/ — ledger spec, profile computation, toggle system, cross-context translation
  - middle-math/rotation/ — engine spec (formalized from seed), junction algorithm, fatigue model (DRAFT)
  - middle-math/rendering/ — UI weight derivation (SEED), Operis weight derivation (SEED), progressive disclosure (SEED)
  - middle-math/roots/ — Almanac math primitives: octave logic, order notation, four-layers, almanac archive pointer
  - middle-math/schemas/ — 6 database schema definitions + README
  - CLAUDE.md — MIDDLE-MATH LAYER section added, work streams table updated
  - whiteboard.md — backlog and session log updated
  - README.md — middle-math/ added to repo structure
Next: Continue card generation pipeline (Deck 09 identity → Deck 09 generation). Middle-math does not block generation.

### Session 025
Date: 2026-02-26
Work: Experience Layer Blueprint — complete architecture package for Phase 4-7
Source: Claude.ai temp architect session
Branch: claude/ppl-experience-layer-LeA4R
Output:
  - seeds/numeric-zip-system.md — 4-digit addressing: Order 1-7, Axis 1-6, Type 1-5, Color 1-8. URL /zip/2123. DB key CHAR(4).
  - seeds/experience-layer-blueprint.md — Master tech architecture. Next.js 14 + Supabase + Stripe + Tailwind + Zustand + Framer Motion. Routing, rendering pipeline, weight→CSS.
  - seeds/data-ethics-architecture.md — No tracking, no analytics SDKs, no third-party cookies. Full export. Full deletion. RLS as ethical infrastructure. Architecture IS the ethics.
  - seeds/mobile-ui-architecture.md — 4 interaction states (Immersed → Dial Active → Drawer Open → Full Tool Floor). Price-is-Right dial metaphor. 🔨 tool drawer. Pinch-zoom canvas.
  - seeds/stripe-integration-pipeline.md — Tier 1 Library Card $10/mo. Tier 2 Residency $25-30/mo. Checkout, webhooks, portal, RLS gating.
  - seeds/claude-code-build-sequence.md — 15 launch sessions (A through N + C-2 voice parser) + 5 post-launch (V-Z automotive). Each scoped and testable.
  - seeds/automotive-layer-architecture.md — Car as sixth screen. Operis read aloud. Voice zip navigation. Playlist mood system (56 Order×Color profiles). Free-tier audio funnel. TTS pipeline. Android Auto + CarPlay. Build sessions V-Z.
  - seeds/voice-parser-architecture.md — Universal building navigation. Not just workouts — handles exercise info, personal progress, community, almanac, education, playlists, multi-intent. 3-layer scoring (zip + floor + content type). ~13,000 keyword entries. No AI model. Runs client-side in milliseconds.
  - seeds/wilson-voice-identity.md — Wilson: PPL± voice identity. Not a chatbot. Voice of the building. TTS from publication standard. SSML formatting. Register shifts by floor. Response patterns for all content types.
  - seeds/regional-filter-architecture.md — Opt-in manual region (no GPS, no tracking). Seasonal content, almanac, Operis framing tuned to geography. ~540 authored sentences for 15 sub-regions × 12 months. Include in Tier 1.
  - middle-math/schemas/zip-metadata-schema.md — CHAR(4) numeric primary key. Population script (1,680 rows via cross-join). Indexed dial positions. All tables reference via CHAR(4) foreign keys.
  - CLAUDE.md — Numeric zip notation, experience layer references, data ethics position
  - whiteboard.md — session log, queue update, backlog
  - README.md — Phase table update, repo structure
  - seeds/README.md — 10 new seeds registered
  - html/README.md — Updated with numeric routing, expanded components, voice parser, car layer
  - middle-math/ARCHITECTURE.md — Section 8: Numeric Zip Layer
  - middle-math/schemas/README.md — zip-metadata-schema.md registered

Key decisions:
  - Numeric zip: every emoji = a dial position number. ⛽🏛🪡🔵 = 2123. URLs, DB keys, weight indices all numeric. Emoji is display only.
  - Data ethics: no tracking, no analytics, full export, full deletion. Architecture IS the ethics. Not a party statement.
  - Mobile UI: 4 states, Price-is-Right dials, 🔨 drawer, pinch-zoom canvas. Phone-first.
  - Voice parser: universal building navigation. Any speech → zip + floor + content type. No AI model. 13k keywords. Client-side milliseconds.
  - Wilson: the voice of the building. Not a chatbot. Publication standard as TTS. Floor-specific register.
  - Car layer: free-tier Operis audio, voice navigation, playlists. Conversion through familiarity.
  - Regional filter: user picks region manually. No GPS. Seasonal + almanac content adjusts.
  - Stripe: 2 products, RLS enforces tiers, Customer Portal for self-service.
  - Build sequence: 20 sessions total. 15 to launch, 5 post-launch for car/audio.
  - Free tier evolves: Operis web + Operis audio + zip previews + playlists + almanac (car). Tier 1 = interactive rooms. Tier 2 = coaching.

Next: Execute Session A (Claude Code) — Next.js skeleton + zip routing. Or continue Deck 09 identity → generation. Experience layer does not block card generation.

### Session 026
Date: 2026-02-27
Work: scl-deep System Doc Population — order, block, emoji macro deep references
Branch: claude/system-doc-population-KkS48
Output:
  - scl-deep/order-specifications.md — Deep spec for all 7 Orders. Full character descriptions, what each Order is NOT, block sequences with rationale, exercise selection filters, Order×Axis and Order×Color interaction matrices, common generation errors, progressive overload structures, absolute ceiling reference table, block exclusion matrix, difficulty scale
  - scl-deep/block-specifications.md — Deep spec for all 22 blocks + SAVE. Each block: role, always-present status, content rules (what goes in / never goes in), context-dependence matrix (how content shifts by Order × Color), set/rep patterns, activation conditions
  - scl-deep/emoji-macros.md — Cultural, historical, symbolic macro meanings for all 61 SCL emojis. Covers all 7 categories. Each entry: cultural macro, cross-domain resonance, SCL resonance. Tier 0 reference for cosmogram research and design system.
Note: Agents timed out on these tasks (3×); all 3 files written directly.
Next: Card generation pipeline — Deck 09 identity → Deck 09 generation.

### Session 027
Date: 2026-03-01
Work: PR #25 Integration + Reverse-Weight Architecture + Operis V3 Prompt Infrastructure
Source: Claude.ai temp architect session (February 27–28, 2026)
Branch: claude/integrate-pr25-reverse-weight-engYD
Output:
  - middle-math/rotation/reverse-weight-resolution.md — Temporal zip-code resolution algorithm. Yesterday→today→tomorrow triangulation. Three phases: read yesterday's fatigue signature, derive tomorrow's stimulus requirements, compute today's adjusted zip. Operis editorial implication: featured Sandbox room = resolution room.
  - scl-deep/vocabulary-standard.md — Language standard. Banned/approved word lists (optimize, unlock, level up, crush it, etc. with replacements). Preferred operator verb set. Factual register standard — all claims traceable to exercise science. Tonal prohibitions. Newspaper test. Application scope.
  - seeds/operis-architecture.md — Four new sections added after "Five Input Layers": Temporal Context (reverse-weight editorial application), Front Page Card (masthead-left/almanac-right broadsheet layout spec), Depth Standard (2,500–4,500 words, newspaper test, 30–40% Historical Desk), Age-Neutral Register (literate teenager + retired architect, no dopamine design, no generational signaling).
  - scl-deep/publication-standard.md — Almanac Aesthetic section added after Three Historical Registers: French Catholic almanac (feast days, agricultural rhythms, civic pulse as factual theater) + American civic almanac (Poor Richard's, Old Farmer's). Vocabulary standard cross-reference.
  - CLAUDE.md — scl-deep/ directory listing updated (vocabulary-standard.md added). SCL-Deep Expansion section added (vocabulary-standard + reverse-weight-resolution references).
  - README.md — scl-deep/ listing updated to note vocabulary-standard.md. middle-math/ listing updated to note rotation/ includes reverse-weight resolution.
  - whiteboard.md — updated; Immediate Queue and Backlog updated.
Architecture verified post-PR-25 merge (10 commits from Session 026 confirmed present).
Operis V3 prompt delivered — front page card, almanac-right layout, age-neutral register, no polarity language on reader-facing surfaces.
Next: Test Operis V3 Prompt in temp architect session with full prompt. Then continue Deck 09 identity → Deck 09 generation.

### Session 028
Date: 2026-03-03
Work: Operis Infrastructure Patch — pipeline architecture, educational layer, Color posture, Sandbox structure, filing system
Source: Genspark temp architect session (March 3, 2026)
Branch: claude/operis-infrastructure-patch-jvIQA
Output:
  - seeds/operis-prompt-pipeline.md — 4-prompt pipeline spec with handoff contracts, Color flow (3 identities), department activation matrix, rotation engine V1.0 reference, automation pathway (NEW)
  - seeds/operis-educational-layer.md — 8-lane educational content architecture unified with Color Context Vernacular tonal registers, seasonal content logic, SCL emoji content lattice (NEW)
  - seeds/operis-color-posture.md — Color of the Day as cognitive posture: 8 postures, determination inputs, prose tinting guidelines, automation scoring pathway (NEW)
  - seeds/operis-sandbox-structure.md — 13-room Sandbox: 8 deterministic Color siblings + 5 Content Rooms from editorial content, content-to-zip mapping chain, ExRx naming convention, generation implications (NEW)
  - operis-editions/historical-events/README.md — historical events database directory planted, 366-file spec, quality standards (NEW)
  - seeds/operis-architecture.md — 4 sections appended: pipeline reference, Layer 6 educational content, Color of the Day, 13-room Sandbox. Open questions updated. (UPDATED)
  - middle-math/rendering/operis-weight-derivation.md — Color of the Day scoring mechanism architecture: 7 input signals, resolution algorithm, confidence levels (UPDATED)
  - scl-deep/publication-standard.md — Color as Cognitive Posture Operis extension section added after Color Context Vernacular (UPDATED)
  - CLAUDE.md — seeds listing updated (4 new), operis-editions/ structure added, Operis Build-Out backlog section added, work streams table updated (UPDATED)
  - whiteboard.md — this session logged, Immediate Queue updated, Operis Build-Out backlog updated (UPDATED)
  - README.md — directory structure updated if needed (UPDATED)
Architecture notes:
  - 13-room Sandbox replaces variable 8–12 room selection. 8 Color siblings are deterministic. 5 Content Rooms are editorial.
  - Content Rooms translate Operis editorial content into physical practice (embodied cognitive learning). Content-to-zip mapping is the editor's craft.
  - Content Room titles follow ExRx naming convention — no editorial/narrative titles. Editorial connection lives in Operis prose, not card titles.
  - Color of the Day has three distinct identities documented: workout Color, publication Color, Operis cognitive posture.
  - Educational content lanes unified with Color Context Vernacular — each lane inherits its Color's tonal register.
  - Pipeline handoff contracts formalized: research brief, enriched content brief, Operis edition. Each is a defined markdown structure.
Next: Superseded by Sessions 029–030 and post-030 follow-up commits. Remaining work is Contract A/B URL enforcement + same-date re-test before returning to Deck 09.

### Session 029
Date: 2026-03-03
Work: Operis V4 Prompt Architecture — four generation prompts stored as seeds, pipeline aligned
Source: Claude.ai temp architect session (March 3, 2026)
Branch: claude/operis-v4-prompts-aIxIr
Output:
  - seeds/operis-researcher-prompt.md — Prompt 1: Researcher. Takes date → Research Brief (Contract A). Role definition, 5 research beats, historical events DB check, output format, V4.0 (NEW)
  - seeds/operis-content-architect-prompt.md — Prompt 2: Content Architect. Takes Research Brief → Enriched Content Brief (Contract B). Color of the Day determination (7 inputs), 8-lane assessment, Word of the Day, Content Room candidates, V4.0 (NEW)
  - seeds/operis-editor-prompt.md — Prompt 3: Editor. Takes both briefs → Operis Edition (Contract C). 8 Color siblings, 5 Content Rooms, Standing Departments, YAML front-matter spec, V4.0 (NEW)
  - seeds/operis-builder-prompt.md — Prompt 4: Builder. Takes edition → committed files. Proofing checklist (8 items), card generation procedure, repo commit, V4.0 (NEW)
  - seeds/operis-prompt-pipeline.md — Section header renamed to "Rotation Engine V1.0", Department Activation Matrix expanded to 17 departments (aligned with architecture), Prompt File Reference table added, Contract C updated with 13-room total, Automation Pathway references prompt seed paths, connects-to updated (UPDATED)
  - seeds/operis-sandbox-structure.md — Content Room Constraint Summary, Content-to-Zip Mapping Chain, and Naming Convention sections added. depends-on updated to include deck-identities/naming-convention.md (UPDATED)
  - seeds/operis-architecture.md — Generation Pipeline section updated with prompt file paths and 13-room confirmation, Standing Departments table aligned to 17 pipeline-matching department names, Rotation Engine V1.0 version note added, connects-to updated (UPDATED)
  - CLAUDE.md — 4 new prompt seed entries added to seeds/ listing, Operis Build-Out backlog updated (UPDATED)
  - whiteboard.md — Session 029 logged, Immediate Queue updated (UPDATED)
Next: Close remaining Contract A/B enforcement gaps (P1 URL+sky fields, P2 per-lane URLs), then re-run P1→P2→P3→P4 on 2024-07-26. After contract pass, continue Deck 09 identity → generation.

### Session 030
Date: 2026-03-04
Work: Operis V4 Pipeline Test — full date test (2024-07-26)
Status: PARTIAL PASS / CONTRACT FAIL

Passes:
- Color posture coherence (🔵 Structured) held across P2→P3.
- 13-room Sandbox mapping fidelity passed (8 siblings + 5 content rooms; Order lock + unique Type/Axis constraints satisfied).
- Department activation matrix behavior passed for Friday (🌾) active departments.

Failures:
- Contract A missing explicit source URLs per historical event and exact sky time fields.
- Contract B missing explicit source URLs per content lane.
- Contract C frontmatter key mismatch (`rooms` used instead of `sandbox-zips`) and missing `sandbox-total: 13`.

Artifacts:
- `operis-editions/test-results/2024-07-26/contract-a-research-brief.md`
- `operis-editions/test-results/2024-07-26/contract-b-content-brief.md`
- `operis-editions/test-results/2024-07-26/contract-c-operis-edition.md`
- `operis-editions/test-results/2024-07-26/pipeline-validation-report.md`

Completed since Session 030:
- ✅ Contract C frontmatter schema preflight (`sandbox-zips`, `sandbox-total`) and parser hardening landed (team refs: `8d730f9`; parser commit: `c024c37`).
- ✅ status allow-list alignment between schema + inventory docs/scripts landed (team refs: `b47b269`; alignment commit: `8f48ad5`).
- ✅ full-audit strict/baseline success-message clarification landed (`5369fff`).
- ✅ tree-notation validation hardening landed (`53f85f3`, `0fbf244`) and integrated with Contract C parsing (`c024c37`).

Open follow-ups:
1) Add strict URL + sky-field enforcement to P1 template/checklist (Contract A gap still open).
2) Add per-lane URL enforcement to P2 template/checklist (Contract B gap still open).
3) Re-run same date test after URL/schema patching.

### Session 031
Date: 2026-03-04
Work: Codex next-round handoff planner authored for container/job continuity
Branch: current active branch
Output:
  - .codex/NEXT-ROUND-HANDOFF.md — copy/paste brief capturing assumed-merged fixes, next task pack (A–D), definition of done, and kickoff prompt for next Codex run.
Notes:
  - Purpose is session-to-session continuity: prevent reopening closed loops and shift focus to container completion ledger + handoff closure evidence.
Next:
  - Execute Task A/B/C from `.codex/NEXT-ROUND-HANDOFF.md` in next active session.

### Session 032
Date: 2026-03-05
Work: Planted systems-eudaimonics seed and wired design-constraint references
Branch: current active branch
Output:
  - seeds/systems-eudaimonics.md — new economic philosophy seed (Eudaimonic alignment, EHI metric, longevity constraints, phase cost constraints, architecture mappings, open questions)
  - CLAUDE.md — DATA ETHICS POSITION section updated to reference systems-eudaimonics alongside data-ethics architecture
  - whiteboard.md — this session log entry
Notes:
  - Treated as constraint-layer architecture (no deliverable artifacts), aligned with requested Codex task instructions.
Next:
  - Use `seeds/systems-eudaimonics.md` as a required read when implementing Stripe/tier gates, bloom/vote/superscript context systems, notification UX, and Operis economics decisions.

### Session 033
Date: 2026-03-05
Work: CX-08 SQL schema materialization
Branch: current active branch
Output:
  - sql/001-create-exercise-library.sql
  - sql/002-create-exercise-families.sql
  - sql/003-create-user-ledger.sql
  - sql/004-create-user-profile.sql
  - sql/005-create-user-toggles.sql
  - sql/006-create-zip-metadata.sql
  - sql/007-populate-zip-metadata.sql
  - sql/README.md
Notes:
  - Materialized schema docs from middle-math/schemas into PostgreSQL 15+ migration files.
  - Included RLS policies with auth.uid(), triggers/functions, indexes, and zip_to_emoji().
  - Zip population script uses cross-join generate_series(1..7,1..6,1..5,1..8) for 1,680 rows.
Next:
  - Apply in Supabase in numeric order and validate against a live Postgres instance.

---

### Reconciliation Note — Unlogged Codex Work (2026-03-04 through 2026-03-05)

The following work was executed across multiple Codex runs and Claude Code sessions
between Sessions 030 and 033. None of these runs were assigned session numbers at
the time. This reconciliation note serves as the historical record.

**Deck 09 Generation (⛽🌹 Strength Aesthetic — 40/40 cards)**
Executed across multiple Codex PRs culminating in PR #59 (be1d53c).
No session numbers assigned. All 40 cards generated, stubs deleted, deck complete.
Deck 09 identity document built during this period.

**CX Container Execution Burst (PRs #58–#67)**
The following containers were executed and merged:
  - CX-03: Zip converter + registry (PR #58, 83868b9)
  - CX-04: Inventory + progress truth tables (PR #60, 87b2fd8)
  - CX-13: Exercise library parser → JSON (PR #61, db7b202)
  - CX-02: Historical events scaffold + 366 stubs (PR #62, 99fc9ac)
  - CX-00B: Systems language audit (PR #63, c3f6ec7)
  - CX-09: Axis weight declarations, all 6 axes (PR #64, 41cc4fa)
  - CX-10: Type + color weight declarations (PR #65, e6be726)
  - CX-16: Deck identity scaffold generator, Decks 10–12 (PR #67, 862de8d)

**Additional infrastructure (CX-05, CX-07)**
Markdownlint configuration and CI lint workflow landed via Codex runs.
Exact PRs not individually tracked. Evidence on disk:
  - .github/linters/.markdownlint-cli2.jsonc
  - .github/workflows/lint.yml
  - .github/workflows/pylint.yml

**First Operis Edition (PR #27, 34c8f41)**
2026-03-02 Operis — first-ever edition. Foundation Functional Push.
Filed at operis-editions/2026/03/2026-03-02.md.

**Architecture Seeds**
  - seeds/color-pipeline-posture.md (PR #83, 0622878)
  - seeds/systems-eudaimonics.md (Session 032 area)
  - seeds/scl-envelope-architecture.md (unlogged)

**Code Review / Validation Hardening**
Contract C parser hardening, tree-notation validation, status allow-list alignment,
full-audit strict/baseline messaging — all landed via Codex PRs in the #50s–#60s range.
Referenced in .codex/NEXT-ROUND-HANDOFF.md as "assumed done and merged."

---

## Session 034 — 2026-03-06 · Critical Path Reconciliation

**Branch:** `claude/critical-path-reconciliation-K7jeB`

**Work summary:** Reconciliation + 3 critical path containers completed.

**Reconciliation (Phase 1):**
- CX-33 (Progress Dashboard) registered as DONE — was built in PR #90 (2026-03-05) but never marked in tracking docs
- CLAUDE.md card count corrected: 80/1,680 → 102/1,680 (Deck 07: 22/40, Deck 08: 40/40, Deck 09: 40/40)
- docs/cx-dependency-graph.md summary updated from 16/36 → 19/36 (pre-advance)

**CX-14 — Weight Vector Computation Engine:**
- `scripts/middle-math/weight_vector.py` — 61-dimensional weight vector derivation engine
- `middle-math/weight-vectors.json` — 1,680 entries, all zip codes, all valid (--validate passes)
- Octave scale [-8, +8], interaction resolution ORDER > COLOR > AXIS > TYPE
- Hard suppression rules enforced: 🌋 Gutter blocked in 🖼/🐂/⚪ contexts

**CX-21 — Content Type Registry:**
- `middle-math/content-type-registry.json` — 109 types across 6 axes
- Per entry: id, name, axis, axis_name, primary_floor, cross_floor_appearances, instance_count, order_depth_level, operator_engagement, description
- Distribution: 🏛=19, 🔨=30, 🌹=20, 🪐=15, ⌛=13, 🐬=12

**CX-28 — Cosmogram Content Scaffold:**
- `scripts/scaffold_cosmograms.py` — generates 42 stub files
- `deck-cosmograms/deck-01-cosmogram.md` through `deck-cosmograms/deck-42-cosmogram.md` — all 42 decks stubbed
- Each stub has full frontmatter (status: STUB, research_required: true) + 13 body sections

**Cascade unlock (Wave 4):**
- CX-15 (Exercise Selection Prototype) — CX-13 ✓, CX-14 ✓ — fully unblocked, critical path next
- CX-22 (Floor Routing Spec) — CX-03 ✓, CX-20 ✓, CX-21 ✓ — fully unblocked
- CX-25 (Vote Weight Integration) — CX-20 ✓, CX-14 ✓ — fully unblocked
- CX-30 (Envelope Schema) — CX-08 ✓, CX-14 ✓, CX-03 ✓ — fully unblocked

**Final state:** 21/36 CX containers complete. 4 containers advanced this session.

---

## Session 035 — Wave 4 Sprint — 2026-03-06

**Branch:** `claude/wave-4-sprint-035-vN8CK`
**Duration:** 1-hour sprint window
**Phase:** 2 — Architecture expansion + engine sweep

**Completed:**
- CX-15 DONE — `scripts/middle-math/exercise_selector.py` — ranked exercise candidates per block for all 1,680 zips. GOLD gate enforced, load ceiling by Order, equipment tier by Color, Type match, cross-block deduplication. `--validate` passes on deck 07 (40 zips, 0 coverage gaps). `--deck`, `--stats`, `--output` flags.
- CX-22 DONE — `middle-math/floor-routing-spec.md` — 109 content types routed to 6 Axis floors. Default landing URLs, access gates, adjacency rules, agent-internal content documented.
- CX-24 DONE — `scripts/middle-math/bloom_engine.py` — 6-level bloom state engine. No streaks, no decay, eudaimonic constraint (bloom never decreases). `--demo` (10-zip table), `--schema` (SQL), `--compute` (single calculation).
- CX-26 DONE — `scripts/middle-math/generate_room_manifest.py` — 13-room Operis Sandbox generator. Derives Order (weekday), Type (5-day rolling), Axis (monthly). 8 Color siblings + 5 Content Room placeholders. `--date` and `--week` flags.
- CX-27 DONE — `scripts/middle-math/compute_superscript.py` — superscript (system suggestions via cosine similarity on weight vectors) + subscript (user overrides: no_barbell, no_machines, injury flags, bookmarks). `--demo` (5-zip table), `--schema` (SQL ALTER TABLE).

**Tracking updated:** `.codex/TASK-ARCHITECTURE.md`, `whiteboard.md`, `docs/cx-dependency-graph.md`

**Cascade unblocked:** CX-22 → CX-29 (Wilson Audio Route Scaffold) now unblocked.

**Final state:** 26/36 CX containers complete. 5 containers completed this session.

---

🧮

### Session 036
Date: 2026-03-06
Branch: claude/envelope-pipeline-036-OsXgl
Work: Envelope pipeline close — CX-25 Vote Weight Integration, CX-30 Envelope Stamper, CX-29 Wilson Audio Spec

**CX-25 — Vote Weight Integration:**
- `scripts/middle-math/vote_weight_adjuster.py`
- Algorithm: tanh(raw_signal / vote_count) → normalized signal in (-1, 1)
- Uniform adjustment across all 61 dimensions, capped at ±0.8 per dimension
- Eudaimonic constraint enforced: votes are signal, not governance
- --validate passes 6,720 checks (1,680 zips × 4 vote configurations)
- --demo shows base vs adjusted comparison for 5 representative zips

**CX-30 — Envelope Stamper:**
- `scripts/middle-math/envelope_stamper.py`
- Atomic retrieval unit: zip identity + base weight vector + vote-adjusted vector + bloom + superscript/subscript
- --anonymous mode: base identity + weight vector only (free-tier envelope)
- --full mode: mock user context demonstrating complete envelope shape
- --deck mode: stamps all 40 envelopes in a deck
- Integrates vote_weight_adjuster, bloom_engine, compute_superscript by import

**CX-29 — Wilson Audio Route Scaffold:**
- `middle-math/wilson-audio-spec.md`
- 3-layer keyword scoring architecture: Layer 1 (~1,160 keywords), Layer 2 (~300 keywords), Layer 3 (~800 keywords)
- ~2,260 total keyword entries, no AI dependency, client-side O(1) lookup
- Wilson voice register by floor: Piano Nobile (technical), Ground Floor (utility), 2nd Floor (temporal), 3rd Floor (social), 4th Floor (personal), 5th Floor (research)

**Tracking updated:** `.codex/TASK-ARCHITECTURE.md`, `whiteboard.md`, `docs/cx-dependency-graph.md`

**Cascade unblocked:** CX-31 (Envelope Similarity & Retrieval) now FULLY UNBLOCKED — both blockers met (CX-30 ✓, CX-21 ✓). Wave 5 capstone is next.

**Final state:** 29/36 CX containers complete. 3 containers completed this session. 7 open: CX-01, CX-17, CX-18, CX-19, CX-31 (+ 2 non-CX audit tasks).

---

## Session 037 — Architecture Capstone (2026-03-06)

**Branch:** `claude/architecture-capstone-037-b7rHF`
**Scope:** Wave 5 close (CX-31) + governance pair (CX-01 → CX-19) + design tokens (CX-18) + audit snapshots

---

**CX-31 — Envelope Similarity & Retrieval Engine (Wave 5 Capstone):**
- `scripts/middle-math/envelope_retrieval.py`
- Cosine similarity engine across 1,680 × 61-dimensional weight vectors
- `compute_similarity(vector_a, vector_b, weights=None) → float [-1, 1]`
- `retrieve_top_n(query_vector, candidates, n, tier) → ranked list`
- `build_query_vector(zip_code, user_context=None) → 61-float list` (composes base + votes + bloom)
- `retrieve_for_operis(date_str, n=13) → manifest` (rotation engine → Tier 1 retrieval)
- 4 content-type retrieval profiles: Tier 1 (Order/seasonal ×2), Tier 2 (Type/Axis ×1.5), Tier 3 (exercise family ×2), Tier 4 (equal weight, threshold 0.9)
- CLI flags: --query, --deck, --operis, --validate, --stats
- `--validate` passes 5/5 checks (bounded, no NaN, symmetric, self-sim=1.0, top-1 is self)
- Architecture complete: every room lookup, Operis sandbox selection, and content retrieval resolves through this function

**CX-01 — Codex Agent Configuration & Task Architecture:**
- `.codex/TASK-ARCHITECTURE.md` governance finalized
- Replaced stale Wave 2/3 readiness tables with current-state table (3 remaining containers)
- Added Container Completion Summary (all 36 containers, sorted by wave, with completion dates)
- CX-01 marked DONE

**CX-19 — Agent Boundaries Document:**
- `.claude/AGENT-BOUNDARIES.md` created
- 5-agent roster: Claude Code, Codex, card-generator (Opus 4.6), deck-auditor (Sonnet 4.6), progress-tracker (Haiku 4.5)
- Per-agent read/write/never-touch matrix (10 file categories)
- Escalation rules for all 5 agents
- Jake-reserved zones: scl-directory.md, exercise-library.md, CANONICAL status, billing/keys, pod review, operator overrides, SCL expansion

**CX-18 — Design Tokens & WeightCSS Spec:**
- `middle-math/design-tokens.json` — 8 Color palettes (6 properties each), 7 Order typographic scales, spacing/radius/animation/shadow/typography tokens
- `middle-math/weight-css-spec.md` — 61-dim weight vector → CSS custom properties (`--ppl-weight-*`), octave scale normalization formula, dimension index map, TypeScript generation function, fallback values

**Block 5 — Audit Snapshots:**
- `reports/` directory created
- `reports/README.md` — regeneration instructions
- `reports/deck-readiness-2026-03-06.md` — deck generation readiness matrix (42 decks)
- `reports/exercise-usage-2026-03-06.md` — exercise coverage across 102 generated cards

**Scripts run:**
- `python scripts/build-dashboard-data.py` — dashboard data refreshed
- `python scripts/validate-negotiosum.py` — whiteboard consistency check

**Tracking updated:** `whiteboard.md`, `.codex/TASK-ARCHITECTURE.md`, `docs/cx-dependency-graph.md`

**Final state:** 33/36 CX containers complete. 4 containers completed this session. CX-17 (Ralph loop) is the only remaining CX container — blocked on Jake pod review. The CX architecture campaign is functionally complete. Project pivots from architecture to content generation.

---


## Session 038 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Exercise Library Expansion (Wave 6)
**Containers completed:** CX-36, CX-37, CX-38, CX-39, CX-40 (5/5 Wave 6)
**CX totals:** 38/44 complete

---

**Phase 0 — Registration:**
- `.codex/TASK-ARCHITECTURE.md` — 8 new CX rows (CX-36–43), Wave 6/7 in Wave Execution Plan, context firewall updated (`exercise-content/` added to MAY Read and MAY Write)
- `whiteboard.md` — header updated "44 defined, 33 complete, 11 open", 8 new task rows across Ordo/Natura/Architectura/Profundum/Fervor sections
- `docs/cx-dependency-graph.md` — Wave 6/7 subgraphs added, dependency edges wired

**CX-36 — Exercise Identity Registry:**
- `scripts/build-exercise-registry.py` — Full Python build script: 16-pattern vocabulary standardization, anatomy inference by pattern + section override, FAMILY_MEMBERS lookup for 8 major families, axis/order affinity scoring (octave scale -8/+8), equipment list inference, knowledge_file path generation, two-pass global ID assignment (EX-0001–EX-2085), CLI `--stats`/`--validate`/`--dry-run`
- `middle-math/exercise-registry.json` — 2,085 entries generated, all exercises with globally unique IDs, anatomy, family linkage, affinity scores

**CX-39 — External Reference Dock:**
- `middle-math/exercise-engine/external-refs.json` — 2,085 null dock entries keyed by EX-ID
- `seeds/exrx-partnership-brief.md` — One-page SEED partnership pitch: integration architecture, traffic flow model, Options A/B/C, technical readiness table

**CX-40 — Exercise Registry SQL Migration:**
- `sql/009-exercise-registry.sql` — Full `exercise_registry` table: TEXT PK, self-referencing parent_id FK, 8 indexes (GIN on scl_types/primary_movers/name_trgm, B-tree on pattern/family/parent), RLS public SELECT, auto-update trigger
- `sql/010-exercise-knowledge.sql` — `exercise_knowledge` table: 1:1 FK to registry, JSONB faults/context/modifiers, status lifecycle EMPTY→CANONICAL, auto-populate stub rows from registry
- `sql/README.md` — Execution order, file mapping, notes, psql commands, row count verification updated for migrations 9 and 10

**CX-38 — Exercise Relationship Graph:**
- `middle-math/exercise-engine/family-trees.json` — 15 families (all movement patterns), 2,085 member entries, root/variant/progression/regression/equipment-swap/unlinked roles
- `middle-math/exercise-engine/substitution-map.json` — 2,085 entries, same_family/tier_down/tier_up/cross_family substitution chains
- `middle-math/exercise-engine/sport-tags.json` — 20 sports indexed, by_sport inverted index + by_exercise per-ID map
- `middle-math/exercise-engine/anatomy-index.json` — 50 muscles + 30 joint actions, primary/secondary/stabilizer inverted index

**CX-37 — Exercise Knowledge Template + First Batch:**
- `scripts/generate-exercise-content.py` — Full CLI generator: pattern-based templates for all 16 patterns (setup/execution/faults/PPL±Context/ColorModifiers/CoachingNotes), `resolve_template_pattern()` for family_id fallback when movement_pattern is catch-all, `--exercise/--section/--type/--batch/--priority-first/--overwrite/--dry-run/--stats` CLI
- `exercise-content/README.md` — Subdirectory structure, file naming, status lifecycle, generation commands, population progress
- `exercise-content/push/`, `pull/`, `legs/`, `plus/`, `ultra/` — Directories created
- 197 knowledge files generated (200 attempted, 3 duplicate slugs collapsed), avg 484 words/file, priority-first ordering (25 high-frequency exercises from usage report first)

**Known data issue logged:**
- `movement_pattern` catch-all: ~1,256 exercises classified as `core-stability` due to PATTERN_KEYWORDS `"car"` substring matching `"carry"` and other collision cases. Generator mitigates via `resolve_template_pattern()` (uses `family_id` for hip-hinge/squat/etc. exercises). Full fix deferred to CX-43 (Selector V2).

**Scripts run:**
- `python scripts/build-exercise-registry.py --validate` — 0 errors
- `python scripts/build-exercise-registry.py --stats` — 2,085 entries confirmed
- `python scripts/generate-exercise-content.py --stats` — 197 files, 9.4% coverage
- `python /tmp/build_cx38.py` — 4 CX-38 files generated

**Final state:** Wave 6 complete (5/5). Wave 7 (CX-41, CX-42, CX-43) fully unblocked. 38/44 CX containers complete. Next session: CX-41 (batch 201–500) or CX-43 (Selector V2). Jake's call on deck generation vs. library expansion priority.

---

## Session 039 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Deck 10 Card Generation
**Deck completed:** Deck 10 — ⛽🪐 Strength × Challenge (40/40)

---

**Work completed:**
- Generated all 40 card files in `cards/⛽-strength/🪐-challenge/` across all 5 Types × 8 Colors.
- Converted all stubs from `status: EMPTY` to `status: GENERATED`.
- Renamed all files from stub format (`[zip]±.md`) to complete semantic format (`[zip]±[operator] [Title].md`).
- Applied operator polarity for 🪐 Challenge correctly:
  - Preparatory colors (⚫🟢🟡⚪) → `🪵 teneo`
  - Expressive colors (🔵🟣🔴🟠) → `🚀 mitto`
- Ensured no duplicate primary exercise across Color variants within each Type.
- Updated `whiteboard.md` progress:
  - Cards: 102 → 142 / 1,680
  - Deck 10 row marked DONE (40/40)

**Validation run:**
- `for f in cards/⛽-strength/🪐-challenge/*/*.md; do python scripts/validate-card.py "$f"; done`
- `bash scripts/validate-deck.sh cards/⛽-strength/🪐-challenge`
- `python scripts/audit-exercise-coverage.py cards/⛽-strength/🪐-challenge`

**Validation outcomes:**
- 40/40 cards passed `validate-card.py`
- Deck validator summary: `40 passed, 0 failed, 0 stubs skipped`
- Exercise coverage audit: no duplicate primary exercises across any Type

**Final state:**
- Deck 10 fully generated and validated.
- Global card count now 142/1,680.

---

## Session 041 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Exercise Library Expansion (Wave 7)
**Container completed:** CX-43 — Exercise Selector V2 (registry-aware)
**CX totals:** 40/44 complete

---

**CX-43 — Exercise Selector V2:**
- `scripts/middle-math/exercise_selector.py` rewritten to V2 with registry-first data loading (`middle-math/exercise-registry.json`) while preserving V1 compatibility via `--v1` (`middle-math/exercise-library.json`).
- Affinity engine upgraded from binary flags to octave-scale vectors using registry-native `axis_affinity` and `order_affinity` weights at their emoji index positions; Type contribution retained at +2.
- Family diversity logic added:
  - Cross-block family reuse gets score multiplier penalty (`×0.3`) instead of hard exclusion.
  - In-block candidate list now enforces unique `family_id` among ranked outputs.
- Substitution chain integration added via `middle-math/exercise-engine/substitution-map.json`; optional output enabled with `--show-subs` (`tier_down`, `tier_up`, `cross_family`).
- Catch-all movement-pattern preprocessing implemented: for `movement_pattern == "core-stability"`, override to `family_id` when family is in major pattern allowlist. Override count logged to stderr.
- Validation extended: `--validate` now checks GOLD gate, cross-block duplicate exercises, and no same-family duplicates within a block.
- CLI expanded with `--all` (all 1,680 zips), `--v1`, and `--show-subs`.

**Validation + evidence:**
- `python scripts/middle-math/exercise_selector.py --all --validate --output json > /tmp/cx43-validate-v2.json`
  - Validation summary: 1,680 checked, 1,680 pass, 0 fail.
  - Evidence file: `/tmp/cx43-validate-v2.json`
- `python scripts/middle-math/exercise_selector.py --zip 2123 --show-subs --output text` (spot check substitution chain rendering)
- `python scripts/middle-math/exercise_selector.py --zip 2123 --v1 --validate --output text` (backward compatibility mode check)

**Tracking updated:** `whiteboard.md`, `.codex/TASK-ARCHITECTURE.md`

**Final state:** CX-43 complete. Wave 7 complete (CX-41, CX-42, CX-43). CX campaign now 40/44 complete.

---

## Session 042 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Exercise Library Expansion (Wave 7)
**Task completed:** Exercise Content Batch 4 (1001–1500)

---

**Work completed:**
- Ran `python scripts/generate-exercise-content.py --batch 1500` to continue generation from the existing 993-file state.
- Generator skipped existing files and wrote 493 new knowledge files, bringing `exercise-content/` to 1,486 files total.
- Confirmed distribution across all five type directories: push (516), pull (496), legs (189), plus (280), ultra (5).
- Spot-checked 3 random generated files for completeness and template structure:
  - `exercise-content/push/pnf-tricep-stretch-contract-relax.md`
  - `exercise-content/pull/seated-hip-internal-rotation.md`
  - `exercise-content/plus/knee-drive-standing.md`

**Validation run:**
- `python scripts/generate-exercise-content.py --batch 1500`
- `python scripts/generate-exercise-content.py --stats`
- `for d in push pull legs plus ultra; do find exercise-content/$d -type f -name '*.md' | wc -l; done`
- Manual content review (`sed`) on 3 random files

**Validation outcomes:**
- Batch run summary: `Written: 493 | Skipped: 1007 | Errors: 0 | Avg words/file: 486`
- Stats summary: `Files written: 1486` (`Coverage: 71.3%`)
- Spot-check files all include frontmatter, setup, execution, common faults, order context, color modifiers, and coaching notes sections; word counts in expected ~400–500 range.

**Tracking updated:** `whiteboard.md`

**Final state:** Exercise content generation now covers 1,486/2,085 exercises. Next batch to reach ~2,000 can proceed with `--batch 2000` when scheduled.

---

## Session 043 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Deck Generation
**Task completed:** Deck 11 (⛽⌛ Strength Time) identity + 40 cards

---

**Work completed:**
- Built `deck-identities/deck-11-identity.md` from scaffold to complete deck identity with philosophy, Type×Color coverage map, color differentiation logic, primary exercise mapping for all 40 zips, and zip identity lines.
- Generated all 40 Deck 11 cards under `cards/⛽-strength/⌛-time/` and renamed every stub to complete semantic filenames with operator emoji and title.
- Updated generated card frontmatter from `status: EMPTY` to `status: GENERATED`.
- Updated `whiteboard.md` card count and deck status to include Deck 11 complete (40/40), total cards now 182/1,680.

**Validation run:**
- `for f in cards/⛽-strength/⌛-time/*/*.md; do python scripts/validate-card.py "$f"; done`
- `bash scripts/validate-deck.sh cards/⛽-strength/⌛-time`
- `python scripts/audit-exercise-coverage.py cards/⛽-strength/⌛-time`

**Validation outcomes:**
- 40/40 cards passed `validate-card.py`
- Deck validator summary: all generated cards valid
- Exercise coverage audit: no duplicate primary exercises across any Type row

**Final state:**
- Deck 11 fully generated and validated.
- Global card count now 182/1,680.

## Session 044 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Deck Generation
**Task completed:** Deck 12 (⛽🐬 Strength Partner) identity + 40 cards

---

**Work completed:**
- Built `deck-identities/deck-12-identity.md` from scaffold to complete identity status with deck philosophy, Type×Color coverage map, color differentiation logic, full 40-zip exercise mapping, and 40 zip identity lines.
- Generated all 40 Deck 12 cards under `cards/⛽-strength/🐬-partner/`, replaced each stub, renamed files to semantic operator + title format, and set frontmatter status to `GENERATED`.
- Updated `whiteboard.md` to mark Deck 12 complete and moved total card count to 222/1,680 with note that the ⛽ Strength Order is complete at 240/1,680 rooms.

**Validation run:**
- `for f in cards/⛽-strength/🐬-partner/*/*.md; do python scripts/validate-card.py "$f"; done`
- `bash scripts/validate-deck.sh cards/⛽-strength/🐬-partner`
- `python scripts/audit-exercise-coverage.py cards/⛽-strength/🐬-partner`

**Validation outcomes:**
- 40/40 cards passed `validate-card.py`
- Deck validator summary: generated cards valid
- Exercise coverage audit: unique primary exercises across each Type row

**Final state:**
- Deck 12 fully generated and validated.
- Global card count now 222/1,680.
- ⛽ Strength Order complete: 240/1,680 rooms filled.

## Session 045 — 2026-03-06

**Branch:** `claude/exercise-library-expansion-LWTl5`
**Campaign:** Exercise Library Expansion (Wave 7)
**Task completed:** Exercise Content Batch 5 FINAL (1501–2085)

---

**Work completed:**
- Ran `python scripts/generate-exercise-content.py --batch 2085` to finish remaining exercise knowledge files.
- Initial generation pass produced 581 new files; coverage audit identified 18 missing exercise IDs caused by slug collisions between same-name variants.
- Updated `scripts/generate-exercise-content.py` to resolve output paths by `exercise_id` and disambiguate collisions with `-ex-####` suffixes.
- Re-ran `python scripts/generate-exercise-content.py --batch 2085`; generator wrote the 18 missing files.
- Confirmed full coverage at 2,085/2,085 and verified distribution across all five type directories.
- Spot-checked 3 random files for completeness and expected content length:
  - `exercise-content/plus/step-and-throw-forward.md` (451 words)
  - `exercise-content/push/9090-external-rotation.md` (441 words)
  - `exercise-content/pull/diaphragmatic-breathing-pelvic-floor-coordination.md` (470 words)

**Validation run:**
- `python scripts/generate-exercise-content.py --batch 2085`
- `python scripts/generate-exercise-content.py --stats`
- `for d in push pull legs plus ultra; do find exercise-content/$d -type f -name '*.md' | wc -l; done`
- Coverage integrity audit (registry IDs vs file frontmatter IDs) via ad-hoc Python check
- Manual content review (`sed` + `wc -w`) on 3 random files

**Validation outcomes:**
- Final batch summary: all remaining files generated; coverage complete after collision-safe path fix.
- Stats summary: `Registry entries: 2085`, `Files written: 2085`, `Coverage: 100.0%`.
- Type distribution: push (575), pull (505), legs (280), plus (650), ultra (75).
- Spot-check files include full template sections and remain in expected ~400–500 word range.

**Tracking updated:** `whiteboard.md`

**Final state:** Exercise content knowledge library is complete at 2,085/2,085 files (100% coverage).
