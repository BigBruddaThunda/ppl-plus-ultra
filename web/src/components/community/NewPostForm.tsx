"use client";

import { useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

interface Props {
  zipCode: string;
  userId: string;
  onPosted: () => void;
}

export function NewPostForm({ zipCode, userId, onPosted }: Props) {
  const [body, setBody] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const trimmed = body.trim();
    if (!trimmed || submitting) return;

    setSubmitting(true);
    setError(null);

    const supabase = getSupabaseClient();
    const { error: insertError } = await supabase
      .from("community_posts")
      .insert({
        user_id: userId,
        zip_code: zipCode,
        body: trimmed,
      });

    if (insertError) {
      if (insertError.message.includes("blocked content")) {
        setError("Post contains words that aren't allowed.");
      } else {
        setError("Couldn't post. Try again.");
      }
      setSubmitting(false);
      return;
    }

    setBody("");
    setSubmitting(false);
    onPosted();
  }

  return (
    <form onSubmit={handleSubmit} className="mb-6">
      <textarea
        value={body}
        onChange={(e) => setBody(e.target.value)}
        placeholder="Share something about this room..."
        maxLength={2000}
        rows={3}
        className="w-full rounded-lg border border-[var(--ppl-border)] bg-transparent px-3 py-2 text-sm placeholder:opacity-30 focus:border-[var(--ppl-accent)] focus:outline-none resize-none"
      />
      {error && (
        <p className="mt-1 text-xs text-red-400">{error}</p>
      )}
      <div className="mt-2 flex items-center justify-between">
        <span className="text-[10px] opacity-30">
          {body.length}/2000
        </span>
        <button
          type="submit"
          disabled={!body.trim() || submitting}
          className="rounded-lg bg-[var(--ppl-accent)] px-4 py-1.5 text-xs font-medium text-[var(--ppl-background)] disabled:opacity-30"
        >
          {submitting ? "Posting..." : "Post"}
        </button>
      </div>
    </form>
  );
}
