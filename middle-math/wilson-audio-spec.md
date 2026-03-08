# Wilson Audio Route Specification
## CX-29 — 3-Layer Keyword Scoring for Voice Navigation

**Status:** COMPLETE
**Completed In:** Session 036 — claude/envelope-pipeline-036
**Depends On:** CX-22 (Floor Routing Spec), seeds/voice-parser-architecture.md, seeds/wilson-voice-identity.md
**Unblocks:** Automotive layer implementation (Phase 7+)

---

## Overview

Wilson is the audible form of the Ppl± publication standard. The voice parser
is the system that converts spoken or typed natural language into a navigation
target inside the Ppl± building. This spec defines the 3-layer keyword scoring
architecture that powers voice navigation.

**Critical design constraints:**

- **No AI model.** Pure keyword lookup + scoring. Runs client-side in milliseconds.
- **No conversation.** Wilson is not a chatbot. It confirms navigation. Nothing more.
- **No inference.** The system matches keywords, scores layers, and resolves. When
  confidence is low, it offers options — it does not guess and route.
- **Three outputs only:** (1) a zip code, (2) an Axis floor, (3) a content type.
  Every voice input resolves to one or more of these, or returns a not-understood response.

**Source documents:**
- `seeds/voice-parser-architecture.md` — full design spec
- `seeds/wilson-voice-identity.md` — Wilson identity, response patterns, confidence thresholds
- `middle-math/floor-routing-spec.md` — 109 content types mapped to 6 floors
- `middle-math/content-type-registry.json` — 109 content types with axis and route data

---

## Architecture: Three Independent Layers

Every input token is scored against all three layers simultaneously.
Layers do not cascade — a match in Layer 1 does not suppress Layer 2.
Final resolution combines scores from all active layers.

```
Input: "heavy pull day"
         │
         ├─→ Layer 1 (Zip) ──────────► Order match: "heavy" → ⛽ Strength
         │                             Type match:  "pull" → 🪡 Pull
         │                             (partial zip — no Axis or Color hit)
         │
         ├─→ Layer 2 (Floor) ─────────► Floor miss (no floor keyword)
         │
         └─→ Layer 3 (Content Type) ──► CT miss (no specific CT keyword)

Partial zip (2 components) → Floor resolution: 🏛 Piano Nobile (default for ⛽🪡)
Wilson response: "Pull day — could mean Classic Pulls 2123 or Functional Pulls 2223. Which?"
```

---

## Layer 1 — Zip Resolution

**Purpose:** Match spoken words to zip code components (Order, Axis, Type, Color).
**Output:** A partial or complete 4-dial zip code.
**Keyword count estimate:** ~1,100 entries

### Layer 1A — Order Keywords (7 Orders, ~70 entries)

| Order | Primary keyword | Synonyms and aliases |
|-------|----------------|----------------------|
| 🐂 Foundation | "foundation" | "learn", "beginner", "intro", "basics", "drill", "form", "technique", "on-ramp" |
| ⛽ Strength | "strength" | "heavy", "max", "barbell", "loaded", "compound", "low rep", "neural" |
| 🦋 Hypertrophy | "hypertrophy" | "pump", "volume", "growth", "bodybuilding", "muscle", "high rep" |
| 🏟 Performance | "performance" | "test", "benchmark", "pr", "max effort", "competition", "sport", "assessment" |
| 🌾 Full Body | "full body" | "total body", "integrated", "flow", "combo", "hybrid", "whole body" |
| ⚖ Balance | "balance" | "correction", "weak point", "asymmetry", "imbalance", "compensate", "accessory" |
| 🖼 Restoration | "restoration" | "recovery", "rest", "mobility", "stretch", "soft", "easy", "gentle", "somatic" |

### Layer 1B — Axis Keywords (6 Axes, ~60 entries)

| Axis | Primary keyword | Synonyms and aliases |
|------|----------------|----------------------|
| 🏛 Basics | "classic" | "basics", "fundamental", "traditional", "standard", "barbell", "bilateral" |
| 🔨 Functional | "functional" | "athletic", "unilateral", "sport", "movement", "standing", "real world" |
| 🌹 Aesthetic | "aesthetic" | "isolation", "definition", "shape", "feel", "mind muscle", "cable", "machine" |
| 🪐 Challenge | "challenge" | "hard", "advanced", "difficult", "brutal", "extreme", "deficit", "pause", "tempo" |
| ⌛ Time | "timed" | "emom", "amrap", "density", "clock", "interval", "zone", "steady state" |
| 🐬 Partner | "partner" | "social", "with someone", "spotter", "paired", "team", "cooperative" |

### Layer 1C — Type Keywords (5 Types, ~50 entries)

| Type | Primary keyword | Synonyms and aliases |
|------|----------------|----------------------|
| 🛒 Push | "push" | "chest", "press", "bench", "tricep", "shoulder", "overhead", "dips" |
| 🪡 Pull | "pull" | "back", "row", "deadlift", "hinge", "bicep", "lat", "pulldown", "pullup" |
| 🍗 Legs | "legs" | "squat", "quad", "hamstring", "glute", "lunge", "leg day", "lower body" |
| ➕ Plus | "power" | "olympic", "plyometric", "carry", "core", "total power", "explosive", "sprint" |
| ➖ Ultra | "cardio" | "conditioning", "endurance", "aerobic", "run", "row", "bike", "zone 2", "ultra" |

### Layer 1D — Color Keywords (8 Colors, ~80 entries)

| Color | Primary keyword | Synonyms and aliases |
|-------|----------------|----------------------|
| ⚫ Teaching | "teaching" | "coached", "learn", "instruction", "cues", "comprehension", "drilling", "slow" |
| 🟢 Bodyweight | "bodyweight" | "no equipment", "home", "park", "hotel", "calisthenics", "no gym" |
| 🔵 Structured | "structured" | "programmed", "prescribed", "trackable", "repeatable", "standard" |
| 🟣 Technical | "technical" | "precision", "quality", "form focus", "skill", "low volume", "perfect" |
| 🔴 Intense | "intense" | "max effort", "high volume", "supersets", "dense", "brutal", "all out" |
| 🟠 Circuit | "circuit" | "stations", "loop", "rotation", "HIIT circuit", "station-based" |
| 🟡 Fun | "fun" | "play", "variety", "explore", "experiment", "sandbox", "mixed" |
| ⚪ Mindful | "mindful" | "slow", "breathe", "tempo", "meditative", "parasympathetic", "gentle" |

### Layer 1E — Exercise Name Keywords (~900 entries)

Every exercise in `exercise-library.md` (~2,185 entries) contributes its name
as a keyword that resolves directly to a Type component.

- "Romanian deadlift" → 🪡 Pull
- "bench press" → 🛒 Push
- "back squat" → 🍗 Legs
- "power clean" → ➕ Plus (GOLD-gated)
- "rowing machine" → ➖ Ultra

Abbreviations and common variants are included:
- "RDL" → Romanian deadlift → 🪡 Pull
- "bench" → bench press → 🛒 Push
- "squat" → back squat → 🍗 Legs (or front squat, goblet squat — same Type)

**Keyword count for Layer 1E:** ~900 (exercise names × ~0.4 abbreviation rate)

**Total Layer 1 estimate:** ~1,160 entries

---

## Layer 2 — Floor Resolution

**Purpose:** Match spoken words to one of the 6 Axis floors.
**Output:** An Axis floor (🏛 🔨 ⌛ 🐬 🌹 🪐) + optional content type filter.
**Keyword count estimate:** ~300 entries

### Floor Primary Keywords (6 floors, ~30 entries)

| Floor | Primary keyword | Latin name |
|-------|----------------|------------|
| 🏛 Piano Nobile | "workout", "training" | Firmitas |
| 🔨 Ground Floor | "library", "tools", "exercises", "scripts" | Utilitas |
| ⌛ 2nd Floor | "calendar", "history", "archive", "seasonal" | Temporitas |
| 🐬 3rd Floor | "community", "partner", "coaching", "social" | Sociatas |
| 🌹 4th Floor | "personal", "my workouts", "progress", "logs" | Venustas |
| 🪐 5th Floor | "research", "deep", "cosmogram", "architecture" | Gravitas |

### Floor Alias Keywords (~120 entries)

Aliases drawn from floor character descriptions in floor-routing-spec.md:

**🏛 Piano Nobile aliases:** "deck", "card", "zip", "operis", "scl", "reference",
"program", "today's workout", "what's today", "tomorrow"

**🔨 Ground Floor aliases:** "exercise", "movement", "technique", "how to",
"find an exercise", "what is", "muscle", "equipment", "gear"

**⌛ 2nd Floor aliases:** "what day", "last week", "this month", "when", "next",
"previous", "schedule", "past sessions", "date"

**🐬 3rd Floor aliases:** "with someone", "spotter", "class", "group", "coach",
"trainer", "pair", "team", "friends"

**🌹 4th Floor aliases:** "my history", "last time", "I did", "my sessions",
"bookmark", "saved", "favourite", "profile"

**🪐 5th Floor aliases:** "cosmogram", "seed", "whiteboard", "spec", "architecture",
"deep reference", "deck identity", "systems"

### Content Type Name Keywords as Floor Signals (~150 entries)

Each of the 109 content type names in content-type-registry.json functions as
a Layer 2 floor signal, routing to that content type's primary floor.

Examples:
- "operis" / "operis edition" → 🏛 Piano Nobile (CT-002)
- "cosmogram" → 🏛/🪐 (CT-003, primary 🏛, secondary 🪐)
- "exercise library" → 🔨 Ground Floor (CT-020)
- "zip web" → 🔨 Ground Floor (CT-022)
- "season" → ⌛ 2nd Floor (CT-040–044 range)
- "community" → 🐬 3rd Floor
- "log" / "session log" → 🌹 4th Floor (CT-060 range)

**Total Layer 2 estimate:** ~300 entries

---

## Layer 3 — Content Type Resolution

**Purpose:** Match spoken words to one of the 109 Ppl± content types.
**Output:** A specific content type ID (CT-001 through CT-109) + its primary floor.
**Keyword count estimate:** ~800 entries

Content types are drawn from `middle-math/content-type-registry.json`.
Each content type contributes:
1. Its exact name as a keyword (e.g., "The Workout Card" → CT-001)
2. A shortened colloquial form (e.g., "workout card", "card" → CT-001)
3. Synonyms and aliases specific to that type

### High-Priority Content Types (30 types for launch, ~300 entries)

| CT | Name | Keywords |
|----|------|---------|
| CT-001 | The Workout Card | "card", "workout card", "room", "this room" |
| CT-002 | The Operis Edition | "operis", "today's operis", "daily", "edition" |
| CT-003 | The Deck Cosmogram | "cosmogram", "deck research", "deck identity deep" |
| CT-004 | The Deck Identity | "deck identity", "deck overview", "deck map" |
| CT-005 | The Zip Code Address | "zip code", "address", "room address" |
| CT-008 | The Order Profile | "order profile", "what is strength", "order explained" |
| CT-009 | The Axis Profile | "axis profile", "what is basics", "floor profile" |
| CT-010 | The Type Profile | "type profile", "push type", "pull type", "legs type" |
| CT-020 | The Exercise Library Entry | "exercise", "how do I", "show me", "what is" |
| CT-040 | Seasonal Content | "season", "seasonal", "time of year" |
| CT-060 | User Session Log | "my log", "session log", "what I did", "history" |

### Remaining Content Types (~500 entries for all 109)

All 109 content type names + short forms + 2–4 synonyms each.
Full keyword table is generated from content-type-registry.json at build time.

**Total Layer 3 estimate:** ~800 entries

---

## Scoring Rules

### Per-Token Scoring

Each word in the input is scored independently against all three layers:

| Layer | Match type | Points |
|-------|-----------|--------|
| Layer 1 | Exact keyword match to Order | 3 pts for that Order position |
| Layer 1 | Exact keyword match to Axis | 3 pts for that Axis position |
| Layer 1 | Exact keyword match to Type | 3 pts for that Type position |
| Layer 1 | Exact keyword match to Color | 3 pts for that Color position |
| Layer 1 | Exercise name → Type | 2 pts for that Type position |
| Layer 2 | Floor keyword match | 3 pts for that floor |
| Layer 2 | Content type name → floor | 2 pts for that floor |
| Layer 3 | Content type exact name | 3 pts for that CT |
| Layer 3 | Content type alias | 2 pts for that CT |

### Phrase Matching

Multi-word phrases are scored as a unit before single tokens:
- "full body" scores before "body" alone
- "no equipment" scores before "equipment" alone
- Phrase matches add 1 bonus point over their component single-token score

### Zip Resolution Threshold

| Components matched | Outcome |
|-------------------|---------|
| All 4 (Order + Axis + Type + Color) | Full zip resolved — navigate directly |
| 3 components | Near-match — offer 1–3 candidate zips for confirmation |
| 2 components | Partial zip — resolve to floor + suggest zip family |
| 1 component | Single-signal — resolve to floor only |
| 0 | No zip signal |

### Confidence Thresholds

Thresholds from `seeds/wilson-voice-identity.md`:

| Confidence | Threshold | Action |
|-----------|-----------|--------|
| High | > 0.85 | Navigate immediately |
| Moderate | 0.65–0.85 | Announce destination, ask confirmation |
| Low | 0.30–0.65 | Offer 2–3 options |
| Not understood | < 0.30 | Invite retry |

### Disambiguation Priority

When multiple layers match with similar scores, resolve in this order:

1. **Layer 1 (Zip)** wins over Layer 2 and Layer 3 — a specific room beats a floor
2. **Layer 2 (Floor)** wins over Layer 3 — a floor beats a content type
3. **Layer 3 (Content Type)** is used only when Layer 1 and Layer 2 are both weak

Exception: if Layer 3 (content type) scores > 0.9 and identifies a CT with a
unique floor that differs from any Layer 2 signal, Layer 3 overrides Layer 2.
This handles cases like "show me the cosmogram for deck 7" where the CT
(CT-003) routes to both 🏛 and 🪐 depending on intent.

### Partial Match Cascade

When a full zip cannot be resolved (fewer than 4 components):
- Known components filter the registry to the matching zip family
- The system offers the highest-bloom member of the zip family as a suggestion
- If user is anonymous, offer the first entry in the zip family (lowest numeric)

---

## Wilson Voice Register by Floor

Wilson's tonal register shifts by floor. These shifts are in pace and
vocabulary, not in persona — Wilson does not change who it is.

### 🏛 Piano Nobile — Full Technical Register

Wilson speaks precisely and completely. Full set/rep prescription.
Full block sequence. Uses Ppl± vocabulary natively.

> "Heavy Classic Pulls — 2123. Six blocks. Bread and Butter: Romanian
> deadlift, weighted pull-up, Pendlay row. Four sets, five reps.
> Three minutes rest. Sixty-five minutes estimated."

**Vocabulary:** Zip codes, block names, exercise names from ExRx standard,
Order names, rep/set/rest notation. No synonyms — exact terminology.

### 🔨 Ground Floor — Utility Register

Wilson is operational. Confirms actions. Returns search results.

> "Searching exercise library for Romanian deadlift. Showing 3 results."
> "Deck 7 — Strength Basics — 40 rooms, 5 types."

**Vocabulary:** Action verbs (searching, showing, loading), counts, categories.
No workout cues here — this floor is navigation and reference.

### ⌛ 2nd Floor — Temporal Register

Wilson orients to time. Announces dates, streaks, schedule context.

> "March 6th, 2026. Thursday. Week 9 of the build."
> "Last logged session at this room: February 28th."

**Vocabulary:** Dates, ordinals, durations, before/after, week/month framing.
No present tense coaching — historical and contextual only.

### 🐬 3rd Floor — Social Register

Wilson uses second-person. Acknowledges the partner context.

> "Partner session ready. Alternating sets confirmed."
> "Your spotter can view the session card at this address."

**Vocabulary:** "you", "your partner", "both", "alternating", "rotation".
Does not address the partner directly — speaks to the user about the partner.

### 🌹 4th Floor — Personal Register

Wilson references the user's history directly. First-person context signals.

> "You've logged 3 sessions here. Bloom level: Active."
> "Your last logged weight for weighted pull-up: 35kg added."

**Vocabulary:** "you've", "your", "last time", "previously", "history".
Uses logged data. Does not manufacture context if no data exists.

### 🪐 5th Floor — Research Register

Wilson slows down. Announces document titles and section headers.
Does not summarize — announces and waits.

> "Deck 7 Cosmogram. Strength Basics. Deep reference document."
> "Section 3: Exercise character analysis. Opening."

**Vocabulary:** Document names, section labels, author/date context.
Wilson does not editorialize on research content — it announces and presents.

---

## Keyword Count Summary

| Layer | Sub-category | Estimated Entries |
|-------|-------------|-------------------|
| Layer 1A | Order keywords | ~70 |
| Layer 1B | Axis keywords | ~60 |
| Layer 1C | Type keywords | ~50 |
| Layer 1D | Color keywords | ~80 |
| Layer 1E | Exercise name keywords | ~900 |
| **Layer 1 Total** | | **~1,160** |
| Layer 2 — Floor primary | Floor names + Latin | ~30 |
| Layer 2 — Floor aliases | Character aliases | ~120 |
| Layer 2 — CT-as-floor | Content type → floor | ~150 |
| **Layer 2 Total** | | **~300** |
| Layer 3 — High priority CTs | 30 types, launch set | ~300 |
| Layer 3 — Remaining CTs | 79 additional types | ~500 |
| **Layer 3 Total** | | **~800** |
| **Grand total** | | **~2,260 keyword entries** |

---

## Implementation Notes

### Build Time vs Runtime

The keyword table is built at app initialization (or build time for static
apps) from:
1. The SCL emoji dictionary (CLAUDE.md) — Orders, Axes, Types, Colors
2. `exercise-library.md` via `scripts/middle-math/parse_exercise_library.py`
3. `middle-math/content-type-registry.json` — 109 content types
4. Hardcoded aliases (this document)

The runtime lookup is a plain dictionary lookup (`O(1)` per token).
No regex. No fuzzy matching. No AI inference.

### Normalization

Before scoring, all inputs are:
1. Lowercased
2. Stripped of punctuation
3. Tokenized by whitespace
4. Tested for multi-word phrases (longest-match-first)

### Phonetic Tolerance

For voice input, common mispronunciations are handled by alias entries:
- "hypertrophy" / "hyper trophy" / "hypertrify" → 🦋 Hypertrophy
- "emom" / "e mom" / "every minute" → ⌛ Time
- "Romanian" / "Roman-ian" / "RDL" → Romanian Deadlift → 🪡 Pull

### No AI Dependency

This system makes no API calls. It performs no language model inference.
It is a lookup table with scoring arithmetic. It runs in < 10ms on any
client device. The tradeoff is brittleness on novel phrasing — the system
handles known vocabulary and fails gracefully on unknown input by returning
low confidence and inviting retry.

---

## Wilson Response Script Reference

Full response patterns from `seeds/wilson-voice-identity.md`:

```
High confidence (> 0.85):
  "Heavy pull. Classic Pulls — 2123. Going there."

Moderate confidence (0.65–0.85):
  "I'm reading heavy pull, Classic Pulls — 2123. Confirm?"

Low confidence (0.30–0.65):
  "Pull day could mean Classic Pulls — 2123, or Functional Pulls — 2223. Which?"

Not understood (< 0.30):
  "Try again. Say the training focus, muscle group, or room you want."

Floor navigation (Layer 2 only):
  "Library floor. Exercise library — Ground Floor. Opening."

Content type navigation (Layer 3):
  "Showing deck cosmogram for Strength Basics — Deck 7."
```

---

*CX-29 complete. Closes Wave 4. Wilson audio layer ready for Phase 7 implementation.*
