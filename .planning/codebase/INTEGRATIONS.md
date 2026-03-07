# External Integrations

**Analysis Date:** 2026-03-07

## Current Phase Status

PPL± is in Phase 2 (Workout Generation). No external services are active or connected. This document describes: (1) what is active now, and (2) what is architecturally specified for Phase 4+. Integration seeds are committed to `seeds/` but not built.

---

## Active Integrations (Phase 2 — current)

### Claude CLI (`claude`)
- **Role:** AI backbone for workout card generation and session automation
- **Invocation:** Direct CLI call from `scripts/ralph/ralph.sh`: `cat "$PROMPT" | claude --print`
- **Also invoked:** Claude Code reads CLAUDE.md and whiteboard.md at session start; all card generation runs through Claude Code or Codex agents
- **Auth:** API key managed outside the repo (not committed)

### Amp CLI (`amp`)
- **Role:** Alternative AI tool for ralph loop automation
- **Invocation:** `cat "$PROMPT" | amp` (via `scripts/ralph/ralph.sh --tool amp`)
- **Status:** Supported but not primary

### GitHub Actions CI
- **Role:** Automated validation of card content on push and PR
- **Workflow 1:** `.github/workflows/lint.yml` — baseline audit of all decks with generated cards; PR hard gate runs `scripts/check-card-schema.py` and `scripts/lint-scl-rules.py` on changed cards
- **Workflow 2:** `.github/workflows/pylint.yml` — pylint across all Python scripts on every push
- **Auth:** GitHub Actions default token (standard)
- **Artifacts:** Uploads `scripts/.artifacts/card-inventory.json` and `card-inventory.csv` with 30-day retention

### OpenAI Codex CLI
- **Role:** Alternative AI agent for card generation and validation workflows
- **Config:** `.codex/config.toml` — model: `gpt-5.3-codex`, multi-agent enabled, 5 thread max
- **Agents defined:** `generator`, `validator`, `explorer`, `reviewer` (plus all GSD agents)
- **Auth:** API key managed outside the repo

---

## Planned Integrations (Phase 4+, not built)

All specifications below are committed as seed documents. No code exists. Environment variables referenced are planned — none are present in the running environment.

### Supabase (PostgreSQL + Auth + Storage + Realtime)
- **Role:** Primary database, user authentication, file storage, community realtime
- **Spec:** `seeds/experience-layer-blueprint.md`, `seeds/data-ethics-architecture.md`
- **Schema:** 10 SQL migrations in `sql/` (ready to run — schema is fully specified, not yet deployed)
  - `sql/001` — exercise_library
  - `sql/002` — exercise_families
  - `sql/003` — user_ledger
  - `sql/004` — user_profile
  - `sql/005` — user_toggles
  - `sql/006` — zip_metadata (1,680 rows, one per zip code)
  - `sql/007` — zip_metadata population (4-way cross join)
  - `sql/008` — room schema (rooms, room_visits, room_votes, bloom_history, nav edges)
  - `sql/009` — exercise_registry (2,085 exercises with EX-0001–EX-2085 IDs)
  - `sql/010` — exercise_knowledge (coaching content, auto-seeded from registry)
- **Auth method:** `auth.uid()` via Supabase RLS policies on all user-scoped tables
- **Realtime:** Per-zip Supabase Realtime channels for the 🐬 community floor
- **Required env vars (planned):** `SUPABASE_DB_URL`, `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`
- **Deploy command (when ready):** `supabase db push` or `psql "$SUPABASE_DB_URL" -f sql/001-...`

### Stripe
- **Role:** Subscription payments — two products, checkout, customer portal, webhook lifecycle
- **Spec:** `seeds/stripe-integration-pipeline.md`
- **Products:**
  - `ppl_library_card` — Tier 1, $10/month (workout access, logging, history)
  - `ppl_residency` — Tier 2, $25–30/month (+ community floor, program builder, coaching mode)
- **Free tier:** Operis read + zip previews (no subscription required)
- **Webhook events:** `customer.subscription.created`, `updated`, `deleted`, `invoice.payment_succeeded`, `invoice.payment_failed`
- **Webhook handler:** Updates Supabase `user_profile.tier` on every subscription lifecycle event
- **RLS gating:** Supabase RLS enforces content access by tier at the database level
- **Required env vars (planned):** `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`, `STRIPE_PRICE_ID_TIER1`, `STRIPE_PRICE_ID_TIER2`

### Vercel
- **Role:** Hosting, auto-deploy from GitHub, edge functions, ISR for room pages
- **Spec:** `seeds/experience-layer-blueprint.md`, `seeds/platform-architecture-v2.md`
- **Deploy trigger:** Push to main branch
- **ISR:** Room pages (`/zip/[zipcode]`) use Incremental Static Regeneration

### Resend
- **Role:** Transactional email only (receipts, account notices)
- **Spec:** `seeds/experience-layer-blueprint.md`
- **Required env vars (planned):** `RESEND_API_KEY`

### Android Auto / CarPlay
- **Role:** Automotive layer — Operis read aloud, voice zip navigation, curated playlists
- **Spec:** `seeds/automotive-layer-architecture.md`
- **Voice system:** Wilson TTS identity specified in `seeds/wilson-voice-identity.md`
- **Status:** Phase 7+ — not blocked by current work

---

## Data Storage (current)

**Databases:**
- None active. All data is flat files in the repository.

**File Storage:**
- Git repository is the sole data store for Phase 2
- Card files: `cards/[order]/[axis]/[type]/[zip]±[op] [Title].md`
- Exercise library: `exercise-library.md` (~133KB, ~2,185 exercises)
- Middle-math data: `middle-math/*.json` (zip-registry.json, weight-vectors.json, exercise-library.json, exercise-registry.json, navigation-graph.json, design-tokens.json, content-type-registry.json)

**Caching:**
- `scripts/.artifacts/` — CI artifact output (card-inventory.json, card-inventory.csv), not committed to git
- `.claude/cache/gsd-update-check.json` — GSD update check cache (written by `.claude/hooks/gsd-check-update.js`)
- `/tmp/claude-ctx-[session].json` — Context window metrics bridge file (written by `.claude/hooks/gsd-statusline.js`, ephemeral)

---

## Authentication and Identity

**Current:** None. Repository is local/git only. No user accounts in Phase 2.

**Planned (Phase 4+):**
- Supabase Auth — handles identity, session tokens, OAuth if added
- Subscription tier (`free` | `tier1` | `tier2`) stored on `user_profile` table
- RLS enforces access at DB level; no separate middleware auth check required

---

## Monitoring and Observability

**Error Tracking:** None configured.

**Logs:**
- Python scripts write to stdout; CI captures via GitHub Actions logs
- Validation errors written to stdout by `scripts/validate-card.py` (PostToolUse hook captures output)
- Progress dashboard written to stdout by `scripts/progress-report.py` (SessionStart hook)

---

## CI/CD and Deployment

**Hosting (current):** GitHub only. No deployment target in Phase 2.

**CI Pipeline:**
- GitHub Actions, two workflows in `.github/workflows/`
- `lint.yml` runs on push to main and on PRs to main
- `pylint.yml` runs on all pushes, matrix Python 3.8/3.9/3.10
- `ripgrep` (`rg`) used inside CI bash steps (assumed available on ubuntu-latest)

**Deployment (planned Phase 4+):** Vercel, triggered by GitHub push to main.

---

## Webhooks and Callbacks

**Incoming (planned):**
- Stripe webhook handler — receives subscription lifecycle events, updates Supabase profile tier
- Route: `/api/webhooks/stripe` (Next.js API route, Phase 6)

**Outgoing (planned):**
- None specified beyond Stripe Checkout redirects and Customer Portal return URLs

---

## External Data Sources

**ExRx.net:** Referenced as the factual register for exercise information in `scl-deep/vocabulary-standard.md`. Exercises in `exercise-library.md` follow ExRx naming convention. No API connection — human-curated reference only.

**Historical events database:** `operis-editions/historical-events/` — 366 date-indexed files planned (MM-DD.md format), currently empty stubs. Scaffold script: `scripts/operis/scaffold_historical_events.py`. Operis Prompt 1 (Researcher) checks this path before web research.

**Web research:** Operis generation pipeline (Prompts 1–4 in `seeds/operis-*.md`) calls for web research on historical events and astronomical data. Executed in external AI sessions (Genspark, Claude.ai web), not via API from this repo.

---

## Environment Configuration

**Required now (active):**
- None. All scripts run against local filesystem. No env vars required for Phase 2 operation.

**Required for Phase 4+ (planned, not yet used):**
- `SUPABASE_DB_URL` — PostgreSQL connection string
- `NEXT_PUBLIC_SUPABASE_URL` — Supabase project URL
- `NEXT_PUBLIC_SUPABASE_ANON_KEY` — Supabase anon key
- `SUPABASE_SERVICE_ROLE_KEY` — Service role key (webhook handler)
- `STRIPE_SECRET_KEY` — Stripe API key
- `STRIPE_WEBHOOK_SECRET` — Stripe webhook signing secret
- `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` — Stripe publishable key
- `STRIPE_PRICE_ID_TIER1` — Price ID for Library Card product
- `STRIPE_PRICE_ID_TIER2` — Price ID for Residency product
- `RESEND_API_KEY` — Resend transactional email

**Secrets location:** `.env` file (gitignored). `supabase/.temp/` is also gitignored.

---

*Integration audit: 2026-03-07*
