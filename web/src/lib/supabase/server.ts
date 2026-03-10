// Supabase Server Client — Stub for Session D
//
// TODO (Session D): Install @supabase/supabase-js and @supabase/ssr
// TODO (Session D): Read NEXT_PUBLIC_SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY from env
// TODO (Session D): Create actual server client using createServerClient()

export interface AuthUser {
  id: string;
  email: string;
  tier: number; // 0=Free, 1=Library Card, 2=Community Pass
}

/**
 * Get the authenticated user from the current request context.
 * Returns null when auth is not yet connected.
 */
export async function getAuthUser(): Promise<AuthUser | null> {
  // TODO (Session D): Wire to Supabase
  // 1. const supabase = createServerClient(...)
  // 2. const { data: { user } } = await supabase.auth.getUser()
  // 3. If user, query profiles table for tier
  // 4. Return { id, email, tier }
  return null;
}

/**
 * Check if user is authenticated. Redirects to /login if not.
 * Use in protected route Server Components.
 */
export async function requireAuth(): Promise<AuthUser> {
  const user = await getAuthUser();
  if (!user) {
    // TODO (Session D): Use redirect() from next/navigation
    throw new Error("Not authenticated");
  }
  return user;
}
