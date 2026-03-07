# Architecture

**Analysis Date:** 2026-03-07

## Pattern Overview

**Overall:** Content generation pipeline with layered specification authority

PPL± is not a web application. It is a content repository and generation system. The architecture is a multi-layer specification stack: rules at the top, generated markdown files at the bottom, with Python validation scripts, Claude agent skills, and a computation engine specification layer in between.

**Key Characteristics:**
- The zip code (4-emoji address) is the universal key — every card, every file, every future database row, every URL derives from it
- Authority flows downward: `CLAUDE.md` → `scl-directory.md` → `exercise-library.md` → generated card files
- No runtime environment exists yet; the "system" is AI-assisted generation of static markdown files
- Middle-math is an architecture specification (DRAFT), not running code
- The Archideck meta-layer enables parallel multi-project operation under a shared SCL grammar

## Layers

**Layer 0 — Kernel (SCL Grammar):**
- Purpose: Universal language specification shared across all projects
- Location: `archideck/KERNEL.md`
- Contains: 61-emoji dictionary, 7 categories, zip code grammar, polysemic mapping table, Ralph Loop process, Negotiosum contract system
- Depends on: Nothing — it is the root
- Used by: All projects, all agents, all generation sessions

**Layer 1 — Project Operating Rules:**
- Purpose: PPL±-specific generation law; overrides and extends the kernel for fitness domain
- Location: `CLAUDE.md` (root), `scl-directory.md`, `generation-philosophy.md`, `card-template-v2.md`
- Contains: Order/Axis/Type/Color parameters, constraint hierarchy, block sequences, tonal rules, validation checklist, operator table, format requirements
- Depends on: KERNEL.md (grammar base)
- Used by: All generation agents, validation scripts, deck identity documents

**Layer 2 — Exercise Authority:**
- Purpose: The only valid source for exercise names used in generated cards
- Location: `exercise-library.md` (~2,185 exercises, 133KB, sections A–Q)
- Contains: Exercise names organized by muscle group, SCL Type mapping, Order relevance, Axis emphasis, Equipment Tier range, GOLD gate status, Operator affinity
- Depends on: Layer 1 for type routing definitions
- Used by: Card generation agents, `scripts/exercise-usage-report.py`, `scripts/middle-math/parse_exercise_library.py`

**Layer 3 — Deck Identity Documents:**
- Purpose: Per-deck exercise mapping, coverage map, color differentiation logic, philosophy
- Location: `deck-identities/deck-[XX]-identity.md` (18 of 42 decks populated)
- Contains: Coverage map (Type × Color grid), primary exercise assignments per card, naming guidance, color differentiation logic
- Depends on: Layers 1 and 2
- Used by: Card generation agent reads deck identity before generating any card in that deck

**Layer 4 — Generated Card Files:**
- Purpose: The master content artifacts — fully-specified workout cards in SCL markdown format
- Location: `cards/[order-folder]/[axis-folder]/[type-folder]/[filename].md`
- Contains: YAML frontmatter (zip, operator, status, deck, order, axis, type, color, blocks) + workout content in SCL format
- Depends on: All layers above
- Used by: Future HTML rendering layer (Phase 4/5), future procedural engine as templates

**Layer 5 — Middle-Math Engine (Architecture DRAFT):**
- Purpose: Specification for the future procedural computation engine between SCL rules and rendered output
- Location: `middle-math/` (7 subdirectories, spec-only — no runtime code)
- Contains: Weight system declarations (61 emojis on -8 to +8 scale), exercise selection algorithm, user context schemas, rotation engine spec, rendering derivation specs, database schemas
- Depends on: All layers above (reads rules, reads exercises, reads cards)
- Used by: Phase 4/5 development (not yet built)

**Layer 6 — Meta-Layer (Archideck):**
- Purpose: Cross-project contract tracking, universal agent operating protocol, intake for raw ideas
- Location: `archideck/` (KERNEL.md, CONTRACTS.md, AGENT-CONTRACT.md, intake/, projects/)
- Contains: Negotiosum switchboard (CONTRACTS.md), agent session start sequence, intake landing zone, non-PPL± project scaffolds
- Depends on: Nothing (runs alongside all projects)
- Used by: All sessions across all projects

## Data Flow

**Card Generation Pipeline:**

1. Agent reads `CLAUDE.md` (operating rules) + `archideck/KERNEL.md` (language)
2. Agent reads `whiteboard.md` to identify the active zip code
3. Agent reads `deck-identities/deck-[XX]-identity.md` to load the coverage map and exercise assignments
4. Agent reads relevant sections of `exercise-library.md` for the card's Type
5. Agent locates stub file at `cards/[order]/[axis]/[type]/[zip]±.md`
6. Agent generates workout content respecting constraint hierarchy: Order > Color > Axis > Equipment
7. Agent writes generated content to the stub file, updating `status: EMPTY` → `status: GENERATED`
8. Agent renames file from `[zip]±.md` → `[zip]±[operator-emoji] [Title].md`
9. PostToolUse hook auto-runs `python scripts/validate-card.py "[file-path]"`
10. Agent logs the completed zip to `whiteboard.md`

**Validation Flow:**

```
Generated card file
      ↓
scripts/validate-card.py
      ↓ checks:
  - Frontmatter fields present and valid
  - Status value in {EMPTY, GENERATED, GENERATED-V2, CANONICAL}
  - Block count within Order's min-max range
  - No GOLD keywords in non-GOLD colors (not 🔴 or 🟣)
  - Required format elements present
      ↓
Exit 0 (pass) or Exit 1 (fail with error list)
```

**Middle-Math Weight Resolution (future, not yet built):**

```
Zip code (e.g. ⛽🏛🪡🔵 = 2123)
      ↓
Numeric dial decomposition: Order=2, Axis=1, Type=2, Color=3
      ↓
61-value weight vector construction (each emoji gets -8 to +8 weight)
      ↓
Constraint hierarchy cascade: Order weights suppress conflicting lower-priority weights
      ↓
Weight vector used for: exercise selection, UI palette, tonal register, Operis editorial decisions
```

**State Management:**

Card status is tracked via YAML frontmatter in each card file:
- `status: EMPTY` — stub awaiting generation
- `status: GENERATED` — V1 format (pre-philosophy-v2)
- `status: GENERATED-V2` — current V2 format
- `status: CANONICAL` — reviewed and approved

Progress tracking runs via `python scripts/progress-report.py` which scans all card files and counts by status. Dashboard data written to `docs/dashboard/data/progress.json`.

## Key Abstractions

**The Zip Code:**
- Purpose: 4-emoji semantic address that fully encodes every constraint for a workout
- Format: `ORDER AXIS TYPE COLOR` (e.g., `⛽🏛🪡🔵`)
- Numeric alias: 4-digit string (e.g., `2123`) for database/URL/API use
- Deck derivation: `deck = (order_position - 1) * 6 + axis_position`
- Examples: `cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Bent-Over Barbell Row — Back Strength Log.md`

**The Card:**
- Purpose: One zip code instantiated as a fully-specified workout document
- Stub format: `[zip]±.md`
- Complete format: `[zip]±[operator-emoji] [Title].md`
- The `±` is the semantic hinge — left is machine-readable address, right is human-readable title
- The operator emoji bridges address to title

**The Deck:**
- Purpose: Collection of 40 cards sharing the same Order × Axis combination
- 42 decks total: 7 Orders × 6 Axes
- Each deck contains 5 Types × 8 Colors = 40 cards
- Identity document at `deck-identities/deck-[XX]-identity.md` specifies the exercise mapping for all 40 cards before generation begins

**The Operator:**
- Purpose: Post-zip Latin-derived verb that sets session intent
- Derived from: Axis × Color polarity (preparatory vs. expressive colors)
- 12 operators + 1 system operator (🧮 SAVE)
- Bridge between machine-readable address and human-readable session character

**The Block:**
- Purpose: Named session container; 22 blocks across 4 functional roles (Orientation, Access, Transformation, Retention)
- Name is fixed; content is entirely context-dependent from zip code
- Block sequence guidelines exist per Order (e.g., ⛽ Strength: `♨️ ▶️ 🧈 🧩 🪫 🚂`)

## Entry Points

**Session Start (Human):**
- Location: `whiteboard.md` (the Negotiosum)
- Triggers: Every generation session begins here
- Responsibilities: Identifies current active deck, open tasks, session instructions

**Card Generation (Agent Skill):**
- Location: `.claude/skills/generate-card/SKILL.md`
- Triggers: `/generate-card ⛽🌹🛒🔵` or similar invocation
- Responsibilities: Full 10-step pipeline from zip code to validated, renamed, logged card file

**Validation (Script):**
- Location: `scripts/validate-card.py`
- Triggers: PostToolUse hook on any edit to `cards/` directory; manual invocation
- Responsibilities: Structural and SCL-rule validation of a single card

**Progress Dashboard (Script):**
- Location: `scripts/progress-report.py`
- Triggers: SessionStart hook; manual invocation
- Responsibilities: Scan all card files, count by status, output generation progress

**Cross-Project Routing (Archideck):**
- Location: `archideck/CONTRACTS.md` (the Negotiosum switchboard)
- Triggers: Any session beginning involving multiple projects
- Responsibilities: Identifies active contracts across PPL±, Graph Parti, Story Engine, Civic Atlas

## Error Handling

**Strategy:** Fail-and-flag. Validation scripts exit non-zero and print specific failures. The generation agent must fix and re-run before proceeding. No silent failures.

**Patterns:**
- Validation script exits 1 with named failures (frontmatter missing, block count out of range, GOLD violation)
- The PostToolUse hook fires automatically after every card edit; validation failures are surfaced immediately
- Deck identity documents pre-specify correct primary exercises to prevent duplicate primary exercise violations before they occur
- Cards marked `REGEN-NEEDED` in deck identity coverage maps flag known incorrect content requiring replacement

## Cross-Cutting Concerns

**Constraint Hierarchy:** Applied at generation time, enforced at validation time. Order > Color > Axis > Equipment. Hard constraints (GOLD gate, barbell exclusions) are binary. Soft constraints (Axis bias) are ranking preferences.

**Tonal Rules:** Applied throughout all card content. Direct, technical, human. No motivational filler. No clinical language. Enforced via tonal rules in `CLAUDE.md` and checked implicitly during generation.

**Zip Code Uniqueness:** Each of 1,680 zip codes maps to exactly one card with a distinct primary exercise. Color variants of the same Type must use different primary exercises. The deck identity document enforces this before generation begins.

**Naming Convention:** `deck-identities/naming-convention.md` specifies card title format. No "The" prefix. No banned words (Protocol, Prescription, System, Routine). Phone-book style: `[Movement/Equipment] — [Muscle/Focus, Context]`.

---

## SCL Subsystem Zip Map

Every major subsystem has a partial zip-code address in the Kernel grammar (Order · Type/Modifier · Color). These addresses locate each subsystem within the 1,680-node navigation graph and the Archideck meta-layer.

| Subsystem | SCL Zip | Rationale |
|-----------|---------|-----------|
| SCL Kernel | 🐂 🏛 🔵 | Tuscan (define/init) + Firmitas (structure) + Structured (systematic) |
| Card Generation Pipeline | 🦋 🤌 🟢 | Ionic (iterate/build) + facio (execute/create) + Growth (self-contained) |
| Exercise Library | 🐂 🏛 ⚫ | Tuscan (define) + Firmitas (structure) + Teaching (complete reference) |
| Operis Editorial Pipeline | 🏟 ⌛ 🔵 | Corinthian (execute/output) + Temporitas (time-based) + Structured |
| Cosmogram System | 🐂 🌹 🟣 | Tuscan (define) + Venustas (beauty/identity) + Technical (precision) |
| Weight Vector Engine | ⚖ 🏛 ⚫ | Vitruvian (calibrate/balance) + Firmitas (structure) + Teaching |
| Navigation Graph | ⚖ 🐬 ⚫ | Vitruvian (calibrate) + Sociatas (connections/edges) + Teaching |
| Bloom Engine | ⚖ 🏛 🟢 | Vitruvian (calibrate) + Firmitas (structure) + Growth (active) |
| HTML Experience Layer | 🖼 🌹 🟡 | Palladian (experience/view) + Venustas (feel/aesthetic) + Fun (exploratory) |
| GSD Orchestration | 🌾 🏛 🔵 | Composite (integrate/combine) + Firmitas (structure) + Structured |
| Archideck Meta-Layer | 🐂 🏛 ⚪ | Tuscan (define) + Firmitas (structure) + Mindful (clear/authoritative) |
| Validation Pipeline | ⛽ 🏛 🔵 | Doric (validate/verify) + Firmitas (structure) + Structured |

**Zip grammar note:** These use Kernel grammar (Order · Axis/Modifier · Color), not PPL± dialect (Order · Axis · Type · Color). Partial zips are valid per KERNEL.md Principle 5.

---

*Architecture analysis: 2026-03-07*
