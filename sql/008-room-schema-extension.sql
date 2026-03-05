-- CX-20 / 008
-- Room Schema Extension
-- Extends zip_metadata with room-level tracking: floors, bloom state, navigation edges, visits, votes.
-- Derived from: seeds/experience-layer-blueprint.md, seeds/systems-eudaimonics.md, middle-math/schemas/zip-metadata-schema.md

-- =============================================================================
-- TABLE: rooms
-- One row per zip code (1,680 total). Populated from zip_metadata on migration.
-- floor_id maps axis_position to the Axis-as-App-Floor model (1–6).
-- nav_north/east/south/west are the 4 directional edges from the navigation graph.
-- =============================================================================

CREATE TABLE IF NOT EXISTS rooms (
  zip_code    CHAR(4) PRIMARY KEY REFERENCES zip_metadata(zip_code) ON DELETE CASCADE
    CHECK (
      SUBSTRING(zip_code, 1, 1) BETWEEN '1' AND '7' AND
      SUBSTRING(zip_code, 2, 1) BETWEEN '1' AND '6' AND
      SUBSTRING(zip_code, 3, 1) BETWEEN '1' AND '5' AND
      SUBSTRING(zip_code, 4, 1) BETWEEN '1' AND '8'
    ),

  floor_id    SMALLINT NOT NULL CHECK (floor_id BETWEEN 1 AND 6),

  bloom_level INTEGER NOT NULL DEFAULT 0 CHECK (bloom_level >= 0),

  total_visits INTEGER NOT NULL DEFAULT 0 CHECK (total_visits >= 0),

  last_visited TIMESTAMPTZ,

  nav_north   CHAR(4) REFERENCES zip_metadata(zip_code),
  nav_east    CHAR(4) REFERENCES zip_metadata(zip_code),
  nav_south   CHAR(4) REFERENCES zip_metadata(zip_code),
  nav_west    CHAR(4) REFERENCES zip_metadata(zip_code),

  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_rooms_floor       ON rooms (floor_id);
CREATE INDEX IF NOT EXISTS idx_rooms_bloom       ON rooms (bloom_level);
CREATE INDEX IF NOT EXISTS idx_rooms_last_visited ON rooms (last_visited);
CREATE INDEX IF NOT EXISTS idx_rooms_nav_north   ON rooms (nav_north);
CREATE INDEX IF NOT EXISTS idx_rooms_nav_east    ON rooms (nav_east);
CREATE INDEX IF NOT EXISTS idx_rooms_nav_south   ON rooms (nav_south);
CREATE INDEX IF NOT EXISTS idx_rooms_nav_west    ON rooms (nav_west);

ALTER TABLE rooms ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "rooms_public_read" ON rooms;
CREATE POLICY "rooms_public_read"
  ON rooms FOR SELECT
  TO authenticated, anon
  USING (true);

CREATE OR REPLACE FUNCTION set_rooms_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS rooms_updated_at ON rooms;
CREATE TRIGGER rooms_updated_at
  BEFORE UPDATE ON rooms
  FOR EACH ROW EXECUTE FUNCTION set_rooms_updated_at();

-- =============================================================================
-- TABLE: room_visits
-- Append-only log. One row per user visit to a room. session_data is a JSONB
-- blob capturing the session state at the time of visit (exercises completed,
-- weights used, notes). Immutable after insert — no UPDATE policy.
-- =============================================================================

CREATE TABLE IF NOT EXISTS room_visits (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code     CHAR(4) NOT NULL REFERENCES rooms(zip_code),
  visited_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  session_data JSONB NOT NULL DEFAULT '{}'::JSONB
);

CREATE INDEX IF NOT EXISTS idx_room_visits_user      ON room_visits (user_id);
CREATE INDEX IF NOT EXISTS idx_room_visits_zip       ON room_visits (zip_code);
CREATE INDEX IF NOT EXISTS idx_room_visits_at        ON room_visits (visited_at);
CREATE INDEX IF NOT EXISTS idx_room_visits_user_zip  ON room_visits (user_id, zip_code);

ALTER TABLE room_visits ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "room_visits_own_select" ON room_visits;
CREATE POLICY "room_visits_own_select"
  ON room_visits FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "room_visits_own_insert" ON room_visits;
CREATE POLICY "room_visits_own_insert"
  ON room_visits FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

-- =============================================================================
-- TABLE: room_votes
-- User quality signal per room. vote_value: 1 = thumbs up, -1 = thumbs down,
-- 0 = neutral/retracted. One row per user per room (unique constraint).
-- =============================================================================

CREATE TABLE IF NOT EXISTS room_votes (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code    CHAR(4) NOT NULL REFERENCES rooms(zip_code),
  vote_value  SMALLINT NOT NULL CHECK (vote_value IN (-1, 0, 1)),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, zip_code)
);

CREATE INDEX IF NOT EXISTS idx_room_votes_user ON room_votes (user_id);
CREATE INDEX IF NOT EXISTS idx_room_votes_zip  ON room_votes (zip_code);

ALTER TABLE room_votes ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "room_votes_own_select" ON room_votes;
CREATE POLICY "room_votes_own_select"
  ON room_votes FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "room_votes_own_insert" ON room_votes;
CREATE POLICY "room_votes_own_insert"
  ON room_votes FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

DROP POLICY IF EXISTS "room_votes_own_update" ON room_votes;
CREATE POLICY "room_votes_own_update"
  ON room_votes FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE OR REPLACE FUNCTION set_room_votes_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS room_votes_updated_at ON room_votes;
CREATE TRIGGER room_votes_updated_at
  BEFORE UPDATE ON room_votes
  FOR EACH ROW EXECUTE FUNCTION set_room_votes_updated_at();

-- =============================================================================
-- TABLE: bloom_history
-- Append-only log of bloom level changes per user per room. Bloom is depth,
-- not gamification (see seeds/systems-eudaimonics.md). Each row records a
-- state transition. reason is a brief human-readable description of the trigger.
-- =============================================================================

CREATE TABLE IF NOT EXISTS bloom_history (
  id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id    UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code   CHAR(4) NOT NULL REFERENCES rooms(zip_code),
  old_level  INTEGER NOT NULL CHECK (old_level >= 0),
  new_level  INTEGER NOT NULL CHECK (new_level >= 0),
  changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  reason     TEXT
);

CREATE INDEX IF NOT EXISTS idx_bloom_history_user     ON bloom_history (user_id);
CREATE INDEX IF NOT EXISTS idx_bloom_history_zip      ON bloom_history (zip_code);
CREATE INDEX IF NOT EXISTS idx_bloom_history_user_zip ON bloom_history (user_id, zip_code);
CREATE INDEX IF NOT EXISTS idx_bloom_history_at       ON bloom_history (changed_at);

ALTER TABLE bloom_history ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "bloom_history_own_select" ON bloom_history;
CREATE POLICY "bloom_history_own_select"
  ON bloom_history FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

DROP POLICY IF EXISTS "bloom_history_own_insert" ON bloom_history;
CREATE POLICY "bloom_history_own_insert"
  ON bloom_history FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

-- =============================================================================
-- POPULATION: 1,680 rooms from zip_metadata
-- floor_id = axis_position (the Axis is the floor of the building).
-- nav_* columns are NULL until populated by the navigation graph builder (CX-23).
-- =============================================================================

INSERT INTO rooms (zip_code, floor_id)
SELECT zip_code, axis_position AS floor_id
FROM zip_metadata
ON CONFLICT (zip_code) DO NOTHING;

-- =============================================================================
-- VERIFICATION
-- =============================================================================

SELECT COUNT(*) AS rooms_count FROM rooms;
-- Expected: 1680
