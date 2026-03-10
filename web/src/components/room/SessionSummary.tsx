"use client";

import { useEffect, useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

interface SetLog {
  block_name: string;
  exercise_name: string;
  set_number: number;
  reps: number | null;
  weight: number | null;
  unit: string;
  rpe: number | null;
}

export function SessionSummary({ zipCode }: { zipCode: string }) {
  const [logs, setLogs] = useState<SetLog[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) { setLoading(false); return; }

      const todayStart = new Date();
      todayStart.setHours(0, 0, 0, 0);

      // Find today's session
      const { data: session } = await supabase
        .from("workout_sessions")
        .select("id")
        .eq("user_id", user.id)
        .eq("zip_code", zipCode)
        .gte("started_at", todayStart.toISOString())
        .maybeSingle();

      if (session) {
        const { data: fetchedLogs } = await supabase
          .from("set_logs")
          .select("block_name, exercise_name, set_number, reps, weight, unit, rpe")
          .eq("session_id", session.id)
          .order("logged_at", { ascending: true });

        if (fetchedLogs) setLogs(fetchedLogs);
      }

      setLoading(false);
    }
    load();
  }, [zipCode]);

  if (loading || logs.length === 0) return null;

  // Group by exercise
  const grouped = logs.reduce<Record<string, SetLog[]>>((acc, log) => {
    const key = `${log.block_name}:${log.exercise_name}`;
    if (!acc[key]) acc[key] = [];
    acc[key].push(log);
    return acc;
  }, {});

  return (
    <div className="mt-4 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-5">
      <p className="text-xs font-medium uppercase tracking-widest opacity-50">
        Session Recap
      </p>
      <div className="mt-3 space-y-3">
        {Object.entries(grouped).map(([key, sets]) => (
          <div key={key}>
            <p className="text-sm font-medium">{sets[0].exercise_name}</p>
            <p className="text-[10px] opacity-30">{sets[0].block_name}</p>
            <div className="mt-1 space-y-0.5">
              {sets.map((s) => (
                <p key={s.set_number} className="text-xs opacity-60">
                  Set {s.set_number}:{" "}
                  {s.reps && `${s.reps} reps`}
                  {s.weight && ` @ ${s.weight}${s.unit}`}
                  {s.rpe && ` RPE ${s.rpe}`}
                </p>
              ))}
            </div>
          </div>
        ))}
      </div>
      <p className="mt-3 text-xs opacity-30">
        {logs.length} set{logs.length !== 1 ? "s" : ""} logged today
      </p>
    </div>
  );
}
