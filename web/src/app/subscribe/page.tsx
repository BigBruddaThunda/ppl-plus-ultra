"use client";

import Link from "next/link";
import { useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

const TIERS = [
  {
    name: "Free",
    price: "$0",
    period: "",
    description: "Lobby access. Browse the building.",
    features: [
      "View rotation schedule",
      "Browse exercise library",
      "Explore deck grids",
      "Read Operis editions",
    ],
    priceId: null,
    highlight: false,
  },
  {
    name: "Library Card",
    price: "$10",
    period: "/month",
    description: "Full room access. 1,680 workouts. Exercise library. Workout logging.",
    features: [
      "Enter all 1,680 rooms",
      "Full workout card content",
      "Personal workout logging",
      "Equipment profile",
      "Saved rooms",
      "Floor navigation (all 6 floors)",
    ],
    priceId: process.env.NEXT_PUBLIC_STRIPE_TIER1_PRICE_ID || null,
    highlight: true,
  },
  {
    name: "Community Pass",
    price: "$25",
    period: "/month",
    description: "Everything in Library Card + Operis editions, community floor, partner features.",
    features: [
      "Everything in Library Card",
      "Full Operis editorial access",
      "Community floor",
      "Partner workout features",
      "Priority cosmogram research",
      "Wilson voice navigation",
    ],
    priceId: process.env.NEXT_PUBLIC_STRIPE_TIER2_PRICE_ID || null,
    highlight: false,
  },
];

export default function SubscribePage() {
  const [loading, setLoading] = useState<string | null>(null);

  async function handleCheckout(priceId: string) {
    setLoading(priceId);

    // Check if user is logged in
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();

    if (!user) {
      window.location.href = "/login";
      return;
    }

    const res = await fetch("/api/stripe/checkout", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ priceId }),
    });

    const data = await res.json();

    if (data.url) {
      window.location.href = data.url;
    } else {
      setLoading(null);
    }
  }

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-3xl px-6 py-12">
        {/* ── Header ── */}
        <div className="mb-2">
          <Link href="/" className="text-xs opacity-40 hover:opacity-70">
            Home
          </Link>
        </div>

        <header className="mb-10 text-center">
          <h1 className="text-2xl font-semibold">Choose Your Access</h1>
          <p className="mt-2 text-sm opacity-50">
            1,680 rooms. Pick how deep you go.
          </p>
        </header>

        {/* ── Tier Cards ── */}
        <div className="grid gap-4 md:grid-cols-3">
          {TIERS.map((tier) => (
            <div
              key={tier.name}
              className={`rounded-xl border p-6 ${
                tier.highlight
                  ? "border-[var(--ppl-accent)] bg-[var(--ppl-surface)]"
                  : "border-[var(--ppl-border)]"
              }`}
            >
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                {tier.name}
              </p>
              <div className="mt-2">
                <span className="text-3xl font-semibold">{tier.price}</span>
                {tier.period && (
                  <span className="text-sm opacity-50">{tier.period}</span>
                )}
              </div>
              <p className="mt-2 text-sm opacity-60">
                {tier.description}
              </p>

              <ul className="mt-4 space-y-2">
                {tier.features.map((feature) => (
                  <li key={feature} className="flex items-start gap-2 text-sm">
                    <span className="mt-0.5 text-xs opacity-40">+</span>
                    <span className="opacity-70">{feature}</span>
                  </li>
                ))}
              </ul>

              {tier.priceId ? (
                <button
                  onClick={() => handleCheckout(tier.priceId!)}
                  disabled={loading === tier.priceId}
                  className={`mt-6 w-full rounded-lg px-4 py-2.5 text-sm font-medium ${
                    tier.highlight
                      ? "bg-[var(--ppl-accent)] text-[var(--ppl-background)] hover:opacity-90 disabled:opacity-50"
                      : "border border-[var(--ppl-accent)] text-[var(--ppl-accent)] hover:opacity-90 disabled:opacity-50"
                  }`}
                >
                  {loading === tier.priceId ? "Redirecting..." : "Subscribe"}
                </button>
              ) : (
                <button
                  disabled
                  className="mt-6 w-full rounded-lg border border-[var(--ppl-border)] px-4 py-2.5 text-sm font-medium opacity-40 cursor-not-allowed"
                >
                  Current Plan
                </button>
              )}
            </div>
          ))}
        </div>

        {/* ── FAQ ── */}
        <section className="mt-12">
          <h2 className="mb-4 text-xs font-medium uppercase tracking-widest opacity-50">
            Questions
          </h2>
          <div className="space-y-4">
            <div>
              <p className="text-sm font-medium">What do I get for free?</p>
              <p className="mt-1 text-sm opacity-60">
                Browse the building. See the rotation schedule, explore decks, search the exercise library. Room content requires a Library Card.
              </p>
            </div>
            <div>
              <p className="text-sm font-medium">Can I cancel anytime?</p>
              <p className="mt-1 text-sm opacity-60">
                Yes. Monthly billing. Cancel through your account dashboard. Your data exports on request.
              </p>
            </div>
            <div>
              <p className="text-sm font-medium">What about my data?</p>
              <p className="mt-1 text-sm opacity-60">
                No analytics fingerprinting. No third-party tracking. Full data export on request. Full deletion on command. You are the customer, not the product.
              </p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
