---
planted: 2026-03-05
status: SEED
depends-on: seeds/color-context-vernacular.md, scl-deep/color-specifications.md, scl-deep/systems-glossary.md
connects-to: seeds/codex-container-directory-v3.md, seeds/operis-prompt-pipeline.md, CLAUDE.md, whiteboard.md
supersedes: nothing (first specification)
---

# Color Pipeline Posture

## Section 1 — One Sentence

The 8 Colors are cognitive postures that govern not only workout content but the entire production pipeline — how agents communicate, how tasks are classified, how dependencies are modeled, and how quality is validated across all project workflows.

---

## Section 2 — The Vehicle Principle

Real-world organizations already use color theory on vehicles. The signal precedes the words. A fire engine arriving at a building does not need to announce itself — the red says: maximum output, every system engaged, stakes are real. A postal truck does not need to explain its schedule — the blue says: known route, predictable delivery, same window every time. A school bus does not ask for patience — the yellow-orange says: learning in progress, proceed with care, not the main event.

The fleet categories:
- School buses (⚫ black) — marked for learning, signals patience required
- Bicycles (🟢 green) — stripped down, self-sufficient, no dependencies, goes anywhere
- Postal trucks (🔵 blue) — same route, same schedule, total predictability
- Hazmat transports (🟣 purple) — specialized equipment, trained operators, no margin for error
- Fire engines (🔴 red) — every system at capacity, the team knows what they are doing
- Delivery vans (🟠 orange) — multiple stops, short dwell time, efficiency lives in the transitions
- Food trucks (🟡 yellow) — mobile, unexpected locations, creative but still serving real food
- Ambulances (⚪ white) — lights on, moving carefully, the patient's condition determines pace

PPL± extends this principle into digital production. Each Color signals to agents, architects, and builders what kind of work this is and how to approach it — before a single instruction is read. The posture is pre-loaded. The fleet is pre-sorted. The agent that picks up a ⚫ Teaching task knows: define terms, read your own output as if the next reader has never seen the repo, do not assume. The agent that picks up a 🔴 Intense task knows: measure yourself by throughput, cut the filler, emit.

This is not decoration. It is pipeline architecture.

---

## Section 3 — The Eight Production Postures

---

### ⚫ Teaching — Ordo Operis (Order of the Work)

**Workout posture:** Pedagogical patience. Pattern learning at sub-maximal load. Coaching cues over exertion. Comprehension before performance. The on-ramp, not the highway.

**Vehicle archetype:** The driving school car — marked with roof signs, dual controls, deliberate speed. It signals to every other vehicle: learning in progress. The instructor in the passenger seat is the poka-yoke. The student at the wheel is the point.

**Pipeline posture:** Onboarding documents, glossaries, READMEs, templates, scaffolds, schema definitions, stub formats. The output is infrastructure for other outputs. These tasks produce the conditions under which everything else becomes possible.

**Agent register:** Explanatory. Never assumes prior knowledge. Defines terms on first use, even when the definition exists in the main bus (CLAUDE.md, scl-directory.md). Reads its own output as if the next agent has never seen the repo. Writes for someone who will arrive cold.

**Dependency model:** May read the main bus freely. May read any authoritative source in the repo. Produces output that stands alone — the Teaching artifact should not require its own context document. If a README requires a README, the posture failed.

**Validation style:** Does a fresh reader understand this without external context? The scan cycle for a Teaching artifact is single-rung: comprehension. Run the gemba test — sit in front of the document as a new collaborator on their first session and ask whether it is enough.

**Example CX containers:** CX-00A (Systems Glossary — definitions for all system-operation terms), CX-02 (Historical Events Scaffold — template structure for 366 MM-DD.md files), CX-05 (Markdownlint Config — rules as documented constraints), CX-06 (Frontmatter Schema & Validator — schema as teaching artifact for all future card authors)

**Operis pipeline role:** None directly. Teaching posture lives in the scaffold and documentation layer, not in editorial. However, the CLAUDE.md operating instructions, scl-directory.md, and exercise-library.md are all Teaching posture documents — the authoritative sources that every other agent reads before acting.

---

### 🟢 Bodyweight — Natura Operis (Nature of the Work)

**Workout posture:** Self-sufficiency. No barbell, no machine, no gym. Just the body and what it can produce. The check valve — does your built capacity transfer when the infrastructure disappears?

**Vehicle archetype:** The bicycle courier — stripped down to the minimum required, goes anywhere regardless of road conditions, zero external dependencies. Carries the payload through neighborhoods a truck cannot reach. The measure of the courier is arrival, not comfort.

**Pipeline posture:** Zero-dependency utilities. Local scripts, parsers, converters, generators that require nothing but the repo and Python stdlib. Tasks that run in airplane mode. Tools that produce correct output from repo state alone, without network access, external APIs, or database calls.

**Agent register:** Compact and direct. No external references. No calls out to services or documentation beyond the repo itself. Every import is from stdlib or a file that exists locally. If the script requires a network request, it is not Bodyweight.

**Dependency model:** Reads repo files only. Writes to `scripts/` or `middle-math/`. The dependency graph terminates at the repository boundary. A Bodyweight container that reaches outside the repo is misclassified.

**Validation style:** Does it run in airplane mode? Does it produce correct output from repo state alone? The interlock is simple: run it disconnected. If it fails, it was not Bodyweight.

**Example CX containers:** CX-03 (Zip Converter — emoji ↔ numeric conversion, array lookup only), CX-13 (Exercise Library JSON Parser — reads exercise-library.md, writes structured JSON, no network), CX-17 (Ralph Loop Validation — batch orchestrator for 41 pod stubs, reads cards/ directory, reports state)

**Operis pipeline role:** None. Bodyweight is the offline utility layer. The Operis pipeline requires network access at Prompts 1 and 2. It is not Bodyweight territory. However, the scripts that run between pipeline steps — progress checks, card validation, stub detection — operate in Bodyweight posture.

---

### 🔵 Structured — Architectura Operis (Architecture of the Work)

**Workout posture:** Standard gym session. Full equipment available. Predetermined plan. The sets, reps, and rest periods are prescribed before arriving. The work is to execute the plan, not to invent it.

**Vehicle archetype:** The postal service truck — same route, same delivery window, same sorting protocol. The driver does not decide the route. The route was decided by a system that has run it ten thousand times. Reliability is the product.

**Pipeline posture:** Systematic execution of established patterns. Deck generation once identity exists. CI workflows that run the same checks on every push. SQL migrations that follow the established schema format. Template-following tasks where the structure is already decided and the work is to fill it correctly.

**Agent register:** Precise and formulaic. Same section headers every time. No improvisation. If the template has 15 required elements, all 15 are present. The agent does not ask whether the format is right — the format is already decided. It executes.

**Dependency model:** Reads templates and patterns from existing files. Produces output in established format. The Structured agent is a high-fidelity copier of established structure, not an architect. The architecture was already resolved. This agent emits it.

**Validation style:** Does the output match the template mechanically? Are all fields present? Does the schema parse? The scan cycle for a Structured artifact is a rung-by-rung checklist against the template. Every rung must pass.

**Example CX containers:** CX-01 (Codex Agent Config — follows agent boundary pattern), CX-04 (Inventory & Progress Scripts — same report format every run), CX-07 (GitHub Actions CI Lint Workflow — YAML follows established Actions schema), CX-08 (SQL Schema Materialization — 7 migration files following migration format), CX-09 (Axis Weight Declarations — follows existing Order weight pattern), CX-10 (Type & Color Weight Declarations — same format as Axis weights), CX-12 (Operator Weight Declarations — same format as all weight declarations), CX-16 (Deck Identity Scaffold Generator — produces identity docs in established deck identity format), CX-26 (Operis Room Manifest Generator — follows established manifest format), CX-27 (Superscript/Subscript Data Model — follows schema conventions from CX-20)

**Operis pipeline role:** The Builder (Prompt 4) operates in Structured posture. It emits — it does not create. The edition was written by the Editor. The Builder's job is to proof the 8-item checklist, generate any EMPTY featured zip cards according to SCL rules, file the edition at the correct path, and commit. Same steps, every edition. No deviation.

---

### 🟣 Technical — Profundum Operis (The Deep Work)

**Workout posture:** Precision under complexity. GOLD exercises unlocked. Demonstrated competence required. Lower volume, extended rest, quality above throughput. The lift is complex enough that a small error cascades — so the protocol slows down to get it right.

**Vehicle archetype:** The hazmat transport — specialized equipment, certified operators, no margin for error. The vehicle is marked because the cargo requires particular handling. Everyone who encounters it adjusts their behavior. The driver does not rush.

**Pipeline posture:** Complex multi-file reasoning. Weight vector computation. Exercise selection filter chains. Envelope stamping. Room schema extensions that require consistency across multiple dependent systems. Anything where a small error in one file corrupts downstream resolution across a large portion of the 1,680-card space.

**Agent register:** Exact. Uses glossary terms precisely — not approximately. Includes validation criteria in every output section. Shows its work. If a weight vector is computed, the inputs are stated, the formula is shown, the output is stated, and a test case is included. The Technical agent does not ask to be trusted — it provides the evidence.

**Dependency model:** Reads many files. Cross-references extensively. The output must be consistent with all inputs simultaneously. A Technical container that passes its own tests but contradicts a constraint in scl-directory.md has failed. Consistency across the full set of authoritative sources is the bar.

**Validation style:** Does the test case pass? Does round-trip conversion hold (emoji → numeric → emoji returns the original)? Do edge cases resolve correctly? Include self-test in output. The interlock for a Technical artifact is a runnable verification step, not a visual inspection.

**Example CX containers:** CX-11 (Block Weight Declarations — all 22 blocks + SAVE, complex interaction rules), CX-14 (Weight Vector Computation Engine — 61-value vector for any zip code, full cross-product), CX-15 (Exercise Selection Filter Chain — multi-rung filter applying all four dials simultaneously), CX-18 (Design Tokens & WeightCSS — weight values to CSS custom properties, precision mapping), CX-20 (Room Schema Extension — bloom, voting, navigation schema requires consistency with CX-08), CX-21 (Content Type Registry — 109 types with retrieval profiles, cross-referenced with floor routing), CX-22 (Floor Routing Specification — zip code to floor assignment with edge cases), CX-23 (Navigation Graph Builder — 4 directional neighbors per zip, graph integrity required), CX-24 (Bloom State Engine — pure-function implementation, state machine must be formally correct), CX-25 (Vote Weight Integration — user voting feedback loop touches projection layer), CX-29 (Wilson Audio Route Specification — 3-layer keyword scoring, ~13,000 entries, no AI), CX-30 (Envelope Schema & Stamping Prototype — condition vectors across all content types), CX-31 (Envelope Similarity Function & Retrieval Prototype — must return correct results on test cases)

**Operis pipeline role:** The Content Architect (Prompt 2) operates in Technical posture. Color of the Day determination uses 7 inputs (research brief, seasonal position, monthly operator, Liberal Art, current events, content landscape, temporal arc) and must resolve consistently. The same date run twice should produce the same Color. The reasoning chain must be shown, not asserted.

---

### 🔴 Intense — Fervor Operis (The Heat of the Work)

**Workout posture:** Maximum output. Full accountability. Every system engaged. The hardest version the operator can control. The pump is real, the stakes are real, the measurement is volume produced under quality constraints.

**Vehicle archetype:** The fire engine — every system at capacity, the team has trained for this, the call is live. Not the time for process debate. The procedures were established in training. Now they execute. Stakes are real.

**Pipeline posture:** High-output production sprints measured by throughput. Forty-card deck generation. Full Operis P1–P4 pipeline run on a single date. Batch population of 366 historical events with real research. Any task where the quality bar is established by upstream infrastructure (identity docs, templates, lint config) and the remaining work is to fill the space — correctly, at volume.

**Agent register:** Economical. No filler. No hedging. Output measured in cards generated, files populated, records committed. The Intense agent does not narrate its process — it produces its output. After the session: throughput is the metric.

**Dependency model:** Reads identity documents, deck cosmograms (when populated), exercise library, and SCL rules as the upstream infrastructure. The deck identity document is the cache that was warmed by upstream Technical and Structured work. Intense execution draws on that cache at speed.

**Validation style:** Did we produce the target count? Did all outputs pass the lint pipeline (validate-card.py scan cycle)? Did zero cards fail the rung-by-rung validation checklist? Throughput is the primary metric. Every card that fails validation does not count toward throughput — it counts as a bottleneck. Fix the bottleneck before continuing.

**Example tasks:** Deck 09 generation (40 cards, after deck identity exists), Deck 10–12 generation (120 cards, after identity docs exist), historical events database population (CX-02 batch phase — 366 files, real research, one-time build), future Operis batch runs when the pipeline is automated.

**Operis pipeline role:** The Researcher (Prompt 1) on batch historical events database population operates in Intense posture — cover ground, cite sources, fill the database. The goal is 366 dated files, each with verified historical events across 5 beats. Single-date Researcher runs (daily Operis) operate closer to 🟣 Technical posture, because depth matters more than volume for a single edition.

---

### 🟠 Circuit — Nuntius Operis (The Messenger of the Work)

**Workout posture:** Station-based rotation. The clock organizes. Each station recovers while others work. Efficiency lives in the transitions, not in any single station. Loop logic required: no two adjacent stations target the same tissue.

**Vehicle archetype:** The delivery van on its route — multiple stops, short dwell time at each, the efficiency of the run is measured by successful handoffs per hour, not by how long it lingers at any address. The manifest is complete when every address has been visited.

**Pipeline posture:** Multi-target sweeps. Audits, inventory reports, batch validation, terminology consistency checks, anything that touches many files quickly and reports back without modifying source files. The Circuit agent reads broadly and writes a summary. It does not rewrite what it finds.

**Agent register:** Terse per item, comprehensive across the sweep. Summary-first with supporting detail below. Each visited file gets a terse status — pass, flag, note — not a paragraph. The report structure mirrors the circuit structure: one pass around the loop, one result per station.

**Dependency model:** Reads broadly across the repo. Writes reports (typically to whiteboard.md or to a named audit file). Does not modify source files. A Circuit container that edits the files it sweeps has broken posture — that edit is a different task.

**Validation style:** Did every target get visited? Is the summary accurate? Are zero files missed? The interlock for a Circuit pass is a count: targets in must equal targets reported. A sweep that skips five files and reports clean is a miss, not a pass.

**Example CX containers:** CX-00B (Systems Language Audit — read-only sweep of all files for terminology consistency), CX-04 (Inventory & Progress Scripts — dual-use container; its reporting function is Circuit, its script-writing function is Structured)

**Example tasks:** Running run-full-audit.sh across all generated decks. Terminology sweeps when vocabulary-standard.md is updated. Checking all 1,680 stub files for correct frontmatter format. Verifying CX container completion status across the project.

**Operis pipeline role:** The Builder's proofing checklist (8-item pass across the edition before commit) is a Circuit pass — every room visited, every check logged, summary reported. The Builder in its proofing phase operates in Circuit posture, then shifts to Structured posture for the commit sequence.

---

### 🟡 Fun — Lusus Operis (The Play of the Work)

**Workout posture:** Exploration within boundaries. Equipment tier 0–5 available. The 🏖 Sandbox block is active. Surprise is welcome. The constraint is that exploration must stay within valid SCL territory — not random, but not predetermined either.

**Vehicle archetype:** The food truck — mobile, shows up in unexpected locations, offers something that did not exist on that corner yesterday. Still serving real food. The cooking is real. The surprise is in the placement and the menu, not in whether the ingredients are edible.

**Pipeline posture:** Cosmogram research. Naming passes. New seed documents. Architectural experiments. Temp architect sessions where the output is something that did not exist before — a specification, a design, a framework, a named concept. This session is 🟡 Fun posture. This document is the food truck.

**Agent register:** Looser. Associative. Willing to draw connections that other postures would not attempt. Still architecturally grounded — the creative latitude ends where structural incoherence begins. A Fun-posture output that is surprising AND internally consistent has hit the mark. A Fun-posture output that is surprising but contradicts scl-directory.md has failed.

**Dependency model:** Reads broadly for inspiration and context. Writes new seed files. May propose new concepts that require naming. Does not modify authoritative sources — the Fun agent proposes, the Mindful review confirms or rejects.

**Validation style:** Is it architecturally sound despite being creative? Does it connect to existing seeds through explicit references? Is it surprising AND useful — or just one of those? The gemba test for a Fun artifact: does someone reading it immediately understand both what it is and why it matters?

**Example CX containers:** CX-28 (Cosmogram Content Scaffold — 42 stubs produced by a generative act of naming and structuring, not template-following). **Example tasks:** First deck cosmogram research and population. New seed documents (this document is one). Operis editorial voice experiments. Naming convention passes across a new artifact class. Temp architect sessions (Genspark, Claude.ai web) producing blueprint documents.

**Operis pipeline role:** The Editor (Prompt 3) operates with Lusus latitude when writing the 5 editorial Content Room entries. The 8 Color sibling rooms (workout content) follow Structured posture — they emit workouts. The 5 Content Rooms (Dispatch, Notice, Thread, Almanac Entry, and the wild card) are where editorial judgment lives, where the food truck parks, where the writing is original.

---

### ⚪ Mindful — Eudaimonia Operis (The Flourishing of the Work)

**Workout posture:** Deliberate slowness. Breath focus. 4-second eccentrics. Extended rest. The session ends with the operator fresher than they arrived. No training debt incurred.

**Vehicle archetype:** The ambulance in non-emergency mode — lights on, no siren, moving carefully. It is not rushing to produce output. It is checking whether the patient is stable. The care is the product. Speed would be the error.

**Pipeline posture:** Review, reflection, constraint enforcement. CANONICAL reviews of generated cards. Vocabulary standard compliance passes. Eudaimonics checks against seeds/systems-eudaimonics.md. Reading generated output as a user would — the gemba walk, not the producer's inspection. Whiteboard pruning that removes completed tasks and promotes notes-to-decisions.

**Agent register:** Considered. Never rushes to output. Checks its own work against principles before committing. Asks: does this serve the user's flourishing? Does this read right? Is this sentence something a copy editor would pass? The Mindful agent is the last reader before output becomes canonical.

**Dependency model:** Reads the constraint documents — systems-eudaimonics.md, scl-deep/vocabulary-standard.md, scl-deep/publication-standard.md — and compares all other output against them. The Mindful agent does not produce primary content. It validates that primary content meets the standards that the constraint documents establish.

**Validation style:** The gemba test — does this read right when encountered as a user, not a producer? The eudaimonics test — does this feature, wording, or architectural decision serve the user's long-term flourishing, or does it serve short-term engagement at flourishing's expense? The vocabulary test — are banned words absent? Is the factual register maintained?

**Example CX containers:** CX-19 (Agent Boundaries Document — reviews the full agent operating surface and ensures no container exceeds its declared scope; the CLAUDE.md append in CX-19 requires Mindful posture for the review that precedes it). **Example tasks:** CANONICAL review passes on generated decks. Vocabulary audits when new content types are introduced. Eudaimonics compliance reviews of new features before they move from seed to active. Whiteboard pruning sessions between phases.

**Operis pipeline role:** The publication standard (scl-deep/publication-standard.md) and the vocabulary standard (scl-deep/vocabulary-standard.md) are Eudaimonia Operis artifacts. They govern tone across all editorial output. Every Operis edition passes through the vocabulary standard before publication. The proofing checklist item 8 — "Does the tone hold across all 13 rooms?" — is a Mindful posture check embedded in the Builder's Structured sequence.

---

## Section 4 — Color Tagging Protocol

**Assignment rules:**

Every CX container gets one primary Color tag in the Codex Container Directory. The tag appears in the container's header block, alongside its phase and wave.

Every temp architect session gets a Color tag at session start. Jake declares the Color, or the architect proposes it in the first output block. The Color sets the cognitive posture for the entire session — what kind of output to produce, what kind of register to use, what validation style to apply.

Every Claude Code session gets a Color tag in its opening prompt. The session header includes `COLOR: [emoji] [Latin name]`. The tag is visible to every agent reading the session context.

Every task row on the whiteboard carries a Color tag. The Color appears after the task name. Example: `- [ ] CX-14 Weight Vector Engine 🟣`

**Primary Color governs:**
- Agent register (how the agent communicates)
- Dependency model (what it reads, what it writes to)
- Validation style (what constitutes a passing output)

**When a task spans two postures:** The primary Color is the one that governs the agent register and validation style — the dominant cognitive posture, not the secondary output characteristic. A CX-14 weight vector computation that also produces volume (Intense secondary output) is still 🟣 Technical, because the register is exact, the validation is formal, and the failure mode is cascading error — not missed throughput.

**Operis pipeline Color assignments:**
- Prompt 1 (Researcher): 🔴 Intense for batch historical events population; 🟣 Technical for single-date Operis runs
- Prompt 2 (Content Architect): 🟣 Technical — 7-input Color of the Day determination must resolve consistently
- Prompt 3 (Editor): 🟡 Fun — 5 Content Rooms require editorial creative latitude
- Prompt 4 (Builder): 🔵 Structured — emits, proofs checklist, commits

**Git branch color naming:**

Branch names use plain English color words, not Latin names. The system layer uses words everyone in the system recognizes without reference. Format: `codex/[color]-[container-description]`.

Examples:
- `codex/black-systems-glossary` (CX-00A, ⚫ Teaching)
- `codex/purple-weight-vector-engine` (CX-14, 🟣 Technical)
- `codex/red-deck09-generation` (🔴 Intense deck sprint)
- `codex/blue-ci-lint-workflow` (CX-07, 🔵 Structured)

The eight branch color words: black, green, blue, purple, red, orange, yellow, white. Each maps directly to its Color posture. No ambiguity, no lookup required.

---

## Section 5 — Negotiosum Integration

The whiteboard (whiteboard.md) is the Negotiosum — the place where work is dispatched, tracked, and completed. The Color posture system becomes the Negotiosum's organizational architecture when the whiteboard adopts Color sections as department headers.

**How it maps:**

Each Color section on the whiteboard is a department of the Negotiosum. Tasks are filed under their Color. Completion is checked by Color — a single section's tasks can be reviewed without reading the full board. Health is audited by Color — a Circuit sweep of the whiteboard identifies which departments are backlogged, which are current, which are blocked.

**Department headers use Latin names:**
- `## ⚫ Ordo Operis` — documentation, scaffolds, templates in progress
- `## 🟢 Natura Operis` — local utility scripts, parsers, zero-dependency tools
- `## 🔵 Architectura Operis` — systematic execution, template-following, CI, schemas
- `## 🟣 Profundum Operis` — complex multi-file work, engines, precision computation
- `## 🔴 Fervor Operis` — active production sprints, deck generation, batch runs
- `## 🟠 Nuntius Operis` — sweeps, audits, inventory, reporting tasks
- `## 🟡 Lusus Operis` — seeds, cosmograms, architecture experiments, naming work
- `## ⚪ Eudaimonia Operis` — reviews, CANONICAL passes, vocabulary audits, pruning

**Dispatch by Color:** When Jake adds a task to the whiteboard, it goes to the section that matches its cognitive posture. The Color is not assigned after the task is written — it is chosen as the first act of writing the task, because the Color sets the frame.

**Completion check by Color:** At the end of a session, reviewing a single Color section shows all work in that posture at a glance. No need to parse the full board looking for items.

**Health audit by Color:** A weekly 🟠 Circuit sweep of the Negotiosum itself — how many tasks per department are open, in-progress, blocked? — gives a project health picture organized by cognitive type, not by arbitrary date order.

The whiteboard restructuring that adopts this architecture is a separate task filed under 🟡 Lusus Operis (it is an architectural experiment before it becomes a structural decision) and then confirmed by ⚪ Eudaimonia Operis review.

---

## Section 6 — Relationship to Existing Architecture

**Extends** seeds/color-context-vernacular.md from workout content tonal registers into the full production pipeline. The Color Context Vernacular governs how Wilson's voice and Operis prose use Color as tonal signal. This document governs how agents, containers, and sessions use Color as cognitive posture. The two layers are parallel and non-competing. A 🔴 Intense production sprint and a 🔴-colored Operis tonal register are the same Color in two different contexts — the posture logic behind them is the same (maximum output, real stakes, measurement is throughput).

**Does not modify** the workout-layer Color definitions. The 8 Colors as equipment tiers, GOLD gates, and session format rules remain governed by scl-deep/color-specifications.md. This document adds a third context (pipeline posture) without changing the first two (workout content, tonal register).

**Uses glossary terms** from scl-deep/systems-glossary.md throughout: main bus, emit, scan cycle, rung, interlock, poka-yoke, gemba, cache hit/miss, authoritative source, bottleneck, throughput, projection, inserter. When this document uses one of those terms, it uses the glossary definition exactly — no paraphrase.

**Respects vocabulary standard** from scl-deep/vocabulary-standard.md. No banned words. No fitness-register violations. No motivational filler. The newspaper test applies to every sentence in this document.

**Informs but does not replace** the agent boundary definitions planned for .claude/AGENT-BOUNDARIES.md (CX-19). The Color posture of a container is a cognitive classification, not a permission boundary. The AGENT-BOUNDARIES document governs which files each container may write. This document governs what cognitive stance the container takes while operating. Both dimensions are necessary. Neither replaces the other.

---

## Section 7 — Open Questions

**Git branch naming:** This document recommends plain English color words (black, green, blue, purple, red, orange, yellow, white) for branch name prefixes rather than Latin names. This decision should be confirmed before the first batch of Codex containers ships. Once the first branches are created with a naming convention, changing it introduces inconsistency in the git history. The convention should be decided once and held.

**Operis edition Color tag vs Color of the Day:** The Operis Color of the Day governs the editorial posture of the edition's content (seeds/operis-color-posture.md). The production pipeline posture of the Builder running that day's edition is always 🔵 Structured. These are different things — one is the cognitive posture of the content, the other is the cognitive posture of the production run. Should the edition's frontmatter carry both tags separately? Format candidate: `color-of-day: 🟣` and `production-posture: 🔵`. Open.

**Color-tagging overhead:** Color-tagging every CX container, every session, and every whiteboard task adds annotation overhead. The overhead is justified when it aids routing — when seeing a tag immediately changes how an agent approaches the work. For a solo operator, the value is primarily in the Negotiosum structure and in the agent register discipline it enforces. The break-even point is probably when a second human joins the project — at that point, the Color tag is the fastest way to communicate what kind of work a task is, before any task description is read. The system should be ready for that transition. The tags cost little now. They pay when the team grows.

---

🧮
