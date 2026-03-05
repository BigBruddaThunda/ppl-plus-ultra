-- CX-08 / 002
-- Derived from: middle-math/schemas/exercise-families-schema.md

CREATE TABLE IF NOT EXISTS exercise_families (
  family_id             TEXT PRIMARY KEY,
  name                  TEXT NOT NULL,
  description           TEXT,
  type_primary          TEXT NOT NULL,
  movement_category     TEXT NOT NULL CHECK (
    movement_category IN ('pull', 'push', 'squat', 'hinge', 'carry', 'conditioning', 'isolation')
  ),
  root_exercise_id      TEXT REFERENCES exercise_library(exercise_id),
  created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
