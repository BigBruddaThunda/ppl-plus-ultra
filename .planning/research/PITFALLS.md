# Pitfalls Research

**Domain:** Offline text parser + weight-vector-to-CSS rendering + Claude Code skill/hook/subagent infrastructure
**Researched:** 2026-03-13
**Confidence:** HIGH (hooks/subagent behavior verified against official Claude Code docs; parser and CSS pitfalls verified against multiple authoritative sources)

---

## Critical Pitfalls

### Pitfall 1: Keyword Token Collision Between Dial Dimensions

**What goes wrong:**
A keyword is a strong signal for two different dials simultaneously. "Heavy" scores for Order (⛽ Strength) AND for Color (🟣 Technical — precision/quality association). "Easy" scores for Order (🖼 Restoration) AND Axis (🏛 Basics — accessible interpretation). When the scoring function returns max-score winners per dimension independently, collision keywords push two dimensions toward a result that is internally coherent but wrong for the user's actual intent.

**Why it happens:**
The vocabulary is built dimension-by-dimension in isolation. No cross-dimension disambiguation logic exists. When "heavy barbell pull" scores ⛽🏛🪡 cleanly but then "heavy" also presses Color toward 🟣 Technical instead of 🔵 Structured, the user gets a different room than they intended. The collision is invisible — the parse appears confident.

**How to avoid:**
Build a conflict-resolution pass after per-dimension scoring. For each token that scored in multiple dimensions, weight its contribution by which dimension it most uniquely identifies. "Heavy" should give full score to Order and zero to Color because its cross-dimension hit rate in the training vocabulary is asymmetric. Implement a `dimension_affinity_score` per keyword that biases the token's contribution toward its primary dimension. Mark collision-prone keywords explicitly in the dictionary during construction.

**Warning signs:**
During manual testing, inputs like "heavy technique session" produce 🟣 Technical Color results instead of ⚫ Teaching. Inputs like "easy recovery" route to 🖼 Restoration correctly on Order but flip Axis to 🏛 Basics instead of staying at the user's Axis default. Confidence score is high despite wrong results.

**Phase to address:**
Parser construction phase (Session C-2). Build the collision resolution pass before the dictionary reaches full scale. Retrofitting is painful once all 13K entries exist.

---

### Pitfall 2: PostToolUse Hook Fires on Canvas Writes and Breaks Validation

**What goes wrong:**
The existing PostToolUse hook on `Edit|Write` runs `validate-card.py` against any edited file matching `cards/`. When the blank-canvas infrastructure starts writing files to `canvas/` (`.tsx`, `.json`, design tokens, parser output), and when new hooks are added to auto-apply publication standard or art direction, ALL of these fire on every Write/Edit. This creates compounding hook execution where a canvas file write triggers card validation (silently fails, `|| true` suppresses), THEN fires the art-direction hook, THEN possibly fires a canvas-specific validation hook — all in a single tool call. The noise is invisible to the user but costs time on every write.

**Why it happens:**
The existing hook uses `grep -q 'cards/'` to gate card validation, which is correct isolation. But the new hooks being designed (auto-apply publication standard, art direction enforcement) have no such gating. A hook with `matcher: "Edit|Write"` and no path filter runs on every file write in the entire repo, including generated scaffolding, temp files, and test outputs.

**How to avoid:**
Every new PostToolUse hook must include an explicit path gate in its command body. Pattern: `FILE=$(parse_file_path_from_stdin); if echo "$FILE" | grep -q '[target-path-prefix]/'; then [action]; fi`. Never add a hook that runs unconditionally on all writes. For canvas-specific hooks, gate on `canvas/`. For publication standard enforcement, gate on `canvas/` OR `cards/` explicitly, not the whole repo. Document which hooks own which paths in `.claude/AGENT-BOUNDARIES.md`.

**Warning signs:**
Hook execution delay increases after adding new hooks. Running `/progress-report` or a simple card edit takes noticeably longer than before. Any PostToolUse hook output appearing in output for a file write outside its intended path.

**Phase to address:**
Phase 1 infrastructure build — before any hooks are added to the canvas system. Write the path-gating pattern into the hook specification before implementing.

---

### Pitfall 3: Stop Hook Infinite Loop via Exit Code 2

**What goes wrong:**
A Stop hook (or SubagentStop hook) that exits with code 2 blocks Claude from stopping. Claude then tries to stop again. The hook runs again. Exits 2 again. Infinite loop. This is a known, documented failure mode in Claude Code (GitHub issue #10205). The existing infrastructure uses Stop hooks for session-end tasks. Any new Stop hook that validates state before allowing Claude to stop is at risk.

**Why it happens:**
Exit code 2 from a Stop hook means "block the stop." Claude interprets this as "I must continue working." It generates another response and tries to stop again. The hook condition may never resolve (e.g., "stop only if whiteboard.md has been updated" — but if the condition is broken, Claude can't update it without the hook allowing it to proceed).

**How to avoid:**
Stop hooks must use informational exit (code 0 or code 1) only. They can inject a message via `additionalContext` asking Claude to take an action before stopping, but they must NOT block the stop itself. For mandatory pre-stop tasks (whiteboard update, session log append), use a PreToolUse hook on UserPromptSubmit that injects a reminder at session start, not a Stop blocker. For the canvas system specifically: canvas state persistence hooks should be async (`async: true`) so they do not block the stop event at all.

**Warning signs:**
Claude appears stuck in a loop of short responses followed by "Let me finish up..." without making progress. The session cannot be ended with a normal stop. Verbose mode (Ctrl+O) shows the Stop hook running repeatedly.

**Phase to address:**
Phase 1 infrastructure build, specifically when defining the canvas state persistence hook and any "end of session" cleanup hooks.

---

### Pitfall 4: Weight Vector Produces Semantically Incoherent CSS When Dials Have Opposing Signals

**What goes wrong:**
The weight-vector-to-CSS pipeline treats each dimension independently and then combines CSS custom properties. When a zip code like ⛽🌹🛒🟡 is processed, the Order (⛽ Strength) pushes toward compact/dense typography with cool-gray intensity, while the Color (🟡 Fun) pushes toward warm yellow, high saturation, and spacious playful layout. Both signals apply their full CSS output. The result is a layout that is simultaneously dense AND warm/playful — the signals cancel each other's tonal coherence. The room looks wrong without a clear rendering reason.

**Why it happens:**
The spec in `middle-math/rendering/ui-weight-derivation.md` correctly defines that Color dominates (+8 primary weight). But the implementation typically ignores the dominance rule and applies all signals additively. When CSS custom properties for typography density come from Order and color palette comes from Color, there is no built-in arbitration that says "when Order and Color conflict on density, Color wins if it differs by more than N weight points."

**How to avoid:**
The CSS derivation function must implement the constraint hierarchy from CLAUDE.md: Order beats Axis, Color beats Axis, but Color does not override Order's structural parameters (block count, density) — only its palette and saturation. Separate the CSS properties into "structural" (owned by Order: density, spacing, block rhythm) and "tonal" (owned by Color: palette, saturation, gradient). Never let Color properties override structural Order properties. Build this arbitration into the derivation spec before implementing the CSS pipeline.

**Warning signs:**
A 🖼 Restoration card renders with tight spacing because another dial pushed a high-density CSS variable. A 🏟 Performance card has warm/playful colors that contradict the clinical whitespace of the test layout. Running the CSS derivation on all 1,680 zips and reviewing extreme cases (high-order conflict with high-color signal) reveals incoherent combinations.

**Phase to address:**
Design token definition phase — before any CSS custom properties are assigned to dial weights. The arbitration layer must be in the specification, not patched in after.

---

### Pitfall 5: Parser Defaults Override User Intent on Underspecified Inputs

**What goes wrong:**
The scoring function assigns defaults when a dial dimension scores zero (e.g., no Axis keywords detected → default to 🏛 Basics, position 1). This is necessary — a parse result must be a complete 4-dial address. But defaults become wrong the moment the user's context carries implicit information. "Heavy pull today" has no Axis keywords, so 🏛 Basics is assigned. A user with a history of 🔨 Functional training and no experience with 🏛 Basics gets routed to the wrong room. The default is structurally correct but context-blind.

**Why it happens:**
The parser is designed as a stateless function: input text → parse result. It has no access to user history, onboarding preferences, or session state. This is correct for the offline/no-AI design constraint. But the routing layer that calls `routeFromParse()` applies defaults without any post-parse context injection step.

**How to avoid:**
Add a context injection layer between the parser output and the router. The parser produces a result with `confidence` and flags which dimensions used defaults (`defaulted_dimensions: ['axis', 'color']`). The routing layer checks these flags and replaces defaults with user-preference data when available (onboarding equipment selection, last-visited Axis, saved room history). The parser stays stateless. The routing layer is stateful. Keep these two concerns completely separated. The `ParseResult` interface must include `defaulted_dimensions` from day one — retrofitting this onto a shipped parser is a breaking API change.

**Warning signs:**
New users with no history consistently get routed to 🏛🔵 (Basics + Structured) as defaults regardless of what they typed. The default zip (⛽🏛🪡🔵) appears in logs far more than its actual frequency in the 1,680 address space would predict.

**Phase to address:**
Session C-2 parser implementation. The `defaulted_dimensions` field must be in the `ParseResult` interface from the start. Context injection is Session E (onboarding data) or later.

---

### Pitfall 6: MDX Parser Breaks on Emoji in Frontmatter and Block Headers

**What goes wrong:**
The `.md` card files use emoji extensively in frontmatter values (`zip: ⛽🏛🪡🔵`), in block headers (`## 🧈 Bread/Butter`), and in exercise names (`🪡 Romanian Deadlift`). MDX's `remark-mdx` pipeline and `gray-matter` handle UTF-8 emoji in YAML frontmatter inconsistently across Node.js versions and operating systems. Emoji in markdown headings render correctly in browsers but fail regex-based block section parsing that extracts content by heading text. A heading parser looking for `## .*` and then splitting on `##` breaks when block names contain multi-byte emoji sequences.

**Why it happens:**
Standard regex character classes (`\w`, `.`) do not match emoji by default in JavaScript. Emoji are multi-codepoint sequences (e.g., 🏛 is U+1F3DB, which is two UTF-16 code units in JavaScript). A regex like `/^## (.+)$/m` technically matches the heading, but downstream string operations that assume single-byte characters break on the captured group. YAML parsers (js-yaml, which gray-matter uses internally) handle emoji in values fine, but the YAML key names and value positions must not assume character count equals display width.

**How to avoid:**
Use the Unicode-aware flag (`u`) on all regexes that process card content: `/^## (.+)$/mu`. Test parsing on cards with the highest emoji density (the ±🤌, ±🚀 named cards with operator emojis in filenames). Build a card parsing test suite in Session B that explicitly tests emoji-containing headings, frontmatter values, and exercise names. Do not use `str.length` for display-width calculations in card content — use a Unicode-aware grapheme counter library (`Intl.Segmenter` in Node 16+).

**Warning signs:**
Block section extraction returns empty arrays for headings with emoji. Frontmatter `zip` value parses as a string but character-count assertions fail (a 4-emoji zip is 4 graphemes but 8+ JavaScript string units). Filename-based routing breaks because the filename contains emoji in the operator position.

**Phase to address:**
Session B (Card Rendering). Must be tested before any block section extraction logic is shipped.

---

### Pitfall 7: Subagent Context Is Clean But Produces Stale Outputs

**What goes wrong:**
A subagent (card-generator, deck-auditor) is invoked with a fresh context. Because its context is clean, it reads CLAUDE.md, exercise-library.md, and the deck identity. But if a skill was updated in the session (e.g., the deck identity was just written), the subagent reads the old version from disk — or worse, the cache. The main session's in-memory state (whiteboard changes, recently generated cards) is invisible to the subagent. The subagent then validates cards against rules that were updated mid-session, misses the newly generated cards, and reports incorrect progress counts.

**Why it happens:**
Subagents get a completely separate context window. This is by design (isolation = cleanliness). But isolation also means the subagent cannot see uncommitted changes unless they are already written to disk. If the main session has modified whiteboard.md in memory but not yet written it, the subagent reads the stale version. The generation count in the progress report is wrong.

**How to avoid:**
Write all shared state to disk before invoking subagents. The main session must flush whiteboard.md, any updated deck identity documents, and any in-progress card writes before delegating to card-generator or deck-auditor. Never invoke a subagent to validate work that the main session is currently holding in-memory. The canonical rule: subagents read from disk only. Main session must commit to disk first.

**Warning signs:**
Subagent progress reports show lower card counts than the main session's recent work. Deck-auditor flags validation failures on cards that were recently corrected in the main session. Card-generator produces exercises that were banned mid-session but not flushed to disk in the relevant files.

**Phase to address:**
Any phase that introduces subagent delegation. Document the "flush before delegate" rule in `.claude/AGENT-BOUNDARIES.md` before the first subagent is invoked on canvas work.

---

### Pitfall 8: Skill Auto-Activation Loads the Wrong Skill for Ambiguous Tasks

**What goes wrong:**
Skills activate automatically when their description matches the task context. If two skills have overlapping activation triggers — for example, `/blank-canvas` (initializes canvas workspace) and `generate-card` (generates a single workout card) — a task description like "generate the canvas for deck 09" could activate `generate-card` instead of `/blank-canvas`. The skill loads its full instructions, overrides the active context, and Claude begins generating card content instead of canvas scaffolding.

**Why it happens:**
Skill descriptions are matched by semantic similarity. If two skills share vocabulary ("generate," "canvas," "deck"), the model may load the wrong one. The more skills exist in `.claude/`, the higher the collision probability. The current repo already has `generate-card` and `build-deck-identity` as skills — adding canvas-specific skills increases the collision surface.

**How to avoid:**
Write skill `description` fields to be maximally discriminating. Use terms that appear only in that skill's domain. For the canvas system: "blank-canvas" skill description should explicitly state "for the canvas/ directory visual workspace — NOT for workout card generation." Add explicit negative conditions: "Do NOT use this skill when the task involves generating workout content for cards/ directory." Test new skills by providing the exact task description to Claude and verifying which skill (if any) activates.

**Warning signs:**
A request to "open the canvas workspace" triggers card validation instead of workspace initialization. Verbose mode shows the wrong skill's instructions loaded. The initial task output structure matches the wrong skill's output format.

**Phase to address:**
Phase 1 infrastructure, when writing the `blank-canvas` skill definition and `canvas-renderer` subagent definition.

---

## Technical Debt Patterns

Shortcuts that seem reasonable but create long-term problems.

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Hardcoding hex values in CSS instead of referencing design tokens | Faster initial styling | Palette changes require touching every hardcoded instance; breaks when Color weight derivation changes | Never — the CSS pipeline exists precisely to avoid this |
| Storing parser dictionary as a flat array instead of an indexed structure | Simpler to write | Scoring 13K entries on every input takes ~50ms at full scale on mobile; token lookup degrades | Acceptable at ≤2K entries (MVP); must be indexed before full 13K dictionary is built |
| Using string matching on emoji filenames instead of numeric zip codes | Readable filenames | Emoji string matching fails on OS path encoding differences (Windows vs Linux); filename comparisons break | Never for system operations; use numeric zip as the key, display emoji only in UI |
| Global PostToolUse hook with no path gating | Easy to write | Runs on every file write in the repo; slow; irrelevant outputs for non-card/non-canvas files | Never |
| Deriving all 30+ CSS custom properties from scratch on every render | Conceptually clean | 1,680 × 30 = 50,400 derivations on initial load; ISR cannot cache weight derivation results | Compute at build time, cache the descriptor JSON per zip; derive CSS lazily |
| Sharing the main session context for canvas work instead of using canvas-renderer subagent | Saves session switching | Canvas rewrites (v0 prompts) pollute the main session context; after 3 rewrites the context is exhausted | Never for v0-style full rewrites; use main session only for targeted edits |

---

## Integration Gotchas

Common mistakes when connecting to external services.

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Claude Code PostToolUse hooks | Using exit code 2 to "block" a PostToolUse event — PostToolUse fires after the tool succeeds, so exit 2 does not undo the write | PostToolUse cannot block; use PreToolUse to block, PostToolUse only to react |
| Claude Code Stop hooks | Blocking the stop event with exit code 2 to force whiteboard updates | Use `async: true` on Stop hooks; they run in background without blocking session end |
| MDX with gray-matter | Passing `compileMDX` the raw file content with emoji in frontmatter without a YAML parser configured for Unicode | Use `gray-matter` to strip frontmatter first, pass body-only to MDX, parse frontmatter separately |
| Subagent invocation | Invoking subagent before flushing main session writes to disk | Always `Write` all shared files before spawning a subagent |
| CSS custom property derivation | Applying Tailwind utility classes AND CSS custom properties to the same element, letting Tailwind overwrite the derived properties | Use CSS custom properties exclusively for dynamic design tokens; use Tailwind only for static layout utilities |
| Supabase RLS + weight vector API | Calling `/api/zip/[zipcode]/weight` from a client component without auth headers — the weight vector is public but the endpoint may be protected if mistakenly RLS-gated | Weight vector endpoint must be explicitly marked as public in RLS policy; it contains no user data |

---

## Performance Traps

Patterns that work at small scale but fail as usage grows.

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| Loading full 13K-entry parser dictionary on every input event (keypress) | Parser latency creeps from 6ms to 60ms+ as dictionary grows; mobile keyboard lag | Load dictionary once at app init, store in module-level variable; never re-parse the JSON on each input | At ~5K entries if loaded per-keystroke |
| Running Levenshtein distance fuzzy match across all 2,185 exercise names for every token | Parse latency exceeds 50ms target on mobile; users perceive keyboard lag | Pre-index exercise names with a trigram index or prefix trie at dictionary load time; use exact match first, fuzzy only on miss | At >500 exercise names if run naively per token |
| Computing weight vector for all 1,680 zips at runtime on ISR revalidation | Cold start takes >5 seconds; ISR revalidation blocks; Vercel function timeout | Pre-compute all 1,680 weight descriptors at build time, store as static JSON; weight computation is deterministic and can be static | Immediately on cold start if not pre-computed |
| PostToolUse hooks that run Python scripts (`validate-card.py`) on every Write to canvas/ files | Hook execution adds 2–3 seconds per file write in canvas; iterative canvas work becomes slow | Path-gate all hooks; Python interpreter startup cost is non-trivial on Windows; use `|| true` exits only where the script cannot crash Claude | After first canvas-heavy session with un-gated hooks |
| Storing design token descriptor as inline styles rather than as a CSS custom properties block on `:root` | Every React re-render re-applies all 30+ inline styles; React diffing overhead multiplies with component count | Apply weight-derived CSS custom properties to `:root` once at page load; components read them via `var(--token-name)` | At ~20+ custom properties per component if inline |

---

## "Looks Done But Isn't" Checklist

Things that appear complete but are missing critical pieces.

- [ ] **Parser confidence score:** A parse result with `confidence: 0.87` looks correct — verify that the confidence function penalizes defaulted dimensions. A result that defaults all four dials can still score 0.87 if the input has strong floor-layer signals. A confident-looking result that defaulted the zip entirely is not a valid route.
- [ ] **CSS design token system:** All 8 Color palettes are defined in `design-tokens.json` — verify that the tokens are structured as semantic tokens (e.g., `--color-structured-dominant`) not primitive values (e.g., `#4B7BEC`). Primitive tokens in components bypass the weight derivation system entirely.
- [ ] **Hook path gating:** A new PostToolUse hook is written and tested — verify that the path gate condition covers the right prefix AND that it handles the case where `file_path` is undefined (Write tool uses `file_path`, Edit tool uses `path` — the existing hook handles both; new hooks must too).
- [ ] **Subagent definition completeness:** The `canvas-renderer` subagent is defined with a `name`, `description`, `tools`, and `model` — verify the frontmatter also includes which skills it should NOT load. Without explicit exclusion, the card-generation skill may auto-activate inside a canvas subagent.
- [ ] **MDX emoji rendering:** Block headers with emoji render correctly in the browser — verify that the block section extraction logic (used for the block overview at 0.5x zoom) also correctly identifies blocks from emoji headings, not just renders them visually.
- [ ] **Canvas state persistence:** Local canvas state saves to `.local/` on change — verify that `.local/` is in `.gitignore` AND that the git snapshot command (`canvas-to-production.sh`) explicitly excludes `.local/` from what it commits. Accidentally committing local working state instead of the production snapshot corrupts the architectural record.
- [ ] **Weight vector to CSS pipeline:** The derivation function produces a descriptor JSON — verify that the CSS application step uses `setProperty` on `:root` and not inline style on individual components. Inline styles are not inheritable by child components.

---

## Recovery Strategies

When pitfalls occur despite prevention, how to recover.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Token collision causing systematic mis-routing | MEDIUM | Identify collision keywords via test suite; add `dimension_affinity_score` field to affected dictionary entries retroactively; no structural refactor needed if the interface was designed to accept the field |
| Infinite loop from Stop hook exit code 2 | LOW | Kill the Claude Code session (Ctrl+C); edit `.claude/settings.json` to remove the blocking Stop hook; restart; replace with an `async: true` informational hook |
| CSS incoherence from opposing dial signals | HIGH | Requires retrofitting the arbitration layer into the CSS derivation spec and regenerating all pre-computed descriptors; if design tokens were already shipped, Tailwind config must also be updated; avoid by building arbitration first |
| MDX emoji parsing break in production | MEDIUM | Add `u` flag to all regex patterns in the block parser; add `remark-frontmatter` plugin if gray-matter is not pre-stripping YAML; can be patched without schema changes |
| Subagent producing stale validation results | LOW | Flush all in-memory state to disk (re-run the Write operations); re-invoke the subagent; no structural change needed |
| Wrong skill auto-activating | LOW | Rename or rephrase the `description` field of the colliding skill; no code changes; test with the task description that triggered the wrong activation |
| Parser dictionary growing beyond 13K with no indexing | HIGH | Requires rebuilding the lookup structure from a flat array to an indexed structure; all scoring code that iterates the array must be refactored to use index lookups; avoid by designing the index structure before the dictionary reaches 3K entries |

---

## Pitfall-to-Phase Mapping

How roadmap phases should address these pitfalls.

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| Keyword token collision | Parser construction (Session C-2) | Manual test suite: 20 collision-prone inputs produce expected dial assignments |
| PostToolUse hook fires on wrong paths | Phase 1 infrastructure build | Hook path gating verified by writing a test file to `canvas/` and confirming card validator does NOT fire |
| Stop hook infinite loop | Phase 1 infrastructure build, before any Stop hooks are added | Verified by inspecting all Stop hooks for exit code 2 usage; async flag present on any that run blocking operations |
| Weight vector CSS incoherence | Design token specification phase, before CSS pipeline implementation | Run derivation on 5 intentionally-conflicting zips (⛽🌹🛒🟡, 🏟🌹🛒⚪, 🖼🪐🍗🔴) and verify structural vs. tonal arbitration is respected |
| Parser defaults override user intent | Session C-2 parser implementation | `ParseResult` interface includes `defaulted_dimensions` array; confirmed in type definition before any routing code is written |
| MDX emoji parsing break | Session B card rendering | Test suite includes 5 emoji-dense card files; all block sections extract correctly; `u` flag present on all content regexes |
| Subagent stale output | First phase introducing subagent delegation | AGENT-BOUNDARIES.md documents "flush before delegate" rule; verified by checking whiteboard.md state before and after subagent invocation |
| Skill auto-activation collision | Phase 1 infrastructure build, when writing canvas skill definitions | Test by invoking ambiguous task descriptions and verifying which skill (if any) Claude reports loading |

---

## Sources

- [Claude Code Hooks Reference — official docs](https://code.claude.com/docs/en/hooks) — hook lifecycle, exit codes, PostToolUse behavior, Stop hook infinite loop prevention. HIGH confidence.
- [Claude Code hooks infinite loop issue — GitHub #10205](https://github.com/anthropics/claude-code/issues/10205) — documented Stop hook infinite loop failure mode. HIGH confidence.
- [PostToolUse exit code 2 discrepancy — GitHub #19009](https://github.com/anthropics/claude-code/issues/19009) — confirmed PostToolUse cannot block tool execution (tool already ran). HIGH confidence.
- [Claude Code hooks mastery — disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) — hook patterns and `stop_hook_active` loop prevention. MEDIUM confidence.
- [CSS Variables Guide: Design Tokens — FrontendTools](https://www.frontendtools.tech/blog/css-variables-guide-design-tokens-theming-2025) — semantic vs. primitive token distinction, runtime derivation patterns. MEDIUM confidence.
- [Intent Classification pitfalls — Label Your Data](https://labelyourdata.com/articles/machine-learning/intent-classification) — taxonomy size, dimension collision, multi-intent ambiguity handling. MEDIUM confidence.
- [react-markdown emoji handling — GitHub issue #61](https://github.com/remarkjs/react-markdown/issues/61) — emoji in markdown headings edge cases. MEDIUM confidence.
- [Parse Markdown Frontmatter in MDX — DEV Community](https://dev.to/phuctm97/parse-markdown-frontmatter-in-mdx-remark-and-unified-1026) — gray-matter + MDX frontmatter separation pattern. MEDIUM confidence.
- Ppl± internal architecture: `seeds/voice-parser-architecture.md`, `middle-math/rendering/ui-weight-derivation.md`, `.claude/settings.json`, `.claude/hooks/gsd-context-monitor.js`. HIGH confidence (first-party source, read directly from repo).

---

*Pitfalls research for: Ppl± Blank Canvas Infrastructure (offline parser + CSS rendering pipeline + Claude Code skill/hook/subagent infrastructure)*
*Researched: 2026-03-13*
