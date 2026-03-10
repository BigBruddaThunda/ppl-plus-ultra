import { NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";
import { createClient } from "@supabase/supabase-js";
import { getAuthUser } from "@/lib/supabase/server";

function getServiceSupabase() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!
  );
}

function tierFromPriceId(priceId: string): number {
  if (priceId === process.env.STRIPE_TIER1_PRICE_ID) return 1;
  if (priceId === process.env.STRIPE_TIER2_PRICE_ID) return 2;
  return 0;
}

export async function GET(request: Request) {
  const user = await getAuthUser();
  if (!user) {
    return NextResponse.json({ error: "Not authenticated" }, { status: 401 });
  }

  const { searchParams } = new URL(request.url);
  const sessionId = searchParams.get("session_id");

  if (!sessionId) {
    return NextResponse.json({ error: "Missing session_id" }, { status: 400 });
  }

  const session = await stripe.checkout.sessions.retrieve(sessionId);

  // Verify this session belongs to this user
  if (session.client_reference_id !== user.id) {
    return NextResponse.json({ error: "Session mismatch" }, { status: 403 });
  }

  if (session.status === "complete" && session.subscription) {
    const subscription = await stripe.subscriptions.retrieve(session.subscription as string);
    const priceId = subscription.items.data[0]?.price.id;
    const tier = tierFromPriceId(priceId);

    const supabase = getServiceSupabase();
    await supabase
      .from("profiles")
      .update({
        tier,
        stripe_customer_id: session.customer as string,
        stripe_subscription_id: session.subscription as string,
        updated_at: new Date().toISOString(),
      })
      .eq("id", user.id);

    return NextResponse.json({ tier });
  }

  return NextResponse.json({ tier: 0 });
}
