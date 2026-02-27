# Zip Metadata Schema — Numeric Primary Key

Status: DRAFT — Uses 4-digit numeric zip code as primary key per `seeds/numeric-zip-system.md`.

---

## Table Definition

```sql
CREATE TABLE zip_metadata (
  -- Primary key: 4-digit numeric zip code
  zip_code         CHAR(4) PRIMARY KEY
    CHECK (
      SUBSTRING(zip_code, 1, 1) BETWEEN '1' AND '7' AND -- Order: 1-7
      SUBSTRING(zip_code, 2, 1) BETWEEN '1' AND '6' AND -- Axis: 1-6
      SUBSTRING(zip_code, 3, 1) BETWEEN '1' AND '5' AND -- Type: 1-5
      SUBSTRING(zip_code, 4, 1) BETWEEN '1' AND '8'     -- Color: 1-8
    ),

  -- Dial positions (decomposed for indexed filtering)
  order_position   SMALLINT NOT NULL CHECK (order_position BETWEEN 1 AND 7),
  axis_position    SMALLINT NOT NULL CHECK (axis_position BETWEEN 1 AND 6),
  type_position    SMALLINT NOT NULL CHECK (type_position BETWEEN 1 AND 5),
  color_position   SMALLINT NOT NULL CHECK (color_position BETWEEN 1 AND 8),

  -- Deck reference
  deck_number      SMALLINT NOT NULL
    CHECK (deck_number BETWEEN 1 AND 42)
    GENERATED ALWAYS AS ((order_position - 1) * 6 + axis_position) STORED,

  -- Card status (matches SCL status convention)
  card_status      TEXT NOT NULL DEFAULT 'EMPTY'
    CHECK (card_status IN ('EMPTY', 'GENERATED', 'CANONICAL')),

  -- Operator (from Axis × Color polarity table)
  operator_emoji   TEXT,   -- e.g. '🤌'
  operator_name    TEXT,   -- e.g. 'facio'

  -- Card content (populated when card_status = GENERATED or CANONICAL)
  card_title       TEXT,   -- e.g. 'Heavy Classic Pulls'
  markdown_content TEXT,   -- full .md card content

  -- Middle-math computation outputs
  weight_vector    JSONB,  -- 61-value weight vector from middle-math/ARCHITECTURE.md
  primary_palette  JSONB,  -- { primary: '#hex', secondary: '#hex', accent: '#hex', text: '#hex' }

  -- Block structure
  block_sequence   TEXT[], -- e.g. ARRAY['♨️','▶️','🧈','🧩','🪫','🚂']

  -- Timestamps
  created_at       TIMESTAMPTZ DEFAULT NOW(),
  updated_at       TIMESTAMPTZ DEFAULT NOW()
);
```

---

## Indexes

```sql
-- Dial position indexes (for filtered browsing)
CREATE INDEX idx_zip_order   ON zip_metadata (order_position);
CREATE INDEX idx_zip_axis    ON zip_metadata (axis_position);
CREATE INDEX idx_zip_type    ON zip_metadata (type_position);
CREATE INDEX idx_zip_color   ON zip_metadata (color_position);
CREATE INDEX idx_zip_deck    ON zip_metadata (deck_number);
CREATE INDEX idx_zip_status  ON zip_metadata (card_status);

-- Composite index for deck × type filtering (common pattern: browse a deck's pull/push/legs)
CREATE INDEX idx_zip_deck_type ON zip_metadata (deck_number, type_position);

-- Composite index for Order × Type browsing (see all push workouts across all strength days)
CREATE INDEX idx_zip_order_type ON zip_metadata (order_position, type_position);
```

---

## Population Script

Generates all 1,680 valid zip codes via cross-join of the 4 dial ranges:

```sql
-- Generate all 1,680 zip rows
INSERT INTO zip_metadata (zip_code, order_position, axis_position, type_position, color_position)
SELECT
  CONCAT(o::text, a::text, t::text, c::text) AS zip_code,
  o AS order_position,
  a AS axis_position,
  t AS type_position,
  c AS color_position
FROM
  generate_series(1, 7) AS o,  -- Orders 1-7
  generate_series(1, 6) AS a,  -- Axes 1-6
  generate_series(1, 5) AS t,  -- Types 1-5
  generate_series(1, 8) AS c   -- Colors 1-8
ON CONFLICT (zip_code) DO NOTHING;

-- Verify count
SELECT COUNT(*) FROM zip_metadata;
-- Expected: 1680
```

**Verification:** 7 × 6 × 5 × 8 = 1,680. The cross-join produces exactly this count with no duplicates because the 4-digit zip code is deterministically derived from the four positions.

---

## Emoji Display Function

The emoji is derived at the application layer, not stored in the database. The conversion function (from `seeds/numeric-zip-system.md`) runs client-side.

```sql
-- Optional: PostgreSQL helper function if emoji display needed in SQL queries
CREATE OR REPLACE FUNCTION zip_to_emoji(zip CHAR(4)) RETURNS TEXT AS $$
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

-- Example: SELECT zip_to_emoji('2123'); → '⛽🏛🪡🔵'
```

---

## Foreign Key Pattern

All tables that reference a specific room use `CHAR(4)` foreign keys to `zip_metadata`:

```sql
-- workout_logs: which room was logged
ALTER TABLE workout_logs ADD COLUMN
  zip_code CHAR(4) REFERENCES zip_metadata(zip_code);

-- saved_workouts: which room is saved
ALTER TABLE saved_workouts ADD COLUMN
  zip_code CHAR(4) REFERENCES zip_metadata(zip_code);

-- zip_visits: which room was visited
CREATE TABLE zip_visits (
  id        BIGSERIAL PRIMARY KEY,
  user_id   UUID REFERENCES auth.users(id),
  zip_code  CHAR(4) REFERENCES zip_metadata(zip_code),
  visited_at TIMESTAMPTZ DEFAULT NOW()
);

-- program_sequence: which rooms are in a user's program
CREATE TABLE program_sequence (
  id          BIGSERIAL PRIMARY KEY,
  user_id     UUID REFERENCES auth.users(id),
  zip_code    CHAR(4) REFERENCES zip_metadata(zip_code),
  sequence_position SMALLINT,
  scheduled_date    DATE
);

-- community_posts: which room a post belongs to
ALTER TABLE community_posts ADD COLUMN
  zip_code CHAR(4) REFERENCES zip_metadata(zip_code);

-- room_threads (alias for community in zip context)
CREATE TABLE room_threads (
  id       BIGSERIAL PRIMARY KEY,
  zip_code CHAR(4) REFERENCES zip_metadata(zip_code),
  -- thread content columns...
);
```

Referential integrity is enforced at the database level. A zip code that does not exist in `zip_metadata` cannot be referenced in any of these tables. Since the population script pre-generates all 1,680 valid zips, any valid zip can be referenced immediately.

---

## Row Level Security

```sql
-- zip_metadata: public read, no user writes (content managed by admin/CI pipeline)
ALTER TABLE zip_metadata ENABLE ROW LEVEL SECURITY;

CREATE POLICY "zip_metadata_public_read"
  ON zip_metadata FOR SELECT
  TO authenticated, anon
  USING (true);

-- No INSERT/UPDATE/DELETE policy for application users.
-- Card content is written via service role key from the build pipeline.
```

---

## Updated_at Trigger

```sql
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER zip_metadata_updated_at
  BEFORE UPDATE ON zip_metadata
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

---

## Relationship to Card Files

When a `.md` card in the repository is:
- **EMPTY:** `zip_metadata.card_status = 'EMPTY'`, `markdown_content = NULL`
- **GENERATED:** `zip_metadata.card_status = 'GENERATED'`, `markdown_content = [full card text]`
- **CANONICAL:** `zip_metadata.card_status = 'CANONICAL'`, `markdown_content = [verified card text]`

The sync between `.md` files and the database is managed by the build pipeline (CI/CD or manual import script). Card generation remains the authoritative source; the database is the rendered/queryable layer.

---

## See Also

- `seeds/numeric-zip-system.md` — Numeric addressing standard
- `middle-math/ARCHITECTURE.md` Section 8 — Integration with weight vector computation
- `middle-math/schemas/zip-weight-cache-schema.md` — Optional pre-computed weight cache
- `seeds/experience-layer-blueprint.md` — Rendering pipeline that uses this schema
