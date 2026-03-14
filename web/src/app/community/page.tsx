import { Suspense } from "react";
import Link from "next/link";
import { getAuthUser } from "@/lib/supabase/server";
import { RecentActivity } from "./RecentActivity";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Community | Ppl±",
  description: "Recent activity across all 1,680 rooms.",
};

export const dynamic = "force-dynamic";

export default async function CommunityPage() {
  const user = await getAuthUser();

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        <div className="mb-2">
          <Link href="/" className="text-xs opacity-40 hover:opacity-70">
            Home
          </Link>
        </div>

        <header className="mb-8">
          <h1 className="text-2xl font-semibold">🐬 Community</h1>
          <p className="mt-1 text-sm opacity-50">
            Recent activity across all rooms.
          </p>
        </header>

        {!user ? (
          <section className="rounded-xl border border-[var(--ppl-border)] p-8 text-center">
            <p className="text-sm opacity-50 mb-3">
              Sign in to see community activity.
            </p>
            <Link
              href="/login"
              className="inline-block rounded-lg bg-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-background)]"
            >
              Sign In
            </Link>
          </section>
        ) : (
          <Suspense fallback={<div className="py-8 text-center text-sm opacity-40">Loading...</div>}>
            <RecentActivity userTier={user.tier} userId={user.id} />
          </Suspense>
        )}
      </main>
    </div>
  );
}
