# Exercise Families Schema

Movement family hierarchy table. One row per family. Exercises reference this table via `family_id` in `exercise_library`.

---

## Table: exercise_families

```sql
CREATE TABLE exercise_families (
  family_id             TEXT PRIMARY KEY,       -- "hip-hinge"
  name                  TEXT NOT NULL,          -- "Hip Hinge"
  description           TEXT,                   -- Brief description of the family
  type_primary          TEXT NOT NULL,          -- Primary SCL Type: "🪡"
  movement_category     TEXT NOT NULL,          -- "pull" | "push" | "squat" | "hinge" | "carry" | "conditioning" | "isolation"
  root_exercise_id      TEXT REFERENCES exercise_library(exercise_id),
  created_at            TIMESTAMP DEFAULT NOW()
);
```

---

## Example Rows

```sql
INSERT INTO exercise_families VALUES
  ('hip-hinge',        'Hip Hinge',          'Hip-dominant pulling patterns. Deadlifts, RDLs, good mornings.', '🪡', 'hinge',        'barbell-deadlift',     NOW()),
  ('squat',            'Squat',              'Knee-dominant quad/glute patterns. Back squat, front squat, split squat.', '🍗', 'squat',        'barbell-back-squat',   NOW()),
  ('horizontal-press', 'Horizontal Press',   'Horizontal pushing patterns. Bench press, push-up, flye.',     '🛒', 'push',         'barbell-bench-press',  NOW()),
  ('vertical-press',   'Vertical Press',     'Vertical pushing patterns. Overhead press, push press.',       '🛒', 'push',         'barbell-overhead-press', NOW()),
  ('horizontal-pull',  'Horizontal Pull',    'Horizontal pulling patterns. Rows, face pulls.',                '🪡', 'pull',         'barbell-bent-over-row', NOW()),
  ('vertical-pull',    'Vertical Pull',      'Vertical pulling patterns. Pull-ups, pulldowns.',               '🪡', 'pull',         'weighted-pull-up',     NOW()),
  ('isolation-curl',   'Isolation Curl',     'Elbow flexion isolation. Curl variations.',                    '🪡', 'isolation',    'barbell-curl',         NOW()),
  ('isolation-ext',    'Isolation Extension','Elbow extension isolation. Tricep variations.',                 '🛒', 'isolation',    'close-grip-bench-press', NOW());
```

---

## Relationship to exercise_library

```
exercise_families
  family_id (PK)
      ↑
exercise_library
  family_id (FK)
  parent_exercise_id (FK → exercise_library.exercise_id)
  family_role: "root" | "variant" | "progression" | "regression" | "equipment-swap"
  transfer_ratio: 0.00-1.20
```

The root exercise in each family has `parent_exercise_id = NULL` and `family_role = "root"`. All other exercises in the family have a parent and a transfer ratio.

---

🧮
