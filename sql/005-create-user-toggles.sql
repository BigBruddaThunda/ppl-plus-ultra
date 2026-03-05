-- CX-08 / 005
-- Derived from: middle-math/schemas/user-toggles-schema.md

CREATE TABLE IF NOT EXISTS user_exercise_toggles (
  toggle_id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id               UUID NOT NULL REFERENCES auth.users(id),

  -- Toggle specification
  toggle_type           TEXT NOT NULL CHECK (toggle_type IN ('exercise', 'equipment_tier', 'movement_pattern', 'type')),
  entity_id             TEXT NOT NULL,
  modifier              TEXT,

  -- Status
  active                BOOLEAN NOT NULL DEFAULT true,
  reason                TEXT,

  -- Duration
  expires_at            TIMESTAMPTZ,
  session_limit         INTEGER,
  sessions_used         INTEGER NOT NULL DEFAULT 0,

  -- Metadata
  created_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at            TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, toggle_type, entity_id),
  CHECK (session_limit IS NULL OR session_limit >= 0),
  CHECK (sessions_used >= 0),
  CHECK (
    modifier IS NULL OR modifier IN ('gte', 'eq')
  )
);

ALTER TABLE user_exercise_toggles ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Users manage their own toggles" ON user_exercise_toggles;
CREATE POLICY "Users manage their own toggles"
  ON user_exercise_toggles FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_toggles_user_active ON user_exercise_toggles (user_id, active);
CREATE INDEX IF NOT EXISTS idx_toggles_user_type ON user_exercise_toggles (user_id, toggle_type);

CREATE OR REPLACE FUNCTION set_user_exercise_toggles_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_user_exercise_toggles_updated_at ON user_exercise_toggles;
CREATE TRIGGER trg_user_exercise_toggles_updated_at
BEFORE UPDATE ON user_exercise_toggles
FOR EACH ROW EXECUTE FUNCTION set_user_exercise_toggles_updated_at();
