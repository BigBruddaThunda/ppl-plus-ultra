---
phase: 07-scripts-and-state-persistence
plan: 01
subsystem: infra
tags: [bash, node, esm, canvas, weight-engine, css-vars, git-snapshot, skill]

# Dependency graph
requires:
  - phase: 05-rendering-pipeline
    provides: resolveZip() and weightsToCSSVars() — the weight engine pipeline this plan wraps
  - phase: 06-claude-code-infrastructure
    provides: skill frontmatter pattern and allowed-tools convention for canvas-save
provides:
  - canvas-to-production.sh: one-way copy gate from canvas/components/ to production directories
  - batch-propagate.sh: weight engine driver templating design elements across N zip codes
  - run-weight.mjs: Node ESM wrapper outputting CSS vars JSON for any 4-digit numeric zip
  - /canvas-save skill: git snapshot of canvas/ working state with explicit path staging
  - canvas/.local/ directory: git-ignored local working state sandbox
affects:
  - phase 08+: canvas workflow loop — production promotion and multi-zip propagation
  - canvas-renderer subagent: uses batch-propagate.sh and canvas-to-production.sh as primary tools

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "ESM dynamic import with pathToFileURL() for Windows-compatible file:// paths"
    - "bash --skip-build flag pattern for CI vs. interactive usage"
    - "canvas/.local/ gitignore pattern for ephemeral working state"
    - "Explicit git add paths in skill (never git add -A) for safe snapshot commits"

key-files:
  created:
    - canvas/scripts/canvas-to-production.sh
    - canvas/scripts/batch-propagate.sh
    - canvas/scripts/run-weight.mjs
    - .claude/skills/canvas-save/SKILL.md
  modified:
    - .gitignore

key-decisions:
  - "pathToFileURL() required for Node ESM dynamic import on Windows — bare drive-letter paths (C:\\...) are rejected by the ESM loader"
  - "canvas-to-production.sh uses explicit [[ -e DEST ]] pre-check instead of cp -n exit code — cp -n silently succeeds on Windows even when target exists"
  - "batch-propagate.sh --skip-build flag added so CI environments can skip tsc recompilation when dist/ is already fresh"
  - "canvas-save skill stages canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/ explicitly — no glob patterns that could accidentally capture .local/ if gitignore is misconfigured"

patterns-established:
  - "Windows ESM compatibility: all dynamic import() calls use pathToFileURL(resolve(...)) not bare paths"
  - "canvas/.local/ is the standard location for ephemeral scratch files the agent must not commit"
  - "canvas-save is the canonical commit pathway for canvas/ state — never git add -A from canvas workspace"

requirements-completed: [CLCD-04, CLCD-05, CLCD-06]

# Metrics
duration: 4min
completed: 2026-03-14
---

# Phase 7 Plan 01: Scripts and State Persistence Summary

**Bash boundary-enforced production gate, Node ESM weight engine driver, multi-zip batch propagator, and /canvas-save git snapshot skill closing the canvas workflow loop**

## Performance

- **Duration:** ~4 min
- **Started:** 2026-03-14T20:47:21Z
- **Completed:** 2026-03-14T20:51:00Z
- **Tasks:** 2
- **Files modified:** 5 (3 created in canvas/scripts/, 1 skill, 1 gitignore)

## Accomplishments

- canvas-to-production.sh: enforces one-way copy boundary with extension routing (.html/.ts/.tsx/.css), prohibited directory check, and no-overwrite guard
- batch-propagate.sh: templates a named design element across N zip codes using the compiled weight engine, writes HTML files with CSS vars style blocks to canvas/components/ only
- run-weight.mjs: minimal ESM driver wrapping resolveZip() + weightsToCSSVars() + tokens, outputs complete CSS vars JSON to stdout for any 4-digit zip
- /canvas-save skill: 6-step snapshot workflow that verifies gitignore, reports branch, stages explicit canvas/ subdirs only, and refuses empty commits
- canvas/.local/ directory git-ignored before creation to prevent accidental staging

## Task Commits

Each task was committed atomically:

1. **Task 1: Create canvas-to-production.sh and batch-propagate.sh with Node weight driver** - `c70c2c94` (feat)
2. **Task 2: Set up canvas/.local/ git-ignored directory and /canvas-save skill** - `3c5e080b` (feat)

## Files Created/Modified

- `canvas/scripts/canvas-to-production.sh` - Boundary-enforced one-way copy gate from canvas/components/ to production paths
- `canvas/scripts/batch-propagate.sh` - Weight engine driver: templates design elements across N zip codes, writes to canvas/components/ only
- `canvas/scripts/run-weight.mjs` - Node ESM driver: resolveZip() + weightsToCSSVars() + tokens → CSS vars JSON to stdout
- `.claude/skills/canvas-save/SKILL.md` - /canvas-save skill: 6-step git snapshot workflow
- `.gitignore` - Added canvas/.local/ section

## Decisions Made

- **pathToFileURL() for Windows ESM**: Node's dynamic `import()` rejects bare Windows drive-letter paths (`C:\...`). Used `pathToFileURL(resolve(...)).href` to produce valid `file:///C:/...` URLs. Cross-platform compatible.
- **Explicit file existence check over cp -n**: `cp -n` silently exits 0 on Windows even when the target exists. Replaced with `[[ -e "$DEST" ]]` pre-check for reliable no-overwrite enforcement.
- **--skip-build flag on batch-propagate.sh**: Separates build phase from propagation phase, enabling CI environments to reuse an existing dist/ without re-running tsc.
- **Explicit path list in canvas-save**: Stages `canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/` by name rather than `canvas/` glob, ensuring canvas/.local/ is never staged even if gitignore is misconfigured.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed cp -n no-overwrite enforcement on Windows**
- **Found during:** Task 1 (canvas-to-production.sh testing)
- **Issue:** `cp -n` silently exits 0 on Windows Git Bash when destination exists — the plan specified `cp -n` as the no-overwrite mechanism
- **Fix:** Replaced `cp -n` with explicit `[[ -e "$DEST" ]]` pre-check before copy
- **Files modified:** canvas/scripts/canvas-to-production.sh
- **Verification:** Second copy of same file correctly exits 1 with "Destination already exists" message
- **Committed in:** c70c2c94 (Task 1 commit)

**2. [Rule 1 - Bug] Fixed Windows ESM dynamic import paths in run-weight.mjs**
- **Found during:** Task 1 (run-weight.mjs testing)
- **Issue:** `import(distRoot + '/weights/resolver.js')` where distRoot was a Windows absolute path — Node ESM loader rejects `C:\...` protocol, requires `file:///C:/...`
- **Fix:** Added `pathToFileURL()` wrapper converting absolute paths to file:// URLs
- **Files modified:** canvas/scripts/run-weight.mjs
- **Verification:** `node canvas/scripts/run-weight.mjs 2123` outputs correct CSS vars JSON with --ppl-weight-font-weight: 800
- **Committed in:** c70c2c94 (Task 1 commit)

---

**Total deviations:** 2 auto-fixed (2 bugs — both Windows platform-specific behavior differences)
**Impact on plan:** Both fixes required for correctness on the target platform. No scope creep.

## Issues Encountered

- The tsc `rootDir: "."` setting (covering both `src/` and `tests/`) causes compiled output to land in `canvas/dist/src/` not `canvas/dist/` — adjusted run-weight.mjs import paths accordingly.

## User Setup Required

None — no external service configuration required.

## Next Phase Readiness

- Full canvas workflow loop is closed: weight engine → batch propagation → production promotion → git snapshot
- canvas-renderer subagent can now use batch-propagate.sh and canvas-to-production.sh as primary tools
- /canvas-save skill available for all canvas workspace sessions
- Phase 8+ can focus on card template rendering using the propagated CSS vars

---
*Phase: 07-scripts-and-state-persistence*
*Completed: 2026-03-14*
