---
planted: 2026-03-24
status: SEED
phase-relevance: Phase 3.1+ (quality rebuild), all future phases (directional constraint)
blocks: nothing — this is a directional document, not a deliverable
depends-on:
  - CLAUDE.md
  - scl-directory.md
  - seeds/negentropy-thesis.md
  - seeds/systems-eudaimonics.md
  - seeds/digital-city-architecture.md
  - seeds/city-compiler-architecture.md
  - seeds/data-ethics-architecture.md
  - seeds/life-copilot-architecture.md
connects-to:
  - seeds/experience-layer-blueprint.md
  - seeds/mobile-ui-architecture.md
  - seeds/exploration-immersion-architecture.md
  - seeds/heros-almanac-v8-architecture.md
  - seeds/character-progression-architecture.md
  - seeds/elevator-architecture.md
  - seeds/operis-architecture.md
  - seeds/outside-system-v2-architecture.md
  - seeds/voice-parser-architecture.md
  - middle-math/rotation/reverse-weight-resolution.md
  - middle-math/exercise-registry.json
  - exercise-library.md
supersedes: nothing (first specification)
---

# Architectural Reset Direction — What Tightens When the System Rebuilds

🔵🪐 — systematic + deep

## One Sentence

Every time the Ppl± architecture is reconsidered from first principles, the constraint surface tightens, the coverage improves, the naming sharpens, and the system becomes more internally consistent — because the act of rebuilding is itself negentropy.

---

## Section 1 — What the Reset Is

This is not a pivot. Nothing is being thrown away. This is the system looking at itself with fresh eyes and asking: does the architecture still serve the thesis?

The thesis: Ppl± is the externalization of 20,000 hours of personal training experience into a computable system (`seeds/negentropy-thesis.md`). The SCL-61 is the compression format. The 1,680 zip codes are the address space. The constraint hierarchy is the decision logic. The exercise library is the content substrate.

The reset is an audit of how well each layer expresses that thesis. Where the expression is weak, the architecture tightens. Where the expression is strong, it gets documented more clearly so nothing is lost to context drift.

---

## Section 2 — What Got Tighter

### 2.1 — The Hollow Template Clarification

**Before:** The 1,680 cards were understood as the primary output — generate all cards, then build the experience layer on top.

**After:** The 1,680 cards are one instantiation of 1,680 topological addresses. Each address has a shape (block sequence, set structure, rest architecture, constraint surface) that exists independent of content. The hollow template is not a future feature — it is the same address with the content layer zeroed out. This means:

- User-built workouts are not a separate system. They are the same room with user-placed furniture.
- Auto-complete is not AI magic. It is the constraint solver filling empty slots in a room whose shape is already defined.
- The City Compiler (`seeds/city-compiler-architecture.md`) already resolves room shapes. The hollow template is a rendering option, not a new computation.

### 2.2 — The Constraint Solver as Live System

**Before:** Exercise selection was a generation-time computation. Select exercises, write card, done.

**After:** Exercise selection is a real-time computation that runs at generation time AND at user interaction time. The same algorithm that populates a card from scratch also:

- Populates a hollow template when a user taps a slot
- Recalculates remaining options when a user swaps an exercise mid-workout
- Adjusts the pool based on what has already been placed (non-redundancy filter)
- Weights options by what comes after (forward-looking coherence)

The exercise selection algorithm is not a card generation tool. It is a live constraint solver that operates at every timescale from annual rotation to per-exercise swap. This is the same math, different execution contexts.

### 2.3 — The Exercise Library as Constraint Surface

**Before:** The library was understood as a reference document — exercises mapped to types, tiers, and axes.

**After:** The library is the substrate that the constraint solver filters against. Its size (2,085 entries) is not about user choice. It is about mathematical coverage. Every possible zip code × user state × mid-workout position needs at least a handful of valid options. The library exists because the constraint surface demands it.

This reframes library expansion: new exercises are not added for variety. They are added when the constraint solver identifies coverage gaps — zip code × state combinations where the filtered pool is too small.

### 2.4 — Multi-Timescale Coherence

**Before:** The rotation engine, reverse-weight resolution, and workout generation were understood as separate systems with handoff points.

**After:** They are the same principle operating at different timescales. The rotation engine is the annual constraint solver. Reverse-weight resolution is the daily constraint solver. Mid-workout swap is the per-exercise constraint solver. All three:

1. Take the current state as input
2. Filter the possibility space through the constraint hierarchy
3. Weight the remaining options by context (what came before, what comes after)
4. Produce the best-fit output for this moment

Recognizing this unifies the architecture. The "rotation engine" and the "exercise selection algorithm" and the "mid-workout swap handler" can share infrastructure because they are isomorphic operations at different timescales.

### 2.5 — Zip Code as Communication Protocol

**Before:** The zip code was understood as an internal addressing system — how the system organizes itself.

**After:** The zip code is also an external communication protocol — how users communicate training state to each other. Four digits (2123) or four emojis (⛽🏛🪡🔵) carry more workout information than a paragraph of natural language. The Color dial carries emotional metadata (intensity, mood, intent) that plain language workout descriptions never encode.

This is not a social feature. It is a property of the compression format itself. Any system that compresses complex state into short addresses creates a communication protocol as a side effect. The zip code is both the system's internal bus and the user's external shorthand.

---

## Section 3 — What Ripples

These tightenings are not isolated insights. They ripple through the entire seed library.

### The Experience Layer

The experience layer (`seeds/experience-layer-blueprint.md`) must render both fully-furnished rooms and hollow templates. This is not two rendering modes — it is one rendering pipeline that accepts content-density as a parameter. Zero content = hollow template. Full content = pre-generated card. Partial content = user mid-build. The renderer is the same.

### The Mobile UI

The mobile UI (`seeds/mobile-ui-architecture.md`) must support mid-workout exercise swaps. The 4-dial UI already exists for navigation. The exercise slot becomes tappable. The dropdown is the constraint solver's output for that slot given the current workout state. The UI change is minimal. The computation behind it is the same constraint solver that generated the card in the first place.

### The Voice Layer

Wilson (`seeds/wilson-voice-identity.md`) and the voice parser (`seeds/voice-parser-architecture.md`) can describe hollow templates verbally: "You're in room 2123. Strength, Basics, Pull, Structured. Five blocks. First slot is open. I'd suggest deadlifts based on what you've done this week." The voice layer navigates the same address space and runs the same constraint solver. The modality changes. The math doesn't.

### The Operis

The Operis (`seeds/operis-architecture.md`) features zip codes daily. The featured Sandbox room is the reverse-weight resolution room — the room the system recommends based on temporal triangulation. This is the daily-timescale version of the same constraint solver that operates at the per-exercise timescale during a workout.

### The Outside System

Real-world activities logged as zip code matches (`seeds/outside-system-v2-architecture.md`) feed the same personal weight vector that the constraint solver uses. An outdoor hike logged as ⚖➖🟢 shifts the vector, which shifts tomorrow's reverse-weight resolution, which shifts the constraint surface of every room the user enters next. The outside system is not a separate feature. It is an entropy input channel that the negentropy engine metabolizes.

### Character Progression

The character progression system (`seeds/character-progression-architecture.md`) tracks which rooms a user has visited, which exercises they've performed, which Orders they favor. This is a read model derived from the same events (logged sets) that the constraint solver uses. The progression system and the constraint solver share a data source. They are two projections of the same event stream.

### The Exploration Layer

Fog of war (`seeds/exploration-immersion-architecture.md`) is a rendering of the constraint surface's coverage. Unexplored rooms are rooms where the user's personal weight vector has no data. The fog lifts when data arrives. The exploration layer is a visualization of the negentropy engine's state — where has entropy been absorbed, and where are there still gaps?

---

## Section 4 — What the Reset Proves

The system gets better by even contemplating the reset.

Three passes of sharing vision, articulating the abstract, and reconnecting to first principles produced:

1. **The hollow template insight** — the address is not the content. Two valid states of the same room.
2. **The live constraint solver** — exercise selection is not a generation-time tool. It is a real-time system.
3. **Multi-timescale unification** — rotation, reverse-weight, and mid-workout swap are isomorphic operations.
4. **Zip-as-communication** — the internal address is also the external shorthand.
5. **Library-as-coverage** — the exercise library exists for the math, not the user.

None of these are new features. They are clarifications of what the architecture already does. The system didn't change. The description of the system got tighter. And because the description is the specification (this is a spec-first project), tighter description means tighter system.

This is the negentropy thesis applied to itself: the system absorbs the disorder of its own growth history and produces a more internally consistent architecture. The reset is not maintenance. It is the system metabolizing its own evolution.

---

## Section 5 — Directional Constraints Going Forward

### Every new feature must answer:

1. **Does it operate on the zip code address space?** If not, it is outside the system. Justify its existence or route it through an existing address.
2. **Does the constraint hierarchy (Order > Color > Axis > Equipment) govern it?** If not, it bypasses the skeleton. The skeleton does not bend.
3. **Does it absorb entropy or create it?** Features that absorb user entropy and produce better system state are aligned. Features that create entropy (ad-hoc state, unaddressed data, unrouted information) are spaghetti.
4. **Is it the same principle at a different timescale?** Before building a new system, check if an existing system already does the same thing at a different timescale. If so, extend the existing system.
5. **Does the exercise library have coverage for it?** If the feature creates new constraint intersections, verify that the library has enough valid exercises at those intersections.

### The 100-year question still holds:

Would this decision still make sense if the system runs for 100 years? If yes, build it into the skeleton. If no, build it as content that the skeleton can shed and replace.

---

🧮
