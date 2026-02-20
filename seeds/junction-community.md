---
planted: 2026-02-20
status: SEED
phase-relevance: Phase 5/6 (HTML + User Accounts)
blocks: nothing in Phase 2-4
connects-to: seeds/axis-as-app-floors.md (Sociatas floor)
---

# 🚂 Junction — Community Layer & Almanac Queue

## One Sentence

The 🚂 Junction block evolves from static follow-up suggestions into a living community recommendation surface where usage patterns, user votes, and personal history converge to suggest the next workout zip code — and selecting one queues it into the user's personal Almanac.

## Three Horizons

### Horizon 1 (Now — Phase 2/3)
Junction contains static 1–3 suggested follow-up zip codes with rationale, authored during card generation. These are the architect's recommendations baked into the master card. This is what exists today.

### Horizon 2 (Phase 5/6 — HTML + User Accounts)
Junction renders static suggestions as tappable zip code links. Selecting one queues it into the user's Almanac — a personal workout queue. The Almanac is an ordered list, not a calendar. The user decides when. The system holds what.

### Horizon 3 (Future — RAG + Community)
Three data sources feed the Junction: the master suggestion (architect's original, never removed), the community layer (people who completed this zip leave structured feedback and vote on follow-up zip codes), and personal history (RAG-powered recommendations based on the user's own patterns).

## Data Architecture

- The zip code is the universal key. Every community board, vote, almanac entry, and usage log keys to the 4-emoji zip code.
- User data never touches master files. Community data and user almanacs live in their own layers.
- The Almanac is a queue, not a calendar. No scheduling, no time slots. Just an ordered list of what's next.
- Junction votes are scoped to the source zip code. Each zip accumulates its own outbound recommendation graph.

## Community Board Concept

Each zip code gets a public record — more like a building logbook than a forum. Users who complete a zip can leave: modifications and why, junction follow-up suggestions with votes, difficulty ratings, equipment notes, and general notes. All tagged with user history context (completion count, recency, logged weights). Experienced users' recommendations carry visible credibility.

## Open Questions

- Does the community layer require user accounts, or can it start anonymous?
- Should Junction votes be weighted by completion count?
- Does the Almanac queue have a max depth?
- Should community boards be per-zip (1,680 boards) or per-deck (42 boards)?
