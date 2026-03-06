# exercise-content/

Coaching knowledge files for every exercise in the PPL± registry.
One `.md` file per exercise. 1:1 with `middle-math/exercise-registry.json`.

## Structure

```
exercise-content/
├── push/      — 🛒 Push exercises (Chest, Shoulders, Triceps)
├── pull/      — 🪡 Pull exercises (Back, Biceps, Rear Delts)
├── legs/      — 🍗 Legs exercises (Quads, Hamstrings, Glutes, Calves)
├── plus/      — ➕ Plus exercises (Olympic, Plyometric, Carries, Core)
└── ultra/     — ➖ Ultra exercises (Conditioning, Cardio, Agility)
```

## File Naming

`{slug}.md` where slug = exercise name lowercased, spaces → hyphens,
parentheses and special characters removed.

Example: `Barbell Bench Press` → `barbell-bench-press.md`

## Status Lifecycle

```
EMPTY → GENERATED → REVIEWED → CANONICAL
```

- `EMPTY` — stub row in `exercise_knowledge` table, no file written
- `GENERATED` — file written by `scripts/generate-exercise-content.py`
- `REVIEWED` — manually reviewed for accuracy and PPL± voice
- `CANONICAL` — locked version, master reference

## File Format

Each file contains:
1. YAML frontmatter (exercise_id, name, type, movement_pattern, status, generated)
2. `## What It Is` — 2-3 sentence overview
3. `## Setup` — ordered setup cues (3-6 items)
4. `## Execution` — ordered execution cues (4-8 items)
5. `## Common Faults` — fault/correction pairs (3-5 faults)
6. `## What It Trains` — primary movers, secondary movers, joint actions
7. `## PPL± Context` — per-Order behavior + Color modifiers
8. `## Family` — pattern, role, regressions, progressions, equipment swaps
9. `## Coaching Notes` — PPL± voice paragraph

## Generation

```bash
# Single exercise by ID
python scripts/generate-exercise-content.py --exercise EX-0001

# All exercises of a type
python scripts/generate-exercise-content.py --type Pull

# First 200 by priority
python scripts/generate-exercise-content.py --batch 200 --priority-first

# Stats
python scripts/generate-exercise-content.py --stats
```

## Population Progress

Initial batch (CX-37): first 200 files generated with priority weighting.
Remaining batches: CX-41 (201-500), CX-42 (501-1000), beyond via CX-43.

Source: `middle-math/exercise-registry.json`
Family data: `middle-math/exercise-engine/family-trees.json`
Populated into: `exercise_knowledge` table via `sql/010-exercise-knowledge.sql`
