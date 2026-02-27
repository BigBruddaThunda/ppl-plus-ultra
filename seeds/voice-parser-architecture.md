---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 5/6
blocks: nothing in Phase 2-4
depends-on: seeds/numeric-zip-system.md, seeds/experience-layer-blueprint.md, seeds/axis-as-app-floors.md, seeds/content-types-architecture.md, scl-directory.md
connects-to: seeds/automotive-layer-architecture.md, seeds/mobile-ui-architecture.md, seeds/wilson-voice-identity.md
---

# 🔍 Voice Parser Architecture — Universal Building Navigation

🔵🟣 — structured + technical

## One Sentence

The PPL± voice parser is the building's front desk — a client-side, AI-free keyword scoring system that converts any natural language input (spoken or typed) into three addressing coordinates (zip code + floor + content type) by scoring against a ~13,000-entry vocabulary built from all 61 SCL attributes, 6 app floors, 109 content types, and ~2,185 exercises.

---

## Scope — What The Parser Handles

The parser is not just a workout selector. It is the navigation interface for the entire building. Any input → a location in the app.

**Three addressing coordinates:**
1. **Zip code** (4 digits): Which room — Order + Axis + Type + Color
2. **Floor** (1 of 6): Which axis layer — 🏛 tools, 🔨 utilitas, 🌹 personal, 🪐 deep, ⌛ time, 🐬 community
3. **Content type** (1 of 109): Which kind of content within that floor — workout, exercise info, progress stats, almanac entry, educational article, playlist, thread, etc.

Not every input specifies all three. The parser returns the highest-confidence interpretation of what was asked and routes accordingly.

---

## Three-Layer Vocabulary

### Layer 1 — Zip Keywords (26 dial positions)

Each of the 26 SCL emoji has a set of natural language synonyms that map to its numeric position.

**Order keywords:**
| Emoji | Position | Keywords |
|-------|----------|---------|
| 🐂 | 1 | foundation, beginner, learn, technique, light, easy, intro, pattern, base, sub-max |
| ⛽ | 2 | strength, heavy, low reps, 5x5, neural, force, strong, max, barbell, power |
| 🦋 | 3 | hypertrophy, muscle, size, volume, pump, growth, bodybuilding, 8-12, aesthetic load |
| 🏟 | 4 | performance, test, PR, max effort, competition, benchmark, record |
| 🌾 | 5 | full body, total body, integrated, flow, complex, everything |
| ⚖ | 6 | balance, correction, weak links, asymmetry, rehab, fix, gap, imbalance |
| 🖼 | 7 | restoration, recovery, rest, easy, light, heal, mobility, chill, deload |

**Axis keywords:**
| Emoji | Position | Keywords |
|-------|----------|---------|
| 🏛 | 1 | basics, classic, barbell, fundamental, standard, traditional, old school, proven |
| 🔨 | 2 | functional, unilateral, athletic, movement, real world, sport, single leg, standing |
| 🌹 | 3 | aesthetic, isolation, pump, feel, shape, appearance, mind-muscle, cable, look |
| 🪐 | 4 | challenge, hard, advanced, difficult, brutal, tough, advanced, deficit, pause |
| ⌛ | 5 | time, EMOM, AMRAP, timed, clock, interval, density, stopwatch |
| 🐬 | 6 | partner, buddy, together, social, group, spotter, friend |

**Type keywords:**
| Emoji | Position | Keywords |
|-------|----------|---------|
| 🛒 | 1 | push, chest, press, bench, shoulders, triceps, overhead, push-up |
| 🪡 | 2 | pull, back, row, pulldown, lat, biceps, rear delt, hinge, deadlift, pull-up |
| 🍗 | 3 | legs, squat, quad, hamstring, glutes, calves, lower body |
| ➕ | 4 | plus, power, core, olympic, carry, plyo, explosive, full body power |
| ➖ | 5 | ultra, cardio, conditioning, running, rowing, bike, aerobic, zone 2 |

**Color keywords:**
| Emoji | Position | Keywords |
|-------|----------|---------|
| ⚫ | 1 | teaching, coaching, technique, slow, learn, cues, form |
| 🟢 | 2 | bodyweight, no equipment, home, hotel, park, outdoors, calisthenics |
| 🔵 | 3 | structured, programmed, sets reps, trackable, logged, scheduled |
| 🟣 | 4 | technical, precision, quality, careful, skill, exact |
| 🔴 | 5 | intense, hard, max, high volume, superset, brutal, push it |
| 🟠 | 6 | circuit, stations, rotation, loop, around the room |
| 🟡 | 7 | fun, play, variety, explore, mix it up, different, switch |
| ⚪ | 8 | mindful, slow, breath, meditative, calm, gentle, tempo |

### Layer 2 — Floor Keywords (6 floors)

Each floor has natural language triggers that route to the floor rather than a specific zip.

| Floor | Emoji | Keywords |
|-------|-------|---------|
| Firmitas / Room | 🏛 | room, workout, session, today, train, lift, exercise (generic), floor, building |
| Utilitas / Tools | 🔨 | tools, calculator, library, lookup, find exercise, how-to, equipment, search |
| Venustas / Personal | 🌹 | my history, progress, stats, how am I doing, log, personal, my data, records |
| Gravitas / Deep | 🪐 | learn, why, science, deep dive, article, education, research, explain |
| Temporitas / Time | ⌛ | calendar, schedule, almanac, seasonal, month, today's date, when |
| Sociatas / Community | 🐬 | community, what are people saying, discussion, thread, post, share |

### Layer 3 — Content Type Keywords (109 types from seeds/content-types-architecture.md)

Subset of high-priority types for launch (30 types → expand post-launch):

| Content type | Keywords |
|-------------|---------|
| Workout card | workout, session, room, train today |
| Exercise info | what is, how to, explain exercise, form for |
| PR log | personal record, PR, max, best set |
| Volume stats | how much, volume, total, week |
| Seasonal context | season, time of year, almanac, what month |
| Playlist | music, playlist, songs, what to listen to |
| EMOM | EMOM, every minute, timed blocks |
| AMRAP | AMRAP, as many as possible, max reps |
| Rest day | rest, off day, recovery day |
| Deck overview | deck, what's in this deck, 40 rooms |

---

## Worked Examples

### Example 1 — Workout Request
**Input:** "heavy pull day"
**Layer 1 scoring:**
- "heavy" → Order: ⛽ (score 8)
- "pull" → Type: 🪡 (score 8)
- Axis: unspecified → default to 🏛 Basics (score 3)
- Color: unspecified → default to 🔵 Structured (score 3)
**Result:** zip=2123 (⛽🏛🪡🔵), floor=🏛 room, content=workout
**Route:** `/zip/2123`

### Example 2 — Exercise Info Query
**Input:** "how do I do a Romanian deadlift"
**Layer 1 scoring:** "deadlift" → Type: 🪡 (score 5)
**Layer 2 scoring:** "how do I" → floor: 🔨 Tools (score 9)
**Layer 3 scoring:** "how to" → content: exercise info (score 9)
**Result:** zip=nil (exercise info, not workout), floor=🔨 utilitas, content=exercise_info, exercise_name="Romanian deadlift"
**Route:** `/tools/exercise/romanian-deadlift`

### Example 3 — Personal Progress
**Input:** "how am I doing on legs this month"
**Layer 2 scoring:** "how am I doing" → floor: 🌹 personal (score 9)
**Layer 1 scoring:** "legs" → Type: 🍗 (score 8)
**Layer 3 scoring:** "this month" → temporal filter
**Result:** floor=🌹 personal, content=volume_stats, type_filter=🍗
**Route:** `/me/history?type=3&period=month`

### Example 4 — Community
**Input:** "what are people saying about restoration workouts"
**Layer 2 scoring:** "what are people saying" → floor: 🐬 community (score 9)
**Layer 1 scoring:** "restoration" → Order: 🖼 (score 8)
**Result:** floor=🐬 sociatas, content=community_thread, order_filter=🖼
**Route:** `/community?order=7`

### Example 5 — Almanac / Seasonal
**Input:** "what's the training focus for February"
**Layer 2 scoring:** "almanac", "month" → floor: ⌛ time (score 9)
**Layer 3 scoring:** "training focus" → content: seasonal_context
**Result:** floor=⌛ temporitas, content=almanac_month, month=February
**Route:** `/almanac/february`

### Example 6 — Educational / Deep
**Input:** "explain why strength training uses low reps"
**Layer 2 scoring:** "explain why" → floor: 🪐 gravitas (score 9)
**Layer 1 scoring:** "strength" → Order: ⛽ (score 6), "low reps" confirms
**Layer 3 scoring:** "explain" → content: educational_article
**Result:** floor=🪐 gravitas, content=article, topic="neural-adaptation-low-reps"
**Route:** `/learn/neural-adaptation-low-reps`

### Example 7 — Vague Mood Input
**Input:** "I want something easy today"
**Layer 1 scoring:** "easy" → Order: 🖼 (score 5) OR 🐂 (score 4)
**Disambiguation:** "today" → lean toward Operis recommendation
**Result:** low confidence → prompt: "Did you mean restoration (🖼) or foundation (🐂)?"
**Route:** Confirmation dialog before navigating

### Example 8 — Multi-Intent
**Input:** "play me a strength playlist and show me my best sets"
**Intent 1:** "playlist" → Layer 3: playlist, Order: ⛽
**Intent 2:** "best sets" → Layer 2: 🌹 personal, Layer 3: PR_log
**Result:** Two results returned. App asks: "Which first?" → displays both as options
**Route:** User selects; both destinations queued

---

## Exercise Library as Vocabulary

The ~2,185 exercises in `exercise-library.md` are part of the voice parser's vocabulary. When the parser detects an exercise name (or near-match), it routes to that exercise's info page or surfaces workouts containing it.

**Exercise entry JSON format:**
```typescript
interface ExerciseVocabEntry {
  name: string;            // canonical name: "Romanian Deadlift"
  aliases: string[];       // ["RDL", "stiff leg deadlift", "Romanian DL"]
  scl_type: number;        // 1-5 (Type position)
  axis_affinity: number;   // 1-6 (primary axis)
  section: string;         // library section: "D", "H", etc.
  is_gold: boolean;        // GOLD gate status
}
```

**Fuzzy matching:** Levenshtein distance ≤ 2 on exercise names. "Romanian deadlfit" matches "Romanian Deadlift". Aliases expand coverage. Common gym abbreviations (RDL, OHP, DB, KB) are pre-aliased.

---

## Content Type Vocabulary by Floor

Full 109 types from `seeds/content-types-architecture.md` organized by floor. At launch, implement top 30. Expand in subsequent sessions.

**🏛 Firmitas floor (workout content):** workout card, deck overview, block explanation, operator definition
**🔨 Utilitas floor (tools):** exercise info, exercise demo, weight calculator, 1RM estimator, rest timer, equipment guide, warm-up generator
**🌹 Venustas floor (personal):** workout history, PR log, volume stats, progress chart, exercise frequency, session streak
**🪐 Gravitas floor (educational):** training article, exercise science, programming principle, nutrition note, recovery guide, biomechanics
**⌛ Temporitas floor (time):** almanac entry, seasonal context, monthly focus, weekly cadence, rest day guide, annual rhythm
**🐬 Sociatas floor (community):** community thread, workout discussion, exercise question, progress share, partner request

---

## Routing Architecture

```typescript
interface ParseResult {
  zipCode?: string;           // e.g. "2123"
  floor?: number;             // 1-6 (axis position)
  contentType?: string;       // e.g. "exercise_info"
  entityName?: string;        // e.g. "Romanian Deadlift"
  filters?: Record<string, number>; // e.g. { type: 3, period: 'month' }
  confidence: number;         // 0-1
  ambiguous: boolean;         // true if multiple good matches
  alternatives?: ParseResult[]; // other interpretations if ambiguous
}

function routeFromParse(result: ParseResult): string {
  if (result.contentType === 'exercise_info' && result.entityName) {
    return `/tools/exercise/${slugify(result.entityName)}`;
  }
  if (result.floor === 6 /* community */) {
    return result.zipCode
      ? `/zip/${result.zipCode}/community`
      : `/community`;
  }
  if (result.floor === 4 /* personal */) {
    const params = new URLSearchParams(result.filters as Record<string, string>);
    return `/me/history?${params}`;
  }
  if (result.zipCode) {
    const floorPath = floorToPath(result.floor);
    return floorPath
      ? `/zip/${result.zipCode}/${floorPath}`
      : `/zip/${result.zipCode}`;
  }
  return '/'; // fallback to Operis
}
```

**New routes implied by the parser:**
- `/tools/exercise/[slug]` — exercise info pages (Session J)
- `/almanac/[month]` — almanac month pages (Session I)
- `/learn/[topic]` — educational articles (Session J)
- `/community?order=[n]` — filtered community view

---

## Technical Implementation

### Dictionary Structure

```typescript
interface VocabDictionary {
  orders: Array<{ position: number; emoji: string; keywords: string[] }>;
  axes:   Array<{ position: number; emoji: string; keywords: string[] }>;
  types:  Array<{ position: number; emoji: string; keywords: string[] }>;
  colors: Array<{ position: number; emoji: string; keywords: string[] }>;
  floors: Array<{ position: number; emoji: string; keywords: string[] }>;
  contentTypes: Array<{ id: string; floor: number; keywords: string[] }>;
  exercises: ExerciseVocabEntry[];
}
```

### Scoring Algorithm

```typescript
function scoreInput(input: string, dict: VocabDictionary): ParseResult {
  const tokens = tokenize(input.toLowerCase()); // split, stem, remove stopwords

  const orderScores = dict.orders.map(o => ({
    position: o.position,
    score: tokens.filter(t => o.keywords.some(k => fuzzyMatch(t, k))).length
  }));

  const axisScores  = dict.axes.map(a => ({ ... }));
  const typeScores  = dict.types.map(t => ({ ... }));
  const colorScores = dict.colors.map(c => ({ ... }));
  const floorScores = dict.floors.map(f => ({ ... }));
  const typeScores3 = dict.contentTypes.map(ct => ({ ... }));

  const order = maxScore(orderScores) ?? defaultOrder();
  const axis  = maxScore(axisScores)  ?? defaultAxis();
  const type  = maxScore(typeScores)  ?? null;
  const color = maxScore(colorScores) ?? defaultColor();
  const floor = maxScore(floorScores) ?? 1;
  const content = maxScore(typeScores3) ?? 'workout';

  const zipCode = type ? `${order}${axis}${type}${color}` : undefined;
  const confidence = calculateConfidence(orderScores, axisScores, typeScores, colorScores, floorScores);

  return { zipCode, floor, contentType: content, confidence, ambiguous: confidence < 0.70 };
}
```

### Size and Complexity Analysis

| Vocabulary layer | Entries | Size estimate |
|-----------------|---------|---------------|
| 26 dial positions × ~15 keywords avg | ~390 keywords | ~8 KB |
| 6 floors × ~20 keywords avg | ~120 keywords | ~2 KB |
| 109 content types × ~10 keywords avg | ~1,090 keywords | ~15 KB |
| 2,185 exercises × name + aliases | ~6,500 entries | ~150 KB |
| Stopwords, tokenizer | — | ~5 KB |
| **Total** | **~8,100 unique keywords** | **~180 KB** |

Dictionary loads once on app initialization. Scoring a single input: tokenize (~1ms) + scan dictionary (~5ms) = ~6ms total. No server round-trip. No AI model. No API key.

### Voice-to-Text Layer

Web Speech API (`window.SpeechRecognition`) handles voice input. Returns transcript string. Parser then scores the string.

```typescript
const recognition = new window.SpeechRecognition();
recognition.lang = 'en-US';
recognition.continuous = false;
recognition.interimResults = false;
recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  const result = scoreInput(transcript, dict);
  if (result.confidence > 0.85) {
    router.push(routeFromParse(result));
  } else {
    setParseResult(result); // show disambiguation UI
  }
};
```

Fallback for no Web Speech API support: text input only. The parser itself is agnostic to input method.

---

## Relationship to Wilson

Wilson reads back the parse result before navigating (when confidence < 1.0). This serves two functions:
1. Confirms the interpretation (reduces wrong navigations)
2. Teaches the vocabulary (users learn what "heavy pull" means in PPL± terms)

Wilson response for parse confirmation:
> "Heavy pull. I'm reading ⛽ Strength, 🪡 Pull, 🏛 Basics — Heavy Classic Pulls. Going there now."

Wilson does not say "I'm not sure" or "I didn't understand." Low-confidence parses offer options, not failures:
> "Pull day could be Classic Pulls, Functional Pulls, or Aesthetic Pulls. Which?"

---

## Build Session

**Session C-2** in `seeds/claude-code-build-sequence.md`.

Sequence: After Session A (routing works) and Session C (dial navigation works). C-2 adds the third input modality (voice/text) alongside dial navigation and direct URL entry.

---

## Onboarding Integration Idea

During Session E onboarding, show the user 3 example voice inputs and their results. Let them try one. This teaches the vocabulary passively before they need it. Plant the phrase "just tell me what you want" early.

---

🧮
