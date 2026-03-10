import { loadExercises } from "@/lib/exercise-loader";
import { ExerciseSearch } from "./ExerciseSearch";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Exercise Library | Ppl±",
  description: "2,085 exercises mapped to the SCL system.",
};

export default function ToolsPage() {
  const exercises = loadExercises();

  return (
    <div className="min-h-screen bg-neutral-950 text-white">
      <div className="mx-auto max-w-2xl px-6 py-12">
        <h1 className="text-2xl font-bold mb-1">Exercise Library</h1>
        <p className="text-sm font-mono opacity-40 mb-6">
          {exercises.length} exercises across 17 sections
        </p>
        <ExerciseSearch exercises={exercises} />
      </div>
    </div>
  );
}
