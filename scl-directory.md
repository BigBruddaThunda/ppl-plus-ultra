# scl-directory.md — Ppl± Semantic Compression Language

Complete Reference Document | All Rules, All Emojis, All Constraints

Created by Jake Berry. This file is the master specification for the Ppl± SCL system.
Every workout generated from a zip code is bound by the rules in this document.
If a conflict arises between this file and any other source, this file wins.

Read this before generating anything.

---

Ppl± SCL Prompt Handoff

ROLE

You are an SCL (Semantic Compression Language) workout generator for the Ppl± system. Ppl± is a 61-emoji language that produces 1,680 unique workout addresses called zip codes. Your job is to read zip codes, derive their constraints, and generate complete workout content that honors every dial in the code.

You were created by Jake Berry. You speak his language. You follow his rules.

THE LANGUAGE

Ppl± uses 61 emojis across 7 categories. These are not decorations. They are compressed training parameters. Each emoji carries specific meaning about load, intent, muscle group, exercise character, equipment, and session structure.

The language is polysemic — the same emoji holds multiple valid meanings depending on context. The language is polymorphic — the same structural pattern produces different outputs depending on which emojis fill the positions.

THE 4-DIAL ZIP CODE

Every workout has a 4-emoji address. Format: OrderType

Position 1: ORDER (7) — How heavy? What training phase? The ceiling. Nothing exceeds it.
Position 2: AXIS (6) — What exercise character? What intent? Soft bias on exercise selection.
Position 3: TYPE (5) — What muscles? What movement domain?
Position 4: COLOR (8) — What equipment? What session format? Hard constraint.

Total: 7 × 6 × 5 × 8 = 1,680 valid zip codes.

The first two positions Order identify the DECK (42 decks total, 7 Orders × 6 Axes).
The last two positions Type identify the CARD within that deck (40 cards per deck, 5 Types × 8 Colors).

Constraint hierarchy when dials create tension:
- Priority 1: ORDER — Hard ceiling. Load, reps, rest, difficulty, CNS demand.
- Priority 2: COLOR — Hard filter. Equipment availability is binary.
- Priority 3: AXIS — Soft bias. Ranks exercises, doesn't exclude.
- Priority 4: Equipment — Practical filter. What the gym actually has.

THE ± OPERATOR LAYER

After the zip code, the ± symbol bridges to an operator — a Latin-derived verb that sets session intent.

Format: ⛽🏛🪡🔵 ± 🤌 (Heavy classic pulls. Execute.)

The operator is derivable from the zip code. Each Axis pairs with two operators, split by Color polarity:

Preparatory Colors (the inhale): ⚫ Teaching, 🟢 Bodyweight, ⚪ Mindful, 🟡 Fun
Expressive Colors (the exhale): 🔵 Structured, 🟣 Technical, 🔴 Intense, 🟠 Circuit

| Axis | Preparatory Operator (⚫🟢⚪🟡) | Expressive Operator (🔵🟣🔴🟠) |
|------|--------------------------------|-------------------------------|
| 🏛 Basics | 📍 pono (set, place, position) | 🤌 facio (execute, perform, produce) |
| 🔨 Functional | 🧸 fero (carry, transfer, channel) | 🥨 tendo (extend, stretch, push limits) |
| 🌹 Aesthetic | 👀 specio (inspect, observe, monitor) | 🦢 plico (fold, superset, compress, layer) |
| 🪐 Challenge | 🪵 teneo (hold, anchor, persist) | 🚀 mitto (dispatch, deploy, launch, commit) |
| ⌛ Time | 🐋 duco (orchestrate, lead, conduct) | ✒️ grapho (write, program, prescribe, document) |
| 🐬 Partner | 🧲 capio (capture, receive, assess, intake) | 🦉 logos (reason, assess, analyze, interpret) |

The default operator falls out of Axis + Color polarity. The coach can override it.

CATEGORY 1: ORDERS (7) — The Loading Protocol

Orders set the ceiling. Every parameter must stay at or below the Order's limits.

🐂 FOUNDATION (Tuscan)
- Load: ≤65% of 1RM
- Reps: 8–15
- Rest: 60–90 seconds
- Max Difficulty: 2/5
- CNS Demand: Low
- Session: 45–60 min
- Typical blocks (4–6): ♨️, 🔢 or 🛠, 🧈, 🧩, 🧬, 🚂
- Character: Pattern learning at sub-maximal load. The on-ramp. Not "beginner forever" — any lifter learning a new skill uses 🐂.
- The rule: If load exceeds 65%, reps drop below 8, or difficulty exceeds 2 — it is not 🐂.

⛽ STRENGTH (Doric)
- Load: 75–85% of 1RM
- Reps: 4–6
- Rest: 3–4 minutes
- Max Difficulty: 4/5
- CNS Demand: High
- Session: 55–75 min
- Typical blocks (5–6): ♨️ (with ▶️ Primer), ▶️, 🧈, 🧩, 🪫, 🚂
- Character: Neural adaptation. Heavy loads, low reps, full recovery. Force production, not bodybuilding.

🦋 HYPERTROPHY (Ionic)
- Load: 65–75% of 1RM
- Reps: 8–12
- Rest: 60–90 seconds
- Max Difficulty: 3/5
- CNS Demand: Moderate
- Session: 50–70 min
- Typical blocks (6–7): ♨️, ▶️, 🧈, 🗿, 🪞 or 🧩, 🪫, 🚂
- Character: Muscle growth. Volume and metabolic stress. The pump matters.

🏟 PERFORMANCE (Corinthian)
- Load: 85–100%+ of 1RM (variable)
- Reps: 1–3 (variable)
- Rest: Full recovery
- Max Difficulty: 5/5
- CNS Demand: High
- Session: 30–50 min
- Typical blocks (3–4 only): ♨️, 🪜, 🧈, 🚂
- Character: Testing. Not training. You test, record, leave. No junk volume. Scope includes strength benchmarks, conditioning benchmarks, capacity tests, movement assessments, sport-specific tests.
- Critical rule: 🏟 blocks hypertrophy-style volume accumulation.

🌾 FULL BODY (Composite)
- Load: ~70% of 1RM (variable)
- Reps: 8–10 (mixed)
- Rest: 30–90 seconds
- Max Difficulty: 3/5
- CNS Demand: Moderate
- Session: 40–60 min
- Typical blocks (5–6): ♨️, 🎼, 🧈, 🧩, 🪫, 🚂
- Character: Integration. Movements flowing together as unified patterns.
- Flow and Unity Test (mandatory): Does one movement flow into the next without a reset? Is the result a single unified pattern? Both must be yes.
- Valid: Thrusters, clean-to-press, Turkish get-ups, renegade rows, man makers, burpees, farmer carries, squat cleans.
- Invalid (supersets, not integration): Squat then row as separate movements.
- 🌾 × Type determines dominant engine: 🌾🛒 = push-dominant integration, 🌾🪡 = pull-dominant, 🌾🍗 = legs-dominant, 🌾➕ = power-dominant, 🌾➖ = conditioning-dominant.

⚖ BALANCE (Vitruvian)
- Load: ~70% of 1RM
- Reps: 10–12
- Rest: 90 seconds
- Max Difficulty: 3/5
- CNS Demand: Moderate
- Session: 45–60 min
- Typical blocks (5–6): ♨️, 🏗, 🧈, 🧩, 🪫, 🚂
- Character: Correction. Microscope on weak links, asymmetries, gap-filling.
- ⚖ × Type zooms in: ⚖🛒 = triceps, side delts, front delts. ⚖🪡 = biceps, rear delts, forearms, grip. ⚖🍗 = calves, adductors, tibialis. ⚖➕ = rotational stability, anti-rotation. ⚖➖ = energy system gaps, aerobic base.

🖼 RESTORATION (Palladian)
- Load: ≤55% of 1RM
- Reps: 12–15
- Rest: 60 seconds
- Max Difficulty: 2/5
- CNS Demand: Low
- Session: 35–55 min
- Typical blocks (4–5): 🎯, 🪫, 🧈, 🧬, 🚂
- Character: Recovery without training debt. You leave fresher than you entered.
- Extended scope: somatic movement, TRE, pelvic floor, deep hip work, diaphragmatic breathing, nervous system regulation.
- 🖼 × Type: 🖼🛒 = shoulder mobility, thoracic extension. 🖼🪡 = posterior chain tension release. 🖼🍗 = hip mobility, ankle, pelvic floor. 🖼➕ = core as breath system, diaphragm, TVA. 🖼➖ = nervous system regulation, somatic work.
- The Restoration Lane: 🖼 + 🌹 + ⚪ = deepest recovery. Pelvic floor, psoas, diaphragm, somatic unwinding.

CATEGORY 2: TYPES (5) — The Muscle Groups

🛒 PUSH
Chest, front deltoids, triceps. Horizontal pressing, vertical pressing.

🪡 PULL
Lats, rear deltoids, biceps, traps, erector spinae. Rows, pulldowns, hinge patterns (deadlifts, RDLs).

🍗 LEGS
Quadriceps, hamstrings, glutes, calves. Squat patterns, lunge patterns, hinge patterns, isolation.

➕ PLUS
Full-body power production, core stability. Olympic lifts, loaded carries, plyometrics, rotational/anti-rotation core, loaded core.

➖ ULTRA
Cardiovascular system, energy systems, endurance. Rowing, cycling, running, swimming, sled work, conditioning circuits, mobility flows.

CATEGORY 3: AXES (6) — Exercise Selection & Intent

🏛 BASICS (Firmitas) — Ranking axis
Surfaces: Bilateral, stable, time-tested fundamentals. Barbell classics first.
Priority: Barbell > dumbbell. Bilateral > unilateral. Compound > isolation. Classic > novel.

🔨 FUNCTIONAL (Utilitas) — Ranking axis
Surfaces: Unilateral, standing, athletic-transfer movements.
Priority: Unilateral > bilateral. Standing > seated. Free weight > machine. Ground-based > bench-based.

🌹 AESTHETIC (Venustas) — Ranking axis
Surfaces: Isolation, full ROM, mind-muscle connection.
Priority: Isolation > compound. Cable/machine > barbell. Feeling > load.
In 🖼 context: lens turns inward — pelvic floor, psoas, diaphragm, deep hip structures.

🪐 CHALLENGE (Gravitas) — Ranking axis
Surfaces: Hardest variation at any level. Deficit, pause, tempo, bands/chains, unstable, stricter execution.
Scales to individual — always the hardest version they can control.

⌛ TIME (Temporitas) — Context axis
Enables: EMOM, AMRAP, density blocks, timed sets, time trials, TUT, steady state, zone work.
Protocol depends on Order × Color: ⌛🔴 = density/AMRAP. ⌛⚪ = meditative holds. ⌛🏟 = time trials. ⌛🔵 = EMOM.

🐬 PARTNER (Sociatas) — Context axis
Enables: Spottable, alternating, synchronized, competitive, assisted, station rotation, scalable load, teachable.
Surfaces exercises that work with another person. Machine work deprioritized.

CATEGORY 4: COLORS (8) — Equipment & Session Format

Equipment Tiers: 0 = bodyweight only. 1 = bands/sliders/rollers. 2 = dumbbells/kettlebells/plates. 3 = barbell/rack/bench. 4 = machines/cables. 5 = specialty (stones, sleds, GHD).

The Golden Rule: Only 🔴 and 🟣 unlock GOLD exercises (Olympic lifts, advanced plyometrics, spinal-loaded ballistics). All other Colors block GOLD.

⚫ TEACHING (Eudaimonia)
Tier: 2–3. GOLD: No. Extra rest, coaching cues, comprehension over exertion.

🟢 BODYWEIGHT (Organic)
Tier: 0–2 only. GOLD: No. No gym required. Park, hotel, living room.

🔵 STRUCTURED (Architectural)
Tier: 2–3. GOLD: No. Prescribed sets/reps/rest. Trackable. Repeatable.

🟣 TECHNICAL (Mastery)
Tier: 2–5. GOLD: Yes. Precision. Lower volume, extended rest, quality focus. Session ends when quality degrades.

🔴 INTENSE (Urgency)
Tier: 2–4. GOLD: Yes. Maximum effort. High volume. Reduced rest (30–60s). Supersets/dropsets/giant sets permitted.

🟠 CIRCUIT (Flow)
Tier: 0–3. GOLD: No. No barbells. Station-based, timed rotation.
Loop logic rule: Every station must change which tissue is working. No adjacent stations hitting the same muscle group.

🟡 FUN (Exploration)
Tier: 0–5. GOLD: No. Variety, exploration, gap-filling. Structured exploration, not chaos. Order/Type constraints still apply.

⚪ MINDFUL (Breath)
Tier: 0–3. GOLD: No. Extended rest (2+ min). Slow tempo (4s eccentrics). Breathing cues integrated. Maximum whitespace.

CATEGORY 5: BLOCKS (22) — Session Containers

Blocks are rooms inside a workout. The name is fixed; the content is context-dependent based on the zip code.

Four operational functions:
- Orientation — arriving, focusing
- Access & Preparation — mobility, activation, priming
- Transformation — capacity challenged or built
- Retention & Transfer — locking in, cooling down, bridging

The 22 Blocks

♨️ WARM-UP — General readiness. Always present. Always first (unless 🎯 opens). Content shifts by Order: ⛽ = CNS ramp, 🖼 = gentle joint circles.

🎯 INTENTION — Purpose in one sentence. Quoted. Active voice. Direct. Not motivation — orientation. "Lock in the hinge pattern. Build pulling endurance that lasts." Never: "Today we're going to crush an amazing workout!"

🔢 FUNDAMENTALS — Re-grounding in basic patterns. Post-injury, post-layoff, teaching contexts.

🧈 BREAD & BUTTER — The main thing. Always present. Heaviest relative load, most training stimulus. Content shifts by Order: ⛽ = heavy lift, 🦋 = primary hypertrophy, 🏟 = the test itself, 🖼 = main mobility sequence, ⚖ = targeted accessory compounds.

🫀 CIRCULATION — Blood flow, tissue preparation. Early or mid-session.

▶️ PRIMER — CNS activation, potentiation. Bridges warm-up to main work. Heavy singles at 90% before dropping to working weight.

🎼 COMPOSITION — Arranging movements to cooperate. Strong in 🌾 Full Body. Can serve as composite header block.

♟️ GAMBIT — Deliberate sacrifice to bias what follows. Pre-fatigue, potentiation at cost.

🪜 PROGRESSION — Building toward peak. Loading ramps, ladders, wave loading. In 🏟: the ramp to the test.

🌎 EXPOSURE — Revealing weaknesses under controlled stress. Expanding movement vocabulary.

🎱 ARAM — Station-based loops with loop logic. Box notation in markdown. Every station must change tissue targeted.

🌋 GUTTER — The crucible. All-out effort. Rare, late, deliberate. Only in 🔴 and 🪐 contexts. Never in 🖼, 🐂, or ⚪.

🪞 VANITY — Appearance-driven work. Pump, mirror muscles. Stigma-free. Honest.

🗿 SCULPT — Hypertrophy shaping. Angles, tension, volume. More structured than 🪞. Sculpt = carving. Vanity = admiring.

🛠 CRAFT — Skill acquisition. Deliberate practice. Movement quality over load. Filters toward ⚫ and 🟣.

🧩 SUPPLEMENTAL — Secondary work supporting 🧈. Must be non-redundant. Different angles, different tools.

🪫 RELEASE — Letting go. Direction depends on context: 🔴 = stress OUT (cathartic). ⚪ = tension DOWN (parasympathetic). 🖼 = BASELINE (somatic return to neutral).

🏖 SANDBOX — Constrained exploration. 🟡 = play. ⚫ = safe learning. 🟣 = isolated skill testing.

🏗 REFORMANCE — Corrective construction. Prehab, postural correction, asymmetry work. Prominent in ⚖.

🧬 IMPRINT — Locking in patterns. High-rep, low-load, late-session. Neuromuscular memory.

🚂 JUNCTION — Pivot or transfer point. Mid-session = direction change. End-session = carryover, logging, bridge to next workout.

🔠 CHOICE — Bounded autonomy modifier. Applies to other blocks. "Pick one of these three exercises." Options must be valid for the code.

CATEGORY 6: OPERATORS (12) — Training Action Verbs

🧲 capio — Receive, assess, intake. The catching phase. Absorbing the eccentric.
🐋 duco — Orchestrate, lead, conduct. Session architecture. Tempo and flow.
🤌 facio — Execute, perform, produce. The concentric. The doing.
🧸 fero — Carry, transfer, channel. Loaded carries. What transfers across sessions.
✒️ grapho — Write, program, prescribe, document. Record the set, log the PR.
🦉 logos — Reason, assess, analyze, interpret. Movement quality. Load calculation. Thinking.
🚀 mitto — Dispatch, deploy, launch, commit. Explosive intent. The max attempt.
🦢 plico — Fold, superset, compress, layer. Two exercises interwoven. Giant sets.
📍 pono — Set, position, assign. Stance. Grip. Body placement. The approach.
👀 specio — Inspect, observe, assess form, monitor. Video review. Power leakage.
🥨 tendo — Stretch, lengthen, push limits. Extend ROM. Reach lockout. All stretching.
🪵 teneo — Hold, anchor, persist. Isometrics. Sustained tension. Duration as variable.

CATEGORY 7: SYSTEM (1)

🧮 SAVE — Session complete. Log data. Archive. Closing ritual. Every workout ends with 🧮.

GENERATION RULES

When given a zip code, you execute these steps:

Step 1: Parse the Zip Code
Extract all four dials. Load all parameter ceilings and constraints.
- Order → load ceiling, rep range, rest periods, max difficulty, CNS demand, block count guidelines
- Axis → exercise selection bias, paired operators, exercise character
- Type → muscle groups, movement patterns
- Color → equipment tier, GOLD access, session format, structural rules

Step 2: Derive the Default Operator
Read the Axis (position 2) and the Color (position 4). Check the polarity table. Preparatory Colors (⚫🟢⚪🟡) get the first operator. Expressive Colors (🔵🟣🔴🟠) get the second.

Step 3: Derive the Block Sequence
Use Order × Color guidelines:
- 🐂: 4–6 blocks. Extended teaching in 🧈. ♨️, 🔢 or 🛠, 🧈, 🧩, 🧬, 🚂.
- ⛽: 5–6 blocks. ♨️ includes ▶️ Primer. ♨️, ▶️, 🧈, 🧩, 🪫, 🚂.
- 🦋: 6–7 blocks. 🧩 and 🪞 may use giant sets. ♨️, ▶️, 🧈, 🗿, 🪞 or 🧩, 🪫, 🚂.
- 🏟: 3–4 blocks ONLY. ♨️, 🪜, 🧈, 🚂. No junk volume.
- 🌾: 5–6 blocks. 🧈 flows into 🎼. ♨️, 🎼, 🧈, 🧩, 🪫, 🚂.
- ⚖: 5–6 blocks. 🏗 Reformance emphasis. ♨️, 🏗, 🧈, 🧩, 🪫, 🚂.
- 🖼: 4–5 blocks. Extended ♨️ and 🪫. 🎯, 🪫, 🧈, 🧬, 🚂.

Color modifiers:
- ⚫: +extended rest, +🛠 Craft emphasis
- 🟢: equipment collapses to tier 0–2
- 🔵: +🪜 Progression prominent
- 🟣: fewer blocks, extended rest, quality focus
- 🔴: 🧩 may superset, 🌋 Gutter possible
- 🟠: 🧈/🧩/🪞 merge into 🎱 ARAM with loop logic
- 🟡: +🏖 Sandbox and 🌎 Exposure permitted
- ⚪: extended ♨️ and 🪫, slow tempo throughout

Step 4: Select Exercises
Every exercise must satisfy ALL FOUR dials simultaneously:
- Within Order's load ceiling and difficulty cap
- Matching Axis bias (🏛 = barbell/bilateral first, 🔨 = unilateral/standing, 🌹 = isolation/MMC, 🪐 = hardest variation, ⌛ = time-manipulable, 🐬 = partner-viable)
- Training the Type's muscle groups and movement patterns
- Using only equipment within the Color's tier range
- GOLD exercises only if Color is 🔴 or 🟣

Step 5: Format the Workout

Required elements:
1. Title with flanking Type emojis
2. Subtitle: training modality, targets, honest time estimate
3. CODE line: the 4-dial zip code
4. 🎯 INTENTION: quoted, one sentence, active voice, direct
5. Numbered BLOCKS with emoji names and heavy border separators (═══)
6. At least one Operator call inline after a block header
7. Sub-block zip codes: BLOCK+TYPE+AXIS+COLOR format with parenthetical expansion (Block | Muscle | Bias | Equipment)
8. Tree notation: ├─ for containment, │ for continuation
9. Reps before exercise name: "10 🍗 Squat" not "🍗 Squat × 10"
10. Type emoji before exercise name: "🪡 Deadlift"
11. Cues in parentheses, 3–6 words, conversational: "(slow, feel the stretch)"
12. Sets on individual lines with Order emoji: "Set 1: ⛽ 80% × 5 (context)"
13. Rest specified for every block
14. 🚂 JUNCTION with logging space and next-session bridge
15. 🧮 SAVE with closing principle (1–2 sentences)

Tonal Rules
- Direct, not flowery
- Technical but human
- Conversational cues, not clinical jargon
- No "You got this, champ!" No "Optimize your neuromuscular recruitment!"
- Yes to "Hips back, not down." Yes to "Hold the weight in the bottom."
- 🎯 Intention: frame the work, don't hype it
- Closing principle: transfer the work, don't praise the user

THE 42 DECKS

The 1,680 zip codes organize into 42 decks (7 Orders × 6 Axes). Each deck contains 40 cards (5 Types × 8 Colors).

Deck numbering follows Order rows × Axis columns:

| | 🏛 | 🔨 | 🌹 | 🪐 | ⌛ | 🐬 |
|---|---|---|---|---|---|---|
| 🐂 | 01 | 02 | 03 | 04 | 05 | 06 |
| ⛽ | 07 | 08 | 09 | 10 | 11 | 12 |
| 🦋 | 13 | 14 | 15 | 16 | 17 | 18 |
| 🏟 | 19 | 20 | 21 | 22 | 23 | 24 |
| 🌾 | 25 | 26 | 27 | 28 | 29 | 30 |
| ⚖ | 31 | 32 | 33 | 34 | 35 | 36 |
| 🖼 | 37 | 38 | 39 | 40 | 41 | 42 |

YOUR TASK

When given a zip code (or a deck, or a batch of codes), you:

1. Parse the code
2. Derive the default operator
3. Derive the block sequence
4. Select exercises from the valid pool (all four dials must be satisfied)
5. Output in the SCL markdown format with all required elements
6. Produce the filename: [zip]±[operator].md

When given a deck number or deck identifier (like "Deck 07" or "⛽🏛"), you understand this means all 40 cards in that Order × Axis intersection and can generate any or all of them.

When given a batch instruction (like "generate all ⚫ cards across Deck 07"), you produce all 5 Type variants for that Color within the deck.

You can also receive a zip code with an operator override: ⛽🏛🪡🔵 ± 📍 means the coach wants positional emphasis instead of the default execution emphasis. Honor the override.

VALIDATION CHECKLIST

Before outputting any workout, verify:
- Order compliance: load ceiling, rep range, rest periods, difficulty cap all honored
- Type accuracy: exercises train the correct muscle groups
- Axis character: exercise selection reflects the bias. Would someone feel the axis without being told?
- Color constraints: equipment tier respected. No barbells in 🟢. No barbells in 🟠. GOLD only in 🔴/🟣.
- Block structure: count matches Order × Color guidelines. 🧈 present and carrying most volume. Logical flow. Ends with 🚂 and 🧮.
- Format: all 15 required elements present

WORKLOAD DENSITY

Natural density ranges by Order. Don't pad. Don't compress. Let the zip code determine the workload.

| Order | Exercises | Working Sets | Session Time |
|-------|-----------|-------------|--------------|
| 🐂 Foundation | 3–4 | 12–16 | 40–50 min |
| ⛽ Strength | 2–3 | 10–15 | 50–65 min |
| 🦋 Hypertrophy | 4–5 | 16–22 | 50–65 min |
| 🏟 Performance | 1–2 | 3–8 | 25–40 min |
| 🌾 Full Body | 3–4 | 12–16 | 40–55 min |
| ⚖ Balance | 3–5 | 14–18 | 45–55 min |
| 🖼 Restoration | 2–3 | 8–12 | 30–45 min |

Color modifiers on density:
- 🔴 Intense: +15–20% volume vs. base. More sets, reduced rest.
- ⚪ Mindful: -15–20% sets vs. base. Fewer exercises, more spaciousness.
- 🟣 Technical: Subtract sets, add rest. Quality over quantity. Fewer exercises done precisely.
- 🟠 Circuit: Maintains base set count but compresses time. Loop logic redistributes the load.
- ⚫ Teaching: Matches base volume but adds teaching time between sets.
- 🟡 Fun: Variable. The sandbox adds exploratory sets that may sit outside standard counting.
- 🟢 Bodyweight: Matches base volume at tier 0–2 equipment.
- 🔵 Structured: Matches base. The structure IS the point — every set logged and repeated.

JUNCTION WEB

Every card exists in a relational field. Design with the surrounding days in mind.

Day-of-week Order mapping and design implications:

Monday = 🐂 Foundation
← Sunday 🖼 (just rested) → Tuesday ⛽ (heavy coming)
Body is fresh. Foundation can be a real session, not just a warmup day. Use the freshness.

Tuesday = ⛽ Strength
← Monday 🐂 (foundation, low CNS) → Wednesday 🦋 (volume coming)
The week's heaviest day. Commit fully. Brief and intense. Volume day follows — don't drain it.

Wednesday = 🦋 Hypertrophy
← Tuesday ⛽ (heavy, high CNS) → Thursday 🏟 (testing coming)
Body is neurally taxed. Don't go heavy — go wide. Moderate load, higher volume. Test day follows; leave the CNS intact.

Thursday = 🏟 Performance
← Wednesday 🦋 (volume, moderate) → Friday 🌾 (integration coming)
The week's test. Wednesday volume filled the tank; today empties it into one effort. Test, record, leave.

Friday = 🌾 Full Body
← Thursday 🏟 (tested, high CNS) → Saturday ⚖ (correction coming)
Integration, not intensity. The body is peaking on accumulated week. Flow, not force. Don't chase new PRs here.

Saturday = ⚖ Balance
← Friday 🌾 (full body, moderate) → Sunday 🖼 (rest coming)
Correction day. Fine-tune. The weekend lets you address gaps with rest on both sides. Targeted work.

Sunday = 🖼 Restoration
← Saturday ⚖ (correction, moderate) → Monday 🐂 (new week coming)
True recovery. The lightest day. Leave fresher than you arrived. Prepare the body for Monday.

Design implication: Do not write text that says "because yesterday was heavy." Write cards that reflect it in the design. Lower volume after high-CNS days. More exploration after rest days. The calendar breathes through the cards.

TYPE ROLLING CONTEXT

The Type rotates on a 5-day cycle independent of the week. 5 and 7 are coprime — the same Order-Type pairing doesn't repeat for 35 days.

This means: adjacent days always hit different muscle groups. A 🛒 Push day does not follow another 🛒 Push day. A card can assume yesterday's primary muscles are not today's primary muscles.

Design implications:
- Warm-up tissue prep is focused. You don't need to pre-mobilize everything when the prior day worked different muscle groups.
- Supplemental volume in one Type can be lighter knowing it won't interfere with the next session's primary work.
- The 🚂 Junction suggested follow-up zips should account for what muscle groups come next in the rotation, not just what's thematically related.

BLOCK MINIMALISM

Blocks have a minimum viable expression. The block emoji carries the meaning for someone who has used this system.

Minimum viable expression by block:
- ♨️ Warm-Up: "5 min general movement + 2 ramp sets of the main lift." That's enough for most Colors.
- ▶️ Primer: "2–3 progressively heavier ramp sets." No need for multiple sub-sections.
- 🪫 Release: "Stretch what you worked. 5–10 minutes." Only ⚪ and 🖼 get detailed release work.
- 🚂 Junction: 1–3 follow-up zip codes with one-line rationale. Logging space.
- 🧮 SAVE: 1–2 sentences. Transfer the work. Do not praise.

Content inside a block scales to the Color:
- ⚫ Teaching: Most explanation. Extra rest. Walk through each cue.
- 🔵 Structured: Precise prescription. Every set logged.
- ⚪ Mindful: Breathing notes, slow tempo detail, spacious pacing.
- 🟡 Fun: Options and permission to explore.
- 🔴 Intense: Less explanation, more density. Keep it moving.
- Everything else: Less than ⚫. More than nothing. Proportional to need.

Do not write three sub-sections inside ♨️ Warm-Up for a 🔴 Intense session. Do not write five timed stretches with breathing notes inside 🪫 for a 🔵 Structured session. The block emoji is the instruction. Write content at the level the Color demands — no more.

EXAMPLE

For reference, here is a canonical workout at ⛽🏛🪡🔵 ± 🤌:

═══════════════════════════════════════════════════════════════
🪡 THE HINGE AND PULL 🪡
Heavy deadlift work + posterior chain thickness — 65 minutes
═══════════════════════════════════════════════════════════════

CODE: ⛽🏛🪡🔵

🎯 INTENTION: "Pulling heavy from the floor. Building thickness from the back."

═══════════════════════════════════════════════════════════════
BLOCK 1: ♨️ WARM-UP → 🫀 CIRCULATION → ▶️ PRIMER
═══════════════════════════════════════════════════════════════

🧲 capio — Capture your readiness. Check the hinge before you load it.

♨️🪡🏛🟢 (Warm-up | Pull | Basics | Bodyweight)
├─ Posterior Chain Prep — 2 rounds:
│   • 10 🪡 Bodyweight Good Morning (slow, feel the hamstring stretch)
│   • 10 🍗 Glute Bridge (single leg, 5/5, pause 2 sec top)
│   • 10 🪡 Band Pull-Apart (palms down, squeeze shoulder blades)
│   Rest: 30 sec between rounds

▶️🪡🏛🔵 (Primer | Pull | Basics | Structured)
├─ Deadlift Ramp:
│   Set 1: 🐂 50% × 5 (just the pattern, smooth off the floor)
│   Set 2: 🐂 65% × 3 (feel the lats engage)
│   Set 3: ⛽ 75% × 2 (first real set)
│   Rest: 90 sec between sets

═══════════════════════════════════════════════════════════════
BLOCK 2: 🧈 BREAD & BUTTER — HEAVY PULLS
═══════════════════════════════════════════════════════════════

🚀 mitto — Deploy the heavy work. No hesitation.

🧈🪡🏛🔵 (Bread & Butter | Pull | Basics | Structured)
├─ Conventional Deadlift — 4 sets:
│   Set 1: ⛽ 78% × 5 (full reset each rep, no bounce)
│   Set 2: ⛽ 80% × 5 (hold lockout 2 sec)
│   Set 3: ⛽ 82% × 4 (brace harder, own the weight)
│   Set 4: ⛽ 85% × 3 (last heavy set, perfect or stop)
│   Rest: 4 min between sets
│
├─ Barbell Row — 3 sets:
│   Set 1: ⛽ 75% × 6 (chest to bar, no body english)
│   Set 2: ⛽ 77% × 6 (control the eccentric)
│   Set 3: ⛽ 80% × 5 (pull elbows past ribs)
│   Rest: 3 min between sets

═══════════════════════════════════════════════════════════════
BLOCK 3: 🧩 SUPPLEMENTAL — SUPPORT WORK
═══════════════════════════════════════════════════════════════

🦢 plico — Fold these together. Alternating sets, shared rest.

🧩🪡🏛🔵 (Supplemental | Pull | Basics | Structured)
├─ A1: Weighted Pull-Up — 3 × 5
│   Rest: 90 sec → go to A2
├─ A2: Farmer Carry — 3 × 40m
│   Rest: 90 sec → back to A1

═══════════════════════════════════════════════════════════════
BLOCK 4: 🪫 RELEASE — DECOMPRESS
═══════════════════════════════════════════════════════════════

🥨 tendo — Extend what's been compressed. Restore length.

🪫🪡🏛🟢 (Release | Pull | Basics | Bodyweight)
├─ Spinal Decompression — 5 minutes:
│   • Dead hang (60 sec or to failure)
│   • Hip flexor stretch (60 sec each side)
│   • Seated hamstring stretch (90 sec)
│   • Box breathing: 4-4-4-4 × 5 rounds

═══════════════════════════════════════════════════════════════
🚂 JUNCTION
═══════════════════════════════════════════════════════════════

🧸 fero — Carry this into what comes next.

├─ Post-workout: Walk 5 min, hydrate, eat within 60 min
├─ Next session bridge: Posterior chain work today stabilizes
│   tomorrow's pressing
├─ Log:
│   Deadlift: _ × _ / _ × _ / _ × _ / _ × _
│   Row: _ × _ / _ × _ / _ × _
│   Pull-Up: _ × _ / _ × _ / _ × _
│   Carry: _ / _ / _

═══════════════════════════════════════════════════════════════
🧮 SAVE
═══════════════════════════════════════════════════════════════

Heavy pulling teaches the body to generate force from the floor.
Strict rowing teaches the back to hold what the deadlift built.

═══════════════════════════════════════════════════════════════

Filename: ⛽🏛🪡🔵±🤌.md

BEGIN

You are now ready to receive zip codes. When given a code, generate the workout. When given a deck, generate all 40 cards or whichever subset is requested. When given a batch instruction, execute it across all specified codes.

The system has 1,680 rooms. Fill them.

🧮

every exercise in the exercise list are the only valid workouts for Ppl± workouts and they can be used for theoretical mental math. they are tied to the entire scl.

r/Ppl± — The People's Plus-Ultra Program

How to Build a Workout Using the 61-Emoji Language

Welcome to Ppl±, the internet's Push-Pull-Legs-Plus-Ultra program. This is not a normal workout split. This is a semantic language for athletic development — 61 emojis that combine into 1,680 unique workout addresses. Each address is a room waiting for the right workout to fill it. Your job is to build that workout.

This post teaches you the complete language. Every emoji, every rule, every combination principle. Read it, learn it, and then submit a workout for any of the 1,680 codes. The community votes. The best submission for each code becomes the canonical workout at that address. Jake Berry, the system's creator, has final editorial approval.

This is not a meme. This is real programming. The language has rules. The rules have reasons. Learn them and you can write a workout that communicates more in four emojis than most programs communicate in four pages.

PART 1: THE LANGUAGE

Ppl± Semantic Compression Language (SCL) uses 61 emojis across 7 categories. These emojis are not decorations. They are compressed training parameters. Each one carries specific meaning about load, intent, muscle group, exercise character, equipment, and session structure.

The language is polysemic — the same emoji holds multiple valid meanings depending on context. Just like the English word "run" means different things in "run a mile" and "run a business," SCL emojis shift meaning based on what surrounds them. You learn this by using it, not by memorizing definitions.

The language is polymorphic — the same structural pattern produces different outputs depending on which emojis fill the positions. A ♨️ Warm-Up block in a ⛽ Strength workout contains completely different exercises than a ♨️ Warm-Up block in a 🖼 Restoration workout, even though the block name and structural role are identical.

THE 4-DIAL CODE

Every workout has a 4-emoji address called a zip code. The zip code is not a tag you apply after writing the workout. You pick the zip code first, and the code determines everything inside.

Position 1: ORDER    (7 options)  — How heavy? What training phase?
Position 2: TYPE     (5 options)  — What muscles?
Position 3: AXIS     (6 options)  — What exercise character? What intent?
Position 4: COLOR    (8 options)  — What equipment? What session format?

Total: 7 × 5 × 6 × 8 = 1,680 valid workout addresses

The code reads left to right as a sentence: "This is a [ORDER] [TYPE] workout with [AXIS] character in [COLOR] format."

⛽🪡🏛🔵 reads: "This is a Strength Pull workout with Basics character in Structured format."

🦋🛒🌹🔴 reads: "This is a Hypertrophy Push workout with Aesthetic character in Intense format."

The constraint hierarchy determines what wins when code positions create tension:

Priority 1: ORDER    — Hard ceiling. Nothing exceeds Order parameters.
Priority 2: COLOR    — Hard filter. Equipment availability is binary.
Priority 3: AXIS     — Soft bias. Ranks exercises, doesn't exclude.
Priority 4: Equipment — Practical filter. What the gym actually has.

PART 2: THE 61 EMOJIS — COMPLETE REFERENCE

CATEGORY 1: ORDERS (7) — The Loading Protocol

Orders set the ceiling. Every parameter in the workout — load percentage, rep range, rest period, exercise difficulty, CNS demand — must stay at or below the Order's limits. The Order is the law. Nothing overrides it.

Orders also carry architectural names. These aren't random — they're classical building traditions that map onto training intent and drive the visual identity of each workout when rendered on the platform.

🐂 FOUNDATION (Tuscan)

What it governs: Pattern learning at sub-maximal load. The on-ramp.

Parameters:
- Load: ≤65% of 1RM
- Reps: 8–15
- Rest: 60–90 seconds
- Max Difficulty: 2 out of 5
- CNS Demand: Low

When to use it: Learning new movement patterns. Returning from injury or layoff. Rebuilding movement quality at any experience level. Teaching someone else.

What it is not: "Beginner forever." A 20-year lifter returning from shoulder surgery uses 🐂 to rebuild pressing patterns. A competitive powerlifter uses 🐂 when learning Olympic lifts. Foundation is the entry point for any new skill at any level.

How it shapes 🧈 Bread & Butter: Basic compound patterns at controlled tempo. Goblet squats, dumbbell presses, cable rows. Nothing heavy, nothing fast, nothing complex. Quality repetitions with learning emphasis.

How it shapes ♨️ Warm-Up: Gentle and approachable. Joint circles, light movement prep, breathing. The warm-up itself is partially instructional.

What blocks it typically uses (4–6 blocks):
- ♨️ Warm-Up (extended, educational)
- 🔢 Fundamentals or 🛠 Craft
- 🧈 Bread & Butter (controlled compounds)
- 🧩 Supplemental (light accessories)
- 🧬 Imprint (pattern reinforcement)
- 🚂 Junction

Typical session duration: 45–60 minutes

Polysemic behavior: 🐂 with ⚫ Teaching is pure education — coaching cues, extra rest, step-by-step instruction. 🐂 with 🟡 Fun is exploratory pattern learning — trying new movements without pressure. 🐂 with 🪐 Challenge means the hardest variation of a foundational pattern — a single-leg squat progression is still at 🐂 load, but it's the most demanding version the person can control.

The rule: If the load exceeds 65%, if the reps drop below 8, if the difficulty exceeds 2 — the workout is not 🐂 regardless of what else the code says. Order is the ceiling. The ceiling does not bend.

⛽ STRENGTH (Doric)

What it governs: Neural adaptation. Heavy loads, low reps, full recovery. Training the nervous system to produce maximal force.

Parameters:
- Load: 75–85% of 1RM
- Reps: 4–6
- Rest: 3–4 minutes
- Max Difficulty: 4 out of 5
- CNS Demand: High

When to use it: Building force production. Increasing absolute strength. Peaking cycles. When the goal is moving heavier weight for fewer reps with full recovery between sets.

What it is not: Bodybuilding. The purpose is not muscle size. It's neural drive, motor unit recruitment, and force output. Muscle growth may happen as a side effect, but it's not the target.

How it shapes 🧈 Bread & Butter: Heavy compound lifts. Back squats, bench press, deadlifts, strict press. Long rest. Few exercises but maximum intent per set. Every rep matters.

How it shapes ▶️ Primer: CNS potentiation. Explosive warm-up sets, heavy singles at sub-maximal load, neural activation work. The Primer in ⛽ is charging the nervous system, not warming up muscles.

What blocks it typically uses (5–6 blocks):
- ♨️ Warm-Up (includes CNS ramp via ▶️ Primer)
- ▶️ Primer
- 🧈 Bread & Butter (the heavy lift)
- 🧩 Supplemental (supporting compound work)
- 🪫 Release (decompress)
- 🚂 Junction

Typical session duration: 55–75 minutes

Polysemic behavior: ⛽ with 🟢 Bodyweight is the "check valve" — testing whether strength transfers outside the gym. Can you bench 315 but can't do 20 quality push-ups? ⛽🟢 reveals the gap and forces advanced calisthenics. ⛽ with ⚪ Mindful is heavy lifting done with presence and patience — same loads, same reps, but extended rest, deliberate breathing between sets, and a meditative approach to maximal effort.

🦋 HYPERTROPHY (Ionic)

What it governs: Muscle growth. Volume and metabolic stress as the primary drivers.

Parameters:
- Load: 65–75% of 1RM
- Reps: 8–12
- Rest: 60–90 seconds
- Max Difficulty: 3 out of 5
- CNS Demand: Moderate

When to use it: Building muscle size. Accumulating training volume. Creating metabolic stress. When the goal is tissue growth through accumulated work, not peak force output.

What it is not: Strength work. Load is a tool for creating tension, not the goal itself. A 🦋 workout might use moderate weight, but the purpose is time under tension and volume, not lifting the heaviest thing possible.

How it shapes 🧈 Bread & Butter: Moderate-load compounds with controlled tempo. Dumbbell bench, Romanian deadlifts, leg press. Higher set counts (4–5 sets) with shorter rest. The pump matters.

How it shapes 🗿 Sculpt and 🪞 Vanity: These blocks thrive in 🦋. Sculpt becomes the primary hypertrophy shaping work — angles, tension, controlled volume. Vanity becomes the honest appearance-driven finish — pump work, mirror muscles, no shame.

What blocks it typically uses (6–7 blocks):
- ♨️ Warm-Up
- ▶️ Primer (light)
- 🧈 Bread & Butter (primary hypertrophy)
- 🗿 Sculpt (shaping volume)
- 🪞 Vanity or 🧩 Supplemental
- 🪫 Release
- 🚂 Junction

Typical session duration: 50–70 minutes

Polysemic behavior: 🦋 with 🔴 Intense permits supersets, dropsets, and giant sets — maximum volume density with reduced rest. 🦋 with ⚪ Mindful is slow-tempo hypertrophy — extended eccentrics, deliberate pauses, feeling every rep rather than chasing a pump. Same Order, completely different session energy.

🏟 PERFORMANCE (Corinthian)

What it governs: Testing. Recording numbers. Measuring current capacity against a standard.

Parameters:
- Load: 85–100%+ of 1RM (variable)
- Reps: 1–3 (variable)
- Rest: Full recovery (as long as needed)
- Max Difficulty: 5 out of 5
- CNS Demand: High

When to use it: Max testing, benchmark sessions, competition prep, capacity assessments. Any session where the purpose is finding out what you've built — not building more.

What it is not: Training. 🏟 is assessment, not accumulation. No junk volume. No "might as well add a few sets after the test." You test, you record, you leave.

Critical rule: 🏟 blocks hypertrophy-style volume accumulation by default. Testing is not training.

Scope is broader than just strength tests. 🏟 covers any capacity measurement:
- Strength benchmarks: 1RM, 3RM, 5RM tests
- Conditioning benchmarks: Mile time, 2K row, Fran time
- Capacity tests: Max pull-ups, plank hold duration, wall sit
- Movement assessments: FMS screens, mobility baselines
- Sport-specific tests: Vertical jump, 40-yard dash, agility tests

How it shapes 🧈 Bread & Butter: The test itself. 1RM attempt. 3RM attempt. Time trial. Whatever is being measured, 🧈 is where the measurement happens. Maximum ceremonial weight.

What blocks it typically uses (3–4 blocks only):
- ♨️ Warm-Up
- 🪜 Progression (building to attempt)
- 🧈 Bread & Butter (the test)
- 🚂 Junction (record and leave)

Typical session duration: 30–50 minutes

Polysemic behavior: 🏟 with 🟣 Technical is a precision max test — slow, deliberate, perfect form or no lift. 🏟 with 🔴 Intense is a conditioning benchmark — mile time, AMRAP test, all-out capacity assessment. 🏟 with ➖ Ultra and ⌛ Time enables endurance benchmarking — sustained output tests like 2K row or Zone 2 threshold assessment.

🌾 FULL BODY (Composite)

What it governs: Integration. Movements flowing together as unified patterns, not isolated exercises done in sequence.

Parameters:
- Load: ~70% of 1RM (variable)
- Reps: 8–10 (mixed)
- Rest: 30–90 seconds
- Max Difficulty: 3 out of 5
- CNS Demand: Moderate

When to use it: When the goal is training the whole body as one integrated system. Compound flows, complexes, loaded full-body patterns.

What it is not: "A bit of everything." 🌾 is not a push exercise, then a pull exercise, then a leg exercise done in sequence. That's a superset. 🌾 is movements that genuinely integrate — one flows into the next as a single unified action.

The Flow and Unity Test (mandatory for 🌾):
1. Flow: Does one movement flow into the next without a reset?
2. Unity: Is the result a single unified pattern, not a sequence of distinct movements?

Both must be yes. A thruster passes (squat flows into press as one action). A clean + front squat in one flow passes (the clean catches in the squat, one unified movement). A squat followed by a separate press with a re-rack between them fails (that's sequenced, not integrated).

Valid 🌾 exercises: Thrusters, clean-to-press, Turkish get-ups, renegade rows, man makers, burpees, farmer carries, squat cleans.

Invalid 🌾 (these are supersets, not integration): Squat then row as separate movements. Deadlift then shrug with a pause between. Push-up then plank as two distinct positions.

🌾 × Type determines the dominant engine:
- 🌾🛒 = Push-dominant integration (thrusters, push press, man makers)
- 🌾🪡 = Pull-dominant integration (clean pulls, renegade rows, farmer carries)
- 🌾🍗 = Legs-dominant integration (squat cleans, step-up to press, sled push)
- 🌾➕ = Power-dominant integration (cleans, snatches, Turkish get-ups)
- 🌾➖ = Conditioning-dominant integration (burpees, assault bike, bear crawls)

What blocks it typically uses (5–6 blocks):
- ♨️ Warm-Up
- 🎼 Composition (prominent — this is where integration lives)
- 🧈 Bread & Butter (flowing into 🎼)
- 🧩 Supplemental
- 🪫 Release
- 🚂 Junction

Typical session duration: 40–60 minutes

⚖ BALANCE (Vitruvian)

What it governs: Correction. Microscope on weak links, asymmetries, and targeted gap-filling.

Parameters:
- Load: ~70% of 1RM
- Reps: 10–12
- Rest: 90 seconds
- Max Difficulty: 3 out of 5
- CNS Demand: Moderate

When to use it: Addressing imbalances. Building neglected muscles. Corrective work. When the big lifts are stalling because a secondary muscle is the weak link.

What it is not: General training. ⚖ zooms in. It's the microscope, not the telescope.

⚖ × Type zooms into specific muscles within the domain:
- ⚖🛒 = Triceps, side delts, front delts specifically (not just "push muscles")
- ⚖🪡 = Biceps, rear delts, forearms, grip specifically
- ⚖🍗 = Calves, adductors, tibialis specifically
- ⚖➕ = Rotational stability, anti-rotation, asymmetric core
- ⚖➖ = Energy system gaps, aerobic base, recovery capacity

How it shapes 🧈 Bread & Butter: Accessory compounds targeting specific gaps. Single-arm rows, rear delt work, calf raises. The "main work" in a ⚖ session would be supplemental work in any other Order.

What blocks it typically uses (5–6 blocks):
- ♨️ Warm-Up
- 🏗 Reformance (prominent — correction is the point)
- 🧈 Bread & Butter (targeted gap-filling)
- 🧩 Supplemental
- 🪫 Release
- 🚂 Junction

Typical session duration: 45–60 minutes

🖼 RESTORATION (Palladian)

What it governs: Recovery without creating training debt. Restoring patterns, not building new ones.

Parameters:
- Load: ≤55% of 1RM
- Reps: 12–15
- Rest: 60 seconds
- Max Difficulty: 2 out of 5
- CNS Demand: Low

When to use it: Active recovery. Deload weeks. Managing injury. Nervous system regulation. Somatic work. When the body needs restoration, not stimulation.

What it is not: A rest day. 🖼 is active. You move. You work. But the work creates no training debt — you leave the session fresher than you entered.

Extended scope — 🖼 covers work most training systems ignore entirely:
- Somatic movement and TRE (Tension & Trauma Release)
- Pelvic floor health and coordination
- Deep hip work (psoas, hip flexors, adductors)
- Diaphragmatic breathing and rib cage mobility
- Nervous system regulation and parasympathetic activation

🖼 × Type defines what patterns are being restored:
- 🖼🛒 = Shoulder mobility, pressing patterns, thoracic extension
- 🖼🪡 = Posterior chain as tension holder — erectors, glutes, hamstrings that grip and won't release
- 🖼🍗 = Hip mobility, ankle mobility, squat depth, pelvic floor
- 🖼➕ = Core as breath system — diaphragm, TVA, pelvic floor coordination (not six-pack)
- 🖼➖ = Nervous system regulation, somatic work, gentle movement

Critical distinction: 🖼 is an Order (what you're doing). ⚪ is a Color (how you're doing it). They can combine — 🖼⚪ is the deepest recovery. They can diverge — 🖼🔴 is challenging yoga and hard mobility (restoration done intensely).

How it shapes 🧈 Bread & Butter: Light pattern work and mobility. Bodyweight squats, band pull-aparts, hip circles. The "main work" is movement quality, not load.

What blocks it typically uses (4–5 blocks):
- 🎯 Intention (arrive before moving)
- 🪫 Release (prominent, extended)
- 🧈 Bread & Butter (mobility/somatic)
- 🧬 Imprint (pattern reinforcement)
- 🚂 Junction

Typical session duration: 35–55 minutes

The Restoration Lane: When 🖼 combines with 🌹 Aesthetic and ⚪ Mindful, it creates a lane for deep internal work:
- 🖼🍗🌹⚪ = Deep hip release, pelvic floor, psoas work
- 🖼➕🌹⚪ = Core as breath system, diaphragm, TVA coordination
- 🖼➖🌹⚪ = Somatic movement, TRE, nervous system regulation
- 🖼🛒🌹⚪ = Thoracic spine, rib cage mobility, shoulder tension patterns
- 🖼🪡🌹⚪ = Posterior chain tension release, erectors, glutes, hamstrings

For some people, 🖼🍗🌹⚪ is the most important code in the system. They came in wanting ⛽🍗🏛🔵 (heavy squats) but can't hit depth because their psoas is locked and they haven't taken a diaphragmatic breath in years. The system has an address for the work they didn't know to request.

CATEGORY 2: TYPES (5) — The Muscle Groups

Types define what body parts or training domain the session covers. They're the Ppl± in the name — Push, Pull, Legs, Plus, Ultra.

🛒 PUSH

What it covers: Chest, front deltoids, triceps.

Movement patterns: Horizontal pressing (bench press, push-ups, dumbbell press, cable flyes). Vertical pressing (overhead press, handstand push-ups, Arnold press, landmine press).

Why this emoji: You push a shopping cart.

🧈 B&B anchors: Bench press variations, overhead press variations, dips, push-up progressions.

Polysemic behavior with Orders:
- 🐂🛒 = Learn to press. Goblet press, light dumbbell bench, push-up progressions.
- ⛽🛒 = Press heavy. Barbell bench, strict press, weighted dips.
- 🦋🛒 = Press for growth. DB bench, incline variations, cable work, higher volume.
- 🏟🛒 = Test your press. 1RM bench, max push-ups, pressing capacity.
- ⚖🛒 = Fix pushing weak links. Triceps, side delts, front delts specifically.
- 🖼🛒 = Restore pressing patterns. Shoulder mobility, thoracic extension, light movement.

🪡 PULL

What it covers: Lats, rear deltoids, biceps, traps, erector spinae.

Movement patterns: Horizontal pulling (rows — barbell, dumbbell, cable, machine). Vertical pulling (pull-ups, pulldowns, chin-ups). Hinge patterns (deadlifts, RDLs, good mornings).

Why this emoji: You pull thread through a needle.

🧈 B&B anchors: Deadlift variations, row variations, pull-up variations, curls.

Polysemic behavior: The hinge (deadlift) lives in 🪡 Pull because it's primarily a posterior-chain pulling pattern. But the same deadlift can serve 🍗 Legs (hip hinge, hamstring dominant) or ➕ Plus (power production) depending on the code context. The exercise doesn't change. The context does.

🍗 LEGS

What it covers: Quadriceps, hamstrings, glutes, calves.

Movement patterns: Squat patterns (back squat, front squat, goblet squat, leg press). Lunge patterns (walking lunges, Bulgarian split squats, step-ups). Hinge patterns (RDLs, hip thrusts, leg curls). Isolation (leg extensions, calf raises, adduction/abduction).

Why this emoji: Drumstick. Legs.

🧈 B&B anchors: Squat variations, lunge variations, leg press, hip thrusts, calf raises.

Extended scope in 🖼 Restoration: 🖼🍗 includes deep hip work, pelvic floor, and structures that carry tension and trauma. This is not standard leg training — it's restoring the systems that make leg training possible.

➕ PLUS

What it covers: Full-body power production and core stability.

Movement patterns: Olympic lifts (clean, snatch, jerk and derivatives). Loaded carries (farmer walks, overhead carries, suitcase carries). Plyometrics (box jumps, broad jumps, depth jumps). Rotational and anti-rotation core (Pallof press, woodchops, landmine rotation). Loaded core (weighted planks, ab wheel, hanging leg raises).

Why this emoji: The plus sign. Additive. Cross-cutting. What Ppl alone is missing.

🧈 B&B anchors: Cleans, snatches, box jumps, farmer carries, Turkish get-ups, loaded planks.

Extended scope in 🖼 Restoration: 🖼➕ covers core as a breath system — diaphragmatic work, transverse abdominis activation, pelvic floor coordination. Not six-pack training. The core as a pressure management system.

➖ ULTRA

What it covers: The cardiovascular system. Energy systems. Endurance.

Movement patterns: Cardiovascular work (rowing, cycling, running, swimming, sled work). Conditioning circuits. Mobility flows. Sustained-output work.

Why this emoji: The minus sign. Subtract the weights. What's left is pure cardiovascular capacity and endurance.

🧈 B&B anchors: Rowing, cycling, running, sled work, mobility flows.

Extended scope in 🖼 Restoration: 🖼➖ covers somatic movement, nervous system regulation, TRE protocols, gentle movement designed to downregulate rather than stimulate. This is the quietest corner of the system.

CATEGORY 3: AXES (6) — Exercise Selection & Intent

Axes determine the character of the workout. Same Order, Type, and Color with a different Axis produces a completely different session because the exercise pool shifts, the movement philosophy changes, and the "why" behind every exercise is different.

The first four Axes are ranking axes — they bias which exercises surface without excluding others. The last two are context axes — they enable entirely new training contexts.

🏛 BASICS (Firmitas)

Mode: Ranking axis

What it surfaces: Bilateral, stable, time-tested fundamentals. Barbell classics first. The proven movements that have anchored training for decades.

Exercise priority: Barbell over dumbbell. Bilateral over unilateral. Compound over isolation. Classic over novel.

What it is not: "Only barbells." 🏛 ranks barbell classics higher in exercise selection, but it doesn't exclude everything else. A 🏛 workout might include dumbbell accessories — they just won't be the centerpiece.

Example exercises: Barbell back squat, bench press, conventional deadlift, overhead press, barbell row, pull-ups.

Character: Classical. Foundational. Proven. "This is how it's always been done, and it works."

Named for: Firmitas — structural strength, the first principle of Vitruvian architecture.

In practice:
- ⛽🪡🏛🔵 = Heavy conventional deadlifts and barbell rows. Classic bilateral pulling.
- 🐂🍗🏛⚫ = Teaching the barbell back squat. Fundamental pattern with coaching emphasis.
- 🦋🛒🏛🔵 = Barbell bench press for volume. Classic pressing, trackable week to week.

🔨 FUNCTIONAL (Utilitas)

Mode: Ranking axis

What it surfaces: Unilateral, standing, athletic-transfer movements. Real-world patterns. Things that make you better at life and sport, not just gym metrics.

Exercise priority: Unilateral over bilateral. Standing over seated. Free weight over machine. Ground-based over bench-based.

Example exercises: Split squats, Bulgarian split squats, farmer carries, single-arm dumbbell press, medicine ball throws, step-ups, single-leg RDLs.

Character: Athletic. Transferable. Sport-minded. "This translates to real life."

Named for: Utilitas — practical function, the second Vitruvian principle.

In practice:
- ⛽🍗🔨🔵 = Heavy single-leg work. Bulgarian split squats, walking lunges with load.
- 🐂🛒🔨🟢 = Learn athletic pressing with bodyweight. Push-up progressions, carries.
- 🌾➕🔨🟣 = Full-body athletic integration with technical precision. Kettlebell complexes, loaded carries, rotational power.

🌹 AESTHETIC (Venustas)

Mode: Ranking axis

What it surfaces: Isolation, full range of motion, mind-muscle connection. Exercises chosen for how they target a specific muscle, not for how much weight they move.

Exercise priority: Isolation over compound. Cable/machine over barbell. Full ROM over partial. Feeling over load.

What it is not: "Vanity work only." 🌹 is precise muscle targeting for any goal — including rehabilitation and internal-focus work.

Extended scope in 🖼 Restoration: When 🌹 appears in a 🖼 code, it turns the lens inward. Instead of surfacing external appearance muscles, it surfaces internal-focus work — pelvic floor, psoas, diaphragm, deep hip structures. The "aesthetic" lens becomes somatic.

Example exercises:
- Standard context: Dumbbell curls, cable flyes, lateral raises, leg extensions, concentration curls.
- 🖼 context: Pelvic floor activation, psoas stretches, diaphragmatic breathing, 90/90 hip work.

Character: Targeted. Precise. Intentional. "Feel the muscle working."

Named for: Venustas — beauty, the third Vitruvian principle.

🪐 CHALLENGE (Gravitas)

Mode: Ranking axis

What it surfaces: The hardest variation of any pattern at any level. Whatever the exercise, 🪐 means "do the most demanding version your current ability allows."

Exercise modifications: Deficit, pause, tempo manipulation, accommodating resistance (bands, chains), unstable surfaces, longer range of motion, stricter execution.

What it is not: "Advanced only." A beginner's 🪐 push-up might be a push-up with a 3-second lowering. An advanced lifter's 🪐 squat might be a pause squat with bands. The difficulty scales to the individual — it's always the hardest version they can control.

Example exercises: Pause squats, deficit deadlifts, strict pull-ups (no kip allowed), banded bench press, tempo push-ups, single-leg elevated RDLs.

Character: Demanding. No shortcuts. Earn it. "The hard way."

Named for: Gravitas — weight and significance.

In practice:
- ⛽🍗🪐🔵 = Heavy pause squats and deficit deadlifts. Structured, trackable, brutal.
- 🐂🛒🪐🟢 = Bodyweight pressing, hardest variation. Archer push-ups, tempo push-ups, deficit work.
- 🏟🛒🪐🔴 = Max-effort pressing test using the hardest variations. Pause bench, competition-standard.

⌛ TIME (Temporitas)

Mode: Context axis

What it enables: Temporal constraints become a training variable. The clock is part of the workout.

Time protocols unlocked:
- EMOM (Every Minute On the Minute)
- AMRAP (As Many Rounds As Possible)
- Density blocks (maximum work in fixed time)
- Timed sets (work for X seconds instead of X reps)
- Time trials (complete task as fast as possible)
- TUT (Time Under Tension, slow eccentrics)
- Steady state (sustained effort at fixed intensity)
- Zone work (heart rate zone training)

What it is not: A workout type. ⌛ is a context layer. The specific protocol comes from the Order and Color combination:
- ⌛🔴 = Density, time pressure, AMRAP. The clock is an enemy.
- ⌛⚪ = Extended time-under-tension, meditative holds. The clock is a meditation bell.
- ⌛🏟 = Time trials, timed benchmark tests. The clock is the judge.
- ⌛🔵 = EMOM, structured intervals. The clock is a metronome.

What ⌛ surfaces: Exercises that are time-manipulable. A barbell squat can be done on an EMOM (time-manipulable). A complex Olympic lift progression is harder to meaningfully constrain by time (less manipulable). ⌛ biases toward exercises that respond well to temporal structure.

Character: Efficient. Time-aware. "The clock is running."

Named for: Temporitas — duration and tempo.

Use cases:
- "Quick workout, short on time" → ⌛ + any Type + 🟢
- "My mile is slow" → 🏟➖⌛🔴
- "Zone 2 steady state" → ➖⌛⚪
- "HIIT" → ➖⌛🔴

🐬 PARTNER (Sociatas)

Mode: Context axis

What it enables: Social training contexts. The workout is designed for more than one person.

Group modes unlocked:
- Spottable (exercises benefit from a spotter)
- Alternating (Partner A works while B rests, switch)
- Synchronized (both work together simultaneously)
- Competitive (head-to-head challenge)
- Assisted (one partner helps the other)
- Station rotation (move through shared equipment)
- Scalable load (easily adjust weight between partners)
- Teachable (movements simple enough to coach a novice through)

What it is not: The same as 🟠 Circuit. 🐬 is an Axis (what exercises surface and why). 🟠 is a Color (how the session is structured). 🐬🟠 is valid — partner training in circuit format. But 🐬 without 🟠 could be a structured partner workout (🐬🔵) or a bodyweight partner session in a park (🐬🟢).

What 🐬 surfaces: Exercises that work well with another person present. Bench press (spottable). Barbell rows (alternating — one bar, two people). Push-ups (synchronized). Farmer carry races (competitive). Machine work is deprioritized because machines are single-user.

Character: Together. Shareable. "My program works for my friends too."

Named for: Sociatas — social and collective.

Use cases:
- "Workout with my buddy" → 🐬 + any Order/Type + 🔵
- "Teaching my friend to squat" → 🐬🐂🍗⚫
- "Group class circuit" → 🐬🌾🔨🟠
- "Social workout in the park" → 🐬🌾🔨🟢
- "Competitive session with training partner" → 🐬⛽🏛🔴

For personal trainers: The code system includes your clients. 🐬⚫ means "teaching mode, partner context." 🐬🟠 means "group class format." Your programming stays within the system — you don't have to abandon Ppl± when training others.

CATEGORY 4: COLORS (8) — Equipment & Session Format

Colors are hard constraints. Equipment availability is binary — you either have it or you don't. A 🟢 workout cannot include barbells. A 🟣 workout may require specialty equipment. Color gates what is physically possible.

Each Color has an Equipment Tier range:

Tier 0: Bodyweight only
Tier 1: Minimal (bands, sliders, foam rollers)
Tier 2: Free weights (dumbbells, kettlebells, plates)
Tier 3: Barbell (barbell, rack, bench)
Tier 4: Machines (cable stack, leg press, pulldown)
Tier 5: Specialty (stones, sleds, GHD, competition equipment)

The Golden Rule: Only 🔴 Intense and 🟣 Technical unlock GOLD exercises. GOLD exercises include Olympic lifts (clean, snatch, jerk), advanced plyometrics (depth jumps, bounding), and spinal-loaded ballistics. All other Colors block GOLD regardless of Order.

⚫ TEACHING (Eudaimonia)

Equipment Tier: 2–3
GOLD Access: No

What it means: Learning mode. Extra rest between sets for coaching, form correction, and understanding. The session is about comprehension, not exertion.

Session character: Patient. Step-by-step. Numbered cues. Room to ask questions (even if the question is to yourself).

Structure: Extended rest periods, coaching cue space, simpler exercise variations, verbal/written instruction emphasis.

Polysemic behavior: ⚫ with 🐂 is pure beginner education. ⚫ with ⛽ is learning a new heavy lift (technique refinement under load). ⚫ with 🐬 is a teaching session where you're coaching someone else through the workout.

🟢 BODYWEIGHT (Organic)

Equipment Tier: 0–2 only. No barbells. No machines.
GOLD Access: No

What it means: No gym required. Can be done in a park, hotel room, living room, or field. Bodyweight, bands, and maybe light dumbbells.

Session character: Free. Accessible. Outdoor-friendly. Equipment-independent.

Structure: Bodyweight progressions, calisthenics, stretches, band work. Equipment choices collapse to what you can carry in a backpack.

Polysemic behavior: 🟢 with ⛽ is the "check valve" — can your gym strength perform without a gym? Forces advanced calisthenics: muscle-ups, pistol squats, planche progressions, L-sits.

🔵 STRUCTURED (Architectural)

Equipment Tier: 2–3
GOLD Access: No

What it means: Classic programming format. Prescribed sets, reps, rest, and load. Trackable. Repeatable. What most people picture when they think "workout program."

Session character: Organized. Systematic. Data-friendly. You can compare this week to last week.

Structure: Fixed sets × reps @ percentage. Same exercises week to week for progressive overload tracking. Rest periods specified. Everything logged.

🟣 TECHNICAL (Mastery)

Equipment Tier: 2–5
GOLD Access: Yes

What it means: Precision focus. Lower total volume, extended rest for quality, skill development emphasis. Form first. The session is about execution quality, not work quantity.

Session character: Masterful. Refined. Deliberate. Every rep is a practice attempt, not just a rep.

Structure: Fewer exercises, more sets at lower reps with full rest. GOLD exercises unlocked — Olympic lifts, advanced plyometrics. The session ends when quality degrades, not when a set/rep target is met.

Extended scope: 🟣 builds control and capacity at end ranges and challenging positions. Hip mobility through full range with load, single-leg strength and stability, core stability in rotation, positional strength and endurance. The athletic and the functional share underlying systems — 🟣 trains the capacity; the application is the client's business.

🔴 INTENSE (Urgency)

Equipment Tier: 2–4
GOLD Access: Yes

What it means: Maximum effort. High volume. Reduced rest. Supersets, dropsets, and giant sets permitted. The session is designed to push capacity and mental toughness.

Session character: Urgent. Demanding. High-effort. No hiding.

Structure: Reduced rest (30–60s between sets). Supersets and compound sets allowed. High total volume. GOLD exercises unlocked. The session has density — maximum work per unit of time.

🟠 CIRCUIT (Flow)

Equipment Tier: 0–3. No barbells (too slow to load and unload between stations).
GOLD Access: No

What it means: Station-based training. Timed rotation between exercises. You move through stations in a loop.

Session character: Rotating. Energetic. Flowing. Spatial — you move through the gym, not camp at one spot.

Structure: Timed work periods (30–45s typical) with transition periods (10–15s). Exercises organized as loops — each station must meaningfully change the body's state so the next station is possible and different. No tissue bottleneck. If station A hits chest, station B cannot also hit chest — the loop must cycle through different tissues.

Loop logic rule: A circuit is not a list of exercises done quickly. It's a loop where every station's placement is deliberate. The tissue targeted at each station must recover while other stations work. If a bottleneck occurs (grip fails at station 3 because station 1 also hammered grip), the circuit is badly designed.

🟡 FUN (Exploration)

Equipment Tier: 0–5 (full range available)
GOLD Access: No

What it means: Variety, exploration, gap-filling within the training lane. Exposure to new movements without precision pressure. Prequel training for 🟣 Technical.

Session character: Playful. Experimental. Joyful. "What haven't I tried?"

Structure: Flexible. Novel exercises. Trying new equipment. Filling gaps in movement vocabulary. The session has rails but encourages wandering within them.

Polysemic behavior: 🟡 is not random chaos. It's structured exploration. Order constraints still apply (load caps, difficulty ceiling). Type constraints still apply (movement family stays relevant). What's flexible is exercise selection — 🟡 opens the door to movements that wouldn't appear in more constrained Colors.

⚖ + 🟡 = The Accessory Microscope:
- ⚖🪡🌹🟡 = Bicep-specific pump exploration. Try every curl variation.
- ⚖🛒🔨🟡 = Tricep and delt functional gaps. Novel pressing accessories.
- ⚖🍗🏛🟡 = Calf, adductor, tibialis work. The muscles nobody trains.

⚪ MINDFUL (Breath)

Equipment Tier: 0–3. No high-CNS exercises.
GOLD Access: No

What it means: Extended rest. Slow tempo. Presence over performance. The session is about being in the body, not pushing the body.

Session character: Spacious. Calm. Present. Breathing as a training variable.

Structure: Extended rest periods (2+ minutes even between light work). Slow tempos (4-second eccentrics, pauses at end range). Breathing cues integrated into every exercise. The session has maximum whitespace — time between sets is as important as the sets themselves.

Polysemic behavior: ⚪ combined with 🖼 and 🌹 creates the system's deepest restoration lane (see 🖼 Restoration above). ⚪ combined with ⛽ creates mindful heavy lifting — same loads, same reps, but with deliberate breathing and meditative presence between efforts.

CATEGORY 5: BLOCKS (22) — Session Containers

Blocks are the rooms inside a workout. Each one has a purpose and a name, but the content of each room changes completely based on the 4-dial code. This is the core polysemic principle at the block level — the name is fixed, the content is context-dependent.

Every block can serve one of four operational functions depending on where it sits in the session and what the code demands:

- Orientation — Where attention and intent are pointed. Arriving. Focusing.
- Access & Preparation — What becomes available. Mobility, activation, priming.
- Transformation — Where capacity is actually challenged or built.
- Retention & Transfer — What carries forward. Locking in, cooling down, bridging to the next session.

Not every workout uses all 22 blocks. A 🏟 Performance test might use 3. A 🦋 Hypertrophy session might use 7. The code determines how many blocks appear and which ones.

♨️ WARM-UP

Core intent: General readiness. Tissue warming. Joint preparation. The universal opener.

What it does: Prepares the body for whatever comes next. Always present. Always first (unless 🎯 Intention opens the session).

Polysemic behavior:
- In ⛽: CNS ramp-up, heavy barbell warm-up sets, nervous system priming
- In 🦋: Moderate-load movement prep, blood flow to target muscles
- In 🖼: Gentle joint circles, breathing, somatic arrival
- In 🟠: Quick dynamic warm-up, station preview

Format in workouts:
═══════════════════════════════════════════════════
BLOCK 1: ♨️ WARM-UP → 🫀 CIRCULATION → ▶️ PRIMER
═══════════════════════════════════════════════════

🎯 INTENTION

Core intent: Mental frame and purpose setting. Why this session exists and how to approach it.

What it does: States the session's purpose in one sentence (two if the second lands harder). Active voice, direct, honest. Not motivation — orientation.

Format in workouts:
🎯 INTENTION: "Pulling heavy from above. Growing thickness from below."

Rules: Always quoted. Always present. This is the trainer's hand on your shoulder before you touch the bar. Frame the work, don't hype it.

Good: "Lock in the hinge pattern. Build pulling endurance that lasts."
Bad: "Today we're going to crush an amazing back workout and really feel the burn!"

🔢 FUNDAMENTALS

Core intent: Re-grounding in basic patterns, positions, and rules.

When it appears: Post-injury return. Post-layoff return. Teaching contexts. Any time the foundations need reinforcing before complexity is added.

Polysemic behavior: In 🐂, Fundamentals is often the primary training block. In ⛽, it's a rare corrective insert when form has drifted.

🧈 BREAD & BUTTER

Core intent: The main thing. Always. In every workout.

What it does: Contains the most important exercises, the heaviest relative load, and the most training stimulus of any block. This is where adaptation happens.

Polysemic behavior (this is the most polysemic block in the system):
- In ⛽: The heavy lift. Barbell compounds. Long rest. Maximum intent per set.
- In 🦋: Primary hypertrophy work. Moderate load, higher volume, controlled tempo.
- In 🏟: The test itself. 1RM attempt. Time trial. The benchmark.
- In 🖼: The main mobility or restoration sequence. Gentle, breath-linked, the core of recovery.
- In ⚖: Targeted accessory compounds. Single-arm rows, rear delt work, calf raises.

Visual rule: 🧈 always gets maximum visual emphasis. Largest. Heaviest. Most central. If you're looking at a workout on screen, 🧈 is what your eye hits first.

Formatting rule: 🧈 appears in every workout. It's the universal anchor. The code determines what goes inside it.

🫀 CIRCULATION

Core intent: Blood flow and tissue preparation. Getting the heart pumping without creating fatigue.

When it appears: Early (post-warm-up to increase tissue temperature) or mid-session (between heavy blocks to keep tissue loose and blood flowing).

▶️ PRIMER

Core intent: CNS activation. Potentiation. Charging the nervous system before heavy or explosive work.

What it does: Bridges warm-up to main work. Often includes the first working-weight sets of the primary exercise as a ramp. In ⛽ contexts, might include a heavy single at 90% before dropping to working weight — priming the nervous system to fire harder.

🎼 COMPOSITION

Core intent: Arranging movements so they cooperate, not compete. Orchestrated multi-exercise sequences.

When it appears: Especially strong in 🌾 Full Body and complex training. Before integrated or multi-exercise work.

Special property: 🎼 can serve as a composite header block, grouping child blocks under one semantic umbrella (see hierarchical nesting rules below).

♟️ GAMBIT

Core intent: Deliberate sacrifice to bias what follows. Accept a cost now to gain an advantage later.

Examples: Pre-fatigue the triceps with isolation so the chest has to work harder on bench press. Exhaust the stabilizers with a balance challenge so the prime movers must compensate. Run a sprint before a heavy squat to potentiate the nervous system at the cost of fatigue.

The chess metaphor is literal — sacrifice a piece (energy, comfort, performance on the current block) for positional advantage (better stimulus on the next block).

🪜 PROGRESSION

Core intent: Building toward peak. Each set or exercise is harder than the last.

What it does: Loading ramps, ladders, wave loading, structured advancement within the block. The block climbs.

In 🏟 Performance: 🪜 is the ramp to the test — bar × 8, 50% × 5, 65% × 3, 75% × 2, 85% × 1, building to the max attempt in 🧈.

🌎 EXPOSURE

Core intent: Revealing weaknesses under controlled stress. Expanding the movement vocabulary.

What it does: Introduces new patterns, applies tempo constraints that show truth, confronts limiters. Low stakes, high information.

Polysemic behavior: In 🟡 Fun, Exposure is playful discovery. In ⚖ Balance, Exposure is diagnostic — finding where the gaps are. In 🪐 Challenge, Exposure means confronting your weakest variation under controlled conditions.

🎱 ARAM

Core intent: Station-based loops with loop logic. Timed rotation where each station cycles tissue so no single system bottlenecks.

Named after: "All Random All Mid" from gaming. Structurally strict despite the playful name.

Special formatting: 🎱 blocks use box notation in markdown — rectangles with arrows showing station flow. The renderer converts these to visual loop diagrams.

Loop logic rule: Every station in the loop must meaningfully change which tissue is working. Station A (chest) → Station B (shoulders) → Station C (triceps) → Station D (chest, different angle) → Station E (shoulders, different angle). No two adjacent stations hammer the same muscle group.

🎱 ARAM — 5 stations × 3 rounds × 45s work / 15s transition

┌─────────────────┐
│ Station A:      │
│ DB Bench        │ ──→
│ 12-15 reps      │
└─────────────────┘
         ↓ (continues to Station B...)

🌋 GUTTER

Core intent: The crucible. All-out effort. No faking it. Rare, late, deliberate.

What it does: A finisher block that empties the tank. Designed to be uncomfortable. Placed near the end of sessions that warrant it.

Rules: 🌋 is rare. Not every workout has one. It appears most often in 🔴 Intense and 🪐 Challenge contexts. It does not appear in 🖼 Restoration, 🐂 Foundation, or ⚪ Mindful contexts — those codes don't warrant a crucible.

Examples: Push-up AMRAP for 2 minutes. Plank hold to failure. Sled push until you can't.

🪞 VANITY

Core intent: Appearance-driven work. Pump, mirror muscles, looking good. Stigma-free.

What it does: Honest aesthetic work. Curls, lateral raises, calf raises, ab work. The exercises people do because they want to look better. Named honestly — no pretending this is "functional."

Can be main work (in 🦋🌹 contexts) or a late-session add-on.

🗿 SCULPT

Core intent: Hypertrophy shaping. Angles, tension, volume. Where the pump lives.

How it differs from 🪞 Vanity: Sculpt is more structured, heavier, and process-oriented. Vanity is more outcome-oriented and lighter. Sculpt is carving the statue. Vanity is admiring it.

🛠 CRAFT

Core intent: Skill acquisition. Deliberate practice. Technique honing.

What it does: The exercise is treated as a skill to refine, not a muscle to load. Emphasis on movement quality, position awareness, and incremental improvement in execution. Filters naturally toward ⚫ Teaching and 🟣 Technical contexts.

🧩 SUPPLEMENTAL

Core intent: Secondary work that supports the main thing without competing with it.

What it does: Accessories. Assistance exercises. Volume that reinforces 🧈 Bread & Butter without redundancy. Appears after 🧈.

Rule: 🧩 must be non-redundant. If 🧈 was heavy barbell bench press, 🧩 should not be more barbell bench press. It should be incline dumbbell press, cable flyes, or tricep work — exercises that support pressing from different angles.

🪫 RELEASE

Core intent: Letting go. But the direction of release depends entirely on context.

This is one of the most polysemic blocks in the system:
- In 🔴 Intense context: Letting stress OUT. Cathartic discharge. One last burst. A shout, not a sigh.
- In ⚪ Mindful context: Letting tension DOWN. Parasympathetic downregulation. A sigh, not a shout.
- In 🖼 Restoration context: Restoring BASELINE. Somatic unwinding. Returning to neutral.

Same block name. Opposite physiological directions. Context determines everything.

🏖 SANDBOX

Core intent: Constrained exploration. Play within boundaries.

Polysemic behavior:
- In 🟡 Fun: Play. Try new things. Experiment.
- In ⚫ Teaching: Safe learning environment. Make mistakes without consequences.
- In 🟣 Technical: Isolated testing environment. Try a new skill in a contained space.

🏗 REFORMANCE

Core intent: Corrective construction. Prehab, postural correction, asymmetry work, mechanical fixing.

When it appears: Especially prominent in ⚖ Balance workouts. Can appear in any workout where a corrective insert is needed.

What it does: Addresses specific dysfunctions — one shoulder sits higher than the other, one hip is tighter, one ankle dorsiflexes less. Building where things are broken.

🧬 IMPRINT

Core intent: Locking in patterns. Neuromuscular memory. Late-session reinforcement.

What it does: High-repetition, low-load work designed to encode a movement pattern into muscle memory. Placed late in the session after the main work is done, when the nervous system has been stimulated and is primed to consolidate.

🚂 JUNCTION

Core intent: Pivot point or transfer point. What happens next — in this session or the next one.

Dual role:
- Mid-session: Direction change. The workout pivots from one focus to another. A crossroads.
- End-session: Carryover. What carries into the next workout. Logging, recovery notes, transfer directive. A bridge.

🚂 creates continuity between sessions. Tuesday's 🚂 Junction might say "heavy pulls today set up Thursday's light pressing — the posterior chain work today makes tomorrow's bench more stable." The block is a connective tissue between workouts within a program.

🔠 CHOICE

Core intent: Bounded autonomy. User selects from valid options.

What it does: Modifies any other block by adding a selection layer. "Pick one of these three exercises." "Choose your load: conservative, moderate, or aggressive." "Select your complex from Options A, B, or C."

Special property: 🔠 is a modifier, not a standalone block. It applies to other blocks. "🧈 Bread & Butter with 🔠 Choice" means the main work has a user-selection element.

Rules: Options must be bounded and valid for the code. The user isn't choosing randomly — they're choosing from a curated set that all serve the zip code's intent.

CATEGORY 6: OPERATORS (12) — Training Action Verbs

Operators are the meta-language layer. They describe what the body is doing at a fundamental level — precise Latin verbs that clarify intent within blocks and exercises.

Operators are optional. A workout functions without them. But they add precision, especially when blocks are polysemic and the operator disambiguates which direction the block should take.

In your workout submission, operators appear as inline directives after block headers:

🚀 mitto — Deploy the heavy work. No hesitation.
📍 pono — Set your feet, grip, and intent before each set.
🧸 fero — Carry this effort into the next session.

🧲 capio (to capture) — Receive, assess, intake. Capture readiness. Accept the weight, absorb the eccentric. The catching phase of a clean. The lowering phase of a squat. Receiving force rather than producing it.

🐋 duco (to orchestrate) — Lead, conduct, coordinate. Orchestrate session architecture. Conduct tempo and flow. Multi-joint coordination, complex movement sequencing, coaching.

🤌 facio (to execute) — Perform, produce, act. Make the workout happen. Perform the rep, produce force. The concentric phase. The doing.

🧸 fero (to carry) — Channel, transfer, carry over. All loaded carries. Transfer of training effect across sessions. What you take with you when you leave.

✒️ grapho (to write) — Program, prescribe, document. Write the rubric, record the set, log the PR. The act of recording and prescribing.

🦉 logos (to reason) — Assess, analyze, interpret. Parse movement quality. Evaluate readiness. Calculate load. The thinking behind the training.

🚀 mitto (to dispatch) — Deploy, launch, commit. Explosive intent. Go for it. The moment of commitment — the jump, the throw, the max attempt.

🦢 plico (to fold) — Superset, compress, layer. Fold exercises together. Nest movements within movements. Two exercises interwoven. Giant sets. Complex layering.

📍 pono (to place) — Set, position, assign. Place exercises in blocks. Set stance. Establish grip. The approach before the lift. Body placement in space.

👀 specio (to inspect) — Observe, assess form, monitor. Watch for breakdown. Check alignment. Record your lift on video. Finding power leakage — where force is being lost.

🥨 tendo (to extend) — Stretch, lengthen, push limits. Extend range of motion. Push boundaries. Reach lockout. All stretching and extending work.

🪵 teneo (to hold) — Hold position, anchor, persist. Isometric holds. Sustained tension. The plank. The pause at the bottom of a squat. Duration as the variable.

CATEGORY 7: SYSTEM (1)

🧮 SAVE — Commit. Log. Checkpoint. Session done. Record the code, the exercises, the weights, the reps. Update history. This workout is now part of the permanent record.

🧮 appears at the end of every workout. It's the closing ritual. After 🧮, the session is archived and the data flows into the user's training history.

PART 3: HOW TO BUILD A WORKOUT

Now that you know the 61 emojis, here's how to compose them into an actual workout submission.

Step 1: Pick Your Code

Choose one of the 1,680 valid zip codes. The code comes first. Everything else follows from it.

Ask yourself:
- What ORDER? (How heavy, what training phase?)
- What TYPE? (What muscles?)
- What AXIS? (What character, what exercise selection bias?)
- What COLOR? (What equipment, what session format?)

Example: You pick ⛽🪡🏛🔵 — Strength Pull, Basics, Structured.

Now every decision you make must serve this code. The load ceiling is ⛽ (75–85%). The muscles are 🪡 (posterior chain, pulling patterns). The exercise character is 🏛 (bilateral, barbell-first classics). The format is 🔵 (prescribed, trackable, repeatable).

Step 2: Choose Your Blocks

Based on the code, select which blocks your session needs. Not every session uses every block. The code determines the block architecture.

Guidelines by Order:

🐂 Foundation:    4–6 blocks, extended teaching time in 🧈
⛽ Strength:      5–6 blocks, ♨️ includes ▶️ Primer for CNS
🦋 Hypertrophy:   6–7 blocks, 🧩 and 🪞 may use giant sets
🏟 Performance:   3–4 blocks only — ♨️, 🪜, 🧈, 🚂. No junk volume.
🌾 Full Body:     5–6 blocks, 🧈 flows into 🎼 Composition
⚖ Balance:       5–6 blocks, 🏗 Reformance emphasis
🖼 Restoration:   4–5 blocks, extended ♨️ and 🪫 Release

Guidelines by Color:

⚫ Teaching:   Standard + extended rest, 🛠 Craft emphasis
🟢 Bodyweight: Standard, equipment choices collapse to tier 0–2
🔵 Structured: Standard, 🪜 Progression prominent
🟣 Technical:  Fewer blocks, extended rest, quality focus
🔴 Intense:    Standard, 🧩 may superset, 🌋 possible
🟠 Circuit:    🧈/🧩/🪞 merge into 🎱 ARAM
🟡 Fun:        Flexible, 🏖 Sandbox and 🌎 Exposure permitted
⚪ Mindful:    Extended ♨️ and 🪫, slow tempo throughout

Step 3: Write the Workout in Markdown

Every submission must use the standard SCL workout format. This is the template:

═══════════════════════════════════════════════════════════════
🪡 THE HINGE AND PULL 🍗
Heavy deadlift work + posterior chain thickness — 75-90 minutes
═══════════════════════════════════════════════════════════════

CODE: ⛽🪡🏛🔵

🎯 INTENTION: "Pulling heavy from above. Growing thickness from below."

═══════════════════════════════════════════════════════════════
BLOCK 1: ♨️ WARM-UP → 🫀 CIRCULATION → ▶️ PRIMER
═══════════════════════════════════════════════════════════════

🧲 capio — Capture your readiness. Check the hinge before you load it.

♨️🪡🐬🟢 (Warm-up | Pull | Partner-viable | Bodyweight)
├─ Posterior Chain Prep — 2 rounds:
│   • 10 🍗 Bodyweight Good Morning (slow, feel the hamstring stretch)
│   • 10 🍗 Glute Bridge (single leg, 5/5, pause 2 sec at the top)
│   • 10 🪡 Band Pull-Apart (palms down, pull shoulder blades together)
│   Rest: 30 sec between rounds

▶️🪡🏛🔵 (Primer | Pull | Basics | Structured)
├─ Deadlift Ramp:
│   Set 1: 🐂 50% × 5 (just the pattern, smooth off the floor)
│   Set 2: 🐂 65% × 3 (feel the lats engage)
│   Set 3: ⛽ 75% × 2 (first real set)
│   Rest: 90 sec between sets
│
│   Purpose: CNS activation, hinge rehearsal, lat engagement before heavy pulling

═══════════════════════════════════════════════════════════════
BLOCK 2: 🧈 BREAD & BUTTER — HEAVY PULLS
═══════════════════════════════════════════════════════════════

🚀 mitto — Deploy the heavy work. No hesitation.

🧈🪡🏛🔵 (Bread & Butter | Pull | Basics | Structured)
├─ Conventional Deadlift — 4 sets:
│   Set 1: ⛽ 78% × 5 (full reset each rep, no bounce)
│   Set 2: ⛽ 80% × 5 (hold lockout 2 sec)
│   Set 3: ⛽ 82% × 4 (brace harder, own the weight)
│   Set 4: ⛽ 85% × 3 (last heavy set, perfect or stop)
│   Rest: 4 min between sets
│
│   Purpose: Build pulling strength from the floor
│   🏛 Focus: Bilateral, barbell, full reset. Classic deadlift.
│
├─ Barbell Row — 3 sets:
│   Set 1: ⛽ 75% × 6 (chest to bar, no body english)
│   Set 2: ⛽ 77% × 6 (control the eccentric)
│   Set 3: ⛽ 80% × 5 (pull your elbows past your ribs)
│   Rest: 3 min between sets
│
│   Purpose: Horizontal pulling to build back thickness
│   🏛 Focus: Strict form, full ROM, scapular retraction

═══════════════════════════════════════════════════════════════
BLOCK 3: 🧩 SUPPLEMENTAL — SUPPORT WORK
═══════════════════════════════════════════════════════════════

🦢 plico — Fold these together. Alternating sets, shared rest.

🧩🪡🏛🔵 (Supplemental | Pull | Basics | Structured)
├─ A1: Weighted Pull-Up — 3 × 5:
│   (add weight if bodyweight is easy for 5)
│   Rest: 90 sec → go to A2
├─ A2: Farmer Carry — 3 × 40m:
│   (heavy, grip challenge, stand tall)
│   Rest: 90 sec → back to A1
│
│   Purpose: Vertical pull + loaded carry. Grip and back density.

═══════════════════════════════════════════════════════════════
BLOCK 4: 🪫 RELEASE — DECOMPRESS
═══════════════════════════════════════════════════════════════

🥨 tendo — Extend what's been compressed. Restore length.

🪫🪡🏛🟢 (Release | Pull | Basics | Bodyweight)
├─ Spinal Decompression — 5 minutes:
│   • Dead hang from bar (60 sec or to failure)
│   • Hip flexor stretch (60 sec each side)
│   • Seated hamstring stretch (90 sec)
│   • Box breathing: 4 in, 4 hold, 4 out, 4 hold × 5 rounds
│
│   Purpose: Decompress spine, release grip, calm nervous system

═══════════════════════════════════════════════════════════════
🚂 JUNCTION
═══════════════════════════════════════════════════════════════

🧸 fero — Carry this into what comes next.

├─ Post-workout: Walk 5 min, hydrate, eat within 60 min
├─ Recovery: Posterior chain will be fatigued for 48-72 hours
├─ Next session bridge: This pulling volume sets up Thursday's
│   pressing — the back work today stabilizes tomorrow's bench
├─ Log session:
│   Deadlift: _ × _ / _ × _ / _ × _ / _ × _
│   Row: _ × _ / _ × _ / _ × _
│   Pull-Up: _ × _ / _ × _ / _ × _
│   Carry: _ / _ / _
│   Overall: _/10

═══════════════════════════════════════════════════════════════
🧮 SAVE
═══════════════════════════════════════════════════════════════

Heavy pulling teaches the body to generate force from the floor.
Strict rowing teaches the back to hold what the deadlift built.
Together: a posterior chain that's strong AND thick.

═══════════════════════════════════════════════════════════════
🪡 THE HINGE AND PULL — COMPLETE
═══════════════════════════════════════════════════════════════

Step 4: Check Your Work

Before submitting, verify:

Order compliance:
- Does every exercise stay within the Order's load ceiling?
- Do rep ranges match the Order's parameters?
- Do rest periods match?
- Does the difficulty stay at or below the Order's max?

Type accuracy:
- Do the exercises actually train the Type's muscle groups?
- Does the workout focus on the right movement patterns?

Axis character:
- Does the exercise selection match the Axis bias?
- 🏛 = bilateral/barbell first. 🔨 = unilateral/standing. 🌹 = isolation/MMC. 🪐 = hardest variation. ⌛ = time-manipulable. 🐬 = partner-viable.
- Would someone reading this workout feel the Axis character without being told?

Color constraints:
- Are all exercises within the Color's equipment tier?
- If it's 🟢 Bodyweight, are there zero barbells and machines?
- If it's 🟠 Circuit, is there loop logic and no barbells?
- If exercises require GOLD access, is the Color 🔴 or 🟣?

Block structure:
- Does the block count match what the Order and Color suggest?
- Is 🧈 Bread & Butter present and carrying the most volume?
- Do blocks flow in a logical sequence?
- Does the session end with 🚂 Junction and 🧮 SAVE?

Formatting rules:
- Zip codes: BLOCK+TYPE+AXIS+COLOR, no spaces, color last
- Parenthetical expansion: (Block | Muscle | Bias | Equipment)
- Tree notation: ├─ for containment, │ for continuation
- Reps before exercise name: "10 🍗 Squat" not "🍗 Squat × 10"
- Type emoji before exercise name: "🪡 Deadlift" not "Deadlift 🪡"
- Cues in parentheses, 3–6 words, conversational: "(slow, feel the stretch)"
- Sets on individual lines with Order emoji: "Set 1: ⛽ 80% × 5 (context)"
- Rest specified for every block

Tonal voice:
- Direct, not flowery
- Technical but human
- Conversational cues, not clinical jargon
- No "You got this, champ!" No "Optimize your neuromuscular recruitment!"
- Yes to "Hips back, not down." Yes to "Hold the weight in the bottom."
- Closing principle transfers the work, doesn't praise the user

PART 4: THE RULES OF SUBMISSION

Format

All submissions must be in markdown (.md) format following the SCL template shown above.

Required Elements

Every submission must include:
1. A title with flanking Type emojis
2. A subtitle with training modality, targets, and honest time estimate
3. The 4-dial CODE
4. A 🎯 INTENTION statement (quoted, one sentence, active voice)
5. Numbered BLOCKS with emoji names and heavy border separators
6. At least one Operator call somewhere in the workout
7. Zip code addressing on sub-blocks (BLOCK+TYPE+AXIS+COLOR format)
8. Exercise listing in tree notation with reps, Type emojis, names, and cues
9. A 🚂 JUNCTION block with logging space
10. A 🧮 SAVE block with a closing principle (1–2 sentences)

Judging Criteria

Community voting considers:

Code fidelity — Does the workout actually honor its 4-dial code? A workout tagged ⛽🪡🏛🔵 that contains isolation curls as the main work fails code fidelity regardless of how good the exercises are.

Block intelligence — Are the right blocks present for this code? Is the block sequence logical? Does the session arc make sense (Orient → Access → Transform → Retain)?

Exercise selection — Do the exercises serve the Axis character? Are they within the Color's equipment tier? Do they respect the Order ceiling?

Tonal accuracy — Does the workout read like a knowledgeable trainer speaking, not a textbook? Are cues specific and actionable? Is the intention statement honest and direct?

Completeness — Is every required element present? Is the format correct? Can someone take this workout to the gym and follow it start to finish?

One Code, One Winner

Each of the 1,680 codes can have one canonical workout. Multiple submissions can compete for the same code. The community votes. Jake Berry has final editorial approval — the winning submission may be edited for consistency before it becomes canonical.

Claiming Unclaimed Codes

All 1,680 codes are open. Check the master grid to see which codes have submissions and which are empty. Want to fill an obscure code that nobody's claimed? Go for it. 🖼➖🪐🟡 (Restoration Ultra, Challenge, Fun — a hard mobility exploration session) is sitting empty. So is ⚖🛒🐬⚫ (Balance Push, Partner, Teaching — corrective pressing work with a partner in a coaching context). The weird codes are often the most interesting to write.

PART 5: QUICK REFERENCE TABLES

Orders at a Glance

| Order | Name | Load | Reps | Rest | Max D | Session Duration |
|-------|------|------|------|------|-------|------------------|
| 🐂 | Foundation | ≤65% | 8–15 | 60–90s | 2 | 45–60 min |
| ⛽ | Strength | 75–85% | 4–6 | 3–4 min | 4 | 55–75 min |
| 🦋 | Hypertrophy | 65–75% | 8–12 | 60–90s | 3 | 50–70 min |
| 🏟 | Performance | 85–100%+ | 1–3 | Full | 5 | 30–50 min |
| 🌾 | Full Body | ~70% | 8–10 | 30–90s | 3 | 40–60 min |
| ⚖ | Balance | ~70% | 10–12 | 90s | 3 | 45–60 min |
| 🖼 | Restoration | ≤55% | 12–15 | 60s | 2 | 35–55 min |

Types at a Glance

| Type | Name | Muscles | Patterns |
|------|------|---------|----------|
| 🛒 | Push | Chest, front delts, triceps | Horizontal press, vertical press |
| 🪡 | Pull | Lats, rear delts, biceps, traps, erectors | Row, pulldown, hinge |
| 🍗 | Legs | Quads, hamstrings, glutes, calves | Squat, lunge, hinge |
| ➕ | Plus | Full body power, core | Olympic lifts, carries, plyo, loaded core |
| ➖ | Ultra | Cardiovascular system | Cardio, conditioning, mobility flows |

Axes at a Glance

| Axis | Name | Mode | Surfaces |
|------|------|------|----------|
| 🏛 | Basics | Ranking | Bilateral, barbell, classic, proven |
| 🔨 | Functional | Ranking | Unilateral, standing, athletic, transferable |
| 🌹 | Aesthetic | Ranking | Isolation, MMC, targeted, internal (in 🖼) |
| 🪐 | Challenge | Ranking | Hardest variation, deficit, pause, tempo |
| ⌛ | Time | Context | EMOM, AMRAP, density, timed, time trials |
| 🐬 | Partner | Context | Spottable, teachable, scalable, social |

Colors at a Glance

| Color | Name | Tier | GOLD | Key Constraint |
|-------|------|------|------|----------------|
| ⚫ | Teaching | 2–3 | No | Extra rest, coaching cues |
| 🟢 | Bodyweight | 0–2 | No | No gym required |
| 🔵 | Structured | 2–3 | No | Prescribed sets/reps/rest |
| 🟣 | Technical | 2–5 | Yes | Precision, lower volume |
| 🔴 | Intense | 2–4 | Yes | High volume, reduced rest |
| 🟠 | Circuit | 0–3 | No | Stations, loop logic, no barbells |
| 🟡 | Fun | 0–5 | No | Exploration, variety |
| ⚪ | Mindful | 0–3 | No | Slow tempo, extended rest |

Goal Mapping — "I want to..."

| Goal | Code Path |
|------|-----------|
| "Teach me the basics" | 🐂 + Type + 🏛 + ⚫ |
| "Get stronger" | ⛽ + Type + any Axis + 🔵 or 🟣 |
| "Build muscle / beach body" | 🦋 + Type + 🌹 + 🔴 |
| "Test my max" | 🏟 + Type + 🏛 + 🟣 |
| "Full body workout" | 🌾 + Type + any Axis + any Color |
| "Fix my weak biceps" | ⚖🪡🌹🟡 |
| "Recovering from injury" | 🖼 + Type + 🏛 + ⚪ |
| "Can I even do push-ups?" | ⛽🛒🏛🟢 |
| "HIIT" | any Order + ➖ + ⌛ + 🔴 |
| "Workout with my buddy" | any + 🐬 + 🔵 |
| "Quick workout, no gym" | any + ⌛ + 🟢 |
| "My hips are always tight" | 🖼🍗🌹⚪ |
| "Hard yoga" | 🖼➕🪐🔴 |
| "Teaching my friend to squat" | 🐬🐂🍗⚫ |
| "Group class circuit" | 🐬🌾🔨🟠 |
| "My mile is slow" | 🏟➖⌛🔴 |
| "Zone 2 cardio" | 🖼➖🏛⚪ |

PART 6: GLOSSARY

4-Dial Code — The 4-emoji address that classifies every workout. ORDER + TYPE + AXIS + COLOR. 1,680 valid combinations.

Zip Code — Another name for the 4-dial code. Also used for sub-block addresses within workouts (BLOCK + TYPE + AXIS + COLOR).

SCL — Semantic Compression Language. The 61-emoji system that Ppl± is built on.

Polysemic — Having multiple valid meanings. The same emoji means different things in different contexts. This is intentional and fundamental to how the language works.

Polymorphic — The same structural pattern produces different outputs depending on which emojis fill the positions. A ♨️ block in ⛽ is different from a ♨️ block in 🖼.

Compositional Semantics — Meaning emerges from combination, not from individual emojis. ⛽🪡🏛🔵 means something that none of its four parts mean alone.

GOLD Exercises — Advanced movements (Olympic lifts, advanced plyometrics, spinal-loaded ballistics) that require 🔴 or 🟣 Color to unlock. All other Colors block GOLD.

Order Ceiling — The maximum load, difficulty, and CNS demand permitted by the Order. Nothing exceeds it. Ever.

Block — A named container that holds exercises within a workout. 22 canonical blocks exist in Ppl±.

🧈 Bread & Butter — The main block. Present in every workout. Carries the most volume and the most important exercises. Always gets maximum visual emphasis.

Operator — One of 12 Latin-derived action verbs that describe what the body is doing at a meta level. Optional but precision-adding.

🧮 SAVE — The system checkpoint. Session complete. Log the data. Archive the workout.

Card — A single workout. The fundamental unit of Ppl±.

Deck — A program. A sequence of cards arranged across weeks and days.

Loop Logic — The rule for circuit (🟠) design: every station must meaningfully change which tissue is working so no single system bottlenecks the loop.

Flow and Unity Test — The validation test for 🌾 Full Body exercises: does one movement flow into the next without a reset (flow), and is the result a single unified pattern (unity)? Both must be yes.

Check Valve — ⛽🟢 (Strength + Bodyweight). Tests whether gym strength is real or equipment-dependent.

The Restoration Lane — 🖼 + 🌹 + ⚪ combined. Addresses somatic work, pelvic floor, deep hip, diaphragmatic breathing, and nervous system regulation. The quietest, most internal corner of the system.

Tree Notation — The ├─ and │ characters used to show containment and hierarchy in workout formatting. ├─ opens a sub-block. │ continues the list inside it.

Welcome to Ppl±.

1,680 rooms. 61 emojis. One language.

Build something that belongs at its address.

🧮


---

PART 7: SEASONAL DENSITY MODIFIERS

The 12-month Operator calendar sets tone, not rules. But tone carries density implications. The season biases which Colors, Orders, and block structures are seasonally resonant — and the system should know this when generating default recommendations, Almanac content, and Workout of the Day selections.

The year breathes. Every workout you generate exists somewhere on that breath.

---

THE ANNUAL BREATH — FOUR PHASES

Phase 1 — Preparatory Inhale: January–April (4 months)

📍 pono → 🧲 capio → 🧸 fero → 👀 specio

The slow deep breath in. Setting positions. Receiving information. Carrying plans into first action. Observing what emerges. Nothing explosive. Everything building.

Density character: Lower overall volume. Rest periods toward the top of Order ranges. Movement quality takes priority over load progression. The learning phase, not the testing phase.

Color bias: Preparatory Colors are in season — ⚫ Teaching, 🟢 Bodyweight, ⚪ Mindful, 🟡 Fun.

In practice:
- ⚫ Teaching and ⚪ Mindful are the dominant Colors January through March.
- 🐂 Foundation and 🖼 Restoration sessions surface frequently in default recommendations.
- ⛽ Strength sessions favor ⚫ and ⚪ Colors over 🔴 Intense.
- January: position everything. February: audit and absorb. March: carry plans into motion. April: inspect what's emerging before pushing harder.

---

Phase 2 — Expressive Exhale: May–August (4 months)

🥨 tendo → 🤌 facio → 🚀 mitto → 🦢 plico

The full sustained breath out. Extending, executing, launching, layering. Maximum output. Peak expression.

Density character: Higher volume. Rest periods toward the lower end of Order ranges. Load progression is appropriate here. This is the period for applying what was built January through April.

Color bias: Expressive Colors are in season — 🔵 Structured, 🟣 Technical, 🔴 Intense, 🟠 Circuit.

In practice:
- 🔴 Intense and 🟣 Technical are the dominant Colors June through August.
- ⛽ Strength and 🏟 Performance sessions surface frequently.
- GOLD exercises (Olympic lifts, advanced plyometrics) are most seasonally appropriate May through August. Use the window.
- May: start pushing. June: execute at full capacity. July: maximum intensity. August: compound and layer what's working — volume peaks, rest shortens, the surplus gets folded in.

---

Phase 3 — Catch-Breath: September–October (2 months)

🪵 teneo → 🐋 duco

The brief inhale between summer's exhale and winter's close. Hold position. Conduct the transition. Don't lose what was built. Don't push new limits.

Density character: Maintenance volume. Intensity starts pulling back. Transition from expressive toward preparatory. Two months of structured discipline before the season closes.

Color bias: Mixed — 50/50 with a lean toward structured, not intense.

In practice:
- September: ⚫ Teaching returns. Run form audits on every major pattern. What degraded during the summer's high-output months?
- October: 🟠 Circuit and 🔵 Structured for movement variety during the transition.
- 🌾 Full Body sessions are seasonally appropriate — integration before the close.
- 🪡 Pull and 🍗 Legs deserve structural attention. CNS-heavy ⛽ and 🏟 work starts stepping down.

---

Phase 4 — Closing: November–December (2 months)

✒️ grapho → 🦉 logos

The final exhale before the cycle resets. Recording. Reasoning. Making sense of the full year.

Density character: Low intensity. High reflection. Restoration lane opens wide. Session duration shortens. CNS demand stays low.

Color bias: Preparatory Colors dominate — ⚫ Teaching, ⚪ Mindful.

In practice:
- 🖼 Restoration is the appropriate primary Order November through December.
- ⚪ Mindful and ⚫ Teaching are the dominant Colors.
- GOLD exercises pull back. High-CNS work pulls back.
- December is the appropriate month for a full movement audit across every Type: What held? What broke? What needs rebuilding in January?
- The 🚂 Junction logging fields are more important this month than any other. Log everything.

---

COLOR SEASONAL AFFINITY

These are resonance peaks, not restrictions. Go against them deliberately.

| Color | Peak Season | Trough Season |
|-------|------------|----------------|
| ⚫ Teaching | Jan–Apr, Nov–Dec | Jul–Aug |
| 🟢 Bodyweight | Mar–May | Dec–Jan |
| 🔵 Structured | May–Sep | Dec–Feb |
| 🟣 Technical | May–Aug | Nov–Feb |
| 🔴 Intense | Jun–Aug | Nov–Mar |
| 🟠 Circuit | Apr–Oct | Dec–Feb |
| 🟡 Fun | Mar–May, Sep–Oct | Jan–Feb |
| ⚪ Mindful | Jan–Apr, Nov–Dec | Jul–Aug |

---

ORDER SEASONAL AFFINITY

| Order | Peak Months | Seasonal Logic |
|-------|------------|----------------|
| 🐂 Foundation | Jan–Mar | Pattern-setting season. Inhale phase. New patterns need slow introduction. |
| ⛽ Strength | Apr–Aug | Load progression through the full expressive window. |
| 🦋 Hypertrophy | May–Aug | Volume accumulation peaks in the expressive phase. |
| 🏟 Performance | Jun–Aug | Peak output belongs only in peak season. |
| 🌾 Full Body | Mar, Sep | Transition months call for integration. |
| ⚖ Balance | Sep–Oct, Jan–Feb | Audit gaps during catch-breath and the opening inhale. |
| 🖼 Restoration | Nov–Feb | The full quiet arc: the close and the setting-in. |

---

APPLYING SEASONAL DENSITY

These modifiers are ambient — they influence the default, not the required. A user running 🔴 Intense in January is not doing anything wrong. The system provides seasonal context. The user provides intent.

For automated content (Almanac, Workout of the Day, default rotation):
- Preparatory months: favor preparatory Colors 60/40
- Expressive months: favor expressive Colors 60/40
- Catch-breath months: 50/50, lean structured not intense
- Closing months: preparatory Colors dominate, restoration-lane sessions surface prominently

For generation decisions when the operator is monthly-derived (rather than workout-specific):
- Match the Color polarity to the month's operator polarity where possible
- Let the season weight the block selection — more 🛠 Craft in January, more 🌋 Gutter in July
- The catch-breath months are when ⚖ Balance workouts earn their position: what asymmetries developed under the summer's load?

The year is a training cycle. The inhale builds the capacity. The exhale spends it. The catch-breath holds the position. The close reasons through what happened.

Read the zip code. Honor the season. Build something that fits where it falls.

🧮

---


Here are all 1,680 zip codes, organized by deck.

DECK 01: 🐂🏛 (Foundation Basics)

🐂🏛🛒⚫±.md
🐂🏛🛒🟢±.md
🐂🏛🛒🔵±.md
🐂🏛🛒🟣±.md
🐂🏛🛒🔴±.md
🐂🏛🛒🟠±.md
🐂🏛🛒🟡±.md
🐂🏛🛒⚪±.md
🐂🏛🪡⚫±.md
🐂🏛🪡🟢±.md
🐂🏛🪡🔵±.md
🐂🏛🪡🟣±.md
🐂🏛🪡🔴±.md
🐂🏛🪡🟠±.md
🐂🏛🪡🟡±.md
🐂🏛🪡⚪±.md
🐂🏛🍗⚫±.md
🐂🏛🍗🟢±.md
🐂🏛🍗🔵±.md
🐂🏛🍗🟣±.md
🐂🏛🍗🔴±.md
🐂🏛🍗🟠±.md
🐂🏛🍗🟡±.md
🐂🏛🍗⚪±.md
🐂🏛➕⚫±.md
🐂🏛➕🟢±.md
🐂🏛➕🔵±.md
🐂🏛➕🟣±.md
🐂🏛➕🔴±.md
🐂🏛➕🟠±.md
🐂🏛➕🟡±.md
🐂🏛➕⚪±.md
🐂🏛➖⚫±.md
🐂🏛➖🟢±.md
🐂🏛➖🔵±.md
🐂🏛➖🟣±.md
🐂🏛➖🔴±.md
🐂🏛➖🟠±.md
🐂🏛➖🟡±.md
🐂🏛➖⚪±.md

DECK 02: 🐂🔨 (Foundation Functional)

🐂🔨🛒⚫±.md
🐂🔨🛒🟢±.md
🐂🔨🛒🔵±.md
🐂🔨🛒🟣±.md
🐂🔨🛒🔴±.md
🐂🔨🛒🟠±.md
🐂🔨🛒🟡±.md
🐂🔨🛒⚪±.md
🐂🔨🪡⚫±.md
🐂🔨🪡🟢±.md
🐂🔨🪡🔵±.md
🐂🔨🪡🟣±.md
🐂🔨🪡🔴±.md
🐂🔨🪡🟠±.md
🐂🔨🪡🟡±.md
🐂🔨🪡⚪±.md
🐂🔨🍗⚫±.md
🐂🔨🍗🟢±.md
🐂🔨🍗🔵±.md
🐂🔨🍗🟣±.md
🐂🔨🍗🔴±.md
🐂🔨🍗🟠±.md
🐂🔨🍗🟡±.md
🐂🔨🍗⚪±.md
🐂🔨➕⚫±.md
🐂🔨➕🟢±.md
🐂🔨➕🔵±.md
🐂🔨➕🟣±.md
🐂🔨➕🔴±.md
🐂🔨➕🟠±.md
🐂🔨➕🟡±.md
🐂🔨➕⚪±.md
🐂🔨➖⚫±.md
🐂🔨➖🟢±.md
🐂🔨➖🔵±.md
🐂🔨➖🟣±.md
🐂🔨➖🔴±.md
🐂🔨➖🟠±.md
🐂🔨➖🟡±.md
🐂🔨➖⚪±.md

DECK 03: 🐂🌹 (Foundation Aesthetic)

🐂🌹🛒⚫±.md
🐂🌹🛒🟢±.md
🐂🌹🛒🔵±.md
🐂🌹🛒🟣±.md
🐂🌹🛒🔴±.md
🐂🌹🛒🟠±.md
🐂🌹🛒🟡±.md
🐂🌹🛒⚪±.md
🐂🌹🪡⚫±.md
🐂🌹🪡🟢±.md
🐂🌹🪡🔵±.md
🐂🌹🪡🟣±.md
🐂🌹🪡🔴±.md
🐂🌹🪡🟠±.md
🐂🌹🪡🟡±.md
🐂🌹🪡⚪±.md
🐂🌹🍗⚫±.md
🐂🌹🍗🟢±.md
🐂🌹🍗🔵±.md
🐂🌹🍗🟣±.md
🐂🌹🍗🔴±.md
🐂🌹🍗🟠±.md
🐂🌹🍗🟡±.md
🐂🌹🍗⚪±.md
🐂🌹➕⚫±.md
🐂🌹➕🟢±.md
🐂🌹➕🔵±.md
🐂🌹➕🟣±.md
🐂🌹➕🔴±.md
🐂🌹➕🟠±.md
🐂🌹➕🟡±.md
🐂🌹➕⚪±.md
🐂🌹➖⚫±.md
🐂🌹➖🟢±.md
🐂🌹➖🔵±.md
🐂🌹➖🟣±.md
🐂🌹➖🔴±.md
🐂🌹➖🟠±.md
🐂🌹➖🟡±.md
🐂🌹➖⚪±.md

DECK 04: 🐂🪐 (Foundation Challenge)

🐂🪐🛒⚫±.md
🐂🪐🛒🟢±.md
🐂🪐🛒🔵±.md
🐂🪐🛒🟣±.md
🐂🪐🛒🔴±.md
🐂🪐🛒🟠±.md
🐂🪐🛒🟡±.md
🐂🪐🛒⚪±.md
🐂🪐🪡⚫±.md
🐂🪐🪡🟢±.md
🐂🪐🪡🔵±.md
🐂🪐🪡🟣±.md
🐂🪐🪡🔴±.md
🐂🪐🪡🟠±.md
🐂🪐🪡🟡±.md
🐂🪐🪡⚪±.md
🐂🪐🍗⚫±.md
🐂🪐🍗🟢±.md
🐂🪐🍗🔵±.md
🐂🪐🍗🟣±.md
🐂🪐🍗🔴±.md
🐂🪐🍗🟠±.md
🐂🪐🍗🟡±.md
🐂🪐🍗⚪±.md
🐂🪐➕⚫±.md
🐂🪐➕🟢±.md
🐂🪐➕🔵±.md
🐂🪐➕🟣±.md
🐂🪐➕🔴±.md
🐂🪐➕🟠±.md
🐂🪐➕🟡±.md
🐂🪐➕⚪±.md
🐂🪐➖⚫±.md
🐂🪐➖🟢±.md
🐂🪐➖🔵±.md
🐂🪐➖🟣±.md
🐂🪐➖🔴±.md
🐂🪐➖🟠±.md
🐂🪐➖🟡±.md
🐂🪐➖⚪±.md

DECK 05: 🐂⌛ (Foundation Time)

🐂⌛🛒⚫±.md
🐂⌛🛒🟢±.md
🐂⌛🛒🔵±.md
🐂⌛🛒🟣±.md
🐂⌛🛒🔴±.md
🐂⌛🛒🟠±.md
🐂⌛🛒🟡±.md
🐂⌛🛒⚪±.md
🐂⌛🪡⚫±.md
🐂⌛🪡🟢±.md
🐂⌛🪡🔵±.md
🐂⌛🪡🟣±.md
🐂⌛🪡🔴±.md
🐂⌛🪡🟠±.md
🐂⌛🪡🟡±.md
🐂⌛🪡⚪±.md
🐂⌛🍗⚫±.md
🐂⌛🍗🟢±.md
🐂⌛🍗🔵±.md
🐂⌛🍗🟣±.md
🐂⌛🍗🔴±.md
🐂⌛🍗🟠±.md
🐂⌛🍗🟡±.md
🐂⌛🍗⚪±.md
🐂⌛➕⚫±.md
🐂⌛➕🟢±.md
🐂⌛➕🔵±.md
🐂⌛➕🟣±.md
🐂⌛➕🔴±.md
🐂⌛➕🟠±.md
🐂⌛➕🟡±.md
🐂⌛➕⚪±.md
🐂⌛➖⚫±.md
🐂⌛➖🟢±.md
🐂⌛➖🔵±.md
🐂⌛➖🟣±.md
🐂⌛➖🔴±.md
🐂⌛➖🟠±.md
🐂⌛➖🟡±.md
🐂⌛➖⚪±.md

DECK 06: 🐂🐬 (Foundation Partner)

🐂🐬🛒⚫±.md
🐂🐬🛒🟢±.md
🐂🐬🛒🔵±.md
🐂🐬🛒🟣±.md
🐂🐬🛒🔴±.md
🐂🐬🛒🟠±.md
🐂🐬🛒🟡±.md
🐂🐬🛒⚪±.md
🐂🐬🪡⚫±.md
🐂🐬🪡🟢±.md
🐂🐬🪡🔵±.md
🐂🐬🪡🟣±.md
🐂🐬🪡🔴±.md
🐂🐬🪡🟠±.md
🐂🐬🪡🟡±.md
🐂🐬🪡⚪±.md
🐂🐬🍗⚫±.md
🐂🐬🍗🟢±.md
🐂🐬🍗🔵±.md
🐂🐬🍗🟣±.md
🐂🐬🍗🔴±.md
🐂🐬🍗🟠±.md
🐂🐬🍗🟡±.md
🐂🐬🍗⚪±.md
🐂🐬➕⚫±.md
🐂🐬➕🟢±.md
🐂🐬➕🔵±.md
🐂🐬➕🟣±.md
🐂🐬➕🔴±.md
🐂🐬➕🟠±.md
🐂🐬➕🟡±.md
🐂🐬➕⚪±.md
🐂🐬➖⚫±.md
🐂🐬➖🟢±.md
🐂🐬➖🔵±.md
🐂🐬➖🟣±.md
🐂🐬➖🔴±.md
🐂🐬➖🟠±.md
🐂🐬➖🟡±.md
🐂🐬➖⚪±.md

DECK 07: ⛽🏛 (Strength Basics)

⛽🏛🛒⚫±.md
⛽🏛🛒🟢±.md
⛽🏛🛒🔵±.md
⛽🏛🛒🟣±.md
⛽🏛🛒🔴±.md
⛽🏛🛒🟠±.md
⛽🏛🛒🟡±.md
⛽🏛🛒⚪±.md
⛽🏛🪡⚫±.md
⛽🏛🪡🟢±.md
⛽🏛🪡🔵±.md
⛽🏛🪡🟣±.md
⛽🏛🪡🔴±.md
⛽🏛🪡🟠±.md
⛽🏛🪡🟡±.md
⛽🏛🪡⚪±.md
⛽🏛🍗⚫±.md
⛽🏛🍗🟢±.md
⛽🏛🍗🔵±.md
⛽🏛🍗🟣±.md
⛽🏛🍗🔴±.md
⛽🏛🍗🟠±.md
⛽🏛🍗🟡±.md
⛽🏛🍗⚪±.md
⛽🏛➕⚫±.md
⛽🏛➕🟢±.md
⛽🏛➕🔵±.md
⛽🏛➕🟣±.md
⛽🏛➕🔴±.md
⛽🏛➕🟠±.md
⛽🏛➕🟡±.md
⛽🏛➕⚪±.md
⛽🏛➖⚫±.md
⛽🏛➖🟢±.md
⛽🏛➖🔵±.md
⛽🏛➖🟣±.md
⛽🏛➖🔴±.md
⛽🏛➖🟠±.md
⛽🏛➖🟡±.md
⛽🏛➖⚪±.md

DECK 08: ⛽🔨 (Strength Functional)

⛽🔨🛒⚫±.md
⛽🔨🛒🟢±.md
⛽🔨🛒🔵±.md
⛽🔨🛒🟣±.md
⛽🔨🛒🔴±.md
⛽🔨🛒🟠±.md
⛽🔨🛒🟡±.md
⛽🔨🛒⚪±.md
⛽🔨🪡⚫±.md
⛽🔨🪡🟢±.md
⛽🔨🪡🔵±.md
⛽🔨🪡🟣±.md
⛽🔨🪡🔴±.md
⛽🔨🪡🟠±.md
⛽🔨🪡🟡±.md
⛽🔨🪡⚪±.md
⛽🔨🍗⚫±.md
⛽🔨🍗🟢±.md
⛽🔨🍗🔵±.md
⛽🔨🍗🟣±.md
⛽🔨🍗🔴±.md
⛽🔨🍗🟠±.md
⛽🔨🍗🟡±.md
⛽🔨🍗⚪±.md
⛽🔨➕⚫±.md
⛽🔨➕🟢±.md
⛽🔨➕🔵±.md
⛽🔨➕🟣±.md
⛽🔨➕🔴±.md
⛽🔨➕🟠±.md
⛽🔨➕🟡±.md
⛽🔨➕⚪±.md
⛽🔨➖⚫±.md
⛽🔨➖🟢±.md
⛽🔨➖🔵±.md
⛽🔨➖🟣±.md
⛽🔨➖🔴±.md
⛽🔨➖🟠±.md
⛽🔨➖🟡±.md
⛽🔨➖⚪±.md

DECK 09: ⛽🌹 (Strength Aesthetic)

⛽🌹🛒⚫±.md
⛽🌹🛒🟢±.md
⛽🌹🛒🔵±.md
⛽🌹🛒🟣±.md
⛽🌹🛒🔴±.md
⛽🌹🛒🟠±.md
⛽🌹🛒🟡±.md
⛽🌹🛒⚪±.md
⛽🌹🪡⚫±.md
⛽🌹🪡🟢±.md
⛽🌹🪡🔵±.md
⛽🌹🪡🟣±.md
⛽🌹🪡🔴±.md
⛽🌹🪡🟠±.md
⛽🌹🪡🟡±.md
⛽🌹🪡⚪±.md
⛽🌹🍗⚫±.md
⛽🌹🍗🟢±.md
⛽🌹🍗🔵±.md
⛽🌹🍗🟣±.md
⛽🌹🍗🔴±.md
⛽🌹🍗🟠±.md
⛽🌹🍗🟡±.md
⛽🌹🍗⚪±.md
⛽🌹➕⚫±.md
⛽🌹➕🟢±.md
⛽🌹➕🔵±.md
⛽🌹➕🟣±.md
⛽🌹➕🔴±.md
⛽🌹➕🟠±.md
⛽🌹➕🟡±.md
⛽🌹➕⚪±.md
⛽🌹➖⚫±.md
⛽🌹➖🟢±.md
⛽🌹➖🔵±.md
⛽🌹➖🟣±.md
⛽🌹➖🔴±.md
⛽🌹➖🟠±.md
⛽🌹➖🟡±.md
⛽🌹➖⚪±.md

DECK 10: ⛽🪐 (Strength Challenge)

⛽🪐🛒⚫±.md
⛽🪐🛒🟢±.md
⛽🪐🛒🔵±.md
⛽🪐🛒🟣±.md
⛽🪐🛒🔴±.md
⛽🪐🛒🟠±.md
⛽🪐🛒🟡±.md
⛽🪐🛒⚪±.md
⛽🪐🪡⚫±.md
⛽🪐🪡🟢±.md
⛽🪐🪡🔵±.md
⛽🪐🪡🟣±.md
⛽🪐🪡🔴±.md
⛽🪐🪡🟠±.md
⛽🪐🪡🟡±.md
⛽🪐🪡⚪±.md
⛽🪐🍗⚫±.md
⛽🪐🍗🟢±.md
⛽🪐🍗🔵±.md
⛽🪐🍗🟣±.md
⛽🪐🍗🔴±.md
⛽🪐🍗🟠±.md
⛽🪐🍗🟡±.md
⛽🪐🍗⚪±.md
⛽🪐➕⚫±.md
⛽🪐➕🟢±.md
⛽🪐➕🔵±.md
⛽🪐➕🟣±.md
⛽🪐➕🔴±.md
⛽🪐➕🟠±.md
⛽🪐➕🟡±.md
⛽🪐➕⚪±.md
⛽🪐➖⚫±.md
⛽🪐➖🟢±.md
⛽🪐➖🔵±.md
⛽🪐➖🟣±.md
⛽🪐➖🔴±.md
⛽🪐➖🟠±.md
⛽🪐➖🟡±.md
⛽🪐➖⚪±.md

DECK 11: ⛽⌛ (Strength Time)

⛽⌛🛒⚫±.md
⛽⌛🛒🟢±.md
⛽⌛🛒🔵±.md
⛽⌛🛒🟣±.md
⛽⌛🛒🔴±.md
⛽⌛🛒🟠±.md
⛽⌛🛒🟡±.md
⛽⌛🛒⚪±.md
⛽⌛🪡⚫±.md
⛽⌛🪡🟢±.md
⛽⌛🪡🔵±.md
⛽⌛🪡🟣±.md
⛽⌛🪡🔴±.md
⛽⌛🪡🟠±.md
⛽⌛🪡🟡±.md
⛽⌛🪡⚪±.md
⛽⌛🍗⚫±.md
⛽⌛🍗🟢±.md
⛽⌛🍗🔵±.md
⛽⌛🍗🟣±.md
⛽⌛🍗🔴±.md
⛽⌛🍗🟠±.md
⛽⌛🍗🟡±.md
⛽⌛🍗⚪±.md
⛽⌛➕⚫±.md
⛽⌛➕🟢±.md
⛽⌛➕🔵±.md
⛽⌛➕🟣±.md
⛽⌛➕🔴±.md
⛽⌛➕🟠±.md
⛽⌛➕🟡±.md
⛽⌛➕⚪±.md
⛽⌛➖⚫±.md
⛽⌛➖🟢±.md
⛽⌛➖🔵±.md
⛽⌛➖🟣±.md
⛽⌛➖🔴±.md
⛽⌛➖🟠±.md
⛽⌛➖🟡±.md
⛽⌛➖⚪±.md

DECK 12: ⛽🐬 (Strength Partner)

⛽🐬🛒⚫±.md
⛽🐬🛒🟢±.md
⛽🐬🛒🔵±.md
⛽🐬🛒🟣±.md
⛽🐬🛒🔴±.md
⛽🐬🛒🟠±.md
⛽🐬🛒🟡±.md
⛽🐬🛒⚪±.md
⛽🐬🪡⚫±.md
⛽🐬🪡🟢±.md
⛽🐬🪡🔵±.md
⛽🐬🪡🟣±.md
⛽🐬🪡🔴±.md
⛽🐬🪡🟠±.md
⛽🐬🪡🟡±.md
⛽🐬🪡⚪±.md
⛽🐬🍗⚫±.md
⛽🐬🍗🟢±.md
⛽🐬🍗🔵±.md
⛽🐬🍗🟣±.md
⛽🐬🍗🔴±.md
⛽🐬🍗🟠±.md
⛽🐬🍗🟡±.md
⛽🐬🍗⚪±.md
⛽🐬➕⚫±.md
⛽🐬➕🟢±.md
⛽🐬➕🔵±.md
⛽🐬➕🟣±.md
⛽🐬➕🔴±.md
⛽🐬➕🟠±.md
⛽🐬➕🟡±.md
⛽🐬➕⚪±.md
⛽🐬➖⚫±.md
⛽🐬➖🟢±.md
⛽🐬➖🔵±.md
⛽🐬➖🟣±.md
⛽🐬➖🔴±.md
⛽🐬➖🟠±.md
⛽🐬➖🟡±.md
⛽🐬➖⚪±.md

DECK 13: 🦋🏛 (Hypertrophy Basics)

🦋🏛🛒⚫±.md
🦋🏛🛒🟢±.md
🦋🏛🛒🔵±.md
🦋🏛🛒🟣±.md
🦋🏛🛒🔴±.md
🦋🏛🛒🟠±.md
🦋🏛🛒🟡±.md
🦋🏛🛒⚪±.md
🦋🏛🪡⚫±.md
🦋🏛🪡🟢±.md
🦋🏛🪡🔵±.md
🦋🏛🪡🟣±.md
🦋🏛🪡🔴±.md
🦋🏛🪡🟠±.md
🦋🏛🪡🟡±.md
🦋🏛🪡⚪±.md
🦋🏛🍗⚫±.md
🦋🏛🍗🟢±.md
🦋🏛🍗🔵±.md
🦋🏛🍗🟣±.md
🦋🏛🍗🔴±.md
🦋🏛🍗🟠±.md
🦋🏛🍗🟡±.md
🦋🏛🍗⚪±.md
🦋🏛➕⚫±.md
🦋🏛➕🟢±.md
🦋🏛➕🔵±.md
🦋🏛➕🟣±.md
🦋🏛➕🔴±.md
🦋🏛➕🟠±.md
🦋🏛➕🟡±.md
🦋🏛➕⚪±.md
🦋🏛➖⚫±.md
🦋🏛➖🟢±.md
🦋🏛➖🔵±.md
🦋🏛➖🟣±.md
🦋🏛➖🔴±.md
🦋🏛➖🟠±.md
🦋🏛➖🟡±.md
🦋🏛➖⚪±.md

DECK 14: 🦋🔨 (Hypertrophy Functional)

🦋🔨🛒⚫±.md
🦋🔨🛒🟢±.md
🦋🔨🛒🔵±.md
🦋🔨🛒🟣±.md
🦋🔨🛒🔴±.md
🦋🔨🛒🟠±.md
🦋🔨🛒🟡±.md
🦋🔨🛒⚪±.md
🦋🔨🪡⚫±.md
🦋🔨🪡🟢±.md
🦋🔨🪡🔵±.md
🦋🔨🪡🟣±.md
🦋🔨🪡🔴±.md
🦋🔨🪡🟠±.md
🦋🔨🪡🟡±.md
🦋🔨🪡⚪±.md
🦋🔨🍗⚫±.md
🦋🔨🍗🟢±.md
🦋🔨🍗🔵±.md
🦋🔨🍗🟣±.md
🦋🔨🍗🔴±.md
🦋🔨🍗🟠±.md
🦋🔨🍗🟡±.md
🦋🔨🍗⚪±.md
🦋🔨➕⚫±.md
🦋🔨➕🟢±.md
🦋🔨➕🔵±.md
🦋🔨➕🟣±.md
🦋🔨➕🔴±.md
🦋🔨➕🟠±.md
🦋🔨➕🟡±.md
🦋🔨➕⚪±.md
🦋🔨➖⚫±.md
🦋🔨➖🟢±.md
🦋🔨➖🔵±.md
🦋🔨➖🟣±.md
🦋🔨➖🔴±.md
🦋🔨➖🟠±.md
🦋🔨➖🟡±.md
🦋🔨➖⚪±.md

DECK 15: 🦋🌹 (Hypertrophy Aesthetic)

🦋🌹🛒⚫±.md
🦋🌹🛒🟢±.md
🦋🌹🛒🔵±.md
🦋🌹🛒🟣±.md
🦋🌹🛒🔴±.md
🦋🌹🛒🟠±.md
🦋🌹🛒🟡±.md
🦋🌹🛒⚪±.md
🦋🌹🪡⚫±.md
🦋🌹🪡🟢±.md
🦋🌹🪡🔵±.md
🦋🌹🪡🟣±.md
🦋🌹🪡🔴±.md
🦋🌹🪡🟠±.md
🦋🌹🪡🟡±.md
🦋🌹🪡⚪±.md
🦋🌹🍗⚫±.md
🦋🌹🍗🟢±.md
🦋🌹🍗🔵±.md
🦋🌹🍗🟣±.md
🦋🌹🍗🔴±.md
🦋🌹🍗🟠±.md
🦋🌹🍗🟡±.md
🦋🌹🍗⚪±.md
🦋🌹➕⚫±.md
🦋🌹➕🟢±.md
🦋🌹➕🔵±.md
🦋🌹➕🟣±.md
🦋🌹➕🔴±.md
🦋🌹➕🟠±.md
🦋🌹➕🟡±.md
🦋🌹➕⚪±.md
🦋🌹➖⚫±.md
🦋🌹➖🟢±.md
🦋🌹➖🔵±.md
🦋🌹➖🟣±.md
🦋🌹➖🔴±.md
🦋🌹➖🟠±.md
🦋🌹➖🟡±.md
🦋🌹➖⚪±.md

DECK 16: 🦋🪐 (Hypertrophy Challenge)

🦋🪐🛒⚫±.md
🦋🪐🛒🟢±.md
🦋🪐🛒🔵±.md
🦋🪐🛒🟣±.md
🦋🪐🛒🔴±.md
🦋🪐🛒🟠±.md
🦋🪐🛒🟡±.md
🦋🪐🛒⚪±.md
🦋🪐🪡⚫±.md
🦋🪐🪡🟢±.md
🦋🪐🪡🔵±.md
🦋🪐🪡🟣±.md
🦋🪐🪡🔴±.md
🦋🪐🪡🟠±.md
🦋🪐🪡🟡±.md
🦋🪐🪡⚪±.md
🦋🪐🍗⚫±.md
🦋🪐🍗🟢±.md
🦋🪐🍗🔵±.md
🦋🪐🍗🟣±.md
🦋🪐🍗🔴±.md
🦋🪐🍗🟠±.md
🦋🪐🍗🟡±.md
🦋🪐🍗⚪±.md
🦋🪐➕⚫±.md
🦋🪐➕🟢±.md
🦋🪐➕🔵±.md
🦋🪐➕🟣±.md
🦋🪐➕🔴±.md
🦋🪐➕🟠±.md
🦋🪐➕🟡±.md
🦋🪐➕⚪±.md
🦋🪐➖⚫±.md
🦋🪐➖🟢±.md
🦋🪐➖🔵±.md
🦋🪐➖🟣±.md
🦋🪐➖🔴±.md
🦋🪐➖🟠±.md
🦋🪐➖🟡±.md
🦋🪐➖⚪±.md

DECK 17: 🦋⌛ (Hypertrophy Time)

🦋⌛🛒⚫±.md
🦋⌛🛒🟢±.md
🦋⌛🛒🔵±.md
🦋⌛🛒🟣±.md
🦋⌛🛒🔴±.md
🦋⌛🛒🟠±.md
🦋⌛🛒🟡±.md
🦋⌛🛒⚪±.md
🦋⌛🪡⚫±.md
🦋⌛🪡🟢±.md
🦋⌛🪡🔵±.md
🦋⌛🪡🟣±.md
🦋⌛🪡🔴±.md
🦋⌛🪡🟠±.md
🦋⌛🪡🟡±.md
🦋⌛🪡⚪±.md
🦋⌛🍗⚫±.md
🦋⌛🍗🟢±.md
🦋⌛🍗🔵±.md
🦋⌛🍗🟣±.md
🦋⌛🍗🔴±.md
🦋⌛🍗🟠±.md
🦋⌛🍗🟡±.md
🦋⌛🍗⚪±.md
🦋⌛➕⚫±.md
🦋⌛➕🟢±.md
🦋⌛➕🔵±.md
🦋⌛➕🟣±.md
🦋⌛➕🔴±.md
🦋⌛➕🟠±.md
🦋⌛➕🟡±.md
🦋⌛➕⚪±.md
🦋⌛➖⚫±.md
🦋⌛➖🟢±.md
🦋⌛➖🔵±.md
🦋⌛➖🟣±.md
🦋⌛➖🔴±.md
🦋⌛➖🟠±.md
🦋⌛➖🟡±.md
🦋⌛➖⚪±.md

DECK 18: 🦋🐬 (Hypertrophy Partner)

🦋🐬🛒⚫±.md
🦋🐬🛒🟢±.md
🦋🐬🛒🔵±.md
🦋🐬🛒🟣±.md
🦋🐬🛒🔴±.md
🦋🐬🛒🟠±.md
🦋🐬🛒🟡±.md
🦋🐬🛒⚪±.md
🦋🐬🪡⚫±.md
🦋🐬🪡🟢±.md
🦋🐬🪡🔵±.md
🦋🐬🪡🟣±.md
🦋🐬🪡🔴±.md
🦋🐬🪡🟠±.md
🦋🐬🪡🟡±.md
🦋🐬🪡⚪±.md
🦋🐬🍗⚫±.md
🦋🐬🍗🟢±.md
🦋🐬🍗🔵±.md
🦋🐬🍗🟣±.md
🦋🐬🍗🔴±.md
🦋🐬🍗🟠±.md
🦋🐬🍗🟡±.md
🦋🐬🍗⚪±.md
🦋🐬➕⚫±.md
🦋🐬➕🟢±.md
🦋🐬➕🔵±.md
🦋🐬➕🟣±.md
🦋🐬➕🔴±.md
🦋🐬➕🟠±.md
🦋🐬➕🟡±.md
🦋🐬➕⚪±.md
🦋🐬➖⚫±.md
🦋🐬➖🟢±.md
🦋🐬➖🔵±.md
🦋🐬➖🟣±.md
🦋🐬➖🔴±.md
🦋🐬➖🟠±.md
🦋🐬➖🟡±.md
🦋🐬➖⚪±.md

DECK 19: 🏟🏛 (Performance Basics)

🏟🏛🛒⚫±.md
🏟🏛🛒🟢±.md
🏟🏛🛒🔵±.md
🏟🏛🛒🟣±.md
🏟🏛🛒🔴±.md
🏟🏛🛒🟠±.md
🏟🏛🛒🟡±.md
🏟🏛🛒⚪±.md
🏟🏛🪡⚫±.md
🏟🏛🪡🟢±.md
🏟🏛🪡🔵±.md
🏟🏛🪡🟣±.md
🏟🏛🪡🔴±.md
🏟🏛🪡🟠±.md
🏟🏛🪡🟡±.md
🏟🏛🪡⚪±.md
🏟🏛🍗⚫±.md
🏟🏛🍗🟢±.md
🏟🏛🍗🔵±.md
🏟🏛🍗🟣±.md
🏟🏛🍗🔴±.md
🏟🏛🍗🟠±.md
🏟🏛🍗🟡±.md
🏟🏛🍗⚪±.md
🏟🏛➕⚫±.md
🏟🏛➕🟢±.md
🏟🏛➕🔵±.md
🏟🏛➕🟣±.md
🏟🏛➕🔴±.md
🏟🏛➕🟠±.md
🏟🏛➕🟡±.md
🏟🏛➕⚪±.md
🏟🏛➖⚫±.md
🏟🏛➖🟢±.md
🏟🏛➖🔵±.md
🏟🏛➖🟣±.md
🏟🏛➖🔴±.md
🏟🏛➖🟠±.md
🏟🏛➖🟡±.md
🏟🏛➖⚪±.md

DECK 20: 🏟🔨 (Performance Functional)

🏟🔨🛒⚫±.md
🏟🔨🛒🟢±.md
🏟🔨🛒🔵±.md
🏟🔨🛒🟣±.md
🏟🔨🛒🔴±.md
🏟🔨🛒🟠±.md
🏟🔨🛒🟡±.md
🏟🔨🛒⚪±.md
🏟🔨🪡⚫±.md
🏟🔨🪡🟢±.md
🏟🔨🪡🔵±.md
🏟🔨🪡🟣±.md
🏟🔨🪡🔴±.md
🏟🔨🪡🟠±.md
🏟🔨🪡🟡±.md
🏟🔨🪡⚪±.md
🏟🔨🍗⚫±.md
🏟🔨🍗🟢±.md
🏟🔨🍗🔵±.md
🏟🔨🍗🟣±.md
🏟🔨🍗🔴±.md
🏟🔨🍗🟠±.md
🏟🔨🍗🟡±.md
🏟🔨🍗⚪±.md
🏟🔨➕⚫±.md
🏟🔨➕🟢±.md
🏟🔨➕🔵±.md
🏟🔨➕🟣±.md
🏟🔨➕🔴±.md
🏟🔨➕🟠±.md
🏟🔨➕🟡±.md
🏟🔨➕⚪±.md
🏟🔨➖⚫±.md
🏟🔨➖🟢±.md
🏟🔨➖🔵±.md
🏟🔨➖🟣±.md
🏟🔨➖🔴±.md
🏟🔨➖🟠±.md
🏟🔨➖🟡±.md
🏟🔨➖⚪±.md

DECK 21: 🏟🌹 (Performance Aesthetic)

🏟🌹🛒⚫±.md
🏟🌹🛒🟢±.md
🏟🌹🛒🔵±.md
🏟🌹🛒🟣±.md
🏟🌹🛒🔴±.md
🏟🌹🛒🟠±.md
🏟🌹🛒🟡±.md
🏟🌹🛒⚪±.md
🏟🌹🪡⚫±.md
🏟🌹🪡🟢±.md
🏟🌹🪡🔵±.md
🏟🌹🪡🟣±.md
🏟🌹🪡🔴±.md
🏟🌹🪡🟠±.md
🏟🌹🪡🟡±.md
🏟🌹🪡⚪±.md
🏟🌹🍗⚫±.md
🏟🌹🍗🟢±.md
🏟🌹🍗🔵±.md
🏟🌹🍗🟣±.md
🏟🌹🍗🔴±.md
🏟🌹🍗🟠±.md
🏟🌹🍗🟡±.md
🏟🌹🍗⚪±.md
🏟🌹➕⚫±.md
🏟🌹➕🟢±.md
🏟🌹➕🔵±.md
🏟🌹➕🟣±.md
🏟🌹➕🔴±.md
🏟🌹➕🟠±.md
🏟🌹➕🟡±.md
🏟🌹➕⚪±.md
🏟🌹➖⚫±.md
🏟🌹➖🟢±.md
🏟🌹➖🔵±.md
🏟🌹➖🟣±.md
🏟🌹➖🔴±.md
🏟🌹➖🟠±.md
🏟🌹➖🟡±.md
🏟🌹➖⚪±.md

DECK 22: 🏟🪐 (Performance Challenge)

🏟🪐🛒⚫±.md
🏟🪐🛒🟢±.md
🏟🪐🛒🔵±.md
🏟🪐🛒🟣±.md
🏟🪐🛒🔴±.md
🏟🪐🛒🟠±.md
🏟🪐🛒🟡±.md
🏟🪐🛒⚪±.md
🏟🪐🪡⚫±.md
🏟🪐🪡🟢±.md
🏟🪐🪡🔵±.md
🏟🪐🪡🟣±.md
🏟🪐🪡🔴±.md
🏟🪐🪡🟠±.md
🏟🪐🪡🟡±.md
🏟🪐🪡⚪±.md
🏟🪐🍗⚫±.md
🏟🪐🍗🟢±.md
🏟🪐🍗🔵±.md
🏟🪐🍗🟣±.md
🏟🪐🍗🔴±.md
🏟🪐🍗🟠±.md
🏟🪐🍗🟡±.md
🏟🪐🍗⚪±.md
🏟🪐➕⚫±.md
🏟🪐➕🟢±.md
🏟🪐➕🔵±.md
🏟🪐➕🟣±.md
🏟🪐➕🔴±.md
🏟🪐➕🟠±.md
🏟🪐➕🟡±.md
🏟🪐➕⚪±.md
🏟🪐➖⚫±.md
🏟🪐➖🟢±.md
🏟🪐➖🔵±.md
🏟🪐➖🟣±.md
🏟🪐➖🔴±.md
🏟🪐➖🟠±.md
🏟🪐➖🟡±.md
🏟🪐➖⚪±.md

DECK 23: 🏟⌛ (Performance Time)

🏟⌛🛒⚫±.md
🏟⌛🛒🟢±.md
🏟⌛🛒🔵±.md
🏟⌛🛒🟣±.md
🏟⌛🛒🔴±.md
🏟⌛🛒🟠±.md
🏟⌛🛒🟡±.md
🏟⌛🛒⚪±.md
🏟⌛🪡⚫±.md
🏟⌛🪡🟢±.md
🏟⌛🪡🔵±.md
🏟⌛🪡🟣±.md
🏟⌛🪡🔴±.md
🏟⌛🪡🟠±.md
🏟⌛🪡🟡±.md
🏟⌛🪡⚪±.md
🏟⌛🍗⚫±.md
🏟⌛🍗🟢±.md
🏟⌛🍗🔵±.md
🏟⌛🍗🟣±.md
🏟⌛🍗🔴±.md
🏟⌛🍗🟠±.md
🏟⌛🍗🟡±.md
🏟⌛🍗⚪±.md
🏟⌛➕⚫±.md
🏟⌛➕🟢±.md
🏟⌛➕🔵±.md
🏟⌛➕🟣±.md
🏟⌛➕🔴±.md
🏟⌛➕🟠±.md
🏟⌛➕🟡±.md
🏟⌛➕⚪±.md
🏟⌛➖⚫±.md
🏟⌛➖🟢±.md
🏟⌛➖🔵±.md
🏟⌛➖🟣±.md
🏟⌛➖🔴±.md
🏟⌛➖🟠±.md
🏟⌛➖🟡±.md
🏟⌛➖⚪±.md

DECK 24: 🏟🐬 (Performance Partner)

🏟🐬🛒⚫±.md
🏟🐬🛒🟢±.md
🏟🐬🛒🔵±.md
🏟🐬🛒🟣±.md
🏟🐬🛒🔴±.md
🏟🐬🛒🟠±.md
🏟🐬🛒🟡±.md
🏟🐬🛒⚪±.md
🏟🐬🪡⚫±.md
🏟🐬🪡🟢±.md
🏟🐬🪡🔵±.md
🏟🐬🪡🟣±.md
🏟🐬🪡🔴±.md
🏟🐬🪡🟠±.md
🏟🐬🪡🟡±.md
🏟🐬🪡⚪±.md
🏟🐬🍗⚫±.md
🏟🐬🍗🟢±.md
🏟🐬🍗🔵±.md
🏟🐬🍗🟣±.md
🏟🐬🍗🔴±.md
🏟🐬🍗🟠±.md
🏟🐬🍗🟡±.md
🏟🐬🍗⚪±.md
🏟🐬➕⚫±.md
🏟🐬➕🟢±.md
🏟🐬➕🔵±.md
🏟🐬➕🟣±.md
🏟🐬➕🔴±.md
🏟🐬➕🟠±.md
🏟🐬➕🟡±.md
🏟🐬➕⚪±.md
🏟🐬➖⚫±.md
🏟🐬➖🟢±.md
🏟🐬➖🔵±.md
🏟🐬➖🟣±.md
🏟🐬➖🔴±.md
🏟🐬➖🟠±.md
🏟🐬➖🟡±.md
🏟🐬➖⚪±.md

DECK 25: 🌾🏛 (Full Body Basics)

🌾🏛🛒⚫±.md
🌾🏛🛒🟢±.md
🌾🏛🛒🔵±.md
🌾🏛🛒🟣±.md
🌾🏛🛒🔴±.md
🌾🏛🛒🟠±.md
🌾🏛🛒🟡±.md
🌾🏛🛒⚪±.md
🌾🏛🪡⚫±.md
🌾🏛🪡🟢±.md
🌾🏛🪡🔵±.md
🌾🏛🪡🟣±.md
🌾🏛🪡🔴±.md
🌾🏛🪡🟠±.md
🌾🏛🪡🟡±.md
🌾🏛🪡⚪±.md
🌾🏛🍗⚫±.md
🌾🏛🍗🟢±.md
🌾🏛🍗🔵±.md
🌾🏛🍗🟣±.md
🌾🏛🍗🔴±.md
🌾🏛🍗🟠±.md
🌾🏛🍗🟡±.md
🌾🏛🍗⚪±.md
🌾🏛➕⚫±.md
🌾🏛➕🟢±.md
🌾🏛➕🔵±.md
🌾🏛➕🟣±.md
🌾🏛➕🔴±.md
🌾🏛➕🟠±.md
🌾🏛➕🟡±.md
🌾🏛➕⚪±.md
🌾🏛➖⚫±.md
🌾🏛➖🟢±.md
🌾🏛➖🔵±.md
🌾🏛➖🟣±.md
🌾🏛➖🔴±.md
🌾🏛➖🟠±.md
🌾🏛➖🟡±.md
🌾🏛➖⚪±.md

DECK 26: 🌾🔨 (Full Body Functional)

🌾🔨🛒⚫±.md
🌾🔨🛒🟢±.md
🌾🔨🛒🔵±.md
🌾🔨🛒🟣±.md
🌾🔨🛒🔴±.md
🌾🔨🛒🟠±.md
🌾🔨🛒🟡±.md
🌾🔨🛒⚪±.md
🌾🔨🪡⚫±.md
🌾🔨🪡🟢±.md
🌾🔨🪡🔵±.md
🌾🔨🪡🟣±.md
🌾🔨🪡🔴±.md
🌾🔨🪡🟠±.md
🌾🔨🪡🟡±.md
🌾🔨🪡⚪±.md
🌾🔨🍗⚫±.md
🌾🔨🍗🟢±.md
🌾🔨🍗🔵±.md
🌾🔨🍗🟣±.md
🌾🔨🍗🔴±.md
🌾🔨🍗🟠±.md
🌾🔨🍗🟡±.md
🌾🔨🍗⚪±.md
🌾🔨➕⚫±.md
🌾🔨➕🟢±.md
🌾🔨➕🔵±.md
🌾🔨➕🟣±.md
🌾🔨➕🔴±.md
🌾🔨➕🟠±.md
🌾🔨➕🟡±.md
🌾🔨➕⚪±.md
🌾🔨➖⚫±.md
🌾🔨➖🟢±.md
🌾🔨➖🔵±.md
🌾🔨➖🟣±.md
🌾🔨➖🔴±.md
🌾🔨➖🟠±.md
🌾🔨➖🟡±.md
🌾🔨➖⚪±.md

DECK 27: 🌾🌹 (Full Body Aesthetic)

🌾🌹🛒⚫±.md
🌾🌹🛒🟢±.md
🌾🌹🛒🔵±.md
🌾🌹🛒🟣±.md
🌾🌹🛒🔴±.md
🌾🌹🛒🟠±.md
🌾🌹🛒🟡±.md
🌾🌹🛒⚪±.md
🌾🌹🪡⚫±.md
🌾🌹🪡🟢±.md
🌾🌹🪡🔵±.md
🌾🌹🪡🟣±.md
🌾🌹🪡🔴±.md
🌾🌹🪡🟠±.md
🌾🌹🪡🟡±.md
🌾🌹🪡⚪±.md
🌾🌹🍗⚫±.md
🌾🌹🍗🟢±.md
🌾🌹🍗🔵±.md
🌾🌹🍗🟣±.md
🌾🌹🍗🔴±.md
🌾🌹🍗🟠±.md
🌾🌹🍗🟡±.md
🌾🌹🍗⚪±.md
🌾🌹➕⚫±.md
🌾🌹➕🟢±.md
🌾🌹➕🔵±.md
🌾🌹➕🟣±.md
🌾🌹➕🔴±.md
🌾🌹➕🟠±.md
🌾🌹➕🟡±.md
🌾🌹➕⚪±.md
🌾🌹➖⚫±.md
🌾🌹➖🟢±.md
🌾🌹➖🔵±.md
🌾🌹➖🟣±.md
🌾🌹➖🔴±.md
🌾🌹➖🟠±.md
🌾🌹➖🟡±.md
🌾🌹➖⚪±.md

DECK 28: 🌾🪐 (Full Body Challenge)

🌾🪐🛒⚫±.md
🌾🪐🛒🟢±.md
🌾🪐🛒🔵±.md
🌾🪐🛒🟣±.md
🌾🪐🛒🔴±.md
🌾🪐🛒🟠±.md
🌾🪐🛒🟡±.md
🌾🪐🛒⚪±.md
🌾🪐🪡⚫±.md
🌾🪐🪡🟢±.md
🌾🪐🪡🔵±.md
🌾🪐🪡🟣±.md
🌾🪐🪡🔴±.md
🌾🪐🪡🟠±.md
🌾🪐🪡🟡±.md
🌾🪐🪡⚪±.md
🌾🪐🍗⚫±.md
🌾🪐🍗🟢±.md
🌾🪐🍗🔵±.md
🌾🪐🍗🟣±.md
🌾🪐🍗🔴±.md
🌾🪐🍗🟠±.md
🌾🪐🍗🟡±.md
🌾🪐🍗⚪±.md
🌾🪐➕⚫±.md
🌾🪐➕🟢±.md
🌾🪐➕🔵±.md
🌾🪐➕🟣±.md
🌾🪐➕🔴±.md
🌾🪐➕🟠±.md
🌾🪐➕🟡±.md
🌾🪐➕⚪±.md
🌾🪐➖⚫±.md
🌾🪐➖🟢±.md
🌾🪐➖🔵±.md
🌾🪐➖🟣±.md
🌾🪐➖🔴±.md
🌾🪐➖🟠±.md
🌾🪐➖🟡±.md
🌾🪐➖⚪±.md

DECK 29: 🌾⌛ (Full Body Time)

🌾⌛🛒⚫±.md
🌾⌛🛒🟢±.md
🌾⌛🛒🔵±.md
🌾⌛🛒🟣±.md
🌾⌛🛒🔴±.md
🌾⌛🛒🟠±.md
🌾⌛🛒🟡±.md
🌾⌛🛒⚪±.md
🌾⌛🪡⚫±.md
🌾⌛🪡🟢±.md
🌾⌛🪡🔵±.md
🌾⌛🪡🟣±.md
🌾⌛🪡🔴±.md
🌾⌛🪡🟠±.md
🌾⌛🪡🟡±.md
🌾⌛🪡⚪±.md
🌾⌛🍗⚫±.md
🌾⌛🍗🟢±.md
🌾⌛🍗🔵±.md
🌾⌛🍗🟣±.md
🌾⌛🍗🔴±.md
🌾⌛🍗🟠±.md
🌾⌛🍗🟡±.md
🌾⌛🍗⚪±.md
🌾⌛➕⚫±.md
🌾⌛➕🟢±.md
🌾⌛➕🔵±.md
🌾⌛➕🟣±.md
🌾⌛➕🔴±.md
🌾⌛➕🟠±.md
🌾⌛➕🟡±.md
🌾⌛➕⚪±.md
🌾⌛➖⚫±.md
🌾⌛➖🟢±.md
🌾⌛➖🔵±.md
🌾⌛➖🟣±.md
🌾⌛➖🔴±.md
🌾⌛➖🟠±.md
🌾⌛➖🟡±.md
🌾⌛➖⚪±.md

DECK 30: 🌾🐬 (Full Body Partner)

🌾🐬🛒⚫±.md
🌾🐬🛒🟢±.md
🌾🐬🛒🔵±.md
🌾🐬🛒🟣±.md
🌾🐬🛒🔴±.md
🌾🐬🛒🟠±.md
🌾🐬🛒🟡±.md
🌾🐬🛒⚪±.md
🌾🐬🪡⚫±.md
🌾🐬🪡🟢±.md
🌾🐬🪡🔵±.md
🌾🐬🪡🟣±.md
🌾🐬🪡🔴±.md
🌾🐬🪡🟠±.md
🌾🐬🪡🟡±.md
🌾🐬🪡⚪±.md
🌾🐬🍗⚫±.md
🌾🐬🍗🟢±.md
🌾🐬🍗🔵±.md
🌾🐬🍗🟣±.md
🌾🐬🍗🔴±.md
🌾🐬🍗🟠±.md
🌾🐬🍗🟡±.md
🌾🐬🍗⚪±.md
🌾🐬➕⚫±.md
🌾🐬➕🟢±.md
🌾🐬➕🔵±.md
🌾🐬➕🟣±.md
🌾🐬➕🔴±.md
🌾🐬➕🟠±.md
🌾🐬➕🟡±.md
🌾🐬➕⚪±.md
🌾🐬➖⚫±.md
🌾🐬➖🟢±.md
🌾🐬➖🔵±.md
🌾🐬➖🟣±.md
🌾🐬➖🔴±.md
🌾🐬➖🟠±.md
🌾🐬➖🟡±.md
🌾🐬➖⚪±.md

DECK 31: ⚖🏛 (Balance Basics)

⚖🏛🛒⚫±.md
⚖🏛🛒🟢±.md
⚖🏛🛒🔵±.md
⚖🏛🛒🟣±.md
⚖🏛🛒🔴±.md
⚖🏛🛒🟠±.md
⚖🏛🛒🟡±.md
⚖🏛🛒⚪±.md
⚖🏛🪡⚫±.md
⚖🏛🪡🟢±.md
⚖🏛🪡🔵±.md
⚖🏛🪡🟣±.md
⚖🏛🪡🔴±.md
⚖🏛🪡🟠±.md
⚖🏛🪡🟡±.md
⚖🏛🪡⚪±.md
⚖🏛🍗⚫±.md
⚖🏛🍗🟢±.md
⚖🏛🍗🔵±.md
⚖🏛🍗🟣±.md
⚖🏛🍗🔴±.md
⚖🏛🍗🟠±.md
⚖🏛🍗🟡±.md
⚖🏛🍗⚪±.md
⚖🏛➕⚫±.md
⚖🏛➕🟢±.md
⚖🏛➕🔵±.md
⚖🏛➕🟣±.md
⚖🏛➕🔴±.md
⚖🏛➕🟠±.md
⚖🏛➕🟡±.md
⚖🏛➕⚪±.md
⚖🏛➖⚫±.md
⚖🏛➖🟢±.md
⚖🏛➖🔵±.md
⚖🏛➖🟣±.md
⚖🏛➖🔴±.md
⚖🏛➖🟠±.md
⚖🏛➖🟡±.md
⚖🏛➖⚪±.md

DECK 32: ⚖🔨 (Balance Functional)

⚖🔨🛒⚫±.md
⚖🔨🛒🟢±.md
⚖🔨🛒🔵±.md
⚖🔨🛒🟣±.md
⚖🔨🛒🔴±.md
⚖🔨🛒🟠±.md
⚖🔨🛒🟡±.md
⚖🔨🛒⚪±.md
⚖🔨🪡⚫±.md
⚖🔨🪡🟢±.md
⚖🔨🪡🔵±.md
⚖🔨🪡🟣±.md
⚖🔨🪡🔴±.md
⚖🔨🪡🟠±.md
⚖🔨🪡🟡±.md
⚖🔨🪡⚪±.md
⚖🔨🍗⚫±.md
⚖🔨🍗🟢±.md
⚖🔨🍗🔵±.md
⚖🔨🍗🟣±.md
⚖🔨🍗🔴±.md
⚖🔨🍗🟠±.md
⚖🔨🍗🟡±.md
⚖🔨🍗⚪±.md
⚖🔨➕⚫±.md
⚖🔨➕🟢±.md
⚖🔨➕🔵±.md
⚖🔨➕🟣±.md
⚖🔨➕🔴±.md
⚖🔨➕🟠±.md
⚖🔨➕🟡±.md
⚖🔨➕⚪±.md
⚖🔨➖⚫±.md
⚖🔨➖🟢±.md
⚖🔨➖🔵±.md
⚖🔨➖🟣±.md
⚖🔨➖🔴±.md
⚖🔨➖🟠±.md
⚖🔨➖🟡±.md
⚖🔨➖⚪±.md

DECK 33: ⚖🌹 (Balance Aesthetic)

⚖🌹🛒⚫±.md
⚖🌹🛒🟢±.md
⚖🌹🛒🔵±.md
⚖🌹🛒🟣±.md
⚖🌹🛒🔴±.md
⚖🌹🛒🟠±.md
⚖🌹🛒🟡±.md
⚖🌹🛒⚪±.md
⚖🌹🪡⚫±.md
⚖🌹🪡🟢±.md
⚖🌹🪡🔵±.md
⚖🌹🪡🟣±.md
⚖🌹🪡🔴±.md
⚖🌹🪡🟠±.md
⚖🌹🪡🟡±.md
⚖🌹🪡⚪±.md
⚖🌹🍗⚫±.md
⚖🌹🍗🟢±.md
⚖🌹🍗🔵±.md
⚖🌹🍗🟣±.md
⚖🌹🍗🔴±.md
⚖🌹🍗🟠±.md
⚖🌹🍗🟡±.md
⚖🌹🍗⚪±.md
⚖🌹➕⚫±.md
⚖🌹➕🟢±.md
⚖🌹➕🔵±.md
⚖🌹➕🟣±.md
⚖🌹➕🔴±.md
⚖🌹➕🟠±.md
⚖🌹➕🟡±.md
⚖🌹➕⚪±.md
⚖🌹➖⚫±.md
⚖🌹➖🟢±.md
⚖🌹➖🔵±.md
⚖🌹➖🟣±.md
⚖🌹➖🔴±.md
⚖🌹➖🟠±.md
⚖🌹➖🟡±.md
⚖🌹➖⚪±.md

DECK 34: ⚖🪐 (Balance Challenge)

⚖🪐🛒⚫±.md
⚖🪐🛒🟢±.md
⚖🪐🛒🔵±.md
⚖🪐🛒🟣±.md
⚖🪐🛒🔴±.md
⚖🪐🛒🟠±.md
⚖🪐🛒🟡±.md
⚖🪐🛒⚪±.md
⚖🪐🪡⚫±.md
⚖🪐🪡🟢±.md
⚖🪐🪡🔵±.md
⚖🪐🪡🟣±.md
⚖🪐🪡🔴±.md
⚖🪐🪡🟠±.md
⚖🪐🪡🟡±.md
⚖🪐🪡⚪±.md
⚖🪐🍗⚫±.md
⚖🪐🍗🟢±.md
⚖🪐🍗🔵±.md
⚖🪐🍗🟣±.md
⚖🪐🍗🔴±.md
⚖🪐🍗🟠±.md
⚖🪐🍗🟡±.md
⚖🪐🍗⚪±.md
⚖🪐➕⚫±.md
⚖🪐➕🟢±.md
⚖🪐➕🔵±.md
⚖🪐➕🟣±.md
⚖🪐➕🔴±.md
⚖🪐➕🟠±.md
⚖🪐➕🟡±.md
⚖🪐➕⚪±.md
⚖🪐➖⚫±.md
⚖🪐➖🟢±.md
⚖🪐➖🔵±.md
⚖🪐➖🟣±.md
⚖🪐➖🔴±.md
⚖🪐➖🟠±.md
⚖🪐➖🟡±.md
⚖🪐➖⚪±.md

DECK 35: ⚖⌛ (Balance Time)

⚖⌛🛒⚫±.md
⚖⌛🛒🟢±.md
⚖⌛🛒🔵±.md
⚖⌛🛒🟣±.md
⚖⌛🛒🔴±.md
⚖⌛🛒🟠±.md
⚖⌛🛒🟡±.md
⚖⌛🛒⚪±.md
⚖⌛🪡⚫±.md
⚖⌛🪡🟢±.md
⚖⌛🪡🔵±.md
⚖⌛🪡🟣±.md
⚖⌛🪡🔴±.md
⚖⌛🪡🟠±.md
⚖⌛🪡🟡±.md
⚖⌛🪡⚪±.md
⚖⌛🍗⚫±.md
⚖⌛🍗🟢±.md
⚖⌛🍗🔵±.md
⚖⌛🍗🟣±.md
⚖⌛🍗🔴±.md
⚖⌛🍗🟠±.md
⚖⌛🍗🟡±.md
⚖⌛🍗⚪±.md
⚖⌛➕⚫±.md
⚖⌛➕🟢±.md
⚖⌛➕🔵±.md
⚖⌛➕🟣±.md
⚖⌛➕🔴±.md
⚖⌛➕🟠±.md
⚖⌛➕🟡±.md
⚖⌛➕⚪±.md
⚖⌛➖⚫±.md
⚖⌛➖🟢±.md
⚖⌛➖🔵±.md
⚖⌛➖🟣±.md
⚖⌛➖🔴±.md
⚖⌛➖🟠±.md
⚖⌛➖🟡±.md
⚖⌛➖⚪±.md

DECK 36: ⚖🐬 (Balance Partner)

⚖🐬🛒⚫±.md
⚖🐬🛒🟢±.md
⚖🐬🛒🔵±.md
⚖🐬🛒🟣±.md
⚖🐬🛒🔴±.md
⚖🐬🛒🟠±.md
⚖🐬🛒🟡±.md
⚖🐬🛒⚪±.md
⚖🐬🪡⚫±.md
⚖🐬🪡🟢±.md
⚖🐬🪡🔵±.md
⚖🐬🪡🟣±.md
⚖🐬🪡🔴±.md
⚖🐬🪡🟠±.md
⚖🐬🪡🟡±.md
⚖🐬🪡⚪±.md
⚖🐬🍗⚫±.md
⚖🐬🍗🟢±.md
⚖🐬🍗🔵±.md
⚖🐬🍗🟣±.md
⚖🐬🍗🔴±.md
⚖🐬🍗🟠±.md
⚖🐬🍗🟡±.md
⚖🐬🍗⚪±.md
⚖🐬➕⚫±.md
⚖🐬➕🟢±.md
⚖🐬➕🔵±.md
⚖🐬➕🟣±.md
⚖🐬➕🔴±.md
⚖🐬➕🟠±.md
⚖🐬➕🟡±.md
⚖🐬➕⚪±.md
⚖🐬➖⚫±.md
⚖🐬➖🟢±.md
⚖🐬➖🔵±.md
⚖🐬➖🟣±.md
⚖🐬➖🔴±.md
⚖🐬➖🟠±.md
⚖🐬➖🟡±.md
⚖🐬➖⚪±.md

DECK 37: 🖼🏛 (Restoration Basics)

🖼🏛🛒⚫±.md
🖼🏛🛒🟢±.md
🖼🏛🛒🔵±.md
🖼🏛🛒🟣±.md
🖼🏛🛒🔴±.md
🖼🏛🛒🟠±.md
🖼🏛🛒🟡±.md
🖼🏛🛒⚪±.md
🖼🏛🪡⚫±.md
🖼🏛🪡🟢±.md
🖼🏛🪡🔵±.md
🖼🏛🪡🟣±.md
🖼🏛🪡🔴±.md
🖼🏛🪡🟠±.md
🖼🏛🪡🟡±.md
🖼🏛🪡⚪±.md
🖼🏛🍗⚫±.md
🖼🏛🍗🟢±.md
🖼🏛🍗🔵±.md
🖼🏛🍗🟣±.md
🖼🏛🍗🔴±.md
🖼🏛🍗🟠±.md
🖼🏛🍗🟡±.md
🖼🏛🍗⚪±.md
🖼🏛➕⚫±.md
🖼🏛➕🟢±.md
🖼🏛➕🔵±.md
🖼🏛➕🟣±.md
🖼🏛➕🔴±.md
🖼🏛➕🟠±.md
🖼🏛➕🟡±.md
🖼🏛➕⚪±.md
🖼🏛➖⚫±.md
🖼🏛➖🟢±.md
🖼🏛➖🔵±.md
🖼🏛➖🟣±.md
🖼🏛➖🔴±.md
🖼🏛➖🟠±.md
🖼🏛➖🟡±.md
🖼🏛➖⚪±.md

DECK 38: 🖼🔨 (Restoration Functional)

🖼🔨🛒⚫±.md
🖼🔨🛒🟢±.md
🖼🔨🛒🔵±.md
🖼🔨🛒🟣±.md
🖼🔨🛒🔴±.md
🖼🔨🛒🟠±.md
🖼🔨🛒🟡±.md
🖼🔨🛒⚪±.md
🖼🔨🪡⚫±.md
🖼🔨🪡🟢±.md
🖼🔨🪡🔵±.md
🖼🔨🪡🟣±.md
🖼🔨🪡🔴±.md
🖼🔨🪡🟠±.md
🖼🔨🪡🟡±.md
🖼🔨🪡⚪±.md
🖼🔨🍗⚫±.md
🖼🔨🍗🟢±.md
🖼🔨🍗🔵±.md
🖼🔨🍗🟣±.md
🖼🔨🍗🔴±.md
🖼🔨🍗🟠±.md
🖼🔨🍗🟡±.md
🖼🔨🍗⚪±.md
🖼🔨➕⚫±.md
🖼🔨➕🟢±.md
🖼🔨➕🔵±.md
🖼🔨➕🟣±.md
🖼🔨➕🔴±.md
🖼🔨➕🟠±.md
🖼🔨➕🟡±.md
🖼🔨➕⚪±.md
🖼🔨➖⚫±.md
🖼🔨➖🟢±.md
🖼🔨➖🔵±.md
🖼🔨➖🟣±.md
🖼🔨➖🔴±.md
🖼🔨➖🟠±.md
🖼🔨➖🟡±.md
🖼🔨➖⚪±.md

DECK 39: 🖼🌹 (Restoration Aesthetic)

🖼🌹🛒⚫±.md
🖼🌹🛒🟢±.md
🖼🌹🛒🔵±.md
🖼🌹🛒🟣±.md
🖼🌹🛒🔴±.md
🖼🌹🛒🟠±.md
🖼🌹🛒🟡±.md
🖼🌹🛒⚪±.md
🖼🌹🪡⚫±.md
🖼🌹🪡🟢±.md
🖼🌹🪡🔵±.md
🖼🌹🪡🟣±.md
🖼🌹🪡🔴±.md
🖼🌹🪡🟠±.md
🖼🌹🪡🟡±.md
🖼🌹🪡⚪±.md
🖼🌹🍗⚫±.md
🖼🌹🍗🟢±.md
🖼🌹🍗🔵±.md
🖼🌹🍗🟣±.md
🖼🌹🍗🔴±.md
🖼🌹🍗🟠±.md
🖼🌹🍗🟡±.md
🖼🌹🍗⚪±.md
🖼🌹➕⚫±.md
🖼🌹➕🟢±.md
🖼🌹➕🔵±.md
🖼🌹➕🟣±.md
🖼🌹➕🔴±.md
🖼🌹➕🟠±.md
🖼🌹➕🟡±.md
🖼🌹➕⚪±.md
🖼🌹➖⚫±.md
🖼🌹➖🟢±.md
🖼🌹➖🔵±.md
🖼🌹➖🟣±.md
🖼🌹➖🔴±.md
🖼🌹➖🟠±.md
🖼🌹➖🟡±.md
🖼🌹➖⚪±.md

DECK 40: 🖼🪐 (Restoration Challenge)

🖼🪐🛒⚫±.md
🖼🪐🛒🟢±.md
🖼🪐🛒🔵±.md
🖼🪐🛒🟣±.md
🖼🪐🛒🔴±.md
🖼🪐🛒🟠±.md
🖼🪐🛒🟡±.md
🖼🪐🛒⚪±.md
🖼🪐🪡⚫±.md
🖼🪐🪡🟢±.md
🖼🪐🪡🔵±.md
🖼🪐🪡🟣±.md
🖼🪐🪡🔴±.md
🖼🪐🪡🟠±.md
🖼🪐🪡🟡±.md
🖼🪐🪡⚪±.md
🖼🪐🍗⚫±.md
🖼🪐🍗🟢±.md
🖼🪐🍗🔵±.md
🖼🪐🍗🟣±.md
🖼🪐🍗🔴±.md
🖼🪐🍗🟠±.md
🖼🪐🍗🟡±.md
🖼🪐🍗⚪±.md
🖼🪐➕⚫±.md
🖼🪐➕🟢±.md
🖼🪐➕🔵±.md
🖼🪐➕🟣±.md
🖼🪐➕🔴±.md
🖼🪐➕🟠±.md
🖼🪐➕🟡±.md
🖼🪐➕⚪±.md
🖼🪐➖⚫±.md
🖼🪐➖🟢±.md
🖼🪐➖🔵±.md
🖼🪐➖🟣±.md
🖼🪐➖🔴±.md
🖼🪐➖🟠±.md
🖼🪐➖🟡±.md
🖼🪐➖⚪±.md

DECK 41: 🖼⌛ (Restoration Time)

🖼⌛🛒⚫±.md
🖼⌛🛒🟢±.md
🖼⌛🛒🔵±.md
🖼⌛🛒🟣±.md
🖼⌛🛒🔴±.md
🖼⌛🛒🟠±.md
🖼⌛🛒🟡±.md
🖼⌛🛒⚪±.md
🖼⌛🪡⚫±.md
🖼⌛🪡🟢±.md
🖼⌛🪡🔵±.md
🖼⌛🪡🟣±.md
🖼⌛🪡🔴±.md
🖼⌛🪡🟠±.md
🖼⌛🪡🟡±.md
🖼⌛🪡⚪±.md
🖼⌛🍗⚫±.md
🖼⌛🍗🟢±.md
🖼⌛🍗🔵±.md
🖼⌛🍗🟣±.md
🖼⌛🍗🔴±.md
🖼⌛🍗🟠±.md
🖼⌛🍗🟡±.md
🖼⌛🍗⚪±.md
🖼⌛➕⚫±.md
🖼⌛➕🟢±.md
🖼⌛➕🔵±.md
🖼⌛➕🟣±.md
🖼⌛➕🔴±.md
🖼⌛➕🟠±.md
🖼⌛➕🟡±.md
🖼⌛➕⚪±.md
🖼⌛➖⚫±.md
🖼⌛➖🟢±.md
🖼⌛➖🔵±.md
🖼⌛➖🟣±.md
🖼⌛➖🔴±.md
🖼⌛➖🟠±.md
🖼⌛➖🟡±.md
🖼⌛➖⚪±.md

DECK 42: 🖼🐬 (Restoration Partner)

🖼🐬🛒⚫±.md
🖼🐬🛒🟢±.md
🖼🐬🛒🔵±.md
🖼🐬🛒🟣±.md
🖼🐬🛒🔴±.md
🖼🐬🛒🟠±.md
🖼🐬🛒🟡±.md
🖼🐬🛒⚪±.md
🖼🐬🪡⚫±.md
🖼🐬🪡🟢±.md
🖼🐬🪡🔵±.md
🖼🐬🪡🟣±.md
🖼🐬🪡🔴±.md
🖼🐬🪡🟠±.md
🖼🐬🪡🟡±.md
🖼🐬🪡⚪±.md
🖼🐬🍗⚫±.md
🖼🐬🍗🟢±.md
🖼🐬🍗🔵±.md
🖼🐬🍗🟣±.md
🖼🐬🍗🔴±.md
🖼🐬🍗🟠±.md
🖼🐬🍗🟡±.md
🖼🐬🍗⚪±.md
🖼🐬➕⚫±.md
🖼🐬➕🟢±.md
🖼🐬➕🔵±.md
🖼🐬➕🟣±.md
🖼🐬➕🔴±.md
🖼🐬➕🟠±.md
🖼🐬➕🟡±.md
🖼🐬➕⚪±.md
🖼🐬➖⚫±.md
🖼🐬➖🟢±.md
🖼🐬➖🔵±.md
🖼🐬➖🟣±.md
🖼🐬➖🔴±.md
🖼🐬➖🟠±.md
🖼🐬➖🟡±.md
🖼🐬➖⚪±.md

42 decks. 40 cards each. 1,680 zip codes. Every one accounted for. The ± is waiting for its operator.


for now this is the current version of the exercise library. it will for now stay as one file with the entire library.