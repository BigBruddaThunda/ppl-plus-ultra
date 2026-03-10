import { NextResponse } from "next/server";
import { getAuthUser, getSupabaseServer } from "@/lib/supabase/server";
import { stripe } from "@/lib/stripe";
import { createClient } from "@supabase/supabase-js";

function getServiceSupabase() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!
  );
}

export async function DELETE(request: Request) {
  const user = await getAuthUser();
  if (!user) return NextResponse.json({ error: "Not authenticated" }, { status: 401 });

  const body = await request.json();
  if (body.confirmation !== "DELETE MY ACCOUNT") {
    return NextResponse.json({ error: "Confirmation required" }, { status: 400 });
  }

  const supabase = await getSupabaseServer();
  const serviceSupabase = getServiceSupabase();

  // Cancel Stripe subscription if exists
  const { data: profile } = await supabase
    .from("profiles")
    .select("stripe_subscription_id")
    .eq("id", user.id)
    .single();

  if (profile?.stripe_subscription_id) {
    try {
      await stripe.subscriptions.cancel(profile.stripe_subscription_id);
    } catch {
      // Subscription may already be cancelled
    }
  }

  // Delete user data (cascades via FK ON DELETE CASCADE)
  // But we explicitly clean up to be thorough
  await Promise.all([
    supabase.from("set_logs").delete().eq("user_id", user.id),
    supabase.from("workout_sessions").delete().eq("user_id", user.id),
    supabase.from("saved_rooms").delete().eq("user_id", user.id),
    supabase.from("zip_visits").delete().eq("user_id", user.id),
    supabase.from("user_equipment").delete().eq("user_id", user.id),
  ]);

  // Delete profile
  await serviceSupabase.from("profiles").delete().eq("id", user.id);

  // Delete auth user (requires service role)
  await serviceSupabase.auth.admin.deleteUser(user.id);

  return NextResponse.json({ deleted: true });
}
