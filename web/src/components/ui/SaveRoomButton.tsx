"use client";

import { useEffect, useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

export function SaveRoomButton({ zipCode }: { zipCode: string }) {
  const [saved, setSaved] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function check() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) { setLoading(false); return; }

      const { data } = await supabase
        .from("saved_rooms")
        .select("id")
        .eq("user_id", user.id)
        .eq("zip_code", zipCode)
        .maybeSingle();

      setSaved(!!data);
      setLoading(false);
    }
    check();
  }, [zipCode]);

  async function toggle() {
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    if (saved) {
      await supabase
        .from("saved_rooms")
        .delete()
        .eq("user_id", user.id)
        .eq("zip_code", zipCode);
      setSaved(false);
    } else {
      await supabase
        .from("saved_rooms")
        .insert({ user_id: user.id, zip_code: zipCode });
      setSaved(true);
    }
  }

  if (loading) return null;

  return (
    <button
      onClick={toggle}
      className={`rounded-lg border px-3 py-1.5 text-xs font-medium transition-colors ${
        saved
          ? "border-[var(--ppl-accent)] text-[var(--ppl-accent)]"
          : "border-[var(--ppl-border)] opacity-50 hover:opacity-100"
      }`}
    >
      {saved ? "Saved" : "Save Room"}
    </button>
  );
}
