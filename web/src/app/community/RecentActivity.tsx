"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { getSupabaseClient } from "@/lib/supabase/client";

interface RecentPost {
  id: string;
  zip_code: string;
  body: string;
  reply_count: number;
  created_at: string;
}

function timeAgo(dateStr: string): string {
  const seconds = Math.floor(
    (Date.now() - new Date(dateStr).getTime()) / 1000
  );
  if (seconds < 60) return "just now";
  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  if (days < 30) return `${days}d ago`;
  return new Date(dateStr).toLocaleDateString();
}

interface Props {
  userTier: number;
  userId: string;
}

export function RecentActivity({ userTier }: Props) {
  const [posts, setPosts] = useState<RecentPost[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data } = await supabase
        .from("community_posts")
        .select("id, zip_code, body, reply_count, created_at")
        .order("created_at", { ascending: false })
        .limit(50);

      if (data) setPosts(data as RecentPost[]);
      setLoading(false);
    }
    load();
  }, []);

  if (loading) {
    return <div className="py-8 text-center text-sm opacity-40">Loading...</div>;
  }

  if (posts.length === 0) {
    return (
      <div className="rounded-xl border border-[var(--ppl-border)] p-8 text-center">
        <p className="text-sm opacity-40">
          No community activity yet. Visit a room and start the conversation.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {userTier === 1 && (
        <div className="rounded-lg border border-[var(--ppl-border)] p-4 text-center mb-4">
          <p className="text-sm opacity-60">
            You can read posts. Upgrade to Community Pass to participate.
          </p>
          <Link
            href="/subscribe"
            className="mt-2 inline-block rounded-lg bg-[var(--ppl-accent)] px-4 py-1.5 text-xs font-medium text-[var(--ppl-background)]"
          >
            Upgrade
          </Link>
        </div>
      )}

      {posts.map((post) => (
        <Link
          key={post.id}
          href={`/zip/${post.zip_code}/community`}
          className="block rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-4 hover:border-[var(--ppl-accent)] transition-colors"
        >
          <div className="flex items-center justify-between mb-1.5">
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono opacity-50">
                Room {post.zip_code}
              </span>
              <span className="text-[10px] opacity-30">
                {timeAgo(post.created_at)}
              </span>
            </div>
            {post.reply_count > 0 && (
              <span className="text-[10px] opacity-40">
                {post.reply_count} {post.reply_count === 1 ? "reply" : "replies"}
              </span>
            )}
          </div>
          <p className="text-sm opacity-80 line-clamp-2">
            {post.body}
          </p>
        </Link>
      ))}
    </div>
  );
}
