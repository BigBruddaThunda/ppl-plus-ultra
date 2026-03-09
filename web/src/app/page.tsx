import Link from "next/link";

const ORDERS = [
  { emoji: "🐂", name: "Foundation", key: "1" },
  { emoji: "⛽", name: "Strength", key: "2" },
  { emoji: "🦋", name: "Hypertrophy", key: "3" },
  { emoji: "🏟", name: "Performance", key: "4" },
  { emoji: "🌾", name: "Full Body", key: "5" },
  { emoji: "⚖", name: "Balance", key: "6" },
  { emoji: "🖼", name: "Restoration", key: "7" },
];

const SAMPLE_ZIPS = [
  { code: "2123", label: "⛽🏛🪡🔵 — Strength Basics Pull Structured" },
  { code: "1115", label: "🐂🏛🛒🔴 — Foundation Basics Push Intense" },
  { code: "3341", label: "🦋🌹🍗⚫ — Hypertrophy Aesthetic Legs Teaching" },
  { code: "7258", label: "🖼🔨➖⚪ — Restoration Functional Ultra Mindful" },
];

export default function Home() {
  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-16">
        <header className="mb-12">
          <h1 className="text-3xl font-semibold tracking-tight">
            PPL±
          </h1>
          <p className="mt-2 text-lg opacity-70">
            1,680 rooms. 61 emojis. One system.
          </p>
        </header>

        <section className="mb-12">
          <h2 className="mb-4 text-sm font-medium uppercase tracking-widest opacity-50">
            7 Orders
          </h2>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {ORDERS.map((order) => (
              <div
                key={order.key}
                className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-4 text-center"
              >
                <span className="text-2xl">{order.emoji}</span>
                <p className="mt-1 text-xs font-medium opacity-70">{order.name}</p>
              </div>
            ))}
          </div>
        </section>

        <section>
          <h2 className="mb-4 text-sm font-medium uppercase tracking-widest opacity-50">
            Enter a Room
          </h2>
          <div className="space-y-2">
            {SAMPLE_ZIPS.map((zip) => (
              <Link
                key={zip.code}
                href={`/zip/${zip.code}`}
                className="block rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3 font-mono text-sm transition-default hover:border-[var(--ppl-accent)]"
              >
                <span className="opacity-40">/{zip.code}</span>
                <span className="ml-3">{zip.label}</span>
              </Link>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
