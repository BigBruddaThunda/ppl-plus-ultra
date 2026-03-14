"use client";

import { useEffect, useState, useCallback } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";
import { PostCard } from "./PostCard";
import { NewPostForm } from "./NewPostForm";

export interface CommunityPost {
  id: string;
  user_id: string;
  zip_code: string;
  body: string;
  reply_count: number;
  created_at: string;
}

interface Props {
  zipCode: string;
  userTier: number;
  userId: string | null;
}

export function CommunityFeed({ zipCode, userTier, userId }: Props) {
  const [posts, setPosts] = useState<CommunityPost[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchPosts = useCallback(async () => {
    const supabase = getSupabaseClient();
    const { data } = await supabase
      .from("community_posts")
      .select("id, user_id, zip_code, body, reply_count, created_at")
      .eq("zip_code", zipCode)
      .order("created_at", { ascending: false })
      .limit(50);

    if (data) setPosts(data as CommunityPost[]);
    setLoading(false);
  }, [zipCode]);

  useEffect(() => {
    fetchPosts();
  }, [fetchPosts]);

  // Realtime subscription
  useEffect(() => {
    const supabase = getSupabaseClient();
    const channel = supabase
      .channel(`community:${zipCode}`)
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "community_posts",
          filter: `zip_code=eq.${zipCode}`,
        },
        () => {
          // Refetch on any change — simple and correct
          fetchPosts();
        }
      )
      .subscribe();

    return () => {
      supabase.removeChannel(channel);
    };
  }, [zipCode, fetchPosts]);

  if (loading) {
    return (
      <div className="py-8 text-center text-sm opacity-40">
        Loading...
      </div>
    );
  }

  return (
    <div>
      {/* New post form — Tier 2 only */}
      {userTier >= 2 && userId && (
        <NewPostForm zipCode={zipCode} userId={userId} onPosted={fetchPosts} />
      )}

      {/* Tier 1 upgrade nudge */}
      {userTier === 1 && (
        <div className="mb-4 rounded-lg border border-[var(--ppl-border)] p-4 text-center">
          <p className="text-sm opacity-60">
            Upgrade to Community Pass to post and reply.
          </p>
          <a
            href="/subscribe"
            className="mt-2 inline-block rounded-lg bg-[var(--ppl-accent)] px-4 py-1.5 text-xs font-medium text-[var(--ppl-background)]"
          >
            Upgrade
          </a>
        </div>
      )}

      {/* Posts */}
      {posts.length === 0 ? (
        <p className="py-8 text-center text-sm opacity-40">
          No posts in this room yet.{" "}
          {userTier >= 2 ? "Be the first." : ""}
        </p>
      ) : (
        <div className="space-y-3">
          {posts.map((post) => (
            <PostCard
              key={post.id}
              post={post}
              userTier={userTier}
              userId={userId}
              onDeleted={fetchPosts}
            />
          ))}
        </div>
      )}
    </div>
  );
}
