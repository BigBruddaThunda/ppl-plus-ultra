import Link from "next/link";
import {
  getDailyZip,
  getWeekSchedule,
  getAxisForDate,
  getAxisName,
  getMonthName,
  getMonthlyOperator,
  getOrderName,
  getTypeName,
  formatDate,
} from "@/lib/rotation";
import { getFullZipStyle } from "@/lib/design-system";
import { parseNumericZip } from "@/lib/scl";
import { VoiceInput } from "@/components/ui/VoiceInput";

const ORDERS = [
  { emoji: "🐂", name: "Foundation", day: "Mon" },
  { emoji: "⛽", name: "Strength", day: "Tue" },
  { emoji: "🦋", name: "Hypertrophy", day: "Wed" },
  { emoji: "🏟", name: "Performance", day: "Thu" },
  { emoji: "🌾", name: "Full Body", day: "Fri" },
  { emoji: "⚖", name: "Balance", day: "Sat" },
  { emoji: "🖼", name: "Restoration", day: "Sun" },
];

export default function Home() {
  const today = new Date();
  const todayZip = getDailyZip(today);
  const week = getWeekSchedule(today);
  const monthAxis = getAxisForDate(today);
  const monthOp = getMonthlyOperator(today);

  // Theme the hero section with today's zip
  const zip = parseNumericZip(todayZip.numeric);
  const heroStyle = zip ? getFullZipStyle(zip) : {};

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        {/* ── Header ── */}
        <header className="mb-10">
          <h1 className="text-3xl font-semibold tracking-tight">PPL±</h1>
          <p className="mt-1 text-sm opacity-50">
            1,680 rooms. 61 emojis. One system.
          </p>
        </header>

        {/* ── Today's Workout Hero ── */}
        <section
          className="mb-10 rounded-xl border border-[var(--ppl-border)] p-6"
          style={heroStyle as React.CSSProperties}
        >
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Today's Room
          </p>
          <div className="mt-3 flex items-baseline gap-3">
            <span className="text-4xl">
              {todayZip.orderEmoji}{todayZip.axisEmoji}{todayZip.typeEmoji}{todayZip.colorEmoji}
            </span>
            <span className="font-mono text-sm opacity-40">/{todayZip.numeric}</span>
          </div>
          <p className="mt-2 text-sm opacity-70">
            {getOrderName(todayZip.order)} &middot; {getAxisName(todayZip.axis)} &middot; {getTypeName(todayZip.type)}
          </p>
          <Link
            href={`/zip/${todayZip.numeric}`}
            className="mt-4 inline-block rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] transition-opacity hover:opacity-90"
          >
            Enter Room
          </Link>
        </section>

        {/* ── Week Strip ── */}
        <section className="mb-10">
          <h2 className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            This Week
          </h2>
          <div className="grid grid-cols-7 gap-1.5">
            {week.map((day) => (
              <Link
                key={formatDate(day.date)}
                href={`/zip/${day.zip.numeric}`}
                className={`rounded-lg border p-2 text-center transition-default ${
                  day.isToday
                    ? "border-[var(--ppl-accent)] bg-[var(--ppl-surface)]"
                    : "border-[var(--ppl-border)] opacity-60 hover:opacity-100"
                }`}
              >
                <p className="text-[10px] font-medium uppercase tracking-wider opacity-50">
                  {day.dayName}
                </p>
                <p className="mt-1 text-lg">{day.zip.orderEmoji}</p>
                <p className="text-xs">{day.zip.typeEmoji}</p>
              </Link>
            ))}
          </div>
        </section>

        {/* ── Month Context ── */}
        <section className="mb-10 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3">
          <p className="text-xs opacity-50">
            {getMonthName(today)} — {monthOp.emoji} {monthOp.latin}
          </p>
          <p className="mt-1 text-sm">
            <span className="opacity-70">Axis emphasis:</span>{" "}
            <span className="font-medium">{getAxisName(monthAxis)}</span> month
          </p>
        </section>

        {/* ── 7 Orders ── */}
        <section className="mb-10">
          <h2 className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            7 Orders
          </h2>
          <div className="grid grid-cols-4 gap-2 sm:grid-cols-7">
            {ORDERS.map((order) => (
              <div
                key={order.name}
                className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-3 text-center"
              >
                <span className="text-xl">{order.emoji}</span>
                <p className="mt-0.5 text-[10px] font-medium opacity-50">{order.day}</p>
              </div>
            ))}
          </div>
        </section>

        {/* ── Voice Search ── */}
        <section className="mb-10">
          <h2 className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            Find a Room
          </h2>
          <VoiceInput />
        </section>

        {/* ── Quick Links ── */}
        <section>
          <h2 className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            Navigate
          </h2>
          <div className="grid grid-cols-2 gap-2">
            <Link
              href="/tools"
              className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3 text-sm transition-default hover:border-[var(--ppl-accent)]"
            >
              <span className="text-lg">🔨</span>
              <span className="ml-2 opacity-70">Exercise Library</span>
            </Link>
            <Link
              href={`/operis/${formatDate(today)}`}
              className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3 text-sm transition-default hover:border-[var(--ppl-accent)]"
            >
              <span className="text-lg">📰</span>
              <span className="ml-2 opacity-70">Today's Operis</span>
            </Link>
            <Link
              href={`/deck/${todayZip.deck}`}
              className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3 text-sm transition-default hover:border-[var(--ppl-accent)]"
            >
              <span className="text-lg">🗂</span>
              <span className="ml-2 opacity-70">Deck {String(todayZip.deck).padStart(2, "0")}</span>
            </Link>
            <Link
              href="/subscribe"
              className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-3 text-sm transition-default hover:border-[var(--ppl-accent)]"
            >
              <span className="text-lg">🔑</span>
              <span className="ml-2 opacity-70">Subscribe</span>
            </Link>
          </div>
        </section>
      </main>
    </div>
  );
}
