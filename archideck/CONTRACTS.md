# CONTRACTS.md — Negotiosum Switchboard

The sum of negotiation. The living state of all work across all Archideck projects.

---

## ACTIVE

### PPL± — Workout Generation
- **Scope:** Phase 2 deck generation. 262/1,680 cards complete. 7 decks done (01, 07–12).
- **Current:** See `whiteboard.md` (Negotiosum) for task board. See `CLAUDE.md` for generation rules.
- **Next physical action:** Generate next card in active deck per whiteboard.md instructions.
- **Location:** Repository root `/` (PPL± predates Archideck layer)

---

## QUEUED

### PPL± — Experience Layer (Phase 4)
- **Scope:** HTML rendering of `.md` cards into interactive workout UI. User accounts, logging, subscriptions.
- **Blocked by:** Deck generation milestone (Phase 2 completion or critical mass)
- **Seed docs:** `seeds/experience-layer-blueprint.md`, `seeds/mobile-ui-architecture.md`, `seeds/stripe-integration-pipeline.md`
- **Location:** `html/` (scaffold only, non-functional)

### PPL± — Operis Pipeline
- **Scope:** Daily editorial system. 4-prompt pipeline. Cosmogram + temporal filter. V4 architecture complete.
- **Blocked by:** Historical events database (366 files, one-time build), Operis V4 pipeline test
- **Seed docs:** `seeds/operis-prompt-pipeline.md`, `seeds/operis-architecture.md`
- **Location:** `operis-editions/`

### PPL± — Cosmogram Population
- **Scope:** Deep identity documents for all 42 decks. Research prompt + publication standard committed.
- **Blocked by:** Session time (first pass drafts scaffolded, no web deposits yet)
- **Seed docs:** `seeds/cosmogram-research-prompt.md`, `scl-deep/publication-standard.md`
- **Location:** `deck-cosmograms/`

### Graph Parti — District Organization
- **Scope:** Semantic canvas for architecture and complex thinking. 7+1 Order files as district containers. SCL zip codes for every idea, block, and district.
- **Status:** First pass complete. Needs refinement loop, cross-reference to kernel, intake of new ideas.
- **Key concepts:** Standard zip (4-dial) and District zip (6-dial), Ralph Loop as primary sorting process
- **Location:** `projects/graph-parti/`

### Story Engine — Narrative Architecture
- **Scope:** Story and video game architecture using SCL addressing. Acts, characters, scenes, world-building as zip-coded content.
- **Status:** Raw ideas. Needs intake processing through Ralph Loop.
- **Location:** `projects/story-engine/` (scaffold created)

### Civic Atlas — Urban Design Layer
- **Scope:** Real estate, urban planning, and civic design project using SCL addressing. Parcels, zones, districts as zip-coded content.
- **Status:** Raw ideas. Needs intake processing.
- **Location:** `projects/civic-atlas/` (scaffold created)

---

## PARKED

*(Contracts not currently in rotation but not abandoned)*

### PPL± — Linters CI Pipeline
- **Scope:** Three-tier validation (markdownlint-cli2, frontmatter schema, SCL validator). GitHub Actions gate before merge.
- **Blocked by:** Seed not yet promoted to active. PostToolUse hook (Tier 3) already running.
- **Seed docs:** `seeds/linters-architecture.md`

### PPL± — Middle-Math Engine
- **Scope:** Computation engine between SCL spec and rendered experience. Weight declarations, selection algorithms, rotation engine.
- **Status:** Architecture seeded. Weight declarations in first-draft for Orders only.
- **Location:** `middle-math/`

---

## COMPLETED (recent)

- ✅ PPL± Decks 07, 08, 09, 10, 11, 12 generated (all ⛽ Strength Axes)
- ✅ PPL± Deck 01 generated (🐂🏛 Foundation Basics)
- ✅ PPL± infrastructure sprint (scripts, hooks, subagents, skills — Session 18)
- ✅ PPL± Operis V4 pipeline prompts stored as seeds (Sessions 028–029)
- ✅ PPL± Numeric zip notation documented (seed + CLAUDE.md)
- ✅ PPL± Vocabulary standard seeded (`scl-deep/vocabulary-standard.md`)
- ✅ PPL± Reverse-weight resolution seeded (`middle-math/rotation/`)
- ✅ Graph Parti first pass complete (7+1 Order files written)
- ✅ Archideck concept defined (2026-03-07)
- ✅ Archideck infrastructure initialized (2026-03-07) — this session

---

## CONTRACT PROTOCOL

A contract is created when work is scoped and committed to.

- **ACTIVE** — Work is happening in current sessions. Has a clear next physical action.
- **QUEUED** — Scoped and ready. Blocked by a dependency or waiting for session time.
- **PARKED** — Not abandoned. Not blocked. Just not in rotation. Revisit deliberately.
- **COMPLETED** — Done. Stays visible for 2–3 sessions as recent memory, then archives to session-log.md.

To activate a queued contract: state it in session, move to ACTIVE, ensure the blocker is resolved.
To park a contract: acknowledge it explicitly, state the reason, move to PARKED.
To complete a contract: verify the deliverable, move to COMPLETED, note the date.

---

🧮
