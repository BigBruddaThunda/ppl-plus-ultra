# User Exercise Ledger Schema

Raw workout log. One row per exercise set per logged session. The source of truth for all user data.

---

## Table: user_exercise_ledger

```sql
CREATE TABLE user_exercise_ledger (
  -- Identity
  log_id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  session_id            UUID NOT NULL,               -- Groups all sets from one workout
  logged_at             TIMESTAMP NOT NULL DEFAULT NOW(),

  -- Zip code context
  zip_code              TEXT NOT NULL,               -- "⛽🏛🪡🔵"
  zip_order             TEXT NOT NULL,               -- "⛽" (extracted for fast filtering)
  zip_axis              TEXT NOT NULL,               -- "🏛"
  zip_type              TEXT NOT NULL,               -- "🪡"
  zip_color             TEXT NOT NULL,               -- "🔵"

  -- Exercise
  exercise_id           TEXT NOT NULL REFERENCES exercise_library(exercise_id),
  block                 TEXT NOT NULL,               -- "🧈", "🧩", "▶️", etc.

  -- Set data
  set_number            INTEGER NOT NULL,
  prescribed_load_pct   NUMERIC(5,3),               -- 0.800 = 80% of 1RM
  prescribed_load_abs   NUMERIC(7,2),               -- 80.00 kg
  prescribed_reps       INTEGER,

  -- Actual performance
  actual_load_abs       NUMERIC(7,2),               -- What was actually lifted
  actual_reps           INTEGER,
  rpe                   NUMERIC(3,1),               -- 1.0–10.0 (optional)
  completed             BOOLEAN NOT NULL DEFAULT true,

  -- Optional
  notes                 TEXT,                        -- "left knee felt off"
  unit                  TEXT NOT NULL DEFAULT 'kg'  -- 'kg' | 'lbs'
);

-- Row-level security
ALTER TABLE user_exercise_ledger ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only read their own ledger"
  ON user_exercise_ledger FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can only insert their own ledger"
  ON user_exercise_ledger FOR INSERT
  WITH CHECK (auth.uid() = user_id);

-- Indexes for common query patterns
CREATE INDEX idx_ledger_user_exercise ON user_exercise_ledger (user_id, exercise_id);
CREATE INDEX idx_ledger_user_zip ON user_exercise_ledger (user_id, zip_code);
CREATE INDEX idx_ledger_user_order ON user_exercise_ledger (user_id, zip_order);
CREATE INDEX idx_ledger_session ON user_exercise_ledger (session_id);
CREATE INDEX idx_ledger_logged_at ON user_exercise_ledger (user_id, logged_at DESC);
```

---

## Sessions Table

```sql
CREATE TABLE workout_sessions (
  session_id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),
  zip_code              TEXT NOT NULL,
  started_at            TIMESTAMP NOT NULL,
  completed_at          TIMESTAMP,
  total_sets            INTEGER,
  session_rpe           NUMERIC(3,1),               -- Overall session RPE (optional)
  notes                 TEXT
);
```

---

## Common Query Patterns

```sql
-- All sets for a specific user at a specific exercise
SELECT * FROM user_exercise_ledger
WHERE user_id = $1 AND exercise_id = $2
ORDER BY logged_at DESC;

-- Best set per exercise for a user (for 1RM computation)
SELECT exercise_id,
       MAX(actual_load_abs * (1 + actual_reps / 30.0)) AS estimated_1rm
FROM user_exercise_ledger
WHERE user_id = $1
  AND completed = true
  AND logged_at >= NOW() - INTERVAL '90 days'
GROUP BY exercise_id;

-- Session history by zip code
SELECT s.zip_code, COUNT(*) AS sessions, AVG(s.session_rpe) AS avg_rpe
FROM workout_sessions s
WHERE s.user_id = $1
GROUP BY s.zip_code
ORDER BY sessions DESC;
```

---

🧮
