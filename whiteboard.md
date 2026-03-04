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
- [x] Deck 07 (⛽🏛 Strength × Basics) — 40/40 GENERATED-V2 ✅ Retrofitted Session 021 (18 cards flagged REGEN-NEEDED; identity doc built)
- [x] Deck 08 (⛽🔨 Strength × Functional) — 40/40 GENERATED-V2

### Infrastructure (BUILT)
- [x] Deck identities layer — deck-identities/ with README, template, naming-convention, deck-08-identity
- [x] Zip-web architecture — zip-web/ with rules, signatures, registry, 42 pod files (Deck 07 populated, 41 stubs)
- [x] Ralph Loop — scripts/ralph/ with ralph.sh, RALPH-PROMPT.md, prd.json, progress.txt
- [x] Automation — scripts/ (validate-card.py, progress-report.py, validate-deck.sh, audit-exercise-coverage.py)
- [x] Audit workflow docs — scripts/README.md (full audit orchestrator + checklist matrix link)
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

## Deck Campaign Table

Each deck is a 5-lane campaign. See `seeds/deck-campaign-workflow.md` for full spec.

| Deck | Order × Axis | Cosmogram | Identity | Cards | Audit | CANONICAL |
|------|-------------|-----------|----------|-------|-------|-----------|
| 07   | ⛽🏛         | —         | ✅ V2 (Session 021) | ⚠️ 40 (18 REGEN-NEEDED) | ⬜ | ⬜ |
| 08   | ⛽🔨         | —         | ✅ V2 (Session 017) | ✅ 40 (Session 009) | ⬜ | ⬜ |
| 09   | ⛽🌹         | ⬜         | ⬜        | ⬜    | ⬜    | ⬜        |
| 10   | ⛽🪐         | ⬜         | ⬜        | ⬜    | ⬜    | ⬜        |
| 11   | ⛽⌛         | ⬜         | ⬜        | ⬜    | ⬜    | ⬜        |
| 12   | ⛽🐬         | ⬜         | ⬜        | ⬜    | ⬜    | ⬜        |

Status: ⬜ Not started | 🔄 In progress | ✅ Complete | ⚠️ Issues (regen queue active) | — Not applicable

---

## Immediate Queue — Next Sessions

Priority order. Top item is next unless Jake redirects.

Priority order. Top item is next unless Jake redirects.

**0. ✅ Merge Session 028 Infrastructure Patch** — COMPLETE
Merged to main before Session 029.

**1. ✅ Store Operis V4 Prompts in Repo — Session 029** — COMPLETE
Files committed: seeds/operis-researcher-prompt.md, seeds/operis-content-architect-prompt.md, seeds/operis-editor-prompt.md, seeds/operis-builder-prompt.md (all V4.0).
Also updated: seeds/operis-prompt-pipeline.md (version tags, 17-dept matrix, Prompt File Reference), seeds/operis-sandbox-structure.md (Constraint Summary, Mapping Chain, Naming Convention), seeds/operis-architecture.md (pipeline file refs, dept alignment, engine version note), CLAUDE.md (seed listings, backlog status).

**2. ⚠️ Test Operis V4 Pipeline — Full Date Test (Session 030)**
Status: Executed for 2024-07-26 (Friday), Northeastern US deterministic frame.
Result: PARTIAL PASS / CONTRACT FAIL.

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

Follow-up actions:
1) Add strict URL + sky-field enforcement to P1 template/checklist.
2) Add per-lane URL enforcement to P2 template/checklist.
3) Add Contract C frontmatter schema preflight (`sandbox-zips`, `sandbox-total`) to P3.
4) Re-run same date test after prompt/schema patching.

**2A. Codex Audit — Agents-Friendly Expansion (Non-Operis Core)**
Why: Define non-web tasks that strengthen Daily Operis substrate: deck throughput, validation automation, inventory truth tables, and agent handoff contracts.
Depends on: None.
Unblocks: Safer scale-up while web-dependent research is deferred.

**3. Build Deck 09 Identity — `/build-deck-identity 09`**
Why: ⛽🌹 Strength × Aesthetic is next in the generation queue.
Identity doc maps exercises to zip codes before generation starts.
Depends on: Nothing — can run in parallel with Operis pipeline testing.
Unblocks: Deck 09 generation (40 cards).

**4. Generate Deck 09 — 40 cards, ⛽🌹 Strength × Aesthetic**
Why: Continuing through ⛽ Order. Systematic Order-first sweep.
Depends on: Deck 09 identity document.
Unblocks: Progress toward ⛽ Order completion.

**5. Generate First Deck Cosmogram**
Why: Research prompt and publication standard are committed. Ready for first cosmogram via Genspark temp architect session.
Depends on: Genspark session with web access.
Unblocks: Deep content layer for card generation and Operis depth.

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
- scl-deep/ has full reference layer now populated
- emoji-macros.md ✅ committed Session 026 — cultural/historical macro meanings for all 61 emojis
- order-specifications.md ✅ committed Session 026 — deep spec for all 7 Orders (parameters, character, block sequences, interaction matrices, common errors)
- block-specifications.md ✅ committed Session 026 — deep spec for all 22 blocks + SAVE (context-dependence matrices, content rules)
- operator-specifications.md ✅ committed (previous session) — Latin etymology, operator logic
- color-specifications.md ✅ committed (previous session) — equipment tiers, format rules
- type-specifications.md ✅ committed (previous session) — muscle groups, movement patterns
- axis-specifications.md — existing file (v1, imported from scl-deep source layer)
- color-context-vernacular.md — existing file (v1, imported from scl-deep source layer)
- order-parameters.md — existing file (v1, imported from scl-deep source layer)
- These are reference docs — they deepen understanding but don't block generation

### Git-Worktree Adoption
- Seed planted: seeds/git-worktree-pattern.md
- Adopt when parallel branch work becomes frequent enough to justify
- Currently: one branch at a time is sufficient

### PPL± Operis Build-Out
- Seed planted: seeds/operis-architecture.md (supersedes seeds/daily-architecture.md)
- Architecture complete: weekly editorial cadence, 109 content types, generation pipeline spec, front page card layout, depth standard, age-neutral register (Session 027)
- Pipeline architecture planted: seeds/operis-prompt-pipeline.md — 4-prompt pipeline with handoff contracts and Color flow (Session 028)
- Educational layer planted: seeds/operis-educational-layer.md — 8-lane content system mapped to Color Context Vernacular (Session 028)
- Color of the Day architecture planted: seeds/operis-color-posture.md — cognitive posture system, three Color identities, automation pathway (Session 028)
- Sandbox structure planted: seeds/operis-sandbox-structure.md — 13-room architecture (8 Color siblings + 5 Content Rooms), content-to-zip mapping (Session 028)
- Historical events database directory planted: operis-editions/historical-events/ (Session 028)
- Reverse-weight resolution seeded: middle-math/rotation/reverse-weight-resolution.md — triangulates today's featured room between yesterday's fatigue and tomorrow's stimulus
- Vocabulary standard seeded: scl-deep/vocabulary-standard.md — governs all PPL± content generation going forward
- Color weight derivation updated: middle-math/rendering/operis-weight-derivation.md — Color of the Day scoring mechanism planned (Session 028)
- Publication standard updated: scl-deep/publication-standard.md — Color as Cognitive Posture extension added (Session 028)
- Next: Store four Operis V4 prompts in repo as seeds (Researcher, Content Architect, Editor, Builder). Then test pipeline on a real date. Then continue Deck 09 identity and generation.
- Requires: historical events database (366 files, one-time build ~180 hours research, builds incrementally)
- Requires: cosmogram population (provides deep substrate for featured zip descriptions)
- Requires: HTML experience layer (Phase 4/5)
- Automation target: fully automated Operis generation from deterministic inputs + Color scoring mechanism
- Does not block card generation

### Platform Architecture V2
- Seed planted: seeds/platform-architecture-v2.md
- Supersedes: Feb 11 "PPL± ITSELF" document (archived at seeds/platform-architecture-v1-archive.md)
- Requires: card generation progress, cosmogram population, Daily prototype refinement
- Database schema ready for prototyping when Phase 4/5 activates
- Does not block card generation

### Middle-Math Engine
- Directory planted: `middle-math/`
- Weight declarations: Order weights in DRAFT, 5 remaining categories STUB
- Exercise engine: selection algorithm spec written, family trees DRAFT (major patterns only)
- User context: ledger, profile, toggle, translation specs written
- Rotation: engine spec formalized from seed, junction algorithm written, fatigue model DRAFT
- Rendering: UI and Operis weight derivation at SEED level, progressive disclosure at SEED level
- Roots: Almanac math primitives preserved and mapped (octave-logic, order-notation, four-layers, almanac-archive)
- Schemas: 7 database table definitions (exercise library enhanced, families, ledger, profile, toggles, zip weight cache, zip metadata)

Next steps for middle-math:
1. Complete weight declarations for remaining 5 emoji categories (Axes, Types, Colors, Blocks, Operators)
2. Populate exercise family trees for all major movement patterns (currently covers 8 most critical families)
3. Prototype the selection algorithm as executable code (`scripts/middle-math/`)
4. Build transfer ratio table from exercise science reference data
5. Prototype weight vector computation for sample zip codes

### Experience Layer Build-Out
- 20 Claude Code sessions: `seeds/claude-code-build-sequence.md`
- Sessions A-C2: skeleton, rendering, navigation, voice parser (Phase 4/5)
- Sessions D-H: auth, profiles, Stripe, logging, saved rooms (Phase 6)
- Sessions I-L: Operis, floors, zoom, community (Phase 5/6)
- Sessions M-N: data export/deletion, production deployment (Phase 7)
- Sessions V-Z: TTS, audio API, playlists, Android Auto, CarPlay (Phase 7+)
- Each session: scoped, testable, produces working increment
- Can interleave with card generation

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
  - whiteboard.md — updated (this file)
Next: Continue card generation pipeline (Deck 09 identity or Deck 07 regen queue). Daily and platform seeds do not block generation.

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
Next: Test full Operis V4 pipeline on a real date (run P1→P2→P3→P4 in sequence). Then Build Deck 09 identity. Then Generate Deck 09.

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
Next: Store four Operis V4 prompts in repo as seeds (Session 029). Then test P1→P2→P3 on a real date. Then continue Deck 09.

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
  - whiteboard.md — this session logged; Immediate Queue and Backlog updated.
Architecture verified post-PR-25 merge (10 commits from Session 026 confirmed present).
Operis V3 prompt delivered — front page card, almanac-right layout, age-neutral register, no polarity language on reader-facing surfaces.
Next: Test Operis V3 Prompt in temp architect session with full prompt. Then continue Deck 09 identity → Deck 09 generation.

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
  - whiteboard.md — This session log, queue update, backlog
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

- The 4-dial elevator model: Order=building, Axis=floor, Type=wing, Color=room.
  1,680 rooms. One elevator. Four dials. The Operis is the morning's default destination.

- Piano nobile floor stack (bottom to top on screen, ground to penthouse in building):
  🔨 ground → 🏛 piano nobile → ⌛ 2nd → 🐬 3rd → 🌹 4th → 🪐 5th.
  Scroll direction on phone is inverse of building direction. Progressive disclosure IS the architecture.

- The Operis is the front door the system was missing. Solves cold start,
  solves onboarding, solves room circulation, and is automatable once
  inputs are populated (historical DB + cosmograms + calendar data + pub standard).

- PPL± Operis is the official name for the platform's daily publication. Latin genitive "of
  the work." Phonetically approximates "off the press." Supersedes the working title "The
  Daily." Full architecture in seeds/operis-architecture.md. Named Session 023.

- Programs are guided tours through the zip web — sequences of addresses,
  not sequences of workouts. The rooms already exist. The program is the itinerary.

- Publication standard constraint added: no "it's not X, it's Y" framing.
  The publication is informational. The reader informs the opinion.
  Independent of Party or Faction. Committed to Useful Knowledge.

Update this file whenever the project state changes.
The whiteboard is always the current truth.

🧮
