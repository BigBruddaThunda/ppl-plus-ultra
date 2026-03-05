# Codex Next-Round Handoff Brief (Post Engine Coupling Session — 2026-03-05)

Use this as the copy/paste kickoff brief for the next Codex container run.

## 1) What Just Landed

Engine coupling session (2026-03-05) completed the following:

- **CX-11 Block Weight Declarations** — DONE · `middle-math/weights/block-weights.md` (790-line working draft, confirmed on disk from prior run)
- **CX-12 Operator Weight Declarations** — DONE · `middle-math/weights/operator-weights.md` (502-line working draft, confirmed on disk from prior run)
- **CX-20 Room Schema Extension** — DONE · `sql/008-room-schema-extension.sql` — 4 tables (rooms, room_visits, room_votes, bloom_history), RLS policies, indexes, 1,680-row population
- **CX-23 Navigation Graph Builder** — DONE · `scripts/build-navigation-graph.py` + `middle-math/navigation-graph.json` — 1,680 nodes × 4 edges = 6,720 directional edges, all passing Type Exclusion Rule validation
- **CX-33 Progress Dashboard** — DONE · `scripts/build-dashboard-data.py` + `docs/dashboard/index.html` + `docs/dashboard/data/progress.json`
- **CX-32 Mermaid Dependency Graph** — DONE (prior run, registered this session)
- **CX-34 Codespaces Dev Container** — DONE (prior run, registered this session)
- **CX-35 Negotiosum Validator** — DONE (prior run, registered this session)

All registrations committed to:
- `.codex/TASK-ARCHITECTURE.md` — CX-32 through CX-35 added, CX-11 and CX-12 marked DONE
- `whiteboard.md` — header updated to 36 defined / 16 complete / 20 open
- `docs/cx-dependency-graph.md` — 4 new nodes, 2 status updates, summary updated
- `docs/README.md` — expanded from stub to proper index

## 2) Current State

- Cards: 102/1,680 (Deck 07: 22/40 ⚠️ — 18 REGEN-NEEDED, Deck 08: 40/40 ✅, Deck 09: 40/40 ✅)
- CX Containers: 36 defined, 16 complete (+ CX-33 if built), 20 open
- Wave 3: CX-11 ✅, CX-12 ✅ — **CX-14 now fully unblocked**
- Wave 2: CX-20 ✅, CX-23 ✅ — CX-24 and CX-27 newly unblocked
- Critical path: **CX-14 → CX-15**

## 3) Recommended Next Tasks (priority order)

### Task A — CX-14 Weight Vector Computation Engine (CRITICAL PATH)

**Status:** Newly unblocked. All 5 dependencies met: CX-09 ✓, CX-10 ✓, CX-11 ✓, CX-12 ✓, CX-03 ✓.

Write: `scripts/middle-math/weight_vector.py`

Content: For each zip code (1,680), compute a multi-dimensional weight vector from
all 5 weight declaration files. The vector encodes the zip's complete training identity
as a numeric representation for exercise selection.

Reads before writing:
- `middle-math/weights/order-weights.md`
- `middle-math/weights/axis-weights.md`
- `middle-math/weights/type-weights.md`
- `middle-math/weights/color-weights.md`
- `middle-math/weights/block-weights.md`
- `middle-math/weights/operator-weights.md`
- `middle-math/ARCHITECTURE.md` (weight system section)
- `middle-math/zip-registry.json` (all 1,680 zips)

---

### Task B — CX-21 Content Type Registry

**Status:** Unblocked (CX-00A ✓). Lightweight but unblocks CX-22 Floor Routing.

Write: `middle-math/content-type-registry.json`

Content: 109 content types from seeds/content-types-architecture.md → structured JSON.

Reads before writing:
- `seeds/content-types-architecture.md`
- `seeds/axis-as-app-floors-architecture.md` (if exists)

---

### Task C — CX-24 Bloom State Engine

**Status:** Newly unblocked (CX-20 ✓, CX-03 ✓).

Write: `scripts/middle-math/bloom_engine.py`

Content: Computes bloom level transitions from room_visits history.
Bloom = depth of engagement, not gamification (see seeds/systems-eudaimonics.md).

Reads before writing:
- `sql/008-room-schema-extension.sql` (bloom_history schema)
- `seeds/systems-eudaimonics.md`
- `middle-math/zip-registry.json`

---

### Task D — CX-28 Cosmogram Content Scaffold (lightweight)

**Status:** Unblocked (CX-04 ✓). Low effort — scaffolds 42 stub files.

Write: `scripts/scaffold_cosmograms.py`
Run: creates `deck-cosmograms/deck-01-cosmogram.md` through `deck-cosmograms/deck-42-cosmogram.md`

Reads before writing:
- `deck-cosmograms/README.md`
- `scl-deep/publication-standard.md`
- `seeds/cosmogram-research-prompt.md`

---

## 4) Jake-Blocked Items (do not touch)

- platform-v1-archive body paste (~15k words)
- color-context-vernacular vocabulary update (25→61 emojis)
- order-parameters vocabulary update
- Deck 07 regen decision (18 REGEN-NEEDED cards)
- Deck 07 Ralph pod review approval
- First CANONICAL review (Deck 08 gemba test)

## 5) Do NOT Touch

- Card content in `cards/`
- Operis editions (except `operis-editions/historical-events/` scaffolds)
- `scl-directory.md`, `exercise-library.md`
- Any seed file marked "Jake-blocked" in whiteboard Notes
- Files requiring live web research to populate

## 6) Definition of Done (next session)

- CX-14 weight_vector.py written and computing vectors for all 1,680 zips
- CX-21 content-type-registry.json populated with 109 entries
- All completed containers marked DONE in TASK-ARCHITECTURE.md with commit + evidence
- whiteboard.md updated to reflect new completions
- validate-negotiosum.py passes with no mismatches

## 7) Kickoff Prompt (copy/paste)

"Use `.codex/NEXT-ROUND-HANDOFF.md` as source of truth for this session.
All items in Section 1 are assumed done and merged.
Execute Task A (CX-14) as highest priority — all blockers are now met.
Task B (CX-21) can run in parallel.
Do not regenerate card content.
Commit once with a focused PR.
Update whiteboard.md and TASK-ARCHITECTURE.md before closing."
