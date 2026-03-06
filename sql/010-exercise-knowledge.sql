-- 010-exercise-knowledge.sql
-- CX-40: Exercise Knowledge table
-- One row per exercise. Stores coaching cues, fault corrections, and PPL± context.
-- 1:1 relationship with exercise_registry.
-- Populated by scripts/generate-exercise-content.py (CX-37).
-- Knowledge files: exercise-content/{type}/{slug}.md

-- ─────────────────────────────────────────────────────────────────────────────
-- TABLE: exercise_knowledge
-- ─────────────────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS exercise_knowledge (
  -- Identity (FK to registry)
  exercise_id         TEXT        PRIMARY KEY
                      REFERENCES exercise_registry(exercise_id) ON DELETE CASCADE,

  -- Content fields
  description         TEXT,           -- 2-3 sentence overview: what it is, what it trains, why it exists

  -- Ordered coaching arrays
  setup_cues          TEXT[],         -- ordered setup steps (3–6 items)
  execution_cues      TEXT[],         -- ordered execution steps (4–8 items)

  -- Fault-correction pairs
  common_faults       JSONB,          -- [{"fault": "...", "correction": "..."}, ...]

  -- PPL± system-specific content
  ppl_context         JSONB,          -- {"foundation": "...", "strength": "...", "hypertrophy": "...", "restoration": "..."}
  color_modifiers     JSONB,          -- {"technical": "...", "intense": "...", "mindful": "..."}

  -- Coaching notes (PPL± voice paragraph)
  coaching_notes      TEXT,

  -- Sport application
  sport_tags          TEXT[],         -- inherited from registry; may be overridden here

  -- Content management
  status              TEXT        NOT NULL DEFAULT 'EMPTY',  -- EMPTY | GENERATED | REVIEWED | CANONICAL
  knowledge_file      TEXT,           -- source file: exercise-content/{type}/{slug}.md
  generated_at        TIMESTAMPTZ,
  reviewed_at         TIMESTAMPTZ,
  updated_at          TIMESTAMPTZ     DEFAULT now()
);

-- ─────────────────────────────────────────────────────────────────────────────
-- CONSTRAINTS
-- ─────────────────────────────────────────────────────────────────────────────

ALTER TABLE exercise_knowledge
  ADD CONSTRAINT chk_knowledge_status CHECK (
    status IN ('EMPTY', 'GENERATED', 'REVIEWED', 'CANONICAL')
  );

-- common_faults must be a JSON array (if present)
ALTER TABLE exercise_knowledge
  ADD CONSTRAINT chk_common_faults_is_array CHECK (
    common_faults IS NULL OR jsonb_typeof(common_faults) = 'array'
  );

-- ─────────────────────────────────────────────────────────────────────────────
-- ROW LEVEL SECURITY
-- ─────────────────────────────────────────────────────────────────────────────

ALTER TABLE exercise_knowledge ENABLE ROW LEVEL SECURITY;

-- All users can read knowledge (drives workout coaching panel and exercise detail pages)
CREATE POLICY "exercise_knowledge_readable_by_all"
  ON exercise_knowledge
  FOR SELECT
  USING (true);

-- Only service role can write

-- ─────────────────────────────────────────────────────────────────────────────
-- INDEXES
-- ─────────────────────────────────────────────────────────────────────────────

-- Status filter (find all EMPTY entries to batch-generate)
CREATE INDEX idx_exercise_knowledge_status
  ON exercise_knowledge (status);

-- ─────────────────────────────────────────────────────────────────────────────
-- TRIGGER: auto-update updated_at
-- ─────────────────────────────────────────────────────────────────────────────

CREATE OR REPLACE FUNCTION update_exercise_knowledge_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_exercise_knowledge_updated_at
  BEFORE UPDATE ON exercise_knowledge
  FOR EACH ROW
  EXECUTE FUNCTION update_exercise_knowledge_timestamp();

-- ─────────────────────────────────────────────────────────────────────────────
-- INITIAL POPULATION: stub rows for all registry exercises
-- Creates one EMPTY row per exercise so the table reflects completeness.
-- Run after 009-exercise-registry.sql has been loaded with data.
-- ─────────────────────────────────────────────────────────────────────────────

INSERT INTO exercise_knowledge (exercise_id, status, knowledge_file)
SELECT
  exercise_id,
  'EMPTY',
  knowledge_file
FROM exercise_registry
ON CONFLICT (exercise_id) DO NOTHING;

-- ─────────────────────────────────────────────────────────────────────────────
-- COMMENT
-- ─────────────────────────────────────────────────────────────────────────────

COMMENT ON TABLE exercise_knowledge IS
  'One-to-one coaching content for each exercise in exercise_registry. '
  'Setup cues, execution cues, common faults, PPL± per-Order context, coaching notes. '
  'Populated by scripts/generate-exercise-content.py (CX-37). '
  'Source files: exercise-content/{type}/{slug}.md. '
  'Status lifecycle: EMPTY → GENERATED → REVIEWED → CANONICAL.';

COMMENT ON COLUMN exercise_knowledge.ppl_context IS
  'Per-Order behavior description. Keys: foundation, strength, hypertrophy, '
  'performance, full_body, balance, restoration. '
  'Content is unique to PPL± — explains how the exercise behaves differently '
  'under each of the 7 loading protocols.';

COMMENT ON COLUMN exercise_knowledge.common_faults IS
  'Array of fault-correction pairs. '
  'Schema: [{"fault": "Lumbar rounding", "correction": "Brace before unracking. If you lose position at the bottom, reduce load."}]';
