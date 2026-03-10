-- Wave 3 Migration: Onboarding + Logging + Saved Rooms
-- Run this in Supabase SQL Editor
-- Depends on: profiles table (already exists)

-- =============================================================================
-- 1. Add onboarding + region columns to profiles
-- =============================================================================

ALTER TABLE public.profiles
  ADD COLUMN IF NOT EXISTS region TEXT,
  ADD COLUMN IF NOT EXISTS onboarding_complete BOOLEAN DEFAULT false;

-- =============================================================================
-- 2. Equipment toggles (simplified from 005 — no exercise_library FK)
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.user_equipment (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  tier        INTEGER NOT NULL CHECK (tier BETWEEN 0 AND 5),
  available   BOOLEAN NOT NULL DEFAULT true,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE (user_id, tier)
);

ALTER TABLE public.user_equipment ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users manage own equipment"
  ON public.user_equipment FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- =============================================================================
-- 3. Workout sessions + set logs
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.workout_sessions (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code      TEXT NOT NULL,
  started_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at  TIMESTAMPTZ,
  session_rpe   NUMERIC(3,1) CHECK (session_rpe IS NULL OR session_rpe BETWEEN 1.0 AND 10.0),
  notes         TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE public.workout_sessions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users manage own sessions"
  ON public.workout_sessions FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_sessions_user ON public.workout_sessions (user_id, started_at DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_zip ON public.workout_sessions (user_id, zip_code);

CREATE TABLE IF NOT EXISTS public.set_logs (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id    UUID NOT NULL REFERENCES public.workout_sessions(id) ON DELETE CASCADE,
  user_id       UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  block_name    TEXT NOT NULL,
  exercise_name TEXT NOT NULL,
  set_number    INTEGER NOT NULL CHECK (set_number > 0),
  reps          INTEGER CHECK (reps IS NULL OR reps > 0),
  weight        NUMERIC(7,2) CHECK (weight IS NULL OR weight >= 0),
  unit          TEXT NOT NULL DEFAULT 'lbs' CHECK (unit IN ('kg', 'lbs')),
  rpe           NUMERIC(3,1) CHECK (rpe IS NULL OR rpe BETWEEN 1.0 AND 10.0),
  notes         TEXT,
  logged_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE public.set_logs ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users manage own set logs"
  ON public.set_logs FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_set_logs_session ON public.set_logs (session_id);
CREATE INDEX IF NOT EXISTS idx_set_logs_user ON public.set_logs (user_id, logged_at DESC);

-- =============================================================================
-- 4. Saved rooms
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.saved_rooms (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code    TEXT NOT NULL,
  notes       TEXT,
  saved_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE (user_id, zip_code)
);

ALTER TABLE public.saved_rooms ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users manage own saved rooms"
  ON public.saved_rooms FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_saved_rooms_user ON public.saved_rooms (user_id, saved_at DESC);

-- =============================================================================
-- 5. Zip visits (auto-tracked room views)
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.zip_visits (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code    TEXT NOT NULL,
  visited_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE public.zip_visits ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users read own visits"
  ON public.zip_visits FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users insert own visits"
  ON public.zip_visits FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_zip_visits_user ON public.zip_visits (user_id, zip_code);
CREATE INDEX IF NOT EXISTS idx_zip_visits_at ON public.zip_visits (user_id, visited_at DESC);

-- =============================================================================
-- VERIFICATION
-- =============================================================================
SELECT 'Wave 3 migration complete' AS status;
