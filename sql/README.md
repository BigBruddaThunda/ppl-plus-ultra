# SQL Migrations — CX-08 Schema Materialization

Executable PostgreSQL 15+ migrations derived from `middle-math/schemas/*.md`.

## Execution Order

1. `001-create-exercise-library.sql`
2. `002-create-exercise-families.sql`
3. `003-create-user-ledger.sql`
4. `004-create-user-profile.sql`
5. `005-create-user-toggles.sql`
6. `006-create-zip-metadata.sql`
7. `007-populate-zip-metadata.sql`

> Run in numeric order. Foreign keys are arranged so references target tables created in earlier files.

## File Mapping to Specs

- `001-create-exercise-library.sql` ← `middle-math/schemas/exercise-library-schema.md`
- `002-create-exercise-families.sql` ← `middle-math/schemas/exercise-families-schema.md`
- `003-create-user-ledger.sql` ← `middle-math/schemas/user-ledger-schema.md`
- `004-create-user-profile.sql` ← `middle-math/schemas/user-profile-schema.md`
- `005-create-user-toggles.sql` ← `middle-math/schemas/user-toggles-schema.md`
- `006-create-zip-metadata.sql` ← `middle-math/schemas/zip-metadata-schema.md`
- `007-populate-zip-metadata.sql` ← `middle-math/schemas/zip-metadata-schema.md` (population section)

`middle-math/schemas/zip-weight-cache-schema.md` remains optional and is intentionally not materialized in this numbered set.

## Notes

- RLS policies use `auth.uid()` for user-scoped tables.
- `zip_metadata` includes `zip_to_emoji(zip CHAR(4))` as a PostgreSQL helper.
- `007` inserts all valid numeric zip combinations using a 4-way cross join: 7 × 6 × 5 × 8 = 1,680.

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
```

Verify zip row count:

```sql
SELECT COUNT(*) FROM zip_metadata;
-- expected: 1680
```
