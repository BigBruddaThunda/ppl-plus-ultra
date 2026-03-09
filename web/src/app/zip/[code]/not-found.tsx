import Link from "next/link";

export default function ZipNotFound() {
  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <p className="text-6xl">🧮</p>
        <h1 className="mt-4 text-xl font-semibold">Room not found</h1>
        <p className="mt-2 text-sm opacity-60">
          Valid zip codes are 4-digit numbers: [1-7][1-6][1-5][1-8]
        </p>
        <Link
          href="/"
          className="mt-6 inline-block rounded-lg border border-[var(--ppl-border)] px-4 py-2 text-sm transition-default hover:border-[var(--ppl-accent)]"
        >
          Back to lobby
        </Link>
      </div>
    </div>
  );
}
