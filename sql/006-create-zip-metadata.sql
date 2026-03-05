-- CX-08 / 006
-- Derived from: middle-math/schemas/zip-metadata-schema.md

CREATE TABLE IF NOT EXISTS zip_metadata (
  zip_code         CHAR(4) PRIMARY KEY
    CHECK (
      SUBSTRING(zip_code, 1, 1) BETWEEN '1' AND '7' AND
      SUBSTRING(zip_code, 2, 1) BETWEEN '1' AND '6' AND
      SUBSTRING(zip_code, 3, 1) BETWEEN '1' AND '5' AND
      SUBSTRING(zip_code, 4, 1) BETWEEN '1' AND '8'
    ),

  order_position   SMALLINT NOT NULL CHECK (order_position BETWEEN 1 AND 7),
  axis_position    SMALLINT NOT NULL CHECK (axis_position BETWEEN 1 AND 6),
  type_position    SMALLINT NOT NULL CHECK (type_position BETWEEN 1 AND 5),
  color_position   SMALLINT NOT NULL CHECK (color_position BETWEEN 1 AND 8),

  deck_number      SMALLINT GENERATED ALWAYS AS (((order_position - 1) * 6 + axis_position)) STORED,

  card_status      TEXT NOT NULL DEFAULT 'EMPTY'
    CHECK (card_status IN ('EMPTY', 'GENERATED', 'CANONICAL')),

  operator_emoji   TEXT,
  operator_name    TEXT,

  card_title       TEXT,
  markdown_content TEXT,

  weight_vector    JSONB,
  primary_palette  JSONB,

  block_sequence   TEXT[],

  created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  CHECK (deck_number BETWEEN 1 AND 42),
  CHECK (
    zip_code = CONCAT(order_position::text, axis_position::text, type_position::text, color_position::text)
  )
);

CREATE INDEX IF NOT EXISTS idx_zip_order ON zip_metadata (order_position);
CREATE INDEX IF NOT EXISTS idx_zip_axis ON zip_metadata (axis_position);
CREATE INDEX IF NOT EXISTS idx_zip_type ON zip_metadata (type_position);
CREATE INDEX IF NOT EXISTS idx_zip_color ON zip_metadata (color_position);
CREATE INDEX IF NOT EXISTS idx_zip_deck ON zip_metadata (deck_number);
CREATE INDEX IF NOT EXISTS idx_zip_status ON zip_metadata (card_status);
CREATE INDEX IF NOT EXISTS idx_zip_deck_type ON zip_metadata (deck_number, type_position);
CREATE INDEX IF NOT EXISTS idx_zip_order_type ON zip_metadata (order_position, type_position);

ALTER TABLE zip_metadata ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "zip_metadata_public_read" ON zip_metadata;
CREATE POLICY "zip_metadata_public_read"
  ON zip_metadata FOR SELECT
  TO authenticated, anon
  USING (true);

CREATE OR REPLACE FUNCTION set_zip_metadata_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS zip_metadata_updated_at ON zip_metadata;
CREATE TRIGGER zip_metadata_updated_at
  BEFORE UPDATE ON zip_metadata
  FOR EACH ROW EXECUTE FUNCTION set_zip_metadata_updated_at();

CREATE OR REPLACE FUNCTION zip_to_emoji(zip CHAR(4))
RETURNS TEXT AS $$
DECLARE
  orders TEXT[] := ARRAY['','🐂','⛽','🦋','🏟','🌾','⚖','🖼'];
  axes   TEXT[] := ARRAY['','🏛','🔨','🌹','🪐','⌛','🐬'];
  types  TEXT[] := ARRAY['','🛒','🪡','🍗','➕','➖'];
  colors TEXT[] := ARRAY['','⚫','🟢','🔵','🟣','🔴','🟠','🟡','⚪'];
BEGIN
  RETURN
    orders[SUBSTRING(zip,1,1)::int] ||
    axes[SUBSTRING(zip,2,1)::int]   ||
    types[SUBSTRING(zip,3,1)::int]  ||
    colors[SUBSTRING(zip,4,1)::int];
END;
$$ LANGUAGE plpgsql IMMUTABLE;
