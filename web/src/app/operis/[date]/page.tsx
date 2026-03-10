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

interface Props {
  params: Promise<{ date: string }>;
}

function parseDate(dateStr: string): Date | null {
  const match = dateStr.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (!match) return null;
  const d = new Date(parseInt(match[1]), parseInt(match[2]) - 1, parseInt(match[3]));
  if (isNaN(d.getTime())) return null;
  return d;
}

const WEEKDAY_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

export default async function OperisPage({ params }: Props) {
  const { date: dateStr } = await params;
  const date = parseDate(dateStr);

  if (!date) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[var(--ppl-background)]">
        <div className="text-center">
          <p className="text-4xl">📰</p>
          <h1 className="mt-4 text-xl font-semibold">Invalid Date</h1>
          <p className="mt-2 text-sm opacity-60">
            Use format: /operis/YYYY-MM-DD
          </p>
          <Link href="/" className="mt-4 inline-block text-sm opacity-50 hover:opacity-100">
            Back to Home
          </Link>
        </div>
      </div>
    );
  }

  const zip = getDailyZip(date);
  const week = getWeekSchedule(date);
  const axis = getAxisForDate(date);
  const monthOp = getMonthlyOperator(date);
  const weekday = WEEKDAY_NAMES[date.getDay()];
  const isToday = formatDate(date) === formatDate(new Date());

  return (
    <div className="min-h-screen bg-[var(--ppl-background)]">
      <main className="mx-auto max-w-2xl px-6 py-12">
        {/* ── Header ── */}
        <div className="mb-2">
          <Link href="/" className="text-xs opacity-40 hover:opacity-70">
            Home
          </Link>
        </div>

        <header className="mb-8">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Operis Edition
          </p>
          <h1 className="mt-2 text-2xl font-semibold">
            {zip.orderEmoji} {weekday}, {getMonthName(date)} {date.getDate()}, {date.getFullYear()}
          </h1>
          {isToday && (
            <span className="mt-1 inline-block rounded-full bg-[var(--ppl-accent)] px-2 py-0.5 text-[10px] font-medium text-[var(--ppl-background)]">
              Today
            </span>
          )}
        </header>

        {/* ── Featured Room ── */}
        <section className="mb-8 rounded-xl border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <p className="text-xs font-medium uppercase tracking-widest opacity-50">
            Featured Room
          </p>
          <div className="mt-3 flex items-baseline gap-3">
            <span className="text-3xl">
              {zip.orderEmoji}{zip.axisEmoji}{zip.typeEmoji}{zip.colorEmoji}
            </span>
            <span className="font-mono text-sm opacity-40">/{zip.numeric}</span>
          </div>
          <p className="mt-2 text-sm opacity-70">
            {getOrderName(zip.order)} &middot; {getAxisName(zip.axis)} &middot; {getTypeName(zip.type)}
          </p>
          <p className="mt-1 text-xs opacity-40">
            Deck {String(zip.deck).padStart(2, "0")}
          </p>
          <Link
            href={`/zip/${zip.numeric}`}
            className="mt-4 inline-block rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] transition-opacity hover:opacity-90"
          >
            Enter Room
          </Link>
        </section>

        {/* ── Month Context ── */}
        <section className="mb-8 rounded-lg border border-[var(--ppl-border)] px-4 py-3">
          <p className="text-xs opacity-50">
            {getMonthName(date)} — {monthOp.emoji} {monthOp.latin}
          </p>
          <p className="mt-1 text-sm">
            <span className="opacity-70">Axis emphasis:</span>{" "}
            <span className="font-medium">{getAxisName(axis)}</span> month
          </p>
        </section>

        {/* ── Week Context ── */}
        <section className="mb-8">
          <h2 className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            This Week
          </h2>
          <div className="grid grid-cols-7 gap-1.5">
            {week.map((day) => {
              const dayDate = formatDate(day.date);
              const isCurrent = dayDate === dateStr;
              return (
                <Link
                  key={dayDate}
                  href={`/operis/${dayDate}`}
                  className={`rounded-lg border p-2 text-center transition-default ${
                    isCurrent
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
              );
            })}
          </div>
        </section>

        {/* ── Editorial Content Placeholder ── */}
        <section className="rounded-lg border border-dashed border-[var(--ppl-border)] px-4 py-6 text-center">
          <p className="text-sm opacity-40">
            Full editorial content will appear here once the Operis pipeline is connected.
          </p>
          <p className="mt-2 text-xs opacity-30">
            13-room Sandbox &middot; Historical events &middot; Featured exercises
          </p>
        </section>

        {/* ── Navigation ── */}
        <div className="mt-8 flex justify-between text-xs">
          <Link
            href={`/operis/${formatDate(new Date(date.getFullYear(), date.getMonth(), date.getDate() - 1))}`}
            className="opacity-40 hover:opacity-70"
          >
            &larr; Previous day
          </Link>
          <Link
            href={`/operis/${formatDate(new Date(date.getFullYear(), date.getMonth(), date.getDate() + 1))}`}
            className="opacity-40 hover:opacity-70"
          >
            Next day &rarr;
          </Link>
        </div>
      </main>
    </div>
  );
}
