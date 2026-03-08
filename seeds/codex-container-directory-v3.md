# 🟡 Ppl± CODEX CONTAINER DIRECTORY & PLAN v3.0

Date: 2026-03-04  
Author: Claude Opus 4.6 — Temp Architect Session  
For: Jake Berry / Codex Agent Pipeline  
Repo: github.com/BigBruddaThunda/ppl-plus-ultra  
Repo state: 80/1,680 cards generated. Phase 2 active. 42 seeds planted. Envelope architecture committed.

## HOW TO USE THIS DOCUMENT

Each container below is a self-contained Codex task. Copy the container block into a Codex session as the task prompt. Codex reads the repo files listed under "Reads," writes only to the paths listed under "Writes," and validates its own output using the criteria at the bottom of each container. Containers with dependencies must wait until the listed prerequisites are merged to main. Independent containers can run in parallel across separate Codex sessions.

---

## PHASE 0 — LANGUAGE FOUNDATION

### CX-00A: Systems Glossary

**Goal:** Create `scl-deep/systems-glossary.md` — a single authoritative file defining all system-level terms used across the repo, organized into sections: pipeline, data flow, state management, resolution, validation, feedback, UX, project health.

**Depends on:** Nothing

**Reads:** `CLAUDE.md`, `middle-math/ARCHITECTURE.md`, `scl-deep/vocabulary-standard.md`, `scl-deep/publication-standard.md`, `seeds/operis-prompt-pipeline.md`

**Writes:** `scl-deep/systems-glossary.md`

**Instructions for Codex:**

Create a glossary document at `scl-deep/systems-glossary.md`. Scan the repo for all system-operation terms (pipeline, bus, inserter, scan cycle, cache hit/miss, snapshot, resolution, interlock, setpoint, filter, emit, rung, etc.) and define each one in two sentences or fewer. Organize definitions into eight sections: Pipeline (how data moves through the system), Data Flow (how content travels between files and tables), State Management (how status markers and phase tracking work), Resolution (how conflicts between dials, weights, or rules are resolved), Validation (how the scan cycle, linters, and hooks verify correctness), Feedback (how votes, bloom, and usage data loop back into the system), UX (how floors, dials, rooms, and navigation are described), and Project Health (how progress, coverage, and readiness are measured). Include a PPL-to-Systems translation table mapping Ppl concepts (zip code, deck, block, Order, Axis, etc.) to their systems-language equivalents (address, batch, container, priority dial, depth dial, etc.). Use `scl-deep/publication-standard.md` voice throughout. Follow existing frontmatter format from other `scl-deep/` files.

**Validation:** Every term used in `CLAUDE.md`'s "SYSTEMS LANGUAGE" section must appear in the glossary. No definitions exceed two sentences. The translation table must cover all 7 SCL categories.

**Does NOT:** Modify any existing file. Create new SCL rules or emojis.

### CX-00B: Systems Language Audit

**Goal:** Audit the repo for inconsistent terminology and produce `scl-deep/systems-language-audit.md`.

**Depends on:** CX-00A (glossary must exist as the standard)

**Reads:** All `.md` files in root, `seeds/`, `scl-deep/`, `middle-math/`, `deck-identities/`, `zip-web/`, `.claude/`, `.codex/`

**Writes:** `scl-deep/systems-language-audit.md`

**Instructions for Codex:**

Read every markdown file in the repo. For each file, compare the terminology used to `scl-deep/systems-glossary.md`. Flag instances where a glossary term is described using a different word (e.g., "pipeline" in one file, "workflow" in another for the same concept). Output a markdown table per file: columns are file path, line number (approximate), found term, glossary term, suggested replacement. Group by file. Sort by severity (high = glossary term exists but a completely different word is used; medium = close synonym used; low = informal shorthand). Include a summary section at the top with total files audited, total inconsistencies found, and a priority list of the ten most-repeated inconsistencies. Do NOT modify any source files — this is a read-only audit.

**Validation:** Every file in `seeds/` and `middle-math/` must appear in the audit (even if it has zero inconsistencies). The summary table must be present. File paths must be relative to repo root.

**Does NOT:** Modify any source file. This is a report only.

---

## PHASE 1 — INFRASTRUCTURE

All Phase 1 containers depend on CX-00A being merged. All are independent of each other.

### CX-01: Codex Agent Configuration & Task Architecture

**Goal:** Update `.codex/` agent definitions and create task architecture reference files.

**Depends on:** CX-00A

**Reads:** `.codex/config.toml`, `.codex/agents/*.toml`, `CLAUDE.md`, `scl-deep/systems-glossary.md`

**Writes:** `.codex/TASK-ARCHITECTURE.md`, `.codex/HANDOFF-CONTRACTS.md`, updated `.codex/agents/*.toml` (4 files)

**Instructions for Codex:**

Create `.codex/TASK-ARCHITECTURE.md` containing: the complete Codex Container index (CX-00A through CX-31, one line per container with name, dependency, wave), the wave execution plan, and the context firewall rules. Create `.codex/HANDOFF-CONTRACTS.md` defining what each Codex agent type (generator, validator, explorer, reviewer) may read and write, what is prohibited, and the handoff format between agents. Update each agent `.toml` file to reference the new architecture and contracts files in their context fields. Use glossary terms from `scl-deep/systems-glossary.md` throughout.

**Validation:** All 32 containers appear in the task architecture index. All 4 agent toml files reference the new docs. Handoff contracts cover read/write/never-touch for each agent type.

**Does NOT:** Create new agents. Modify `CLAUDE.md`.

### CX-02: Historical Events Scaffold

**Goal:** Create 366 empty markdown files in `operis-editions/historical-events/` (one per calendar date, MM-DD.md format).

**Depends on:** CX-00A

**Reads:** `operis-editions/historical-events/` (confirm directory exists), `seeds/operis-architecture.md` (historical events spec)

**Writes:** `operis-editions/historical-events/01-01.md` through `12-31.md` (366 files), `scripts/operis/scaffold_historical_events.py`

**Instructions for Codex:**

Create `scripts/operis/scaffold_historical_events.py` that generates 366 markdown files (Jan 1 through Dec 31, including Feb 29). Each file uses this frontmatter:

```yaml
date: MM-DD
status: EMPTY
events: []
envelope_version: 1
```

Body: `This date has no historical events recorded. Populate via Operis Prompt 1 (Researcher).`

The script must be idempotent — skip files that already exist. Run the script to generate all 366 files.

**Validation:** Exactly 366 files exist in `operis-editions/historical-events/`. All filenames match MM-DD.md pattern. All contain valid YAML frontmatter. Feb 29 exists.

**Does NOT:** Populate any historical events. Write editorial content.

### CX-03: Zip Converter Utilities

**Goal:** Build emoji-to-numeric and numeric-to-emoji conversion utilities and a static JSON registry of all 1,680 zip codes.

**Depends on:** CX-00A

**Reads:** `seeds/numeric-zip-system.md`, `CLAUDE.md` (emoji dictionaries), `scl-directory.md`

**Writes:** `scripts/middle-math/zip_converter.py`, `scripts/middle-math/zip_registry.py`, `middle-math/zip-registry.json`

**Instructions for Codex:**

Create `scripts/middle-math/zip_converter.py` with functions: `emoji_to_numeric(emoji_zip: str) -> str` (e.g., `"⛽🏛🪡🔵" → "2123"`), `numeric_to_emoji(numeric_zip: str) -> str` (reverse), `validate_zip(zip_str: str) -> bool` (checks valid ranges: digit 1 in 1-7, digit 2 in 1-6, digit 3 in 1-5, digit 4 in 1-8), `zip_to_deck(zip_str: str) -> int` (formula: `(order-1)*6 + axis`), `zip_to_path(emoji_zip: str) -> str` (returns `cards/[order-folder]/[axis-folder]/[type-folder]/`). Include the full emoji-to-position lookup tables from `CLAUDE.md`. CLI: `python zip_converter.py --convert "⛽🏛🪡🔵"`.

Create `scripts/middle-math/zip_registry.py` that generates `middle-math/zip-registry.json` — a file containing all 1,680 valid zip codes with fields: numeric_zip, emoji_zip, order (position + emoji + name), axis, type, color, deck_number, operator (derived from Axis × Color polarity per `CLAUDE.md`), card_path. Run the script to generate the JSON.

**Validation:** JSON contains exactly 1,680 entries. All numeric zips are unique. All deck numbers are 1-42. Round-trip conversion (emoji → numeric → emoji) is lossless for all 1,680 entries.

**Does NOT:** Modify any card files. Create new zip codes.

### CX-04: Inventory & Progress Truth Tables

**Goal:** Create scripts that report repo state, deck readiness, and exercise usage.

**Depends on:** CX-00A

**Reads:** `cards/` (scan frontmatter), `exercise-library.md`, `deck-identities/`, `deck-cosmograms/`, `scripts/progress-report.py` (existing)

**Writes:** `scripts/inventory.py`, `scripts/deck-readiness.py`, `scripts/exercise-usage-report.py`

**Instructions for Codex:**

Create `scripts/inventory.py` that scans the entire repo and outputs: total files by directory, total card stubs vs. generated vs. canonical, total seeds, total deck identities, total cosmograms, total scripts, total weight declaration files and their status (DRAFT/STUB/COMPLETE). Output as formatted markdown table to stdout.

Create `scripts/deck-readiness.py` that checks each of the 42 decks against the 5-lane campaign model (cosmogram, identity, cards, audit, canonical) and outputs a readiness matrix. For each deck: does the cosmogram exist and is it non-STUB? Does the identity doc exist? How many cards are generated/empty/canonical? Has `validate-deck.sh` been run? Output as a markdown table.

Create `scripts/exercise-usage-report.py` that parses all generated cards in `cards/`, extracts exercise names, and reports: frequency per exercise, exercises never used, exercises used more than 10 times, exercises used in only one Color variant. Reads `exercise-library.md` for the master list.

**Validation:** `inventory.py` output includes every directory in the repo structure. `deck-readiness.py` shows all 42 decks. All scripts run without errors on the current repo state.

**Does NOT:** Modify any files. Write to any directory other than `scripts/`.

### CX-05: Markdownlint Configuration

**Goal:** Configure markdownlint-cli2 for the repo.

**Depends on:** CX-00A

**Reads:** `seeds/linters-architecture.md`, `.github/linters/README.md`

**Writes:** `.github/linters/.markdownlint-cli2.jsonc`

**Instructions for Codex:**

Create `.github/linters/.markdownlint-cli2.jsonc` with rules tuned for Ppl±: allow emoji in headings (disable MD044 for emoji characters), allow long lines in code blocks, enforce consistent heading style (ATX), require blank lines around headings and lists, enforce no trailing spaces, allow HTML (some cards may use inline HTML). Disable rules that conflict with the SCL card format (e.g., MD033 for inline HTML, MD013 for line length in specific contexts). Include comments explaining each rule choice and why it fits or exempts Ppl± content.

**Validation:** `markdownlint-cli2 --config .github/linters/.markdownlint-cli2.jsonc README.md` runs without crashing (config is valid JSON5). Config file has comments explaining each rule.

**Does NOT:** Run markdownlint on the full repo (that's CX-07).

### CX-06: Frontmatter Schema & Validator

**Goal:** Create a JSON schema for card frontmatter and a validator script.

**Depends on:** CX-00A

**Reads:** `CLAUDE.md` (card stub template, status convention), `deck-identities/template.md`

**Writes:** `.github/linters/card-frontmatter-schema.json`, `scripts/validate-frontmatter.py`

**Instructions for Codex:**

Create `.github/linters/card-frontmatter-schema.json` as a JSON Schema (draft-07) that validates card frontmatter fields: zip (string, 4 emoji characters), operator (string, emoji + Latin name), status (enum: EMPTY, GENERATED, GENERATED-V2, GENERATED-V2-REGEN-NEEDED, CANONICAL), deck (integer, 1-42), order (string matching pattern), axis (string), type (string), color (string), blocks (string of emoji sequence). All fields required for GENERATED+ status; only zip, status, deck required for EMPTY.

Create `scripts/validate-frontmatter.py` that reads a card file, extracts YAML frontmatter, validates against the schema, and reports pass/fail with specific error messages. Support `--batch` flag to validate all cards in `cards/`. CLI: `python scripts/validate-frontmatter.py cards/path/to/card.md` or `python scripts/validate-frontmatter.py --batch`.

**Validation:** Run against one known-good card from Deck 08 (must pass) and one known stub (must pass for EMPTY schema). Run `--batch` and report total pass/fail count.

**Does NOT:** Modify any card files.

### CX-07: CI Lint Workflow

**Goal:** Create a GitHub Actions workflow that runs validation on push.

**Depends on:** CX-05, CX-06

**Reads:** `.github/linters/`, `scripts/validate-card.py`, `scripts/validate-frontmatter.py`

**Writes:** `.github/workflows/lint.yml`

**Instructions for Codex:**

Create `.github/workflows/lint.yml` that triggers on push to main and pull requests. Steps: (1) checkout repo, (2) set up Python 3.11, (3) run `scripts/validate-frontmatter.py --batch` on all cards, (4) run `scripts/validate-card.py` on any cards modified in the PR (use `git diff` to identify changed card files), (5) report results. Use `continue-on-error: false` for frontmatter validation (hard fail) and `continue-on-error: true` for content validation (soft warning, since many cards are stubs). Include a comment header explaining the two-tier approach.

**Validation:** Workflow YAML is valid GitHub Actions syntax. Both script paths exist. The workflow references Python 3.11.

**Does NOT:** Run the workflow (that happens on push). Install markdownlint as a step yet (defer to future container).

### CX-08: SQL Schema Materialization

**Goal:** Convert the 7 markdown schema specs into executable PostgreSQL migration files.

**Depends on:** CX-00A

**Reads:** `middle-math/schemas/*.md` (all 7 schema files + README)

**Writes:** `sql/001-create-exercise-library.sql`, `sql/002-create-exercise-families.sql`, `sql/003-create-user-ledger.sql`, `sql/004-create-user-profile.sql`, `sql/005-create-user-toggles.sql`, `sql/006-create-zip-metadata.sql`, `sql/007-populate-zip-metadata.sql`, `sql/README.md`

**Instructions for Codex:**

For each markdown schema in `middle-math/schemas/`, create a corresponding SQL migration file. Translate the table definitions, constraints, indexes, RLS policies, and triggers specified in each markdown into valid PostgreSQL 15+ DDL. For zip-metadata-schema.md, create both the table DDL (006) and the population script (007) that cross-joins series 1-7, 1-6, 1-5, 1-8 to insert all 1,680 valid zip codes. Include the `zip_to_emoji()` PL/pgSQL function from the schema spec. Create `sql/README.md` documenting: execution order, what each file does, which markdown spec it derives from, and how to run against a Supabase project.

**Validation:** All SQL files parse cleanly (no syntax errors). The population script produces exactly 1,680 rows. All FK references point to tables created in earlier-numbered files. RLS policies use `auth.uid()`.

**Does NOT:** Create tables not specified in the existing schema docs. Connect to any database.

---

## PHASE 2 — ENGINE

### CX-09: Axis Weight Declarations

**Goal:** Populate `middle-math/weights/axis-weights.md` with weight declarations for all 6 Axes.

**Depends on:** CX-00A

**Reads:** `scl-directory.md` (Axis definitions and character), `middle-math/weights/weight-system-spec.md`, `middle-math/weights/order-weights.md` (as template), `middle-math/weights/interaction-rules.md`, `scl-deep/axis-specifications.md`

**Writes:** `middle-math/weights/axis-weights.md`

**Instructions for Codex:**

Replace the STUB content in axis-weights.md with full weight declarations for all 6 Axes (🏛 Basics, 🔨 Functional, 🌹 Aesthetic, 🪐 Challenge, ⌛ Time, 🐬 Partner). For each Axis, provide: self-weight (+8 when primary), affinity weights (positive cascades to other emojis this Axis amplifies), and suppression weights (negative cascades to emojis this Axis deprioritizes). Derive all values from the Axis character descriptions in `scl-directory.md` and the deep specs in `scl-deep/axis-specifications.md`. Follow the exact format used in `order-weights.md`. Include a rationale comment for each weight value that is +6 or higher, or -4 or lower. Ensure all weights are within the [-8, +8] octave scale.

**Validation:** All 6 Axes have declarations. Every weight is on the [-8, +8] scale. No Axis has a self-weight other than +8. Format matches `order-weights.md` structure.

**Does NOT:** Modify `order-weights.md`. Create new Axes.

### CX-10: Type & Color Weight Declarations

**Goal:** Populate `middle-math/weights/type-weights.md` and `middle-math/weights/color-weights.md`.

**Depends on:** CX-00A

**Reads:** `scl-directory.md`, `middle-math/weights/weight-system-spec.md`, `middle-math/weights/order-weights.md` (template), `middle-math/weights/interaction-rules.md`, `scl-deep/type-specifications.md`, `scl-deep/color-specifications.md`

**Writes:** `middle-math/weights/type-weights.md`, `middle-math/weights/color-weights.md`

**Instructions for Codex:**

Replace STUB content in both files. For Types (5): declare affinity/suppression weights based on muscle group overlap, movement pattern compatibility, and the interaction rules (Type is soft context — lowest priority dial). For Colors (8): declare affinity/suppression weights based on equipment tier constraints, GOLD gate status, session format character, and the interaction rules (Color is hard filter — second priority after Order). Pay special attention to the GOLD rule: 🔴 and 🟣 have GOLD affinity (+6 to GOLD-gated sections); all other Colors have GOLD suppression (-8). Include format matching `order-weights.md`.

**Validation:** 5 Types and 8 Colors fully declared. GOLD gate weights correct (only 🔴 and 🟣 positive). All weights on [-8, +8] scale. No equipment tier contradictions.

**Does NOT:** Modify existing weight files. Create new Types or Colors.

### CX-11: Block Weight Declarations

**Goal:** Populate `middle-math/weights/block-weights.md` for all 22 Blocks + SAVE.

**Depends on:** CX-09, CX-10

**Reads:** `scl-directory.md` (block definitions), `CLAUDE.md` (block sequence guidelines), `middle-math/weights/weight-system-spec.md`, `middle-math/weights/order-weights.md`, `middle-math/weights/axis-weights.md`, `middle-math/weights/color-weights.md`, `scl-deep/block-specifications.md`

**Writes:** `middle-math/weights/block-weights.md`

**Instructions for Codex:**

Declare weights for all 22 Blocks and 🧮 SAVE. Block weights describe how strongly each block is activated or suppressed at a given zip code. Derive from: the block sequence guidelines in `CLAUDE.md` (which blocks appear in which Orders), the Color modifiers (🟠 merges blocks into ARAM, ⚪ extends ♨️ and 🪫, etc.), and the block-specifications deep spec. For example: 🌋 Gutter should have strong activation (+6) in 🔴 Intense and 🪐 Challenge contexts, and hard suppression (-8) in 🖼 Restoration, 🐂 Foundation, and ⚪ Mindful contexts. Format per `order-weights.md`.

**Validation:** All 23 entries (22 blocks + SAVE) declared. 🌋 Gutter suppressions match `CLAUDE.md` prohibitions. 🧈 Bread & Butter is +8 in all contexts (always present). Block counts align with Order guidelines.

**Does NOT:** Add new blocks.

### CX-12: Operator Weight Declarations

**Goal:** Populate `middle-math/weights/operator-weights.md` for all 12 Operators.

**Depends on:** CX-09, CX-10

**Reads:** `scl-directory.md` (operator table), `CLAUDE.md` (polarity split), `middle-math/weights/weight-system-spec.md`, `scl-deep/operator-specifications.md`, `seeds/almanac-macro-operators.md`

**Writes:** `middle-math/weights/operator-weights.md`

**Instructions for Codex:**

Declare weights for all 12 Operators. Operators are derived from Axis × Color polarity (Preparatory vs. Expressive). Each Operator has affinities to the Axis and Color group that produce it, and suppression toward the opposing polarity group. Also map the 12 monthly macro operators from almanac-macro-operators.md. Format per `order-weights.md`.

**Validation:** All 12 operators declared. Polarity relationships preserved (each Axis's two operators have complementary affinity/suppression patterns). Monthly operator assignments match the almanac seed.

**Does NOT:** Create new operators. Modify the polarity table.

### CX-13: Exercise Library Parser

**Goal:** Parse `exercise-library.md` into structured JSON.

**Depends on:** CX-00A

**Reads:** `exercise-library.md`

**Writes:** `scripts/middle-math/parse_exercise_library.py`, `middle-math/exercise-library.json`

**Instructions for Codex:**

Create `scripts/middle-math/parse_exercise_library.py` that reads `exercise-library.md` and extracts every exercise into a JSON array. For each exercise, capture: id (sequential within section), section (A-Q), name, scl_types (which Types it serves), order_relevance (which Orders it's appropriate for), axis_emphasis (which Axes it ranks high in), equipment_tier (numeric range), gold_gated (boolean), movement_pattern, muscle_groups, bilateral (boolean), compound (boolean). Output as `middle-math/exercise-library.json`. Include a CLI `--stats` flag that prints: total exercises, exercises per section, exercises per Type, GOLD-gated count, tier distribution.

**Validation:** JSON contains approximately 2,185 exercises (within 5% of the stated count). All 17 sections (A-Q) represented. GOLD-gated exercises match `CLAUDE.md`'s list (Section J all, Section K all, Section Q all, specific items in B, C, D). Run `--stats` and include output in commit message.

**Does NOT:** Modify `exercise-library.md`. Add exercises not in the library.

### CX-14: Weight Vector Computation Engine

**Goal:** Build a Python module that computes the full 61-value weight vector for any zip code.

**Depends on:** CX-09, CX-10, CX-11, CX-12, CX-03

**Reads:** `middle-math/weights/*.md` (all weight declarations), `middle-math/weights/interaction-rules.md`, `scripts/middle-math/zip_converter.py`

**Writes:** `scripts/middle-math/weight_vector.py`

**Instructions for Codex:**

Create `scripts/middle-math/weight_vector.py` containing: a function `compute_weight_vector(emoji_zip: str, temporal_date: date | None = None) -> dict[str, float]` that parses the weight declaration files, applies the 4-dial primary weights (+8 for each active dial emoji), cascades affinities and suppressions per dial, resolves conflicts using the hierarchy (Order > Color > Axis > Type), sums and clamps soft weights to [-8, +8], and optionally applies the temporal nudge layer if a date is provided. Returns a dictionary of all 61 emoji keys mapped to their computed weight. Include `--zip` CLI: `python weight_vector.py --zip "⛽🏛🪡🔵"` prints the full vector. Include `--compare` flag that takes two zips and shows their vector differences.

**Validation:** The worked example from weight-system-spec.md (Strength + Basics + Pull + Structured) must produce the documented result vector. Hard suppressions must override lower-priority affinities. All 61 values must be within [-8, +8].

**Does NOT:** Modify any weight declaration files. This is read-only consumption.

### CX-15: Exercise Selection Prototype

**Goal:** Build the exercise selection filter chain.

**Depends on:** CX-13, CX-14

**Reads:** `middle-math/exercise-engine/selection-algorithm.md`, `middle-math/exercise-engine/substitution-rules.md`, `middle-math/exercise-library.json` (from CX-13), `scripts/middle-math/weight_vector.py` (from CX-14)

**Writes:** `scripts/middle-math/exercise_selector.py`

**Instructions for Codex:**

Create `scripts/middle-math/exercise_selector.py` implementing the 6-step selection pipeline from selection-algorithm.md: (1) read template role, (2) extract zip constraints, (3) gather user constraints (mock as empty for prototype), (4) filter and rank candidates from exercise-library.json using the weight vector, (5) check user ledger (mock as empty), (6) return selection with prescription. The prototype uses mock user data (no database) but the full filter chain must be functional. Include `--zip` and `--block` CLI: `python exercise_selector.py --zip "⛽🏛🪡🔵" --block "🧈"` returns the top exercise candidate for Bread & Butter at that zip code. Handle edge cases: no valid candidates (trigger substitution walk), GOLD-gated exercises filtered by Color.

**Validation:** Output for ⛽🏛🪡🔵 must produce Pull-type exercises within Strength load range and Basics axis preference and Structured equipment tier. No GOLD exercises in non-GOLD colors. No barbells in 🟢 or 🟠 contexts.

**Does NOT:** Connect to a database. Generate workout cards.

### CX-16: Deck Identity Scaffold Generator

**Goal:** Script to generate deterministic portions of deck identity documents for decks 09-12.

**Depends on:** CX-03, CX-04

**Reads:** `deck-identities/template.md`, `deck-identities/deck-08-identity.md` (as example), `middle-math/zip-registry.json` (from CX-03), `exercise-library.md`

**Writes:** `scripts/deck-identity-scaffold.py`, `deck-identities/deck-09-identity.md`, `deck-identities/deck-10-identity.md`, `deck-identities/deck-11-identity.md`, `deck-identities/deck-12-identity.md`

**Instructions for Codex:**

Create `scripts/deck-identity-scaffold.py` that generates a deck identity document scaffold. For a given deck number, the script: looks up the Order × Axis from the zip registry, lists all 40 zip codes in the deck (5 Types × 8 Colors), pre-fills the frontmatter and section headers, lists the valid exercise sections from `exercise-library.md` for each Type in this deck, and marks the exercise mapping section as TODO — requires Claude Code `/build-deck-identity` session. Run for decks 09-12 (the remaining ⛽ Strength decks). Each output file must follow the exact format of `deck-identities/deck-08-identity.md`.

**Validation:** Each file contains exactly 40 zip codes. Deck numbers match Order × Axis calculation. Exercise section routing matches `CLAUDE.md` Type routing rules. Frontmatter is valid YAML.

**Does NOT:** Map specific exercises to specific zip codes (that requires editorial judgment via /build-deck-identity). Generate workout cards.

### CX-17: Ralph Loop Validation & Batch

**Goal:** Add validation to the Ralph Loop and create a batch orchestrator.

**Depends on:** CX-03

**Reads:** `scripts/ralph/ralph.sh`, `scripts/ralph/RALPH-PROMPT.md`, `zip-web/zip-web-rules.md`, `zip-web/zip-web-pods/deck-07-pods.md` (prototype)

**Writes:** `scripts/ralph/validate-pod.py`, `scripts/ralph/ralph-batch.sh`

**Instructions for Codex:**

Create `scripts/ralph/validate-pod.py` that reads a completed pod file and validates: all 40 zip codes in the deck have N/E/S/W entries, no directional neighbor shares the same Type as the source (Type exclusion rule), all neighbor zip codes are valid (exist in the 1,680 registry), no zip code is its own neighbor, and fatigue signatures are present. Report pass/fail per pod entry.

Create `scripts/ralph/ralph-batch.sh` that loops through all 42 deck pod files, runs `validate-pod.py` on each populated one, and outputs a summary. Skip stubs (files where N/E/S/W are empty).

**Validation:** Run `validate-pod.py` on `deck-07-pods.md` — must pass (it's the prototype). Run `ralph-batch.sh` — must complete without crashing, showing 1 validated and 41 stubs.

**Does NOT:** Populate any pod files. Modify the Ralph Loop prompt.

### CX-18: Design Tokens & WeightCSS Spec

**Goal:** Create design token files for the experience layer and a spec for weight-driven CSS.

**Depends on:** CX-00A

**Reads:** `seeds/art-direction.md`, `seeds/experience-layer-blueprint.md` (weight→CSS section), `scl-directory.md` (Color definitions)

**Writes:** `html/design-system/tokens.json`, `middle-math/rendering/weight-css-spec.md`

**Instructions for Codex:**

Create `html/design-system/tokens.json` containing: 8 Color palettes (each with primary, secondary, background, text, accent, border colors), 7 Order density settings (compact to spacious), 6 Axis typography settings (font weight, letter spacing, line height), base spacing scale, border radius scale, and animation timing tokens. Derive colors from the Color characters in `scl-directory.md` and the art direction seed. Use CSS custom property naming convention: `--ppl-color-[colorname]-[role]`.

Create `middle-math/rendering/weight-css-spec.md` documenting how the weight vector maps to CSS custom properties at render time. Reference the TypeScript example from experience-layer-blueprint.md. Specify: which weight dimensions control which CSS properties, the mathematical mapping functions, and fallback values when weights are neutral.

**Validation:** JSON is valid. All 8 Colors have complete palettes. All 7 Orders have density values. The CSS spec covers saturation, density, font-weight, rest-color, and border-radius at minimum.

**Does NOT:** Create functional CSS files. Build React components.

### CX-19: Agent Boundaries Document

**Goal:** Document agent boundary interlocks and update `CLAUDE.md`.

**Depends on:** CX-00A, CX-01

**Reads:** `CLAUDE.md`, `.codex/HANDOFF-CONTRACTS.md` (from CX-01), `scl-deep/systems-glossary.md`

**Writes:** `.claude/AGENT-BOUNDARIES.md`, appends to `CLAUDE.md`

**Instructions for Codex:**

Create `.claude/AGENT-BOUNDARIES.md` defining: the full read/write/never-touch matrix for Claude Code sessions, Codex sessions, and Temp Architect sessions. Include the context firewall from this plan. Define the "never-touch" list explicitly: card content in `cards/`, Operis editions in `operis-editions/`, `scl-directory.md`, `exercise-library.md`, any file requiring web research to populate. Define what constitutes a "clean handoff" between sessions (what must be committed, what must be documented in whiteboard.md, what state must be verified).

Append a "AGENT BOUNDARIES" section to `CLAUDE.md` that references `.claude/AGENT-BOUNDARIES.md` with a one-paragraph summary and a pointer to the full document.

**Validation:** The never-touch list matches the context firewall in this plan. `CLAUDE.md` append is at the end, after the existing INFRASTRUCTURE LAYER section. The boundaries document uses glossary terms.

**Does NOT:** Modify any section of `CLAUDE.md` above the append point.

---

## PHASE 3 — ROOM ARCHITECTURE & ENVELOPE SYSTEM

### CX-20: Room Schema Extension

**Goal:** Extend the database schema for multi-floor rooms, bloom state, voting, and navigation edges.

**Depends on:** CX-08

**Reads:** `middle-math/schemas/zip-metadata-schema.md`, `seeds/elevator-architecture.md`, `seeds/axis-as-app-floors.md`, `seeds/almanac-room-bloom.md`, `seeds/scl-envelope-architecture.md`

**Writes:** `sql/008-room-schema-extension.sql`, `middle-math/schemas/room-schema-extension.md`

**Instructions for Codex:**

Create PostgreSQL migration `sql/008-room-schema-extension.sql` containing: (1) room_floor_content table (zip_code FK, floor enum of 6 axis names, content_type_id 1-109, content_body, content_metadata JSONB, status EMPTY/DRAFT/PUBLISHED, timestamps; unique on zip+floor+content_type_id), (2) room_bloom_state table (user_id FK, zip_code FK, visit_count, first/last visited timestamps, personal_notes, custom_room_name, bloom_level 0-5; unique on user+zip; RLS user-only), (3) room_votes table (user_id FK, zip_code FK, vote SMALLINT -1/1, voted_at; unique on user+zip; RLS user-only), (4) room_navigation_edges table (source_zip FK, target_zip FK, direction N/E/S/W, rationale, fatigue_compatibility numeric; unique on source+direction), (5) ALTER zip_metadata adding bloom_eligible, operis_feature_count, last_featured_at, vote_score columns, (6) bloom level trigger (auto-increment at visit thresholds: 3→1, 5→2, 10→3, 25→4, 50→5), (7) vote_score materialized view.

Write companion spec `middle-math/schemas/room-schema-extension.md` matching existing schema doc format.

**Validation:** SQL parses against PostgreSQL 15+. All FKs reference tables from `sql/001-007`. RLS uses `auth.uid()`. Bloom thresholds are monotonically increasing.

**Does NOT:** Touch existing SQL files. Create Operis content.

### CX-21: Content Type Registry

**Goal:** Create a machine-readable JSON registry of all 109 content types with retrieval profiles for the envelope system.

**Depends on:** CX-00A

**Reads:** `seeds/content-types-architecture.md`, `seeds/axis-as-app-floors.md`, `seeds/scl-envelope-architecture.md` (retrieval profiles section)

**Writes:** `middle-math/schemas/content-type-registry.json`, `middle-math/schemas/content-type-registry.md`, `scripts/middle-math/validate_content_types.py`

**Instructions for Codex:**

Parse all 109 content types from `seeds/content-types-architecture.md`. For each type, create a JSON entry with: id, name, primary_floor, floor_emoji, cross_floor array, operator_affinity (emoji + name, or null), operator_emoji, curriculum_level (1-7), curriculum_name, instance_count, phase_relevance, description, and a new retrieval_profile object containing: tier_1_weight (0.0-1.0), tier_2_weight, tier_3_weight, tier_4_weight, similarity_threshold ("high"/"moderate"/"low"), derived from the Content Type Retrieval Profiles section in `seeds/scl-envelope-architecture.md`. For types not explicitly profiled in the envelope seed, infer the profile from the type's floor and character.

Create companion markdown doc and validation script. Validation script checks: 109 IDs sequential, valid floors, valid operators or null, valid curriculum levels, all retrieval_profile fields present.

**Validation:** JSON has exactly 109 entries. All retrieval profiles have all 5 fields. Workout cards (Type 1) have threshold "high". Community posts (Type 99) have threshold "low".

**Does NOT:** Create new content types. Modify the source document.

### CX-22: Floor Routing Spec

**Goal:** Define URL routing, floor-switching logic, and progressive disclosure for the experience layer.

**Depends on:** CX-03, CX-20, CX-21

**Reads:** `seeds/experience-layer-blueprint.md`, `seeds/elevator-architecture.md`, `seeds/axis-as-app-floors.md`, `seeds/mobile-ui-architecture.md`, `seeds/scl-envelope-architecture.md`

**Writes:** `middle-math/rendering/floor-routing-spec.md`, `middle-math/rendering/floor-content-matrix.md`

**Instructions for Codex:**

Create floor-routing-spec.md containing: (1) route table mapping every URL pattern from the experience blueprint to its floor, content types, and tier requirement, (2) default floor logic (🏛 firmitas as piano nobile arrival), (3) floor transition model (scroll = progressive disclosure; tab = explicit switch; URL = deep link), (4) tier gating matrix (free sees 🏛+🔨+limited ⌛; tier-1 unlocks all rooms + 🌹 + 🪐; tier-2 unlocks 🐬 coaching features), (5) progressive disclosure scroll order (🏛 top → ⌛ → 🐬 → 🌹 → 🪐 → 🔨 bottom), (6) envelope retrieval integration per floor (which floors trigger condition-based retrieval and at what threshold per the envelope architecture).

Create floor-content-matrix.md as a 6×109 matrix (floors × content types, cells = P/X/—).

**Validation:** All 109 types appear in at least one floor. All 6 floors have 5+ types. Scroll order matches elevator-architecture.md. Envelope thresholds match scl-envelope-architecture.md.

**Does NOT:** Write Next.js code. Create new URL patterns.

### CX-23: Navigation Graph Builder

**Goal:** Script to generate room-to-room navigation edges for all 1,680 zip codes.

**Depends on:** CX-03, CX-04, CX-08

**Reads:** `zip-web/zip-web-rules.md`, `zip-web/zip-web-signatures.md`, `zip-web/zip-web-registry.md`, `zip-web/zip-web-pods/deck-07-pods.md`

**Writes:** `scripts/middle-math/build_navigation_graph.py`, `middle-math/navigation/navigation-graph-spec.md`, `middle-math/navigation/navigation-graph.json`, `sql/009-populate-navigation-edges.sql`

**Instructions for Codex:**

Build a script that generates 4 directional neighbors (N=progressive/harder, E=lateral, S=regressive/easier, W=complementary) for each of the 1,680 zip codes using the 5-factor scoring from zip-web-rules.md and fatigue signatures from zip-web-signatures.md. Enforce the Type exclusion rule (no neighbor shares source Type). Output JSON (1,680 entries × 4 directions) and SQL INSERTs for the room_navigation_edges table. Include `--validate` flag and a companion spec document.

**Validation:** JSON has exactly 1,680 entries. All 4 directions populated per entry. No self-neighbors. Type exclusion holds universally. Deck 07 output should align with the hand-populated prototype pods.

**Does NOT:** Modify pod files. Override manually-populated pods.

### CX-24: Bloom State Engine

**Goal:** Build Room Bloom computation as a deterministic pure-function module.

**Depends on:** CX-20, CX-03

**Reads:** `seeds/almanac-room-bloom.md`, `seeds/axis-as-app-floors.md`, `middle-math/schemas/room-schema-extension.md`

**Writes:** `scripts/middle-math/bloom_engine.py`, `middle-math/user-context/bloom-engine-spec.md`

**Instructions for Codex:**

Create bloom_engine.py with: BloomLevel enum (EMPTY/SEEDLING/SPROUT/GROWING/BLOOMING/FULL_BLOOM at 0/1-2/3-4/5-9/10-24/25+ visits), compute_bloom_level(), bloom_content_gates() (returns which UI elements are visible at each level — from workout-card-only at EMPTY to full history + trend arrows + custom room name at FULL_BLOOM), and compute_bloom_data() (takes user data as arguments, returns bloom state). Pure functions, no database calls. CLI entry point. Write companion spec document.

**Validation:** Bloom levels monotonically non-decreasing. Content gates additive (higher includes all lower). Pure functions — no imports of database libraries.

**Does NOT:** Make database calls. Define visual CSS.

### CX-25: Vote Weight Integration

**Goal:** Define how ➕/➖ votes feed back into personal rotation weight adjustments.

**Depends on:** CX-20, CX-14

**Reads:** `middle-math/weights/weight-system-spec.md`, `middle-math/weights/interaction-rules.md`, `seeds/scl-envelope-architecture.md` (community voting section)

**Writes:** `middle-math/user-context/vote-weight-integration.md`, `scripts/middle-math/vote_weight_adjuster.py`

**Instructions for Codex:**

Create the spec and script for the two-layer voting system from the envelope architecture: (1) per-content votes rank content within similarity-matched results (the envelope is immutable; votes adjust ranking, not context), (2) per-user aggregate votes adjust the user's personal rotation weight for the voted zip code's dial emojis (+1 per ➕, -1 per ➖, clamped at +3 per emoji, decaying 0.1/month, cannot override hard suppressions). Tier-1+ subscribers have active vote weights; free users store votes latently (activated on subscription). Script: compute_vote_adjustments() and apply_votes_to_vector() as pure functions.

**Validation:** Hard suppression override holds. Decay reaches 0 at 10 months. Per-emoji clamp at +3. Pure functions, no DB calls.

**Does NOT:** Modify the core weight-vector engine. Create a popularity ranking system.

### CX-26: Operis Room Manifest Generator

**Goal:** Script to generate the 13-room Sandbox manifest for any date.

**Depends on:** CX-03, CX-04

**Reads:** `seeds/operis-sandbox-structure.md`, `seeds/operis-architecture.md`, `seeds/default-rotation-engine.md`

**Writes:** `scripts/operis/generate_room_manifest.py`, `middle-math/rotation/room-manifest-spec.md`

**Instructions for Codex:**

Create a script that takes a date and derives: (1) the daily default zip via the 3-gear rotation engine (Gear 1: day→Order, Gear 2: rolling 5-day Type cycle, Gear 3: month→Axis), (2) the 8 Color siblings (same O×A×T, all 8 Colors), (3) card status for each sibling (check file existence in cards/), (4) 5 Content Room structural slots (all share today's Order, 5 unique Types, 5 unique Axes from the 5 not used by the siblings). Output JSON manifest and human-readable markdown. Include generation pressure stats (how many siblings are EMPTY).

**Validation:** 8 siblings share O×A×T, differ only in Color. 5 Content Room slots have unique Types and unique Axes (none matching sibling Axis). Day→Order mapping matches operis-architecture.md.

**Does NOT:** Generate editorial content. Select Content Room Colors (that's editorial).

### CX-27: Superscript/Subscript Data Model

**Goal:** Define the ± exercise annotation system data model and computation.

**Depends on:** CX-20, CX-08

**Reads:** `seeds/exercise-superscript.md`, `seeds/almanac-room-bloom.md`, `middle-math/schemas/user-ledger-schema.md`, `middle-math/schemas/user-profile-schema.md`, `seeds/scl-envelope-architecture.md`

**Writes:** `middle-math/user-context/superscript-subscript-spec.md`, `scripts/middle-math/compute_superscript.py`

**Instructions for Codex:**

Define the data model: superscript (top number = suggested weight based on 1RM × Order load ceiling × rep modifier; Tier 1+ only; free users see "—"), subscript (bottom number = days since last performed; color-coded green/yellow/orange/red; available to all logged users). Create pure-function computation script with: compute_superscript(), compute_subscript(), compute_exercise_annotation(). Superscript never exceeds Order load ceiling. Subscript status thresholds: ≤7 days=recent, 8-14=moderate, 15-30=stale, >30=very_stale, null=new. Include bloom-level gating (annotations appear progressively with room visits per CX-24).

**Validation:** Superscript respects Order ceiling. Subscript non-negative. Tier gating enforced. Pure functions.

**Does NOT:** Define visual rendering. Modify user data.

### CX-28: Cosmogram Content Scaffold

**Goal:** Generate 42 cosmogram stub files and a template.

**Depends on:** CX-04

**Reads:** `deck-cosmograms/README.md`, `seeds/cosmogram-research-prompt.md`, `scl-deep/publication-standard.md`

**Writes:** `deck-cosmograms/cosmogram-template.md`, `deck-cosmograms/deck-01-cosmogram.md` through `deck-42-cosmogram.md`, `scripts/cosmogram/scaffold_cosmograms.py`

**Instructions for Codex:**

Create template with sections: One Sentence, Architectural Identity, Historical Roots, Cultural Context, The 40 Rooms, Connections, Research Sources. Create scaffold script that generates 42 stubs (zero-padded deck numbers) with correct Order×Axis metadata from the deck reference. Idempotent — skip existing files.

**Validation:** Exactly 42 files. All deck numbers 01-42. All frontmatter filled except researcher/research_session. No content in section bodies.

**Does NOT:** Generate cosmogram content. Modify existing cosmogram files.

### CX-29: Wilson Audio Route Scaffold

**Goal:** Spec the API routes and floor-specific voice registers for Wilson audio.

**Depends on:** CX-22

**Reads:** `seeds/wilson-voice-identity.md`, `seeds/voice-parser-architecture.md`, `seeds/automotive-layer-architecture.md`, `seeds/experience-layer-blueprint.md`

**Writes:** `middle-math/rendering/wilson-audio-spec.md`, `middle-math/schemas/audio-route-registry.md`

**Instructions for Codex:**

Create audio spec covering: all audio API routes (`/api/audio/operis/today`, `/api/audio/zip/[zipcode]/preview`, etc.), register-by-floor table (firmitas=front-desk, utilitas=workshop, venustas=personal, gravitas=lecture, temporitas=almanac, sociatas=agora), SSML formatting rules (pauses, emphasis, pitch), audio content assembly order per route, and tier gating (free=Operis audio only; tier-1=+zip previews; tier-2=+full read-through+Wilson Note). Create machine-readable audio route registry as companion doc.

**Validation:** All audio routes from experience blueprint covered. Register assignments align with floor characters. Tier gating matches platform architecture.

**Does NOT:** Implement TTS. Generate audio.

### CX-30: Envelope Schema & Stamping Prototype

**Goal:** Build the database schema for SCL envelopes and a prototype stamping function.

**Depends on:** CX-08, CX-14, CX-03

**Reads:** `seeds/scl-envelope-architecture.md` (full document — this is the primary spec), `middle-math/weights/interaction-rules.md`, `seeds/regional-filter-architecture.md`, `seeds/default-rotation-engine.md`

**Writes:** `sql/010-create-content-envelopes.sql`, `sql/011-create-content-pins.sql`, `middle-math/schemas/content-envelope-schema.md`, `middle-math/schemas/content-pin-schema.md`, `scripts/middle-math/envelope_stamper.py`

**Instructions for Codex:**

Create `sql/010-create-content-envelopes.sql` with the content_envelopes table from the envelope seed: id UUID PK, content_id UUID, content_table TEXT, content_type_id INTEGER, zip_code CHAR(4) nullable FK, envelope_vector (JSONB for portability; include a comment noting pgvector VECTOR(61) as the preferred production type), region TEXT, season TEXT, lunar_phase TEXT, lunar_illumination NUMERIC(3,2), daylight_hours NUMERIC(4,1), solstice_distance INTEGER, monthly_operator TEXT, day_of_week_order INTEGER, scl_tags TEXT[], envelope_version INTEGER DEFAULT 1, created_at TIMESTAMPTZ, vote_score INTEGER DEFAULT 0. Indexes: composite on (content_type_id, region), on (zip_code), on (created_at DESC), on (vote_score DESC). Include a GIN index on scl_tags.

Create `sql/011-create-content-pins.sql` with the content_pins table: id UUID PK, user_id UUID FK, envelope_id UUID FK → content_envelopes, latitude NUMERIC(10,7), longitude NUMERIC(10,7), annotation TEXT, media_urls TEXT[], visibility TEXT CHECK ('public','members','private') DEFAULT 'public'. RLS: public readable by authenticated; members readable by subscribers; private owner-only. Write restricted to owner.

Create companion markdown schema docs following existing format in `middle-math/schemas/`.

Create `scripts/middle-math/envelope_stamper.py` with: compute_envelope(zip_code: str, date: date, region: str | None = None) -> dict that computes the full envelope object for a given zip code and date. Uses `weight_vector.py` (CX-14) to compute the 61-value vector. Derives seasonal, lunar, daylight, and operator fields from the date and rotation engine logic. Returns the complete envelope dictionary matching the format in the seed document. Include CLI: `python envelope_stamper.py --zip "⛽🏛🪡🔵" --date 2026-03-04 --region "southeast-us"`.

**Validation:** SQL parses cleanly. Envelope stamper produces a 61-value vector for any valid zip code. All envelope fields from the seed spec are present. Round-trip: stamp an envelope, inspect all fields, confirm none are null except optional region.

**Does NOT:** Implement similarity search (that's CX-31). Connect to a database. Create content.

### CX-31: Envelope Similarity Function & Retrieval Prototype

**Goal:** Build the vector similarity computation and a prototype retrieval query.

**Depends on:** CX-30, CX-21

**Reads:** `seeds/scl-envelope-architecture.md` (similarity measurement, retrieval query, tier weights sections), `middle-math/schemas/content-type-registry.json` (from CX-21, for retrieval profiles)

**Writes:** `scripts/middle-math/envelope_retrieval.py`, `middle-math/schemas/retrieval-engine-spec.md`

**Instructions for Codex:**

Create `scripts/middle-math/envelope_retrieval.py` with:

1. `weighted_cosine_similarity(vector_a: list[float], vector_b: list[float], tier_weights: dict) -> float` — computes similarity using the 4-tier weighting system from the envelope seed. Tier weights are loaded from the content type's retrieval profile in `content-type-registry.json`.
2. `retrieve(live_vector: list[float], corpus: list[dict], floor: str, content_type_filter: list[int] | None, zip_filter: str | None, limit: int = 20) -> list[dict]` — the core retrieval function. Takes a live vector and a list of enveloped content items (each a dict with envelope_vector, content_type_id, vote_score, etc.). Computes similarity for each, applies the floor-specific threshold from the envelope seed (high for 🏛, moderate for ⌛ and 🪐, low for 🐬), filters by content type and zip if specified, ranks by similarity score with vote_score as tiebreaker, returns top N results.
3. CLI: `python envelope_retrieval.py --live-zip "⛽🏛🪡🔵" --date 2026-03-04 --floor temporitas --corpus sample-corpus.json` where `sample-corpus.json` is a test file with 10-20 sample enveloped content items (create this as a test fixture).

Create `middle-math/schemas/retrieval-engine-spec.md` documenting: the similarity algorithm, the tier weighting system, the floor-specific thresholds, the vote-score tiebreaker, and the relationship to the content type retrieval profiles.

**Validation:** Similarity function returns 1.0 for identical vectors. Similarity decreases monotonically as vectors diverge. Floor thresholds are applied correctly (high threshold returns fewer results than low threshold for the same corpus). Vote score breaks ties. Pure functions, no DB calls.

**Does NOT:** Implement pgvector queries. Build a real corpus. Connect to a database.

---

## DEPENDENCY MAP v3.0

```text
PHASE 0:
  CX-00A ──────────────────────────────────┐
  CX-00B ← CX-00A                         │
                                           ↓
PHASE 1 (all depend on CX-00A):           │
  CX-01  ─┐                               │
  CX-02  ─┤                               │
  CX-03  ─┤  all independent              │
  CX-04  ─┤  of each other                │
  CX-05  ─┤                               │
  CX-06  ─┤                               │
  CX-08  ─┘                               │
  CX-07  ← CX-05, CX-06                   │
                                           │
PHASE 2:                                   │
  CX-09  ← CX-00A                         │
  CX-10  ← CX-00A                         │
  CX-11  ← CX-09, CX-10                   │
  CX-12  ← CX-09, CX-10                   │
  CX-13  ← CX-00A                         │
  CX-14  ← CX-09, CX-10, CX-11, CX-12, CX-03
  CX-15  ← CX-13, CX-14                   │
  CX-16  ← CX-03, CX-04                   │
  CX-17  ← CX-03                          │
  CX-18  ← CX-00A                         │
  CX-19  ← CX-00A, CX-01                  │
                                           │
PHASE 3:                                   │
  CX-20  ← CX-08                          │
  CX-21  ← CX-00A                         │
  CX-22  ← CX-03, CX-20, CX-21            │
  CX-23  ← CX-03, CX-04, CX-08            │
  CX-24  ← CX-20, CX-03                   │
  CX-25  ← CX-20, CX-14                   │
  CX-26  ← CX-03, CX-04                   │
  CX-27  ← CX-20, CX-08                   │
  CX-28  ← CX-04                          │
  CX-29  ← CX-22                          │
  CX-30  ← CX-08, CX-14, CX-03            │
  CX-31  ← CX-30, CX-21                   │
```

## WAVE EXECUTION PLAN v3.0

**Wave 1 — Foundation (all independent, run concurrently):**  
CX-00A, CX-00B, CX-01, CX-02, CX-03, CX-04, CX-05, CX-06, CX-08

**Wave 2 — After Wave 1 merges (independent within wave):**  
CX-07, CX-09, CX-10, CX-13, CX-16, CX-17, CX-18, CX-19, CX-20, CX-21, CX-23, CX-26, CX-28

**Wave 3 — After Wave 2 merges:**  
CX-11, CX-12, CX-14, CX-22, CX-24, CX-27

**Wave 4 — After Wave 3 merges:**  
CX-15, CX-25, CX-29, CX-30

**Wave 5 — Final:**  
CX-31

## CONTEXT FIREWALL v3.0

**Codex MAY read:** `CLAUDE.md`, `scl-directory.md`, `whiteboard.md`, `README.md`, `scl-deep/`, `seeds/`, `middle-math/`, `deck-identities/`, `deck-cosmograms/README.md`, `zip-web/`, `cards/` (status checks only), `exercise-library.md` (parse only), `scripts/`

**Codex MAY write:** `middle-math/`, `scripts/`, `sql/`, `deck-cosmograms/` (stubs only), `.codex/`, `.claude/`, `.github/`, `html/design-system/`, `operis-editions/historical-events/` (scaffolds only), `scl-deep/systems-glossary.md`, `scl-deep/systems-language-audit.md`

**Codex NEVER touches:** Card content in `cards/`, Operis editions (except historical-events scaffolds), `scl-directory.md`, `exercise-library.md`, `CLAUDE.md` (only CX-19 appends), any file needing web research, any SCL rule or emoji creation/modification

## QUANTITATIVE SUMMARY

| Metric | Count |
|--------|-------|
| Total containers | 32 (CX-00A through CX-31) |
| Phase 0 | 2 |
| Phase 1 | 9 |
| Phase 2 | 11 |
| Phase 3 | 12 |
| New SQL files | 5 (007-011) |
| New Python scripts | 15 |
| New spec/reference documents | 14 |
| New JSON registries | 3 |
| Cosmogram stubs created | 42 |
| Historical event stubs created | 366 |
| Navigation edges generated | 6,720 |
| Content types registered | 109 |
| Envelope fields defined | 18 |
| Execution waves | 5 |

🧮
