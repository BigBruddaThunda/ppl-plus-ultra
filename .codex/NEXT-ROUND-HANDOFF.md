# Codex Next-Round Handoff Brief (Post Critical Path Reconciliation — 2026-03-06)

Use this as the copy/paste kickoff brief for the next Codex container run.

## 1) What Just Landed

Critical path reconciliation session (2026-03-06) completed the following:

- **CX-33 reconciled** — Progress Dashboard (PR #90, 2026-03-05) registered as DONE. Stale tracking corrected.
- **CX-14 Weight Vector Computation Engine** — DONE · `scripts/middle-math/weight_vector.py` + `middle-math/weight-vectors.json` — 1,680 vectors, 61 dimensions, octave scale [-8,+8], --validate passes, hard suppression rules enforced
- **CX-21 Content Type Registry** — DONE · `middle-math/content-type-registry.json` — 109 types across 6 axes, cross-floor appearances, operator affinities
- **CX-28 Cosmogram Content Scaffold** — DONE · `scripts/scaffold_cosmograms.py` + 42 stub files in `deck-cosmograms/deck-01-cosmogram.md` through `deck-cosmograms/deck-42-cosmogram.md`
- **CLAUDE.md corrected** — Card count: 80/1,680 → 102/1,680

All registrations committed to:
- `.codex/TASK-ARCHITECTURE.md` — CX-14, CX-21, CX-28 marked DONE; Wave 4 cascade table added
- `whiteboard.md` — header: 21 complete, 15 open; cascade notes appended
- `docs/cx-dependency-graph.md` — CX14, CX21, CX28 added to done class; summary updated 21/36
- `session-log.md` — Session 034 entry appended
- `docs/dashboard/data/progress.json` — rebuilt

## 2) Current State

- Cards: 102/1,680 (Deck 07: 22/40 ⚠️ — 18 REGEN-NEEDED, Deck 08: 40/40 ✅, Deck 09: 40/40 ✅)
- CX Containers: 36 defined, 21 complete, 15 open
- Critical path: **CX-15 → CX-29** (CX-15 fully unblocked: CX-13 ✓, CX-14 ✓)
- Wave 4 newly unblocked: CX-15, CX-22, CX-25, CX-30

## 3) Recommended Next Tasks (priority order)

### Task A — CX-15 Exercise Selection Prototype (CRITICAL PATH)

**Status:** Fully unblocked (CX-13 ✓, CX-14 ✓).

Write: `scripts/middle-math/exercise_selector.py`

Content: Given a zip code, produce a ranked exercise list using weight vectors + exercise library JSON.
The selector is the engine that automates card generation at scale.

Reads before writing:
- `middle-math/weights/weight-system-spec.md`
- `middle-math/weight-vectors.json` (1,680 entries)
- `middle-math/exercise-library.json` (from CX-13)
- `scripts/middle-math/weight_vector.py` (reuse emoji/numeric conversion)
- `middle-math/ARCHITECTURE.md`

---

### Task B — CX-22 Floor Routing Spec

**Status:** Fully unblocked (CX-03 ✓, CX-20 ✓, CX-21 ✓).

Write: `middle-math/floor-routing-spec.md`

Content: Routing rules for each Axis as an app floor. Which content types appear on which floor.
Cross-floor appearance logic. Navigation between floors.

Reads before writing:
- `middle-math/content-type-registry.json` (CX-21 output)
- `seeds/axis-as-app-floors-architecture.md` (if exists)
- `seeds/elevator-architecture.md`
- `seeds/content-types-architecture.md`

---

### Task C — CX-24 Bloom State Engine

**Status:** Unblocked (CX-20 ✓, CX-03 ✓).

Write: `scripts/middle-math/bloom_engine.py`

Content: Computes bloom level transitions from room_visits history.
Bloom = depth of engagement, not gamification.

Reads before writing:
- `sql/008-room-schema-extension.sql` (bloom_history schema)
- `seeds/systems-eudaimonics.md`
- `middle-math/zip-registry.json`

---

### Task D — CX-30 Envelope Schema + Stamping Prototype

**Status:** Fully unblocked (CX-08 ✓, CX-14 ✓, CX-03 ✓).

Write: `scripts/middle-math/envelope_stamper.py`

Content: Schema and stamping logic for SCL envelopes. Reads zip + vector, stamps envelope metadata.

Reads before writing:
- `seeds/scl-envelope-architecture.md`
- `middle-math/weight-vectors.json` (CX-14 output)
- `middle-math/zip-registry.json`

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
- Cosmogram stubs (status: STUB — awaiting Jake-directed research population)

## 6) Definition of Done (next session)

- CX-15 exercise_selector.py written and producing ranked lists for sample zip codes
- At least one of CX-22, CX-24, or CX-30 completed
- All completed containers marked DONE in TASK-ARCHITECTURE.md with evidence
- whiteboard.md header updated
- validate-negotiosum.py passes with no mismatches

## 7) Kickoff Prompt (copy/paste)

"Use `.codex/NEXT-ROUND-HANDOFF.md` as source of truth for this session.
All items in Section 1 are assumed done and merged.
Execute Task A (CX-15) as highest priority — all blockers are met.
Task B (CX-22) is the next most valuable unlock.
Do not regenerate card content. Do not populate cosmogram stubs.
Commit once with a focused PR.
Update whiteboard.md and TASK-ARCHITECTURE.md before closing."
