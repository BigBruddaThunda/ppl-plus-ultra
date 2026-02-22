# Zip-Web Rules — Complete Specification

This is the single source of truth for how zip-web pods are constructed. All agents (Claude Code, Codex, Ralph) read this file before generating pod content.

---

## Core Principle

Every zip code is a standalone workout. Every zip code is also a hub in a web. Each hub has exactly 4 outgoing directional edges (N/E/S/W). Each edge points to a zip code of a **different Type** than the hub. The hub plus its 4 neighbors form a pod — 5 workouts covering all 5 Types.

---

## The Type Exclusion Rule — HARD CONSTRAINT

If the main zip's Type is X, then N, W, S, and E must each be a different Type from the remaining 4.

- All 4 non-hub Types must appear **exactly once** across the 4 directions
- No Type may appear twice in N/E/S/W
- The hub Type **may not appear** in N/E/S/W

**Example:**
Main zip = ⛽🏛🛒🔵 (Type = 🛒 Push)
N/E/S/W must collectively contain exactly one 🪡, one 🍗, one ➕, one ➖.
The assignment of which Type goes to which direction is determined by coaching logic (see below).

**Validation:** Before writing any pod, verify the pod Types string. Format: `[hub] + [N] + [E] + [S] + [W]` must contain each of the 5 Types exactly once.

---

## The Directional Character

Each direction carries a specific coaching rationale. The content of each slot must honor its direction's character.

### N — Progression
The workout that builds directly on what the hub created. It capitalizes on the neural, muscular, or metabolic state the hub zip produced.

- If the hub was heavy compound bilateral, N might be the same movement pattern at a slightly reduced Order to consolidate the pattern
- If the hub trained a specific muscle group intensely, N might train that group's antagonist at matched intensity
- N is what a smart trainer programs as your next session if the goal is forward momentum in your training arc
- N should NOT be a step backward in intensity or difficulty

**Key signal:** N asks "what does this session set up well?"

### E — Balance
The workout that addresses what the hub neglected or exposed.

- If the hub was bilateral, E might be unilateral
- If the hub was high CNS, E might be moderate CNS
- If the hub was heavy barbell, E might be bodyweight or cable
- E fills gaps. It's the complementary session the hub was silently asking for
- E brings the system back toward equilibrium across planes, load, and training character

**Key signal:** E asks "what did this session leave unaddressed?"

### S — Recovery-Aware
The workout that respects accumulated fatigue.

- S assumes the trainee is somewhat depleted from the hub
- It offers productive training that lets stressed systems breathe while building capacity in other areas
- S tends toward: lower CNS demand, different tissue groups, softer session formats relative to the hub
- After 🏟 Performance, S should be recovery-oriented (🖼 or 🐂)
- After 🔴 Intense density, S should offer lower density (⚪ or ⚫)
- S is NOT a rest day — it is a productive session that happens to be easier than the hub

**Key signal:** S asks "what can this person do well when partially depleted?"

### W — Exploration
The least obvious connection. W opens a new training vector.

- W introduces a different Order-Axis combination the user wouldn't naturally gravitate toward
- W creates novel stimulus and prevents the web from becoming predictable
- W might shift the movement character, equipment format, or training intent dramatically
- W is the trainer's "trust me on this one"
- W should still be a valid, coherent workout — novelty is the goal, not chaos

**Key signal:** W asks "what would genuinely surprise this person and expand their capacity?"

---

## Fatigue Signature Derivation

Every zip code has a computable fatigue profile based on its 4 dials. This derivation is mechanical.

### CNS Load (from Order)

| Order | Name | CNS Rating | Numeric |
|-------|------|-----------|---------|
| 🐂 | Foundation | Low | 1 |
| ⛽ | Strength | High | 4 |
| 🦋 | Hypertrophy | Moderate | 2 |
| 🏟 | Performance | High | 4 |
| 🌾 | Full Body | Moderate | 2 |
| ⚖ | Balance | Moderate | 2 |
| 🖼 | Restoration | Low | 1 |

### Tissue Fatigue (from Type)

| Type | Name | Primary Tissue | Secondary Tissue | Recovery Window |
|------|------|---------------|-----------------|-----------------|
| 🛒 | Push | Chest, Front Delts, Triceps | Core (stabilization) | 48–72h |
| 🪡 | Pull | Lats, Rear Delts, Biceps, Traps, Erectors | Grip, Core | 48–72h |
| 🍗 | Legs | Quads, Hamstrings, Glutes, Calves | Core, Lower Back | 48–72h |
| ➕ | Plus | Full Body (Power), Core | CNS (explosive demand) | 48–72h |
| ➖ | Ultra | Cardiovascular System | Legs (running), Back (rowing) | 24–48h |

### Session Density (from Color)

| Color | Name | Density | Numeric |
|-------|------|---------|---------|
| ⚫ | Teaching | Low | 1 |
| 🟢 | Bodyweight | Moderate | 2 |
| 🔵 | Structured | Moderate | 2 |
| 🟣 | Technical | Low | 1 |
| 🔴 | Intense | High | 4 |
| 🟠 | Circuit | High | 3 |
| 🟡 | Fun | Variable | 2 |
| ⚪ | Mindful | Low | 1 |

### Movement Character (from Axis)

| Axis | Name | Character | Carry-Over Effect |
|------|------|-----------|-------------------|
| 🏛 | Basics | Bilateral/Barbell/Stable | Spinal loading, grip fatigue, bilateral pattern grooved |
| 🔨 | Functional | Unilateral/Standing/Athletic | Stabilizer fatigue, balance demand, proprioceptive load |
| 🌹 | Aesthetic | Isolation/FullROM/Cables | Localized tissue pump, low systemic fatigue |
| 🪐 | Challenge | Hardest/Deficit/Pause/Tempo | High neuromuscular demand, joint stress at end range |
| ⌛ | Time | Clock-driven/Metabolic | Metabolic fatigue, pacing patterns, cardiovascular demand |
| 🐬 | Partner | Social/Alternating/Competitive | Variable — depends on partner dynamic |

### Composite Fatigue Signature Format

```
[zip] | CNS: [1-4] | Tissue: [primary] | Density: [1-4] | Character: [movement type]
```

Examples:
```
⛽🏛🛒🔴 | CNS: 4 | Tissue: Chest/FDelts/Triceps | Density: 4 | Character: Bilateral/Barbell/Stable
⛽🏛🛒⚪ | CNS: 4 | Tissue: Chest/FDelts/Triceps | Density: 1 | Character: Bilateral/Barbell/Stable
🖼🌹🍗⚪ | CNS: 1 | Tissue: Quads/Hams/Glutes/Calves | Density: 1 | Character: Isolation/FullROM/Somatic
```

---

## Neighbor Selection Logic

The neighbor zip code at each direction is selected by coaching logic that weighs five factors.

### Factor 1: Fatigue Signature of the Main Hub

Read the hub's composite fatigue signature before selecting neighbors:
- **CNS Load**: How much does the hub tax the nervous system?
- **Tissue Fatigue**: Which muscles were worked and how hard?
- **Session Density**: How compressed was the work?
- **Movement Character**: What motor patterns were trained?

### Factor 2: Readiness Profile for the Neighbor

The neighbor should be something the trainee is ready for given the hub's fatigue signature.

- High CNS hub → N can be moderate-high; S and E should not also be high CNS
- Tissue-fatigued hub → neighbors must train different tissue (guaranteed by Type exclusion rule)
- High-density hub → S and E should offer lower density
- Bilateral hub → E should favor unilateral or corrective work

### Factor 3: Downstream Coherence (2-hop awareness)

Each neighbor zip is also a hub with its own N/E/S/W. The selected neighbor should be one whose own pod makes sense as a continuation. Avoid selecting neighbors that would create dead-end clusters or circular traps.

Think 2 hops ahead: main → neighbor → neighbor's neighbors.

### Factor 4: Dial Variety Across the 4 Neighbors

Across the 4 neighbors of any hub, aim for variety across ALL dials — not just Type:
- **Order variety**: Not all 4 neighbors at the same Order. Spread loading phases.
- **Axis variety**: Not all 4 neighbors sharing the hub's Axis. Different movement characters.
- **Color variety**: Not all 4 neighbors at the same Color. Different formats and equipment.

This is a **soft goal**, not a hard constraint. Some overlap is acceptable. Monotony is not.

### Factor 5: Training Logic Principles

Apply these in order of strength (earlier = stronger signal):

1. After high-CNS work (⛽/🏟), favor lower-CNS neighbors at S and E
2. After high-density work (🔴), favor lower-density at S (⚪, ⚫, or 🟣)
3. After Restoration (🖼), N can be ambitious — the body is fresh
4. After Foundation (🐂), N can increase intensity — patterns are established
5. After Performance testing (🏟), S must be recovery-oriented, E should be corrective
6. After Full Body integration (🌾), neighbors can specialize
7. After Balance correction (⚖), N should capitalize on corrections with compound work
8. After heavy bilateral (🏛), E should favor unilateral (🔨) or corrective (⚖) Axis
9. ➖ Ultra workouts have shorter recovery windows (24–48h) — neighbors can be heavier sooner
10. 🌹 Aesthetic workouts produce localized pump with low systemic fatigue — neighbors can be intense

---

## Overlap Rules

Different main zips **can** share the same neighbor zip. This is expected and acceptable.

- If ⛽🏛🛒🔵 and ⛽🔨🛒🟣 both point to 🦋🌹🪡⚪ at S, that's fine
- Popular zip codes may appear as neighbors in many pods
- Unpopular or edge-case zips may appear in fewer
- There is **no symmetry requirement**: if Zip A points to Zip B at N, Zip B is NOT required to point back to Zip A at any direction

---

## Coverage Goal (Soft)

Across any hub's 4 neighbors:
- Prefer representation from at least 3 different Orders
- Prefer representation from at least 2 different Axes
- Prefer representation from at least 3 different Colors

This is aspirational, not required. Some hubs (especially edge-case Orders like 🏟 Performance) will naturally cluster toward adjacent Orders.

---

## Relationship to Almanac

The zip-web is **detached** from the Almanac rotation engine (seeds/default-rotation-engine.md).

The Almanac generates a daily default zip from three gears: Order by weekday, Type by rolling 5-day cycle, Axis by monthly operator. The zip-web provides an alternative navigation path.

The two systems are parallel and compatible:
- A user following the Almanac gets a zip each day. They can check that zip's N/E/S/W for alternatives.
- A user ignoring the Almanac can enter the web at any zip and navigate by pod connections.
- The systems never conflict — both produce valid standalone workouts.

The zip-web does not prescribe timing. It prescribes relationships. The Almanac prescribes timing. They answer different questions.

---

## Pod Validation Checklist

Before writing any pod entry as complete, verify all of the following:

**Type constraint:**
- [ ] Hub Type is identified
- [ ] All 4 remaining Types are represented in N/E/S/W
- [ ] No Type repeated across N/E/S/W
- [ ] Hub Type not present in any N/E/S/W slot

**Neighbor validity:**
- [ ] Every neighbor zip exists in zip-web-registry.md as a valid 4-emoji combination
- [ ] All 4 dials of each neighbor are valid SCL values

**Directional character:**
- [ ] N neighbor makes sense as a progression from the hub
- [ ] E neighbor addresses what the hub neglected or exposed
- [ ] S neighbor respects accumulated fatigue (lower CNS or density vs hub)
- [ ] W neighbor opens a genuinely different training vector

**Training logic:**
- [ ] High CNS hub → S and E are not also high CNS (unless W/Exploration makes a deliberate contrast)
- [ ] High density hub → S neighbor is lower density
- [ ] Fatigue signature of hub informs neighbor selection
- [ ] Coaching rationale is present and makes training sense

**Format:**
- [ ] Pod header includes zip code and workout title (if generated)
- [ ] Fatigue signature line is correct for the hub
- [ ] Direction table has N/E/S/W entries
- [ ] Pod Types validation line is present
- [ ] Coaching rationale is 1–2 sentences, direct, no filler

---

## Pod Format Reference

```markdown
⛽🏛🛒🔵 — Heavy Classic Presses

Fatigue Signature: CNS: 4 | Tissue: Chest/FDelts/Triceps | Density: 2 | Character: Bilateral/Barbell/Stable

| Dir | Zip | Why |
|-----|-----|-----|
| N (Progression) | ⛽🏛🪡🔵 | Heavy pulls after heavy presses. The upper back that drives the press gets immediate reciprocal loading — this is the classic bilateral strength pairing. |
| E (Balance)     | ⚖🔨🍗🔵 | After bilateral pressing, the hips and unilateral leg patterns are completely unaddressed. ⚖🔨 applies corrective single-leg logic to the lower body gap. |
| S (Recovery)    | 🖼🌹➖⚪  | After max-strength pressing, the CNS needs a session that produces nothing taxing. Restoration conditioning at mindful pace resets without adding debt. |
| W (Exploration) | 🌾⌛➕🟣  | Full Body Time-based power work is the opposite of isolated bilateral pressing — it opens a movement integration vector that heavy bench training never touches. |

Pod Types: 🛒 (hub) + 🪡 + 🍗 + ➖ + ➕ = 🛒🪡🍗➖➕ ✓
```

---

## Agent Instructions for Pod Population

When populating a stub pod file:

1. Read this file completely
2. Read `zip-web-signatures.md` for hub fatigue profiles
3. Read `zip-web-registry.md` to verify neighbor zip validity
4. If Deck 07 pods exist and are populated, use them as the quality bar
5. For each of the 40 hubs in the target deck:
   a. Identify hub fatigue signature
   b. Apply Type exclusion rule — map 4 remaining Types to N/E/S/W
   c. Select specific neighbor zips using coaching logic and training principles
   d. Write 1–2 sentence rationale for each direction
   e. Run the pod validation checklist
6. Commit with message: `feat: [StoryID] - Populate pods for Deck XX`
7. Update prd.json and progress.txt

One deck per session. Validate every pod before committing.
