# Middle-Math Architecture — PPL± Computation Engine

The deterministic system between what PPL± is and what the user sees.

---

## Section 1 — The Weight System

Every one of the 61 SCL emojis carries a weight value on a -8 to +8 scale at every zip code address. The weight is derived from the SCL rules — not invented, not inferred. -8 means hard exclusion. 0 means neutral. +8 means defining: this IS the output's character.

The four dials in a zip code set primary weights at +8 for their own emojis, then cascade affinities (positive) and suppressions (negative) to all other emojis based on the rules in `scl-directory.md`. An Order that prohibits a block (e.g., 🖼 Restoration prohibiting 🌋 Gutter) becomes a -8 suppression on that block emoji. An Order that makes a block typical (e.g., ⛽ Strength and ▶️ Primer) becomes a +6 affinity.

When multiple dials have opinions about the same emoji, they combine according to the constraint hierarchy: Order > Color > Axis > Type. Hard suppressions from higher-priority dials cannot be overridden upward by lower-priority affinities. Soft weights sum and clamp to [-8, +8]. The result is a 61-value weight vector unique to every zip code address.

See `weights/` for the full specification and per-category weight declarations.

---

## Section 2 — The Procedural Exercise Engine

Master cards define exercise roles — movement pattern, block position, compound/isolation, bilateral/unilateral, equipment tier — not specific exercises. At render time, the engine queries the exercise library filtered by zip code constraints and user context, ranks by axis affinity weight and user history, and selects the top match. The same template produces different output for different users and different contexts.

The exercise library (~2,185 exercises across sections A–Q) is the source pool. Family trees group exercises by movement pattern with transfer ratios between parent and child exercises. When an exercise is unavailable (user toggle, equipment absence), the engine walks the family tree to find the nearest valid substitute.

This architecture separates the stable from the variable. The zip code and its rules are stable. The exercise that fills a given role shifts with context.

See `exercise-engine/` for the selection algorithm, family trees, and template specification.

---

## Section 3 — The User Context Layer

Three data structures define what a user brings to any given zip code.

The **exercise ledger** is the raw log: one row per exercise per logged workout, tagged with zip code context, prescribed vs. actual load, reps completed, RPE. It grows every session.

The **exercise profile** is derived from the ledger: estimated 1RM per exercise, trend (progressing, plateau, declining), order/color history (which contexts this user has logged this exercise in), last-seen date. The profile computes automatically from ledger data.

The **toggle system** is the filter layer: exercises, equipment tiers, movement patterns, and full Types can be toggled off. A user with no barbell toggles off equipment tier 3+. A user rehabbing a shoulder toggles off overhead pressing movements. Toggles never delete — they set the weight to -8 and exclude from selection until lifted.

See `user-context/` for schema specifications and computation formulas.

---

## Section 4 — Cross-Context Translation

A user who has squatted at ⛽🏛🍗🔵 (Strength, Basics, Legs, Structured) needs a prescription when they arrive at 🦋🔨🍗🔴 (Hypertrophy, Functional, Legs, Intense). Their logged numbers are at one address. The prescription is for another. The weight system provides the mathematical bridge.

The weight differential between two zip codes produces a translation factor. The Order weight ratio captures the load change (⛽ at 75–85% vs. 🦋 at 65–75%). The Color modifier captures format changes. The Axis character shift captures exercise selection changes that affect comparable difficulty. Apply the translation factor to the user's known performance, output a starting prescription at the new address.

The translation is imperfect by design. It is a starting point, not a guarantee. The ledger accumulates data at the new address and refines the profile from there.

See `user-context/cross-context-translation.md` for worked examples.

---

## Section 5 — The Rendering Layer

The 61-weight vector for a given zip code shapes more than exercise selection. It shapes what the user sees.

Color weights influence the UI palette: the primary Color emoji's palette dominates, secondary Color affinities blend in as accents. Order weights influence information density and pacing: ⛽ Strength renders tight and dense; 🖼 Restoration renders with whitespace and breath. Color weights influence tonal register: ⚫ Teaching carries a coaching voice; 🔴 Intense carries urgency. Typography treatment follows the same weight logic.

The same weight system that selects exercises also selects how the page is built. The zip code is a complete rendering instruction, not just a workout address.

See `rendering/` for derivation specifications. Note: rendering files are SEED-LEVEL — they specify the interface between middle-math and the Phase 4/5 design system.

---

## Section 6 — The Operis Bridge

The daily zip code from the rotation engine has a weight vector. That vector shapes the Operis editorial decisions.

Content type activation: each of the 109 content types has an Axis home weight (see `seeds/content-types-architecture.md`). The day's Axis weights determine which content types are amplified in that edition. High 🏛 Basics weight → fundamentals content prominent. High 🌹 Aesthetic weight → form analysis and visual content prominent.

Department count is governed by Order weight — already specified in the Operis weekly cadence (see `seeds/operis-architecture.md`). Tonal register is governed by Color weights, mapped to the tonal system in `scl-deep/publication-standard.md`. Cosmogram vocabulary: the day's zip code weight vector determines which deck's cosmogram language and imagery surface in the editorial.

The Operis is not randomly generated. Every editorial decision traces back to a weight. The publication is deterministic.

See `rendering/operis-weight-derivation.md` for the complete specification.

---

## Section 7 — Almanac Roots

The Hero's Almanac diagnostic system contributed foundational math to PPL±. The user-facing assessment framework — the 7 Dares, 224 questions, 224 Archetypes, the character creator — is archived. The underlying math is preserved as system-level primitives.

The octave scoring logic (1–8 scale per Dare) became the -8 to +8 bipolar weight scale. The 7-Order developmental ladder became the 7 PPL± Orders, governing workouts, editorial depth, and curriculum posture simultaneously. The 4-Lens perspective framework (Ladder, Lenses, Voices, Scales) became 4 of the 6 Axes. The 8-Voice tonal system became the 8 PPL± Colors.

The transformation was complete. The assessment framing came off. The math stayed. Character in the Almanac was built through a quiz. Character in PPL± is built through use — the exercise ledger grows, the profile sharpens, the system learns the user without asking.

See `roots/` for the preserved primitives and the translation document.

---

## Section 8 — The Numeric Zip Layer

Every PPL± emoji has a numeric position on its dial: Order 1-7, Axis 1-6, Type 1-5, Color 1-8. The 4-digit numeric zip code (e.g., `2123` for `⛽🏛🪡🔵`) is the system-layer addressing key used in URLs, database primary keys, API parameters, weight vector indices, and every context where emojis cannot operate.

The emoji is the display layer. The number is the computation layer. Conversion between them is a single array lookup in either direction. The numeric positions ARE the array indices for weight vector computation: `vector[order - 1] = 8` sets the Order primary weight; `vector[6 + axis] = 8` sets the Axis primary weight; and so on through all four dials.

The deck number is derived arithmetically: `deck = (order - 1) * 6 + axis`. Zip 2123 → Deck 7. Zip 7658 → Deck 42.

The zip_metadata table uses `CHAR(4)` as its primary key, with individual dial positions decomposed into indexed `SMALLINT` columns for filtered queries. All referencing tables (workout_logs, saved_workouts, zip_visits, room_threads, program_sequence) use `CHAR(4)` foreign keys. Referential integrity is enforced at the database level — a zip code that doesn't exist in zip_metadata cannot be referenced anywhere in the system.

See `seeds/numeric-zip-system.md` for the full notation standard. See `middle-math/schemas/zip-metadata-schema.md` for the table definition and population script.

---

## Relationship to Card Generation

Card generation (Phase 2) continues independently. Middle-math does not block it. The 1,600 remaining cards generate as fully-specified workout cards, named exercises and all. Middle-math's template format is an evolution of that system, not a replacement. When the procedural engine is built, fully-specified cards remain valid alongside template-format cards. The engine handles both.

The weight declarations in `weights/` are derived directly from rules already embedded in `scl-directory.md` and `CLAUDE.md`. Nothing in middle-math invents new rules — it makes existing rules computable.

---

🧮
