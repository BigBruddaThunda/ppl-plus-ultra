# AGENT-CONTRACT.md — Universal Agent Operating Instructions

This contract loads before any project-specific CLAUDE.md.
It is the session start sequence and cross-project operating rules for any AI agent working inside the Archideck.

---

## SESSION START SEQUENCE

Every session follows this sequence in order. Do not skip steps.

1. **Read `archideck/KERNEL.md`** — The language. Always first. Compressed SCL seed. Enough context to understand the system.
2. **Read `archideck/CONTRACTS.md`** — The switchboard. What is active, queued, and parked across all projects.
3. **Determine which project/contract is the focus** — Ask the user or derive from context. If unclear, list the ACTIVE contracts and ask which to work on.
4. **Read that project's `CLAUDE.md` and `whiteboard.md`** — Project-specific rules and current state. These override defaults but do not contradict the kernel.
5. **Work.**

For PPL±: the project-level `CLAUDE.md` is at the repository root. It is the full operating specification. The KERNEL is context. The CLAUDE.md is the law for PPL± generation.

---

## CROSS-PROJECT RULES

**Containment.** Each project is containered. Do not modify files in project A while working on project B unless explicitly told to. If you find yourself editing `cards/` while scoped to Graph Parti, stop.

**Universal insight capture.** If work in one project produces a refinement to SCL grammar, a shared tool idea, or a kernel update, write it to `archideck/intake/` with minimal tagging. Do not modify the kernel mid-session unless kernel update is the stated task.

**Shared tools.** Cross-project scripts and utilities live in `shared/`. Project-specific scripts stay in their project directory. If a tool is used in two projects, it belongs in `shared/`.

**The kernel is the authority.** Project-level documents extend the kernel. They never contradict it. If a project doc conflicts with KERNEL.md, the kernel wins. Flag the conflict; do not silently override.

**The full spec is the authority for PPL±.** Within the PPL± project, `scl-directory.md` is the uncompressed specification. If there is a conflict between KERNEL.md and scl-directory.md, scl-directory.md wins for PPL± generation. The kernel is a compressed reference, not an override.

---

## INTAKE PROTOCOL

When the user dumps raw ideas, fragments, connections, or fractal bursts:

1. **Capture everything.** Do not filter or judge. The dump is the input; your job is to receive it.
2. **Tag each item with minimal SCL context.** Relevant project (if obvious), relevant Order (if clear), relevant emojis (if they apply).
3. **Write to `archideck/intake/YYYY-MM-DD-[slug].md`** — one file per dump or session.
4. **Do not sort into project directories** unless explicitly told to. Intake stays in intake until a Ralph Loop session sorts it.
5. **Note the intake on the whiteboard.** Add a row to the appropriate Color section of the Negotiosum indicating intake was received.

The intake directory is not a trash can. It is a landing zone. Everything in it has value; it just hasn't been assigned a room yet.

---

## NEGOTIOSUM CONTRACT PROTOCOL

The Negotiosum (`whiteboard.md` in each project, `archideck/CONTRACTS.md` for cross-project) is the living state of all work.

**Creating contracts:**
- A contract is created when work is scoped and has a committed deliverable.
- A contract has: scope, current state, next physical action, location, and blockers.
- New contracts go into QUEUED unless work starts immediately (then ACTIVE).

**Updating contracts:**
- Move QUEUED → ACTIVE when work begins in a session.
- Move ACTIVE → COMPLETED when the deliverable is verified.
- Move ACTIVE → PARKED when work stops without completion and without a clear resumption date.

**The next physical action is mandatory.** A contract without a next physical action is a wish, not a contract. If you cannot state the next action in one sentence, the contract is not ready.

---

## THE KERNEL RULE

The kernel (`archideck/KERNEL.md`) is compressed SCL — the generative grammar, not the full specification.

- Read KERNEL.md to **understand** the system.
- Read `scl-directory.md` to **execute** within the system.
- Read the project's `CLAUDE.md` to **follow** the project's rules.

Do not attempt to generate PPL± workouts from KERNEL.md alone. It does not contain the exercise library routing, tonal rules, validation checklist, or block sequence guidelines needed for correct generation. It contains the grammar. The full spec contains the execution rules.

---

## WHEN THINGS CONFLICT

**KERNEL.md vs. scl-directory.md:** scl-directory.md wins. The kernel is a compression. If the compression missed something, the full spec is authoritative.

**scl-directory.md vs. CLAUDE.md:** CLAUDE.md wins for the PPL± project. CLAUDE.md is the operating layer; scl-directory.md is the reference.

**CLAUDE.md vs. whiteboard.md:** whiteboard.md wins for the current session. If whiteboard.md says to do X and CLAUDE.md says to do Y by default, do X. The whiteboard is the active task board.

**Handoff document vs. whiteboard.md:** Flag the conflict. The handoff may reference outdated state. Do not proceed until the conflict is resolved.

---

## PARALLEL WORK POSTURE

The Archideck assumes multiple projects are active simultaneously. The kernel enables this by providing shared grammar without shared context pollution.

When working across projects in a single session:
- State which contract is active at the start of each context switch.
- Do not carry assumptions from one project into another.
- If you notice a cross-project connection, write it to `archideck/intake/` rather than acting on it mid-session.

Parallel work is not multitasking. It is containered work in sequence, with a shared kernel that makes the switching fast.

---

🧮
