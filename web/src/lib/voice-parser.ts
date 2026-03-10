// Voice Parser — 3-layer keyword scoring for zip navigation
// No AI model. Pure keyword lookup + scoring. Client-side.

interface ParseResult {
  order: number | null;   // 1-7
  axis: number | null;    // 1-6
  type: number | null;    // 1-5
  color: number | null;   // 1-8
  floor: string | null;
  confidence: number;     // 0-1
  label: string;          // human-readable description
}

type KeywordMap = Record<string, { dial: string; position: number; weight: number }>;

// Layer 1: Zip keywords
const ZIP_KEYWORDS: KeywordMap = {
  // Orders (position 1-7)
  foundation: { dial: "order", position: 1, weight: 1 },
  learn: { dial: "order", position: 1, weight: 0.7 },
  beginner: { dial: "order", position: 1, weight: 0.7 },
  intro: { dial: "order", position: 1, weight: 0.6 },
  drill: { dial: "order", position: 1, weight: 0.6 },
  form: { dial: "order", position: 1, weight: 0.5 },
  technique: { dial: "order", position: 1, weight: 0.6 },
  "on-ramp": { dial: "order", position: 1, weight: 0.7 },

  strength: { dial: "order", position: 2, weight: 1 },
  heavy: { dial: "order", position: 2, weight: 0.8 },
  max: { dial: "order", position: 2, weight: 0.6 },
  loaded: { dial: "order", position: 2, weight: 0.6 },
  "low rep": { dial: "order", position: 2, weight: 0.7 },
  neural: { dial: "order", position: 2, weight: 0.5 },

  hypertrophy: { dial: "order", position: 3, weight: 1 },
  pump: { dial: "order", position: 3, weight: 0.8 },
  volume: { dial: "order", position: 3, weight: 0.7 },
  growth: { dial: "order", position: 3, weight: 0.7 },
  bodybuilding: { dial: "order", position: 3, weight: 0.8 },
  muscle: { dial: "order", position: 3, weight: 0.6 },
  "high rep": { dial: "order", position: 3, weight: 0.7 },

  performance: { dial: "order", position: 4, weight: 1 },
  test: { dial: "order", position: 4, weight: 0.7 },
  benchmark: { dial: "order", position: 4, weight: 0.8 },
  pr: { dial: "order", position: 4, weight: 0.8 },
  competition: { dial: "order", position: 4, weight: 0.7 },
  assessment: { dial: "order", position: 4, weight: 0.6 },

  "full body": { dial: "order", position: 5, weight: 1 },
  "total body": { dial: "order", position: 5, weight: 0.9 },
  integrated: { dial: "order", position: 5, weight: 0.6 },
  flow: { dial: "order", position: 5, weight: 0.5 },
  combo: { dial: "order", position: 5, weight: 0.6 },
  "whole body": { dial: "order", position: 5, weight: 0.9 },

  balance: { dial: "order", position: 6, weight: 1 },
  correction: { dial: "order", position: 6, weight: 0.7 },
  "weak point": { dial: "order", position: 6, weight: 0.7 },
  asymmetry: { dial: "order", position: 6, weight: 0.7 },
  imbalance: { dial: "order", position: 6, weight: 0.7 },
  accessory: { dial: "order", position: 6, weight: 0.6 },

  restoration: { dial: "order", position: 7, weight: 1 },
  recovery: { dial: "order", position: 7, weight: 0.8 },
  mobility: { dial: "order", position: 7, weight: 0.7 },
  stretch: { dial: "order", position: 7, weight: 0.7 },
  gentle: { dial: "order", position: 7, weight: 0.6 },
  somatic: { dial: "order", position: 7, weight: 0.7 },
  "rest day": { dial: "order", position: 7, weight: 0.6 },

  // Axes (position 1-6)
  classic: { dial: "axis", position: 1, weight: 0.8 },
  basics: { dial: "axis", position: 1, weight: 1 },
  fundamental: { dial: "axis", position: 1, weight: 0.8 },
  traditional: { dial: "axis", position: 1, weight: 0.7 },
  bilateral: { dial: "axis", position: 1, weight: 0.6 },

  functional: { dial: "axis", position: 2, weight: 1 },
  athletic: { dial: "axis", position: 2, weight: 0.8 },
  unilateral: { dial: "axis", position: 2, weight: 0.7 },
  sport: { dial: "axis", position: 2, weight: 0.6 },
  standing: { dial: "axis", position: 2, weight: 0.5 },

  aesthetic: { dial: "axis", position: 3, weight: 1 },
  isolation: { dial: "axis", position: 3, weight: 0.8 },
  definition: { dial: "axis", position: 3, weight: 0.7 },
  "mind muscle": { dial: "axis", position: 3, weight: 0.8 },
  cable: { dial: "axis", position: 3, weight: 0.5 },

  challenge: { dial: "axis", position: 4, weight: 1 },
  hard: { dial: "axis", position: 4, weight: 0.7 },
  advanced: { dial: "axis", position: 4, weight: 0.7 },
  difficult: { dial: "axis", position: 4, weight: 0.7 },
  deficit: { dial: "axis", position: 4, weight: 0.7 },
  pause: { dial: "axis", position: 4, weight: 0.5 },
  tempo: { dial: "axis", position: 4, weight: 0.5 },

  timed: { dial: "axis", position: 5, weight: 1 },
  emom: { dial: "axis", position: 5, weight: 0.9 },
  amrap: { dial: "axis", position: 5, weight: 0.9 },
  density: { dial: "axis", position: 5, weight: 0.7 },
  interval: { dial: "axis", position: 5, weight: 0.7 },
  "steady state": { dial: "axis", position: 5, weight: 0.7 },

  partner: { dial: "axis", position: 6, weight: 1 },
  social: { dial: "axis", position: 6, weight: 0.7 },
  spotter: { dial: "axis", position: 6, weight: 0.7 },
  paired: { dial: "axis", position: 6, weight: 0.7 },
  team: { dial: "axis", position: 6, weight: 0.7 },

  // Types (position 1-5)
  push: { dial: "type", position: 1, weight: 1 },
  chest: { dial: "type", position: 1, weight: 0.8 },
  press: { dial: "type", position: 1, weight: 0.7 },
  bench: { dial: "type", position: 1, weight: 0.8 },
  tricep: { dial: "type", position: 1, weight: 0.7 },
  shoulder: { dial: "type", position: 1, weight: 0.6 },
  overhead: { dial: "type", position: 1, weight: 0.6 },
  dips: { dial: "type", position: 1, weight: 0.7 },

  pull: { dial: "type", position: 2, weight: 1 },
  back: { dial: "type", position: 2, weight: 0.8 },
  row: { dial: "type", position: 2, weight: 0.7 },
  deadlift: { dial: "type", position: 2, weight: 0.8 },
  hinge: { dial: "type", position: 2, weight: 0.7 },
  bicep: { dial: "type", position: 2, weight: 0.7 },
  lat: { dial: "type", position: 2, weight: 0.7 },
  pulldown: { dial: "type", position: 2, weight: 0.7 },
  pullup: { dial: "type", position: 2, weight: 0.8 },

  legs: { dial: "type", position: 3, weight: 1 },
  squat: { dial: "type", position: 3, weight: 0.8 },
  quad: { dial: "type", position: 3, weight: 0.7 },
  hamstring: { dial: "type", position: 3, weight: 0.7 },
  glute: { dial: "type", position: 3, weight: 0.7 },
  lunge: { dial: "type", position: 3, weight: 0.7 },
  "leg day": { dial: "type", position: 3, weight: 0.9 },
  "lower body": { dial: "type", position: 3, weight: 0.8 },

  power: { dial: "type", position: 4, weight: 0.8 },
  olympic: { dial: "type", position: 4, weight: 0.9 },
  plyometric: { dial: "type", position: 4, weight: 0.8 },
  carry: { dial: "type", position: 4, weight: 0.7 },
  core: { dial: "type", position: 4, weight: 0.7 },
  explosive: { dial: "type", position: 4, weight: 0.7 },
  sprint: { dial: "type", position: 4, weight: 0.6 },

  cardio: { dial: "type", position: 5, weight: 1 },
  conditioning: { dial: "type", position: 5, weight: 0.8 },
  endurance: { dial: "type", position: 5, weight: 0.8 },
  aerobic: { dial: "type", position: 5, weight: 0.7 },
  run: { dial: "type", position: 5, weight: 0.7 },
  bike: { dial: "type", position: 5, weight: 0.7 },
  "zone 2": { dial: "type", position: 5, weight: 0.8 },
  ultra: { dial: "type", position: 5, weight: 0.9 },

  // Colors (position 1-8)
  teaching: { dial: "color", position: 1, weight: 1 },
  coached: { dial: "color", position: 1, weight: 0.7 },
  instruction: { dial: "color", position: 1, weight: 0.7 },

  bodyweight: { dial: "color", position: 2, weight: 1 },
  "no equipment": { dial: "color", position: 2, weight: 0.9 },
  home: { dial: "color", position: 2, weight: 0.6 },
  park: { dial: "color", position: 2, weight: 0.7 },
  hotel: { dial: "color", position: 2, weight: 0.7 },
  calisthenics: { dial: "color", position: 2, weight: 0.8 },
  "no gym": { dial: "color", position: 2, weight: 0.8 },

  structured: { dial: "color", position: 3, weight: 1 },
  programmed: { dial: "color", position: 3, weight: 0.8 },
  prescribed: { dial: "color", position: 3, weight: 0.7 },
  trackable: { dial: "color", position: 3, weight: 0.7 },
  repeatable: { dial: "color", position: 3, weight: 0.6 },

  technical: { dial: "color", position: 4, weight: 1 },
  precision: { dial: "color", position: 4, weight: 0.8 },
  quality: { dial: "color", position: 4, weight: 0.5 },
  "form focus": { dial: "color", position: 4, weight: 0.8 },
  skill: { dial: "color", position: 4, weight: 0.6 },
  perfect: { dial: "color", position: 4, weight: 0.5 },

  intense: { dial: "color", position: 5, weight: 1 },
  "max effort": { dial: "color", position: 5, weight: 0.8 },
  "high volume": { dial: "color", position: 5, weight: 0.7 },
  supersets: { dial: "color", position: 5, weight: 0.8 },
  "all out": { dial: "color", position: 5, weight: 0.7 },

  circuit: { dial: "color", position: 6, weight: 1 },
  stations: { dial: "color", position: 6, weight: 0.8 },
  loop: { dial: "color", position: 6, weight: 0.6 },
  rotation: { dial: "color", position: 6, weight: 0.6 },
  hiit: { dial: "color", position: 6, weight: 0.7 },

  fun: { dial: "color", position: 7, weight: 1 },
  play: { dial: "color", position: 7, weight: 0.8 },
  variety: { dial: "color", position: 7, weight: 0.6 },
  explore: { dial: "color", position: 7, weight: 0.6 },
  sandbox: { dial: "color", position: 7, weight: 0.7 },

  mindful: { dial: "color", position: 8, weight: 1 },
  slow: { dial: "color", position: 8, weight: 0.6 },
  breathe: { dial: "color", position: 8, weight: 0.7 },
  meditative: { dial: "color", position: 8, weight: 0.8 },
  parasympathetic: { dial: "color", position: 8, weight: 0.7 },
};

const ORDER_NAMES = ["", "Foundation", "Strength", "Hypertrophy", "Performance", "Full Body", "Balance", "Restoration"];
const AXIS_NAMES = ["", "Basics", "Functional", "Aesthetic", "Challenge", "Time", "Partner"];
const TYPE_NAMES = ["", "Push", "Pull", "Legs", "Plus", "Ultra"];
const COLOR_NAMES = ["", "Teaching", "Bodyweight", "Structured", "Technical", "Intense", "Circuit", "Fun", "Mindful"];

export function scoreInput(input: string): ParseResult {
  const normalized = input.toLowerCase().trim();
  const tokens = normalized.split(/\s+/);

  // Score each dial
  const scores: Record<string, { position: number; score: number }[]> = {
    order: [],
    axis: [],
    type: [],
    color: [],
  };

  // Check multi-word phrases first, then single words
  const phrases = [
    ...tokens.map((_, i) => tokens.slice(i, i + 3).join(" ")).filter((p) => p.includes(" ")),
    ...tokens.map((_, i) => tokens.slice(i, i + 2).join(" ")).filter((p) => p.includes(" ")),
    ...tokens,
  ];

  const matched = new Set<string>();

  for (const phrase of phrases) {
    if (matched.has(phrase)) continue;
    const entry = ZIP_KEYWORDS[phrase];
    if (entry) {
      scores[entry.dial].push({ position: entry.position, score: entry.weight });
      matched.add(phrase);
    }
  }

  // Pick best match per dial
  function bestMatch(hits: { position: number; score: number }[]): { position: number; score: number } | null {
    if (hits.length === 0) return null;
    return hits.reduce((best, h) => (h.score > best.score ? h : best));
  }

  const order = bestMatch(scores.order);
  const axis = bestMatch(scores.axis);
  const type = bestMatch(scores.type);
  const color = bestMatch(scores.color);

  const dialCount = [order, axis, type, color].filter(Boolean).length;
  const totalScore = [order, axis, type, color].reduce((s, d) => s + (d?.score ?? 0), 0);
  const confidence = dialCount === 0 ? 0 : Math.min(1, totalScore / 4 * (dialCount / 4 + 0.5));

  // Build label
  const parts: string[] = [];
  if (order) parts.push(ORDER_NAMES[order.position]);
  if (axis) parts.push(AXIS_NAMES[axis.position]);
  if (type) parts.push(TYPE_NAMES[type.position]);
  if (color) parts.push(COLOR_NAMES[color.position]);

  return {
    order: order?.position ?? null,
    axis: axis?.position ?? null,
    type: type?.position ?? null,
    color: color?.position ?? null,
    floor: null,
    confidence,
    label: parts.length > 0 ? parts.join(" + ") : "No match",
  };
}

export function routeFromParse(result: ParseResult): string | null {
  if (result.confidence === 0) return null;

  // Build numeric zip with defaults for missing dials
  const o = result.order ?? 2;  // default: Strength
  const a = result.axis ?? 1;   // default: Basics
  const t = result.type ?? 1;   // default: Push
  const c = result.color ?? 3;  // default: Structured

  return `/zip/${o}${a}${t}${c}`;
}
