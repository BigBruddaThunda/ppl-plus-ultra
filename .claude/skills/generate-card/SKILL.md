---
name: generate-card
description: Generate a single PPL± workout card from its zip code. Reads identity doc, validates, generates, renames stub, logs to whiteboard.
disable-model-invocation: true
argument-hint: "[zip-code e.g. ⛽🌹🛒🔵]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

Generate a workout card for zip code $ARGUMENTS.

## Workflow

### 1. Parse the Zip Code
Extract Order, Axis, Type, Color from $ARGUMENTS.

Emoji sets:
- Orders: 🐂⛽🦋🏟🌾⚖🖼
- Axes: 🏛🔨🌹🪐⌛🐬
- Types: 🛒🪡🍗➕➖
- Colors: ⚫🟢🔵🟣🔴🟠🟡⚪

### 2. Determine the Deck Number
Use the Order×Axis grid from CLAUDE.md to find the deck number.

### 3. Load Identity Document
Check if `deck-identities/deck-[XX]-identity.md` exists.
- If yes: read it. Find the zip code's row. Extract the primary exercise, title, operator, and block sequence.
- If no: proceed with SCL rules from `scl-directory.md` and `CLAUDE.md` only.

### 4. Locate the Stub File
Find the stub at: `cards/[order-folder]/[axis-folder]/[type-folder]/[zip]±.md`

Folder naming: `[emoji]-[slug]` format. Example: `⛽-strength`, `🏛-basics`, `🛒-push`

Read the stub frontmatter to confirm zip code and parameters.

### 5. Load Exercise Library
Read `exercise-library.md` — specifically the sections relevant to this Type:
- 🛒 Push → Sections C (Chest), B (Shoulders), E (Arms — triceps)
- 🪡 Pull → Sections D (Back), B (Shoulders posterior), E (Arms — biceps), G (Hips — hinges)
- 🍗 Legs → Sections H (Thighs), G (Hips & Glutes), I (Lower Leg)
- ➕ Plus → Sections F (Core), J (Olympic), K (Plyometrics), L (Kettlebell), Q (Strongman)
- ➖ Ultra → Sections M (Cardio), O (Agility), N (Sport)

All exercises must come from this library. No invented exercises.

### 6. Generate the Workout

Follow all rules in CLAUDE.md. The constraint hierarchy:
1. ORDER — hard ceiling, never exceeded
2. COLOR — hard filter, equipment is binary
3. AXIS — soft bias, ranks selection
4. Equipment — practical filter

Run the full validation checklist from CLAUDE.md mentally before writing.

All 15 required format elements must be present:
1. Title with flanking Type emojis
2. Subtitle: modality, targets, time estimate
3. CODE line: 4-dial zip code
4. 🎯 INTENTION: quoted, one sentence, active voice
5. Numbered BLOCKS with emoji names and ═══ separators
6. At least one Operator call after a block header
7. Sub-block zip codes with parenthetical expansion
8. Tree notation (├─, │)
9. Reps before exercise name: "10 🍗 Squat"
10. Type emoji before exercise name
11. Cues in parentheses, 3–6 words, conversational
12. Sets on individual lines with Order emoji
13. Rest specified for every block
14. 🚂 JUNCTION with 1–3 next-session zip codes and rationale
15. 🧮 SAVE with 1–2 sentence closing principle

### 7. Write the Card
Replace stub content. Update frontmatter:
- `status: EMPTY` → `status: GENERATED`
- Keep all other frontmatter fields

### 8. Derive Title and Rename File
Follow `deck-identities/naming-convention.md`:
- Template: `[Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]`
- No "The" prefix
- No banned words: Protocol, Prescription, Program, System, Routine, Blueprint, Formula, Method
- No vibe-speak (Full Send, Dial It In, Playground, etc.)

Derive the operator from the Operator table (Axis × Color polarity).

Rename: `[zip]±.md` → `[zip]±[operator-emoji] [Title].md`

### 9. Validate
Run: `python scripts/validate-card.py "[new-file-path]"`

If validation fails:
- Read the failure messages
- Fix the issues
- Re-run validation
- Do not proceed until the card passes

### 10. Log
Append to whiteboard.md session log:
```
- [zip]±[operator] [Title] — GENERATED
```

## Tonal Rules (enforced)
- Direct, not flowery
- Technical but human
- Conversational cues ("Hips back, not down." not "optimize neuromuscular recruitment")
- No motivational filler. No "You got this!" No "Crush it today!"
- 🎯 Intention: frame the work, do not hype it
- 🧮 SAVE closing: transfer the work, do not praise the user
