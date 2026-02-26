# User Exercise Toggles Schema

Toggle table for user exercise/equipment/movement/type exclusions.

---

## Table: user_exercise_toggles

```sql
CREATE TABLE user_exercise_toggles (
  toggle_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),

  -- Toggle specification
  toggle_type           TEXT NOT NULL,              -- "exercise" | "equipment_tier" | "movement_pattern" | "type"
  entity_id             TEXT NOT NULL,              -- The ID of what is toggled
                                                    -- exercise: "barbell-deadlift"
                                                    -- equipment_tier: "3"
                                                    -- movement_pattern: "hip-hinge"
                                                    -- type: "🍗"
  modifier              TEXT,                       -- For equipment_tier: "gte" | "eq"
                                                    -- For others: null

  -- Status
  active                BOOLEAN NOT NULL DEFAULT true,
  reason                TEXT,                        -- Optional user note: "lower back injury"

  -- Duration
  expires_at            TIMESTAMP,                  -- null = indefinite
  session_limit         INTEGER,                    -- null = no limit; N = expires after N sessions
  sessions_used         INTEGER NOT NULL DEFAULT 0, -- Increments on each session where toggle was active

  -- Metadata
  created_at            TIMESTAMP DEFAULT NOW(),
  updated_at            TIMESTAMP DEFAULT NOW(),

  UNIQUE (user_id, toggle_type, entity_id)
);

-- RLS
ALTER TABLE user_exercise_toggles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users manage their own toggles"
  ON user_exercise_toggles FOR ALL
  USING (auth.uid() = user_id);

-- Index
CREATE INDEX idx_toggles_user_active ON user_exercise_toggles (user_id, active);
CREATE INDEX idx_toggles_user_type ON user_exercise_toggles (user_id, toggle_type);
```

---

## Toggle Expiry Logic

Toggles expire when:
1. `expires_at` is set and `NOW() >= expires_at` → auto-deactivate
2. `session_limit` is set and `sessions_used >= session_limit` → auto-deactivate

```sql
-- Check and expire stale toggles (run on session start)
UPDATE user_exercise_toggles
SET active = false, updated_at = NOW()
WHERE user_id = $1
  AND active = true
  AND (
    (expires_at IS NOT NULL AND expires_at <= NOW())
    OR
    (session_limit IS NOT NULL AND sessions_used >= session_limit)
  );
```

---

## Example Toggles

```sql
-- Toggle off a specific exercise
INSERT INTO user_exercise_toggles (user_id, toggle_type, entity_id, reason)
VALUES ($1, 'exercise', 'barbell-deadlift', 'lower back injury');

-- Toggle off all barbell+ (tier 3 and above) — no barbell available
INSERT INTO user_exercise_toggles (user_id, toggle_type, entity_id, modifier)
VALUES ($1, 'equipment_tier', '3', 'gte');

-- Toggle off all overhead movements — shoulder impingement
INSERT INTO user_exercise_toggles (user_id, toggle_type, entity_id, reason)
VALUES ($1, 'movement_pattern', 'vertical-press', 'shoulder impingement');

-- Skip legs for 2 sessions — post leg day soreness
INSERT INTO user_exercise_toggles (user_id, toggle_type, entity_id, session_limit, reason)
VALUES ($1, 'type', '🍗', 2, 'DOMS from Monday session');
```

---

🧮
