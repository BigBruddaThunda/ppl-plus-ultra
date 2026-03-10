import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { loadExercises, filterByType } from "@/lib/exercise-loader";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Tools | Ppl±" };
  return { title: `Tools — ${zip.raw} | Ppl±` };
}

const TYPE_EMOJI: Record<string, string> = {
  Push: "🛒", Pull: "🪡", Legs: "🍗", Plus: "➕", Ultra: "➖",
};

export default async function ToolsFloor({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  const allExercises = loadExercises();
  const exercises = filterByType(allExercises, zip.type);

  return (
    <section
      className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)]"
      style={{
        marginTop: "var(--ppl-space-lg)",
        padding: "var(--ppl-space-lg)",
        borderRadius: "var(--ppl-radius-md)",
      }}
    >
      <h2 className="text-lg font-semibold mb-1">
        🔨 Exercise Library
      </h2>
      <p className="text-xs font-mono opacity-40 mb-4">
        {exercises.length} exercises for {zip.typeEmoji} {zip.type}
      </p>

      <div className="space-y-2">
        {exercises.map((ex) => (
          <div
            key={ex.id}
            className="flex items-start gap-3 py-2 border-b border-[var(--ppl-border)] last:border-0"
          >
            <span className="text-sm shrink-0">
              {ex.scl_types.map((t) => TYPE_EMOJI[t] || "").join("")}
            </span>
            <div className="min-w-0">
              <p className="text-sm font-medium truncate">{ex.name}</p>
              <p className="text-xs opacity-50">
                {ex.muscle_groups} · Tier {ex.equipment_tier[0]}–{ex.equipment_tier[1]}
                {ex.gold_gated && " · GOLD"}
                {ex.compound && " · Compound"}
              </p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
