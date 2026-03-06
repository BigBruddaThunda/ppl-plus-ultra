# Next Round Handoff — Post Session 038

**Date:** 2026-03-06
**Branch closed:** `claude/exercise-library-expansion-LWTl5`
**State:** 38/44 CX containers complete. Wave 6 (Exercise Library Foundation) delivered.

---

## What Was Completed This Session

### CX-36 — Exercise Identity Registry
- `scripts/build-exercise-registry.py` — Full build script for registry
- `middle-math/exercise-registry.json` — 2,085 exercises, EX-0001–EX-2085, globally unique IDs
- Each entry: anatomy (primary/secondary/stabilizers/joint_actions), standardized movement_pattern (16-pattern vocab), family linkage (family_id/family_role/parent_id/transfer_ratio), axis_affinity + order_affinity (octave scale -8/+8), equipment[], sport_tags[], knowledge_file path

### CX-39 — External Reference Dock
- `middle-math/exercise-engine/external-refs.json` — 2,085 null ExRx/video/research docks
- `seeds/exrx-partnership-brief.md` — Partnership pitch for ExRx.net URL mapping

### CX-40 — Exercise Registry SQL Migrations
- `sql/009-exercise-registry.sql` — `exercise_registry` table (TEXT PK, self-ref FK, RLS, 8 indexes)
- `sql/010-exercise-knowledge.sql` — `exercise_knowledge` table (1:1 FK, JSONB coaching content, auto-stub population)
- `sql/README.md` — Updated with migrations 9 and 10

### CX-38 — Exercise Relationship Graph
- `middle-math/exercise-engine/family-trees.json` — 15 families, 2,085 member entries
- `middle-math/exercise-engine/substitution-map.json` — Same-family, tier-up/down, cross-family substitution chains per exercise
- `middle-math/exercise-engine/sport-tags.json` — 20 sports indexed, by_sport and by_exercise maps
- `middle-math/exercise-engine/anatomy-index.json` — 50 muscles + 30 joint actions, inverted primary/secondary/stabilizer index

### CX-37 — Exercise Knowledge Template + First Batch
- `scripts/generate-exercise-content.py` — Full CLI generator (--exercise/--type/--batch/--priority-first/--stats)
- `exercise-content/README.md` — Structure, naming, status lifecycle, generation commands
- `exercise-content/{push,pull,legs,plus,ultra}/` — 197 knowledge files (avg 484 words each)
- Priority-first ordering: top 25 high-frequency exercises (from usage report) generated first

---

## Known Issue: movement_pattern Classification

**Status:** Non-blocking. Logged in whiteboard.md Notes.

The registry builder's `PATTERN_KEYWORDS["core-stability"]` includes `"car"` which substring-matches `"carry"`. Result: ~1,256 exercises show `movement_pattern: "core-stability"` including carries and some other patterns.

**Mitigation in place:** `generate-exercise-content.py` has `resolve_template_pattern()` which uses `family_id` as a fallback when `movement_pattern` is `"core-stability"` but `family_id` is a major pattern (hip-hinge, squat, etc.). This gives correct PPL± Context templates to affected exercises.

**Full fix:** Rebuild the registry with corrected `PATTERN_KEYWORDS`. Deferred to CX-43 (Selector V2) or a targeted CX-36 patch session.

---

## Current Open Containers

| Container | Blocker | Priority |
|-----------|---------|----------|
| CX-41 | CX-37 ✓ (unblocked) | Next batch: `python scripts/generate-exercise-content.py --batch 500 --overwrite` |
| CX-42 | CX-41 | After CX-41 |
| CX-43 | CX-36 ✓, CX-38 ✓, CX-15 ✓ (all unblocked) | Upgrade exercise_selector.py to use registry |
| CX-17 | Jake pod review | Blocked on Jake |

---

## Next Session Options

**Option A — CX-41: Knowledge Content Batch 2 (exercises 201–500)**
```bash
python scripts/generate-exercise-content.py --batch 500 --overwrite
```
Extends coverage from 9.4% to ~24%. Same generator, same quality.

**Option B — CX-43: Exercise Selector V2**
Upgrade `scripts/middle-math/exercise_selector.py` to query `middle-math/exercise-registry.json` directly (anatomy, family, affinity scores) instead of the flat exercise-library.json. All blockers cleared (CX-36, CX-38, CX-15 done).

**Option C — Deck Generation**
Continue ⛽ Strength sweep: Deck 10 (⛽🪐), Deck 11 (⛽⌛), Deck 12 (⛽🐬). Requires deck identity docs first.

**Option D — movement_pattern registry fix**
Patch `scripts/build-exercise-registry.py` to fix the "car" substring collision and other pattern misclassifications. Rebuild `exercise-registry.json`. This improves CX-38 and CX-37 content quality automatically.

---

## Key File Locations

| Purpose | Path |
|---------|------|
| Exercise registry (source of truth) | `middle-math/exercise-registry.json` |
| Registry builder | `scripts/build-exercise-registry.py` |
| Knowledge generator | `scripts/generate-exercise-content.py` |
| Knowledge files | `exercise-content/{push,pull,legs,plus,ultra}/*.md` |
| Family trees | `middle-math/exercise-engine/family-trees.json` |
| Substitution map | `middle-math/exercise-engine/substitution-map.json` |
| Sport tags | `middle-math/exercise-engine/sport-tags.json` |
| Anatomy index | `middle-math/exercise-engine/anatomy-index.json` |
| External ref dock | `middle-math/exercise-engine/external-refs.json` |
| SQL migrations | `sql/009-exercise-registry.sql`, `sql/010-exercise-knowledge.sql` |
| Active task board | `whiteboard.md` |
| CX container tracking | `.codex/TASK-ARCHITECTURE.md` |

---

## Validation Commands

```bash
# Registry integrity
python scripts/build-exercise-registry.py --validate
python scripts/build-exercise-registry.py --stats

# Knowledge coverage
python scripts/generate-exercise-content.py --stats

# Negotiosum health
python scripts/validate-negotiosum.py

# Dashboard
python scripts/build-dashboard-data.py
```

---

🧮
