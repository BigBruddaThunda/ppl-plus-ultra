-- CX-08 / 003
-- Derived from: middle-math/schemas/user-ledger-schema.md

CREATE TABLE IF NOT EXISTS user_exercise_ledger (
  -- Identity
  log_id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  session_id            UUID NOT NULL,
  logged_at             TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Zip context (numeric zip system)
  zip_code              CHAR(4) NOT NULL,
  zip_order             TEXT NOT NULL,
  zip_axis              TEXT NOT NULL,
  zip_type              TEXT NOT NULL,
  zip_color             TEXT NOT NULL,

  -- Exercise
  exercise_id           TEXT NOT NULL REFERENCES exercise_library(exercise_id),
  block                 TEXT NOT NULL,

  -- Set data
  set_number            INTEGER NOT NULL CHECK (set_number > 0),
  prescribed_load_pct   NUMERIC(5,3),
  prescribed_load_abs   NUMERIC(7,2),
  prescribed_reps       INTEGER,

  -- Actual performance
  actual_load_abs       NUMERIC(7,2),
  actual_reps           INTEGER,
  rpe                   NUMERIC(3,1),
  completed             BOOLEAN NOT NULL DEFAULT true,

  -- Optional
  notes                 TEXT,
  unit                  TEXT NOT NULL DEFAULT 'kg' CHECK (unit IN ('kg', 'lbs')),

  CHECK (prescribed_load_pct IS NULL OR prescribed_load_pct BETWEEN 0 AND 9.999),
  CHECK (rpe IS NULL OR rpe BETWEEN 1.0 AND 10.0),
  CHECK (prescribed_reps IS NULL OR prescribed_reps > 0),
  CHECK (actual_reps IS NULL OR actual_reps > 0),
  CHECK (prescribed_load_abs IS NULL OR prescribed_load_abs >= 0),
  CHECK (actual_load_abs IS NULL OR actual_load_abs >= 0)
);

CREATE TABLE IF NOT EXISTS workout_sessions (
  session_id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  zip_code              CHAR(4) NOT NULL,
  started_at            TIMESTAMPTZ NOT NULL,
  completed_at          TIMESTAMPTZ,
  total_sets            INTEGER,
  session_rpe           NUMERIC(3,1),
  notes                 TEXT,
  CHECK (total_sets IS NULL OR total_sets >= 0),
  CHECK (session_rpe IS NULL OR session_rpe BETWEEN 1.0 AND 10.0)
);

ALTER TABLE user_exercise_ledger ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can only read their own ledger" ON user_exercise_ledger;
CREATE POLICY "Users can only read their own ledger"
  ON user_exercise_ledger FOR SELECT
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "Users can only insert their own ledger" ON user_exercise_ledger;
CREATE POLICY "Users can only insert their own ledger"
  ON user_exercise_ledger FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_ledger_user_exercise ON user_exercise_ledger (user_id, exercise_id);
CREATE INDEX IF NOT EXISTS idx_ledger_user_zip ON user_exercise_ledger (user_id, zip_code);
CREATE INDEX IF NOT EXISTS idx_ledger_user_order ON user_exercise_ledger (user_id, zip_order);
CREATE INDEX IF NOT EXISTS idx_ledger_session ON user_exercise_ledger (session_id);
CREATE INDEX IF NOT EXISTS idx_ledger_logged_at ON user_exercise_ledger (user_id, logged_at DESC);
