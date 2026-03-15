---
name: blank-canvas
description: "Initialize the canvas workspace and load current state. Reads canvas/src/ structure, reports phase completion, confirms agent is scoped to canvas/ paths only."
disable-model-invocation: true
allowed-tools: Read, Bash, Grep, Glob
---

Initialize the canvas workspace.

## Workflow

### 1. Load Canvas Workspace State

Read the workspace manifest and directory structure:

```
Read canvas/package.json
Glob canvas/src/**/*.ts
Glob canvas/tests/**/*.test.ts
```

Report: package name, version, script targets, and how many source files and test files exist.

### 2. Report Phase Completion

Check which Phase 1–5 artifacts exist:

| Phase | Artifact | Check |
|-------|----------|-------|
| 1 | canvas/src/types/scl.ts | Does file exist? |
| 2 | canvas/src/weights/ | Does directory contain .ts files? |
| 3 | canvas/src/rendering/ | Does directory contain index.ts? |
| 4 | canvas/src/tokens/tokens.ts | Does file exist? |
| 5 | canvas/src/rendering/index.ts | Does weightsToCSSVars export exist? |

Use Bash: `test -f canvas/src/types/scl.ts && echo PHASE1_OK || echo PHASE1_MISSING`

For each phase, report: COMPLETE or MISSING.

### 3. Load Boundary Rules

Read `.claude/AGENT-BOUNDARIES.md` — specifically the Canvas Path-Gating section and the canvas-renderer subagent constraints.

Confirm the active write scope: **canvas/ paths only.**

Prohibited write targets:
- `cards/` — workout card content (card-generator territory)
- `html/` — legacy HTML scaffold (separate phase)
- `web/` — web application layer (Phase 4/5)
- `middle-math/` — computation engine (separate workspace)

### 4. Report Current State

Output a summary in this format:

```
Canvas Workspace State
======================
Package: [name@version]
Source files: [count]
Test files: [count]

Phase completion:
  Phase 1 (types):     [COMPLETE | MISSING]
  Phase 2 (weights):   [COMPLETE | MISSING]
  Phase 3 (rendering): [COMPLETE | MISSING]
  Phase 4 (tokens):    [COMPLETE | MISSING]
  Phase 5 (pipeline):  [COMPLETE | MISSING]

canvas/components/ contents:
  [list files or "empty — ready for canvas-renderer"]

Active agent scope: canvas/ only
Prohibited: cards/, html/, web/, middle-math/
```

If $ARGUMENTS is provided, focus the report on the named phase (e.g., "5" → show Phase 5 details).
