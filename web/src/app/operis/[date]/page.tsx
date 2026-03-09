// Operis daily edition — curated workout for a specific date
// Placeholder for Phase 2

export default async function OperisPage({
  params,
}: {
  params: Promise<{ date: string }>;
}) {
  const { date } = await params;

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <p className="text-4xl">📰</p>
        <h1 className="mt-4 text-xl font-semibold">
          Operis — {date}
        </h1>
        <p className="mt-2 text-sm opacity-60">
          Daily curated edition
        </p>
        <p className="mt-4 font-mono text-xs opacity-30">
          Operis editions coming in Phase 2
        </p>
      </div>
    </div>
  );
}
