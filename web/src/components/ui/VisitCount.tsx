"use client";

import { useEffect, useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

export function VisitCount({ zipCode }: { zipCode: string }) {
  const [count, setCount] = useState<number | null>(null);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) return;

      const { count } = await supabase
        .from("zip_visits")
        .select("*", { count: "exact", head: true })
        .eq("user_id", user.id)
        .eq("zip_code", zipCode);

      setCount(count);
    }
    load();
  }, [zipCode]);

  if (count === null || count === 0) return null;

  return (
    <span className="text-xs opacity-40">
      Visited {count} time{count !== 1 ? "s" : ""}
    </span>
  );
}
