-- 009-exercise-registry.sql
-- CX-40: Exercise Registry table
-- Stores enriched exercise data produced by scripts/build-exercise-registry.py
-- Primary key: TEXT exercise_id in "EX-NNNN" format (globally unique across all 2,085 exercises)
-- Derived from: middle-math/exercise-registry.json

-- ─────────────────────────────────────────────────────────────────────────────
-- TABLE: exercise_registry
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS exercise_registry (
  -- Identity
  exercise_id         TEXT        PRIMARY KEY,          -- "EX-0001" through "EX-2085"
  source_id           INTEGER,                          -- original per-section sequential ID from exercise-library.json
  source_section      TEXT,                             -- "A" through "Q"
  name                TEXT        NOT NULL,
  canonical_name      TEXT        NOT NULL,

  -- SCL classification
  scl_types           TEXT[]      NOT NULL,             -- ["Push"] | ["Pull"] | ["Legs"] | ["Plus"] | ["Ultra"]
  order_relevance     TEXT[],                           -- ["Foundation", "Strength", ...]
  axis_emphasis       TEXT[],                           -- ["Basics", "Functional", ...]
  equipment_tier_min  INTEGER     NOT NULL DEFAULT 0,   -- 0–5 (Tier 0 = bodyweight, Tier 5 = specialty)
  equipment_tier_max  INTEGER     NOT NULL DEFAULT 5,
  gold_gated          BOOLEAN     NOT NULL DEFAULT false,

  -- Movement classification
  movement_pattern    TEXT        NOT NULL,             -- standardized 16-pattern vocabulary
  movement_subpattern TEXT,                             -- original source pattern (if non-standard)
  muscle_groups       TEXT,                             -- source section region (e.g. "CHEST", "BACK")

  -- Biomechanics
  bilateral           BOOLEAN     NOT NULL DEFAULT true,
  compound            BOOLEAN     NOT NULL DEFAULT false,

  -- Anatomy (inferred from movement pattern + section + name)
  primary_movers      TEXT[]      NOT NULL DEFAULT '{}',
  secondary_movers    TEXT[]               DEFAULT '{}',
  stabilizers         TEXT[]               DEFAULT '{}',
  joint_actions       TEXT[]               DEFAULT '{}',

  -- Equipment
  equipment           TEXT[]               DEFAULT '{}',  -- ["barbell"] | ["dumbbell", "bench"] | etc.

  -- Family tree (see CX-38 for full JSON family structure)
  family_id           TEXT,                             -- "hip-hinge" | "squat" | ... | or movement_pattern for unlinked
  family_role         TEXT,                             -- "root" | "variant" | "progression" | "regression" | "equipment-swap" | "unlinked"
  parent_id           TEXT        REFERENCES exercise_registry(exercise_id) ON DELETE SET NULL,
  transfer_ratio      NUMERIC(4,2),                     -- 0.55–1.20 | NULL for unlinked

  -- Affinity scores (octave scale -8 to +8)
  axis_affinity       JSONB,                            -- {"classic": 8, "functional": 2, "aesthetic": 0, "challenge": 3, "time": 0, "partner": 2}
  order_affinity      JSONB,                            -- {"foundation": 4, "strength": 8, "hypertrophy": 3, "performance": 6, "full_body": 2, "balance": 1, "restoration": 0}

  -- Sport tags (from CX-38)
  sport_tags          TEXT[]               DEFAULT '{}',

  -- External integration dock (populated by CX-39 / ExRx partnership pipeline)
  external_ref        JSONB,                            -- {"exrx_url": null, "video_url": null, "research_urls": [], "partner_status": "unmapped"}

  -- Knowledge content link
  knowledge_file      TEXT,                             -- "exercise-content/pull/barbell-bent-over-row.md"

  -- Metadata
  status              TEXT        NOT NULL DEFAULT 'REGISTERED',  -- REGISTERED | REVIEWED | DEPRECATED
  created_at          TIMESTAMPTZ          DEFAULT now(),
  updated_at          TIMESTAMPTZ          DEFAULT now()
);

-- ─────────────────────────────────────────────────────────────────────────────
-- CONSTRAINTS
-- ─────────────────────────────────────────────────────────────────────────────

-- Movement pattern must be in the 16-pattern vocabulary
ALTER TABLE exercise_registry
  ADD CONSTRAINT chk_movement_pattern CHECK (
    movement_pattern IN (
      'hip-hinge', 'vertical-pull', 'horizontal-pull', 'isolation-curl',
      'horizontal-press', 'vertical-press', 'isolation-extension', 'squat',
      'lunge', 'leg-isolation', 'carry', 'anti-rotation', 'core-stability',
      'olympic', 'conditioning', 'plyometric'
    )
  );

-- Family role must be a valid value
ALTER TABLE exercise_registry
  ADD CONSTRAINT chk_family_role CHECK (
    family_role IN ('root', 'variant', 'progression', 'regression', 'equipment-swap', 'unlinked')
    OR family_role IS NULL
  );

-- Equipment tier range must be valid
ALTER TABLE exercise_registry
  ADD CONSTRAINT chk_equipment_tier CHECK (
    equipment_tier_min >= 0 AND equipment_tier_max <= 5 AND equipment_tier_min <= equipment_tier_max
  );

-- ─────────────────────────────────────────────────────────────────────────────
-- ROW LEVEL SECURITY
-- ─────────────────────────────────────────────────────────────────────────────

ALTER TABLE exercise_registry ENABLE ROW LEVEL SECURITY;

-- All authenticated and anonymous users can read the registry
CREATE POLICY "exercise_registry_readable_by_all"
  ON exercise_registry
  FOR SELECT
  USING (true);

-- Only service role can write (insert/update/delete)
-- Default policy: no INSERT/UPDATE/DELETE from client — service role bypasses RLS

-- ─────────────────────────────────────────────────────────────────────────────
-- INDEXES
-- ─────────────────────────────────────────────────────────────────────────────

-- SCL type filter (most common query pattern: "find exercises of type Pull")
CREATE INDEX idx_exercise_registry_type
  ON exercise_registry USING GIN (scl_types);

-- Movement pattern filter
CREATE INDEX idx_exercise_registry_pattern
  ON exercise_registry (movement_pattern);

-- Family traversal
CREATE INDEX idx_exercise_registry_family_id
  ON exercise_registry (family_id);

-- Parent-child traversal
CREATE INDEX idx_exercise_registry_parent_id
  ON exercise_registry (parent_id);

-- Anatomy lookup (drives exercise selector V2 — "find all exercises that train quadriceps")
CREATE INDEX idx_exercise_registry_primary_movers
  ON exercise_registry USING GIN (primary_movers);

CREATE INDEX idx_exercise_registry_secondary_movers
  ON exercise_registry USING GIN (secondary_movers);

-- Gold gate filter
CREATE INDEX idx_exercise_registry_gold_gated
  ON exercise_registry (gold_gated)
  WHERE gold_gated = true;

-- Text search on exercise name
CREATE INDEX idx_exercise_registry_name_trgm
  ON exercise_registry USING GIN (name gin_trgm_ops);

-- ─────────────────────────────────────────────────────────────────────────────
-- TRIGGER: auto-update updated_at
-- ─────────────────────────────────────────────────────────────────────────────

CREATE OR REPLACE FUNCTION update_exercise_registry_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_exercise_registry_updated_at
  BEFORE UPDATE ON exercise_registry
  FOR EACH ROW
  EXECUTE FUNCTION update_exercise_registry_timestamp();

-- ─────────────────────────────────────────────────────────────────────────────
-- COMMENT
-- ─────────────────────────────────────────────────────────────────────────────

COMMENT ON TABLE exercise_registry IS
  'Enriched exercise registry. Source: middle-math/exercise-registry.json. '
  'Primary key EX-NNNN is globally unique across all 2,085 exercises. '
  'Populated by scripts/build-exercise-registry.py (CX-36). '
  'Anatomy, family linkage, and affinity scores are inferred at build time. '
  'External refs populated by CX-39 pipeline. '
  'Knowledge files live in exercise-content/{type}/{slug}.md (CX-37).';
