"use client";

import { useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";
import { ReplyThread } from "./ReplyThread";
import type { CommunityPost } from "./CommunityFeed";

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
  post: CommunityPost;
  userTier: number;
  userId: string | null;
  onDeleted: () => void;
}

export function PostCard({ post, userTier, userId, onDeleted }: Props) {
  const [showReplies, setShowReplies] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const isOwner = userId === post.user_id;

  async function handleDelete() {
    if (!confirm("Delete this post?")) return;
    setDeleting(true);
    const supabase = getSupabaseClient();
    await supabase.from("community_posts").delete().eq("id", post.id);
    onDeleted();
  }

  return (
    <article className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-4">
      {/* Header */}
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          <span className="text-xs font-medium opacity-70">
            {isOwner ? "you" : "member"}
          </span>
          <span className="text-[10px] opacity-30">
            {timeAgo(post.created_at)}
          </span>
        </div>
        {isOwner && (
          <button
            onClick={handleDelete}
            disabled={deleting}
            className="text-[10px] opacity-30 hover:opacity-70 hover:text-red-400"
          >
            {deleting ? "..." : "delete"}
          </button>
        )}
      </div>

      {/* Body */}
      <p className="text-sm whitespace-pre-wrap break-words">
        {post.body}
      </p>

      {/* Reply toggle */}
      <div className="mt-3 flex items-center gap-3">
        <button
          onClick={() => setShowReplies(!showReplies)}
          className="text-[11px] opacity-40 hover:opacity-70"
        >
          {showReplies
            ? "hide replies"
            : post.reply_count > 0
              ? `${post.reply_count} ${post.reply_count === 1 ? "reply" : "replies"}`
              : "reply"}
        </button>
      </div>

      {/* Reply thread */}
      {showReplies && (
        <ReplyThread
          postId={post.id}
          userTier={userTier}
          userId={userId}
        />
      )}
    </article>
  );
}
