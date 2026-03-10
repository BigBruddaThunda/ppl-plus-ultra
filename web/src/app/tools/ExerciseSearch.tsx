"use client";

import { useState, useMemo } from "react";
import type { Exercise } from "@/lib/exercise-loader";

const TYPE_FILTERS = [
  { key: "all", emoji: "All", label: "All" },
  { key: "Push", emoji: "🛒", label: "Push" },
  { key: "Pull", emoji: "🪡", label: "Pull" },
  { key: "Legs", emoji: "🍗", label: "Legs" },
  { key: "Plus", emoji: "➕", label: "Plus" },
  { key: "Ultra", emoji: "➖", label: "Ultra" },
];

const TYPE_EMOJI: Record<string, string> = {
  Push: "🛒", Pull: "🪡", Legs: "🍗", Plus: "➕", Ultra: "➖",
};

interface Props {
  exercises: Exercise[];
}

export function ExerciseSearch({ exercises }: Props) {
  const [query, setQuery] = useState("");
  const [typeFilter, setTypeFilter] = useState("all");
  const [goldOnly, setGoldOnly] = useState(false);

  const filtered = useMemo(() => {
    let result = exercises;

    if (typeFilter !== "all") {
      result = result.filter((ex) => ex.scl_types.includes(typeFilter));
    }

    if (goldOnly) {
      result = result.filter((ex) => ex.gold_gated);
    }

    if (query.trim()) {
      const q = query.toLowerCase();
      result = result.filter(
        (ex) =>
          ex.name.toLowerCase().includes(q) ||
          ex.muscle_groups.toLowerCase().includes(q) ||
          ex.movement_pattern.toLowerCase().includes(q)
      );
    }

    return result;
  }, [exercises, query, typeFilter, goldOnly]);

  return (
    <div>
      {/* Search input */}
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search exercises..."
        className="w-full px-4 py-3 rounded-lg bg-white/5 border border-white/10 text-sm font-mono text-white placeholder:text-white/30 focus:outline-none focus:border-white/30"
      />

      {/* Type filter chips */}
      <div className="flex gap-2 mt-3 flex-wrap">
        {TYPE_FILTERS.map((f) => (
          <button
            key={f.key}
            onClick={() => setTypeFilter(f.key)}
            className="px-3 py-1.5 rounded-md text-xs font-mono transition-colors"
            style={{
              background: typeFilter === f.key ? "rgba(255,255,255,0.15)" : "rgba(255,255,255,0.05)",
              border: typeFilter === f.key ? "1px solid rgba(255,255,255,0.3)" : "1px solid transparent",
            }}
          >
            {f.emoji} {f.label}
          </button>
        ))}
        <button
          onClick={() => setGoldOnly(!goldOnly)}
          className="px-3 py-1.5 rounded-md text-xs font-mono transition-colors"
          style={{
            background: goldOnly ? "rgba(255,215,0,0.15)" : "rgba(255,255,255,0.05)",
            border: goldOnly ? "1px solid rgba(255,215,0,0.4)" : "1px solid transparent",
            color: goldOnly ? "rgb(255,215,0)" : "inherit",
          }}
        >
          GOLD
        </button>
      </div>

      {/* Count */}
      <p className="text-xs font-mono opacity-30 mt-3 mb-4">
        {filtered.length} result{filtered.length !== 1 ? "s" : ""}
      </p>

      {/* Results */}
      <div className="space-y-1">
        {filtered.slice(0, 100).map((ex) => (
          <div
            key={ex.id}
            className="flex items-start gap-3 py-2 border-b border-white/5 last:border-0"
          >
            <span className="text-sm shrink-0 w-8 text-center">
              {ex.scl_types.map((t) => TYPE_EMOJI[t] || "").join("")}
            </span>
            <div className="min-w-0 flex-1">
              <p className="text-sm truncate">{ex.name}</p>
              <p className="text-xs opacity-40">
                {ex.muscle_groups} · {ex.movement_pattern} · Tier {ex.equipment_tier[0]}–{ex.equipment_tier[1]}
                {ex.gold_gated && " · GOLD"}
                {ex.compound && " · Compound"}
                {!ex.bilateral && " · Unilateral"}
              </p>
            </div>
            <span className="text-[10px] font-mono opacity-20 shrink-0">
              #{ex.id}
            </span>
          </div>
        ))}
        {filtered.length > 100 && (
          <p className="text-xs font-mono opacity-30 py-2 text-center">
            Showing first 100 of {filtered.length}. Refine your search.
          </p>
        )}
      </div>
    </div>
  );
}
