---
planted: 2026-03-09
status: SEED — DLC
phase-relevance: Phase 5–7 (User Experience, Almanac, Community)
blocks: nothing currently — character creator and personalization layer
depends-on: scl-directory.md, seeds/abacus-architecture.md, middle-math/weights/operator-weights.md, scl-deep/operator-specifications.md
connects-to: seeds/digital-city-architecture.md, seeds/experience-layer-blueprint.md, seeds/almanac-calendar-architecture.md, middle-math/ARCHITECTURE.md (Section 7), seeds/outside-system-v2-architecture.md, seeds/cathedral-cup-architecture.md
legacy-sources: THE OUTSIDE SYSTEM v0.4.pdf, THE HERO'S ALMANAC v7.0.pdf, THE FARMER'S ALMANAC v4.0.pdf
---

# The Hero's Almanac v8 — Character Creator Architecture

## Section 1 — Thesis

The Hero's Almanac v8 is an optional character creator built on the 61 SCL. It produces a 61-dimensional personal weight vector using the same math (octave scale, cosine similarity) that already drives zip-code weight vectors, envelope retrieval, and exercise selection. The Almanac is the cold-start onboarding layer. The exercise ledger is the warm-data layer. The Almanac's influence decays as logged data accumulates.

Where you start is not where you end.

The infrastructure already exists: `middle-math/weight-vectors.json` (1,680 zip-code vectors on 61 dimensions), `envelope_retrieval.py` (cosine similarity matching), `middle-math/weights/operator-weights.md` (12 operator affinity profiles), `middle-math/abacus-profiles/` (35 program archetype contexts). The Almanac adds a personal vector to the same bus. Everything else — archetype matching, House sorting, abacus recommendation, community role emergence, XP accumulation — falls out of the math that's already built.

---

## Section 2 — The 7 Dares

Seven assessment chapters, one per Order. Each Dare explores the user's relationship with that Order's developmental phase. Each Dare contains 61 questions — one per SCL emoji dimension. Questions are human-readable, pass the grandma test, and do not expose SCL internals to the user.

7 Dares × 61 questions = **427 total questions.**

Dare naming follows the publication standard — informational, no hype, no fantasy taxonomy. Working names only in this seed (final names require cosmogram research and publication standard proofing).

### Dare structure per Order

**🐂 Foundation Dare** — Relationship with learning, patience, sub-maximal work, coaching. How do you approach something new? Do you slow down to learn or push through to perform? What is your relationship with being coached?

**⛽ Strength Dare** — Relationship with heavy loads, force, neural focus, barbell comfort. How do you feel about maximum effort? Is the barbell a tool or a barrier? Do you chase numbers or avoid them?

**🦋 Hypertrophy Dare** — Relationship with volume, aesthetic goals, muscle growth, time-under-tension. Do you train for appearance? How do you feel about the pump? Is the mirror a training tool or a distraction?

**🏟 Performance Dare** — Relationship with testing, competition, peak effort, benchmarks. Do you test yourself? How do you handle performance anxiety? Are benchmarks motivating or threatening?

**🌾 Full Body Dare** — Relationship with integration, flow, compound movement, functional unity. Do you prefer isolation or integration? How do you feel about complex movement sequences? Does training need to feel like training?

**⚖ Balance Dare** — Relationship with correction, asymmetry, detail, weakness. Do you address weaknesses or avoid them? How much patience do you have for corrective work? Can you tolerate unglamorous training?

**🖼 Restoration Dare** — Relationship with recovery, rest, nervous system, slowing down. Do you rest or do you feel guilty resting? Is recovery a priority or an afterthought? How do you relate to stillness?

Each emoji dimension gets scored from 7 different developmental angles across the 7 Dares. The final personal vector value for each dimension is a blend of all 7 scores.

---

## Section 3 — The Two-Layer Answer System

Each of the 427 questions has two response layers:

### Layer 1 — The Answer

A/B/C/D multiple choice or Yes/No binary. Determines the directional weight adjustment on the corresponding emoji dimension. Answer maps to a value between **-4 and +4** on the octave scale.

### Layer 2 — The Importance Flag

**➕ or ➖**: "Is this dimension important to you or not?"

Independent of the answer content. The importance flag controls how much the answer matters to the overall profile:
- ➕ = full weight multiplier (1.0)
- Neutral/blank = default multiplier (0.5)
- ➖ = reduced multiplier (0.25)

### Scoring Formula

```
user_vector[emoji_index] += answer_weight × importance_multiplier
```

Vector clamped to **[-8, +8]** per dimension after all 7 Dares process. Same emoji scored 7 times from 7 developmental angles — the final value is a blend.

### Partial Completion

Partial completion supported. Unanswered dimensions default to population-median values. More answers = sharper profile = more precise recommendations. Fewer answers still produce a usable profile. The system degrades gracefully.

---

## Section 4 — The 12 Houses (Operators as Guilds)

The 12 operators function as 12 sorting-hat Houses — independent philosophical-action identities.

**Critical distinction:** Operators are NOT locked to calendar months. The month mapping in `seeds/almanac-macro-operators.md` is one specific use of operators in one specific context (the Operis ambient filter). In the Almanac, operators are guilds. These two functions must never be conflated.

### House Sorting Mechanism

After the 7 Dares produce a personal vector, the system computes cosine similarity between the user's vector and all 12 operator weight profiles (from `middle-math/weights/operator-weights.md`). The highest-similarity operator is the user's primary House.

### Working House Names

(Require publication standard proofing and cosmogram-derived naming in future passes)

| Emoji | Latin | Working Name | Character |
|-------|-------|-------------|-----------|
| 📍 | pono | The Architects | Position, setup, proven ground |
| 🧲 | capio | The Receivers | Absorb, assess, intake before acting |
| 🧸 | fero | The Carriers | Transfer, bridge, connect domains |
| 👀 | specio | The Observers | See, detect, precision of form |
| 🥨 | tendo | The Extenders | Push limits, stretch boundaries |
| 🤌 | facio | The Executors | Do the work, produce, perform |
| 🚀 | mitto | The Launchers | Commit fully, max attempt, send |
| 🦢 | plico | The Layerers | Compound, fold, superset, synthesize |
| 🪵 | teneo | The Anchors | Hold, persist, maintain under pressure |
| 🐋 | duco | The Conductors | Orchestrate, manage systems, macro view |
| ✒️ | grapho | The Scribes | Document, log, prescribe, record |
| 🦉 | logos | The Interpreters | Reason, analyze, find meaning in data |

### Multi-Classing

Cosine similarity against all 12 operators produces a ranked list:
- **Primary House** = highest match
- **Secondary House** = second-highest
- **Tertiary House** = third-highest

Multi-class blend influences abacus recommendations and community identity.

### Math Check

Each operator is the default for exactly 140 zip codes (1 Axis × 4 Colors × 5 Types × 7 Orders = 140). 12 × 140 = 1,680. Clean coverage. The operator distribution is perfectly uniform across the system.

---

## Section 5 — 1,680 Archetypes

The user's personal weight vector is computationally identical to a zip-code weight vector. Cosine similarity between the personal vector and all 1,680 zip-code vectors produces a ranked list. The #1 match is the user's archetype — their home room.

**The archetype IS a zip-code address.**

1,680 archetypes × 12 Houses = **20,160 total identity combinations** (the theoretical ceiling). Users experience this as: base archetype (zip code) + dominant House (operator). The combination produces training character without requiring the user to understand the math.

### Archetype Naming

Deferred. Archetype names should emerge from cosmogram research and deck identity documents. Each archetype name is a zip code's identity expressed as a character trait, grounded in real cultural tradition per the publication standard.

---

## Section 6 — XP as Vector Accumulation

Every action in Ppl± generates zip-code-specific data that feeds back into the user's personal vector. This is not gamification XP — it is the natural weight of experience accumulating on specific SCL dimensions.

Actions that adjust the vector:
- Logging a workout
- Exploring a room
- Completing a color
- Reading an Operis
- Contributing community content

### Mechanism

Each logged action adjusts the relevant emoji dimensions of the personal vector by small increments (scale TBD). Over time, the warm ledger data outweighs the cold Almanac data. The personal vector evolves. The archetype can shift. The abacus recommendations adjust. The system grows with the user.

The abacus math turns because the user turns it. Personal vector changes → cosine similarity shifts against all 1,680 rooms and 35 abacus profiles → recommendations evolve → new rooms open, stale ones recede.

---

## Section 7 — Community Role Emergence

Users whose personal vectors have high cosine similarity to specific zip-code rooms become natural leaders of those rooms' community threads. Not appointed — emergent from the math.

When a room's turn comes in the Operis rotation, its highest-affinity users' contributions surface first.

### House-Based Functional Roles

House-based sub-groups within a zip-code community create organic functional roles:
- The **facio** contingent leads execution content
- The **specio** contingent leads form-check threads
- The **grapho** contingent maintains the knowledge base
- The **logos** contingent leads analysis and interpretation

Nobody is assigned. The sorting produces social architecture.

Each user's ranked list of all 1,680 rooms is unique. The buildings are shared infrastructure. The streets you walk are your own architectural vernacular.

---

## Section 8 — Intercolumniation

The intercolumniation layer (the space between sessions) becomes part of the user profile. Recovery capacity is computable from Almanac baseline data (sleep, stress, age, injury history, training frequency) and refined by logged data (performance changes with different rest intervals).

### Three Systems Modified

1. **Rotation engine** — bias toward lower-CNS Orders when recovery is low
2. **Abacus bonus pool** — surface more 🖼 recovery alternatives for slow-recovery profiles
3. **Exercise selection** — prevent high-overlap muscle group loading on consecutive sessions

### Schema Fields Needed

Future exercise library schema expansion should add per-exercise fields:
- `cns_load` (1–5 scale of central nervous system demand)
- `primary_recovery_group` (which muscle groups need recovery time)
- `recovery_hours_estimate` (minimum hours before the same movement pattern should be loaded again)

These fields feed the intercolumniation engine. See also: the intercolumniation section appended to `seeds/abacus-architecture.md`.

---

## Section 9 — Integration Points

The Almanac connects to existing systems without requiring new computational paradigms:

| System | File | Integration |
|--------|------|-------------|
| Envelope retrieval | `envelope_retrieval.py` | Personal vector used as query vector for content matching |
| Exercise selector | `exercise_selector.py` | Personal vector adjusts exercise affinity scoring |
| Abacus profiles | `middle-math/abacus-profiles/` | Cosine similarity for program recommendation |
| Rotation engine | `seeds/default-rotation-engine.md` | Intercolumniation filter on daily suggestions |
| Weight vectors | `middle-math/weight-vectors.json` | Archetype matching via existing 61-dim cosine similarity |
| Operator weights | `middle-math/weights/operator-weights.md` | House sorting via existing affinity profiles |

No new math engine required. The infrastructure exists. The Almanac adds a personalization vector that plugs into the existing bus.

---

## Section 10 — What This Is Not

- **Not mandatory.** Every feature has a default-mode fallback for users who skip the Almanac.
- **Not gamification.** XP is vector weight, not points. Houses are philosophical orientations, not factions. Archetypes are zip-code addresses, not fantasy classes.
- **Not a replacement for the exercise ledger.** The Almanac provides cold-start identity. The ledger provides warm identity. The system blends with increasing ledger weight.
- **Not a locked identity.** Where you start is not where you end. The personal vector evolves with every action.
- **Not active scope.** This is DLC. It needs serious rework on question mapping, naming conventions (publication standard proofing), and functional design passes before it touches the architecture.

---

## Section 11 — Legacy PDF Context

Three documents predate the current 61 SCL architecture. Their conceptual DNA is preserved in this seed:

| Legacy Concept | v8 Destination |
|---------------|----------------|
| Character creator with PAR-Q, goals, stats, archetype system | Section 2–3 (7 Dares, two-layer answers) |
| Octave logic | Preserved as the -8 to +8 bipolar weight scale (already in the system per `middle-math/ARCHITECTURE.md` Section 7) |
| 7 Dares structure | Rebuilt on the 7 Orders with 61 questions per Dare |
| Wilson AI personality layer | Deferred (referenced in `seeds/wilson-voice-identity.md`) |
| r/outside real-world activity logging | Deferred (see `seeds/outside-system-v2-architecture.md`) |
| Cathedral Cup / Vitruvian Games competitive layer | Deferred (see `seeds/cathedral-cup-architecture.md`) |
| Farmer's Almanac daily calendar | Already seeded in `seeds/almanac-calendar-architecture.md` |

Implementation details, data models, exercise libraries, and UI flows from these PDFs are not carried forward. They predate the architecture. Only concepts are preserved and rebuilt on the current 61 SCL foundation.

---

## Section 12 — Open Questions for Future Design Passes

1. **Question mapping:** How do 61 questions per Dare translate to human-readable prompts that pass the grandma test? This is the hardest design problem and needs dedicated sessions.

2. **Naming conventions:** All House names and archetype names need publication standard proofing. Working names in this seed are placeholders.

3. **Functional flow:** How does the character creator UI feel? Quiz? Visual selector? Narrative journey? This needs mobile UI sketching.

4. **Scoring calibration:** What's the right answer_weight range? What's the right importance_multiplier scale? Needs playtesting.

5. **Population-median defaults:** What are the baseline values for unanswered dimensions? Needs data or reasonable assumptions.

6. **XP increment scale:** How much does a single logged workout adjust the personal vector? Too much = volatile identity. Too little = no evolution. Needs tuning.

7. **Intercolumniation decay model:** How does recovery capacity change with training age, seasonal context, life stress? Sports science consultation needed.

8. **Community role thresholds:** At what cosine similarity level does a user become a "natural leader" of a room? How many leaders per room? Needs community design thinking.

9. **House visual identity:** Each House needs a visual register (color, typography, iconography) that maps to the existing design token system. Needs art direction.

10. **Operator-as-House vs. operator-as-month:** The system now has operators serving two functions — guild identity (Almanac) and ambient monthly filter (Operis). These must not be conflated. Documentation needs to be explicit about which context applies where.

---

🧮
