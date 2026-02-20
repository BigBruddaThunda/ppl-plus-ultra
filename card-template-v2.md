# card-template-v2.md — PPL± Card Format Standard

This is the v2 card template. It replaces the v1 15-element required format.
Generated under this standard carry `status: GENERATED-V2`.

Read `generation-philosophy.md` before generating any card.

---

## REQUIRED ELEMENTS (8)

These eight elements must be present in every card. Everything else is optional and should only be included when it serves the specific zip code's Color.

1. **Frontmatter** — zip, operator, status, deck, order, axis, type, color, blocks
2. **Title** — `# [TYPE EMOJI] [Title] [TYPE EMOJI]` with flanking Type emojis
3. **Subtitle line** — training modality, muscle targets, honest time estimate
4. **CODE line** — the 4-dial zip code
5. **Intention** — quoted, one sentence, active voice, direct. Frame the work, don't hype it.
6. **Numbered blocks** with emoji names and heavy border separators (═══)
7. **🚂 JUNCTION** — log space (blank fields, not pre-filled) + 1–3 follow-up zips with one-line rationale
8. **🧮 SAVE** — 1–2 sentences. Transfer the work. Do not praise.

---

## OPTIONAL ELEMENTS

Include these when they add value for the specific Color. Do not include by default.

- **Sub-block zip codes** `⛽🏛🛒🔵♨️ (Warm-Up | Chest | Basics | Tier 2–3)` — useful as metadata in complex cards, optional elsewhere
- **Tree notation** `├─ │ └─` — useful when showing nested structure, optional when a list reads cleanly
- **Operator call after block header** — include when the operator meaningfully changes how the block is read
- **Inline cues on exercises** — include only when non-obvious. Max 1–2 per exercise, max 3–6 words.
- **🎯 Intention block** — can precede the first block when the session has a specific orientation needed
- **Explicit rest lines inside blocks** — always specify rest in 🔵 (it's the prescription). In other Colors, specify when Color calls for it or when it differs from the Order default.

---

## THE FORMAT

```markdown
---
zip: [ORDER][AXIS][TYPE][COLOR]
operator: [EMOJI] [latin name]
status: GENERATED-V2
deck: [number]
order: [emoji] [Name] | [load%] | [rep range] | [rest] | CNS: [level]
axis: [emoji] [Name] | [short description]
type: [emoji] [Name] | [muscles]
color: [emoji] [Name] | Tier [X–X] | GOLD: [Yes/No] | [short format description]
blocks: [emoji] → [emoji] → ...
---

# [TYPE EMOJI] [Title] [TYPE EMOJI]

[Training modality] | [Muscles] | [Time estimate]

CODE: [ORDER][AXIS][TYPE][COLOR]

> "[Intention — one sentence, active voice, direct]"

═══════════════════════════════════════

## 1. ♨️ WARM-UP

[Block content proportional to Color. Brief for most Colors. Detailed for ⚫ and ⚪.]

═══════════════════════════════════════

## 2. [BLOCK EMOJI] [BLOCK NAME]

[Operator call if relevant]

[Block content]

Rest: [rest specification]

═══════════════════════════════════════

[... additional blocks ...]

═══════════════════════════════════════

## [N]. 🚂 JUNCTION

\`\`\`
Date: ___________
[Primary lift]: ___/___/___  ×  [reps]
[Secondary lift]: ___/___    ×  [reps]
[Any Color-specific fields]
\`\`\`

Next →
- [zip] — [one-line reason]
- [zip] — [one-line reason]
- [zip] — [one-line reason]

═══════════════════════════════════════

## 🧮 SAVE

[1–2 sentences. Transfer the work forward. Do not praise.]
```

---

## CONTENT SCALING BY COLOR

The same block structure produces different content at different Colors. Let the Color drive the depth and tone of each block.

| Color | ♨️ Warm-Up | 🪫 Release | Cue density | Log format |
|-------|-----------|-----------|-------------|------------|
| ⚫ Teaching | Full, explained | Full, explained | High | Detailed |
| 🔵 Structured | Brief | Brief | Low | Exact: load/reps/RPE per set |
| ⚪ Mindful | Slow, breathwork | Full, timed | Low | Tempo held Y/N |
| 🟡 Fun | Brief | Brief | Low | Sandbox option + finding |
| 🔴 Intense | Brief | Standard | Low | Load/reps/rest |
| 🟣 Technical | Standard | Standard | Medium | Quality notes |
| 🟢 Bodyweight | Brief | Brief | Low | Load-free, reps only |
| 🟠 Circuit | Brief | Brief | Low | Rounds/time |

---

## EXERCISE FORMAT

Reps before exercise name. Type emoji before exercise name.

```
10 🛒 Barbell Bench Press
```

Not:
```
🛒 Barbell Bench Press × 10
```

Sets on individual lines with load:
```
- Set 1: 78% × 5
- Set 2: 80% × 5
```

Or in table form for 🔵 Structured:
```
| Set | Load | Reps |
|-----|------|------|
| 1   | 78%  | 5    |
```

Cues in parentheses at end, 3–6 words, when needed:
```
- Set 1: 78% × 5 (bar to lower sternum)
```

If the exercise name is self-explanatory, no cue is needed.

---

## BLOCK SEQUENCE REFERENCE

From CLAUDE.md — use as the starting point, then modify for Color:

```
🐂 Foundation:   4–6 blocks  ♨️ 🔢/🛠 🧈 🧩 🧬 🚂
⛽ Strength:     5–6 blocks  ♨️ ▶️ 🧈 🧩 🪫 🚂
🦋 Hypertrophy:  6–7 blocks  ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂
🏟 Performance:  3–4 blocks  ♨️ 🪜 🧈 🚂
🌾 Full Body:    5–6 blocks  ♨️ 🎼 🧈 🧩 🪫 🚂
⚖ Balance:      5–6 blocks  ♨️ 🏗 🧈 🧩 🪫 🚂
🖼 Restoration:  4–5 blocks  🎯 🪫 🧈 🧬 🚂
```

Color modifications:
- ⚪: Drop 🧩 if it crowds the session. Extend 🪫. Let 🧈 breathe.
- 🟡: Replace 🧩 with 🏖. Keep 🧈 as the anchor.
- 🔴: 🧩 may superset with 🧈. 🌋 possible if zip calls for it.
- 🟣: Fewer blocks. Extended rest between each.
- 🟠: 🧈/🧩 merge into 🎱 ARAM with loop logic.
- ⚫: Add 🛠 Craft. More explanation throughout.

---

## WHAT CHANGED FROM V1

**Reduced required elements:** 15 → 8. The seven dropped elements (sub-block zip codes, tree notation, operator calls, inline cues, Type emoji before every exercise, sets-with-Order-emoji format, explicit Intention as a separate block) are now optional. Include them when they serve the card, not because the template requires them.

**Color drives structure:** The block sequence and content depth scale to the Color's personality, not to a uniform template applied across all 8 Colors.

**Density from the zip code:** The workload flows from what the zip code implies. Padding blocks to fill space is not generation.

**Percentage honesty:** Exact percentages live in 🔵 and 🟣 where precision is the Color's point. All other Colors use ranges or feel-based language where appropriate.

**Block minimalism:** ♨️ and 🪫 are short by default. Content inside them scales up only when the Color calls for it (⚫ or ⚪).

---

🧮
