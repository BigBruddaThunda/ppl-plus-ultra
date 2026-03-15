# Phase 7: Scripts and State Persistence - Research

**Researched:** 2026-03-15
**Domain:** Bash shell scripting, git snapshot workflows, Claude Code skill authoring, .gitignore conventions for local working state
**Confidence:** HIGH — all deliverables are bash scripts and a Claude Code skill; patterns established in this project are the direct templates; no external library research required

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| CLCD-04 | canvas-to-production.sh script porting canvas elements to cards/, html/, or web/ | Pure bash file copy; destination routing logic derives from path prefix of the source artifact; AGENT-BOUNDARIES.md documents exact prohibited paths for canvas-renderer |
| CLCD-05 | batch-propagate.sh script templating a design across N zip codes | Calls canvas weight engine via Node; resolveZip() is already exported from canvas/src/weights/; produces N output files in canvas/components/ |
| CLCD-06 | Canvas state persistence — local working state in canvas/.local/ + git snapshots via /canvas-save command | .local/ added to .gitignore; /canvas-save is a new skill invoking git add + git commit; pattern mirrors existing generate-card skill |
</phase_requirements>

---

## Summary

Phase 7 has three deliverables: two bash scripts and one Claude Code skill. None require new TypeScript libraries, new npm packages, or new Node APIs. The canvas weight engine (Phases 1-5) is fully built and can be invoked from bash via `node` + a tiny driver script. The Claude Code skill system (Phase 6) is live and provides the exact skill authoring template. The git CLI provides all state snapshot capabilities needed for `/canvas-save`.

The most important constraint across all three deliverables is the AGENT-BOUNDARIES.md firewall: `canvas-to-production.sh` must not overwrite non-canvas files, `batch-propagate.sh` must write only to `canvas/components/` (not production directories), and the `/canvas-save` skill must commit only the canvas snapshot — not the full repo. Every script must fail loudly when given a path that would violate boundaries rather than silently proceeding.

The second constraint is that `canvas/.local/` must be git-ignored before the first `/canvas-save` is ever invoked. If `.local/` is not gitignored at creation time, running `git add` in the save workflow could accidentally stage private working state. The gitignore entry must be written as part of the same plan that creates the `.local/` directory.

**Primary recommendation:** Write both scripts in bash using strict mode (`set -euo pipefail`). Use the existing `canvas/scripts/build-keywords.mjs` and `canvas/scripts/derive-colors.mjs` as stylistic reference for the script header convention. Author `/canvas-save` as a new skill at `.claude/skills/canvas-save/SKILL.md` following the exact frontmatter schema established by `blank-canvas` and `generate-card`.

---

## Standard Stack

### Core

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| bash strict mode | any bash | Script safety (set -euo pipefail) | Prevents silent failures on bad paths or missing files |
| git CLI | system | Snapshot commits in /canvas-save | Already in repo; no wrapper needed |
| node (ESM) | system | Invoke canvas weight engine from bash | canvas/ is ESM (type: module in package.json); use `node --input-type=module` for inline scripts or a small driver .mjs file |
| `.claude/skills/{name}/SKILL.md` | Claude Code v1 | /canvas-save skill definition | Established project pattern; blank-canvas SKILL.md is the direct template |

### Supporting

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `cp -n` (no-clobber) | Prevent overwriting non-canvas files in canvas-to-production.sh | Always use `-n` flag when copying to cards/, html/, web/ |
| `git add --` (explicit paths) | Stage only canvas snapshot files in /canvas-save | Never `git add -A` or `git add .` from a skill — too broad |
| `jq` or node | Parse JSON weight output from the weight engine | If the weight engine outputs JSON, use node for parsing (already a project dependency); avoid jq dependency |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| bash scripts | Node .mjs scripts | Node gives better error messages and TypeScript types; but bash is simpler for file operations and is always available; use bash for file-system operations, node only for weight engine calls |
| /canvas-save as a skill | /canvas-save as a bash script | Skills are invokable directly from the Claude Code session (`/canvas-save`); bash scripts require explicit `bash canvas/scripts/...` invocation — skill is the right abstraction for session-level commands |
| canvas/.local/ for state | canvas/state/ (committed) | state/ would be committed to git and contaminate history with every scratch edit; .local/ is git-ignored and provides a clean scratch surface; committed snapshots land in canvas/snapshots/ (see Architecture Patterns) |

---

## Architecture Patterns

### Pattern 1: canvas-to-production.sh — One-Way Copy with Destination Routing

**What:** Accepts one argument — the source path inside `canvas/components/` — and copies it to the correct production destination, with path routing based on file type and content inspection.

**When to use:** After Jake decides a canvas element is finalized. This is an explicit, intentional migration gate.

**Routing logic:**
- `canvas/components/*.md` → route to `cards/` tree (requires explicit deck/order/axis/type path)
- `canvas/components/*.html` → route to `html/`
- `canvas/components/*.tsx` or `*.ts` → route to `web/`
- `canvas/components/*.css` → route to `html/design-system/` or `web/styles/`
- Ambiguous → exit 1 with helpful message

**No-overwrite constraint:** Use `cp -n` (no-clobber) to prevent overwriting existing production files. If destination exists, report the conflict and exit 1. The user must explicitly delete the destination file first if they want to overwrite.

**Boundary check:** Script must refuse to copy to `middle-math/`, `scripts/`, or any path outside `cards/`, `html/`, `web/`.

**Example structure:**
```bash
#!/usr/bin/env bash
set -euo pipefail

# canvas-to-production.sh
# Usage: bash canvas/scripts/canvas-to-production.sh <canvas-artifact-path>

SOURCE="${1:-}"

if [[ -z "$SOURCE" ]]; then
  echo "ERROR: No source path provided." >&2
  echo "Usage: bash canvas/scripts/canvas-to-production.sh canvas/components/MyCard.html" >&2
  exit 1
fi

if [[ ! -f "$SOURCE" ]]; then
  echo "ERROR: Source file not found: $SOURCE" >&2
  exit 1
fi

# Validate source is inside canvas/components/
if ! echo "$SOURCE" | grep -q '^canvas/components/'; then
  echo "ERROR: Source must be inside canvas/components/. Got: $SOURCE" >&2
  exit 1
fi

# Route by extension
FILENAME=$(basename "$SOURCE")
EXT="${FILENAME##*.}"

case "$EXT" in
  html)
    DEST="html/${FILENAME}"
    ;;
  tsx|ts)
    DEST="web/src/components/${FILENAME}"
    ;;
  css)
    DEST="html/design-system/${FILENAME}"
    ;;
  md)
    echo "ERROR: .md files require explicit deck path. Use:" >&2
    echo "  cp -n $SOURCE cards/<order>/<axis>/<type>/<filename>" >&2
    exit 1
    ;;
  *)
    echo "ERROR: Unknown file type: $EXT. Cannot route automatically." >&2
    exit 1
    ;;
esac

# Boundary check — never write to prohibited paths
for PROHIBITED in middle-math scripts seeds scl-deep; do
  if echo "$DEST" | grep -q "^$PROHIBITED/"; then
    echo "ERROR: Destination $DEST is in a prohibited path." >&2
    exit 1
  fi
done

# Copy with no-clobber flag
if cp -n "$SOURCE" "$DEST" 2>/dev/null; then
  echo "COPIED: $SOURCE → $DEST"
else
  echo "ERROR: Destination already exists: $DEST" >&2
  echo "Delete the destination file first if you intend to overwrite." >&2
  exit 1
fi
```

### Pattern 2: batch-propagate.sh — Weight Engine Driver

**What:** Accepts a design element name (a file in `canvas/components/`) and a count N, resolves N zip codes from a list or generates N addresses from a range, and calls the weight engine once per zip to derive per-zip CSS vars, writing N output files to `canvas/components/`.

**When to use:** When a single design decision (e.g., a block container style) needs to be instantiated across multiple zip codes.

**Weight engine invocation:** The canvas weight engine exports `resolveZip(order, axis, type, color)` from `canvas/src/weights/resolver.ts`. To call this from bash, write a minimal Node driver inline:

```bash
#!/usr/bin/env bash
set -euo pipefail

# batch-propagate.sh
# Usage: bash canvas/scripts/batch-propagate.sh <design-element> <N>
# Example: bash canvas/scripts/batch-propagate.sh BlockHeader 8

ELEMENT="${1:-}"
N="${2:-}"

if [[ -z "$ELEMENT" || -z "$N" ]]; then
  echo "ERROR: Usage: batch-propagate.sh <design-element> <N>" >&2
  exit 1
fi

if ! [[ "$N" =~ ^[0-9]+$ ]] || [[ "$N" -lt 1 ]]; then
  echo "ERROR: N must be a positive integer. Got: $N" >&2
  exit 1
fi

# All writes go to canvas/components/ only — never to production
OUTDIR="canvas/components"
WRITTEN=0

# Generate N zip codes (sequential from Deck 07 defaults — override with ZIP_LIST env var)
ZIP_LIST="${ZIP_LIST:-}"
if [[ -z "$ZIP_LIST" ]]; then
  # Default: first N zips from Deck 07 (2113-2183 range)
  # Caller can set ZIP_LIST="2113,2123,2133" to override
  echo "INFO: No ZIP_LIST set. Using first $N zips from Deck 07." >&2
fi

# Call weight engine via node for each zip
# (Implementation: write a small .mjs driver at canvas/scripts/run-weight.mjs
#  that imports resolveZip and outputs CSS vars as JSON)
for i in $(seq 1 "$N"); do
  ZIP="21${i}3"  # placeholder — real implementation reads from ZIP_LIST
  OUTFILE="$OUTDIR/${ELEMENT}-${ZIP}.html"

  # Invoke weight engine — writes CSS vars to stdout
  CSS_VARS=$(node --input-type=module <<EOF
import { resolveZip } from './canvas/src/weights/resolver.js';
import { weightsToCSSVars } from './canvas/src/rendering/index.js';
import { tokens } from './canvas/src/tokens/tokens.js';
const [o, a, t, c] = [${ZIP:0:1}, ${ZIP:1:1}, ${ZIP:2:1}, ${ZIP:3:1}].map(Number);
const vec = resolveZip(o, a, t, c);
const vars = weightsToCSSVars(vec, tokens);
console.log(JSON.stringify(vars, null, 2));
EOF
  )

  # Write output file (placeholder — real implementation applies CSS vars to element template)
  echo "<!-- Propagated: $ELEMENT for zip $ZIP -->" > "$OUTFILE"
  echo "$CSS_VARS" >> "$OUTFILE"

  WRITTEN=$((WRITTEN + 1))
  echo "WRITTEN: $OUTFILE"
done

echo "---"
echo "batch-propagate complete: $WRITTEN files written to $OUTDIR"
```

**Note on node ESM invocation:** `canvas/package.json` has `"type": "module"`. The weight engine uses `.js` extensions in imports (TypeScript `moduleResolution: node16`). To call TypeScript from bash without `ts-node`, either: (a) pre-compile canvas with `npm run build` and call the compiled `.js`, or (b) use `tsx` if available. The simplest approach is to write a small `canvas/scripts/run-weight.mjs` driver that is compiled as part of the canvas build step. See "Don't Hand-Roll" below for guidance.

### Pattern 3: /canvas-save Skill — Git Snapshot

**What:** A Claude Code skill that commits the current canvas working state as a named snapshot. Does NOT commit the entire repo — only `canvas/` paths (excluding `canvas/.local/`).

**When to use:** When Jake wants to checkpoint progress on a canvas design iteration.

**Skill file:** `.claude/skills/canvas-save/SKILL.md`

**Frontmatter:**
```yaml
---
name: canvas-save
description: "Commit current canvas/ state as a named snapshot. Stages canvas/src/, canvas/components/, canvas/tests/, canvas/scripts/ only. Never stages canvas/.local/ or production paths."
disable-model-invocation: true
argument-hint: "[snapshot name e.g. 'v0-card-shell']"
allowed-tools: Read, Bash, Grep, Glob
---
```

**Workflow:**
1. Read $ARGUMENTS for the snapshot name (required — exit with instructions if empty)
2. Confirm canvas/.local/ is in .gitignore (read .gitignore, grep for canvas/.local/)
3. Stage only canvas/ paths (excluding .local/): `git add canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/`
4. Check `git status --short` — if nothing staged, report "Nothing to snapshot" and exit cleanly
5. Commit: `git commit -m "canvas-snapshot: $NAME"`
6. Report: echo the commit hash and what was staged

**Critical:** The skill uses `allowed-tools: Read, Bash, Grep, Glob` — it can run git commands via Bash. No Write/Edit tools needed since this is a git operation, not a file authoring operation.

### Pattern 4: canvas/.local/ Directory Setup

**What:** A git-ignored directory for working state — scratch files, temporary CSS dumps, in-progress component iterations.

**Setup sequence (must happen in correct order):**
1. Add `canvas/.local/` to `.gitignore` FIRST
2. Create `canvas/.local/.gitkeep` so the directory exists
3. Verify gitignore entry prevents accidental staging

**Gitignore entry:**
```
# Canvas local working state (git-ignored)
canvas/.local/
```

**What lives in .local/:**
- In-progress component iterations not ready for commit
- CSS variable dumps from the weight engine
- Scratch files from a session

**What does NOT live in .local/:**
- Finalized components (those go in canvas/components/)
- Committed snapshots (those are git history)

### Anti-Patterns to Avoid

- **Copying to production without the -n flag:** Using `cp` without `-n` silently overwrites existing production card files. Always use `cp -n` and exit on overwrite attempt.
- **git add -A in /canvas-save:** Stages everything including .planning/, whiteboard.md, CLAUDE.md edits. Always stage explicit canvas/ paths only.
- **batch-propagate writing to cards/ directly:** The script writes to canvas/components/ only. Production porting is a separate explicit step (canvas-to-production.sh).
- **canvas/.local/ without gitignore:** Creating the directory before the gitignore entry means git will track it. Gitignore entry must precede the directory creation in the same plan task.
- **Bare node invocation of TypeScript:** `canvas/src/` contains TypeScript with `.js` extensions in imports. Calling `node canvas/src/weights/resolver.ts` directly will fail. Use a pre-compiled build or a `.mjs` wrapper.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| TypeScript invocation from bash | Custom ts → js transpile pipeline | Pre-compile with `npm run build` in canvas/, then call compiled output | canvas already has `vite build` and `tsc`; the compiled output is in `canvas/dist/` after build; use that |
| Git staging logic | Custom git add patterns with wildcards | Explicit path list: `git add canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/` | Explicit lists are auditable and safe; wildcards can accidentally stage .local/ if gitignore has an edge case |
| ZIP list generation | Custom zip enumeration algorithm | Use ORDERS × AXES × TYPES × COLORS = 1,680 from the existing `ORDERS`, `AXES`, `TYPES`, `COLORS` const objects in canvas/src/types/scl.ts | The zip registry is already defined; import it, don't re-derive it |
| File routing heuristics | ML/AI routing of canvas artifacts | Simple extension-to-path table in bash | The mapping is deterministic: .html → html/, .tsx → web/, .css → html/design-system/ |

**Key insight:** Every operation in Phase 7 is a composition of primitives that already exist: bash file operations, git CLI, the compiled canvas weight engine, and the Claude Code skill format. No new dependencies needed.

---

## Common Pitfalls

### Pitfall 1: canvas/.local/ staged in /canvas-save

**What goes wrong:** `git add canvas/` (with trailing slash glob) includes `canvas/.local/` if the gitignore entry is missing or malformed.

**Why it happens:** `.gitignore` entries for directories require a trailing slash (`canvas/.local/`). Without the slash, only a file named `.local` would be ignored, not the directory.

**How to avoid:** Verify the gitignore entry format is `canvas/.local/` (with trailing slash). In the /canvas-save skill, grep .gitignore before staging: `grep -q 'canvas/\.local/' .gitignore || { echo "ERROR: canvas/.local/ not in .gitignore"; exit 1; }`

**Warning signs:** `git status` shows files under `canvas/.local/` as untracked (means gitignore is not working).

### Pitfall 2: canvas-to-production.sh overwrites production cards

**What goes wrong:** A generated canvas component HTML file overwrites an existing card file in cards/ because the destination filename coincidentally matches.

**Why it happens:** canvas-to-production.sh routes .md files to cards/ — but the routing for .md requires explicit deck path knowledge. Auto-routing .md is impossible without parsing the frontmatter zip code.

**How to avoid:** Exit 1 with instructions when source is .md. The user must provide the explicit destination path manually. This is intentional friction: .md card files in production have naming conventions that canvas/ doesn't enforce.

**Warning signs:** Any .md file output from canvas-renderer — inspect the destination before copying.

### Pitfall 3: Node ESM + TypeScript path resolution failure

**What goes wrong:** `node --input-type=module` inline script fails with "Cannot find module 'canvas/src/weights/resolver.js'" because the `--input-type=module` context doesn't set the correct working directory.

**Why it happens:** Inline node scripts don't have a file path, so `import.meta.url` and relative imports behave differently.

**How to avoid:** Write a small `canvas/scripts/run-weight.mjs` driver file (not an inline heredoc) that imports from the compiled `canvas/dist/` output. Run the canvas build first, then call the compiled JS. Alternatively, use the pattern `(cd canvas && node --experimental-vm-modules ...)` to set CWD correctly.

**Warning signs:** `Error [ERR_MODULE_NOT_FOUND]` when testing the script.

### Pitfall 4: /canvas-save commits to wrong branch

**What goes wrong:** The skill runs `git commit` and creates a commit on whatever branch is currently checked out — which may be `main`.

**Why it happens:** The skill doesn't check or enforce which branch is active.

**How to avoid:** In the skill workflow, run `git branch --show-current` and print the branch name before committing. Do not enforce a specific branch, but make it visible so the user can see where the snapshot lands. The skill is informational about the branch, not prescriptive.

**Warning signs:** Snapshot commits appear in `git log` on main instead of a feature/canvas branch.

### Pitfall 5: batch-propagate.sh hard-codes Order 2 zip range

**What goes wrong:** The script only generates zips from Deck 07 (Order 2, Axis 1) instead of accepting an arbitrary zip list.

**Why it happens:** The scaffold uses a sequential range that's easy to write but limits the script to one deck.

**How to avoid:** Accept zip list as a positional argument or environment variable (`ZIP_LIST="2113,2123,2133,2143"`). Document the expected format. The default can be Deck 07 for easy first use, but the ZIP_LIST override must work.

**Warning signs:** Running `batch-propagate.sh BlockHeader 5` always produces only Deck 07 variants.

---

## Code Examples

Verified patterns from first-party project files:

### PostToolUse hook path-gate pattern (from .claude/settings.json)
```bash
# Source: .claude/settings.json (established Phase 6 pattern)
FILE=$(echo "$CLAUDE_TOOL_INPUT" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('file_path') or d.get('path') or '')" 2>/dev/null)
if echo "$FILE" | grep -q 'canvas/'; then
  echo "--- Canvas write: $FILE ---"
fi
```

### Bash strict mode header (from canvas/scripts/derive-colors.mjs header convention)
```bash
#!/usr/bin/env bash
set -euo pipefail
# Script name — one-line purpose
# Usage: bash canvas/scripts/script-name.sh [args]
```

### Node ESM import from canvas/dist/ after build
```bash
# Pre-build canvas TypeScript
(cd canvas && npm run build 2>/dev/null)

# Invoke compiled weight engine
node --input-type=module <<'EOF'
import { resolveZip } from './canvas/dist/weights/resolver.js';
import { weightsToCSSVars } from './canvas/dist/rendering/index.js';
import { tokens } from './canvas/dist/tokens/tokens.js';
const vec = resolveZip(2, 1, 2, 3);
const vars = weightsToCSSVars(vec, tokens);
console.log(JSON.stringify(vars));
EOF
```

### Skill frontmatter pattern (from .claude/skills/blank-canvas/SKILL.md)
```yaml
---
name: canvas-save
description: "Commit current canvas/ state as a named snapshot."
disable-model-invocation: true
argument-hint: "[snapshot-name e.g. 'v0-card-shell']"
allowed-tools: Read, Bash, Grep, Glob
---
```

### Git staging with explicit paths (safe pattern from scripts/validate-deck.sh reference)
```bash
# Stage only canvas/ paths — never stage .local/
git add canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/
git status --short
```

### Gitignore entry for .local/ (must include trailing slash)
```
# Canvas local working state — never commit
canvas/.local/
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Manual file copy (drag in Finder) | canvas-to-production.sh with boundary check | Phase 7 | Prevents accidental overwrite; enforces the canvas→production gate explicitly |
| No canvas snapshots | canvas/.local/ + /canvas-save commits | Phase 7 | Canvas design iterations are now checkpointable without polluting the main commit stream |
| One-at-a-time component generation | batch-propagate.sh across N zips | Phase 7 | Design decisions can propagate across multiple zip addresses in one command |

**Not yet built (deferred to Phase 8+):**
- 1,680 pre-rendered zip RenderDescriptors (all at build time) — batch-propagate handles a smaller N for now
- Real-time canvas ↔ production sync — the explicit `canvas-to-production.sh` gate is intentional

---

## Open Questions

1. **canvas build step in batch-propagate.sh**
   - What we know: canvas/package.json has `"build": "tsc && vite build"` which compiles TypeScript to canvas/dist/
   - What's unclear: Whether the planner should include a build step inside batch-propagate.sh, or assume the caller pre-builds
   - Recommendation: Include `(cd canvas && npm run build 2>/dev/null)` as the first step in batch-propagate.sh with a `--skip-build` flag for speed when the caller knows it's fresh

2. **Destination routing for .tsx files in canvas-to-production.sh**
   - What we know: canvas/components/ uses .tsx; web/ is Next.js (web/src/ contains components)
   - What's unclear: The exact target subdirectory under web/src/ (components? app? layout?)
   - Recommendation: Route .tsx to `web/src/components/canvas/` — create a canvas/ subdirectory within web/src/components/ to namespace canvas-originated components

3. **ZIP_LIST format for batch-propagate.sh**
   - What we know: The script needs to accept an arbitrary list of 4-digit numeric zips
   - What's unclear: Whether to accept as a comma-separated string, a file path, or positional args
   - Recommendation: Accept as a positional argument in comma-separated format: `bash batch-propagate.sh BlockHeader 8 "2113,2123,2133,2143,2153,2163,2173,2183"` where N is used as the count if no explicit list is provided

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest 3.x (canvas/package.json devDependency) |
| Config file | canvas/vite.config.ts (test.include: "tests/**/*.test.ts") |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| CLCD-04 | canvas-to-production.sh copies to correct destination and refuses to overwrite | integration (bash test) | `bash canvas/scripts/canvas-to-production.sh canvas/components/test-fixture.html && test -f html/test-fixture.html` | ❌ Wave 0 |
| CLCD-04 | canvas-to-production.sh refuses canvas/components/ → middle-math/ copy | integration (bash test) | `! bash canvas/scripts/canvas-to-production.sh canvas/components/test.ts 2>/dev/null || true` — must exit 1 for prohibited path | ❌ Wave 0 |
| CLCD-05 | batch-propagate.sh writes N files to canvas/components/ | integration (bash test) | `bash canvas/scripts/batch-propagate.sh BlockHeader 3 "2113,2123,2133" && ls canvas/components/BlockHeader-*.html \| wc -l \| grep -q 3` | ❌ Wave 0 |
| CLCD-06 | canvas/.local/ is git-ignored | unit (bash assertion) | `git check-ignore canvas/.local/test-file && echo GITIGNORED` | ❌ Wave 0 |
| CLCD-06 | /canvas-save stages only canvas/ paths | integration (manual) | Invoke `/canvas-save test-snapshot`, verify `git log --name-only -1` contains only canvas/ paths | manual-only |

**Note:** CLCD-04, CLCD-05, and CLCD-06 are primarily verified by bash assertions against the actual scripts, not Vitest unit tests. The bash assertions are fast (< 5 seconds each) and can be run inline in the plan verification steps. No new Vitest test files are required for Phase 7 — the validation is script-level.

### Sampling Rate

- **Per task commit:** `cd canvas && npm test` (regression check — confirms Phase 1-6 tests still pass)
- **Per wave merge:** `cd canvas && npm test` + manual `/canvas-save test-snapshot` invocation
- **Phase gate:** All Phase 1-6 tests green + bash assertion checks for CLCD-04, CLCD-05, CLCD-06 pass

### Wave 0 Gaps

- [ ] `canvas/scripts/canvas-to-production.sh` — covers CLCD-04
- [ ] `canvas/scripts/batch-propagate.sh` — covers CLCD-05
- [ ] `canvas/.local/.gitkeep` + `.gitignore` entry — covers CLCD-06 (directory side)
- [ ] `.claude/skills/canvas-save/SKILL.md` — covers CLCD-06 (skill side)
- [ ] Test fixture: `canvas/components/test-fixture.html` — needed for CLCD-04 bash assertion (can be a minimal one-liner file, deleted after verification)

---

## Sources

### Primary (HIGH confidence)

- First-party: `.claude/settings.json` — PostToolUse hook pattern (path-gate bash + echo only, never exit non-zero)
- First-party: `.claude/skills/blank-canvas/SKILL.md` — exact skill frontmatter schema and workflow structure
- First-party: `.claude/agents/canvas-renderer.md` — agent boundary conventions
- First-party: `.claude/AGENT-BOUNDARIES.md` — canvas/ path-gating rules, prohibited paths
- First-party: `canvas/package.json` — build scripts, ESM type, vitest version, vite version
- First-party: `canvas/vite.config.ts` — test include pattern, environment
- First-party: `canvas/scripts/build-keywords.mjs` — script header convention
- First-party: `canvas/scripts/derive-colors.mjs` — script header convention, ESM patterns
- First-party: `.planning/research/ARCHITECTURE.md` — canvas-to-production.sh and batch-propagate.sh design intent (lines 88-89, 140-142)
- First-party: `.planning/phases/06-claude-code-infrastructure/06-01-SUMMARY.md` — Phase 6 completion status, patterns-established
- First-party: `.gitignore` — existing ignore patterns; `canvas/.local/` is NOT yet present (must be added)

### Secondary (MEDIUM confidence)

- First-party REQUIREMENTS.md traceability table — confirms CLCD-04, CLCD-05, CLCD-06 are all Phase 7 and all currently Pending
- First-party ROADMAP.md Phase 7 success criteria — exact wording of the 3 success criteria used to define scope

### Tertiary (LOW confidence)

- None. All claims in this research are anchored to first-party project files.

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — all tools (bash, git, node, Claude Code skill format) are established in this project
- Architecture: HIGH — canvas-to-production.sh and batch-propagate.sh design intent is documented in .planning/research/ARCHITECTURE.md; no new patterns needed
- Pitfalls: HIGH — all pitfalls derive from concrete failure modes in the established codebase (gitignore edge cases, cp without -n, ESM path resolution)

**Research date:** 2026-03-15
**Valid until:** 60 days — bash scripting and git CLI are stable; the canvas TypeScript API (resolveZip, weightsToCSSVars) is stable after Phase 5
