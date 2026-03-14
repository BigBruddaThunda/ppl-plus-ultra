# SQL Migrations — CX-08 + CX-20 + CX-40 + Community Schema

Executable PostgreSQL 15+ migrations derived from `middle-math/schemas/*.md`.

## Execution Order

1. `001-create-exercise-library.sql`
2. `002-create-exercise-families.sql`
3. `003-create-user-ledger.sql`
4. `004-create-user-profile.sql`
5. `005-create-user-toggles.sql`
6. `006-create-zip-metadata.sql`
7. `007-populate-zip-metadata.sql`
8. `008-room-schema-extension.sql`
9. `009-exercise-registry.sql`
10. `010-exercise-knowledge.sql`
11. `011-wave3-tables.sql`
12. `012-community.sql`

> Run in numeric order. Foreign keys are arranged so references target tables created in earlier files.

## File Mapping to Specs

- `001-create-exercise-library.sql` ← `middle-math/schemas/exercise-library-schema.md`
- `002-create-exercise-families.sql` ← `middle-math/schemas/exercise-families-schema.md`
- `003-create-user-ledger.sql` ← `middle-math/schemas/user-ledger-schema.md`
- `004-create-user-profile.sql` ← `middle-math/schemas/user-profile-schema.md`
- `005-create-user-toggles.sql` ← `middle-math/schemas/user-toggles-schema.md`
- `006-create-zip-metadata.sql` ← `middle-math/schemas/zip-metadata-schema.md`
- `007-populate-zip-metadata.sql` ← `middle-math/schemas/zip-metadata-schema.md` (population section)
- `008-room-schema-extension.sql` ← `seeds/experience-layer-blueprint.md`, `seeds/systems-eudaimonics.md` (CX-20)
- `009-exercise-registry.sql` ← `middle-math/exercise-registry.json` (CX-40 / CX-36)
- `010-exercise-knowledge.sql` ← `exercise-content/` knowledge files (CX-40 / CX-37)

`middle-math/schemas/zip-weight-cache-schema.md` remains optional and is intentionally not materialized in this numbered set.

- `011-wave3-tables.sql` — Onboarding columns, user_equipment, workout_sessions, set_logs, saved_rooms, zip_visits
- `012-community.sql` — community_posts, community_replies, word filter trigger, Realtime, reply count denormalization

## Notes

- RLS policies use `auth.uid()` for user-scoped tables.
- `zip_metadata` includes `zip_to_emoji(zip CHAR(4))` as a PostgreSQL helper.
- `007` inserts all valid numeric zip combinations using a 4-way cross join: 7 × 6 × 5 × 8 = 1,680.
- `008` adds 4 tables for room-level tracking: `rooms` (one row per zip, 1,680 rows), `room_visits` (append-only log), `room_votes` (user quality signals), `bloom_history` (depth transition log). Navigation edges (nav_north/east/south/west) are populated by `scripts/build-navigation-graph.py`.
- `009` creates `exercise_registry`: 2,085 exercises with globally unique IDs (EX-0001–EX-2085), anatomy, family linkage, axis/order affinity, GOLD gate. Self-referencing parent_id for family trees. Requires `pg_trgm` extension for name search index.
- `010` creates `exercise_knowledge`: 1:1 coaching content for each registry entry. Setup cues, execution cues, common faults, Ppl± per-Order context. Auto-populated with EMPTY stub rows from registry at migration time.

## Run Against Supabase

Using Supabase CLI from repo root:

```bash
supabase db push
```

Or apply manually with psql (replace connection string):

```bash
psql "$SUPABASE_DB_URL" -f sql/001-create-exercise-library.sql
psql "$SUPABASE_DB_URL" -f sql/002-create-exercise-families.sql
psql "$SUPABASE_DB_URL" -f sql/003-create-user-ledger.sql
psql "$SUPABASE_DB_URL" -f sql/004-create-user-profile.sql
psql "$SUPABASE_DB_URL" -f sql/005-create-user-toggles.sql
psql "$SUPABASE_DB_URL" -f sql/006-create-zip-metadata.sql
psql "$SUPABASE_DB_URL" -f sql/007-populate-zip-metadata.sql
psql "$SUPABASE_DB_URL" -f sql/008-room-schema-extension.sql
psql "$SUPABASE_DB_URL" -f sql/009-exercise-registry.sql
psql "$SUPABASE_DB_URL" -f sql/010-exercise-knowledge.sql
```

Verify row counts:

```sql
SELECT COUNT(*) FROM zip_metadata;        -- expected: 1680
SELECT COUNT(*) FROM rooms;               -- expected: 1680
SELECT COUNT(*) FROM exercise_registry;   -- expected: 2085
SELECT COUNT(*) FROM exercise_knowledge WHERE status = 'EMPTY';  -- expected: 2085 initially
```
