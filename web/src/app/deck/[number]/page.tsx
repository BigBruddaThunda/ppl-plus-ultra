// Deck view — shows all 40 cards in a deck (5 types × 8 colors)
// Placeholder for Phase 2

export default async function DeckPage({
  params,
}: {
  params: Promise<{ number: string }>;
}) {
  const { number } = await params;

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="text-center">
        <p className="text-4xl">📦</p>
        <h1 className="mt-4 text-xl font-semibold">
          Deck {String(number).padStart(2, "0")}
        </h1>
        <p className="mt-2 text-sm opacity-60">
          40 rooms · 5 types × 8 colors
        </p>
        <p className="mt-4 font-mono text-xs opacity-30">
          Deck browser coming in Phase 2
        </p>
      </div>
    </div>
  );
}
