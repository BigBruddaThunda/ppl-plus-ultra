# Technology Stack

**Project:** Ppl± Blank Canvas Infrastructure
**Domain:** Offline text parser + CSS derivation pipeline + Claude Code infrastructure
**Researched:** 2026-03-13
**Confidence:** HIGH (all versions verified against official docs and npm registry)

---

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| TypeScript | ^5 (current: 5.x) | Primary language for parser, pipeline, canvas | Already in use in `web/`. Strict types prevent errors in the weight vector math. The CSS derivation pipeline is pure math — TS makes it testable and auto-completing. |
| Vite | ^8 (current: 8.0.0) | Dev server + build tool for `canvas/` | Fastest HMR for `.tsx` hot-reload on localhost:3000. No framework lock-in. The canvas is a standalone tool, not a Next.js page — Vite is the right tool here. Next.js is overkill for a local dev canvas with no routing. |
| Vitest | ^4 (current: 4.1.0) | Unit + integration tests for parser and pipeline | Same config as Vite. Tests run in milliseconds. Native TypeScript. The parser's keyword scoring is pure functions — unit testing is trivial with Vitest. No Jest migration needed. |
| React | ^19 (already in web/) | Canvas UI layer (Session 3+) | Already installed in `web/`. Canvas uses same React for component hot-reload via Vite. Defer to Session 3 — infrastructure first. |

### Parser Layer (Subsystem 1 — Keyword Dictionary + Heuristic Classification)

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| fastest-levenshtein | ^1.0 | Levenshtein distance ≤ 2 for exercise name fuzzy matching | Use for exercise name detection only. The ~2,185 exercise names need typo-tolerance. "Romanian deadlfit" → "Romanian Deadlift". Built around Myers 32-bit algorithm — fastest JS/TS Levenshtein implementation. |
| fuse.js | ^7.1.0 | Fuzzy search fallback for alias expansion | Use as a second-pass when Levenshtein misses. Better at multi-word alias matching than pure edit distance. Zero dependencies. Well-maintained (7.1.0 current). |

**What NOT to use for the parser:**
- NLP libraries (node-nlp-typescript, compromise) — way too heavy for keyword scoring. They add dependency weight and require training data. The voice-parser architecture already specifies the algorithm: tokenize → score → max. Pure functions, no model.
- TensorFlow.js — this is explicitly out of scope. The parser must be offline and AI-free.
- ML text classifiers — same reason. The deterministic approach IS the architecture.

### CSS Derivation Pipeline (Subsystem 2 — Weight Vector → CSS Custom Properties)

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| style-dictionary | ^4.1.4 | Design token build pipeline: `design-tokens.json` → CSS custom properties + TS constants | Use for the static design token layer — the 8 Color palettes, 7 Order typographies, 6 Axis gradients. Runs at build time. Strictly typed in v4 with full `.d.ts` files. |

**The pipeline has two distinct layers:**

**Layer A — Static tokens (build-time, style-dictionary):**
The 8 Color palettes, 7 Order typographies, 6 Axis gradients, and block container styles. These don't change at runtime — they are the base palette. style-dictionary v4 compiles `design-tokens.json` → CSS variables file → TypeScript constants. One source of truth, multiple outputs.

**Layer B — Dynamic derivation (runtime, pure TypeScript):**
The `weightsToCSSVars()` function already specified in `seeds/experience-layer-blueprint.md`. Takes a 61-value weight vector, outputs `Record<string, string>` of CSS custom property overrides. This is pure math with `document.documentElement.style.setProperty()` — no library needed. Keep it as a typed pure function.

No library is needed for Layer B. The function is ~30 lines of arithmetic with the spec already written in `middle-math/rendering/ui-weight-derivation.md`. Adding a library here would be abstraction for its own sake.

### Claude Code Infrastructure (Subsystem 3 — Skills/Hooks/Subagents)

**No npm libraries needed.** Claude Code infrastructure is defined in markdown files and JSON config. The stack here is the format, not dependencies.

| Component | Format | Location | Notes |
|-----------|--------|----------|-------|
| Skills | `.claude/skills/<name>/SKILL.md` | Project-level: `.claude/skills/` | Frontmatter-driven. `name`, `description`, `context`, `agent`, `allowed-tools`. Invoked with `/skill-name`. |
| Hooks | JSON in `.claude/settings.json` | Project-level config | `PreToolUse`, `PostToolUse`, `SessionStart`, `Stop`, and 15 other lifecycle events. Three hook types: `command` (shell), `prompt` (single-turn LLM), `agent` (multi-turn with tool access). |
| Subagents | `.claude/agents/<name>.md` | Project-level: `.claude/agents/` | YAML frontmatter: `name`, `description`, `tools`, `model`, `skills`. Already in use in this repo (`card-generator.md`, `deck-auditor.md`). |

**Key format facts verified against official docs (March 2026):**

Skills frontmatter fields: `name`, `description`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `context`, `agent`, `hooks`.

Hooks go in `.claude/settings.json` (project) or `~/.claude/settings.json` (global). Hook event names: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PostToolUseFailure`, `Notification`, `SubagentStart`, `SubagentStop`, `Stop`, `TeammateIdle`, `TaskCompleted`, `InstructionsLoaded`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `SessionEnd`.

**Three hook types:**
- `"type": "command"` — shell command, stdin receives JSON, exit 2 blocks, exit 0 allows
- `"type": "prompt"` — single-turn LLM (Haiku by default), returns `{"ok": true/false, "reason": "..."}`
- `"type": "agent"` — multi-turn with tool access, up to 50 tool-use turns, 60s default timeout

Skills supersede commands: `.claude/skills/<name>/SKILL.md` and `.claude/commands/<name>.md` both work, but skills are recommended and add `context: fork`, subagent execution, and supporting files.

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| `jq` | JSON parsing in hook shell scripts | Required for the existing PostToolUse hook pattern (already in use: `jq -r '.tool_input.file_path'`). Install: `winget install jqlang.jq` on Windows. |
| `python` | Existing scripts (`validate-card.py`, `progress-report.py`) | Already installed. Keep for scripts — don't migrate to Node unless there's a reason. |

---

## Installation

```bash
# canvas/ standalone Vite workspace
npm create vite@latest canvas -- --template react-ts
cd canvas
npm install

# Parser fuzzy matching
npm install fastest-levenshtein fuse.js

# CSS token pipeline (in canvas/ or at repo root)
npm install -D style-dictionary

# Testing
npm install -D vitest @vitest/coverage-v8
```

The `canvas/` directory is a separate `package.json` workspace from `web/`. This isolates the canvas dependencies and keeps it clean. The parser and CSS pipeline libraries go into `canvas/package.json`. Do not add them to `web/package.json` — the web app will consume the compiled outputs, not the build tooling.

---

## Alternatives Considered

| Recommended | Alternative | Why Not |
|-------------|-------------|---------|
| Vite 8 (canvas standalone) | Next.js for canvas | Next.js is already used for `web/`. The canvas is a local dev tool, not a routed app. No SSR needed. No API routes needed. Vite starts faster and has simpler config for a single-page tool. |
| fastest-levenshtein | Fuse.js for all fuzzy matching | Fuse.js uses a bitap algorithm optimized for full-text search, not character-level edit distance. Exercise name fuzzy matching needs edit distance (Levenshtein ≤ 2), not relevance scoring. Use both: fastest-levenshtein for edit distance, fuse.js for alias/multi-word matching. |
| style-dictionary v4 (build-time) | CSS-in-JS (vanilla-extract, linaria) | CSS-in-JS adds runtime overhead and a compilation step. design-tokens.json → CSS variables is a build-time transform. style-dictionary does exactly this with no runtime dependency in the browser. |
| Pure TypeScript `weightsToCSSVars()` | style-dictionary for runtime derivation | style-dictionary is a build pipeline, not a runtime math engine. The weight-to-CSS derivation is arithmetic on a 61-value array — it does not need a pipeline. Keep it as a pure typed function. |
| Vitest 4 | Jest | Jest requires Babel or ts-jest config. Vitest shares Vite's config — zero extra setup for TypeScript. 2-4x faster than Jest for the test sizes this project needs. |
| `.claude/skills/` format | Old `.claude/commands/` format | Skills are the current standard (October 2025 → present). Commands still work but skills add `context: fork`, `allowed-tools`, supporting file directories, and automatic model invocation. Migrate incrementally — existing commands work. |

---

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| ML/NLP libraries for the parser | The parser architecture is explicitly AI-free (specified in `PROJECT.md` constraints). NLP libraries add weight and model dependencies. | Pure TypeScript keyword scoring with fastest-levenshtein for fuzzy matching. |
| Webpack / Create React App | Legacy tooling, 10-100x slower than Vite for HMR. CRA is officially deprecated. | Vite 8. |
| CSS-in-JS runtime libraries (styled-components, Emotion) | Runtime style injection conflicts with the weight-vector CSS custom property approach. `document.documentElement.style.setProperty()` is the correct mechanism — it works with Tailwind's CSS custom property layer already in `web/`. | CSS custom properties set directly via `style.setProperty()`. |
| Lodash for tokenization | Overkill. The tokenizer is `input.toLowerCase().split(/\s+/).filter(stopwords)` — ~5 lines. | Native string methods. |
| Any server-side parser endpoint | The parser must run client-side offline. No API round-trips. | Browser-side TypeScript module loaded once on initialization. |

---

## Stack Patterns by Subsystem

**If building the parser (Subsystem 1):**
- Single `vocab-dictionary.ts` file exports the `VocabDictionary` typed constant
- `exercise-library.md` → parsed at build time → `exercise-vocab.json` → imported into dictionary
- `scoreInput(input: string, dict: VocabDictionary): ParseResult` is the only public function
- fastest-levenshtein handles edit distance; fuse.js handles multi-word alias search
- Vitest unit tests: one test per worked example from `seeds/voice-parser-architecture.md`

**If building the CSS pipeline (Subsystem 2):**
- `design-tokens.json` → style-dictionary v4 → `tokens.css` (static layer) + `tokens.ts` (TS constants)
- `weightsToCSSVars(weights: WeightVector): CSSVarMap` is the runtime layer — pure function, no library
- The function lives in `canvas/src/rendering/weight-to-css.ts`
- Integration test: for each of the 8 primary Colors, verify dominant palette is correct

**If building Claude Code skills (Subsystem 3):**
- Skills go in `.claude/skills/<name>/SKILL.md` at project root (not inside `canvas/`)
- Use `disable-model-invocation: true` for skills with side effects (`/blank-canvas`, `canvas-to-production`)
- Use `context: fork` for the `canvas-renderer` subagent skill — keeps canvas rewrites in isolated context
- PostToolUse hook for art direction validation: `matcher: "Edit|Write"`, triggers Python validation script
- SessionStart hook with `matcher: "compact"` re-injects phase context after compaction (already designed in CLAUDE.md)

---

## Version Compatibility

| Package | Compatible With | Notes |
|---------|----------------|-------|
| `vitest@^4` | `vite@^8` | Same monorepo, shared config. Vitest 4 requires Vite 5+. |
| `style-dictionary@^4.1.4` | Node 18+ | v4 is async-first (`await buildAllPlatforms()`). Fully typed. Breaking change from v3: synchronous API removed. |
| `fuse.js@^7.1.0` | TypeScript 5.x | Ships own types. Zero dependencies. |
| `fastest-levenshtein@^1` | TypeScript 5.x | Ships own types. Zero dependencies. |
| `react@^19` (canvas) | `vite@^8` | Vite's React plugin (`@vitejs/plugin-react`) supports React 19. |
| `next@16.1.6` (web/) | `react@19.2.3` | Already installed and confirmed working. Do not change. |

---

## Existing Stack (web/) — Do Not Change

The `web/` directory already has a working stack. These versions are confirmed from `web/package.json`:

```
next: 16.1.6
react: 19.2.3
react-dom: 19.2.3
zustand: ^5.0.11
framer-motion: ^12.35.2
@use-gesture/react: ^10.3.1
@supabase/supabase-js: ^2.99.0
@supabase/ssr: ^0.9.0
tailwindcss: ^4
stripe: ^20.4.1
gray-matter: ^4.0.3
typescript: ^5
```

The canvas infrastructure lives in `canvas/` (separate package.json), not inside `web/`. Parser and CSS pipeline outputs will be compiled artifacts that `web/` can eventually import as JSON/TS modules — no circular dependencies.

---

## Sources

- Official Claude Code Skills docs: https://code.claude.com/docs/en/skills — skills format, frontmatter fields (HIGH confidence)
- Official Claude Code Hooks docs: https://code.claude.com/docs/en/hooks-guide — hook lifecycle, event types, JSON format (HIGH confidence)
- Vitest 4.1.0 release: https://vitest.dev/ — version confirmed (HIGH confidence)
- style-dictionary v4 migration: https://styledictionary.com/versions/v4/migration/ — v4 async API confirmed (HIGH confidence)
- fuse.js 7.1.0 on npm: https://www.npmjs.com/package/fuse.js — version confirmed (HIGH confidence)
- fastest-levenshtein on npm: https://www.npmjs.com/package/fastest-levenshtein — Myers algorithm, TypeScript support confirmed (HIGH confidence)
- Vite 8.0.0 on npm: https://www.npmjs.com/package/vite — current version confirmed (HIGH confidence)
- `web/package.json` — existing stack versions confirmed by direct file read (HIGH confidence)

---

*Stack research for: Ppl± Blank Canvas Infrastructure — offline parser, CSS derivation pipeline, Claude Code skills/hooks/subagents*
*Researched: 2026-03-13*
