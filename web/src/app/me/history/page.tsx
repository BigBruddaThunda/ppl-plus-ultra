"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

interface Session {
  id: string;
  zip_code: string;
  started_at: string;
  completed_at: string | null;
  session_rpe: number | null;
  notes: string | null;
  set_count: number;
}

export default function HistoryPage() {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) { setLoading(false); return; }

      // Get sessions
      const { data: sessionData } = await supabase
        .from("workout_sessions")
        .select("*")
        .eq("user_id", user.id)
        .order("started_at", { ascending: false })
        .limit(50);

      if (!sessionData) { setLoading(false); return; }

      // Get set counts per session
      const sessionIds = sessionData.map((s: { id: string }) => s.id);
      const { data: logCounts } = await supabase
        .from("set_logs")
        .select("session_id")
        .in("session_id", sessionIds);

      const countMap: Record<string, number> = {};
      if (logCounts) {
        logCounts.forEach((l: { session_id: string }) => {
          countMap[l.session_id] = (countMap[l.session_id] || 0) + 1;
        });
      }

      setSessions(
        sessionData.map((s: { id: string; zip_code: string; started_at: string; completed_at: string | null; session_rpe: number | null; notes: string | null }) => ({
          ...s,
          set_count: countMap[s.id] || 0,
        }))
      );
      setLoading(false);
    }
    load();
  }, []);

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        <div className="mb-2">
          <Link href="/me" className="text-xs opacity-40 hover:opacity-70">
            Dashboard
          </Link>
        </div>

        <header className="mb-8">
          <h1 className="text-2xl font-semibold">Workout History</h1>
          <p className="mt-1 text-sm opacity-50">
            {sessions.length} session{sessions.length !== 1 ? "s" : ""} logged
          </p>
        </header>

        {loading ? (
          <p className="text-sm opacity-40">Loading...</p>
        ) : sessions.length === 0 ? (
          <div className="rounded-xl border border-dashed border-[var(--ppl-border)] p-8 text-center">
            <p className="text-sm opacity-40">No sessions logged yet.</p>
            <p className="mt-1 text-xs opacity-30">
              Log sets during a workout to see your history here.
            </p>
          </div>
        ) : (
          <div className="space-y-3">
            {sessions.map((session) => (
              <Link
                key={session.id}
                href={`/zip/${session.zip_code}`}
                className="block rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-4 transition-colors hover:border-[var(--ppl-accent)]"
              >
                <div className="flex items-center justify-between">
                  <div>
                    <span className="font-mono text-sm">/{session.zip_code}</span>
                    {session.session_rpe && (
                      <span className="ml-2 text-xs opacity-40">
                        RPE {session.session_rpe}
                      </span>
                    )}
                  </div>
                  <span className="text-xs opacity-40">
                    {session.set_count} set{session.set_count !== 1 ? "s" : ""}
                  </span>
                </div>
                <p className="mt-1 text-xs opacity-40">
                  {new Date(session.started_at).toLocaleDateString(undefined, {
                    weekday: "short",
                    month: "short",
                    day: "numeric",
                  })}
                </p>
                {session.notes && (
                  <p className="mt-1 text-xs opacity-30">{session.notes}</p>
                )}
              </Link>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
