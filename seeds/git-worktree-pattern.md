# Git Worktree Pattern

**status: PLANNED**

---

## What

`git worktree` lets you check out multiple branches into separate
directories simultaneously. All worktrees share the same `.git`
history — no duplicate clones.

---

## Why PPL± Needs This

Multiple parallel work streams:
- `main`: always clean, current truth
- Feature branches: cosmogram-infrastructure, linters, deck generation
- Claude Code can work in one worktree while Jake reviews another
- Deck generation continues on main while infra work happens on branches

---

## Convention

Worktree directories as siblings of the main repo:

```
~/projects/
├── ppl-plus-ultra/          ← main (always)
├── ppl-cosmogram/           ← cosmogram-infrastructure branch
├── ppl-linters/             ← feature/linters branch
└── ppl-deck-gen/            ← active deck generation branch
```

---

## Commands

```bash
git worktree add ../ppl-[feature] [branch-name]
git worktree list
git worktree remove ../ppl-[feature]
```

---

## Integration with Claude Code

Claude Code sessions specify which worktree they operate in.
`whiteboard.md` tracks active worktrees and their branch assignments.

---

## When to Adopt

Adopt when parallel branch work becomes frequent enough to justify.
Currently: one branch at a time is sufficient.

🧮
