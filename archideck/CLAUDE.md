# ARCHIDECK — Operating Layer

This repository is a PPL± project with the Archideck meta-layer installed.

---

## ROUTING

**If you are working on PPL± (cards, decks, exercise library, Operis, validation):**

→ Read the root-level `CLAUDE.md` and `whiteboard.md` as normal.
→ The Archideck layer is ambient context. It does not override PPL± generation rules.
→ `scl-directory.md` is the full SCL spec for PPL± generation.
→ `exercise-library.md` is the exercise authority.

**If you are working on Archideck infrastructure (kernel updates, contracts, cross-project tools):**

→ Follow the session start sequence in `archideck/AGENT-CONTRACT.md`.
→ The kernel (`archideck/KERNEL.md`) is your primary reference.
→ Changes to the kernel require explicit session scope. Do not update KERNEL.md while generating cards.

**If you are working on another project (Graph Parti, Story Engine, Civic Atlas):**

→ Follow the session start sequence in `archideck/AGENT-CONTRACT.md`.
→ Read that project's own `CLAUDE.md` and `whiteboard.md` for project-specific rules.
→ The kernel is the shared language. The project docs are the project-specific law.

**If you are doing intake (raw idea capture, fractal bursts, research dumps):**

→ Write to `archideck/intake/YYYY-MM-DD-[slug].md` with minimal SCL tagging.
→ Do not sort into project directories.
→ Note the intake on the active project's whiteboard.

---

## WHAT THE ARCHIDECK IS

The Archideck is the meta-architectural layer. It is not a separate project — it is the root-level operating system that PPL± (and all future projects) runs on top of.

- **KERNEL.md** — Compressed SCL seed. The language. What any agent reads first.
- **CONTRACTS.md** — The Negotiosum switchboard. Cross-project state. What is active, queued, parked, done.
- **AGENT-CONTRACT.md** — Universal agent operating instructions. Session start sequence. Cross-project rules.
- **intake/** — Landing zone for raw ideas before Ralph Loop sorting.
- **projects/** — Project directory for non-PPL± projects.

PPL± lives at the repository root because this repo started as PPL±. The Archideck layer was added on top. Other projects live under `projects/`.

---

## WHAT THE ARCHIDECK IS NOT

- Not a replacement for project-level `CLAUDE.md` files.
- Not a constraint on PPL± generation rules.
- Not a place to route PPL± cards or card generation work.
- Not a separate codebase. No separate build system, no separate package.json, no separate CI.

The Archideck adds new files and directories at the repo root. It does not modify any existing PPL± files.

---

## CONTEXT HIERARCHY

When conflicts arise, this is the resolution order for PPL± work:

1. `whiteboard.md` — Active task board. Current session instructions.
2. `CLAUDE.md` (root) — PPL± operating instructions. Generation law.
3. `scl-directory.md` — Full SCL specification. Execution authority.
4. `archideck/KERNEL.md` — Compressed seed. Background context.

For other projects:
1. That project's `whiteboard.md`
2. That project's `CLAUDE.md`
3. `archideck/KERNEL.md`
4. `archideck/AGENT-CONTRACT.md`

---

🧮
