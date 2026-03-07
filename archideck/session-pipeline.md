# Session Pipeline — Zip-Routed Execution Loop

The daily session contract. Any Claude Code agent picks this up, reads it, and knows exactly what to do.

---

## Overview

Every session is a zip-routed operation. The active contract's zip determines which context to load and which tools to use. No freelancing. No context bloat from irrelevant subsystems.

```
SESSION START
├─ Read archideck/CONTRACTS.md           → identify ACTIVE contract + zip
├─ Read whiteboard.md                    → identify specific next physical action
│
├─ ROUTE on contract zip (Order position)
│   ├─ 🦋 Ionic   → Card Generation pipeline
│   ├─ 🏟 Corinthian → Operis pipeline
│   ├─ 🐂 Tuscan  → Architecture / Kernel work
│   ├─ ⚖ Vitruvian → Middle-math / calibration
│   └─ 🖼 Palladian → HTML / Experience layer
│
├─ EXECUTE (Order-specific context loaded, tools invoked)
│
├─ UPDATE STATE
│   ├─ Update whiteboard.md next-action
│   └─ Update archideck/CONTRACTS.md if contract status changed
│
└─ SESSION END
    └─ 🧮 SAVE
```

---

## Session Start Sequence (every session)

1. Read `archideck/KERNEL.md` — language ground floor
2. Read `archideck/AGENT-CONTRACT.md` — session protocol
3. Read `archideck/CONTRACTS.md` — identify ACTIVE contract and its zip
4. Read `whiteboard.md` — specific next physical action
5. ROUTE on zip → load Order-specific context (see routes below)

---

## Route: 🦋 Ionic — Card Generation

**Contract zip Order = 🦋 (Ionic/Hypertrophy → iterate, build, accumulate)**

Context to load:
- `CLAUDE.md` (root) — generation law
- `scl-directory.md` — full SCL spec
- `exercise-library.md` — exercise authority (Type-specific sections only)
- `deck-identities/deck-[NN]-identity.md` — deck exercise map
- `deck-cosmograms/deck-[NN]-cosmogram-v2.md` — deck identity (if populated)

Tools to use:
- `/generate-card [zip]` — full single-card pipeline
- `card-generator` subagent — isolated context card generation (preferred for main-context preservation)
- `python scripts/validate-card.py [path]` — post-generation validation
- `python scripts/audit-exercise-coverage.py [deck-folder]` — duplicate check

Session end:
- Log completed zip codes to `whiteboard.md`
- Update `archideck/CONTRACTS.md` progress field

**Example zip:** 🦋 🤌 🟢 — building cards in the Growth (bodyweight) color

---

## Route: 🏟 Corinthian — Operis Pipeline

**Contract zip Order = 🏟 (Corinthian/Performance → execute, run, output)**

Context to load:
- `seeds/operis-architecture.md` — editorial structure
- `seeds/operis-prompt-pipeline.md` — 4-prompt pipeline spec
- `scl-deep/publication-standard.md` — content quality standard
- `scl-deep/vocabulary-standard.md` — language rules

Pipeline sequence:
1. Prompt 1 (Researcher): date → Research Brief (Contract A)
2. Prompt 2 (Content Architect): Contract A → Enriched Brief (Contract B)
3. Prompt 3 (Editor): A + B → Full Operis edition (Contract C)
4. Prompt 4 (Builder): Contract C → proofed edition + card generation

Prerequisites before running:
- Historical events database has entries for the target date (`operis-editions/historical-events/[MM-DD].md`)
- Cosmogram v2 exists and is researched for the featured zip's deck
- URL enforcement is patched in Prompts 1 and 2

Session end:
- Commit edition to `operis-editions/[YYYY]/[MM]/[YYYY-MM-DD].md`
- Log date to `whiteboard.md`

**Example zip:** 🏟 ⌛ 🔵 — running the Operis pipeline on a structured schedule

---

## Route: 🐂 Tuscan — Architecture / Kernel Work

**Contract zip Order = 🐂 (Tuscan/Foundation → init, declare, define, setup)**

Context to load:
- `archideck/KERNEL.md` — SCL grammar (authoritative)
- `archideck/CONTRACTS.md` — current contract state
- Relevant `seeds/` document for the specific architecture work
- `scl-deep/systems-glossary.md` — systems language

Tasks in this route:
- Seed writing and planting
- Kernel updates (require explicit session scope — do not update during card generation)
- Contract drafting and updating
- Deck identity document creation (`/build-deck-identity [N]`)
- GSD milestone scaffolding

Kernel rule: Changes to `archideck/KERNEL.md` require explicit session scope statement. Do not update KERNEL.md while generating cards. The kernel is the language — not the implementation.

Session end:
- Update relevant seed files
- Update `archideck/CONTRACTS.md` if new contracts added
- Log to `whiteboard.md`

**Example zip:** 🐂 🏛 🔵 — defining/structuring something systematically

---

## Route: ⚖ Vitruvian — Middle-Math / Calibration

**Contract zip Order = ⚖ (Vitruvian/Balance → calibrate, balance, correct)**

Context to load:
- `middle-math/ARCHITECTURE.md` — engine overview
- `middle-math/weight-vectors.json` — existing weight vectors
- `middle-math/navigation-graph.json` — 1,680-node graph
- Specific subdirectory for the task (weights/, schemas/, rotation/, etc.)

Tasks in this route:
- Weight declaration refinement (`middle-math/weights/*.md`)
- Schema updates (`middle-math/schemas/*.md`)
- Rotation engine work (`middle-math/rotation/*.md`)
- Running weight vector rebuild: `python scripts/middle-math/weight_vector.py`
- Running zip registry: `python scripts/middle-math/zip_registry.py`

Validation:
- `python scripts/middle-math/weight_vector.py --validate` — structure check
- `python scripts/middle-math/zip_registry.py` — 1,680-zip coverage test

Session end:
- Commit updated JSON outputs if rebuilt
- Document changes to weight declarations
- Log to `whiteboard.md`

**Example zip:** ⚖ 🏛 🟣 — calibrating structure with technical precision

---

## Route: 🖼 Palladian — HTML / Experience Layer

**Contract zip Order = 🖼 (Palladian/Restoration → experience, view, render)**

Context to load:
- `seeds/experience-layer-blueprint.md` — master tech architecture
- `seeds/mobile-ui-architecture.md` — 4-dial UI spec
- `seeds/stripe-integration-pipeline.md` — payment spec
- `middle-math/schemas/zip-metadata-schema.md` — database schema
- `seeds/claude-code-build-sequence.md` — 20-session build plan

Development conventions:
- Next.js App Router
- Supabase for auth and database
- Vercel for deployment
- CHAR(4) numeric zip as database primary key
- `/zip/[numeric]` as URL pattern

Session end:
- Commit working code
- Update build sequence progress in `seeds/claude-code-build-sequence.md`
- Log to `whiteboard.md`

**Example zip:** 🖼 🌹 🟢 — building the experience layer (Growth = self-contained, runnable)

---

## Unmapped Orders (extend as contracts activate)

| Order | Kernel Name | Posture | Activate When |
|-------|------------|---------|--------------|
| ⛽ Doric | validate, verify | Validation sweeps, deck audits, linting, CI | Linters CI Pipeline contract activates |
| 🌾 Composite | integrate, merge | Cross-system wiring, GSD orchestration, navigation graph updates | Ralph Loop batch orchestrator activates |

---

## State Management

### Update whiteboard.md at session end

```
In the active color section (e.g., 🔴 Fervor for card generation):
- Change ACTIVE → DONE for the current task
- Add completion note in Note column
- Update next-action row if work continues
```

### Update CONTRACTS.md if contract status changes

```
ACTIVE → COMPLETED: verify deliverable, note date, move section
QUEUED → ACTIVE: state it explicitly, confirm blocker resolved
ACTIVE → PARKED: acknowledge explicitly, state reason
```

### The 🧮 SAVE principle

Every session ends with a closing action that transfers the work:
- Commit the files changed
- Push to the active branch
- Update the whiteboard next-action so the next session knows exactly where to pick up

No session ends with uncommitted work or a whiteboard that says "in progress" with no next step.

---

## Context Load by Order (summary table)

| Order | ZIP | Load | Tools |
|-------|-----|------|-------|
| 🦋 Ionic | 🦋 🤌 🟢 | CLAUDE.md + scl-dir + exercise-lib + deck identity | /generate-card, card-generator subagent, validate-card.py |
| 🏟 Corinthian | 🏟 ⌛ 🔵 | operis-architecture + publication-standard + vocabulary-standard | 4-prompt pipeline, Genspark, operis-builder |
| 🐂 Tuscan | 🐂 🏛 🔵 | KERNEL.md + CONTRACTS.md + relevant seed | seed writing, /build-deck-identity, GSD commands |
| ⚖ Vitruvian | ⚖ 🏛 🟣 | middle-math ARCHITECTURE + weight-vectors + navigation-graph | weight_vector.py, zip_registry.py |
| 🖼 Palladian | 🖼 🌹 🟢 | experience-layer-blueprint + mobile-ui + stripe-integration | Next.js, Supabase, Vercel, Stripe |

---

🧮
