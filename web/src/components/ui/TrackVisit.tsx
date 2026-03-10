"use client";

import { useEffect } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

export function TrackVisit({ zipCode }: { zipCode: string }) {
  useEffect(() => {
    async function track() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return;

      await supabase
        .from("zip_visits")
        .insert({ user_id: user.id, zip_code: zipCode });
    }
    track();
  }, [zipCode]);

  return null;
}
