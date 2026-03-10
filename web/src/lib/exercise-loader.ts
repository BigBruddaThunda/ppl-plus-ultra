// Exercise Library Loader — reads compiled exercise data from middle-math
// Used by both the /tools page and /zip/[code]/tools floor

import { readFileSync } from "fs";
import { join } from "path";

export interface Exercise {
  id: number;
  section: string;
  name: string;
  scl_types: string[];
  order_relevance: string[];
  axis_emphasis: string[];
  equipment_tier: [number, number];
  gold_gated: boolean;
  movement_pattern: string;
  muscle_groups: string;
  bilateral: boolean;
  compound: boolean;
}

// Type key → display name mapping for filtering
const TYPE_DISPLAY: Record<string, string> = {
  push: "Push",
  pull: "Pull",
  legs: "Legs",
  plus: "Plus",
  ultra: "Ultra",
};

let cachedExercises: Exercise[] | null = null;

export function loadExercises(): Exercise[] {
  if (cachedExercises) return cachedExercises;
  const filePath = join(process.cwd(), "..", "middle-math", "exercise-library.json");
  const raw = readFileSync(filePath, "utf-8");
  cachedExercises = JSON.parse(raw) as Exercise[];
  return cachedExercises;
}

export function filterByType(exercises: Exercise[], typeKey: string): Exercise[] {
  const displayName = TYPE_DISPLAY[typeKey];
  if (!displayName) return exercises;
  return exercises.filter((ex) => ex.scl_types.includes(displayName));
}
