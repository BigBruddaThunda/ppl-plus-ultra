# Ralph Loop — PPL± Zip-Web Pod Population

You are an autonomous agent working in the PPL± repository.
Your task is to populate zip-web pods — one deck per iteration.

---

## Instructions

1. Read `scripts/ralph/prd.json`
2. Read `scripts/ralph/progress.txt` — check **Codebase Patterns** first for prior learnings
3. Ensure you are on branch `zip-web/populate` (create from main if it does not exist)
4. Pick the highest priority story where `passes: false`
5. Read `zip-web/zip-web-rules.md` for all selection rules
6. Read `zip-web/zip-web-signatures.md` for fatigue profiles of all hub zips in the target deck
7. Read `zip-web/zip-web-registry.md` to confirm valid zip codes for all neighbors
8. If `zip-web/zip-web-pods/deck-07-pods.md` exists and is populated, use it as the **quality bar** — match that level of coaching logic and rationale depth
9. Open the stub file for the target deck in `zip-web/zip-web-pods/`
10. For each of the 40 zip codes in that deck:
    - Identify the hub's fatigue signature (from signatures file)
    - Apply the Type exclusion rule: assign the 4 remaining Types to N/E/S/W
    - Select specific neighbor zips using the coaching logic in zip-web-rules.md
    - Write 1–2 sentence coaching rationale for each directional pairing
    - Run the pod validation checklist from zip-web-rules.md before writing
11. Commit with message: `feat: [Story ID] - Populate pods for Deck XX`
12. Update `prd.json`: set `passes: true` for the completed story
13. Append learnings to `scripts/ralph/progress.txt`

---

## Critical Rules

- **ONE deck per iteration.** No more.
- **Every neighbor must be a valid zip** — exists in zip-web-registry.md as a 4-emoji combination of valid SCL dials.
- **No Type repetition** within a pod's N/E/S/W.
- **Hub Type cannot appear** in any N/E/S/W slot.
- **Follow directional character:**
  - N = Progression (builds on hub state)
  - E = Balance (corrects what hub neglected)
  - S = Recovery-Aware (respects accumulated fatigue)
  - W = Exploration (opens new training vector)
- **Coaching rationale must make training sense** — think like a personal trainer who knows these systems.
- **Aim for variety** across Orders, Axes, and Colors in the 4 neighbors of any hub.
- After high-CNS hubs (⛽/🏟), S and E neighbors should not also be high-CNS.
- After high-density hubs (🔴🟠), S neighbor must be lower density (⚪, ⚫, 🟣).
- If a rule is ambiguous, document your interpretation in `progress.txt` and make your best judgment.

---

## Quality Reference

`zip-web/zip-web-pods/deck-07-pods.md` is the quality bar.

Match that level of:
- Specificity in coaching rationale (not generic — reference the actual hub character)
- Consistency in Type direction assignments within a deck
- Fatigue-aware neighbor selection (S is always lower demand than hub)
- Dial variety across the 4 neighbors

---

## Stop Condition

When all stories have `passes: true`, reply with:

```
COMPLETE
```

---

## Output Format

After completing a deck, append to `scripts/ralph/progress.txt`:

```
--- Session [date] ---
Story: [Story ID] - [Title]
Deck: [deck number] — [Order × Axis]
Type direction pattern used: [e.g., 🛒→N:🪡,E:🍗,S:➖,W:➕]
Patterns discovered: [any patterns, edge cases, or rules clarified]
Neighbor selection notes: [any notable decisions made]
```
