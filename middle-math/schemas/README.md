# Database Schemas

Table definitions for the middle-math computation layer.

These schemas define the data structures that make the weight system, exercise engine, user context, and rotation engine computable in a production database environment (PostgreSQL via Supabase, per `seeds/platform-architecture-v2.md`).

## Files

- `exercise-library-schema.md` — Enhanced exercise_library table with weight and family columns
- `exercise-families-schema.md` — Movement family tree table
- `user-ledger-schema.md` — user_exercise_ledger table (raw workout logs)
- `user-profile-schema.md` — user_exercise_profile computed view (derived stats)
- `user-toggles-schema.md` — user_exercise_toggles table
- `zip-weight-cache-schema.md` — Optional pre-computed weight vector table (OPTIONAL)
- `zip-metadata-schema.md` — Master room registry: CHAR(4) numeric primary key, dial position columns, CHECK constraints, indexes, 1,680-row population script, foreign key pattern for all referencing tables

## Technology Stack Note

Per `seeds/platform-architecture-v2.md`: PostgreSQL via Supabase. JSONB columns used for variable-length weight data. Materialized views for profile computation. Row-level security for user data isolation.

🧮
