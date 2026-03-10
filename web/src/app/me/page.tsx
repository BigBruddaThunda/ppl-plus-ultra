import Link from "next/link";
import { getDailyZip, getOrderName, getTypeName, formatDate } from "@/lib/rotation";

export default function MePage() {
  const today = new Date();
  const todayZip = getDailyZip(today);

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

        {/* ── Profile Section ── */}
        <section className="mb-6 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <div className="flex items-center gap-4">
            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[var(--ppl-border)] text-2xl">
              🧮
            </div>
            <div>
              <p className="font-medium">Guest</p>
              <p className="text-xs opacity-40">Free Tier</p>
            </div>
          </div>
          <div className="mt-4 flex gap-2">
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
              <p className="mt-1 text-sm">Free — Lobby access only</p>
            </div>
            <Link
              href="/subscribe"
              className="rounded-lg border border-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-accent)]"
            >
              Upgrade
            </Link>
          </div>
        </section>

        {/* ── Workout History ── */}
        <section className="mb-6 rounded-xl border border-dashed border-[var(--ppl-border)] p-5">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Workout History
          </p>
          <p className="mt-3 text-sm opacity-40">
            Your logged sessions will appear here.
          </p>
          <p className="mt-1 text-xs opacity-30">
            Requires account connection.
          </p>
        </section>

        {/* ── Saved Rooms ── */}
        <section className="mb-6 rounded-xl border border-dashed border-[var(--ppl-border)] p-5">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Saved Rooms
          </p>
          <p className="mt-3 text-sm opacity-40">
            Pin your favorite zip codes for quick access.
          </p>
          <p className="mt-1 text-xs opacity-30">
            Requires account connection.
          </p>
        </section>

        {/* ── Equipment Settings ── */}
        <section className="rounded-xl border border-dashed border-[var(--ppl-border)] p-5">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Equipment Profile
          </p>
          <p className="mt-3 text-sm opacity-40">
            Set your available equipment tiers to filter workouts.
          </p>
          <p className="mt-1 text-xs opacity-30">
            Requires account connection.
          </p>
        </section>
      </main>
    </div>
  );
}
