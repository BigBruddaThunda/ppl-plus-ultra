# CONTRACTS.md — Negotiosum Switchboard

The sum of negotiation. The living state of all work across all Archideck projects.

---

## ACTIVE

### Ppl± — Quality Rebuild Campaign (Phase 3.1)
- **Scope:** 1,680/1,680 cards generated. Avg quality score: 88/100. Rebuild campaign targeting Color blindness, Exercise-Type misroutes, parameter violations, and content depth gaps.
- **Current:** Audit pipeline complete. Coverage database generated. Rebuild queue prioritized by score. See `whiteboard.md` for task board.
- **Next physical action:** Rebuild worst-scoring Color categories (🟠 Circuit, 🟡 Fun, ⚪ Mindful) using upgraded card-generator skill.
- **Location:** Repository root `/` (Ppl± predates Archideck layer)

```
zip: 🦋 🤌 🔴
weight-vector-bias: {order: ionic, modifier: facio, color: intense}
depends-on: []
blocks: [ppl-experience-layer, ppl-operis-pipeline]
milestone: M3.1 (Quality Rebuild — before Hypertrophy Order Sweep)
```

### GSD × SCL Orchestration Layer
- **Scope:** Wire GSD framework to SCL zip codes. Codebase map, Negotiosum upgrade, milestone scaffolding, session pipeline.
- **Current:** Executing this session (2026-03-07). Branch: `claude/emoji-fitness-dictionary-aE8LY`.
- **Next physical action:** Complete phases 2–4, commit, push.
- **Location:** `archideck/`, `.planning/`

```
zip: 🐂 🏛 🔵
weight-vector-bias: {order: tuscan, axis: firmitas, color: structured}
depends-on: []
blocks: [all future sessions — unlocks zip-routed routing]
milestone: M0 (Infrastructure — precedes M1)
```

---

## QUEUED

### Ppl± — Experience Layer (Phase 4)
- **Scope:** HTML rendering of `.md` cards into interactive workout UI. User accounts, logging, subscriptions.
- **Blocked by:** Deck generation milestone (Phase 2 completion or critical mass)
- **Seed docs:** `seeds/experience-layer-blueprint.md`, `seeds/mobile-ui-architecture.md`, `seeds/stripe-integration-pipeline.md`
- **Location:** `html/` (scaffold only, non-functional)

```
zip: 🖼 🌹 🟡
weight-vector-bias: {order: palladian, axis: venustas, color: fun}
depends-on: [ppl-workout-generation]
blocks: [ppl-stripe-subscription, ppl-user-accounts]
milestone: M10 (Experience Layer)
```

### Ppl± — Operis Pipeline
- **Scope:** Daily editorial system. 4-prompt pipeline. Cosmogram + temporal filter. V4 architecture complete.
- **Blocked by:** Historical events database (366 files, one-time build), Operis V4 pipeline test
- **Seed docs:** `seeds/operis-prompt-pipeline.md`, `seeds/operis-architecture.md`
- **Location:** `operis-editions/`

```
zip: 🏟 ⌛ 🔵
weight-vector-bias: {order: corinthian, axis: temporitas, color: structured}
depends-on: [ppl-cosmogram-population, ppl-historical-events-db]
blocks: []
milestone: M9 (Operis Pipeline V4)
```

### Ppl± — Cosmogram Population
- **Scope:** Deep identity documents for all 42 decks. Research prompt + publication standard committed. V2 scaffolds generated (machine-first-pass, no web deposits yet).
- **Blocked by:** Session time (Genspark web-access sessions per deck)
- **Seed docs:** `seeds/cosmogram-research-prompt.md`, `scl-deep/publication-standard.md`
- **Location:** `deck-cosmograms/`

```
zip: 🐂 🌹 🟣
weight-vector-bias: {order: tuscan, axis: venustas, color: technical}
depends-on: []
blocks: [ppl-operis-pipeline]
milestone: M8 (Cosmogram First Pass)
```

### Graph Parti — District Organization
- **Scope:** Semantic canvas for architecture and complex thinking. 7+1 Order files as district containers. SCL zip codes for every idea, block, and district.
- **Status:** First pass complete. Needs refinement loop, cross-reference to kernel, intake of new ideas.
- **Key concepts:** Standard zip (4-dial) and District zip (6-dial), Ralph Loop as primary sorting process
- **Location:** `projects/graph-parti/`

```
zip: ⚖ 🏛 🟢
weight-vector-bias: {order: vitruvian, axis: firmitas, color: growth}
depends-on: []
blocks: [ralph-loop-sort, district-refinement, kernel-cross-ref]
milestone: (independent)
```

### Story Engine — Narrative Architecture
- **Scope:** Story and video game architecture using SCL addressing. Acts, characters, scenes, world-building as zip-coded content.
- **Status:** Raw ideas. Needs intake processing through Ralph Loop.
- **Location:** `projects/story-engine/` (scaffold created)

```
zip: 🐂 🌹 🟡
weight-vector-bias: {order: tuscan, axis: venustas, color: fun}
depends-on: []
blocks: [intake-processing, ralph-loop-sort]
milestone: (independent)
```

### Civic Atlas — Urban Design Layer
- **Scope:** Real estate, urban planning, and civic design project using SCL addressing. Parcels, zones, districts as zip-coded content.
- **Status:** Raw ideas. Needs intake processing.
- **Location:** `projects/civic-atlas/` (scaffold created)

```
zip: 🐂 🐬 🟡
weight-vector-bias: {order: tuscan, axis: sociatas, color: fun}
depends-on: []
blocks: [intake-processing, ralph-loop-sort]
milestone: (independent)
```

---

## PARKED

*(Contracts not currently in rotation but not abandoned)*

### Ppl± — Linters CI Pipeline
- **Scope:** Three-tier validation (markdownlint-cli2, frontmatter schema, SCL validator). GitHub Actions gate before merge.
- **Blocked by:** Seed not yet promoted to active. PostToolUse hook (Tier 3) already running.
- **Seed docs:** `seeds/linters-architecture.md`

```
zip: ⛽ 🏛 🔵
weight-vector-bias: {order: doric, axis: firmitas, color: structured}
depends-on: []
blocks: [merge-to-main-policy]
milestone: (infrastructure — no milestone assigned)
```

### Ppl± — Middle-Math Engine
- **Scope:** Computation engine between SCL spec and rendered experience. Weight declarations, selection algorithms, rotation engine.
- **Status:** Architecture seeded. Weight declarations in first-draft for Orders only.
- **Location:** `middle-math/`

```
zip: ⚖ 🏛 🟣
weight-vector-bias: {order: vitruvian, axis: firmitas, color: technical}
depends-on: []
blocks: [ppl-experience-layer]
milestone: (precedes M10)
```

---

## COMPLETED (recent)

- ✅ Ppl± All 42 decks generated (1,680/1,680 — PR #116 batch generation)
- ✅ Ppl± Decks 07, 08, 09, 10, 11, 12 generated (all ⛽ Strength Axes)
- ✅ Ppl± Deck 01 generated (🐂🏛 Foundation Basics)
- ✅ Ppl± infrastructure sprint (scripts, hooks, subagents, skills — Session 18)
- ✅ Ppl± Operis V4 pipeline prompts stored as seeds (Sessions 028–029)
- ✅ Ppl± Numeric zip notation documented (seed + CLAUDE.md)
- ✅ Ppl± Vocabulary standard seeded (`scl-deep/vocabulary-standard.md`)
- ✅ Ppl± Reverse-weight resolution seeded (`middle-math/rotation/`)
- ✅ Graph Parti first pass complete (7+1 Order files written)
- ✅ Archideck concept defined (2026-03-07)
- ✅ Archideck infrastructure initialized (2026-03-07)
- ✅ GSD × SCL Orchestration Layer (2026-03-07 — this session)
  - `.planning/codebase/` (7 documents, SCL-enriched)
  - `archideck/CONTRACTS.md` (zip schema upgrade)
  - `archideck/contract-graph.json`
  - `.planning/milestones/M1–M10-CONTEXT.md`
  - `archideck/session-pipeline.md`

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

### Zip Schema

Each contract carries a zip code block in Kernel grammar (`Order · Axis/Modifier · Color`):

```
zip: [partial zip, 2–3 emojis]
weight-vector-bias: {key: value pairs for dominant dial weights}
depends-on: [list of contract IDs that must complete first]
blocks: [list of contract IDs or sub-tasks this contract enables]
milestone: [GSD milestone label, if applicable]
```

The zip locates the contract within the 1,680-node navigation graph.
The weight-vector-bias describes the dominant cognitive posture of the work.
The depends-on/blocks edges form the contract dependency graph (`archideck/contract-graph.json`).

---

🧮
