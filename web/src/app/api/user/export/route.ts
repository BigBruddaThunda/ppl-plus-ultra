import { NextResponse } from "next/server";
import { getAuthUser, getSupabaseServer } from "@/lib/supabase/server";

export async function GET() {
  const user = await getAuthUser();
  if (!user) return NextResponse.json({ error: "Not authenticated" }, { status: 401 });

  const supabase = await getSupabaseServer();

  const [profile, equipment, sessions, setLogs, saved, visits] = await Promise.all([
    supabase.from("profiles").select("*").eq("id", user.id).single(),
    supabase.from("user_equipment").select("*").eq("user_id", user.id),
    supabase.from("workout_sessions").select("*").eq("user_id", user.id),
    supabase.from("set_logs").select("*").eq("user_id", user.id),
    supabase.from("saved_rooms").select("*").eq("user_id", user.id),
    supabase.from("zip_visits").select("*").eq("user_id", user.id),
  ]);

  const exportData = {
    exported_at: new Date().toISOString(),
    user: { id: user.id, email: user.email },
    profile: profile.data,
    equipment: equipment.data,
    workout_sessions: sessions.data,
    set_logs: setLogs.data,
    saved_rooms: saved.data,
    zip_visits: visits.data,
  };

  return new NextResponse(JSON.stringify(exportData, null, 2), {
    headers: {
      "Content-Type": "application/json",
      "Content-Disposition": `attachment; filename="ppl-export-${new Date().toISOString().slice(0, 10)}.json"`,
    },
  });
}
