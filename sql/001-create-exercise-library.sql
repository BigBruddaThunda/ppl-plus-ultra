-- CX-08 / 001
-- Derived from: middle-math/schemas/exercise-library-schema.md

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS exercise_library (
  -- Identity
  exercise_id           TEXT PRIMARY KEY,
  name                  TEXT NOT NULL,
  display_name          TEXT,
  section               TEXT NOT NULL,
  notes                 TEXT,

  -- SCL Type mapping
  type_primary          TEXT NOT NULL,
  type_secondary        TEXT[],

  -- Movement pattern
  movement_pattern      TEXT NOT NULL,
  compound              BOOLEAN NOT NULL DEFAULT true,
  bilateral             BOOLEAN NOT NULL DEFAULT true,

  -- Equipment
  equipment_tier        INTEGER NOT NULL,
  equipment_tier_max    INTEGER,

  -- GOLD gate
  gold_required         BOOLEAN NOT NULL DEFAULT false,

  -- Weight system columns
  axis_affinity         JSONB NOT NULL DEFAULT '{}'::jsonb,
  order_affinity        JSONB NOT NULL DEFAULT '{}'::jsonb,

  -- Family tree
  family_id             TEXT,
  family_role           TEXT CHECK (family_role IN ('root', 'variant', 'progression', 'regression', 'equipment-swap')),
  parent_exercise_id    TEXT REFERENCES exercise_library(exercise_id),
  transfer_ratio        NUMERIC(4,2) CHECK (transfer_ratio IS NULL OR transfer_ratio BETWEEN 0.00 AND 1.20),

  -- Metadata
  created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  CHECK (equipment_tier BETWEEN 0 AND 5),
  CHECK (equipment_tier_max IS NULL OR equipment_tier_max BETWEEN equipment_tier AND 5)
);

CREATE INDEX IF NOT EXISTS idx_exercise_library_type_primary ON exercise_library (type_primary);
CREATE INDEX IF NOT EXISTS idx_exercise_library_movement_pattern ON exercise_library (movement_pattern);
CREATE INDEX IF NOT EXISTS idx_exercise_library_equipment_tier ON exercise_library (equipment_tier);
CREATE INDEX IF NOT EXISTS idx_exercise_library_family_id ON exercise_library (family_id);
CREATE INDEX IF NOT EXISTS idx_exercise_library_gold_required ON exercise_library (gold_required);

CREATE OR REPLACE FUNCTION set_exercise_library_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_exercise_library_updated_at ON exercise_library;
CREATE TRIGGER trg_exercise_library_updated_at
BEFORE UPDATE ON exercise_library
FOR EACH ROW EXECUTE FUNCTION set_exercise_library_updated_at();
