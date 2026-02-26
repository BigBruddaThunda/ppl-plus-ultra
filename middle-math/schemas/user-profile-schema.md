# User Exercise Profile Schema

Derived stats computed from the exercise ledger. Updated after each logged session.

---

## Table: user_exercise_profile

```sql
CREATE TABLE user_exercise_profile (
  profile_id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  exercise_id           TEXT NOT NULL REFERENCES exercise_library(exercise_id),

  -- Computed stats
  estimated_1rm         NUMERIC(7,2),               -- Epley-derived from best recent set
  best_set_load         NUMERIC(7,2),               -- Actual load from best set
  best_set_reps         INTEGER,                    -- Actual reps from best set
  best_set_date         TIMESTAMP,                  -- Date of best set

  -- Trend
  trend                 TEXT,                       -- "progressing" | "plateau" | "declining" | "insufficient-data"
  trend_slope           NUMERIC(6,3),               -- Linear regression slope over last 6 sessions

  -- History
  session_count         INTEGER NOT NULL DEFAULT 0, -- Total sessions at this exercise
  primary_zip           TEXT,                        -- Zip code with most sessions
  order_history         JSONB NOT NULL DEFAULT '{}', -- {"⛽": 8, "🦋": 3}
  color_history         JSONB NOT NULL DEFAULT '{}', -- {"🔵": 6, "🟣": 3}

  -- Recency
  last_logged_at        TIMESTAMP,
  last_logged_zip       TEXT,

  -- Metadata
  updated_at            TIMESTAMP DEFAULT NOW(),

  UNIQUE (user_id, exercise_id)
);

-- RLS
ALTER TABLE user_exercise_profile ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only read their own profile"
  ON user_exercise_profile FOR SELECT
  USING (auth.uid() = user_id);

-- Index
CREATE INDEX idx_profile_user_exercise ON user_exercise_profile (user_id, exercise_id);
CREATE INDEX idx_profile_user_trend ON user_exercise_profile (user_id, trend);
```

---

## Update Trigger

The profile is refreshed after each ledger insert:

```sql
CREATE OR REPLACE FUNCTION refresh_exercise_profile()
RETURNS TRIGGER AS $$
BEGIN
  -- Recompute profile for the affected exercise
  INSERT INTO user_exercise_profile (
    user_id, exercise_id, estimated_1rm, best_set_load, best_set_reps,
    best_set_date, session_count, primary_zip, order_history, color_history,
    last_logged_at, last_logged_zip, updated_at
  )
  SELECT
    NEW.user_id,
    NEW.exercise_id,
    MAX(actual_load_abs * (1 + actual_reps / 30.0)) AS estimated_1rm,
    -- ... (additional computed columns)
    NOW()
  FROM user_exercise_ledger
  WHERE user_id = NEW.user_id AND exercise_id = NEW.exercise_id
  ON CONFLICT (user_id, exercise_id) DO UPDATE SET
    estimated_1rm = EXCLUDED.estimated_1rm,
    updated_at    = NOW();

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_ledger_insert
  AFTER INSERT ON user_exercise_ledger
  FOR EACH ROW EXECUTE FUNCTION refresh_exercise_profile();
```

---

## Profile Read Pattern

```sql
-- Get profile for prescription computation
SELECT
  p.estimated_1rm,
  p.trend,
  p.primary_zip,
  p.order_history,
  p.color_history,
  p.last_logged_at
FROM user_exercise_profile p
WHERE p.user_id = $1
  AND p.exercise_id = $2;

-- Get all exercises for a user with low-recency (overdue for revisit)
SELECT
  p.exercise_id,
  p.last_logged_at,
  p.primary_zip,
  NOW() - p.last_logged_at AS days_since
FROM user_exercise_profile p
WHERE p.user_id = $1
  AND p.session_count >= 3
ORDER BY p.last_logged_at ASC
LIMIT 20;
```

---

🧮
