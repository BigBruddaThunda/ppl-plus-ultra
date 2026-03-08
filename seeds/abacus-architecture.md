---
planted: 2026-03-08
status: SEED
phase-relevance: Phase 3–6 (Programming Layer, User Experience, Almanac)
blocks: nothing currently — foundational sort architecture
depends-on: seeds/default-rotation-engine.md, scl-directory.md, middle-math/navigation-graph.json
connects-to: seeds/junction-community.md, seeds/elevator-architecture.md, seeds/platform-architecture-v2.md, middle-math/rotation/reverse-weight-resolution.md
---

# The Abacus — Training Program Architecture

## One Sentence

35 training archetypes, each containing 48 zip codes, organize the entire 1,680-room system into complete, overlapping workout programs that any human can select, combine, and rotate.

## Why "Abacus"

The 🧮 emoji already lives in the SCL as the SAVE block — the session-closing ritual. But zoom out on the emoji itself: colored beads on rods in a frame. That is exactly what this layer is. Each abacus is a frame. The beads are zip codes. The rods are the dials. The colors are the Colors. The math is visible.

The word "abacus" also carries the right connotation: calculation by physical arrangement. Not abstract. Not algorithmic. You see the beads. You move them. The answer is the position. That is how a user should experience their training program — visible, tangible, rearrangeable.

Plural: abaci (Latin) or abacuses (English). Use "abaci" in system documentation, "abacuses" nowhere. When addressing users: "your abacus" (singular) or "your training programs" (plural, plain English).

## The Math

The rotation engine (seeds/default-rotation-engine.md) establishes:
- Order cycles on 7 (days of the week)
- Type cycles on 5 (rolling calendar)
- 7 × 5 = 35 days before an Order-Type pairing repeats

This 35-day super-cycle is the natural programming unit. Not "35 days" in the calendar sense — 35 training sessions. A user training 4×/week completes a cycle in ~9 weeks. A user training 6×/week completes it in ~6 weeks. The cycle is session-counted, not date-counted.

**1,680 ÷ 48 = 35 abaci.**

Each abacus contains 48 zip codes:
- **35 working zips** — one per session in the super-cycle. No Order-Type repeat.
- **13 bonus zips** — junction gateways, harder variations, recovery alternatives, cross-program bridges.

## What an Abacus Is

An abacus is a complete training program for a specific training archetype. It contains every session a person following that archetype needs, organized for progressive rotation across the 35-session super-cycle.

Each abacus:
- Covers all 7 Orders across its 35 working zips (every loading protocol appears)
- Covers all 5 Types across its 35 working zips (every muscle group appears)
- Has a dominant Axis bias that defines its character (but is not locked to one Axis)
- Uses a Color distribution that matches the archetype's equipment and intensity profile
- Contains 13 bonus zips for junctions, alternatives, and cross-program exploration

An abacus is NOT:
- A deck (decks are Order × Axis, 40 cards each — the filing system)
- A seasonal calendar (the Operis handles temporal rhythm)
- A rigid 35-day plan (it's a pool that the rotation engine draws from)

## The 35 Training Archetypes

These are the 35 abaci. Every possible way a person would want to train maps to one or more of these. The list is exhaustive by design — if a training style exists, it has an abacus.

### Strength Domain (7 abaci)
1. **General Strength** — Barbell classics, linear progression, balanced push/pull/legs
2. **Powerlifting** — Squat/bench/deadlift focus, peaking cycles, competition prep
3. **Strongman/Odd Object** — Carries, stones, yokes, implements (🟣 and 🔴 heavy)
4. **Calisthenics Strength** — Advanced bodyweight: muscle-ups, levers, planches (🟢 dominant)
5. **Kettlebell Strength** — KB-first programming, swings, TGUs, complexes
6. **Senior Strength** — Joint-friendly loading, machine-assisted, balance integration
7. **Post-Rehab Strength** — Return-to-training progressions, conservative loading, ⚖ heavy

### Hypertrophy Domain (5 abaci)
8. **Bodybuilding** — Isolation-heavy, pump focus, 🌹 Aesthetic dominant
9. **Physique / Recomp** — Balanced hypertrophy + conditioning, leaner bias
10. **Athletic Hypertrophy** — Size that transfers: power-building, sport-hybrid
11. **Minimalist Hypertrophy** — 3×/week full compounds, time-efficient muscle gain
12. **Aesthetic Specialization** — Weak-point targeting, ⚖ Balance + 🌹 Aesthetic cross

### Conditioning Domain (5 abaci)
13. **General Conditioning** — Broad aerobic base, mixed modality, ➖ Ultra dominant
14. **Marathon / Distance Running** — Zone 2 heavy, running-specific mobility and strength
15. **Sprint / Power Conditioning** — Short intervals, explosive repeats, plyometrics
16. **Sport Conditioning** — Field sport energy systems, agility, lateral movement
17. **Fasting Cardio + Strength** — Low-intensity AM conditioning paired with PM strength

### Functional / Athletic Domain (5 abaci)
18. **General Functional Fitness** — 🔨 Functional dominant, transfer-focused
19. **CrossFit-Style** — Mixed modal, EMOM/AMRAP, Olympic lifts + conditioning
20. **Combat Sport Prep** — Rotational power, grip, neck, conditioning circuits
21. **Field Sport Athlete** — Sprint, jump, cut, decelerate — movement-first
22. **Climbing / Grip Sport** — Pull dominance, finger strength, shoulder stability

### Life Stage Domain (5 abaci)
23. **New to Gym** — 🐂 Foundation heavy, teaching-focused, ⚫ dominant Color
24. **Return After Break** — Ramp-back protocol, conservative progression, 🔢 Fundamentals
25. **50+ Active Living** — Joint health priority, balance, bone density, functional independence
26. **Pre/Post Natal** — Pelvic floor, core restoration, modified loading (requires medical clearance flag)
27. **Youth Athletic Development** — Movement literacy, bodyweight mastery, no maximal loading

### Recovery / Wellness Domain (4 abaci)
28. **Active Recovery** — 🖼 Restoration dominant, mobility, somatic, ⚪ Mindful heavy
29. **Stress Management** — Parasympathetic training, breath work, low-CNS movement
30. **Flexibility / Mobility** — ROM-focused, 🌹 in 🖼 context (somatic aesthetic)
31. **Injury Prevention / Prehab** — ⚖ Balance dominant, corrective, 🏗 Reformance heavy

### Specialty Domain (4 abaci)
32. **Olympic Lifting** — Snatch/clean/jerk progression, 🟣 Technical dominant (GOLD required)
33. **Endurance Sport Cross-Training** — Cyclist/swimmer/runner strength complement
34. **Tactical / First Responder** — Occupational fitness, carry capacity, sustained output
35. **Explorer / Outdoor Athlete** — Hiking, rucking, trail movement, minimal equipment

## Abacus Internal Architecture

Each abacus has 48 zip codes arranged across the 35-session rotation:

```
Session Slots (35):
┌──────────────────────────────────────────────────┐
│ S01  S02  S03  S04  S05  S06  S07               │
│ S08  S09  S10  S11  S12  S13  S14               │
│ S15  S16  S17  S18  S19  S20  S21               │
│ S22  S23  S24  S25  S26  S27  S28               │
│ S29  S30  S31  S32  S33  S34  S35               │
└──────────────────────────────────────────────────┘

Bonus Pool (13):
┌──────────────────────────────────────────────────┐
│ B01  B02  B03  B04  B05  B06  B07               │
│ B08  B09  B10  B11  B12  B13                     │
└──────────────────────────────────────────────────┘
```

**Session slot rules:**
- Each of the 7 Orders appears exactly 5 times across 35 sessions
- Each of the 5 Types appears exactly 7 times across 35 sessions
- No two adjacent sessions share the same Type (natural Ppl split)
- Axis distribution reflects the archetype's character (not uniform)
- Color distribution reflects the archetype's equipment profile

**Bonus pool rules:**
- At least 3 must be junction bridges to other abaci (cross-program gateways)
- At least 2 must be harder variations (🪐 Challenge axis) of working zips
- At least 2 must be recovery alternatives (🖼 or ⚪) for deload swaps
- Remaining are variety/exploration zips that fit the archetype
- Any bonus zip may duplicate a zip that exists in another abacus

## Overlap and Merging

A single zip code can appear in multiple abaci. This is not a bug — it is the architecture.

Example: ⛽🏛🪡🔵 (Strength, Basics, Pull, Structured) appears in:
- General Strength (working slot)
- Powerlifting (working slot — deadlift day)
- Athletic Hypertrophy (bonus pool — heavy pull day)
- Return After Break (bonus pool — reintroduction to barbell pulling)

**When a user selects multiple abaci:**
1. Union all zip codes from selected abaci
2. Collapse duplicates (a zip is a zip — it doesn't exist twice)
3. The merged pool becomes the user's available rotation
4. The rotation engine draws from the merged pool using the standard 3-gear logic
5. Junction routing prioritizes zips that serve multiple selected abaci

Example: User selects General Strength (48 zips) + Bodybuilding (48 zips).
If 12 zips overlap, their merged pool = 84 unique zips.
The rotation engine has 84 options instead of 48.
More variety. More progressive options. Same rotation logic.

## Relationship to Existing Systems

### Rotation Engine (seeds/default-rotation-engine.md)
The rotation engine produces a daily Order-Type-Axis suggestion. The abacus **filters** that suggestion. If the engine says "today is ⛽🪡" (Strength, Pull), the abacus narrows to: which ⛽🪡 zip codes are in this user's selected abaci? The Axis and Color come from the abacus's internal distribution, not just the monthly default.

### Junction Routing (seeds/junction-community.md)
Every card's 🚂 Junction block suggests 1–3 next zip codes. In the abacus context, junction suggestions should prefer zips within the user's selected abaci. The 13 bonus zips per abacus exist partly to serve as junction targets.

### Decks (the filing system)
Decks are the library shelf organization: Order × Axis = 42 decks of 40 cards each. Abaci are the reading lists: cross-cutting selections from across the library. A single abacus pulls from multiple decks. The deck system doesn't change. The abacus is a view layer on top of it.

### Operis (seeds/operis-architecture.md)
The daily Operis features zip codes from the rotation engine's full 1,680 pool. It is not filtered by the user's abacus selection. The Operis is the newspaper — everyone gets the same edition. The abacus is the personal training program. They coexist. A user might do their abacus workout AND read the Operis featuring a completely different zip.

### Intercolumniation (future middle-math layer)
The space between sessions matters. A user training 3×/week has different recovery dynamics than 6×/week. The intercolumniation layer (architectural term: the space between columns) adjusts zip selection within the abacus based on:
- Days since last session
- CNS load of previous session (Order-derived)
- Muscle group fatigue (Type-derived)
- This is the reverse-weight resolution applied to program context

## User Experience

### Selection
A user picks 1–3 abaci during onboarding or at any time from settings. Each abacus has a clear, plain-English name and a one-line description. No jargon. No SCL knowledge required.

"What describes your training?" → checkboxes. Done.

### Toggles
Within their selected abaci, users can toggle:
- Specific Types on/off ("I don't do leg day" → 🍗 zips suppressed)
- Specific Colors on/off ("I don't have a barbell" → 🔵 Tier 3 zips suppressed)
- This creates a personalized sub-pool from the abacus union

### Progressive Programming
The 35-session cycle IS progressive programming. The Order rotation ensures:
- Week 1: Foundation → Strength → Hypertrophy → Performance → Full Body → Balance → Restoration
- Week 2: Same Order progression, different Types (shifted by the 5-day roll)
- Week 3–5: Continue shifting until all 35 Order-Type combinations covered

Load progression happens at the card level (weight logging, superscript tracking). The abacus handles programming structure. The card handles load management.

### The "Forever Program" Property
An abacus with 48 zips and a 35-session rotation means:
- 35 unique sessions before any Order-Type repeat
- 13 bonus zips for swap-in variety
- After completing the cycle, the same 35 sessions return but with progressive load from logging
- The program never ends. It just rotates. The user improves within the structure.

## Operis Discovery → Personal Library

The daily Operis features zip codes the user may never have encountered in their selected abaci. The Operis is the newspaper — it shows the full 1,680-room building, not just the user's floor. This makes it a discovery surface.

**Save-to-Abacus flow:**
1. User reads the daily Operis
2. A featured zip code catches their interest — a training style, exercise, or format they want to try
3. They tap **Save** (🧮) on that zip code
4. The zip is added to their personal library — a holding area outside any specific abacus
5. From their library, they can assign saved zips into any of their custom abaci
6. The saved zip enters their rotation on the next cycle

This is the Operis-to-training pipeline. Editorial content becomes personal programming. The Operis is not just reading material — it is a feeder system for the abacus layer.

**What "Save" means technically:**
- The zip code is bookmarked to the user's `saved_zips` collection
- It does NOT automatically enter active rotation (that would disrupt their program)
- The user decides when and where to slot it: into an existing abacus, into a new custom abacus, or just held for later
- Saved zips that never get assigned still appear in the user's personal library as "unslotted" — available but not rotating

## Custom Abaci and Zip Editing

The 35 system abaci are starting points. Users build on top of them.

**Custom abacus creation:**
- A user can create a custom abacus from scratch (empty frame, add zips manually)
- A user can fork a system abacus (copies all 48 zips, then edit)
- A user can merge two system abaci into a custom one (union, collapse duplicates, then edit)

**Zip editing within an abacus:**
- **Add:** Pull zips from saved library, from other abaci, or browse the full 1,680 catalog
- **Remove:** Tap a zip to remove it from this abacus. The zip still exists in the system and in any other abacus that contains it. Removing is per-abacus, not global deletion.
- **Swap:** Replace a working slot zip with a bonus zip or a saved zip. The removed zip moves to the bonus pool or leaves the abacus entirely (user's choice).

**Seasonal profiles:**
- Custom abaci save to the user's profile
- A user can have multiple custom abaci and switch between them
- Use case: "Winter Indoor" abacus (🟢 and 🟠 heavy, no outdoor work), "Summer Athlete" abacus (🔨 Functional heavy, outdoor conditioning), "Competition Prep" abacus (🏟 Performance heavy, peaking focus)
- Switching abaci changes what the rotation engine draws from — same engine, different pool
- Historical data is per-zip, not per-abacus. If you did ⛽🏛🪡🔵 in your winter abacus and it appears in your summer abacus, your logged history carries over. The zip is the zip.

**Sharing (future):**
- A custom abacus could be shared as a link or template
- A coach could build an abacus and assign it to clients
- The 🐬 Partner axis and community features connect here (seeds/junction-community.md)

## Data Model Implications

```
abacus
├── id: INT (1–35)
├── name: VARCHAR — plain English
├── slug: VARCHAR — URL-safe
├── description: TEXT — one line
├── domain: VARCHAR — which of the 7 domains
├── axis_bias: CHAR(1) — dominant axis emoji
├── color_profile: JSONB — Color distribution weights
└── meta: JSONB — archetype-specific parameters

abacus_zip
├── abacus_id: INT → abacus.id
├── zip_numeric: CHAR(4) → zip_metadata.zip_numeric
├── slot_type: ENUM('working', 'bonus')
├── slot_number: INT (1–35 for working, 1–13 for bonus)
├── bonus_role: ENUM('junction', 'variation', 'recovery', 'variety') — NULL for working
└── UNIQUE(abacus_id, zip_numeric)

user_abacus
├── user_id: UUID → profiles.id
├── abacus_id: INT → abacus.id (NULL for custom)
├── custom_name: VARCHAR — NULL for system abaci, user-defined for custom
├── is_custom: BOOLEAN DEFAULT false
├── active: BOOLEAN
├── selected_at: TIMESTAMPTZ
├── season_tag: VARCHAR — optional ("winter", "competition", etc.)
└── UNIQUE(user_id, abacus_id) — for system abaci

user_custom_abacus_zip
├── user_abacus_id: INT → user_abacus.id (custom abaci only)
├── zip_numeric: CHAR(4) → zip_metadata.zip_numeric
├── slot_type: ENUM('working', 'bonus')
└── added_at: TIMESTAMPTZ

saved_zips
├── user_id: UUID → profiles.id
├── zip_numeric: CHAR(4) → zip_metadata.zip_numeric
├── source: ENUM('operis', 'junction', 'browse', 'share')
├── saved_at: TIMESTAMPTZ
├── operis_date: DATE — NULL unless source = 'operis'
├── assigned: BOOLEAN DEFAULT false — true once slotted into an abacus
└── UNIQUE(user_id, zip_numeric)

user_type_toggle
├── user_id: UUID
├── type_emoji: CHAR — 🛒🪡🍗➕➖
├── enabled: BOOLEAN DEFAULT true
└── UNIQUE(user_id, type_emoji)

user_color_toggle
├── user_id: UUID
├── color_emoji: CHAR — ⚫🟢🔵🟣🔴🟠🟡⚪
├── enabled: BOOLEAN DEFAULT true
└── UNIQUE(user_id, color_emoji)
```

## Build Sequence

1. **Define the 35 abaci** — name, domain, description, axis bias, color profile
2. **Populate zip assignments** — 48 zips per abacus, slot type, bonus roles
3. **Validate coverage** — every zip appears in at least 1 abacus, Order/Type distribution per abacus is correct
4. **Build overlap map** — which zips appear in which abaci, shared zip graph
5. **Write SQL migration** — abacus tables, seed data
6. **Build rotation filter** — engine output filtered by user's abacus union
7. **Build toggle system** — Type and Color suppression within the filtered pool
8. **Junction routing update** — prefer in-abacus targets in 🚂 blocks
9. **Operis save button** — 🧮 tap on featured zips adds to saved_zips
10. **Personal library UI** — saved zips view, assign-to-abacus flow
11. **Custom abacus builder** — create/fork/merge, add/remove/swap zips
12. **Seasonal profile switcher** — load different abaci by season or phase

Steps 1–4 are scriptable from the existing zip registry and card data.
Steps 5–8 require the experience layer (Phase 4+).
Steps 9–12 require the experience layer + user accounts (Phase 5–6).

## Open Questions

- Should abaci be strictly non-overlapping in their 35 working slots? (Bonus pool overlap is assumed.) If working slots can overlap, the total unique zip coverage across all 35 abaci is less than 1,225 (35 × 35). If they cannot overlap, exactly 1,225 working slots exist with 455 remaining zips distributed as bonuses (1,680 - 1,225 = 455, and 35 × 13 = 455). The math is exact. This may not be a coincidence.
- How do operators layer onto abacus context? The operator is derived from Axis × Color polarity. Within an abacus, the operator distribution should reflect the archetype's character. Bodybuilding abacus → more 🦢 plico (superset) and 👀 specio (form check). Powerlifting → more 🤌 facio (execute) and 🚀 mitto (max attempt). This is a future layer.
- Should the user see "abacus" terminology, or should the UI say "training program" / "training plan"? The internal system name is abacus. The user-facing name may differ.
- The 35 archetype list needs validation against real-world training populations. Are there gaps? Redundancies? The list should be exhaustive but not padded.
- Intercolumniation weight system: how much does session spacing affect zip selection? A 2-day gap after ⛽ Strength is different from a 4-day gap. The middle-math layer needs a decay/recovery model per Order.

## Archideck Kernel Connection

The abacus architecture is pure SCL applied to itself. The same 4-dial system that addresses individual workouts also organizes workout programs. This is the recursive property of the zip code system — it scales from "what is this single session?" to "what is this entire training life?"

The Archideck kernel can express this: any domain that has a multi-dimensional address space can generate abaci by defining archetypes and populating them with address selections. The abacus pattern is domain-agnostic. Ppl± is the first implementation.

---

## The Abacus as Neighborhood

The abacus is a neighborhood in the digital city. When a user selects their training abaci, they are choosing where they live — which streets they walk, which rooms they frequent, which community they belong to. A powerlifting abacus is a different neighborhood than a yoga-and-mobility abacus, even though they exist in the same city and share the same infrastructure (the SCL, the Operis, the cosmograms, the envelope system).

This is the connection between the workout programming layer and the broader city architecture. The 35 archetypes are 35 neighborhoods. Each has its own character, its own regulars, its own daily rhythm. But all neighborhoods share the same 7 buildings (Orders), the same 6 floors (Axes), the same civic services (Operis, almanac, community). The abacus is what makes the city personal — it's your address within the address system.

Selecting multiple abaci is living in multiple neighborhoods. A user running both "Powerlifting" and "Calisthenics" abaci is splitting their time between two parts of the city with different cultures but shared infrastructure. The rotation engine handles the commute — which neighborhood are you in today?

---

🧮
