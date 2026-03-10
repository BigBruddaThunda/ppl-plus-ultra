import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export interface AuthUser {
  id: string;
  email: string;
  tier: number; // 0=Free, 1=Library Card, 2=Community Pass
  onboarding_complete: boolean;
  region: string | null;
}

export async function getSupabaseServer() {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            );
          } catch {
            // setAll is called from Server Components where cookies
            // can't be set — safe to ignore in that context.
          }
        },
      },
    }
  );
}

export async function getAuthUser(): Promise<AuthUser | null> {
  const supabase = await getSupabaseServer();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) return null;

  const { data: profile } = await supabase
    .from("profiles")
    .select("tier, onboarding_complete, region")
    .eq("id", user.id)
    .single();

  return {
    id: user.id,
    email: user.email ?? "",
    tier: profile?.tier ?? 0,
    onboarding_complete: profile?.onboarding_complete ?? false,
    region: profile?.region ?? null,
  };
}

export async function requireAuth(): Promise<AuthUser> {
  const user = await getAuthUser();
  if (!user) {
    redirect("/login");
  }
  return user;
}
