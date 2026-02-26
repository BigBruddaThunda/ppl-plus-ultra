# Exercise Library Schema — Enhanced

The existing exercise library (~2,185 exercises across sections A–Q in `exercise-library.md`) extended with weight and family columns for the middle-math computation layer.

---

## Table: exercise_library

```sql
CREATE TABLE exercise_library (
  -- Identity
  exercise_id           TEXT PRIMARY KEY,            -- "barbell-deadlift"
  name                  TEXT NOT NULL,               -- "Barbell Deadlift"
  display_name          TEXT,                        -- Alternate display: "Deadlift (Barbell)"
  section               TEXT NOT NULL,               -- Library section: "G"
  notes                 TEXT,                        -- Free text notes from library

  -- SCL Type mapping
  type_primary          TEXT NOT NULL,               -- "🪡" (primary Type emoji)
  type_secondary        TEXT[],                      -- ["🍗"] (secondary Types, if any)

  -- Movement pattern
  movement_pattern      TEXT NOT NULL,               -- "hip-hinge"
  compound              BOOLEAN NOT NULL DEFAULT true,
  bilateral             BOOLEAN NOT NULL DEFAULT true,

  -- Equipment
  equipment_tier        INTEGER NOT NULL,            -- Minimum tier: 3
  equipment_tier_max    INTEGER,                     -- Maximum tier (if bounded): null = same as min

  -- GOLD gate
  gold_required         BOOLEAN NOT NULL DEFAULT false,  -- Requires 🔴 or 🟣 Color

  -- Weight system columns (JSONB)
  axis_affinity         JSONB NOT NULL DEFAULT '{}',
  -- {"🏛": 8, "🔨": 4, "🌹": 2, "🪐": 6, "⌛": 3, "🐬": 5}
  -- Represents this exercise's natural affinity to each Axis
  -- Derived from exercise character, not zip code context

  order_affinity        JSONB NOT NULL DEFAULT '{}',
  -- {"🐂": 5, "⛽": 8, "🦋": 6, "🏟": 7, "🌾": 4, "⚖": 3, "🖼": -6}
  -- Represents how well this exercise fits each Order's character

  -- Family tree
  family_id             TEXT,                        -- FK → exercise_families.family_id
  family_role           TEXT,                        -- "root" | "variant" | "progression" | "regression" | "equipment-swap"
  parent_exercise_id    TEXT REFERENCES exercise_library(exercise_id),  -- null if root
  transfer_ratio        NUMERIC(4,2),               -- null (root) or 0.85, 0.90, etc.

  -- Metadata
  created_at            TIMESTAMP DEFAULT NOW(),
  updated_at            TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_exercise_library_type_primary ON exercise_library (type_primary);
CREATE INDEX idx_exercise_library_movement_pattern ON exercise_library (movement_pattern);
CREATE INDEX idx_exercise_library_equipment_tier ON exercise_library (equipment_tier);
CREATE INDEX idx_exercise_library_family_id ON exercise_library (family_id);
CREATE INDEX idx_exercise_library_gold_required ON exercise_library (gold_required);
```

---

## Example Rows

```sql
-- Barbell Deadlift
INSERT INTO exercise_library VALUES (
  'barbell-deadlift',
  'Barbell Deadlift',
  'Deadlift (Barbell)',
  'G',
  null,
  '🪡',
  '["🍗"]',  -- secondary: also trains glutes/hamstrings
  'hip-hinge',
  true,  -- compound
  true,  -- bilateral
  3,     -- equipment tier: barbell/rack
  null,
  false, -- not GOLD-gated
  '{"🏛": 8, "🔨": 3, "🌹": 2, "🪐": 6, "⌛": 3, "🐬": 4}',
  '{"🐂": 5, "⛽": 8, "🦋": 6, "🏟": 7, "🌾": 4, "⚖": 3, "🖼": -6}',
  'hip-hinge',
  'root',
  null,   -- no parent
  null,   -- no transfer ratio for root
  NOW(), NOW()
);

-- Romanian Deadlift (child of Barbell Deadlift)
INSERT INTO exercise_library VALUES (
  'romanian-deadlift',
  'Romanian Deadlift',
  null,
  'G',
  null,
  '🪡',
  '["🍗"]',
  'hip-hinge',
  true,
  true,
  3,
  null,
  false,
  '{"🏛": 7, "🔨": 4, "🌹": 4, "🪐": 5, "⌛": 3, "🐬": 4}',
  '{"🐂": 5, "⛽": 7, "🦋": 7, "🏟": 5, "🌾": 4, "⚖": 4, "🖼": -5}',
  'hip-hinge',
  'variant',
  'barbell-deadlift',
  0.90,
  NOW(), NOW()
);
```

---

## Migration Note

The existing `exercise-library.md` file contains ~2,185 exercises in prose/table format. Migration to this SQL schema is a Phase 3+ task. The schema here is the target structure. The source data is in the markdown file.

Priority for first migration: the 8 movement families documented in `exercise-engine/family-trees.md`. Approximately 120–150 exercises cover the most critical movement patterns for the initial procedural engine build.

---

🧮
