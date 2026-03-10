import { NextResponse } from "next/server";
import { stripe } from "@/lib/stripe";
import { createClient } from "@supabase/supabase-js";

// Use service role key for webhook — no user context available
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

export async function POST(request: Request) {
  const body = await request.text();
  const signature = request.headers.get("stripe-signature");

  let event;

  // If webhook secret is configured, verify signature
  if (process.env.STRIPE_WEBHOOK_SECRET && signature) {
    try {
      event = stripe.webhooks.constructEvent(
        body,
        signature,
        process.env.STRIPE_WEBHOOK_SECRET
      );
    } catch {
      return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
    }
  } else {
    // In test mode without webhook secret, parse directly
    event = JSON.parse(body);
  }

  const supabase = getServiceSupabase();

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object;
      const userId = session.client_reference_id || session.metadata?.supabase_user_id;
      if (!userId) break;

      // Get the subscription to find the price
      const subscription = await stripe.subscriptions.retrieve(session.subscription as string);
      const priceId = subscription.items.data[0]?.price.id;
      const tier = tierFromPriceId(priceId);

      await supabase
        .from("profiles")
        .update({
          tier,
          stripe_customer_id: session.customer,
          stripe_subscription_id: session.subscription,
          updated_at: new Date().toISOString(),
        })
        .eq("id", userId);

      break;
    }

    case "customer.subscription.updated": {
      const subscription = event.data.object;
      const priceId = subscription.items.data[0]?.price.id;
      const tier = tierFromPriceId(priceId);

      // Find user by stripe_subscription_id
      const { data: profile } = await supabase
        .from("profiles")
        .select("id")
        .eq("stripe_subscription_id", subscription.id)
        .single();

      if (profile) {
        await supabase
          .from("profiles")
          .update({ tier, updated_at: new Date().toISOString() })
          .eq("id", profile.id);
      }
      break;
    }

    case "customer.subscription.deleted": {
      const subscription = event.data.object;

      await supabase
        .from("profiles")
        .update({ tier: 0, updated_at: new Date().toISOString() })
        .eq("stripe_subscription_id", subscription.id);

      break;
    }
  }

  return NextResponse.json({ received: true });
}
