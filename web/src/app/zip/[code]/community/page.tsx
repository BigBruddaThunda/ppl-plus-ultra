import { Suspense } from "react";
import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { getAuthUser } from "@/lib/supabase/server";
import { CommunityFloorClient } from "./CommunityFloorClient";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Community | Ppl±" };
  return { title: `Community — ${zip.raw} | Ppl±` };
}

export default async function CommunityFloor({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  const user = await getAuthUser();

  return (
    <section
      className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)]"
      style={{
        marginTop: "var(--ppl-space-lg)",
        padding: "var(--ppl-space-lg)",
        borderRadius: "var(--ppl-radius-md)",
      }}
    >
      <h2 className="text-lg font-semibold mb-1">
        🐬 Sociatas
      </h2>
      <p className="text-xs font-mono opacity-40 mb-4">
        Room {code} community
      </p>

      {!user ? (
        <div className="py-6 text-center">
          <p className="text-sm opacity-50 mb-3">
            Sign in to see what others are saying about this room.
          </p>
          <a
            href="/login"
            className="inline-block rounded-lg bg-[var(--ppl-accent)] px-4 py-2 text-xs font-medium text-[var(--ppl-background)]"
          >
            Sign In
          </a>
        </div>
      ) : (
        <Suspense fallback={<div className="py-8 text-center text-sm opacity-40">Loading...</div>}>
          <CommunityFloorClient
            zipCode={code}
            userTier={user.tier}
            userId={user.id}
          />
        </Suspense>
      )}
    </section>
  );
}
