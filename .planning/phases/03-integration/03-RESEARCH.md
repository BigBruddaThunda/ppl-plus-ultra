# Phase 3: Integration - Research

**Researched:** 2026-03-14
**Domain:** Constraint resolver + text-to-zip scoring pipeline (TypeScript, Node/Vitest stack)
**Confidence:** HIGH

---

## Summary

Phase 3 wires together two things that Phase 2 left deliberately incomplete: (1) the interaction resolver that applies the constraint hierarchy on top of computeRawVector()'s raw summation, and (2) the text scorer that takes natural language input and produces ranked ParseResult candidates using the keyword dictionary and exercise data built in Phase 2.

The resolver is purely mathematical: it reads the raw vector from computeRawVector(), identifies any positions where a higher-priority dial has a hard suppression (≤ -6), and clamps those positions to the suppressing value, preventing lower-priority dial affinities from overriding them. All the rules live in interaction-rules.md (already committed). The resolver enforces them; the dial tables must not encode hierarchy.

The text scorer is a pipeline: tokenize input, look up terms in dial-keywords.json, accumulate per-dimension scores, identify top-scoring dial positions per dimension group, resolve those positions through the weight engine, and rank the resulting zip code candidates by confidence. Fuzzy matching (fastest-levenshtein for edit-distance typos, fuse.js for multi-word alias expansion) runs before the dictionary lookup to handle imperfect input.

Both libraries (fastest-levenshtein 1.0.16, fuse.js 7.1.0) are confirmed available on npm but not yet installed in canvas/. Installing them as runtime dependencies is a prerequisite task for this phase.

**Primary recommendation:** Build the resolver first (pure TypeScript, zero new dependencies, immediately testable against the hard suppression rules from CLAUDE.md), then build the text scorer on top of it.

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| WGHT-03 | Interaction resolver enforcing constraint hierarchy (Order > Color > Axis > Type) | interaction-rules.md defines the 4-rule algorithm; computeRawVector() provides the input vector; resolver is a pure function wrapping that output |
| WGHT-04 | Hard suppression logic (weight ≤ -6 is absolute, cannot be overridden by lower-priority dial) | interaction-rules.md Rule 1; resolver reads the priority-ordered dials and pins positions where the highest-priority suppression is ≤ -6 |
| PARS-01 | ParseResult type with zip code, weight vector, confidence score, and defaulted_dimensions field | New TypeScript interface in canvas/src/parser/; defaulted_dimensions must be populated on day one — STATE.md decision confirmed |
| PARS-06 | Fuzzy matching with typo tolerance (edit distance ≤ 2) via fastest-levenshtein | fastest-levenshtein@1.0.16 confirmed on npm; distance() function provides edit distance; threshold ≤ 2 per requirement |
| PARS-07 | Multi-word alias expansion via fuse.js | fuse.js@7.1.0 confirmed on npm; FuseOptions with threshold and keys config needed for exercise alias + keyword expansion |
| PARS-08 | Text-to-zip scoring pipeline that produces ranked candidate addresses from natural language input | Full pipeline: tokenize → fuzzy-expand → keyword-score → dial-resolve → weight-compute → rank; no AI, deterministic |

</phase_requirements>

---

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| TypeScript | ^5.7.0 (installed) | All Phase 3 modules | Already in canvas/package.json |
| Vitest | ^3.2.4 (installed) | All Phase 3 tests | Already configured, 6,815 tests passing |
| fastest-levenshtein | 1.0.16 | Edit-distance fuzzy match for PARS-06 | Required by spec, WASM-optimized, fastest option at this edit distance range |
| fuse.js | 7.1.0 | Multi-word alias expansion for PARS-07 | Required by spec, lightweight, works with string arrays from ExerciseEntry.aliases |

**Installation:**
```bash
cd canvas && npm install fastest-levenshtein fuse.js
```

Neither library is in canvas/package.json yet. Both must be added as runtime dependencies (not devDependencies) because the scorer runs at runtime, not only in tests.

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| (none new) | - | Phase 3 has no other new dependencies | Resolver and scorer are pure TS over existing data |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| fastest-levenshtein | natural / levenshtein package | fastest-levenshtein is WASM-based, ~10x faster; spec names it explicitly |
| fuse.js | FlexSearch, MiniSearch | fuse.js is spec-named explicitly; MiniSearch is more powerful but heavier |

---

## Architecture Patterns

### Recommended Project Structure
```
canvas/src/
├── weights/
│   ├── index.ts         — computeRawVector() + barrel (Phase 2, complete)
│   └── resolver.ts      — resolveVector() — NEW Phase 3
├── parser/
│   ├── types.ts         — ExerciseEntry (Phase 2, complete)
│   ├── keywords.ts      — KeywordEntry, DimensionId (Phase 2, complete)
│   ├── parse-result.ts  — ParseResult interface — NEW Phase 3
│   ├── tokenizer.ts     — normalizeInput(), tokenize() — NEW Phase 3
│   ├── scorer.ts        — scoreText() pipeline — NEW Phase 3
│   └── fuzzy.ts         — buildFuzzyMatcher(), expandTokens() — NEW Phase 3
canvas/tests/
├── resolver.test.ts     — hard suppression + hierarchy tests — NEW Phase 3
├── scorer.test.ts       — end-to-end text → ParseResult tests — NEW Phase 3
└── (existing tests unchanged)
```

### Pattern 1: Resolver as a Pure Transformation

The resolver takes the raw vector from computeRawVector() plus the four dial positions, and re-applies the constraint hierarchy as a post-processing pass.

**What:** A pure function `resolveVector(rawVec, orderPos, axisPos, typePos, colorPos): Float32Array`

**When to use:** Called immediately after computeRawVector() in any context that produces a final WeightVector. computeRawVector() stays as-is; resolver wraps it.

**Algorithm:**
```
For each W position i in 1..61:
  1. Read ORDER's declared weight at position i (from ORDERS_WEIGHTS[orderPos])
  2. If ORDER declared ≤ -6: pin vec[i] to that suppression value, stop
  3. Read COLOR's declared weight at position i (from COLORS_WEIGHTS[colorPos])
  4. If COLOR declared ≤ -6: pin vec[i] to that suppression value, stop
  5. Otherwise: keep rawVec[i] as-is (already summed and clamped in Steps 1-3)
```

The key insight from interaction-rules.md: the raw sum from computeRawVector() already handles Steps 1-3 (primary + affinity + suppression cascades). The resolver only needs to enforce the hard suppression ceiling from higher-priority dials. Soft weights are already summed correctly.

**Example:**
```typescript
// Source: middle-math/weights/interaction-rules.md Rule 1
function resolveVector(
  raw: Float32Array,
  orderPos: number,
  axisPos: number,
  typePos: number,
  colorPos: number
): Float32Array {
  const resolved = new Float32Array(raw);
  const orderEntry = ORDERS_WEIGHTS[orderPos];
  const colorEntry = COLORS_WEIGHTS[colorPos];

  for (let i = 1; i <= WEIGHT_VECTOR_LENGTH; i++) {
    const orderSupp = orderEntry?.suppressions[i] ?? 0;
    if (orderSupp <= -6) {
      resolved[i] = orderSupp;
      continue;
    }
    const colorSupp = colorEntry?.suppressions[i] ?? 0;
    if (colorSupp <= -6) {
      resolved[i] = colorSupp;
    }
  }
  return resolved;
}
```

Note: Axis and Type are "soft bias" and "soft context" per interaction-rules.md — their weights already contributed to the raw sum and do not need special resolver handling.

### Pattern 2: ParseResult as a First-Class Type

The ParseResult interface is required from day one with no retrofitting. STATE.md decision: `defaulted_dimensions` must be populated whenever a dial scores zero and defaults.

```typescript
// canvas/src/parser/parse-result.ts
export interface ParseResult {
  zip: string;               // emoji zip: e.g. "⛽🏛🪡🔵"
  numericZip: string;        // 4-digit: e.g. "2123"
  orderPos: number;
  axisPos: number;
  typePos: number;
  colorPos: number;
  weightVector: Float32Array;
  confidence: number;        // 0.0 – 1.0
  defaulted_dimensions: DimensionGroup[];  // which dials defaulted (scored zero)
  matchedTerms: string[];    // which input tokens contributed
}

type DimensionGroup = 'order' | 'axis' | 'type' | 'color';
```

`defaulted_dimensions` is populated by the scorer when a dimension group (order/axis/type/color) receives zero keyword signal from the input. The system defaults to the most neutral position and records the dimension as defaulted.

### Pattern 3: Scoring Pipeline

The text scorer is a deterministic pipeline with no AI component.

```
input string
  → normalize (lowercase, strip punctuation)
  → tokenize (split on whitespace + bigrams)
  → fuzzy expand (edit distance ≤ 2 via fastest-levenshtein against keyword terms)
  → alias expand (fuse.js against exercise aliases + keyword terms)
  → keyword lookup (exact match in dial-keywords.json)
  → accumulate dimension scores (sum affinity_score per DimensionId)
  → select best dial position per dimension group
  → resolve weight vector (computeRawVector → resolveVector)
  → compute confidence score
  → return ParseResult[]  (ranked by confidence, descending)
```

**Confidence score formula:** A simple normalized sum: `(totalMatchedScore / (inputTokenCount * MAX_SCORE_PER_TOKEN))`, clamped to [0, 1]. The exact formula is Claude's discretion — keep it simple and auditable.

**Candidates:** When the input is ambiguous (e.g., a Type keyword matches but Order is unclear), generate multiple ParseResult candidates by trying the top-2 scoring positions for the ambiguous dimension. Return all candidates ranked by confidence.

### Pattern 4: Fuzzy Matching Scope

Fuzzy matching must NOT run over the full 2,085-exercise list on every keystroke. Build a flat string list at module load time (all keyword terms + all exercise aliases), then use fastest-levenshtein's `closest()` function (finds closest match in an array) for typo correction.

```typescript
// canvas/src/parser/fuzzy.ts
import { closest, distance } from 'fastest-levenshtein';

// Built once at module load, not per-call
const ALL_TERMS: string[] = [...keywordTerms, ...exerciseAliases];

export function expandToken(token: string, maxDistance = 2): string[] {
  const match = closest(token, ALL_TERMS);
  if (distance(token, match) <= maxDistance) {
    return [match];
  }
  return [token]; // no close match, pass through
}
```

fuse.js handles multi-word phrases (e.g., "heavy back work" should match "heavy barbell back"). Configure with `threshold: 0.4, minMatchCharLength: 3, keys: ['term', 'aliases']`.

### Anti-Patterns to Avoid

- **Encoding hierarchy in dial tables:** The constraint hierarchy must live only in resolver.ts. ORDERS_WEIGHTS, AXES_WEIGHTS, etc., declare weights per-position but do not know about each other's priority. Any "Order wins over Axis" logic in a dial table is wrong.
- **Running fuzzy match per-query over full exercise list:** O(n) per token × 2,085 exercises × query latency. Build the flat terms list once at module init.
- **Calling resolveVector() without first calling computeRawVector():** The resolver pins hard suppression floors; it does not sum weights itself. Calling it on a zero vector produces wrong output.
- **Nullable confidence scores:** Confidence must always be a number in [0, 1]. An input with zero keyword matches should return a ParseResult with confidence 0 defaulting all four dimensions, not undefined or an error.
- **Multi-word alias stored as a single term in dial-keywords.json:** The keyword dictionary uses single-dimension affinity scores. Multi-word phrases need their own entries ("bench press" not just "bench" + "press" separately). This was enforced in Phase 2 but worth verifying before building the scorer.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Typo tolerance | Custom edit-distance implementation | fastest-levenshtein 1.0.16 | WASM-optimized, handles Unicode correctly, spec-named |
| Fuzzy phrase matching | Custom trigram or BK-tree | fuse.js 7.1.0 | Spec-named, handles multi-word alias arrays, configurable threshold |
| String normalization | Custom diacritic stripping | JS `str.normalize('NFD').replace(/\p{M}/gu, '')` | One-liner, no dependency needed |

**Key insight:** The complexity in Phase 3 is in the pipeline logic (how signals combine), not in any individual algorithm. The two libraries handle the hard parts of fuzzy string matching; the resolver logic is 20-30 lines of pure TypeScript.

---

## Common Pitfalls

### Pitfall 1: Resolver Double-Counts Suppressions

**What goes wrong:** The raw vector from computeRawVector() already includes suppression contributions from all dials (Steps 1-3). If the resolver re-applies all suppressions rather than only enforcing hard suppression ceilings, values will be doubly penalized.

**Why it happens:** The interaction-rules.md description of "apply hierarchy" sounds like re-running the suppression cascade with priority rules, not just checking for ≤ -6 floors.

**How to avoid:** The resolver reads the already-summed rawVec and only pins positions where a higher-priority dial's declared suppression is ≤ -6. It does not re-sum anything. Write a test: `resolveVector(rawVec, ...)` where rawVec already has a position at +4 from summed soft weights, and verify the resolver does not change it.

**Warning signs:** resolveVector() output has more negative values than expected; the worked example in weight-system-spec.md doesn't reproduce.

### Pitfall 2: defaulted_dimensions Not Populated

**What goes wrong:** The scorer returns a ParseResult without populating defaulted_dimensions, treating it as an optional field.

**Why it happens:** defaulted_dimensions feels like metadata, not a first-class output. Easy to defer.

**How to avoid:** Enforce in the ParseResult type (no optional `?` on defaulted_dimensions). The scorer must populate it even if empty (`[]` for a fully-resolved input, `['order', 'axis']` for a partial match). STATE.md decision: "retrofitting is a breaking API change."

**Warning signs:** Any test that asserts `result.defaulted_dimensions !== undefined` — if it needs that assertion, the type wasn't strict enough.

### Pitfall 3: fuse.js Threshold Too Aggressive

**What goes wrong:** fuse.js configured with a low threshold (e.g., 0.2) matches "chest" to "rest" or "test." Phase 3 is a development tool used by Jake; false positives in the scorer produce confusing debug output.

**Why it happens:** fuse.js threshold is a distance score, not an accuracy score — lower threshold means more strict. Unintuitive direction.

**How to avoid:** Set `threshold: 0.4` as the starting value. Write specific tests: "bench press" matches "Bench Press (Barbell)", "squat" does not match "squat rack" as an exercise. Tune based on test results.

**Warning signs:** Unrelated exercises appear in ranked candidates with confidence > 0.5.

### Pitfall 4: Scoring Pipeline Breaks on Collision-Prone Keywords

**What goes wrong:** The keyword "press" has `collision_prone: true` in the dictionary. A naive scorer that takes the first dimension match will route "press" to Push (chest) even when the input is "leg press."

**Why it happens:** Single-word lookup without bigram context.

**How to avoid:** When tokenizing, generate bigrams (adjacent word pairs) in addition to unigrams. Prefer bigram matches over unigram matches when both exist. "leg press" as a bigram maps to Legs; unigram "press" to Push. The longer match wins.

**Warning signs:** "leg press" returns Type=Push in ParseResult.

### Pitfall 5: Module Init Cost Hidden in Tests

**What goes wrong:** The fuzzy terms list is built on every test invocation, making the test suite slow enough that developers stop running it.

**Why it happens:** Building the flat terms list from exercises.json + dial-keywords.json involves JSON parsing and array flattening — cheap per invocation but visible at scale when tests run 100+ times.

**How to avoid:** Export the fuzzy matcher as a module-level singleton built at import time, not per-call. Vitest's module caching handles the rest.

---

## Code Examples

Verified patterns from the existing codebase:

### Accessing the Raw Vector for Resolver Input
```typescript
// Source: canvas/src/weights/index.ts
import { computeRawVector } from '../weights/index.js';
import { WEIGHT_VECTOR_LENGTH } from '../types/scl.js';

const raw = computeRawVector(orderPos, axisPos, typePos, colorPos);
// raw is Float32Array of length 62; slot 0 unused; slots 1-61 for W positions
```

### Reading a Dial Entry's Suppression for Resolver Check
```typescript
// Source: canvas/src/weights/orders.ts pattern
import { ORDERS_WEIGHTS, COLORS_WEIGHTS } from '../weights/index.js';

const orderEntry = ORDERS_WEIGHTS[orderPos];
const suppAtPosition = orderEntry?.suppressions[wPosition] ?? 0;
// suppAtPosition is WeightScale (-8 | -6 | -4 | -2 | 0 | 2 | 4 | 6 | 8)
// Hard suppression check: suppAtPosition <= -6
```

### KeywordEntry Lookup Pattern
```typescript
// Source: canvas/src/parser/keywords.ts + canvas/data/dial-keywords.json
import keywords from '../data/dial-keywords.json';
import type { KeywordEntry } from './keywords.js';

const dict = keywords as KeywordEntry[];
const entry = dict.find(e => e.term === normalizedToken);
if (entry && !entry.collision_prone) {
  dimensionScores[entry.dimension] += entry.affinity_score;
}
```

### W Enum Indexing for ParseResult Positions
```typescript
// Source: canvas/src/types/scl.ts
import { W, ORDERS, AXES, TYPES, COLORS } from '../types/scl.js';

// Order W positions: W.FOUNDATION (1) through W.RESTORATION (7)
// Axis W positions:  W.BASICS (8) through W.PARTNER (13)
// Type W positions:  W.PUSH (14) through W.ULTRA (18)
// Color W positions: W.TEACHING (19) through W.MINDFUL (26)

// Selecting best order position from accumulated dimension scores:
const orderScores = dimensionScores.slice(1, 8);  // W.FOUNDATION..W.RESTORATION
const bestOrderPos = orderScores.indexOf(Math.max(...orderScores)) + 1;
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| computeRawVector() as the final vector | computeRawVector() + resolveVector() | Phase 3 | Hard suppressions were not enforced in Phase 2 output; Phase 3 closes this gap |
| No ParseResult type | ParseResult with defaulted_dimensions from day one | Phase 3 decision | Prevents breaking API change later; STATE.md decision |
| Manual string matching | fastest-levenshtein + fuse.js | Phase 3 | Edit-distance tolerance and alias expansion were not possible with exact dictionary lookup alone |

**Note on computeRawVector():** Do not modify computeRawVector() itself. It correctly implements Steps 1-3. The resolver is an additive layer, not a replacement.

---

## Open Questions

1. **Default position when a dimension scores zero**
   - What we know: defaulted_dimensions must be populated when a dial scores zero
   - What's unclear: what is the "neutral default" position for each dial? (e.g., does Order default to position 3/Hypertrophy as the middle ground, or position 1?)
   - Recommendation: Default to the middle position for each dial (Order: 3/Hypertrophy, Axis: 1/Basics, Type: 1/Push, Color: 3/Structured) — these are the lowest-constraint options. Document the choice in parse-result.ts.

2. **Candidate count for ranked output**
   - What we know: PARS-08 says "ranked zip code candidates" — plural
   - What's unclear: how many candidates to return? All 1,680? Top-N?
   - Recommendation: Return top 5 candidates (hard limit). More than 5 is noise for the use cases described. Make it a configurable parameter with default 5.

3. **Bigram tokenization boundary**
   - What we know: collision-prone keywords require bigram context to score correctly
   - What's unclear: whether to generate all bigrams or only from adjacent content words
   - Recommendation: Generate all adjacent bigrams from the tokenized input (simple and deterministic). Bigram match scores override unigram match scores for the same position.

---

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Vitest ^3.2.4 (installed, 6,815 tests passing) |
| Config file | canvas/vite.config.ts (test.include: "tests/**/*.test.ts") |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` (single suite, no separation needed yet) |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| WGHT-03 | resolveVector() applies Order > Color > Axis > Type hierarchy | unit | `cd canvas && npm test -- resolver.test.ts` | Wave 0 |
| WGHT-04 | Weight ≤ -6 from higher-priority dial is not overridden by lower-priority affinity | unit | `cd canvas && npm test -- resolver.test.ts` | Wave 0 |
| PARS-01 | ParseResult interface has all required fields including defaulted_dimensions | unit | `cd canvas && npm test -- scorer.test.ts` | Wave 0 |
| PARS-06 | Typo input within edit distance 2 matches correct keyword | unit | `cd canvas && npm test -- scorer.test.ts` | Wave 0 |
| PARS-07 | Multi-word alias "Romanian deadlift" matches "RDL" exercise entry | unit | `cd canvas && npm test -- scorer.test.ts` | Wave 0 |
| PARS-08 | "heavy barbell back work" returns ParseResult candidates with ⛽ and 🪡 in top result | integration | `cd canvas && npm test -- scorer.test.ts` | Wave 0 |

### Sampling Rate
- **Per task commit:** `cd canvas && npm test`
- **Per wave merge:** `cd canvas && npm test`
- **Phase gate:** All 6 requirements above pass before `/gsd:verify-work`

### Wave 0 Gaps
- [ ] `canvas/tests/resolver.test.ts` — covers WGHT-03, WGHT-04
- [ ] `canvas/tests/scorer.test.ts` — covers PARS-01, PARS-06, PARS-07, PARS-08
- [ ] Runtime dependency install: `cd canvas && npm install fastest-levenshtein fuse.js`

---

## Sources

### Primary (HIGH confidence)
- `canvas/src/weights/index.ts` — computeRawVector() signature, Float32Array shape, Steps 1-3 boundary
- `canvas/src/weights/types.ts` — WeightEntry, WeightScale, DialWeightTable interfaces
- `canvas/src/parser/keywords.ts` — KeywordEntry, DimensionId, collision_prone field
- `canvas/src/parser/types.ts` — ExerciseEntry with aliases array
- `canvas/src/types/scl.ts` — W enum positions, WEIGHT_VECTOR_LENGTH
- `middle-math/weights/interaction-rules.md` — 4-rule interaction algorithm, hard suppression definition (≤ -6), constraint hierarchy (Order > Color > Axis > Type)
- `middle-math/weights/weight-system-spec.md` — Step 4 description, worked example for ⛽🏛🪡🔵
- `.planning/STATE.md` — defaulted_dimensions decision, Phase 3 resolver design decisions

### Secondary (MEDIUM confidence)
- npm info fastest-levenshtein@1.0.16 — confirmed available, version verified
- npm info fuse.js@7.1.0 — confirmed available, version verified
- `.planning/phases/02-core-data/02-CONTEXT.md` — Phase 2 carry-forward decisions confirmed
- `canvas/tests/weight-tables.test.ts` — existing test patterns for asserting suppression rules

### Tertiary (LOW confidence)
- None — all critical claims verified against primary sources

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — both libraries confirmed on npm; all existing dependencies verified in canvas/package.json
- Architecture: HIGH — resolver algorithm derived directly from interaction-rules.md; pipeline shape derived from requirement descriptions + keyword data structure from Phase 2
- Pitfalls: HIGH — double-counting (verifiable against spec), defaulted_dimensions (STATE.md decision), fuse.js threshold (documented behavior), collision-prone keywords (flagged in existing keyword-dict.test.ts)

**Research date:** 2026-03-14
**Valid until:** 2026-04-14 (stable stack; both library APIs are stable)
