"use client";

import { useState } from "react";
import { getSupabaseClient } from "@/lib/supabase/client";

interface LogOverlayProps {
  zipCode: string;
  blockName: string;
  exerciseName: string;
  onClose: () => void;
  onSaved: () => void;
}

export function LogOverlay({ zipCode, blockName, exerciseName, onClose, onSaved }: LogOverlayProps) {
  const [sets, setSets] = useState([{ reps: "", weight: "", rpe: "" }]);
  const [unit, setUnit] = useState<"lbs" | "kg">("lbs");
  const [notes, setNotes] = useState("");
  const [saving, setSaving] = useState(false);

  function addSet() {
    setSets((prev) => [...prev, { reps: "", weight: "", rpe: "" }]);
  }

  function updateSet(index: number, field: string, value: string) {
    setSets((prev) =>
      prev.map((s, i) => (i === index ? { ...s, [field]: value } : s))
    );
  }

  function removeSet(index: number) {
    if (sets.length <= 1) return;
    setSets((prev) => prev.filter((_, i) => i !== index));
  }

  async function handleSave() {
    setSaving(true);
    const supabase = getSupabaseClient();
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    // Find or create session for this zip today
    const todayStart = new Date();
    todayStart.setHours(0, 0, 0, 0);

    let { data: session } = await supabase
      .from("workout_sessions")
      .select("id")
      .eq("user_id", user.id)
      .eq("zip_code", zipCode)
      .gte("started_at", todayStart.toISOString())
      .maybeSingle();

    if (!session) {
      const { data: newSession } = await supabase
        .from("workout_sessions")
        .insert({ user_id: user.id, zip_code: zipCode })
        .select("id")
        .single();
      session = newSession;
    }

    if (!session) { setSaving(false); return; }

    // Insert set logs
    const logs = sets
      .filter((s) => s.reps || s.weight)
      .map((s, i) => ({
        session_id: session!.id,
        user_id: user.id,
        block_name: blockName,
        exercise_name: exerciseName,
        set_number: i + 1,
        reps: s.reps ? parseInt(s.reps) : null,
        weight: s.weight ? parseFloat(s.weight) : null,
        unit,
        rpe: s.rpe ? parseFloat(s.rpe) : null,
        notes: notes || null,
      }));

    if (logs.length > 0) {
      await supabase.from("set_logs").insert(logs);
    }

    setSaving(false);
    onSaved();
  }

  return (
    <div className="fixed inset-0 z-50 flex items-end justify-center bg-black/50" onClick={onClose}>
      <div
        className="w-full max-w-lg rounded-t-2xl border-t border-[var(--ppl-border)] bg-[var(--ppl-background)] p-6"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="mb-4 flex items-center justify-between">
          <div>
            <p className="text-xs font-medium uppercase tracking-widest opacity-50">
              Log Sets
            </p>
            <p className="mt-0.5 text-sm font-medium">{exerciseName}</p>
            <p className="text-xs opacity-40">{blockName}</p>
          </div>
          <button onClick={onClose} className="text-sm opacity-40 hover:opacity-70">
            Close
          </button>
        </div>

        {/* Unit toggle */}
        <div className="mb-4 flex gap-2">
          <button
            onClick={() => setUnit("lbs")}
            className={`rounded-md px-3 py-1 text-xs ${
              unit === "lbs"
                ? "bg-[var(--ppl-accent)] text-[var(--ppl-background)]"
                : "border border-[var(--ppl-border)] opacity-50"
            }`}
          >
            lbs
          </button>
          <button
            onClick={() => setUnit("kg")}
            className={`rounded-md px-3 py-1 text-xs ${
              unit === "kg"
                ? "bg-[var(--ppl-accent)] text-[var(--ppl-background)]"
                : "border border-[var(--ppl-border)] opacity-50"
            }`}
          >
            kg
          </button>
        </div>

        {/* Sets */}
        <div className="space-y-2">
          {sets.map((set, i) => (
            <div key={i} className="flex items-center gap-2">
              <span className="w-6 text-center text-xs opacity-40">{i + 1}</span>
              <input
                type="number"
                placeholder="Reps"
                value={set.reps}
                onChange={(e) => updateSet(i, "reps", e.target.value)}
                className="w-20 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-3 py-2 text-sm outline-none focus:border-[var(--ppl-accent)]"
              />
              <input
                type="number"
                placeholder="Weight"
                value={set.weight}
                onChange={(e) => updateSet(i, "weight", e.target.value)}
                className="w-24 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-3 py-2 text-sm outline-none focus:border-[var(--ppl-accent)]"
              />
              <input
                type="number"
                placeholder="RPE"
                value={set.rpe}
                onChange={(e) => updateSet(i, "rpe", e.target.value)}
                step="0.5"
                min="1"
                max="10"
                className="w-16 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-3 py-2 text-sm outline-none focus:border-[var(--ppl-accent)]"
              />
              {sets.length > 1 && (
                <button
                  onClick={() => removeSet(i)}
                  className="text-xs opacity-30 hover:opacity-70"
                >
                  x
                </button>
              )}
            </div>
          ))}
        </div>

        <button
          onClick={addSet}
          className="mt-2 text-xs opacity-40 hover:opacity-70"
        >
          + Add set
        </button>

        {/* Notes */}
        <input
          type="text"
          placeholder="Notes (optional)"
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
          className="mt-4 w-full rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-2 text-sm outline-none focus:border-[var(--ppl-accent)]"
        />

        {/* Save */}
        <button
          onClick={handleSave}
          disabled={saving}
          className="mt-4 w-full rounded-lg bg-[var(--ppl-accent)] px-5 py-2.5 text-sm font-medium text-[var(--ppl-background)] disabled:opacity-50"
        >
          {saving ? "Saving..." : "Log Sets"}
        </button>
      </div>
    </div>
  );
}
