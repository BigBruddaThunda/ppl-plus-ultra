---
phase: 03-integration
plan: 02
subsystem: parser
tags: [typescript, vitest, nlp, fuzzy-matching, levenshtein, fuse.js, scoreText, tokenizer, parser]

# Dependency graph
requires:
  - phase: 03-integration
    plan: 01
    provides: resolveZip(), ParseResult interface, DimensionGroup type
  - phase: 02-core-data
    provides: dial-keywords.json, exercises.json, keyword DimensionId types

provides:
  - normalizeInput() and tokenize() producing unigrams + bigrams (tokenizer.ts)
  - expandToken() edit-distance typo correction via fastest-levenshtein (fuzzy.ts)
  - expandPhrase() exercise alias expansion via fuse.js (fuzzy.ts)
  - scoreText() full text-to-zip pipeline returning ranked ParseResult[] (scorer.ts)

affects: [04-parser, 05-renderer, 06-routing]

# Tech tracking
tech-stack:
  added:
    - fastest-levenshtein@1.0.16 — WASM-optimized edit distance (runtime dep)
    - fuse.js@7.1.0 — fuzzy phrase matching (runtime dep)
  patterns:
    - "Module-level singletons: ALL_TERMS corpus and Fuse index built once at import, not per-call"
    - "Two-pass scoring: bigrams first to set flags, then unigrams with collision suppression"
    - "Lower-position tiebreaker in argmax: Pull (pos 2) beats Legs (pos 3) on equal score"
    - "expandPhrase() limited to top 3 results to prevent fuzzy pollution from substring matches"
    - "EXERCISE_TYPE_MAP uses first-write-wins: preserves canonical scl_types for duplicate exercise names"

key-files:
  created:
    - canvas/src/parser/tokenizer.ts
    - canvas/src/parser/fuzzy.ts
    - canvas/src/parser/scorer.ts
    - canvas/tests/scorer.test.ts
  modified:
    - canvas/package.json

key-decisions:
  - "expandPhrase() top-3 cap: fuse.js 'leg press' returns 96 exercises; capping at 3 prevents Push type inflation from substring-matching 'press' exercises. Keyword bigrams are the authoritative source for well-known compound terms."
  - "EXERCISE_TYPE_MAP first-write-wins: exercises.json has 3 Romanian Deadlift (RDL) entries with scl_types [Pull+Plus], [Pull+Legs], [Legs]. First entry (Pull+Plus) is kept; this ensures RDL alias maps to Pull."
  - "Lower-position argmax tiebreaker: when two dimensions tie on score, lower position wins (Pull pos 2 beats Legs pos 3). This reflects the positional ordering of types in the SCL spec."
  - "fastest-levenshtein and fuse.js are runtime deps (not devDeps): scoreText() is called at runtime in the rendered experience layer, not only in tests."

patterns-established:
  - "Pipeline pattern: normalizeInput → tokenize → expandToken (per-token) → keyword dict lookup → expandPhrase (full input) → accumulate scores → argmax → resolveZip → confidence → ParseResult"
  - "Bigram priority: two-pass scoring ensures bigrams always fire before unigrams; collision_prone unigrams suppressed when a bigram already covered that dimension group"
  - "Confidence formula: sum(matched affinity scores) / (tokenCount * 8), clamped [0, 1]. Zero when no keywords matched."

requirements-completed: [PARS-06, PARS-07, PARS-08]

# Metrics
duration: 8min
completed: 2026-03-14
---

# Phase 03 Plan 02: Text-to-zip Scoring Pipeline Summary

**scoreText() deterministic NLP pipeline: edit-distance typo tolerance via fastest-levenshtein, multi-word alias expansion via fuse.js, bigram-over-unigram collision suppression, returning ranked ParseResult[] with confidence scores**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-14T17:12:49Z
- **Completed:** 2026-03-14T17:20:59Z
- **Tasks:** 2 (Task 1: deps install; Task 2: TDD RED + GREEN + 2 auto-fixes)
- **Files modified:** 5

## Accomplishments

- `tokenizer.ts`: normalizeInput() handles unicode NFD, punctuation strip, hyphen preservation; tokenize() produces unigrams + all adjacent bigrams
- `fuzzy.ts`: module-level ALL_TERMS corpus (2,005 keywords + 2,085 exercise names + 2,251 aliases, deduplicated) and Fuse index built once at import; expandToken() corrects typos within edit distance 2; expandPhrase() expands abbreviations via exercise alias search
- `scorer.ts`: full 14-stage scoreText() pipeline — bigrams override unigrams for same dimension group, collision_prone keywords deferred when bigram exists, argmax with lower-pos tiebreaker, resolveZip() integration, confidence formula, up to 5 ranked candidates
- 46 new TDD tests covering all 6 plan behaviors plus shape/confidence/sorting invariants
- Full suite: 6,877 tests passing (6,831 pre-existing + 46 new), zero regressions, zero TypeScript errors

## Task Commits

Each task was committed atomically:

1. **Task 1: Install fuzzy matching dependencies** — `81bb8bd9` (chore)
2. **Task 2 RED: Failing scorer tests** — `bc14d7be` (test)
3. **Task 2 GREEN: tokenizer, fuzzy, scorer implementation** — `77a2d95e` (feat)

## Files Created/Modified

- `canvas/src/parser/tokenizer.ts` — normalizeInput() and tokenize() producing unigrams + bigrams
- `canvas/src/parser/fuzzy.ts` — module-level ALL_TERMS + Fuse singletons; expandToken() and expandPhrase()
- `canvas/src/parser/scorer.ts` — scoreText() full 14-stage pipeline with ParseResult[] output
- `canvas/tests/scorer.test.ts` — 46 TDD tests for all pipeline behaviors
- `canvas/package.json` — fastest-levenshtein@1.0.16 and fuse.js@7.1.0 added as runtime deps

## Decisions Made

- **expandPhrase() top-3 cap**: fuse.js against "leg press" returns 96 exercises (many Push types from substring "press"). Capping at 3 prevents type-dimension pollution. Keyword bigrams are authoritative for compound terms in the dictionary.
- **EXERCISE_TYPE_MAP first-write-wins**: exercises.json has 3 duplicate "Romanian Deadlift (RDL)" entries with divergent scl_types. First entry (id 223, Pull+Plus from Section D) is canonical.
- **Lower-position argmax tiebreaker**: Pull (pos 2) and Legs (pos 3) tied at 15 points for "RDL". Lower position wins — this reflects the SCL spec ordering and ensures Pull > Legs when ambiguous.
- **Runtime deps**: both libraries used by scoreText() at runtime, not test-only.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] expandPhrase() top-3 cap to prevent Push inflation from "leg press"**
- **Found during:** Task 2 GREEN phase (first test run)
- **Issue:** fuse.js "leg press" search returns 96 exercises (Leg Press variants + many Push exercises via "press" substring). This added large Push type score, overriding the "leg press" bigram keyword match (dim 16, Legs). Test expected typePos=3 (Legs), got typePos=1 (Push).
- **Fix:** Limited `expandPhrase()` results to top 3 before type-scoring loop. The keyword dictionary already handles "leg press" as a bigram; phrase expansion is for abbreviations not in the keyword dict.
- **Files modified:** canvas/src/parser/scorer.ts
- **Verification:** "leg press" → typePos=3 (Legs). Test passes.
- **Committed in:** 77a2d95e (Task 2 GREEN commit)

**2. [Rule 1 - Bug] EXERCISE_TYPE_MAP first-write-wins to fix RDL → Pull routing**
- **Found during:** Task 2 GREEN phase (first test run after leg press fix)
- **Issue:** exercises.json has 3 "Romanian Deadlift (RDL)" entries with scl_types [Pull+Plus], [Pull+Legs], [Legs]. Map was last-write-wins so "RDL" mapped to ["Legs"]. All 3 phrase match iterations added Legs+5 each = 15. Pull from first entry was never reached.
- **Fix:** Changed EXERCISE_TYPE_MAP to first-write-wins (skip if name already exists). Now "RDL" maps to Pull+Plus. With 3 phrase match iterations: Pull=15, Plus=15 — tied, lower position wins (Pull pos 2 < Plus pos 4). typePos=2 (Pull).
- **Files modified:** canvas/src/parser/scorer.ts
- **Verification:** scoreText("RDL")[0].typePos === 2. Test passes.
- **Committed in:** 77a2d95e (Task 2 GREEN commit)

---

**Total deviations:** 2 auto-fixed (both Rule 1 - bugs discovered during GREEN phase)
**Impact on plan:** Both fixes address data-driven bugs not visible in spec design. Implementation is correct for the stated behaviors. No scope creep.

## Issues Encountered

- "gobbledygook nonsense" fuzzy expansion: expandToken() is called on these tokens and finds closest terms in ALL_TERMS within distance 2. The expanded tokens still don't match any keyword dict entries, so scores remain zero and confidence = 0. The zero-match path handles this correctly.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- scoreText() is the user-facing entry point for the parser — ready for consumption by routing, rendering, and the voice parser
- All 3 plan requirements satisfied: PARS-06 (edit-distance tolerance), PARS-07 (multi-word alias expansion), PARS-08 (collision-prone bigram priority)
- Phase 3 exit criterion still pending: full validation pass across all 1,680 zip codes needed before resolver is considered production-correct
- The pattern of limiting phrase expansion to top-N results should be documented for future phases if the exercise library grows

---
*Phase: 03-integration*
*Completed: 2026-03-14*
