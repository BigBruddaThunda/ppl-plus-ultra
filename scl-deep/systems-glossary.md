# PPL± Systems Glossary

**What this file is:**
The authoritative vocabulary for how PPL± describes its own architecture and operations.
This is the second bus. The first bus is `scl-directory.md` — the workout language.
This file governs the systems language: how pipelines work, how data flows, how the system validates, remembers, and adapts.

**How to use it:**
Reference, not narrative. Look up a term. Read its definition and PPL meaning.
Do not read this file start-to-finish during generation. Read it when you encounter a systems concept.

**Relationship to scl-directory.md:**
- `scl-directory.md` → the workout language. 61 emojis, 7 categories, 1,680 zip codes.
- `scl-deep/systems-glossary.md` → the architecture language. How the project describes its own operations.
- Both are buses. Both are authoritative. Neither overrides the other — they govern different domains.

**Authority rule:**
If a term is defined here, use this definition. Period. If a document uses a different word for the same concept, the glossary term wins in all new writing and in all patches.

---

## SECTION 1: PIPELINE TERMS (The Compiler)

Terms for describing how data moves through multi-stage transformation.

---

**Lexer**
A stage that scans raw input and emits classified tokens. Does not interpret — only classifies.
In PPL: Operis Prompt 1 (Researcher). Takes a date, emits a structured research brief with each item tagged by department and content lane. The lexer does not decide what content means. It sorts it.

---

**AST (Abstract Syntax Tree)**
A validated structural representation of content, not yet rendered into final form. The AST can be checked for structural correctness before any prose is written.
In PPL: Contract B (the enriched content brief from Operis Prompt 2). The Color of the Day is the root node. Educational lanes are branches. Content Room candidates are leaves. A structurally invalid AST surfaces before any prose is committed.

---

**IR (Intermediate Representation)**
A near-final artifact that is structurally complete but not yet committed to its destination. Reviewable and proofable. Not the emitted output.
In PPL: Contract C (the full Operis edition from Prompt 3). The IR passes human review before the Builder emits it to the repo.

---

**Emit**
The act of producing the final output artifact and writing it to its destination. Emit implies the creative work is complete; this step is mechanical.
In PPL: Prompt 4 (Builder) emits proofed files, generated cards, and committed repo state. The Builder does not make creative decisions. It resolves the IR to disk.

---

**Single-pass**
A pipeline where each stage runs exactly once in sequence. No stage re-runs based on later output.
In PPL: the current Operis pipeline is single-pass. Researcher → Content Architect → Editor → Builder, one time through.

---

**Multi-pass**
A pipeline where output from later stages feeds back into earlier stages on subsequent runs.
In PPL: the Operis-Cosmogram feedback loop is a multi-pass signal. Thin cosmogram coverage in today's edition (later stage output) informs which decks need cosmogram research (earlier stage input on a future run). The system improves its own substrate.

---

**Transpile**
Converting from one representation to another at the same abstraction level. Content doesn't change abstraction — it changes format.
In PPL: the `.md` card → HTML rendering step. The workout doesn't become more or less specified. It changes from markdown to interactive HTML. Same abstraction level, different format. Not compilation.

---

**Source map**
A file that maps compiled output back to its source, enabling debugging by tracing rendered content to its origin.
In PPL: the YAML frontmatter in every card is a source map. It maps the rendered workout back to its zip code, its operator, its deck, its block sequence. Any rendered HTML card must preserve the source map so debugging can trace back to the `.md` origin.

---

## SECTION 2: DATA FLOW TERMS (Unix / Factorio)

Terms for describing how resources move between components.

---

**Main bus**
The central resource channel that all components tap from without duplicating. When the bus updates, all agents receive the update on next read.
In PPL: `CLAUDE.md` and `scl-directory.md`. Every agent reads the bus. No agent copies bus content into its own local storage. If the bus updates, agents see the update — they don't carry stale local copies.

---

**Filter**
A single-purpose stateless transformation step. Filters do one thing. Filters compose.
In PPL: each step of card generation. Parse → derive operator → derive blocks → select exercises → format → validate. Each is a filter. Each is independent. Together they are the card generation pipeline.

---

**Pipe**
The data contract between two filters. Pipes are typed — their shape is defined and stable.
In PPL: the YAML frontmatter struct is the pipe between parse and derive. The zip code string is the pipe between the rotation engine and the Operis lexer. A broken pipe (wrong shape, missing field) surfaces immediately at the receiving filter.

---

**Tee**
A split that duplicates a data stream to two destinations without blocking either.
In PPL: the Operis construction vehicle effect. The primary output stream is the published edition. The tee'd stream is the card generation queue. Both run from the same source. Neither waits for the other.

---

**Inserter**
An automatic mechanism that moves data between systems without human invocation. Inserters are mechanical, always-on, and invisible during normal operation.
In PPL: the PostToolUse validation hook, the SessionStart dashboard hook, and the compaction recovery hook. When the inserter fails to fire, that's a hook configuration issue — not a generation issue.

---

**Belt**
A resource stream with a maximum throughput capacity. Belt saturation determines whether downstream demand can be met.
In PPL: the exercise library is a belt. Its saturation level determines whether every zip code can be fully resolved. A "belt audit" (audit-exercise-coverage.py) checks whether the library has gaps that prevent resolution at certain addresses.

---

**Backpressure**
When a downstream system signals upstream to slow down because it can't process fast enough. Self-regulating — the system adjusts automatically.
In PPL: if the Operis features zip codes faster than cards can be generated, the editorial system experiences backpressure. It must select from already-generated addresses instead of stubs. The system self-limits without requiring human intervention.

---

**Spaghetti**
Ad-hoc connections between components that bypass structured channels. The architectural opposite of a bus.
In PPL: when three seed documents define the same concept with different language — that's spaghetti. When a card generation session references a rule from memory instead of reading `CLAUDE.md` — that's spaghetti. The cure is always the same: route it through the bus.

---

## SECTION 3: STATE MANAGEMENT TERMS (Event Sourcing / Git)

Terms for describing how the system remembers and evolves over time.

---

**Event**
An immutable, timestamped record of something that happened. Events are append-only. You never update an event — you append a correction event.
In PPL: one logged set in the exercise ledger. Date, exercise, load, reps, RPE. Immutable once written.

---

**Event store**
The append-only log of all events. The source of truth for everything that has happened. It only grows.
In PPL: the exercise ledger table. The event store is the foundation of the user profile. Every projection, every recommendation, every adaptive adjustment is derived by reading from the event store.

---

**Projection**
A read-only view computed from replaying events. Projections are derived, not stored directly. If the projection formula changes, replay the event store and get a new projection — same events, different read.
In PPL: the exercise profile (estimated 1RM, trend, Order/Color history). The profile is a projection. It is not the ledger itself. You can re-derive it at any time by replaying the ledger with updated formulas.

---

**Snapshot**
A periodic materialization of current state to avoid full event replay. Snapshots are an optimization, not a source of truth. Future projections replay only events after the snapshot.
In PPL: a cached exercise profile at a point in time. Stored periodically. If the snapshot is stale, replay from the snapshot date forward.

---

**Aggregate**
The entity boundary that events belong to. Events in one aggregate are independent of events in another.
In PPL: the user-exercise pair. All events for user X performing exercise Y across all zip codes and dates form one aggregate. Cross-context translation (e.g., "user squats in 🦋 and 🏟 — what does that tell us?") operates across aggregates.

---

**Commit**
An immutable snapshot of state with a pointer to its parent.
In PPL: a completed and logged session. The user's training history is a chain of commits. Each commit knows what came before it. Revising history requires explicit intent, not accidental overwrite.

---

**HEAD**
The most recent commit. The current reference point for all forward calculations.
In PPL: the user's last logged session. The rotation engine computes from HEAD. The Junction block's suggestions are branches extending from HEAD.

---

**Branch**
A divergence from the expected path. A branch does not erase the mainline — it extends from it.
In PPL: when a user deviates from the default rotation. A user who swaps Thursday's Performance day for a Restoration session has branched. The system records the branch. The mainline is still recoverable.

---

**Merge**
Integrating a divergent path back into the mainline, carrying the divergence's history forward.
In PPL: resuming the default rotation after a deviation while accounting for the deviation in the fatigue model. The missed Performance session informs load recommendations going forward.

---

**Rebase**
Restarting from current position as if the divergence never happened.
In PPL: resuming the rotation from today's date without accounting for missed sessions. Load recommendations treat this as a fresh start. The system needs to support both merge (continuity) and rebase (clean slate) as explicit user strategies.

---

**Cherry-pick**
Selecting a single item from a different branch without merging the entire branch.
In PPL: a user on the default rotation choosing one specific zip code from a different Order. The system accommodates the choice without disrupting rotation state. The pick is logged. The rotation continues from where it was.

---

## SECTION 4: RESOLUTION TERMS (DNS / MTG)

Terms for describing how addresses become content.

---

**Resolution**
The process of converting an address into its content. Resolution is deterministic — the same address always resolves to the same content given the same system state.
In PPL: the full pipeline from zip code to rendered workout. ⛽🏛🪡🔵 resolves to "Heavy Classic Pulls." The resolution is deterministic. It doesn't change session to session. It changes only when the card is updated (GENERATED → CANONICAL), which is an explicit action.

---

**Cache hit**
When a resolved address already has stored content. No computation required — serve the cached result.
In PPL: a GENERATED or CANONICAL card file. The zip code has content. Resolution is instant.

---

**Cache miss**
When an address has no stored content and requires full resolution.
In PPL: an EMPTY stub. The system must run the full generation pipeline to resolve it. Cache misses are the generation queue.

---

**Cache warming**
Proactively resolving addresses before they're requested, to ensure hits when users arrive.
In PPL: the Operis construction vehicle pipeline. Each edition forces resolution of 8–12 addresses, converting stubs to GENERATED cards ahead of user demand. The editorial cycle warms the cache.

---

**TTL (Time To Live)**
The expiration window on cached content. Past TTL, content still serves but is queued for refresh.
In PPL: a planned mechanism where GENERATED cards are flagged for re-validation after N exercise library updates or N system rule changes. Not deletion — a staleness signal. The card still serves. The flag queues a review pass.

---

**Authoritative source**
The origin document that holds the canonical answer. When an agent encounters conflicting information, the authoritative source wins. Always.
In PPL: `CLAUDE.md` for agent instructions. `scl-directory.md` for workout rules. `scl-deep/systems-glossary.md` for systems vocabulary. Recursive resolvers (deck identity docs) check these first.

---

**Recursive resolver**
An intermediary that checks caches before querying the authoritative source. Reduces load on the authoritative source for repeat queries.
In PPL: deck identity documents. They cache exercise-to-zip mappings derived from the authoritative sources. Agents check the deck identity first. If it's stale or missing, they resolve directly against `scl-directory.md`.

---

**Alias**
Two names for the same address. Conversion between aliases is a single lookup — no computation.
In PPL: the emoji zip (⛽🏛🪡🔵) and the numeric zip (2123) are aliases. Both resolve to the same content. The emoji is the display layer. The number is the system layer. See `seeds/numeric-zip-system.md`.

---

**Priority**
The resolution order when multiple authorities conflict. Higher-priority authorities resolve first. Lower-priority authorities cannot override higher-priority resolutions.
In PPL: Order > Color > Axis > Equipment. The constraint hierarchy is a priority stack. Order is the hard ceiling. Nothing overrides it. Color is the hard filter. Axis ranks within the remaining space, then practical equipment availability resolves what can actually be run.

---

**Layer system**
A deterministic cascade for resolving competing modifications to the same entity. Eliminates ambiguity when multiple effects target the same property.
In PPL: the weight vector cascade. Layer 1 (zip code primaries) through Layer 7 (final clamped weight). Within each layer, resolution follows the constraint hierarchy. Same address + same user = same final weight. Every time.

---

## SECTION 5: VALIDATION TERMS (PLC / Opus Magnum)

Terms for describing how the system catches errors.

---

**Scan cycle**
A complete sequential run of all validation checks. Runs completely (all checks, every time), runs automatically (no manual invocation), and runs sequentially (top to bottom, deterministic order).
In PPL: the PostToolUse hook running `validate-card.py` on every card edit. The scan cycle does not skip rungs. It does not partially run. If interrupted, it runs again from the top.

---

**Rung**
A single validation rule in the scan cycle. Rungs are independent — one failing rung does not prevent other rungs from running.
In PPL: "Order load ceiling not exceeded" is a rung. "No barbells in Bodyweight" is a rung. "GOLD exercises only in Technical/Intense" is a rung. Each rung produces pass or fail. Fails are reported together after the full cycle completes.

---

**Interlock**
A hard-wired safety mechanism that structurally prevents dangerous combinations. An interlock is not detected and reported — it is prevented from forming. Higher severity than a rung.
In PPL: "Gutter never appears in Restoration, Foundation, or Mindful" is an interlock, not a rung. The generation pipeline should make this combination structurally impossible to construct, not merely detectable after the fact.

---

**Collision**
Two entities occupying the same space — a conflict that produces invalid state.
In PPL: two Color variants of the same Type using the same primary exercise (two workouts occupying the same exercise slot). Or two constraints contradicting each other on the same parameter. The collision detector (`audit-exercise-coverage.py`) runs as a belt-level audit across a deck, not per-card.

---

**Fizzle**
When an operation fails gracefully because its target became invalid. No error, no crash — the system selects a replacement and continues.
In PPL: when the Operis editorial selects a zip code for the Sandbox, but the card is EMPTY and cannot be featured. The operation fizzles. The editorial selects a replacement zip. Fizzling is the designed failure mode for any operation that targets a potentially invalid address.

---

**Poka-yoke**
Mistake-proofing through structural design. Makes the error impossible to commit in the first place, not detectable after.
In PPL: the stub template with pre-filled frontmatter (prevents wrong zip codes from being generated), the file naming convention (prevents ambiguous card identity), the GOLD gate (prevents dangerous exercises in unqualified contexts). Poka-yoke is upstream of all rungs and interlocks.

---

## SECTION 6: FEEDBACK & ADAPTATION TERMS (Control Theory / Cellular Automata)

Terms for describing how the system improves itself over time.

---

**Setpoint**
The target value for a controlled parameter. The exercise engine computes setpoints from the weight vector and user profile.
In PPL: the prescribed load, reps, and RPE at a given zip code for a given user. "185 lbs × 5 at ⛽ for this user on this zip" is a setpoint.

---

**Error signal**
The difference between setpoint and actual. The error signal feeds the adaptive engine.
In PPL: the difference between prescribed and logged performance. User prescribed 185 lbs × 5, logged 175 lbs × 4. The error signal is negative on both load and reps. The engine reads this to adjust next session's setpoint.

---

**Overshoot**
When a correction exceeds the target. The system adjusts too aggressively and passes the optimal value.
In PPL: if the engine increases next session's target too sharply after one strong performance. Design constraint: limit single-session setpoint adjustments to ±N% to prevent oscillation caused by overshoot.

---

**Steady state**
When the error signal is near zero and the system is stable at its target.
In PPL: a user consistently hitting prescribed targets. At steady state, the system's job shifts from correction to progressive overload — gradually increasing the setpoint to maintain stimulus.

---

**Oscillator**
A pattern that repeats with a fixed period.
In PPL: the rotation engine. Period-7 (Order by weekday). Period-5 (Type by rolling calendar). LCM = Period-35 before exact repetition. The oscillator produces the default weekly training rhythm.

---

**Glider**
A pattern that propagates across a grid, leaving state changes in its wake.
In PPL: the Operis weekly editorial cycle moving through the Order space (Mon→Sun), generating cards and accumulating history as it moves forward. The glider doesn't stay in one place — it moves through the space, activating and transforming.

---

**Population**
The count of active/alive cells in a system. Growth rate is a key health metric.
In PPL: the count of GENERATED + CANONICAL cards. Population / 1,680 = system completion percentage. Cards per week = growth rate. The progress dashboard tracks population.

---

**Andon**
A signal that halts production when a defect is detected. Named for the Toyota assembly line cord.
In PPL: validation failures that block a card from being committed. Future andon signals needed: "this deck's exercise coverage has gaps," "this Operis edition's Content Rooms don't span 5 unique Types," "this card's primary exercise was reclassified in a library update."

---

**Gemba**
Going to the actual place to observe the actual work. The final quality check no automated rung can replace.
In PPL: reading a generated card as a user would — not as a system architect. If the card reads like infrastructure documentation, the gemba test fails. If the tonal rules feel right and the cues land, gemba passes. Gemba is always the last check before CANONICAL.

---

## SECTION 7: USER EXPERIENCE TERMS (Slay the Spire / Dwarf Fortress)

Terms for describing the user's relationship to the system.

---

**Draft offering**
A bounded set of options presented for the user to choose from. The offering is curated, not random. The user picks one, picks none, or navigates independently.
In PPL: the Junction block's follow-up zip suggestions. 1–3 options with rationale. The user is offered a draft. They are not forced to pick from it.

---

**Relic**
A persistent passive modifier that affects all future outputs without requiring re-activation.
In PPL: user toggles. "No overhead pressing" is a relic. It doesn't fire once — it reshapes every future card the exercise engine generates for that user. Relics accumulate. The toggle system manages the relic stack.

---

**Deck thinning**
The progressive narrowing of the selection pool as the system learns the user. The pool gets tighter and more specific, not wider.
In PPL: as the exercise profile develops, exercises the user has outgrown or that provide diminishing returns are deprioritized. Deck thinning is desirable — it focuses resources on high-value selections.

---

**Embark**
The act of choosing a starting point in a pre-existing world. The world exists before the user arrives. They choose where to enter.
In PPL: the onboarding moment. The user reads the Operis, taps a room, and embarks. The 1,680-room building already exists. The user selects their entry point. This is not "starting from scratch" — it is choosing where to begin.

---

**Energy budget**
The total recoverable cost a session can spend. Every block and exercise draws from the budget. The session should approach but not exceed it.
In PPL: determined by the Order (CNS demand, volume ceiling) and modified by the Color (Intense increases budget, Mindful decreases it). A Strength session has a higher energy budget than a Restoration session. Exceeding the budget means the user doesn't recover before the next session.

---

**Synergy**
Two components whose combined value exceeds their individual values.
In PPL: block pairs (Primer + Bread & Butter in Strength), exercise pairings (antagonist supersets in Intense), and Order-Color interactions (Restoration + Mindful = deepest recovery lane). Named synergies in the block spec help agents keep synergistic blocks adjacent.

---

**Scaling**
A component whose value increases over time or repeated use.
In PPL: Hypertrophy is scaling — the muscle growth benefits compound over weeks of consistent volume. Foundation is front-loaded — immediate pattern benefit that diminishes with repetition once the pattern is established. Naming this distinction helps the Operis describe Orders accurately to new users.

---

## SECTION 8: PROJECT HEALTH TERMS (Factorio / Kaizen)

Terms for describing the production state of the repo itself.

---

**Throughput**
Units produced per unit time. Measurable and comparable across methods.
In PPL: cards generated per session, cards per week, Operis editions per week. The progress dashboard reports throughput. Increasing throughput is a project health goal.

---

**Bottleneck**
The slowest stage in the pipeline that limits total throughput. Identifying the bottleneck focuses optimization effort where it matters.
In PPL: currently exercise selection + validation (highest reasoning cost per card). The card-generator subagent was built specifically to isolate the bottleneck in a protected context, preventing it from clogging the main session.

---

**Belt saturation**
Whether a resource stream can supply all downstream demand. A saturated belt has no gaps. An undersaturated belt creates cache misses that cannot be resolved.
In PPL: does the exercise library (~2,185 exercises) cover every possible zip code constraint combination? A belt audit answers this. If certain zip codes have no valid exercises, those addresses are permanently unresolvable until the library is expanded.

---

**Tech tree**
A dependency chain where later capabilities require earlier ones to be complete. The tech tree makes dependency order self-documenting.
In PPL: the deck campaign pipeline. Cosmogram → Identity → Cards → Audit → CANONICAL. You cannot reach CANONICAL without completing every prior stage. The tech tree is why Deck 07's retrofit must precede Deck 09's identity build.

---

**Bus**
See Main bus (Section 2). The architectural opposite of spaghetti. Centralized, single-source. All components tap from it. Two buses in PPL: `scl-directory.md` (workout language) and `scl-deep/systems-glossary.md` (systems language).

---

## PPL-TO-SYSTEMS TRANSLATION TABLE

Complete lookup: PPL concept → systems term → definition source.

| PPL Concept | Systems Term | Section |
|-------------|-------------|---------|
| Operis Prompt 1 (Researcher) | Lexer | §1 Pipeline |
| Contract B (enriched content brief) | AST | §1 Pipeline |
| Contract C (full Operis edition) | IR | §1 Pipeline |
| Builder emitting cards to repo | Emit | §1 Pipeline |
| Single P1→P2→P3→P4 run | Single-pass | §1 Pipeline |
| Operis-Cosmogram multi-run loop | Multi-pass | §1 Pipeline |
| `.md` card → HTML rendering | Transpile | §1 Pipeline |
| Card YAML frontmatter | Source map | §1 Pipeline |
| CLAUDE.md + scl-directory.md | Main bus | §2 Data Flow |
| Each card generation step | Filter | §2 Data Flow |
| YAML frontmatter struct between steps | Pipe | §2 Data Flow |
| Operis → edition + card queue | Tee | §2 Data Flow |
| PostToolUse / SessionStart hook | Inserter | §2 Data Flow |
| Exercise library (~2,185 exercises) | Belt | §2 Data Flow |
| Operis can't feature stubs | Backpressure | §2 Data Flow |
| Three docs defining the same term differently | Spaghetti | §2 Data Flow |
| One logged exercise set | Event | §3 State |
| Exercise ledger table | Event store | §3 State |
| Exercise profile (1RM, trend) | Projection | §3 State |
| Cached exercise profile | Snapshot | §3 State |
| User + exercise pair | Aggregate | §3 State |
| Completed logged session | Commit | §3 State |
| User's last logged session | HEAD | §3 State |
| User deviates from default rotation | Branch | §3 State |
| Resume rotation with deviation history | Merge | §3 State |
| Resume rotation from today, ignore gap | Rebase | §3 State |
| Pick one zip from a different Order | Cherry-pick | §3 State |
| Zip code → rendered workout | Resolution | §4 Resolution |
| GENERATED or CANONICAL card | Cache hit | §4 Resolution |
| EMPTY stub | Cache miss | §4 Resolution |
| Operis construction vehicle pipeline | Cache warming | §4 Resolution |
| Planned staleness flag for GENERATED cards | TTL | §4 Resolution |
| CLAUDE.md / scl-directory.md / this file | Authoritative source | §4 Resolution |
| Deck identity document | Recursive resolver | §4 Resolution |
| Emoji zip + numeric zip for same address | Alias | §4 Resolution |
| Order > Color > Axis > Equipment | Priority | §4 Resolution |
| Weight vector cascade (Layers 1–7) | Layer system | §4 Resolution |
| validate-card.py full run | Scan cycle | §5 Validation |
| Single validation rule in validate-card.py | Rung | §5 Validation |
| "No Gutter in Restoration" (structural) | Interlock | §5 Validation |
| Two Color variants sharing a primary exercise | Collision | §5 Validation |
| Operis can't feature an EMPTY stub | Fizzle | §5 Validation |
| Stub template / GOLD gate / naming convention | Poka-yoke | §5 Validation |
| Prescribed load × reps × RPE for user | Setpoint | §6 Feedback |
| Prescribed vs. logged performance gap | Error signal | §6 Feedback |
| Engine increases setpoint too aggressively | Overshoot | §6 Feedback |
| User consistently hitting prescribed targets | Steady state | §6 Feedback |
| Rotation engine (Period-7 × Period-5) | Oscillator | §6 Feedback |
| Operis cycle moving through Order space | Glider | §6 Feedback |
| GENERATED + CANONICAL card count | Population | §6 Feedback |
| Validation failure blocking a commit | Andon | §6 Feedback |
| Reading a card as a user would | Gemba | §6 Feedback |
| Junction block follow-up zip suggestions | Draft offering | §7 UX |
| User toggles ("No overhead pressing") | Relic | §7 UX |
| Exercise pool narrowing with history | Deck thinning | §7 UX |
| User tapping their first Operis room | Embark | §7 UX |
| Order CNS demand + Color format budget | Energy budget | §7 UX |
| Primer + Bread & Butter block pairing | Synergy | §7 UX |
| Hypertrophy benefits compounding over weeks | Scaling | §7 UX |
| Cards generated per session/week | Throughput | §8 Health |
| Exercise selection + validation reasoning cost | Bottleneck | §8 Health |
| Exercise library coverage of all zip codes | Belt saturation | §8 Health |
| Cosmogram → Identity → Cards → Audit → CANONICAL | Tech tree | §8 Health |

---

## SYSTEMS-TO-PPL REVERSE TABLE

Reverse lookup: systems term → PPL implementation.

| Systems Term | PPL Implementation |
|-------------|-------------------|
| Aggregate | User-exercise pair (user X + exercise Y) |
| Alias | Emoji zip ↔ numeric zip (same content, different display layers) |
| Andon | Validation failure blocking commit; future: coverage gap signals |
| AST | Contract B: enriched content brief with Color of the Day as root node |
| Authoritative source | CLAUDE.md (agent instructions), scl-directory.md (workout rules), this file (systems vocabulary) |
| Backpressure | Operis forced to select GENERATED addresses when stubs can't be featured |
| Belt | Exercise library (~2,185 exercises) — the supply chain for all card generation |
| Belt saturation | Whether the library covers all 1,680 zip code constraint combinations |
| Bottleneck | Exercise selection + validation (highest per-card reasoning cost) |
| Branch | User deviating from default rotation |
| Bus | CLAUDE.md + scl-directory.md (main bus); systems-glossary.md (vocabulary bus) |
| Cache hit | GENERATED or CANONICAL card at a given zip |
| Cache miss | EMPTY stub — requires full resolution pipeline |
| Cache warming | Operis construction vehicle pipeline (8–12 addresses per edition) |
| Cherry-pick | User selecting one zip from a different Order mid-rotation |
| Collision | Two Color variants of the same Type using the same primary exercise |
| Commit | Completed and logged training session |
| Deck thinning | Exercise pool narrowing as user profile develops |
| Draft offering | Junction block's 1–3 suggested follow-up zip codes |
| Emit | Builder (Prompt 4) writing cards and Operis to repo |
| Embark | User tapping their first Operis room — entering the pre-existing world |
| Energy budget | CNS demand ceiling (Order) + format multiplier (Color) |
| Error signal | Gap between prescribed and logged performance |
| Event | One logged exercise set (date, exercise, load, reps, RPE) |
| Event store | Exercise ledger table |
| Filter | Single card generation step (parse, derive, select, format, validate) |
| Fizzle | Operis selection of an EMPTY stub gracefully replaced by a valid address |
| Gemba | Reading a card as a user would — the final human quality check |
| Glider | Operis weekly editorial cycle moving through the Order space |
| HEAD | User's last logged session |
| Inserter | PostToolUse validation hook; SessionStart dashboard hook |
| Interlock | Structural prevention of dangerous combinations (e.g., Gutter in Restoration) |
| IR | Contract C: full Operis edition, proofable before emission |
| Layer system | Weight vector cascade: Layers 1–7 from zip primaries to clamped output |
| Lexer | Operis Prompt 1 (Researcher): date in, tagged research brief out |
| Main bus | CLAUDE.md + scl-directory.md |
| Merge | Resuming default rotation with deviation history carried forward |
| Multi-pass | Operis-Cosmogram feedback loop improving substrate across runs |
| Oscillator | Rotation engine: Period-7 (Order) × Period-5 (Type) = Period-35 LCM |
| Overshoot | Engine adjusting setpoint too aggressively after one strong session |
| Pipe | YAML frontmatter struct between pipeline stages |
| Poka-yoke | Stub template, GOLD gate, file naming convention |
| Population | GENERATED + CANONICAL card count (current: 80 / 1,680) |
| Priority | Order > Color > Axis > Equipment constraint hierarchy |
| Projection | Exercise profile (1RM estimates, trend, history distribution) |
| Rebase | Resuming rotation from today, ignoring the gap from missed sessions |
| Recursive resolver | Deck identity document (checks exercise mappings before hitting scl-directory.md) |
| Relic | User toggle ("No overhead pressing" — reshapes all future card output) |
| Resolution | Full pipeline from zip code to rendered workout |
| Rung | Single validation rule in validate-card.py scan cycle |
| Scaling | Hypertrophy benefits compounding over consistent weeks |
| Scan cycle | validate-card.py full run on every card edit (PostToolUse inserter) |
| Setpoint | Prescribed load × reps × RPE for a given user at a given zip |
| Single-pass | Current Operis pipeline: Researcher → Architect → Editor → Builder |
| Snapshot | Cached exercise profile at a point in time |
| Source map | Card YAML frontmatter — maps rendered output back to zip, operator, deck |
| Spaghetti | Multiple docs defining the same concept differently; agents inferring rules from memory |
| Steady state | User consistently hitting prescribed targets |
| Synergy | Primer + Bread & Butter block pairing; antagonist superset pairs |
| Tech tree | Cosmogram → Identity → Cards → Audit → CANONICAL |
| Tee | Operis → published edition + card generation queue (same source, two streams) |
| Throughput | Cards generated per session or per week |
| Transpile | `.md` card → HTML rendering (same abstraction, different format) |
| TTL | Planned staleness flag on GENERATED cards after library or rule updates |

---

*This glossary is a living document. When a systems concept appears in any PPL document without a glossary term, flag it. The glossary may need expansion, or the concept may need clearer design. Route it through the bus.*

🧮
