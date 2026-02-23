---
name: retrofit-deck
description: Bring a pre-identity-layer deck up to V2 naming and format standards.
disable-model-invocation: true
argument-hint: "[deck-number e.g. 07]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

Retrofit Deck $ARGUMENTS to V2 standards.

## Workflow

### 1. Ensure Identity Document Exists
Check if `deck-identities/deck-$ARGUMENTS-identity.md` exists.
- If not: stop and report "Identity document not found. Run /build-deck-identity $ARGUMENTS first."
- If yes: read it fully before proceeding.

### 2. Read Naming Convention
Read `deck-identities/naming-convention.md`. Every renamed card must pass:
- No title starts with "The"
- No banned words: Protocol, Prescription, Program, System, Routine, Regimen, Blueprint, Formula, Method
- No vibe-speak: Full Send, Playground, Dial It In, etc.
- Template: `[Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]`
- Color context modifiers from the naming-convention doc

### 3. Find All Generated Cards for This Deck
Search `cards/` recursively for files with `deck: $ARGUMENTS` in frontmatter.

Use: `grep -rl "deck: $ARGUMENTS" cards/`

### 4. For Each Card
a. Read the card file completely
b. Check the current filename against naming convention
c. Check if the title in the frontmatter/body matches the identity document's title for this zip
d. If title violates convention OR does not match the identity doc:
   - Derive the compliant title from the identity document
   - Confirm the operator is correctly derived (Axis × Color polarity table)
   - Rename the file: old filename → `[zip]±[operator] [New Title].md`
   - Update frontmatter: change status to `GENERATED-V2`
e. If title is already compliant and matches identity doc: update status to `GENERATED-V2` only

### 5. Create Rename Log
Write `deck-identities/deck-$ARGUMENTS-rename-log.md`:
```
# Deck $ARGUMENTS Rename Log — [date]

## Cards Renamed
| Old Filename | New Filename | Reason |
|---|---|---|
| ... | ... | Title violation / Identity mismatch |

## Cards Status-Updated Only
| Filename | Change |
|---|---|
| ... | GENERATED → GENERATED-V2 |

## Cards Unchanged
| Filename | Status |
|---|---|
| ... | Already compliant |
```

### 6. Validate the Retrofitted Deck
Run: `bash scripts/validate-deck.sh cards/[order-folder]/[axis-folder]/`

Review all failures. If failures are content issues (not structural), log them for Jake's review — do not auto-fix content.

### 7. Run Exercise Coverage Audit
Run: `python scripts/audit-exercise-coverage.py cards/[order-folder]/[axis-folder]/`

Flag any duplicate primary exercises. These require manual resolution.

### 8. Update whiteboard.md
Append to the session log:
```
Deck $ARGUMENTS retrofitted to V2:
  - [X] cards renamed
  - [Y] cards status-updated
  - [Z] validation failures (logged in deck-identities/deck-$ARGUMENTS-rename-log.md)
```

## What NOT to Do
- Do not rewrite card content unless it clearly violates a hard constraint
- Do not change exercise selections — those require a full regeneration
- Do not rename a card to a title not supported by the identity document
- Do not mark a card CANONICAL — that is Jake's call
