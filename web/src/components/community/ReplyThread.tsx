"use client";

import { useEffect, useState, useCallback } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

interface Reply {
  id: string;
  post_id: string;
  user_id: string;
  body: string;
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
  postId: string;
  userTier: number;
  userId: string | null;
}

export function ReplyThread({ postId, userTier, userId }: Props) {
  const [replies, setReplies] = useState<Reply[]>([]);
  const [loading, setLoading] = useState(true);
  const [body, setBody] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchReplies = useCallback(async () => {
    const supabase = getSupabaseClient();
    const { data } = await supabase
      .from("community_replies")
      .select("id, post_id, user_id, body, created_at")
      .eq("post_id", postId)
      .order("created_at", { ascending: true })
      .limit(100);

    if (data) setReplies(data as Reply[]);
    setLoading(false);
  }, [postId]);

  useEffect(() => {
    fetchReplies();
  }, [fetchReplies]);

  // Realtime for replies
  useEffect(() => {
    const supabase = getSupabaseClient();
    const channel = supabase
      .channel(`replies:${postId}`)
      .on(
        "postgres_changes",
        {
          event: "*",
          schema: "public",
          table: "community_replies",
          filter: `post_id=eq.${postId}`,
        },
        () => {
          fetchReplies();
        }
      )
      .subscribe();

    return () => {
      supabase.removeChannel(channel);
    };
  }, [postId, fetchReplies]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const trimmed = body.trim();
    if (!trimmed || submitting || !userId) return;

    setSubmitting(true);
    setError(null);

    const supabase = getSupabaseClient();
    const { error: insertError } = await supabase
      .from("community_replies")
      .insert({
        post_id: postId,
        user_id: userId,
        body: trimmed,
      });

    if (insertError) {
      if (insertError.message.includes("blocked content")) {
        setError("Reply contains words that aren't allowed.");
      } else {
        setError("Couldn't reply. Try again.");
      }
      setSubmitting(false);
      return;
    }

    setBody("");
    setSubmitting(false);
    fetchReplies();
  }

  async function handleDeleteReply(replyId: string) {
    const supabase = getSupabaseClient();
    await supabase.from("community_replies").delete().eq("id", replyId);
    fetchReplies();
  }

  if (loading) {
    return <div className="mt-3 text-xs opacity-30">Loading replies...</div>;
  }

  return (
    <div className="mt-3 border-t border-[var(--ppl-border)] pt-3">
      {/* Replies list */}
      {replies.length > 0 && (
        <div className="space-y-2 mb-3">
          {replies.map((reply) => (
            <div key={reply.id} className="flex gap-2 text-xs">
              <div className="flex-1">
                <span className="font-medium opacity-70">
                  {userId === reply.user_id ? "you" : "member"}
                </span>
                <span className="opacity-30 ml-1.5">
                  {timeAgo(reply.created_at)}
                </span>
                <p className="mt-0.5 opacity-80 whitespace-pre-wrap break-words">
                  {reply.body}
                </p>
              </div>
              {userId === reply.user_id && (
                <button
                  onClick={() => handleDeleteReply(reply.id)}
                  className="text-[10px] opacity-20 hover:opacity-60 hover:text-red-400 shrink-0"
                >
                  x
                </button>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Reply input — Tier 2 only */}
      {userTier >= 2 && userId ? (
        <form onSubmit={handleSubmit} className="flex gap-2">
          <input
            type="text"
            value={body}
            onChange={(e) => setBody(e.target.value)}
            placeholder="Reply..."
            maxLength={1000}
            className="flex-1 rounded-md border border-[var(--ppl-border)] bg-transparent px-2 py-1 text-xs placeholder:opacity-30 focus:border-[var(--ppl-accent)] focus:outline-none"
          />
          <button
            type="submit"
            disabled={!body.trim() || submitting}
            className="rounded-md bg-[var(--ppl-accent)] px-3 py-1 text-[10px] font-medium text-[var(--ppl-background)] disabled:opacity-30"
          >
            {submitting ? "..." : "Reply"}
          </button>
          {error && (
            <span className="text-[10px] text-red-400 self-center">{error}</span>
          )}
        </form>
      ) : userTier === 1 ? (
        <p className="text-[10px] opacity-30">
          Upgrade to Community Pass to reply.
        </p>
      ) : null}
    </div>
  );
}
