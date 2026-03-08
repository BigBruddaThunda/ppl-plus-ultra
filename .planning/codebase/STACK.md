# Technology Stack

**Analysis Date:** 2026-03-07

## Languages

**Primary:**
- Python 3.11 — All scripts: validation, generation, inventory, middle-math computation, scaffolding
- Markdown — Primary content format: card files, spec documents, cosmograms, seeds, all 1,680 workout blueprints
- SQL (PostgreSQL 15+) — Schema migrations in `sql/` (planned, not yet deployed)

**Secondary:**
- Bash — CI orchestration (`scripts/validate-deck.sh`, `scripts/run-full-audit.sh`, `scripts/ralph/ralph.sh`)
- JavaScript (CommonJS, Node) — GSD framework hooks in `.claude/hooks/` (statusline, context monitor, update checker)
- JSON — Data interchange: `middle-math/*.json`, `scripts/ralph/prd.json`, `.claude/gsd-file-manifest.json`

## Runtime

**Environment:**
- Python: 3.11 (pinned via devcontainer image `mcr.microsoft.com/devcontainers/python:3.11`)
- Node.js: v22.22.0 (available in dev environment, used by GSD hooks only)
- Bash: 5.2 (GNU bash, standard Linux shell)

**Package Manager:**
- pip (Python stdlib only + `pyyaml`)
- npm is not used for the Ppl± project itself (only `.claude/package.json` marks the GSD hooks directory as CommonJS)
- Lockfile: not present (no requirements.txt; dependency is pip-installed in `post-create.sh`)

## Frameworks

**Core:**
- None — The repo is a content generation system. No web framework is active in this phase.
- GSD (Get Shit Done) v1.22.4 — Workflow orchestration framework installed in `.claude/get-shit-done/`. Manages Claude Code planning, phase execution, agent dispatch, and session state.

**Testing:**
- None — No test framework is configured. Validation is done by `scripts/validate-card.py` (run via PostToolUse hook and CI).

**Build/Dev:**
- DevContainer — `mcr.microsoft.com/devcontainers/python:3.11` image, configured in `.devcontainer/devcontainer.json`
- GitHub Actions — Two workflows: `lint.yml` (baseline audit + PR hard gate) and `pylint.yml` (Python linting across all `.py` files)
- `jq` 1.7 — Required for `scripts/ralph/ralph.sh` (JSON parsing of `prd.json`)

## Key Dependencies

**Critical:**
- `pyyaml` 6.0.1 — YAML frontmatter parsing across all Python scripts; installed by `post-create.sh` and CI `pip install pyyaml`
- Python standard library only beyond pyyaml: `re`, `os`, `sys`, `json`, `pathlib`, `argparse`, `yaml`, `csv`, `subprocess`, `datetime`, `collections`, `typing`, `unicodedata`, `math`, `random`, `copy`

**Infrastructure:**
- `claude` CLI — Invoked directly from `scripts/ralph/ralph.sh` via `cat "$PROMPT" | claude --print` for automated loop iteration
- `amp` CLI — Alternative tool supported by ralph loop (`--tool amp`)
- `rg` (ripgrep) — Used inside CI workflow steps for searching card statuses; assumed available on GitHub Actions ubuntu-latest runner

## Configuration

**Environment:**
- `.env` file path is in `.gitignore` — contains `SUPABASE_DB_URL` and Stripe credentials (planned Phase 6+, not yet in use)
- Dev environment bootstrapped by `.devcontainer/post-create.sh`: `pip install pyyaml` only
- No `.nvmrc`, `.python-version`, or `pyproject.toml` present

**Build:**
- `.claude/settings.json` — Claude Code hook configuration: PostToolUse auto-validates cards, SessionStart fires progress dashboard and compact re-injection
- `.codex/config.toml` — OpenAI Codex CLI configuration (model, approval policy, sandbox mode, multi-agent thread limits)
- `.github/workflows/lint.yml` — CI pipeline: baseline audit on push, hard gate on PR changed cards
- `.github/workflows/pylint.yml` — Pylint across all Python files on every push (matrix: Python 3.8, 3.9, 3.10)
- `.gitattributes` — Present (contents standard)

## Platform Requirements

**Development:**
- Dev container (Docker + VS Code Dev Containers extension) OR any environment with Python 3.11+ and `pyyaml`
- VS Code extensions configured: `ms-python.python`, `yzhang.markdown-all-in-one`, `vstirbu.vscode-mermaid-preview`
- Black formatter configured as VS Code Python formatter (`python.formatting.provider: black`)
- Tab size: 2 spaces (VS Code setting)

**Production (Phase 4/5, planned — not active):**
- Next.js 14+ (App Router) + TypeScript — web frontend (seeded in `seeds/experience-layer-blueprint.md`)
- Supabase (PostgreSQL + Auth + Storage + Realtime) — database layer (SQL migrations in `sql/`)
- Vercel — hosting (auto-deploy from GitHub, ISR for room pages)
- Stripe — payments (two subscription products, webhooks)
- Resend — transactional email
- Framer Motion + `@use-gesture/react` — dial physics, gesture interaction
- Zustand — client state management
- Tailwind CSS — styling with Ppl± design tokens
- Android Auto / CarPlay — automotive layer (seeded in `seeds/automotive-layer-architecture.md`)

---

*Stack analysis: 2026-03-07*
