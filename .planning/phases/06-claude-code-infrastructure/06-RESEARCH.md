# Phase 6: Claude Code Infrastructure - Research

**Researched:** 2026-03-15
**Domain:** Claude Code skills, subagents, PostToolUse hooks, AGENT-BOUNDARIES.md governance
**Confidence:** HIGH — primary sources are first-party project files (.claude/settings.json, .claude/agents/*.md, .claude/skills/*/SKILL.md, .claude/AGENT-BOUNDARIES.md, .claude/hooks/*.js) plus official Claude Code hooks documentation

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| CLCD-01 | /blank-canvas skill (SKILL.md with auto-invocation description) | Existing skills (generate-card, build-deck-identity, progress-report) provide exact file format and frontmatter schema; SKILL.md lives at .claude/skills/{name}/SKILL.md |
| CLCD-02 | canvas-renderer subagent definition (fresh context for v0, resumable for iteration) | Existing agents (card-generator.md, deck-auditor.md, progress-tracker.md) provide exact format; agent file lives at .claude/agents/{name}.md; disallowedTools pattern established |
| CLCD-03 | PostToolUse hook path-gated to canvas/ directory (informational, never blocking) | Existing cards/ hook in settings.json is the direct template; path-gate pattern documented in .claude/AGENT-BOUNDARIES.md; exit code behavior confirmed via official docs |
</phase_requirements>

---

## Summary

Phase 6 is a configuration authoring phase, not a code-building phase. All three deliverables (skill, subagent, hook) are markdown and JSON files that follow patterns already established in this project. The AGENT-BOUNDARIES.md document at `.claude/AGENT-BOUNDARIES.md` already contains the canvas/ path-gating specification written in Phase 1; Phase 6 makes that specification operational by wiring the actual hook and writing the AGENT-BOUNDARIES section that governs the new canvas-specific agents.

The single most important constraint is the exit code rule: the PostToolUse hook for canvas/ must exit 0 (or any code other than 2) because PostToolUse hooks cannot undo file writes — they are informational by definition. Exit code 2 in PostToolUse shows "blocking error" in the UI but the file write already happened. Using exit 2 in PostToolUse creates misleading output without providing any actual blocking capability. The existing cards/ hook in `settings.json` (line 9) is the correct reference implementation: it uses `|| true` to ensure it never exits non-zero.

The `blank-canvas` skill initializes the canvas workspace context: it reads current canvas state, reports what has been built (Phases 1-5), and sets up the session to work within canvas/ boundaries. The `canvas-renderer` subagent is scoped strictly to `canvas/components/` writes — the AGENT-BOUNDARIES.md matrix in `.claude/AGENT-BOUNDARIES.md` documents this formally.

**Primary recommendation:** Author all three deliverables using existing project files as exact templates. Add the new canvas-renderer row to the AGENT-BOUNDARIES.md Read/Write matrix. Wire the hook as a new entry in `.claude/settings.json` alongside the existing cards/ hook — do not replace or modify the existing hook.

---

## Standard Stack

### Core

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| `.claude/skills/{name}/SKILL.md` | Claude Code v1 | Skill invocation prompt | Established project pattern; all 10 existing skills follow this exact structure |
| `.claude/agents/{name}.md` | Claude Code v1 | Subagent definition | Established project pattern; 5 existing agents follow this exact structure |
| `.claude/settings.json` | Claude Code v1 | Hook wiring | Single hook configuration file; canvas/ hook appended alongside existing cards/ hook |
| `.claude/AGENT-BOUNDARIES.md` | Project v1 | Governance documentation | Already exists; Phase 6 adds canvas-renderer row and updates canvas/ section |

### Skill Frontmatter Schema

The project uses this exact frontmatter shape for skills (from `generate-card/SKILL.md` and `build-deck-identity/SKILL.md`):

```yaml
---
name: {slug}
description: {one-line description used for auto-invocation matching}
disable-model-invocation: true        # prevents model from calling this skill recursively
argument-hint: "[argument format]"    # shown in UI — omit if no arguments
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---
```

`disable-model-invocation: true` is present on all complex multi-step skills. For `blank-canvas`, this should be `true` — the skill is a workflow prompt, not a recursive invocation target.

### Agent Frontmatter Schema

The project uses this exact frontmatter shape for agents (from `card-generator.md` and `deck-auditor.md`):

```yaml
---
name: {slug}
description: {one-line description}
tools: Read, Write, Edit, Bash, Grep, Glob   # tools permitted
model: claude-{model-slug}
disallowedTools: Write, Edit                  # explicit prohibition (used for read-only agents)
skills:
  - {skill-slug}                              # optional — include if agent should use a skill
---
```

For `canvas-renderer`: omit `disallowedTools` (it needs Write/Edit for canvas/), omit `skills` (no existing skill covers canvas rendering workflow), set model to `claude-sonnet-4-6`.

### Supporting

| Item | Purpose | When to Use |
|------|---------|-------------|
| `python3 -c "import sys, json; ..."` stdin parse | Extract file_path from hook JSON input | Existing pattern in cards/ hook — proven to work |
| `grep -q 'canvas/'` | Path gate string match | Existing pattern in AGENT-BOUNDARIES.md canvas path-gating section |
| `|| true` | Prevent hook from exiting non-zero | Every informational PostToolUse hook must use this pattern |

**Installation:** No new packages. All infrastructure is configuration files only.

---

## Architecture Patterns

### Recommended File Layout

```
.claude/
├── settings.json            # add canvas/ PostToolUse hook entry here
├── AGENT-BOUNDARIES.md      # update: add canvas-renderer row + canvas/ section details
├── skills/
│   └── blank-canvas/
│       └── SKILL.md         # CLCD-01
└── agents/
    └── canvas-renderer.md   # CLCD-02
canvas/
└── AGENT-BOUNDARIES.md      # CLCD-03 exit note + Phase 6 completion marker (optional)
```

### Pattern 1: Skill as Initialization Workflow

**What:** A SKILL.md that, when invoked as `/blank-canvas`, reads the current canvas workspace state and orients the session for canvas work.

**When to use:** At the start of any session involving canvas/ development. The skill loads context so the agent knows what has been built (Phases 1-5) and what the current phase boundary is.

**Structure:**

```markdown
---
name: blank-canvas
description: Initialize the canvas workspace and load current state. Reads canvas/src/ structure, reports what phases are complete, and confirms agent is scoped to canvas/ paths only.
disable-model-invocation: true
allowed-tools: Read, Bash, Grep, Glob
---

Initialize the canvas workspace for $ARGUMENTS (optional: phase focus).

## Workflow

### 1. Load Canvas Workspace State
Read canvas/package.json to confirm the workspace is intact.
List canvas/src/ to enumerate existing modules.
List canvas/tests/ to confirm test coverage exists.

### 2. Report Phase Completion
Check which Phase 1-5 artifacts exist:
- canvas/src/types/scl.ts — Phase 1 (SCL types)
- canvas/src/weights/ — Phase 2-3 (weight tables, resolver)
- canvas/src/tokens/ — Phase 4 (design tokens)
- canvas/src/rendering/ — Phase 5 (CSS derivation pipeline)

### 3. Load Boundary Rules
Read .claude/AGENT-BOUNDARIES.md — canvas/ section.
Confirm: this session writes only to canvas/ paths.
Confirm: no writes to cards/, html/, web/, middle-math/.

### 4. Report Current State
Output a summary: which phases are complete, which tests pass,
what canvas/components/ contains (if anything exists yet).
```

**Key constraint:** `allowed-tools` should NOT include Write/Edit — the skill is an orientation tool. Any writes during a canvas session happen in the calling agent or main session, not inside the skill.

### Pattern 2: Subagent with Explicit Scope Constraint

**What:** A canvas-renderer agent definition that limits writes to `canvas/components/` and always reads AGENT-BOUNDARIES.md before any file write.

**When to use:** When generating HTML/TSX components that consume canvas CSS custom properties. The subagent keeps component generation isolated from the main session context.

**Structure:**

```markdown
---
name: canvas-renderer
description: Generates canvas/components/ HTML or TSX rendering artifacts. Scoped strictly to canvas/components/ — never writes to cards/, html/, or web/.
tools: Read, Write, Edit, Bash, Grep, Glob
model: claude-sonnet-4-6
---

You are the Ppl± canvas renderer agent. You generate HTML/TSX component files
inside canvas/components/ using the CSS custom property pipeline built in Phases 1-5.

Before any write:
1. Confirm the destination path starts with canvas/components/
2. If path does not start with canvas/components/ — STOP. Report the conflict. Do not write.

## Scope: What You May Write
- canvas/components/**  — HTML, TSX, or CSS component files only

## Scope: What You Never Touch
- cards/**     — workout card content is Claude Code / card-generator territory
- html/**      — production HTML layer (Phase 4/5 scope)
- web/**       — Next.js application
- middle-math/ — computation engine (source data only)

## Before Generating Any Component
1. Read canvas/src/rendering/index.ts — understand the public rendering API
2. Read canvas/src/tokens/tokens.ts — understand available token structure
3. Confirm the CSS custom properties you'll use exist in weightsToCSSVars() output

## Art Direction Constraint
All canvas/ components use the intaglio/banknote engraving aesthetic:
- Fine hatching patterns for backgrounds (not solid fills)
- High-contrast linework (not gradients with soft edges)
- Guilloche-style decorative borders where borders exist
- Typography: serif or mono, never rounded sans
Apply via CSS classes — never inline styles.
```

### Pattern 3: Path-Gated PostToolUse Hook

**What:** A hook entry in `.claude/settings.json` that fires on Edit/Write to any file, checks if the path starts with `canvas/`, and if so runs an informational art direction check.

**When to use:** Automatically on every canvas/ file write.

**Critical rules:**
- NEVER exit with code 2. PostToolUse cannot undo writes. Exit 2 shows "blocking error" UI but write already succeeded — it is misleading noise.
- Use `|| true` to ensure the hook never exits non-zero.
- Read file_path from stdin JSON, not from environment variable (the `$CLAUDE_TOOL_INPUT` env approach in the existing cards/ hook is the established project pattern — use the same approach for consistency).
- The path-gate grep must match relative paths (`canvas/`) not absolute paths.

**Hook entry for settings.json:**

```json
{
  "matcher": "Edit|Write",
  "hooks": [
    {
      "type": "command",
      "command": "FILE=$(echo \"$CLAUDE_TOOL_INPUT\" | python3 -c \"import sys, json; d=json.load(sys.stdin); print(d.get('file_path') or d.get('path') or '')\" 2>/dev/null); if echo \"$FILE\" | grep -q 'canvas/'; then echo \"--- Canvas write: $FILE ---\"; if echo \"$FILE\" | grep -q 'cards/\\|html/\\|web/\\|middle-math/'; then echo \"WARNING: canvas-renderer attempted write outside canvas/ scope: $FILE\"; fi; fi"
    }
  ]
}
```

This entry is appended as a new element in the `PostToolUse` array alongside the existing cards/ hook. Do not merge them into one command.

### Pattern 4: AGENT-BOUNDARIES.md Canvas Section Update

**What:** Add canvas-renderer to the agent roster table and the Read/Write matrix in `.claude/AGENT-BOUNDARIES.md`, and document the "flush before delegate" rule explicitly.

**When to use:** AGENT-BOUNDARIES.md is the single governance document for all agent scopes. Phase 6 makes the canvas-renderer agent official.

**Additions to the matrix:**

```markdown
| `canvas/components/**` | R/W | — | — | — | — | R/W (scope only) |
```

New row in the Agent Roster table:

```markdown
| **canvas-renderer** | Subagent | claude-sonnet-4-6 | Canvas component generation scoped to canvas/components/ only |
```

New Per-Agent section:

```markdown
### canvas-renderer Subagent
- Writes: **only to canvas/components/**. Any other write is a boundary violation.
- Reads: canvas/src/ (rendering API), canvas/src/tokens/ (token structure), .claude/AGENT-BOUNDARIES.md
- Never writes to: cards/, html/, web/, middle-math/
- Art direction: intaglio/banknote engraving aesthetic enforced on all component output
- "Flush before delegate" rule: if this agent produces stdout output before delegating to another tool, stdout must be flushed first to avoid interleaved output
```

### Anti-Patterns to Avoid

- **Exit code 2 in PostToolUse:** PostToolUse hooks fire after the write succeeds. Exit 2 surfaces a "blocking error" to the UI but cannot undo the write. It creates alarming but meaningless noise. Always exit 0 (or use `|| true`).
- **Absolute path matching in hooks:** The `file_path` field in hook JSON may be absolute or relative depending on context. Match on `canvas/` substring (`grep -q 'canvas/'`), not on an absolute path prefix like `/Users/...`.
- **Write/Edit in skill allowed-tools:** Skills are prompts, not agents. A skill should orient and guide; the calling context performs writes. The `blank-canvas` skill should be read-only (`allowed-tools: Read, Bash, Grep, Glob`).
- **Merging canvas/ and cards/ hooks into one command:** Keep them as separate entries in the PostToolUse array. Combining them creates a maintenance hazard and makes path-gating logic harder to audit.
- **Subagent scope drift:** The canvas-renderer subagent body must contain the scope constraint as its first instruction — before any workflow steps. Scope constraints buried after workflow steps get skipped when the agent is confident.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Parsing hook JSON input | Custom argument parser or env var | `python3 -c "import sys, json; d=json.load(sys.stdin)"` | Established project pattern; handles both `file_path` and `path` field variants |
| Hook debouncing | Custom debounce logic | `|| true` + informational stdout only | PostToolUse hooks can't block anyway — debouncing is irrelevant |
| Canvas state tracking | Custom state file | Read canvas/src/ directory listing on skill invocation | Directory structure is the state; no state file needed for Phase 6 |
| Agent model selection | Research model capabilities | `claude-sonnet-4-6` | This is the project standard model; all existing subagents use this or haiku |

**Key insight:** Phase 6 delivers configuration artifacts, not computation. The only "code" is the bash one-liner in the hook command. Every other deliverable is a markdown file.

---

## Common Pitfalls

### Pitfall 1: Path Gate Fails on Absolute vs Relative Paths

**What goes wrong:** The hook's grep checks `^canvas/` (caret anchor) but `file_path` in the JSON may be an absolute path (`/Users/.../canvas/src/...`). The path gate never fires.

**Why it happens:** The `file_path` field in PostToolUse JSON is whatever path Claude Code received — it may be absolute or relative depending on how the tool was invoked.

**How to avoid:** Use `grep -q 'canvas/'` without a caret anchor. The substring match catches both `/absolute/path/canvas/` and `canvas/relative/path`.

**Warning signs:** The hook never produces output when canvas/ files are written.

### Pitfall 2: Hook Exits Non-Zero

**What goes wrong:** The validation command fails for any reason (python not in PATH, script error, grep returns no matches), exits non-zero, and the hook propagates a non-zero exit. If the hook exits 2, the UI shows a misleading "blocking error" on every canvas/ write.

**Why it happens:** Shell commands that find no matches exit non-zero by default. `grep -q` returns 1 when no match is found.

**How to avoid:** End every hook command with `|| true`. The gsd-context-monitor.js pattern of `process.exit(0)` in all branches is the Node equivalent.

**Warning signs:** Claude Code session shows error indicators after normal canvas/ file writes.

### Pitfall 3: Skill Allowed-Tools Includes Write

**What goes wrong:** If `blank-canvas/SKILL.md` includes `Write` in `allowed-tools`, Claude Code may attempt to invoke the skill to perform writes, creating circular invocation paths.

**Why it happens:** Skills with Write permission look like valid tools for write operations.

**How to avoid:** `blank-canvas` is a read-only orientation skill. `allowed-tools: Read, Bash, Grep, Glob` only. No Write, no Edit.

### Pitfall 4: Canvas-Renderer Agent Writes Outside canvas/components/

**What goes wrong:** The agent writes to `canvas/src/` (modifying the rendering pipeline source) instead of `canvas/components/` (generating consumer artifacts).

**Why it happens:** `canvas/src/` and `canvas/components/` are both in `canvas/` — both pass the outer path gate. The agent may conflate "in canvas/" with "in scope."

**How to avoid:** The scope constraint in the agent body must be explicit: "Write only to `canvas/components/`." The Phase 6 PostToolUse hook should log a WARNING when a canvas/ write lands outside `canvas/components/` so violations surface immediately.

### Pitfall 5: AGENT-BOUNDARIES.md Has Two Competing Canvas Sections

**What goes wrong:** Phase 1 added a "Canvas Path-Gating" section to `.claude/AGENT-BOUNDARIES.md`. Phase 6 adds canvas-renderer to the agent roster. If the Phase 6 plan creates a new section instead of updating the existing one, the document has contradictory sections.

**Why it happens:** The planner may not be aware of the existing "Canvas Path-Gating" section at the bottom of `.claude/AGENT-BOUNDARIES.md`.

**How to avoid:** The plan must explicitly instruct updating the existing "Canvas Path-Gating" section (lines 150-176 of `.claude/AGENT-BOUNDARIES.md`) and adding canvas-renderer to the existing agent roster table. One governance document, one canvas section.

---

## Code Examples

### Existing Hook Pattern (cards/ — the template to follow)

```bash
# Source: .claude/settings.json line 9 — the established project pattern
FILE=$(echo "$CLAUDE_TOOL_INPUT" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('file_path') or d.get('path') or '')" 2>/dev/null)
if echo "$FILE" | grep -q 'cards/'; then
  echo "--- Auto-validating: $FILE ---"
  python scripts/validate-card.py "$FILE" 2>&1 || true
fi
```

The `|| true` at the end is critical. The validate-card.py script may exit non-zero for invalid cards — that's informational, not a hook failure.

### Canvas Hook Pattern (new — mirrors cards/ exactly)

```bash
# canvas/ PostToolUse hook — informational, never blocking
FILE=$(echo "$CLAUDE_TOOL_INPUT" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('file_path') or d.get('path') or '')" 2>/dev/null)
if echo "$FILE" | grep -q 'canvas/'; then
  echo "--- Canvas write: $FILE ---"
  if echo "$FILE" | grep -qv 'canvas/components/\|canvas/tests/\|canvas/src/'; then
    echo "INFO: Write to canvas/ root path: $FILE"
  fi
fi
```

Note: no validation script to call yet (canvas/components/ doesn't exist until Phase 7+). The hook is informational only — logs the write and checks for out-of-scope paths.

### Skill Frontmatter (from generate-card — the template)

```yaml
---
name: generate-card
description: Generate a single Ppl± workout card from its zip code. Reads identity doc, validates, generates, renames stub, logs to whiteboard.
disable-model-invocation: true
argument-hint: "[zip-code e.g. ⛽🌹🛒🔵]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---
```

`blank-canvas` SKILL.md uses the same structure with `allowed-tools: Read, Bash, Grep, Glob` (no Write).

### Agent Frontmatter (from deck-auditor — read-only pattern)

```yaml
---
name: deck-auditor
description: Audits an entire deck for SCL compliance...
tools: Read, Grep, Glob, Bash
model: claude-sonnet-4-6
disallowedTools: Write, Edit
---
```

`canvas-renderer` uses the same structure but with Write/Edit permitted and scope constraint in body.

### Agent Frontmatter (from card-generator — write-permitted pattern)

```yaml
---
name: card-generator
description: Generates a single Ppl± workout card in isolated context...
tools: Read, Write, Edit, Bash, Grep, Glob
model: claude-opus-4-6
skills:
  - generate-card
---
```

`canvas-renderer` mirrors this pattern but uses `claude-sonnet-4-6` (not Opus) since component generation is less knowledge-intensive than workout card generation.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| No canvas/ hooks | Path-gated PostToolUse | Phase 6 (now) | canvas/ writes are logged and scoped; cross-boundary writes surface as warnings |
| No canvas-specific agents | canvas-renderer subagent | Phase 6 (now) | Component generation gets isolated context separate from card generation |
| AGENT-BOUNDARIES.md documents pattern only | AGENT-BOUNDARIES.md + live hook + live agent | Phase 6 (now) | The canvas path-gating specification written in Phase 1 becomes operational |

**Deprecated/outdated:**
- None — this phase creates new artifacts, does not replace existing ones.

---

## Open Questions

1. **Art direction enforcement in hook vs. agent body**
   - What we know: The success criteria says the PostToolUse hook "applies art direction enforcement." The art direction spec is Jake's memory note: intaglio/banknote engraving aesthetic (hatching, guilloche, engraving).
   - What's unclear: There is no `canvas-art-direction.md` or `publication-standard.md` for canvas/ components yet. The hook cannot enforce what is not specified.
   - Recommendation: The hook logs a reminder ("Art direction: intaglio aesthetic — see AGENT-BOUNDARIES.md canvas section") on every canvas/ component write. The agent body carries the art direction rules inline. Full enforcement via a CSS linter or validator is Phase 7+.

2. **canvas/components/ directory — Phase 6 or Phase 7?**
   - What we know: REQUIREMENTS.md shows CLCD-01/02/03 (Phase 6) as skill/subagent/hook, while CLCD-04/05/06 (Phase 7) are scripts and state persistence. Canvas/components/ is where CARD-01/02/03 (Phase 8) card templates land.
   - What's unclear: The canvas-renderer subagent is defined in Phase 6 but its write target (canvas/components/) may not exist until Phase 7 or 8.
   - Recommendation: Create canvas/components/.gitkeep as part of Phase 6 scaffold so the subagent's write target exists. This is a one-file stub, not functional component work.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest ^3.0.0 |
| Config file | canvas/vite.config.ts (test.include: ["tests/**/*.test.ts"]) |
| Quick run command | `cd canvas && npx vitest run` |
| Full suite command | `cd canvas && npx vitest run` |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| CLCD-01 | /blank-canvas skill exists with correct frontmatter | manual | Inspect `.claude/skills/blank-canvas/SKILL.md` frontmatter | No — Wave 0 |
| CLCD-02 | canvas-renderer agent has explicit scope constraint in body | manual | Inspect `.claude/agents/canvas-renderer.md` | No — Wave 0 |
| CLCD-03 | PostToolUse hook fires on canvas/ writes only, exits 0 | manual-only | Invoke Edit on canvas/src/rendering/index.ts, verify hook output; no automated test framework covers hook behavior | No automated test possible |

Phase 6 deliverables are configuration files — they are not testable by Vitest. Validation is by inspection: read the files and verify the frontmatter and body content match the spec.

### Sampling Rate

- Per task commit: `cd canvas && npx vitest run` (confirms Phase 1-5 tests still pass after settings.json changes)
- Per wave merge: `cd canvas && npx vitest run`
- Phase gate: Full Vitest suite green + manual inspection of each deliverable before `/gsd:verify-work`

### Wave 0 Gaps

- [ ] `.claude/skills/blank-canvas/SKILL.md` — CLCD-01 (create in Wave 0)
- [ ] `.claude/agents/canvas-renderer.md` — CLCD-02 (create in Wave 0)
- [ ] `canvas/components/` directory — must exist before canvas-renderer can write there (create `.gitkeep` stub)

*(No test file gaps — Phase 6 config artifacts are not Vitest-testable. Existing canvas/tests/ suite verifies no regressions.)*

---

## Sources

### Primary (HIGH confidence)

- `.claude/settings.json` — existing hook format, `$CLAUDE_TOOL_INPUT` pattern, `|| true` exit handling
- `.claude/AGENT-BOUNDARIES.md` — canvas path-gating specification (lines 150-176), agent roster format, per-agent constraint format
- `.claude/skills/generate-card/SKILL.md` — skill frontmatter schema, `disable-model-invocation`, `allowed-tools`
- `.claude/skills/build-deck-identity/SKILL.md` — multi-step skill workflow structure
- `.claude/agents/card-generator.md` — write-permitted agent pattern
- `.claude/agents/deck-auditor.md` — read-only agent pattern with `disallowedTools`
- `.claude/hooks/gsd-context-monitor.js` — Node hook pattern, stdin reading, exit 0 in all branches
- Official Claude Code Hooks documentation (fetched 2026-03-15) — exit code semantics, stdin JSON input format, PostToolUse cannot block writes

### Secondary (MEDIUM confidence)

- WebSearch result: "PostToolUse hooks: exit code 2 shows 'blocking error' but doesn't actually block" (GitHub issue #19009) — confirms exit 2 is not blocking for PostToolUse

### Tertiary (LOW confidence)

- None needed — all Phase 6 patterns are fully specified by first-party project files.

---

## Metadata

**Confidence breakdown:**
- Skill format: HIGH — 10 existing skills provide exact template
- Agent format: HIGH — 5 existing agents provide exact template
- Hook format: HIGH — existing cards/ hook is the direct template
- Exit code semantics: HIGH — official docs confirmed + existing hooks all use exit 0 / `|| true`
- Art direction content: MEDIUM — intaglio/banknote spec is in memory notes, no formal canvas/ art direction document yet

**Research date:** 2026-03-15
**Valid until:** 2026-04-15 (stable — Claude Code hook format does not change frequently)
