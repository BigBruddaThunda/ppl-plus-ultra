# Codex Next-Round Handoff Brief (Post-Reconciliation — 2026-03-05)

Use this as the copy/paste kickoff brief for the next Codex container run.

## 1) Assumed Done (do not redo)

**Session 031 Tasks A–C** are complete. The reconciliation session (2026-03-05) also completed:

- `.codex/TASK-ARCHITECTURE.md`: Status/Completed In/Evidence columns populated.
  13 containers marked DONE with commit hashes and evidence paths.
- `.codex/HANDOFF-CONTRACTS.md`: closure fields enforced (from Session 031 Task B).
- `whiteboard.md`: Negotiosum reflects merged reality. CX-09, CX-10, CX-16 → DONE.
  Header updated to 13 complete, 19 open.
- `CLAUDE.md`: Updated to 102/1,680 cards across 3 decks (Decks 07, 08, 09).
- `README.md`: Updated to 102/1,680, repo structure includes sql/, session-log.md, licenses.
- `session-log.md`: Reconciliation note appended covering PRs #27–#84 unlogged burst.
- `NEXT-ROUND-HANDOFF.md`: This file — replaced with post-reconciliation brief.

Containers now marked DONE in TASK-ARCHITECTURE.md:
CX-00A, CX-00B, CX-02, CX-03, CX-04, CX-05, CX-06, CX-07, CX-08, CX-09, CX-10, CX-13, CX-16

## 2) Current State

- Cards: 102/1,680 (Deck 07: 22/40 ⚠️ — 18 REGEN-NEEDED, Deck 08: 40/40 ✅, Deck 09: 40/40 ✅)
- CX Containers: 32 defined, 13 complete, 19 open
- Wave 1: COMPLETE (except CX-01 — unblocked, not yet executed)
- Wave 2: 5 DONE (CX-07, CX-09, CX-10, CX-13, CX-16), 8 OPEN (7 unblocked, 1 blocked on CX-01)
- Wave 3: 0 DONE, CX-11 and CX-12 newly unblocked (CX-09, CX-10 done)
- Critical path: CX-11 → CX-12 → CX-14 → CX-15

## 3) Recommended Next Tasks (priority order)

### Task A — CX-11 Block Weight Declarations

**Status:** Now unblocked (CX-09 ✓, CX-10 ✓).

Write: `middle-math/weights/block-weights.md`

Content: 22 blocks + SAVE (🧮). Each block needs weight parameters per Order context.
The block-weights.md declares how each block contributes to session structure scoring.

Reads before writing:
- `scl-deep/block-specifications.md`
- `middle-math/weights/axis-weights.md` (pattern reference)
- `middle-math/weights/order-weights.md` (pattern reference)

---

### Task B — CX-12 Operator Weight Declarations

**Status:** Now unblocked (CX-09 ✓, CX-10 ✓). Can run in parallel with Task A.

Write: `middle-math/weights/operator-weights.md`

Content: 12 operators. Each needs weight vector contribution parameters.

Reads before writing:
- Operator table in `CLAUDE.md`
- `middle-math/weights/axis-weights.md` (pattern reference)

---

### Task C — CX-20 Room Schema Extension

**Status:** Now unblocked (CX-08 ✓).

Write: `sql/008-room-schema-extension.sql`

Content: Adds floors, bloom state, votes, navigation edges to the existing schema.

Reads before writing:
- `sql/001` through `sql/007`
- `middle-math/schemas/` (any existing schema specs)
- `seeds/experience-layer-blueprint.md` (floor model)

---

### Task D — CX-23 Navigation Graph Builder

**Status:** Now unblocked (CX-03 ✓, CX-04 ✓, CX-08 ✓). All dependencies met.

Write: `middle-math/navigation-graph.json` or `scripts/build-navigation-graph.py`

Content: 1,680 nodes × 4 directional edges. Order↑↓, Axis↑↓ neighbors per node.

Reads before writing:
- `zip-web/zip-web-rules.md`
- `middle-math/zip-registry.json`

---

### Task E — CX-01 Codex Agent Task Architecture (housekeeping)

**Status:** Still OPEN. Blocker CX-00A is ✓. Low urgency — TASK-ARCHITECTURE.md already functional.

Write: finalize `.codex/HANDOFF-CONTRACTS.md` structure, `.codex/TASK-ARCHITECTURE.md` any remaining gaps.

---

## 4) Do NOT touch

- Card content in `cards/`
- Operis editions (except `operis-editions/historical-events/` scaffolds)
- `scl-directory.md`, `exercise-library.md`
- Any seed file marked "Jake-blocked" in whiteboard Notes
- Files requiring live web research

## 5) Definition of Done

- CX-11 and CX-12 both written as DRAFT with full block/operator weight tables.
- CX-20 sql/008 migration written.
- CX-23 navigation graph artifact produced (JSON or script).
- All completed containers marked DONE in TASK-ARCHITECTURE.md with commit + evidence.
- whiteboard.md updated to reflect new completions.
- No regressions in `scripts/run-full-audit.sh` (baseline mode).

## 6) Kickoff Prompt (copy/paste)

"Use `.codex/NEXT-ROUND-HANDOFF.md` as source of truth for this session.
All items in Section 1 are assumed done and merged.
Execute Task A (CX-11) and Task B (CX-12) in parallel if possible, then Task C (CX-20).
Do not regenerate card content.
Commit once with a single focused PR.
Update whiteboard.md and TASK-ARCHITECTURE.md container rows before closing."
