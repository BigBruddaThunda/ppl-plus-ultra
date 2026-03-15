---
name: canvas-save
description: "Commit current canvas/ state as a named snapshot. Stages canvas/src/, canvas/components/, canvas/tests/, canvas/scripts/ only. Never stages canvas/.local/ or production paths."
disable-model-invocation: true
argument-hint: "[snapshot-name e.g. 'v0-card-shell']"
allowed-tools: Read, Bash, Grep, Glob
---

Commit the current canvas/ working state as a named git snapshot.

## Workflow

### 1. Read snapshot name

Read `$ARGUMENTS` for the snapshot name.

If `$ARGUMENTS` is empty:
```
Print:
  Usage: /canvas-save <snapshot-name>
  Example: /canvas-save v0-card-shell

  Provide a descriptive snapshot name to create the commit.
Stop — do not proceed.
```

### 2. Verify .gitignore protection

Run:
```bash
grep -q 'canvas/\.local/' .gitignore && echo "GITIGNORE_OK" || echo "GITIGNORE_MISSING"
```

If result is `GITIGNORE_MISSING`:
```
Print:
  ERROR: canvas/.local/ is not in .gitignore.
  Add the following line to .gitignore before committing:
    canvas/.local/
Stop — do not stage or commit anything.
```

### 3. Show current branch

Run:
```bash
git branch --show-current
```

Print the branch name so the user knows where the snapshot will land.

### 4. Stage canvas/ paths (excluding .local/)

Run:
```bash
git add canvas/src/ canvas/components/ canvas/tests/ canvas/scripts/
```

Note: canvas/.local/ is excluded by this explicit path list — it is never staged.

### 5. Check for staged changes

Run:
```bash
git status --short
```

If no files are staged (no lines starting with `A` or `M` in staged column):
```
Print:
  Nothing to snapshot — no staged changes in canvas/src/, canvas/components/,
  canvas/tests/, or canvas/scripts/.
Stop cleanly — do not create an empty commit.
```

### 6. Commit

Run:
```bash
git commit -m "canvas-snapshot: $ARGUMENTS"
```

After commit, run:
```bash
git log --oneline -1
```

Print the commit hash and the list of staged files from `git status --short` output.

Example output:
```
Snapshot committed: a1b2c3d canvas-snapshot: v0-card-shell
Files committed:
  M canvas/src/rendering/weights-to-css-vars.ts
  A canvas/components/BlockHeader-2123.html
```
