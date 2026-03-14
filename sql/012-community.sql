-- Community Floor Migration: Posts + Replies
-- Run this in Supabase SQL Editor
-- Depends on: profiles table with tier column

-- =============================================================================
-- 1. Community posts — one board per zip code (1,680 rooms)
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.community_posts (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  zip_code    TEXT NOT NULL,
  body        TEXT NOT NULL CHECK (char_length(body) BETWEEN 1 AND 2000),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE public.community_posts ENABLE ROW LEVEL SECURITY;

-- Anyone authenticated can read posts (tier gating is in the app layer)
CREATE POLICY "Authenticated users read posts"
  ON public.community_posts FOR SELECT
  USING (auth.uid() IS NOT NULL);

-- Tier 2 users can create posts
CREATE POLICY "Tier 2 users create posts"
  ON public.community_posts FOR INSERT
  WITH CHECK (
    auth.uid() = user_id
    AND EXISTS (
      SELECT 1 FROM public.profiles
      WHERE id = auth.uid() AND tier >= 2
    )
  );

-- Users can update their own posts
CREATE POLICY "Users update own posts"
  ON public.community_posts FOR UPDATE
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Users can delete their own posts
CREATE POLICY "Users delete own posts"
  ON public.community_posts FOR DELETE
  USING (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_community_posts_zip
  ON public.community_posts (zip_code, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_community_posts_user
  ON public.community_posts (user_id, created_at DESC);

-- =============================================================================
-- 2. Community replies — threaded under posts
-- =============================================================================

CREATE TABLE IF NOT EXISTS public.community_replies (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  post_id     UUID NOT NULL REFERENCES public.community_posts(id) ON DELETE CASCADE,
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  body        TEXT NOT NULL CHECK (char_length(body) BETWEEN 1 AND 1000),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE public.community_replies ENABLE ROW LEVEL SECURITY;

-- Anyone authenticated can read replies
CREATE POLICY "Authenticated users read replies"
  ON public.community_replies FOR SELECT
  USING (auth.uid() IS NOT NULL);

-- Tier 2 users can create replies
CREATE POLICY "Tier 2 users create replies"
  ON public.community_replies FOR INSERT
  WITH CHECK (
    auth.uid() = user_id
    AND EXISTS (
      SELECT 1 FROM public.profiles
      WHERE id = auth.uid() AND tier >= 2
    )
  );

-- Users can delete their own replies
CREATE POLICY "Users delete own replies"
  ON public.community_replies FOR DELETE
  USING (auth.uid() = user_id);

CREATE INDEX IF NOT EXISTS idx_community_replies_post
  ON public.community_replies (post_id, created_at ASC);

CREATE INDEX IF NOT EXISTS idx_community_replies_user
  ON public.community_replies (user_id);

-- =============================================================================
-- 3. Word filter function — auto-block obvious content
-- =============================================================================

CREATE OR REPLACE FUNCTION public.check_word_filter()
RETURNS TRIGGER AS $$
DECLARE
  blocked_words TEXT[] := ARRAY[
    'fuck', 'shit', 'ass', 'bitch', 'dick', 'cunt',
    'faggot', 'nigger', 'nigga', 'retard', 'kike', 'chink',
    'spic', 'wetback', 'tranny'
  ];
  word TEXT;
  lower_body TEXT;
BEGIN
  lower_body := lower(NEW.body);
  FOREACH word IN ARRAY blocked_words LOOP
    IF lower_body ~ ('\m' || word || '\M') THEN
      RAISE EXCEPTION 'Post contains blocked content.';
    END IF;
  END LOOP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER filter_post_words
  BEFORE INSERT OR UPDATE ON public.community_posts
  FOR EACH ROW EXECUTE FUNCTION public.check_word_filter();

CREATE TRIGGER filter_reply_words
  BEFORE INSERT OR UPDATE ON public.community_replies
  FOR EACH ROW EXECUTE FUNCTION public.check_word_filter();

-- =============================================================================
-- 4. Enable Realtime on community tables
-- =============================================================================

ALTER PUBLICATION supabase_realtime ADD TABLE public.community_posts;
ALTER PUBLICATION supabase_realtime ADD TABLE public.community_replies;

-- =============================================================================
-- 5. Reply count helper (denormalized for performance)
-- =============================================================================

ALTER TABLE public.community_posts
  ADD COLUMN IF NOT EXISTS reply_count INTEGER NOT NULL DEFAULT 0;

CREATE OR REPLACE FUNCTION public.update_reply_count()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    UPDATE public.community_posts
      SET reply_count = reply_count + 1
      WHERE id = NEW.post_id;
  ELSIF TG_OP = 'DELETE' THEN
    UPDATE public.community_posts
      SET reply_count = reply_count - 1
      WHERE id = OLD.post_id;
  END IF;
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_post_reply_count
  AFTER INSERT OR DELETE ON public.community_replies
  FOR EACH ROW EXECUTE FUNCTION public.update_reply_count();

-- =============================================================================
-- VERIFICATION
-- =============================================================================
SELECT 'Community migration complete' AS status;
