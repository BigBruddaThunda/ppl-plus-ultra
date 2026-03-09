---
planted: 2026-03-09
status: SEED — DLC
phase-relevance: Phase 7+ (Community, Competition)
blocks: nothing currently — competitive layer
depends-on: scl-directory.md, seeds/heros-almanac-v8-architecture.md, seeds/abacus-architecture.md
connects-to: seeds/digital-city-architecture.md, seeds/experience-layer-blueprint.md
legacy-sources: THE HERO'S ALMANAC v7.0.pdf
---

# The Cathedral Cup — Competitive Layer Architecture

## Thesis

Community-wide competitions at specific zip-code addresses. NFL-combine-style benchmark events mapped to the 🏟 Performance Order. Leaderboards living at zip-code community floors. House-based team competitions where the 12 operator guilds (see `seeds/heros-almanac-v8-architecture.md`, Section 4) compete as teams.

The Cathedral Cup is the competitive expression of the city. The buildings (Orders) host events. The floors (Axes) determine the character of the competition. The rooms (zip codes) are the arenas. The Houses (operators) are the teams.

## Structural Concepts

- **Benchmark events** live at 🏟 Performance zip codes. Each of the 240 🏟 rooms (🏟 × 6 Axes × 5 Types × 8 Colors) is a potential competition venue with specific rules derived from the zip code's constraints.

- **House competitions** aggregate individual performances by operator guild. A user's contribution to their House depends on their personal vector's cosine similarity to the event's zip-code vector — higher affinity = higher weight on the leaderboard. You contribute most to events that match your identity.

- **Vitruvian Games** — a seasonal competition format (working name, needs publication standard proofing) that rotates through Orders and Axes on a calendar. The competition calendar aligns with the Operis rotation but is independent of it.

- **Leaderboards** are zip-code-specific. Every room can have a leaderboard. 🏟 rooms have formal competition leaderboards. Other rooms have informal "most active" or "most consistent" recognition, emergent from the community role system (Section 7 of the Almanac seed).

## Open Questions

- **Fairness:** How does the system handle different body weights, training ages, and equipment access? Relative scoring (Wilks, DOTS, allometric) for strength events? Age-graded scoring for conditioning events?

- **Frequency:** How often do Cathedral Cup events run? Continuous rolling leaderboards? Seasonal resets? Annual championships?

- **Prizes and incentives:** In-app recognition only? Subscription tier benefits? Physical prizes? The business model (`seeds/platform-architecture-v2.md`) needs to account for competition costs.

- **Anti-cheating:** Self-reported data means leaderboards are trust-based. Community moderation? Video verification for top positions? Or accept that the leaderboard is aspirational, not certified?

- **Scale:** Does this work with 100 users? 10,000? 1,000,000? House competition requires enough users per House to be meaningful. Minimum viable community size for competitive features needs estimation.

---

🧮
