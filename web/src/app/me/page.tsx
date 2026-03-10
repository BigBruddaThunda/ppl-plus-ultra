import { Suspense } from "react";
import Link from "next/link";
import { redirect } from "next/navigation";
import { getDailyZip, getOrderName, getTypeName } from "@/lib/rotation";
import { getAuthUser } from "@/lib/supabase/server";
import { LogoutButton } from "./LogoutButton";
import { StripeVerify } from "./StripeVerify";

export const dynamic = "force-dynamic";

const TIER_NAMES: Record<number, string> = {
  0: "Free",
  1: "Library Card",
  2: "Community Pass",
};

export default async function MePage() {
  const user = await getAuthUser();
  const today = new Date();
  const todayZip = getDailyZip(today);

  // Redirect new users to onboarding
  if (user && !user.onboarding_complete) {
    redirect("/onboarding");
  }

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        {/* ── Header ── */}
        <div className="mb-2">
          <Link href="/" className="text-xs opacity-40 hover:opacity-70">
            Home
          </Link>
        </div>

        <header className="mb-8">
          <h1 className="text-2xl font-semibold">Dashboard</h1>
          <p className="mt-1 text-sm opacity-50">
            Your training home.
          </p>
        </header>

        <Suspense>
          <StripeVerify />
        </Suspense>

        {/* ── Profile Section ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <div className="flex items-center gap-4">
            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[var(--ppl-border)] text-2xl">
              {user ? "🧮" : "👤"}
            </div>
            <div>
              <p className="font-medium">{user ? user.email : "Guest"}</p>
              <p className="text-xs opacity-40">{user ? TIER_NAMES[user.tier] ?? "Free" : "Not signed in"}</p>
            </div>
          </div>
          <div className="mt-4 flex gap-2">
            {user ? (
              <>
                <LogoutButton />
                <Link
                  href="/me/settings"
                  className="rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-xs font-medium opacity-70 hover:opacity-100"
                >
                  Settings
                </Link>
              </>
            ) : (
              <>
                <Link
                  href="/login"
                  className="rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-xs font-medium opacity-70 hover:opacity-100"
                >
                  Sign In
                </Link>
                <Link
                  href="/signup"
                  className="rounded-lg bg-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-background)]"
                >
                  Create Account
                </Link>
              </>
            )}
          </div>
        </section>

        {/* ── Today's Workout ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] p-5">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Today
          </p>
          <div className="mt-2 flex items-center justify-between">
            <div>
              <span className="text-2xl">
                {todayZip.orderEmoji}{todayZip.typeEmoji}
              </span>
              <span className="ml-2 text-sm opacity-70">
                {getOrderName(todayZip.order)} &middot; {getTypeName(todayZip.type)}
              </span>
            </div>
            <Link
              href={`/zip/${todayZip.numeric}`}
              className="rounded-lg bg-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-background)]"
            >
              Go
            </Link>
          </div>
        </section>

        {/* ── Subscription ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] p-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                Subscription
              </p>
              <p className="mt-1 text-sm">
                {user ? `${TIER_NAMES[user.tier] ?? "Free"} — ${user.tier === 0 ? "Lobby access only" : user.tier === 1 ? "Full room access" : "Full access + community"}` : "Free — Lobby access only"}
              </p>
            </div>
            <Link
              href="/subscribe"
              className="rounded-lg border border-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-accent)]"
            >
              {user && user.tier > 0 ? "Manage" : "Upgrade"}
            </Link>
          </div>
        </section>

        {/* ── Workout History ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] p-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                Workout History
              </p>
              <p className="mt-1 text-sm opacity-50">
                {user ? "Your logged sessions." : "Sign in to start logging."}
              </p>
            </div>
            {user && (
              <Link
                href="/me/history"
                className="rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-xs font-medium opacity-70 hover:opacity-100"
              >
                View
              </Link>
            )}
          </div>
        </section>

        {/* ── Saved Rooms ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] p-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                Saved Rooms
              </p>
              <p className="mt-1 text-sm opacity-50">
                {user ? "Your pinned rooms." : "Sign in to save rooms."}
              </p>
            </div>
            {user && (
              <Link
                href="/me/library"
                className="rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-xs font-medium opacity-70 hover:opacity-100"
              >
                View
              </Link>
            )}
          </div>
        </section>

        {/* ── Equipment Settings ── */}
        <section className="rounded-xl border border-[var(--ppl-border)] p-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest opacity-50">
                Equipment Profile
              </p>
              <p className="mt-1 text-sm opacity-50">
                {user ? "Your available equipment." : "Sign in to set equipment."}
              </p>
            </div>
            {user && (
              <Link
                href="/me/settings"
                className="rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-xs font-medium opacity-70 hover:opacity-100"
              >
                Edit
              </Link>
            )}
          </div>
        </section>
      </main>
    </div>
  );
}
