import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

export async function GET() {
  const checks: Record<string, boolean> = {
    supabase_url: !!process.env.NEXT_PUBLIC_SUPABASE_URL,
    supabase_key: !!process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    stripe_key: !!process.env.STRIPE_SECRET_KEY,
    stripe_webhook: !!process.env.STRIPE_WEBHOOK_SECRET,
  };

  const healthy = Object.values(checks).every(Boolean);

  return NextResponse.json(
    {
      status: healthy ? "ok" : "degraded",
      checks,
      timestamp: new Date().toISOString(),
    },
    { status: healthy ? 200 : 503 }
  );
}
