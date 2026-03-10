// Supabase Auth Middleware — Stub for Session D
//
// TODO (Session D): Install @supabase/supabase-js and @supabase/ssr
// TODO (Session D): Wire real auth token refresh logic

import { NextResponse, type NextRequest } from "next/server";

/**
 * Refresh the auth session on each request.
 * Currently a passthrough — no auth connected yet.
 */
export async function updateSession(request: NextRequest) {
  // TODO (Session D): Wire to Supabase middleware
  // 1. const supabase = createServerClient(url, anonKey, { cookies })
  // 2. await supabase.auth.getUser() — this refreshes the token
  // 3. Return the response with updated cookies
  return NextResponse.next({
    request: { headers: request.headers },
  });
}
