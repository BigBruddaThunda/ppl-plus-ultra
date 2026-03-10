import Link from "next/link";

export default function LoginPage() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-[var(--ppl-background)]">
      <div className="w-full max-w-sm px-6">
        <header className="mb-8 text-center">
          <h1 className="text-2xl font-semibold">Sign In</h1>
          <p className="mt-1 text-sm opacity-50">
            Enter your room.
          </p>
        </header>

        <form className="space-y-4">
          <div>
            <label htmlFor="email" className="block text-xs font-medium uppercase tracking-widest opacity-50">
              Email
            </label>
            <input
              id="email"
              type="email"
              autoComplete="email"
              required
              className="mt-1 block w-full rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-2.5 text-sm outline-none focus:border-[var(--ppl-accent)]"
              placeholder="you@example.com"
            />
          </div>

          <div>
            <label htmlFor="password" className="block text-xs font-medium uppercase tracking-widest opacity-50">
              Password
            </label>
            <input
              id="password"
              type="password"
              autoComplete="current-password"
              required
              className="mt-1 block w-full rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-2.5 text-sm outline-none focus:border-[var(--ppl-accent)]"
              placeholder="••••••••"
            />
          </div>

          <button
            type="button"
            disabled
            className="w-full rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] opacity-50 cursor-not-allowed"
            title="Authentication coming soon"
          >
            Sign In
          </button>

          <p className="text-center text-xs opacity-40">
            Authentication will be connected in a future session.
          </p>
        </form>

        <div className="mt-6 text-center text-sm">
          <span className="opacity-50">No account? </span>
          <Link href="/signup" className="font-medium opacity-70 hover:opacity-100">
            Sign Up
          </Link>
        </div>

        <div className="mt-4 text-center">
          <Link href="/" className="text-xs opacity-40 hover:opacity-70">
            Back to Home
          </Link>
        </div>
      </div>
    </div>
  );
}
