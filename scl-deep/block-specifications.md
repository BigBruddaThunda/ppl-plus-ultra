---
title: SCL Block Specifications
category: scl-deep
status: WORKING DRAFT
planted: 2026-02-27
phase-relevance: Phase 2 (generation) + Phase 3 (Operis) + Phase 4 (experience layer)
depends-on:
  - scl-directory.md
  - CLAUDE.md
  - card-template-v2.md
  - seeds/operis-architecture.md
connects-to:
  - scl-deep/order-specifications.md
  - scl-deep/color-specifications.md
  - middle-math/weights/block-weights.md
  - seeds/content-types-architecture.md
---

# SCL Block Specifications — Deep Reference

## Preamble: Blocks as Rooms

A block is a room inside the workout card. The name is fixed. The content is not.

The same block — same emoji, same name — produces entirely different content depending on the zip code. 🧈 Bread & Butter in a ⛽ Strength session is a heavy compound lift. 🧈 Bread & Butter in a 🏟 Performance session is the test itself. 🧈 Bread & Butter in a 🖼 Restoration session is the main mobility or somatic sequence. The room is called the same thing. What happens inside changes completely.

This context-dependence is not ambiguity. It is the system's core insight: the block is a category of function, not a prescription of content. It names WHAT KIND of work is happening, not WHICH exercises appear.

---

## The Four Operational Functions

Every block belongs to one of four phases in the session arc:

| Function | Phase | What it does |
|----------|-------|--------------|
| **Orientation** | Opening | Arriving, focusing, pointing intent toward the work |
| **Access / Preparation** | Early | Mobility, activation, CNS priming, warming tissue |
| **Transformation** | Middle | Where capacity is built, tested, or expressed |
| **Retention / Transfer** | Close | Locking in patterns, cooling down, bridging forward |

The session arc: **Orient → Access → Transform → Retain**

Color modifiers can compress or expand any phase. ⚪ Mindful extends Orientation and Retention heavily. 🏟 Performance collapses Access and Retention to minimum viable, maximizing Transformation. ⚫ Teaching adds depth to Access at the cost of some Transformation volume.

---

## Always-Present vs. Conditional Blocks

**Always present (every address):**
- ♨️ Warm-Up — opens every session (or is preceded by 🎯 in 🖼 Restoration only)
- 🧈 Bread & Butter — the main work; always carries the most volume or the highest stimulus
- 🚂 Junction — always last before SAVE; the bridge forward
- 🧮 SAVE — the system closer; ends every session

**Conditional blocks** — activated by zip code context:
- ▶️ Primer: activated by ⛽/🏟 Order (CNS potentiation before max effort)
- 🔢 Fundamentals: activated by 🐂 Foundation or ⚫ Teaching contexts
- 🗿 Sculpt / 🪞 Vanity: activated by 🦋 Hypertrophy Order
- 🏗 Reformance: strongly activated by ⚖ Balance Order
- 🌋 Gutter: only valid in 🔴 Intense or 🪐 Challenge contexts — hard exclusions elsewhere
- 🎱 ARAM: activated by 🟠 Circuit Color
- All others: activated by specific Order × Axis × Type × Color combinations

---

## Per-Block Specifications

---

### ♨️ Warm-Up — Orientation / Access

**Role:** Always present. Always first (unless 🎯 precedes in 🖼 context). Prepares tissue, elevates heart rate, cues the nervous system for the work ahead.

**Always present:** Yes.

**Content rules:**
- *Goes inside:* Mobility drills, movement prep specific to the session's Type, low-intensity cardiovascular elevation, dynamic stretching, pattern rehearsal at sub-working loads
- *Never goes inside:* Working sets, PR attempts, heavy loading, anything that generates meaningful fatigue before the main work

**Context-dependence matrix:**

| Context | Warm-Up content |
|---------|----------------|
| 🐂 Foundation | Extended mobility, pattern introduction, movement vocabulary |
| ⛽ Strength | Focused CNS priming, pattern rehearsal at 40–60%, brief |
| 🦋 Hypertrophy | Blood flow emphasis, pump primers, tissue prep |
| 🏟 Performance | Efficient and targeted — just enough to reach working temp |
| 🌾 Full Body | Integration warm-up — movements that preview the unified pattern |
| ⚖ Balance | Corrective mobility targeting the session's specific gaps |
| 🖼 Restoration | 🖼 opens with 🎯 Intention; ♨️ is minimal or absent |
| ⚪ Mindful | Extended — becomes almost meditative; slow movement, breath work |
| 🔴 Intense | Abbreviated — high-intensity demands faster ramp, not longer |

**Set/rep patterns:** 1–2 circuits, 8–15 reps, no load or very light load. Duration: 5–12 minutes.

---

### 🎯 Intention — Orientation

**Role:** One sentence. Quoted. Active voice. Frames the work — does not hype it.

**Always present:** No. Strongest in 🖼 Restoration (where it opens the session before ♨️) and ⚪ Mindful contexts. Optional in other Orders when the coach wants to set explicit session focus.

**Content rules:**
- *Goes inside:* A single quoted sentence in active voice naming what the session is for
- *Never goes inside:* Motivational filler ("you got this"), clinical language, multiple sentences, future-tense promises

**Context-dependence matrix:**

| Context | Intention character |
|---------|-------------------|
| 🖼 Restoration | Opens the session. Somatic, reflective, inward. "Feel the difference between effort and tension." |
| ⚪ Mindful | Spacious and precise. "Move slowly enough to feel exactly where the resistance is." |
| ⛽ Strength | Brief technical focus. "Drive the floor away." |
| 🏟 Performance | The test framing. "This is what the training was for." |

**Format:** `🎯 INTENTION: "Your sentence here."`

---

### 🔢 Fundamentals — Access / Preparation

**Role:** Re-grounding in basics. Post-injury, post-layoff, teaching contexts. Rebuilds pattern literacy before loading.

**Always present:** No. Activated by 🐂 Foundation Order or ⚫ Teaching Color. Less common in other contexts.

**Content rules:**
- *Goes inside:* Foundational movement patterns at minimal load, coaching cues for technique, drill progressions that simplify the main movement
- *Never goes inside:* Working weight, advanced variations, any exercise requiring established skill baseline

**Context-dependence matrix:**

| Context | Fundamentals content |
|---------|---------------------|
| 🐂 Foundation | The session's primary access layer. Pattern naming. Vocabulary building. |
| ⚫ Teaching | Technique breakdown. Coach-heavy. Extended rest. Comprehension first. |
| Return from injury | Movement reassessment at minimal load before progressing |

**Set/rep patterns:** 3–5 exercises, 1–2 sets each, light load, long rest (coaching time). Duration: 10–15 minutes.

---

### 🧈 Bread & Butter — Transformation

**Role:** The main thing. Always present. Carries the most volume, the highest stimulus, or the primary test. The session exists to serve this block.

**Always present:** Yes.

**Content rules:**
- *Goes inside:* The primary compound movement(s) at working weight; the test in Performance; the main mobility sequence in Restoration
- *Never goes inside:* Warm-up exercises, corrective work, cool-down exercises — the content must match the session's transformation purpose

**Context-dependence matrix:**

| Context | Bread & Butter content |
|---------|----------------------|
| ⛽ Strength | Heavy compound lift(s). 3–5 sets × 4–6 reps. Full rest (3–4 min). This is the session's purpose. |
| 🦋 Hypertrophy | 3–4 compound exercises × 3–4 sets × 8–12 reps. Pump is the goal. |
| 🏟 Performance | THE TEST ITSELF. Nothing before or after adds load. 1–3 attempts, full rest, record, leave. |
| 🌾 Full Body | The integrated compound movement that unifies the session. Must flow. |
| ⚖ Balance | Targeted accessory compounds addressing the specific gap (e.g., ⚖🪡 = bicep curls, face pulls, forearm work). |
| 🖼 Restoration | The main mobility or somatic sequence. Not a lift. Not a test. Active recovery or deep tissue work. |
| 🐂 Foundation | Sub-maximal compound work with pattern emphasis. Load is a teaching tool. |

**Set/rep patterns:** Highly variable by Order. See per-Order specifications in scl-deep/order-specifications.md.

---

### 🫀 Circulation — Access / Preparation

**Role:** Blood flow, tissue prep. Early or mid-session. Heart rate elevation and peripheral circulation before main work.

**Always present:** No. Most useful in 🦋 Hypertrophy and 🌾 Full Body contexts. Less common in 🏟 Performance (too much fatigue before test).

**Content rules:**
- *Goes inside:* Low-intensity cardio, sled walks, light cycling, jumping jacks, movement flows that elevate heart rate without creating fatigue
- *Never goes inside:* Heavy compound work, max-effort anything, exercises that would compromise the main work

**Context-dependence matrix:**

| Context | Circulation content |
|---------|-------------------|
| 🦋 Hypertrophy | Pump-focused prep. 5–8 minutes of light cardio or bodyweight movement. |
| 🌾 Full Body | Integrative movement that previews the session's unified pattern. |
| 🖼 Restoration | Gentle movement to start circulation without stress load. |

---

### ▶️ Primer — Access / Preparation

**Role:** CNS activation. Bridges warm-up to main work. Neural potentiation — signals the nervous system that heavy work is coming.

**Always present:** No. Strongly activated by ⛽ Strength and 🏟 Performance Orders.

**Content rules:**
- *Goes inside:* Low-volume, high-intent movements that activate the specific motor patterns needed for the main work (speed deadlifts, jump squats, plyo push-ups, medicine ball throws), activation supersets
- *Never goes inside:* Volume work, grinding reps, anything creating meaningful fatigue

**Context-dependence matrix:**

| Context | Primer content |
|---------|---------------|
| ⛽ Strength | Speed work at 40–60%: 3×2 speed deadlifts before heavy deadlift. PAP (post-activation potentiation). |
| 🏟 Performance | The jump from warm-up to test weight. Activation patterns. 🪜 Progression often precedes this. |
| 🪐 Challenge | Explosive movements matching the session's challenge character. |

**Set/rep patterns:** 2–3 sets × 2–4 reps, short rest (60–90s). Duration: 5–8 minutes.

---

### 🎼 Composition — Transformation

**Role:** Movement arrangement. The composite header block. Strong in 🌾 Full Body — where movements must be arranged into a unified flowing pattern.

**Always present:** No. Primary activation: 🌾 Full Body Order.

**Content rules:**
- *Goes inside:* The arrangement logic for a full-body integrated movement. Not individual exercises but the sequencing logic that makes them flow as one.
- *Never goes inside:* Exercises that require a full reset between them (if a reset is needed, it's a superset, not 🌾 Full Body composition)

**Context-dependence matrix:**

| Context | Composition content |
|---------|-------------------|
| 🌾 Full Body | The integration header. Describes the unified pattern before exercises are listed. Must pass Flow Test and Unity Test. |
| ⌛ Time × 🌾 | The timed version: AMRAP of the unified pattern, or EMOM with the pattern as the unit. |

**Flow and Unity Tests (🌾 only):** (1) Does one movement flow into the next without a reset? (2) Is the result a single unified pattern, not a sequence of movements? Both must be yes. Thrusters pass. Squat-then-row-as-separate-movements fails.

---

### ♟️ Gambit — Access / Transformation

**Role:** Deliberate sacrifice for positional advantage. Pre-fatigue with purpose — a targeted prefatigue strategy that enhances the main work's effectiveness.

**Always present:** No. Activated by 🌹 Aesthetic contexts (pre-exhaustion technique) and 🔴 Intense.

**Content rules:**
- *Goes inside:* Isolation exercise performed before its compound partner to prefatigue the target muscle (cable fly before bench press; leg extension before squat). The sacrifice is real — the main work is compromised somewhat — but the target muscle's relative activation increases.
- *Never goes inside:* Random fatigue with no strategic rationale. The gambit must be connected to the main work that follows.

**Context-dependence matrix:**

| Context | Gambit content |
|---------|---------------|
| 🌹 Aesthetic | Pre-exhaustion protocol. Isolation → compound. The isolating exercise makes the compound more selective. |
| 🔴 Intense | Pre-fatigue + high volume. Greater total stimulus. |

---

### 🪜 Progression — Access / Transformation

**Role:** Loading ramps. Ladders. In 🏟 Performance: the ramp to the test.

**Always present:** No. Activated by 🏟 Performance (essential) and 🔵 Structured (prominent).

**Content rules:**
- *Goes inside:* Ramping sets at increasing loads (e.g., 135×5 → 185×3 → 225×2 → 275×1 → 315 test), progressive volume ladders, intensity progressions
- *Never goes inside:* Working sets at final load (those belong in 🧈), back-off sets (those belong in 🧩)

**Context-dependence matrix:**

| Context | Progression content |
|---------|-------------------|
| 🏟 Performance | The essential ramp to the test. Without this, the test is dangerous. |
| 🔵 Structured | Weekly progressive overload logic: adds load or reps from last session. |
| ⛽ Strength | Loading pyramid before top sets. |

---

### 🌎 Exposure — Transformation

**Role:** Reveal weaknesses under controlled stress. Expand movement vocabulary. Bring the athlete into contact with unfamiliar demands.

**Always present:** No. Activated by 🟡 Fun, ⚖ Balance, and ⚫ Teaching contexts.

**Content rules:**
- *Goes inside:* New movement patterns, unfamiliar implements, challenging positions, movements that are deliberately outside the athlete's comfort zone but within their control
- *Never goes inside:* Max-effort work in unfamiliar patterns (injury risk), exercises the athlete cannot safely execute

**Context-dependence matrix:**

| Context | Exposure content |
|---------|----------------|
| 🟡 Fun | Exploration. New equipment, unusual angles, movements the athlete has never tried. Stakes are low. |
| ⚖ Balance | Targeted exposure to specific weakness — the movement that exposes the gap. |
| ⚫ Teaching | Safe introduction to unfamiliar patterns with coaching support. |

---

### 🎱 ARAM — Transformation

**Role:** Station-based loops. Circuit structure. Each station must change which tissue is working.

**Always present:** No. Primary activation: 🟠 Circuit Color.

**Content rules:**
- *Goes inside:* A complete circuit where each station works a different muscle group or energy system. Format: station A → B → C → D → back to A. Each transition is a tissue recovery.
- *Never goes inside:* Two adjacent stations targeting the same muscle group (violates loop logic). Barbells (🟠 blocks barbells).

**Loop logic rule:** Every station must change which tissue is working. No two adjacent stations target the same muscle group. A circuit is not a list of exercises done quickly — it is a deliberate tissue-rotation loop where each station recovers while others work.

**Markdown format:** Box notation showing the loop.

**Context-dependence matrix:**

| Context | ARAM content |
|---------|-------------|
| 🟠 Circuit | The primary block. Replaces 🧈/🧩 in Circuit addresses. The whole session is the loop. |
| ⌛ Time | Timed circuit with AMRAP character. |

---

### 🌋 Gutter — Transformation

**Role:** All-out effort. The maximum output block. Rare and specific.

**Always present:** No. Hard exclusions apply.

**Hard exclusion rule:** 🌋 Gutter NEVER appears in:
- 🖼 Restoration — hard rule
- 🐂 Foundation — hard rule
- ⚪ Mindful — hard rule

**Activation conditions:** Only valid in 🔴 Intense or 🪐 Challenge contexts.

**Content rules:**
- *Goes inside:* Maximum effort sets, AMRAPs to failure, last-set intensity techniques (drop sets in 🔴, paused maximums in 🪐), the true all-out moment of the session
- *Never goes inside:* Technique work, educational content, volume accumulation at moderate intensity

**Context-dependence matrix:**

| Context | Gutter content |
|---------|---------------|
| 🔴 Intense | Cathartic all-out volume. Drop sets, rest-pause, AMRAP finisher. Stress OUT. |
| 🪐 Challenge | Maximum controlled effort. The hardest variation the athlete can sustain with form. |

---

### 🪞 Vanity — Transformation

**Role:** Appearance-driven work. Pump work. Mirror muscles. Honest. Stigma-free.

**Always present:** No. Primary activation: 🦋 Hypertrophy Order.

**Content rules:**
- *Goes inside:* Isolation work targeting muscles the athlete wants to develop visually — bicep curls, lateral raises, calf raises, ab work. Honest about what it is.
- *Never goes inside:* Compound strength work (that's 🧈), corrective work (that's 🏗), assessment (that's 👀)

**Context-dependence matrix:**

| Context | Vanity content |
|---------|---------------|
| 🦋 Hypertrophy | The pump block. 3–4 isolation exercises × 3 sets × 12–15 reps. Short rest. |
| 🌹 Aesthetic | The honest appearance block — full ROM isolation with mind-muscle connection emphasis. |

**Suppression:** 🏟 Performance (-8). The urge to add pump work after a test is wrong. Resist it.

---

### 🗿 Sculpt — Transformation

**Role:** Hypertrophy shaping. Carving not admiring. Angles, tension, volume. Differs from 🪞 in that it's about engineering specific shapes, not general pump.

**Always present:** No. Primary activation: 🦋 Hypertrophy Order.

**Content rules:**
- *Goes inside:* Targeted hypertrophy work at specific angles designed to develop specific shapes — cable lateral raises for width, incline curls for bicep peak, decline flyes for chest sweep
- *Never goes inside:* Compound strength work, cardio, corrective exercises

**Context-dependence matrix:**

| Context | Sculpt content |
|---------|---------------|
| 🦋 Hypertrophy | Follows 🧈 with more specific angle work. 3 × 10–15. |
| 🌹 Aesthetic | The shaping block — where the muscle's visual profile is developed deliberately. |

---

### 🛠 Craft — Transformation

**Role:** Skill acquisition. Quality over load. The workshop block.

**Always present:** No. Activated by ⚫ Teaching and 🟣 Technical colors, and 🐂 Foundation Order.

**Content rules:**
- *Goes inside:* Skill-building work at reduced load — the same exercises as the main work but with emphasis on technical mastery. Video review. Cue application. Pattern drilling.
- *Never goes inside:* Max-effort work, high volume, anything that prioritizes production over learning

**Context-dependence matrix:**

| Context | Craft content |
|---------|--------------|
| ⚫ Teaching | Coaching-heavy technique work. The session's educational core. |
| 🟣 Technical | Precision focus. Lower reps, longer rest, quality above quantity. |
| 🐂 Foundation | Pattern drilling at sub-maximal load. Learning the movement before owning it. |

---

### 🧩 Supplemental — Transformation

**Role:** Secondary work. Supports 🧈. Must be non-redundant — different angles, different stimulus, different tissue emphasis.

**Always present:** No. Common in ⛽ Strength and 🦋 Hypertrophy.

**Content rules:**
- *Goes inside:* Accessory exercises that support the primary movement — Romanian deadlift after deadlift, rear delt work after rows, tricep extensions after bench, front squat after back squat
- *Never goes inside:* Repetition of the same movement pattern as 🧈 at the same angle (that's just more 🧈 volume, which should be in 🧈); corrective work (that's 🏗)

**Non-redundancy rule:** If 🧩 uses the same primary movement pattern as 🧈, it violates the supplemental purpose. The work must address a different angle or secondary muscle group.

**Context-dependence matrix:**

| Context | Supplemental content |
|---------|---------------------|
| ⛽ Strength | Accessory compounds. RDL after deadlift. Rows after bench. |
| 🦋 Hypertrophy | Volume accumulation at secondary angles. Can superset in 🔴 context. |
| 🌾 Full Body | Additional integrated patterns that support the main composition. |

---

### 🪫 Release — Retention / Transfer

**Role:** Context-dependent. The direction depends entirely on the zip code. The block name is fixed. What it does is not.

**Always present:** No. Common in ⛽ Strength, 🦋 Hypertrophy, 🖼 Restoration, ⚪ Mindful.

**The three directions:**

| Color/Order context | Release direction |
|--------------------|------------------|
| 🔴 Intense | Cathartic discharge. Stress OUT. The tension built during the session releases: stretching, shaking, breathwork, contrast showers. Active processing of accumulated CNS load. |
| ⚪ Mindful | Parasympathetic downregulation. Tension DOWN. Slow, deliberate calming — deep breathing, progressive relaxation, long static holds. The body returns to parasympathetic baseline. |
| 🖼 Restoration | Somatic return to baseline. The body reclaims its resting state after intentional somatic work. Not discharge, not downregulation — return. |
| General (⛽/🦋) | Transition between training and recovery. Light stretching, tissue work, controlled breathing. Bridges the session to the post-training period. |

**Content rules:**
- *Goes inside:* Stretching, mobility work, breathing exercises, foam rolling, light movement, contrast protocols (🔴 context)
- *Never goes inside:* Working sets, loading, any exercise that creates new training stimulus

---

### 🏖 Sandbox — Transformation

**Role:** Constrained exploration. Structured play within the zip code's parameters.

**Always present:** No. Activated by 🟡 Fun and ⚫ Teaching colors.

**Content rules:**
- *Goes inside:* Bounded choice — the athlete picks from a defined set of valid options. The options must all be valid for the current zip code. The session explores rather than executes a fixed prescription.
- *Never goes inside:* Unbounded choice (must be constrained), exercises outside the zip code's valid parameters

**Context-dependence matrix:**

| Context | Sandbox content |
|---------|----------------|
| 🟡 Fun | Play. Exploration. Variety. New things tried within the session's constraints. Low stakes. |
| ⚫ Teaching | Safe learning space. The athlete experiments with form variations under coaching supervision. |
| 🟣 Technical | Skill testing — trying the movement at new angles or with new implements to probe competence. |

---

### 🏗 Reformance — Transformation

**Role:** Corrective construction. Prehab, postural correction, gap-filling.

**Always present:** No. Primary activation: ⚖ Balance Order (near-mandatory here).

**Content rules:**
- *Goes inside:* Exercises targeting identified weaknesses, postural corrections, prehab protocols — glute activation for knee valgus, rotator cuff work for shoulder health, core stability for lower back
- *Never goes inside:* Aesthetic pump work, strength work, conditioning

**Context-dependence matrix:**

| Context | Reformance content |
|---------|------------------|
| ⚖ Balance | The session's primary mechanism. ⚖ is about correction — 🏗 is where the correction happens. |
| 🐂 Foundation | Post-injury or return-to-training correction layer. |
| General prehab | Appears when the coach identifies a gap that needs direct structural work. |

---

### 🧬 Imprint — Retention

**Role:** Locking in patterns. High rep, low load, late session. Neural memory consolidation.

**Always present:** No. Strong in 🐂 Foundation and 🖼 Restoration.

**Content rules:**
- *Goes inside:* High-rep, very low load repetitions of the session's primary patterns — 20–30 reps of goblet squats after a squat session, band pull-aparts after a pull session, banded hip extensions after a leg session
- *Never goes inside:* Heavy loading, new movement patterns not already used in the session

**The imprint rationale:** The last repetitions of a training session have disproportionate influence on motor memory consolidation. High-rep, low-load pattern repetition at the session's close drives the neural pattern deeper.

**Context-dependence matrix:**

| Context | Imprint content |
|---------|----------------|
| 🐂 Foundation | 20–30 reps of the session's primary pattern at minimal load. Lock in the movement. |
| 🖼 Restoration | Gentle repetition of somatic patterns — the body re-learning its resting baseline. |

---

### 🚂 Junction — Retention / Transfer

**Role:** Bridge to next session. The transfer block. Always last before 🧮 SAVE.

**Always present:** Yes.

**Content rules:**
- *Goes inside:* 1–3 suggested follow-up zip codes with rationale, logging space, notes on session performance, what to carry forward
- *Never goes inside:* Additional exercise, working sets, anything that adds training load

**Required format:**
```
Next → [zip code] — [one-line reason]
Next → [zip code] — [one-line reason]
[Logging space: _____________]
```

**The Junction rationale:** The workout doesn't end when the last rep is done. It ends when the athlete knows where they're going next. The Junction names the next address and explains why — creating continuity between sessions that would otherwise be isolated events.

---

### 🔠 Choice — Modifier

**Role:** Bounded autonomy. A modifier that applies to other blocks, not a standalone transformation block.

**Always present:** No. Activated by 🟡 Fun and ⚫ Teaching colors.

**Usage:** 🔠 Choice modifies another block by offering the athlete a selection of valid options rather than a fixed prescription. `🔠 Choice / 🧈 Bread & Butter` means: the athlete chooses one of the listed primary exercises.

**Content rules:**
- *Goes inside:* A bounded list of options. Every option must be valid for the current zip code. The choices constrain; they do not liberate into anything-goes.
- *Never goes inside:* Exercises outside the zip code's parameters, unbounded "do whatever you want"

---

### 🧮 SAVE — System Operator

**Role:** Session complete. Log data. Archive. Closing ritual. Every workout ends here.

**Always present:** Yes. Final block of every session, after 🚂 Junction.

**Content rules:**
- *Goes inside:* A 1–2 sentence closing principle that transfers the work forward. The work done, the pattern embedded, the session's contribution to the larger arc.
- *Never goes inside:* Praise. Motivational filler. "You crushed it." The SAVE transfers; it does not congratulate.

**The SAVE principle:** Transfer the work, do not praise the user. The closing sentence looks forward, not at the session. It speaks to a competent adult who does not need to be managed.

**Format:**
```
🧮 SAVE
[1–2 sentence closing principle.]
```

---

## Block Sequence Guidelines by Order

From scl-directory.md and CLAUDE.md:

```
🐂 Foundation:   4–6 blocks  ♨️ 🔢/🛠 🧈 🧩 🧬 🚂 🧮
⛽ Strength:     5–6 blocks  ♨️ ▶️ 🧈 🧩 🪫 🚂 🧮
🦋 Hypertrophy:  6–7 blocks  ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂 🧮
🏟 Performance:  3–4 blocks  ♨️ 🪜 🧈 🚂 🧮  (no junk volume — ever)
🌾 Full Body:    5–6 blocks  ♨️ 🎼 🧈 🧩 🪫 🚂 🧮
⚖ Balance:      5–6 blocks  ♨️ 🏗 🧈 🧩 🪫 🚂 🧮
🖼 Restoration:  4–5 blocks  🎯 🪫 🧈 🧬 🚂 🧮
```

**Color modifiers on block structure:**
- ⚫ Teaching: extended rest throughout, 🛠 Craft emphasis, comprehension before exertion
- 🟢 Bodyweight: equipment collapses to tier 0–2 across all blocks
- 🔵 Structured: 🪜 Progression prominent in 🧈
- 🟣 Technical: fewer total blocks, extended rest, quality over count
- 🔴 Intense: 🧩 may superset with 🧈, 🌋 Gutter possible late
- 🟠 Circuit: 🧈/🧩/🪞 merge into single 🎱 ARAM block
- 🟡 Fun: 🏖 Sandbox and 🌎 Exposure permitted
- ⚪ Mindful: extended ♨️ and 🪫, slow tempo throughout, 🎯 Intention recommended

---

*scl-directory.md is the operational reference. This document specifies the rules behind the blocks, not the blocks themselves.*

🧮
