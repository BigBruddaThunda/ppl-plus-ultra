# M10 — Experience Layer

**Status:** NOT STARTED (seed architecture complete)
**SCL Zip:** 🖼 🌹 🟢 (Palladian × Venustas × Growth — building the experience)
**Contract:** `ppl-experience-layer`
**PPL Phase:** Phase 4

---

## Scope

Build the interactive web application that renders `.md` card files as interactive workout rooms. User accounts, session logging, and subscription model.

## Prerequisites

| Prerequisite | Status | Milestone |
|-------------|--------|-----------|
| Sufficient generated cards (critical mass) | 280/1,680 (16.7%) | M1–M7 |
| Middle-math weight vectors (rendering) | Complete (DRAFT values) | parked |
| Middle-math schemas (Supabase) | Spec only | parked |
| Stripe integration spec | Seeded | `seeds/stripe-integration-pipeline.md` |

## Tech Stack (from seed docs)

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js (App Router) |
| Backend/Auth | Supabase (PostgreSQL + Row Level Security) |
| Hosting | Vercel |
| Payments | Stripe |
| Database primary key | CHAR(4) numeric zip (e.g., `2123`) |
| Card rendering | Markdown → HTML via MDX |

Full spec: `seeds/experience-layer-blueprint.md`

## Core User Flows

1. **Browse:** Navigate using the 4-dial zip system. Order → Axis → Type → Color → Card.
2. **Train:** Open a card as an interactive workout room. Log sets, reps, load.
3. **Log:** Workout history writes to user ledger (`middle-math/user-context/`).
4. **Subscribe:** Tier 1 ($10/mo) = full card access. Tier 2 ($25-30/mo) = Operis + personalization.

## Seed Documents

| Document | Content |
|---------|---------|
| `seeds/experience-layer-blueprint.md` | Master tech architecture |
| `seeds/numeric-zip-system.md` | URL and database addressing |
| `seeds/mobile-ui-architecture.md` | 4-dial UI, tool drawer |
| `seeds/stripe-integration-pipeline.md` | Subscription products, webhooks |
| `seeds/data-ethics-architecture.md` | Privacy-first design |
| `seeds/claude-code-build-sequence.md` | 20-session build plan (Sessions A–N + V–Z) |
| `seeds/voice-parser-architecture.md` | Wilson voice navigation |
| `seeds/automotive-layer-architecture.md` | Android Auto / CarPlay |

## Build Sequence (from `seeds/claude-code-build-sequence.md`)

Sessions A–N: Core experience (card rendering, auth, logging, payments)
Sessions V–Z: Automotive layer (Android Auto, CarPlay, Wilson voice)

## Verification Criteria

- [ ] Cards render as interactive rooms from `.md` source
- [ ] User can log a workout session and view history
- [ ] Stripe checkout works for Tier 1 and Tier 2
- [ ] RLS gates content by subscription tier
- [ ] Zip-based URL routing works: `/zip/2123` → correct card
- [ ] Mobile UI functional on iOS Safari and Android Chrome
- [ ] Data export and deletion available to user

---

*Previous milestone:* M9 (Operis Pipeline V4)
*Final milestone in Phase 2–4 sequence.*
