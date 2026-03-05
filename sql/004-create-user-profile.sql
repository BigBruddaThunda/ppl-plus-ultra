-- CX-08 / 004
-- Derived from: middle-math/schemas/user-profile-schema.md

CREATE TABLE IF NOT EXISTS user_exercise_profile (
  profile_id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  exercise_id           TEXT NOT NULL REFERENCES exercise_library(exercise_id),

  -- Computed stats
  estimated_1rm         NUMERIC(7,2),
  best_set_load         NUMERIC(7,2),
  best_set_reps         INTEGER,
  best_set_date         TIMESTAMPTZ,

  -- Trend
  trend                 TEXT,
  trend_slope           NUMERIC(6,3),

  -- History
  session_count         INTEGER NOT NULL DEFAULT 0,
  primary_zip           CHAR(4),
  order_history         JSONB NOT NULL DEFAULT '{}'::jsonb,
  color_history         JSONB NOT NULL DEFAULT '{}'::jsonb,

  -- Recency
  last_logged_at        TIMESTAMPTZ,
  last_logged_zip       CHAR(4),

  -- Metadata
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, exercise_id),
  CHECK (session_count >= 0),
  CHECK (
    trend IS NULL OR trend IN ('progressing', 'plateau', 'declining', 'insufficient-data')
  )
);

ALTER TABLE user_exercise_profile ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users can only read their own profile" ON user_exercise_profile;
CREATE POLICY "Users can only read their own profile"
  ON user_exercise_profile FOR SELECT
  USING (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_profile_user_exercise ON user_exercise_profile (user_id, exercise_id);
CREATE INDEX IF NOT EXISTS idx_profile_user_trend ON user_exercise_profile (user_id, trend);

CREATE OR REPLACE FUNCTION refresh_exercise_profile()
RETURNS TRIGGER AS $$
DECLARE
  v_estimated_1rm NUMERIC(7,2);
  v_best_load NUMERIC(7,2);
  v_best_reps INTEGER;
  v_best_date TIMESTAMPTZ;
  v_session_count INTEGER;
  v_primary_zip CHAR(4);
  v_order_history JSONB;
  v_color_history JSONB;
  v_last_logged_at TIMESTAMPTZ;
  v_last_logged_zip CHAR(4);
BEGIN
  SELECT
    MAX(actual_load_abs * (1 + actual_reps / 30.0))::NUMERIC(7,2),
    (ARRAY_AGG(actual_load_abs ORDER BY (actual_load_abs * (1 + COALESCE(actual_reps, 0) / 30.0)) DESC, logged_at DESC))[1]::NUMERIC(7,2),
    (ARRAY_AGG(actual_reps ORDER BY (actual_load_abs * (1 + COALESCE(actual_reps, 0) / 30.0)) DESC, logged_at DESC))[1]::INTEGER,
    (ARRAY_AGG(logged_at ORDER BY (actual_load_abs * (1 + COALESCE(actual_reps, 0) / 30.0)) DESC, logged_at DESC))[1]::TIMESTAMPTZ,
    COUNT(DISTINCT session_id)::INTEGER,
    (
      SELECT l2.zip_code
      FROM user_exercise_ledger l2
      WHERE l2.user_id = NEW.user_id AND l2.exercise_id = NEW.exercise_id
      GROUP BY l2.zip_code
      ORDER BY COUNT(*) DESC, l2.zip_code
      LIMIT 1
    )::CHAR(4),
    COALESCE((
      SELECT jsonb_object_agg(zip_order, cnt)
      FROM (
        SELECT zip_order, COUNT(*)::INT AS cnt
        FROM user_exercise_ledger
        WHERE user_id = NEW.user_id AND exercise_id = NEW.exercise_id
        GROUP BY zip_order
      ) q
    ), '{}'::jsonb),
    COALESCE((
      SELECT jsonb_object_agg(zip_color, cnt)
      FROM (
        SELECT zip_color, COUNT(*)::INT AS cnt
        FROM user_exercise_ledger
        WHERE user_id = NEW.user_id AND exercise_id = NEW.exercise_id
        GROUP BY zip_color
      ) q
    ), '{}'::jsonb),
    MAX(logged_at),
    (ARRAY_AGG(zip_code ORDER BY logged_at DESC))[1]::CHAR(4)
  INTO
    v_estimated_1rm,
    v_best_load,
    v_best_reps,
    v_best_date,
    v_session_count,
    v_primary_zip,
    v_order_history,
    v_color_history,
    v_last_logged_at,
    v_last_logged_zip
  FROM user_exercise_ledger
  WHERE user_id = NEW.user_id
    AND exercise_id = NEW.exercise_id
    AND completed = true
    AND actual_load_abs IS NOT NULL
    AND actual_reps IS NOT NULL;

  INSERT INTO user_exercise_profile (
    user_id,
    exercise_id,
    estimated_1rm,
    best_set_load,
    best_set_reps,
    best_set_date,
    trend,
    trend_slope,
    session_count,
    primary_zip,
    order_history,
    color_history,
    last_logged_at,
    last_logged_zip,
    updated_at
  ) VALUES (
    NEW.user_id,
    NEW.exercise_id,
    v_estimated_1rm,
    v_best_load,
    v_best_reps,
    v_best_date,
    'insufficient-data',
    NULL,
    COALESCE(v_session_count, 0),
    v_primary_zip,
    COALESCE(v_order_history, '{}'::jsonb),
    COALESCE(v_color_history, '{}'::jsonb),
    v_last_logged_at,
    v_last_logged_zip,
    NOW()
  )
  ON CONFLICT (user_id, exercise_id) DO UPDATE SET
    estimated_1rm  = EXCLUDED.estimated_1rm,
    best_set_load  = EXCLUDED.best_set_load,
    best_set_reps  = EXCLUDED.best_set_reps,
    best_set_date  = EXCLUDED.best_set_date,
    session_count  = EXCLUDED.session_count,
    primary_zip    = EXCLUDED.primary_zip,
    order_history  = EXCLUDED.order_history,
    color_history  = EXCLUDED.color_history,
    last_logged_at = EXCLUDED.last_logged_at,
    last_logged_zip= EXCLUDED.last_logged_zip,
    updated_at     = NOW();

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS after_ledger_insert ON user_exercise_ledger;
CREATE TRIGGER after_ledger_insert
  AFTER INSERT ON user_exercise_ledger
  FOR EACH ROW EXECUTE FUNCTION refresh_exercise_profile();
