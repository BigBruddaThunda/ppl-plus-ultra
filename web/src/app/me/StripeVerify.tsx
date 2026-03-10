"use client";

import { useEffect } from "react";
import { useSearchParams, useRouter } from "next/navigation";

export function StripeVerify() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const sessionId = searchParams.get("session_id");

  useEffect(() => {
    if (!sessionId) return;

    fetch(`/api/stripe/verify?session_id=${sessionId}`)
      .then((res) => res.json())
      .then(() => {
        // Remove session_id from URL and refresh to show updated tier
        router.replace("/me");
        router.refresh();
      });
  }, [sessionId, router]);

  if (!sessionId) return null;

  return (
    <div className="mb-6 rounded-xl border border-green-500/30 bg-green-500/10 p-4 text-center text-sm">
      Verifying your subscription...
    </div>
  );
}
