# Phase 2: Core Data - Research

**Researched:** 2026-03-14
**Domain:** TypeScript weight tables, exercise dictionary, keyword dictionary, computeRawVector()
**Confidence:** HIGH (all findings derived from first-party sources in repo)

---

## Summary

Phase 2 has unusually strong first-party sources. Every weight rule is derivable from CLAUDE.md and the existing DRAFT weight declaration files in `middle-math/weights/`. The DRAFT files are not being ported — they are being used as a cross-reference for citation logic while re-authoring fresh TypeScript modules. The exercise library already exists as a parsed JSON file with 2,085 entries. The keyword seed material exists in `seeds/voice-parser-architecture.md`.

The TypeScript shape question is the only design choice the researcher must prescribe. The W enum from Phase 1 (`canvas/src/types/scl.ts`) is the authoritative index. Weight table modules must key to the same positions (ORDERS[1–7], AXES[1–6], TYPES[1–5], COLORS[1–8], BLOCKS[1–22], OPERATORS[1–12]). The phonebook pattern is established and should be extended — const objects keyed by numeric position, same as every other SCL table in scl.ts.

computeRawVector(zip) is a straightforward summation function. It takes the four dial positions from a zip code, looks up each dial's weight declaration object, and sums all affinities and suppressions into a 61-element Float32Array indexed by W enum values. No resolver logic. No hierarchy enforcement. Steps 1–3 only.

**Primary recommendation:** Author six TypeScript weight declaration modules (one per category), port the exercise library to a typed interface with a manual alias layer, mine first-party sources for the keyword dictionary, and wire computeRawVector() as a pure summation. Four separable deliverables, two of them are data authoring.

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Weight Table Authoring:**
- Re-derive all weights from scratch using CLAUDE.md and scl-directory.md as canonical sources. Do NOT port existing DRAFT markdown tables from middle-math/weights/. Fresh derivation ensures no drift from stale drafts.
- All 6 categories: Order (7), Axis (6), Type (5), Color (8), Block (22), Operator (12). The weight vector is 61-dimensional across ALL emojis — all categories must be populated.
- Cross-talk scope: let the researcher decide. Analyze scl-directory.md rules to determine which intra-category relationships actually exist vs. cross-category only.
- Coarse scale: use even values + key thresholds (0, ±2, ±4, ±6, ±8). Mid-range distinctions are noise.
- Citation: Hard suppressions (-6 to -8) and strong affinities (+6 to +8) MUST cite a specific rule from CLAUDE.md or scl-directory.md. Mid-range values can be estimated from character descriptions.
- Phase 2 includes basic summation: computeRawVector(zip) = steps 1–3 (Primary, Affinity Cascade, Suppression Cascade). Step 4 (Interaction Resolution) is Phase 3.
- Ignore existing weight-vectors.json. Stale. Do not anchor to it.

**Exercise Dictionary:**
- Port existing exercise-library.json shape into TypeScript.
- Auto-derive search tokens from exercise names PLUS a manual alias layer (~100–200 high-value entries).
- Drop order_relevance and axis_emphasis fields (they list ALL values and carry no signal).

**Keyword Dictionary:**
- Hybrid source: mine CLAUDE.md + scl-directory.md + exercise-library.md first, then supplement with voice-parser-architecture seed.
- Compound forms preferred over ambiguous singles.
- JSON file + TypeScript types pattern.

### Claude's Discretion
- TypeScript module shape for weight tables (const objects vs. JSON + types)
- Exact number of alias entries (target ~100–200)
- How to structure the keyword mining pipeline
- Test strategy for weight tables and keyword dictionary

### Deferred Ideas (OUT OF SCOPE)
- Per-exercise affinity scoring
- Full 13K keyword dictionary from voice-parser-architecture (v2 scope, XPRS-01)
- Context-aware keyword scoring using user history
- Intra-category cross-talk beyond what scl-directory.md rules actually support
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| WGHT-01 | 61-dimensional weight vector computation for any zip code (-8 to +8 scale) | computeRawVector() derivation section; W enum in scl.ts is the index |
| WGHT-02 | Dial weight tables for all 4 categories (Order: 7, Axis: 6, Type: 5, Color: 8) | All four DRAFT weight files analyzed; hard rules catalogued below |
| PARS-02 | Keyword dictionary (~2,500 fitness terms) with dimension_affinity_score per entry | voice-parser-architecture.md Layer 1 vocabulary is the seed; first-party spec mining adds 1,500–2,000 terms |
| PARS-03 | Exercise name detection using exercise-library.md as authoritative source | exercise-library.json confirmed at 2,085 entries; TypeScript interface defined below |
| PARS-04 | Equipment mention detection mapping to Color tier ranges | Color tier rules in CLAUDE.md fully catalogued; keyword layer maps equipment terms to Color positions |
| PARS-05 | Body part / muscle group detection mapping to Type | Type routing rules in CLAUDE.md fully catalogued; muscle group field in exercise-library.json covers 58 categories |
</phase_requirements>

---

## Research Question 1: Weight Table TypeScript Shape

### Finding

The Phase 1 `scl.ts` establishes the definitive pattern: const objects keyed by numeric position (1-based), typed with `as const satisfies Record<number, SclEntry>`. The W enum provides the 61-position semantic index. Weight tables must follow this same phonebook pattern.

**Recommended TypeScript interface for weight table entries:**

```typescript
// canvas/src/weights/types.ts

export type WeightScale = -8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8;
// Coarse scale per CONTEXT.md locked decision.
// Note: computeRawVector sums float arithmetic, so the type is informational.
// Use number at runtime; WeightScale is the authoring constraint.

export interface WeightEntry {
  /** +8 when this emoji is the active dial. Always self-declares +8. */
  self: 8;
  /**
   * Affinities: W enum position → weight.
   * Only non-zero affinities are listed. Unlisted positions = 0.
   */
  affinities: Partial<Record<number, number>>;
  /**
   * Suppressions: W enum position → weight (negative values).
   * Only non-zero suppressions are listed. Unlisted positions = 0.
   */
  suppressions: Partial<Record<number, number>>;
}

export interface DialWeightTable {
  [position: number]: WeightEntry;
}
```

**Why sparse (Partial) rather than full 61-slot objects:**
- Most dials only touch ~10–20 of the 61 positions. Full 61-slot objects would be 80% zeros.
- computeRawVector() iterates sparse entries and writes to a dense Float32Array. This is faster and easier to author.
- The DRAFT files use the same pattern (listing only non-zero rows).

**Module layout (one file per category):**

```
canvas/src/weights/
  types.ts          — WeightEntry, DialWeightTable, WeightScale interfaces
  orders.ts         — ORDERS_WEIGHTS: DialWeightTable (7 entries)
  axes.ts           — AXES_WEIGHTS: DialWeightTable (6 entries)
  types-weights.ts  — TYPES_WEIGHTS: DialWeightTable (5 entries)  [avoid name clash with types.ts]
  colors.ts         — COLORS_WEIGHTS: DialWeightTable (8 entries)
  blocks.ts         — BLOCKS_WEIGHTS: DialWeightTable (22 entries)
  operators.ts      — OPERATORS_WEIGHTS: DialWeightTable (12 entries)
  index.ts          — re-exports all tables + computeRawVector()
```

**Keying to W enum:** Every weight entry key is a W enum value from scl.ts. Example from DRAFT order-weights.md, translated to TypeScript:

```typescript
// orders.ts (excerpt — ⛽ Strength at position 2)
import { W } from '../types/scl.js';

export const ORDERS_WEIGHTS: DialWeightTable = {
  2: {  // W.STRENGTH = 2
    self: 8,
    affinities: {
      [W.PRIMER]:       6,  // "CNS activation. Bridges warm-up." cited: ⛽ block sequence
      [W.BREAD_BUTTER]: 8,  // "Always present. Most volume." cited: universal block rule
      [W.SUPPLEMENTAL]: 4,
      [W.RELEASE]:      4,  // ⛽ block sequence includes 🪫
      [W.WARM_UP]:      6,  // "Always present." cited: universal block rule
      [W.JUNCTION]:     6,  // always present, cited: all Order sequences
      [W.BASICS]:       2,
      [W.CHALLENGE]:    4,  // "Hardest variation aligns with force production"
      [W.MITTO]:        4,  // "Explosive intent. Max attempt." cited: ⛽ affinities
      [W.FACIO]:        4,  // default expressive operator for 🏛 × expressive colors
      [W.STRUCTURED]:   2,
      [W.TECHNICAL]:    4,
    },
    suppressions: {
      [W.VANITY]:      -4,  // "Pump is irrelevant in ⛽" cited: order-weights.md
      [W.ARAM]:        -4,  // "Station loops reduce rest below ⛽ minimum"
      [W.RESTORATION]: -4,  // "Recovery mode contradicts heavy loading"
      [W.IMPRINT]:     -2,
      [W.CIRCUIT]:     -2,
      [W.FOUNDATION]:  -2,
      [W.GUTTER]:      -2,  // "Only in 🔴 and 🪐."
      [W.MINDFUL]:     -4,  // "Slow tempo contradicts neural CNS demand"
      [W.FULL_BODY]:   -2,
    },
  },
  // ... entries 1, 3-7
};
```

**Confidence:** HIGH — pattern is a direct extension of established Phase 1 conventions.

---

## Research Question 2: Cross-Talk Analysis (Intra-Category Relationships)

### Finding: Which intra-category cross-talk exists in the spec?

The CLAUDE.md and DRAFT weight files reveal the following intra-category cross-talk patterns:

**Order↔Order cross-talk (CONFIRMED in spec):**
- ⛽ Strength suppresses 🐂 Foundation (-2): "⛽ has moved past Foundation-level loading" — cited in order-weights.md
- ⛽ Strength suppresses 🖼 Restoration (-4): contradictory intents
- 🦋 Hypertrophy suppresses ⛽ Strength (-2): "Neural-adaptation heavy loading is not hypertrophy"
- 🦋 Hypertrophy suppresses 🏟 Performance (-4): accumulation vs. test-and-leave
- 🏟 Performance suppresses 🦋 Hypertrophy (-4): same conflict from other direction
- 🖼 Restoration suppresses ⛽ Strength (-6): "Heavy loading contradicts ≤55% ceiling" — HARD SUPPRESSION cited in order-weights.md

**The key question:** Should Order declare suppressions of other Order emojis at all? Analysis says YES, but with important constraint: **Order self-suppression represents "this session has a character that makes the OTHER order less relevant."** It is NOT about priority hierarchy (that's the resolver's job in Phase 3). It reflects semantic tension:
- A Restoration session explicitly suppresses the Strength character — not as a priority rule, but as a content signal (the workout will feel nothing like Strength).
- This is low-signal intra-category cross-talk that still carries content-relevance meaning.

**Axis↔Axis cross-talk (CONFIRMED in spec):**
- 🏛 Basics suppresses 🌹 Aesthetic (-4): "Aesthetic priority stack inverses Basics"
- 🌹 Aesthetic suppresses 🏛 Basics (-4): inverse confirmed
- 🔨 Functional suppresses 🌹 Aesthetic (-4): "internal MMC + machine/isolative bias conflicts with transfer-first standing"
- 🌹 Aesthetic suppresses ⛽ Strength (-4): "neural force-production focus deprioritizes feel-first"

**Type↔Type cross-talk (CONFIRMED, STRONG):**
- 🛒 Push suppresses 🪡 Pull (-6): direct antagonists — HARD SUPPRESSION
- 🪡 Pull suppresses 🛒 Push (-6): same
- 🍗 Legs suppresses 🛒 Push (-4) and 🪡 Pull (-4): lower body vs. upper body
- ➖ Ultra suppresses ⛽ Strength (-4): cardiovascular system vs. neural force production
- 🛒 Push suppresses 🍗 Legs (-4) and ➖ Ultra (-4)

**Color↔Color cross-talk (CONFIRMED, STRONG):**
- 🔴 Intense suppresses ⚪ Mindful (-6): "opposite character" — HARD SUPPRESSION
- ⚪ Mindful suppresses 🔴 Intense (-6): same — HARD SUPPRESSION
- GOLD Colors (🔴, 🟣) have implicit affinity with each other through GOLD gate
- 🟠 Circuit suppresses ⚫ Teaching (moderate): circuit pace is not teaching pace

**Operator↔Operator cross-talk (CONFIRMED, STRUCTURAL):**
- Each Axis pair's opposite-polarity operators suppress each other at -5:
  - 📍 pono ↔ 🤌 facio: "setup suppresses execution, execution suppresses setup"
  - 🧸 fero ↔ 🥨 tendo
  - 👀 specio ↔ 🦢 plico
  - 🪵 teneo ↔ 🚀 mitto
  - 🐋 duco ↔ ✒️ grapho
  - 🧲 capio ↔ 🦉 logos

**Block↔Block cross-talk (MINIMAL — blocks mostly declare Order/Color affinities, not block-to-block):**
- 🌋 Gutter has hard suppressions declared from Orders (🖼, 🐂) and Color (⚪) — these are cross-category
- 🧩 Supplemental has a hard rule: suppresses its own block when it duplicates 🧈's movement pattern
- 🎱 ARAM is defined as replacing 🧈/🧩/🪞 in circuit context — block substitution, not cross-talk

**Summary for planner:** Cross-talk is real and citable for Orders (moderate), Types (strong), Axes (moderate), Colors (strong), and Operators (polarity pairs). Block cross-talk is minimal. The weight tables should include intra-category suppressions where the DRAFT files explicitly cite them. Do not invent intra-category relationships not cited in the spec.

**Confidence:** HIGH — all cross-talk derived from explicit DRAFT citations.

---

## Research Question 3: Cited Hard Rules per Category

### Orders — Hard Rules

| Emoji | Target | Weight | Citation |
|-------|--------|--------|---------|
| 🐂 Foundation | 🌋 Gutter | -8 | CLAUDE.md: "Never in 🖼, 🐂, or ⚪." |
| ⛽ Strength | (none ≤ -6) | — | Strongest suppressions are -4 (soft) |
| 🦋 Hypertrophy | (none ≤ -6) | — | — |
| 🏟 Performance | 🪞 Vanity | -8 | CLAUDE.md: "🏟 blocks hypertrophy-style accumulation by default." |
| 🏟 Performance | 🗿 Sculpt | -8 | Same rule |
| 🏟 Performance | 🎱 ARAM | -7 | "Station loops are junk volume in 🏟 context." |
| 🏟 Performance | 🧩 Supplemental | -7 | "No junk volume after the test." |
| 🖼 Restoration | 🌋 Gutter | -8 | CLAUDE.md: "Never in 🖼, 🐂, or ⚪." |
| 🖼 Restoration | 🏟 Performance | -8 | "Testing contradicts recovery-without-debt" |
| 🖼 Restoration | ⛽ Strength | -6 | "Heavy loading contradicts ≤55% ceiling" — HARD |
| 🖼 Restoration | 🔴 Intense | -6 | "Maximum effort contradicts restoration intent" — HARD |
| 🖼 Restoration | 🚀 mitto | -6 | "Explosive intent contradicts CNS:Low" — HARD |

### Colors — Hard Rules

| Emoji | Target | Weight | Citation |
|-------|--------|--------|---------|
| ⚫ Teaching | 🌋 Gutter | -8 | "All-out effort contradicts comprehension-over-exertion" |
| ⚫ Teaching | GOLD exercises | -8 | CLAUDE.md: "Only 🔴 Intense and 🟣 Technical unlock GOLD exercises." |
| 🟢 Bodyweight | Barbell exercises | -8 | CLAUDE.md: "No barbells in 🟢 Bodyweight." |
| 🟢 Bodyweight | Tier 3+ equipment | -8 | Tier cap = 0–2 |
| 🟢 Bodyweight | GOLD exercises | -8 | CLAUDE.md GOLD rule |
| 🔵 Structured | GOLD exercises | -8 | CLAUDE.md GOLD rule |
| 🔴 Intense | ⚪ Mindful | -6 | "Opposite character. Hard suppression." |
| 🟠 Circuit | Barbell exercises | -8 | CLAUDE.md: "No barbells in 🟠 Circuit." |
| 🟠 Circuit | GOLD exercises | -8 | CLAUDE.md GOLD rule |
| 🟠 Circuit | Same-tissue adjacent stations | -8 | CLAUDE.md loop logic rule |
| 🟠 Circuit | 🌋 Gutter | -8 | "Only in 🔴 and 🪐." |
| 🟡 Fun | GOLD exercises | -8 | CLAUDE.md GOLD rule |
| ⚪ Mindful | 🌋 Gutter | -8 | CLAUDE.md: "Never in 🖼, 🐂, or ⚪." |
| ⚪ Mindful | 🔴 Intense | -6 | "Opposite character. Hard suppression." |
| ⚪ Mindful | High velocity movements | -6 | "Ballistic, explosive, fast-tempo contradict 4s eccentric." |
| ⚪ Mindful | GOLD exercises | -8 | CLAUDE.md GOLD rule |

### Types — Hard Rules

| Emoji | Target | Weight | Citation |
|-------|--------|--------|---------|
| 🛒 Push | 🪡 Pull | -6 | "Direct antagonists: pressing vs. pulling, anterior vs. posterior chain." |
| 🪡 Pull | 🛒 Push | -6 | Same |
| 🍗 Legs | 🛒 Push | -5 | "Pressing patterns are not lower-body tissue." |
| 🍗 Legs | 🪡 Pull | -5 | "Pulling patterns are not lower-body tissue." |

**Confidence:** HIGH — all hard rules (≤ -6) cite explicit CLAUDE.md text.

---

## Research Question 4: Exercise Library Shape

### Current exercise-library.json fields

```
id, section, name, scl_types, order_relevance, axis_emphasis,
equipment_tier, gold_gated, movement_pattern, muscle_groups,
bilateral, compound
```

**Total entries:** 2,085 exercises across 17 sections (A–Q)

**Critical finding on order_relevance and axis_emphasis:**
- 1,715 of 2,085 entries list ALL 7 orders in order_relevance (82% carry no signal)
- 1,670 of 2,085 entries list ALL 6 axes in axis_emphasis (80% carry no signal)
- These fields are noise, not signal. CONTEXT.md decision to drop them is confirmed correct.
- The 370 entries with partial order_relevance are the GOLD-gated exercises (Olympic lifts, plyometrics, strongman) that are restricted to ⛽/🏟/🌾 Orders — this signal is already captured by gold_gated=true + equipment_tier.

**Recommended TypeScript interface:**

```typescript
// canvas/src/parser/types.ts

export interface ExerciseEntry {
  id: number;
  section: string;                    // "A"–"Q"
  name: string;                       // canonical: "Romanian Deadlift (RDL)"
  scl_types: string[];               // ["Pull", "Plus"] — 1-based later via lookup
  equipment_tier: [number, number];   // [min, max] e.g. [0, 5]
  gold_gated: boolean;
  movement_pattern: string;
  muscle_groups: string;
  bilateral: boolean;
  compound: boolean;
  aliases: string[];                  // ADDED: manual + auto-derived alias layer
}
```

**Dropped fields:** order_relevance, axis_emphasis (confirmed no-signal).

**equipment_tier representation:** The JSON stores [min, max] as a 2-element array. This is clean and should be preserved. Equipment tier filtering in the parser: `entry.equipment_tier[0] <= colorTier && colorTier <= entry.equipment_tier[1]`.

**Confidence:** HIGH — field analysis is direct from JSON inspection.

---

## Research Question 5: Alias Candidates

### Auto-derivable aliases

Many canonical names include parenthetical clarifiers that become natural alias forms:

```
"Romanian Deadlift (RDL)"         → aliases: ["RDL", "Romanian deadlift", "stiff-leg DL"]
"Barbell Overhead Press (Standing)" → aliases: ["OHP", "overhead press", "press overhead", "barbell press"]
"Barbell Bench Press"              → aliases: ["bench", "bench press", "flat bench", "BP"]
"Hip Thrust (Barbell)"             → aliases: ["hip thrust", "barbell hip thrust", "glute bridge loaded"]
```

**Auto-derive rule:** Strip parenthetical content → add as alias. Strip equipment prefix → add as alias. The canonical name itself minus the parenthetical is an alias candidate.

### High-value manual aliases (seed list ~100-200 entries)

**Abbreviations (highest recall value):**

| Alias | Canonical Name | Type |
|-------|---------------|------|
| RDL | Romanian Deadlift (RDL) | abbreviation |
| OHP | Barbell Overhead Press (Standing) | abbreviation |
| SLDL | Stiff-Leg Deadlift | abbreviation |
| DB | prefix tag for dumbbell variants | prefix |
| KB | prefix tag for kettlebell variants | prefix |
| BB | prefix tag for barbell variants | prefix |
| SB | prefix tag for Swiss ball variants | prefix |
| BW | prefix tag for bodyweight variants | prefix |
| GHR | Glute Ham Raise | abbreviation |
| GHD | GHD Sit-Up | abbreviation |
| RFE | Rear Foot Elevated (split squat) | abbreviation |
| BSS | Bulgarian Split Squat | abbreviation |
| CGP | Close-Grip Press | abbreviation |
| CGB | Close-Grip Bench | abbreviation |

**Gym slang / tribal names:**

| Alias | Canonical Name |
|-------|---------------|
| skullcrusher | Lying Triceps Extension (EZ Bar) |
| skull crusher | Lying Triceps Extension (EZ Bar) |
| french press | Overhead Triceps Extension |
| JM press | JM Press |
| pullover | Dumbbell Pullover / Barbell Pullover |
| flies / flyes | Dumbbell Chest Fly |
| cable cross | Cable Crossover |
| press-down | Triceps Pushdown |
| pushdown | Triceps Pushdown |
| face pull | Face Pull (Cable) |
| lat pulldown | Lat Pulldown (Cable) |
| seated cable row | Seated Cable Row |
| incline curl | Incline Dumbbell Curl |
| hammer curl | Hammer Curl |
| zottman curl | Zottman Curl |
| preacher curl | Preacher Curl |
| spider curl | Spider Curl |
| Bulgarian | Bulgarian Split Squat |
| pistol | Pistol Squat |
| pistol squat | Pistol Squat |
| box squat | Box Squat (Barbell) |
| pause squat | Paused Back Squat |
| front squat | Front Squat |
| zercher | Zercher Squat |
| good morning | Good Morning (Barbell) |
| hip hinge | Romanian Deadlift (RDL) |
| sumo | Deadlift (Sumo) |
| trap bar DL | Hex Bar Deadlift |
| hex bar deadlift | Hex Bar Deadlift |
| farmer carry | Farmer's Carry |
| farmers walk | Farmer's Carry |
| suitcase carry | Suitcase Carry |
| overhead carry | Overhead Carry |
| KB swing | Kettlebell Swing |
| kettle swing | Kettlebell Swing |
| goblet squat | Goblet Squat (Kettlebell) |
| turkish getup | Turkish Get-Up |
| TGU | Turkish Get-Up |
| clean | Power Clean (as common shorthand) |
| power clean | Power Clean |
| hang clean | Hang Clean (Above Knee) |
| snatch | Power Snatch (common shorthand) |
| push press | Push Press (Barbell) |
| push jerk | Push Jerk (Barbell) |

**Auto-generation strategy for remaining ~100 entries:**
1. Strip parenthetical suffix from any name containing `(...)` — creates a shorter alias
2. Strip equipment prefix ("Barbell", "Dumbbell", "Cable", "Machine", "Kettlebell") — creates equipment-agnostic alias
3. Common plural/singular variants: "press" ↔ "presses", "row" ↔ "rows"

**Total estimated aliases with auto-generation:** ~180–220 manually seeded + ~400–600 auto-derived = ~600–800 total aliases across 2,085 exercises. The Phase 2 requirement is ~100–200 seeded entries for the manual layer.

**Confidence:** MEDIUM — alias candidates derived from inspection of exercise names and gym vernacular knowledge. The auto-derivation rule is HIGH confidence.

---

## Research Question 6: Keyword Dictionary Sources

### Source 1: voice-parser-architecture.md Layer 1 (seed material confirmed)

The file at `seeds/voice-parser-architecture.md` contains Layer 1 vocabulary tables for all 26 SCL dial positions (the 4-emoji zip positions). This is usable directly as a seed:

- Order keywords: ~7 per emoji × 7 = ~50 terms
- Axis keywords: ~7 per emoji × 6 = ~42 terms
- Type keywords: ~7 per emoji × 5 = ~35 terms
- Color keywords: ~7 per emoji × 8 = ~56 terms

Total from Layer 1: ~183 terms already mapped to dimension positions.

### Source 2: CLAUDE.md and scl-directory.md vocabulary mining

The canonical spec files contain hundreds of descriptive terms that can be extracted as keywords:

**Order-mapped terms in CLAUDE.md:**
- Foundation: "sub-maximal", "pattern learning", "on-ramp", "CNS: Low", "difficulty 2/5"
- Strength: "neural adaptation", "force production", "low reps", "full recovery", "CNS: High"
- Hypertrophy: "metabolic stress", "pump", "volume", "time under tension", "muscle growth"
- Performance: "testing", "benchmark", "1RM", "max attempt", "competition"
- Full Body: "integration", "flow", "unified pattern", "complex", "thruster"
- Balance: "correction", "asymmetry", "weak links", "prehab", "targeted accessory"
- Restoration: "recovery", "somatic", "parasympathetic", "deload", "mobility", "TRE"

**Equipment-mapped terms (→ Color tier ranges):**
- Tier 0: "bodyweight only", "no equipment", "calisthenics", "park", "hotel"
- Tier 1: "bands", "resistance band", "sliders", "foam roller"
- Tier 2: "dumbbells", "kettlebells", "plates"
- Tier 3: "barbell", "rack", "bench" → 🔵/🟣/🔴 territory
- Tier 4: "machines", "cables", "cable machine"
- Tier 5: "stones", "sleds", "GHD", "competition" → GOLD territory

**Muscle group terms (→ Type mapping):**
- Push (🛒): "chest", "pec", "pectorals", "front delt", "anterior deltoid", "triceps", "overhead"
- Pull (🪡): "lats", "latissimus", "rear delt", "posterior deltoid", "biceps", "traps", "trapezius", "erectors", "rhomboids", "back", "row"
- Legs (🍗): "quads", "quadriceps", "hamstrings", "glutes", "gluteus", "calves", "lower body", "hip flexors", "tibialis"
- Plus (➕): "core", "olympic lifting", "plyometrics", "loaded carry", "rotational", "anti-rotation", "power"
- Ultra (➖): "cardio", "conditioning", "aerobic", "zone 2", "HIIT", "intervals", "endurance", "rowing machine", "assault bike"

### Compound vs. single-word collision analysis

The "collision-prone keywords" requirement (PARS-02) refers to single words that score multiple dimensions:

| Collision Word | Collision Dimensions | Resolution |
|---------------|---------------------|-----------|
| "heavy" | Order: ⛽ (weight) OR just equipment/load feel | Use "heavy barbell" or "heavy lifting" instead |
| "hard" | Order: 🏟 OR Axis: 🪐 | Use "hard variation" (🪐) vs "max effort" (🏟) |
| "easy" | Order: 🐂 OR Order: 🖼 | Use "light technique" (🐂) vs "recovery" (🖼) |
| "power" | Type: ➕ OR Order: ⛽ | Use "explosive power" (➕) vs "power lift" (⛽) |
| "light" | Load descriptor: matches 🐂, 🖼, 🟢 | Flag as ambiguous; prefer "bodyweight" or "restoration" |
| "pump" | Axis: 🌹 OR Order: 🦋 | Use "hypertrophy pump" vs "aesthetic pump" — both valid |
| "press" | Type: 🛒 (push) OR exercise name | Always compound: "bench press", "overhead press" |
| "row" | Type: 🪡 (pull) OR exercise name | Compound preferred: "barbell row", "cable row" |
| "strength" | Order: ⛽ OR generic goal | Context resolves; "strength training" → ⛽ primary |

**Strategy:** Single collision-prone words are flagged in the keyword dict with `collision_prone: true`. The parser (Phase 3) handles disambiguation. The Phase 2 keyword dict just identifies them.

### Estimated term counts by source

| Source | Estimated Terms | Confidence |
|--------|----------------|-----------|
| voice-parser-architecture.md Layer 1 | 183 | HIGH (direct count) |
| CLAUDE.md order/axis/type/color descriptors | ~400–600 | MEDIUM (needs mining) |
| exercise-library.md muscle group terms | ~200–300 | MEDIUM |
| equipment tier vocabulary | ~100–150 | HIGH (derivable from CLAUDE.md tier table) |
| Compound keyword expansion from above | ~500–800 | MEDIUM |
| **Total Phase 2 target** | **~2,000–2,500** | Meets PARS-02 requirement |

### Recommended keyword dictionary TypeScript interface

```typescript
// canvas/src/parser/keywords.ts

export type DimensionId =
  // Orders 1-7
  | 1 | 2 | 3 | 4 | 5 | 6 | 7
  // Axes 8-13
  | 8 | 9 | 10 | 11 | 12 | 13
  // Types 14-18
  | 14 | 15 | 16 | 17 | 18
  // Colors 19-26
  | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26;
  // Note: Blocks and Operators are NOT keyword dimensions for the parser.
  // Keywords map to the 4-dial zip positions only (Phase 2 scope).

export interface KeywordEntry {
  term: string;                              // the keyword or phrase
  dimension: DimensionId;                    // which W position it maps to
  affinity_score: number;                    // 1–8 (positive only; keyword dict has no suppressions)
  collision_prone: boolean;                  // true if ambiguous single word
  source: 'first-party' | 'voice-seed';    // traceability
}

// dial-keywords.json structure:
// Array of KeywordEntry — imported and validated at build time.
```

**Why blocks/operators are excluded from keyword dict:** Keywords describe what a user WANTS (exercise character, equipment, body part, training style). They map to zip code dimensions (the 4 dials). Blocks and operators are structural/grammatical elements of a workout, not things users ask for by name. The keyword dict is a natural language → zip code bridge.

**Confidence:** HIGH for structure; MEDIUM for exact term count.

---

## Research Question 7: computeRawVector() Design

### Algorithm (Steps 1–3, Phase 2 scope)

```typescript
// canvas/src/weights/index.ts

import { W, WEIGHT_VECTOR_LENGTH } from '../types/scl.js';
import { ORDERS_WEIGHTS } from './orders.js';
import { AXES_WEIGHTS } from './axes.js';
import { TYPES_WEIGHTS } from './types-weights.js';
import { COLORS_WEIGHTS } from './colors.js';
import { BLOCKS_WEIGHTS } from './blocks.js';
import { OPERATORS_WEIGHTS } from './operators.js';

/**
 * Compute the raw 61-dimensional weight vector for a zip code.
 * Steps 1-3 only (Primary weights, Affinity Cascade, Suppression Cascade).
 * Step 4 (Interaction Resolution with constraint hierarchy) is Phase 3.
 *
 * @param orderPos  1–7
 * @param axisPos   1–6
 * @param typePos   1–5
 * @param colorPos  1–8
 * @returns Float32Array of length 61, indexed by W enum values (1-based, slot 0 unused)
 */
export function computeRawVector(
  orderPos: number,
  axisPos: number,
  typePos: number,
  colorPos: number
): Float32Array {
  const vec = new Float32Array(WEIGHT_VECTOR_LENGTH + 1); // +1 for 1-based indexing

  // Step 1: Primary weights — each active dial gets +8 at its own W position
  vec[orderPos]      += 8;  // e.g. orderPos=2 → vec[W.STRENGTH] += 8
  vec[axisPos + 7]   += 8;  // Axes start at W.BASICS=8
  vec[typePos + 13]  += 8;  // Types start at W.PUSH=14
  vec[colorPos + 18] += 8;  // Colors start at W.TEACHING=19

  // Step 2–3: Affinity and Suppression Cascade for each active dial
  const activeDials = [
    ORDERS_WEIGHTS[orderPos],
    AXES_WEIGHTS[axisPos],
    TYPES_WEIGHTS[typePos],
    COLORS_WEIGHTS[colorPos],
  ];

  for (const dial of activeDials) {
    if (!dial) continue;
    for (const [pos, weight] of Object.entries(dial.affinities)) {
      vec[Number(pos)] += weight;
    }
    for (const [pos, weight] of Object.entries(dial.suppressions)) {
      vec[Number(pos)] += weight; // weights are already negative
    }
  }

  // Clamp to [-8, +8]
  for (let i = 1; i <= WEIGHT_VECTOR_LENGTH; i++) {
    vec[i] = Math.max(-8, Math.min(8, vec[i]));
  }

  return vec;
}
```

**Design notes:**
- Returns unclamped partial result before Step 4 (the resolver in Phase 3 will clamp + apply hierarchy). Wait — per the spec, clamping to [-8, +8] IS part of Steps 1–3 (soft weight summation rule). Include clamp in computeRawVector.
- Blocks and Operators weight tables are NOT applied in computeRawVector. Their weights are dial-context-driven (a block's weight depends on the active Order/Color), not zip-input-driven. They are used by the visual renderer (Phase 5) to derive block container styles, not by the basic summation.
- Float32Array: appropriate for numeric weight calculations. Avoids object allocation overhead per vector.

**Primary weights indexing note:** The W enum uses 1-based positions. The four dial categories map to W enum slots:
- Orders: W.FOUNDATION=1 through W.RESTORATION=7 → match orderPos directly
- Axes: W.BASICS=8 through W.PARTNER=13 → axisPos + 7
- Types: W.PUSH=14 through W.ULTRA=18 → typePos + 13
- Colors: W.TEACHING=19 through W.MINDFUL=26 → colorPos + 18

**Confidence:** HIGH — the formula and the W enum positions are verified from scl.ts inspection.

---

## Architecture Patterns

### Recommended project structure for Phase 2

```
canvas/src/
├── types/
│   └── scl.ts              — EXISTS (Phase 1)
├── parser/
│   ├── zip-converter.ts    — EXISTS (Phase 1)
│   ├── types.ts            — NEW: ExerciseEntry, KeywordEntry interfaces
│   └── keywords.ts         — NEW: keyword dict loader + validation
├── weights/
│   ├── types.ts            — NEW: WeightEntry, DialWeightTable interfaces
│   ├── orders.ts           — NEW: ORDERS_WEIGHTS (7 entries)
│   ├── axes.ts             — NEW: AXES_WEIGHTS (6 entries)
│   ├── type-weights.ts     — NEW: TYPES_WEIGHTS (5 entries)
│   ├── colors.ts           — COLORS_WEIGHTS (8 entries)
│   ├── blocks.ts           — BLOCKS_WEIGHTS (22 entries)
│   ├── operators.ts        — OPERATORS_WEIGHTS (12 entries)
│   └── index.ts            — NEW: computeRawVector() + re-exports
└── index.ts                — re-exports (update after Phase 2)

canvas/data/                — NEW directory for JSON data assets
├── exercises.json          — NEW: ported exercise library with aliases
└── dial-keywords.json      — NEW: keyword dictionary

canvas/tests/
├── zip-converter.test.ts   — EXISTS (Phase 1)
├── weight-tables.test.ts   — NEW: spot-check weight values, computeRawVector
└── keyword-dict.test.ts    — NEW: keyword scoring tests
```

### Pattern: const objects for weight tables (NOT JSON)

The weight tables are code, not data. They contain W enum references. They benefit from TypeScript compile-time checking. JSON would lose the W enum semantics. Use TypeScript const objects, same as scl.ts.

### Pattern: JSON for exercise and keyword dicts

The exercise dictionary and keyword dictionary are pure data without code semantics. JSON files imported via `resolveJsonModule: true` (already in tsconfig). TypeScript interfaces validate their shape at build time.

### Anti-pattern: Don't re-export weight tables as flat arrays

The tables should remain structured objects keyed by position. The computeRawVector() function is the single consumer that knows how to iterate them. Do not flatten them.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Fuzzy matching (Phase 3) | Custom edit-distance impl | fastest-levenshtein | Battle-tested; Phase 3 scope |
| Multi-word search (Phase 3) | Custom tokenizer | fuse.js | Already planned in requirements |
| Schema validation of JSON | Custom checker | TypeScript `satisfies` + `as const` | Zero deps, compile-time only |
| Float arithmetic clamping | Custom clamp utility | Inline `Math.max(-8, Math.min(8, v))` | Simple enough to inline |

**Key insight:** Phase 2 is a data authoring phase. The main work is writing correct weight values, not building infrastructure. The infrastructure (TypeScript modules, JSON files, a summation function) is simple. The judgment work is in the weight declarations themselves.

---

## Common Pitfalls

### Pitfall 1: Authoring Block weights without a clear consumer

**What goes wrong:** Block weight tables in Phase 2 seem complete but there is no Phase 2 consumer for them. computeRawVector() only uses Order/Axis/Type/Color weights.

**Why it happens:** The weight vector is 61-dimensional and includes Block slots (W.WARM_UP through W.CHOICE). It's tempting to apply Block weights in computeRawVector().

**How to avoid:** Block and Operator weights ARE required by WGHT-02 (all 6 categories). Author them to spec. But computeRawVector() does NOT apply them — it only applies the four dial weights. The Block/Operator slots in the vector will have non-zero values only after Phase 3's resolver applies them contextually.

**Warning sign:** If computeRawVector() is importing BLOCKS_WEIGHTS or OPERATORS_WEIGHTS, something is wrong.

### Pitfall 2: Porting the stale order_relevance / axis_emphasis fields

**What goes wrong:** exercise-library.json has order_relevance and axis_emphasis fields. The ported exercises.json TypeScript interface inadvertently includes them.

**How to avoid:** Drop these fields at the porting step. The CONTEXT.md decision is locked: these fields carry no signal (82%+ list all values). Confirmed by inspection: 1,715 of 2,085 entries list all 7 orders.

### Pitfall 3: Weight collision between same-position emojis

**What goes wrong:** An Order affinity declares a weight for another Order's W position (e.g., ⛽ Strength declares affinity for 🦋 Hypertrophy). This is valid cross-talk. But if the weight table is keyed inconsistently (e.g., using emoji string keys instead of W enum integer keys), the computeRawVector() summation will miss or double-count.

**How to avoid:** Use W enum numeric keys consistently throughout all weight declarations. Never use emoji strings as keys in weight tables.

### Pitfall 4: Missing the 1-based indexing offset

**What goes wrong:** The W enum is 1-based (W.FOUNDATION=1, not 0). Float32Array indexed from 0 will have off-by-one errors.

**How to avoid:** Allocate `new Float32Array(WEIGHT_VECTOR_LENGTH + 1)` (62 slots, slot 0 unused). Access with W enum values directly.

### Pitfall 5: Over-populating the keyword dictionary with collision-prone singles

**What goes wrong:** Including single words like "heavy" or "easy" as unqualified keyword entries causes multi-dimensional scoring conflicts that Phase 3 cannot resolve cleanly.

**How to avoid:** Follow the compound-first rule from CONTEXT.md. Flag all collision-prone singles with `collision_prone: true`. The Phase 3 scorer can handle them, but the dict needs to mark them.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| exercise-library.md (markdown) | exercise-library.json (parsed) | Before Phase 1 | Direct JSON import; no parsing needed |
| weight-vectors.json (pre-computed) | Fresh computeRawVector() from weight tables | Phase 2 | Tables are authoritative; vectors derived not stored |
| order_relevance / axis_emphasis fields (noise) | Dropped; Type + equipment_tier + gold_gated carry the signal | Phase 2 decision | Cleaner interface; relevant signal preserved |

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest ^3.0.0 (configured in vite.config.ts) |
| Config file | `canvas/vite.config.ts` — test block with `include: ["tests/**/*.test.ts"]` |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` (same — all tests in one suite) |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| WGHT-01 | computeRawVector('2123') returns 61-element array with ⛽=+8, 🏛=+8, 🪡=+8, 🔵=+8 | unit | `cd canvas && npm test` | ❌ Wave 0 |
| WGHT-01 | computeRawVector('2123') has 🌋 Gutter ≤ -6 (Order hard suppression propagates) | unit | `cd canvas && npm test` | ❌ Wave 0 |
| WGHT-01 | computeRawVector sums clamp correctly at ±8 boundary | unit | `cd canvas && npm test` | ❌ Wave 0 |
| WGHT-02 | ORDERS_WEIGHTS[2].self === 8 | unit | `cd canvas && npm test` | ❌ Wave 0 |
| WGHT-02 | ORDERS_WEIGHTS[7].suppressions has 🌋 at -8 (Restoration hard rule) | unit | `cd canvas && npm test` | ❌ Wave 0 |
| WGHT-02 | All 6 category tables have correct entry counts (7, 6, 5, 8, 22, 12) | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-02 | dial-keywords.json has ≥ 2,000 entries | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-02 | "strength" → dimension 2 (W.STRENGTH) with affinity_score ≥ 6 | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-02 | "chest" → dimension 14 (W.PUSH) | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-03 | exercises.json has ~2,085 entries | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-03 | Romanian Deadlift entry has aliases including "RDL" | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-04 | "barbell" keyword maps to Color tier 3 range | unit | `cd canvas && npm test` | ❌ Wave 0 |
| PARS-05 | "lats" keyword maps to Type W.PULL = 15 | unit | `cd canvas && npm test` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `cd canvas && npm test`
- **Per wave merge:** `cd canvas && npm test` (full suite)
- **Phase gate:** Full suite green before `/gsd:verify-work`

### Wave 0 Gaps
- [ ] `canvas/tests/weight-tables.test.ts` — covers WGHT-01, WGHT-02
- [ ] `canvas/tests/keyword-dict.test.ts` — covers PARS-02, PARS-03, PARS-04, PARS-05
- [ ] No new framework installs needed — Vitest already in package.json

---

## Research Question 7 (Continued): Plan Split Recommendation

Phase 2 splits naturally into three parallel-capable plans:

### Recommended Plan Split

**Plan 02-01: Weight Tables** (largest scope — 6 files × ~30-60 entries each)
- Create `canvas/src/weights/types.ts` with WeightEntry, DialWeightTable interfaces
- Author ORDERS_WEIGHTS (7 entries with affinities/suppressions)
- Author AXES_WEIGHTS (6 entries)
- Author TYPES_WEIGHTS (5 entries)
- Author COLORS_WEIGHTS (8 entries)
- Author BLOCKS_WEIGHTS (22 entries)
- Author OPERATORS_WEIGHTS (12 entries)
- Implement `computeRawVector(orderPos, axisPos, typePos, colorPos)` in index.ts
- Tests: weight-tables.test.ts (WGHT-01, WGHT-02)

**Plan 02-02: Exercise Dictionary** (data transformation — port + alias layer)
- Create `canvas/src/parser/types.ts` with ExerciseEntry interface
- Port exercise-library.json → `canvas/data/exercises.json` (drop order_relevance, axis_emphasis)
- Add alias layer: ~100-200 manual entries + auto-derivation rules
- Tests: exercise-dict section of keyword-dict.test.ts (PARS-03)

**Plan 02-03: Keyword Dictionary** (data mining — mine + build + type)
- Create `canvas/data/dial-keywords.json` from first-party sources
- Create `canvas/src/parser/keywords.ts` with KeywordEntry interface
- Mine CLAUDE.md, scl-directory.md for fitness vocabulary
- Supplement with voice-parser-architecture.md Layer 1 seed entries
- Identify and flag all collision-prone keywords
- Tests: keyword-dict.test.ts (PARS-02, PARS-04, PARS-05)

**Plan dependency:** Plans 02-02 and 02-03 can run in parallel. Plan 02-01 (weight tables) should run first or in parallel — it has no dependency on 02-02 or 02-03. computeRawVector() needs weight tables only.

**Why not merge 02-02 and 02-03:** Exercise dict is a data transformation job (port + add aliases). Keyword dict is a data mining + authoring job (read spec files, extract vocabulary, classify). Different skills, different sources. Separate plans means each plan has a clear, testable deliverable.

**Authoring cost estimate:**
- Plan 02-01 (weight tables): High authoring cost. ~6 tables × ~20 average entries = ~120 weight declarations with citations. The heaviest judgment work in Phase 2.
- Plan 02-02 (exercise dict): Medium effort. Port is mechanical; alias layer is the judgment work.
- Plan 02-03 (keyword dict): Medium effort. Mining is systematic; collision flagging is the judgment work.

---

## Open Questions

1. **Block and Operator weights in computeRawVector**
   - What we know: WGHT-01 requires 61-dimensional output. Block/Operator slots (W.WARM_UP through W.SAVE) will be 0 from computeRawVector, populated later by resolver.
   - What's unclear: Does Phase 3 resolver actually need the Block/Operator weights authored, or are they Phase 5 (rendering) only?
   - Recommendation: Author all 6 tables in Phase 2 (WGHT-02 requires it). computeRawVector outputs zeros for Block/Operator slots. Resolver and renderer use the tables later.

2. **exercises.json location: canvas/data/ vs canvas/src/parser/**
   - What we know: tsconfig has `resolveJsonModule: true`. JSON can be imported from anywhere in canvas/.
   - What's unclear: Should data/ be a separate directory from src/ for clarity?
   - Recommendation: `canvas/data/` for JSON assets, `canvas/src/` for TypeScript. Clean separation.

3. **Collision-prone keyword handling in the dict**
   - What we know: Single words like "heavy", "easy", "hard" are ambiguous.
   - What's unclear: Should they be included as low-affinity entries with `collision_prone: true`, or excluded entirely?
   - Recommendation: Include as `collision_prone: true` with their best-guess primary dimension. Phase 3 scorer reads the flag and applies disambiguation logic. Excluding them entirely would cause miss-matches on common inputs.

---

## Sources

### Primary (HIGH confidence)
- `middle-math/weights/order-weights.md` — all 7 Order weight declarations with citations
- `middle-math/weights/axis-weights.md` — all 6 Axis weight declarations with citations
- `middle-math/weights/type-weights.md` — all 5 Type weight declarations with citations
- `middle-math/weights/color-weights.md` — all 8 Color weight declarations with citations
- `middle-math/weights/block-weights.md` — all 22 Block + SAVE weight declarations
- `middle-math/weights/operator-weights.md` — all 12 Operator + SAVE weight declarations
- `middle-math/weights/weight-system-spec.md` — derivation formula, 4-step process, worked example
- `middle-math/weights/interaction-rules.md` — hierarchy and summation rules
- `canvas/src/types/scl.ts` — W enum positions, phonebook pattern, WEIGHT_VECTOR_LENGTH = 61
- `middle-math/exercise-library.json` — 2,085 entries, confirmed field structure via Node.js inspection
- `CLAUDE.md` — canonical SCL rules (hard rules, block sequences, type routing, equipment tiers)

### Secondary (MEDIUM confidence)
- `seeds/voice-parser-architecture.md` — Layer 1 vocabulary seed (~183 keyword entries)
- `.planning/phases/02-core-data/02-CONTEXT.md` — locked decisions confirmed

### Tertiary (LOW confidence)
- Manual alias candidates for gym slang — based on common gym vocabulary, not formally verified against exercise-library.md entries

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — TypeScript, Vitest already in canvas/; no new dependencies for Phase 2
- Weight table shape: HIGH — direct extension of Phase 1 phonebook pattern
- Weight rule citations: HIGH — all hard rules (-6 to -8) verified against CLAUDE.md and DRAFT files
- Cross-talk analysis: HIGH — all intra-category relationships verified against cited DRAFT files
- Exercise library structure: HIGH — verified via Node.js inspection of actual JSON
- Alias candidates: MEDIUM — gym slang is conventional knowledge, not spec-verified
- Keyword count estimate: MEDIUM — projection from source analysis, not exact count

**Research date:** 2026-03-14
**Valid until:** 2026-04-14 (30 days — stable first-party sources)

---

🧮
