"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { getSupabaseClient } from "@/lib/supabase/client";

interface SavedRoom {
  id: string;
  zip_code: string;
  notes: string | null;
  saved_at: string;
}

export default function LibraryPage() {
  const router = useRouter();
  const [rooms, setRooms] = useState<SavedRoom[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const supabase = getSupabaseClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) { setLoading(false); return; }

      const { data } = await supabase
        .from("saved_rooms")
        .select("*")
        .eq("user_id", user.id)
        .order("saved_at", { ascending: false });

      if (data) setRooms(data);
      setLoading(false);
    }
    load();
  }, []);

  async function handleUnsave(zipCode: string) {
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    await supabase
      .from("saved_rooms")
      .delete()
      .eq("user_id", user.id)
      .eq("zip_code", zipCode);

    setRooms((prev) => prev.filter((r) => r.zip_code !== zipCode));
  }

  function handleRandom() {
    if (rooms.length === 0) return;
    const pick = rooms[Math.floor(Math.random() * rooms.length)];
    router.push(`/zip/${pick.zip_code}`);
  }

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        <div className="mb-2">
          <Link href="/me" className="text-xs opacity-40 hover:opacity-70">
            Dashboard
          </Link>
        </div>

        <header className="mb-8 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-semibold">Saved Rooms</h1>
            <p className="mt-1 text-sm opacity-50">
              {rooms.length} room{rooms.length !== 1 ? "s" : ""} saved
            </p>
          </div>
          {rooms.length > 0 && (
            <button
              onClick={handleRandom}
              className="rounded-lg bg-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-background)]"
            >
              Random Room
            </button>
          )}
        </header>

        {loading ? (
          <p className="text-sm opacity-40">Loading...</p>
        ) : rooms.length === 0 ? (
          <div className="rounded-xl border border-dashed border-[var(--ppl-border)] p-8 text-center">
            <p className="text-sm opacity-40">No saved rooms yet.</p>
            <p className="mt-1 text-xs opacity-30">
              Save rooms from any workout page to build your library.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
            {rooms.map((room) => (
              <div
                key={room.id}
                className="rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-4"
              >
                <Link
                  href={`/zip/${room.zip_code}`}
                  className="block text-center"
                >
                  <span className="font-mono text-lg">/{room.zip_code}</span>
                </Link>
                <div className="mt-2 flex items-center justify-between">
                  <span className="text-[10px] opacity-30">
                    {new Date(room.saved_at).toLocaleDateString()}
                  </span>
                  <button
                    onClick={() => handleUnsave(room.zip_code)}
                    className="text-[10px] opacity-30 hover:opacity-70"
                  >
                    Remove
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}
