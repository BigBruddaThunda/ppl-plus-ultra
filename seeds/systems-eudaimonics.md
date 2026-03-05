---
planted: 2026-03-05
status: SEED
phase-relevance: Phase 2 (design constraint), Phase 4-7 (implementation constraint), Phase 7+ (measurement framework)
blocks: nothing — this is a constraint document, not a deliverable
depends-on:
  - seeds/platform-architecture-v2.md
  - seeds/data-ethics-architecture.md
  - seeds/stripe-integration-pipeline.md
  - seeds/operis-architecture.md
  - seeds/scl-envelope-architecture.md
  - seeds/almanac-room-bloom.md
  - middle-math/weights/weight-system-spec.md
  - middle-math/user-context/
  - scl-deep/publication-standard.md
  - scl-deep/vocabulary-standard.md
connects-to:
  - seeds/experience-layer-blueprint.md
  - seeds/operis-sandbox-structure.md
  - seeds/operis-color-posture.md
  - seeds/operis-educational-layer.md
  - seeds/automotive-layer-architecture.md
  - seeds/regional-filter-architecture.md
  - seeds/exercise-superscript.md
  - middle-math/rendering/operis-weight-derivation.md
  - middle-math/user-context/bloom-engine-spec.md (planned, CX-24)
  - middle-math/user-context/vote-weight-integration.md (planned, CX-25)
  - middle-math/user-context/superscript-subscript-spec.md (planned, CX-27)
  - seeds/codex-container-directory-v3.md
supersedes: nothing (first specification of this concept)
---

# PPL± Systems Eudaimonics — The Economic Philosophy of a Training System

🔵⚪ — structured + mindful

## One Sentence

PPL± measures its economic health by whether the system flourishes when its users flourish, and it encodes this alignment into every tier gate, production cycle, retention mechanism, and cost structure so the two cannot diverge.

## What Eudaimonics Means Here

Eudaimonia is Aristotle's term for human flourishing — not happiness as a feeling but the sustained activity of living well according to one's capacities. It is a practice, not a peak state. It is a long arc, not a moment. Training is one of its purest expressions: the daily discipline of showing up, doing the work, recovering, and returning slightly more capable than before.

Eudaimonics is the systems economics that follows from this. Where conventional SaaS economics optimizes for engagement (time on app, session frequency, notification response rate), Eudaimonic economics optimizes for the convergence of system health and user health. The system does not get healthier when the user gets more addicted. The system gets healthier when the user gets stronger, more consistent, more autonomous, and more knowledgeable — because that user produces cleaner data, retains longer through genuine value, and requires less artificial incentive to return.

This is not idealism. It is an architectural constraint that eliminates specific revenue strategies, mandates specific cost structures, and produces specific measurable outcomes. Every clause in this document has implementation consequences.

## The Three Properties of Eudaimonic Economics

### Property 1 — Value Accrues Through Use, Not Through Withholding

Most subscription products gate features to manufacture upgrade pressure. The user hits a wall. The wall says "pay to continue." The value proposition is removal of friction.

PPL± inverts this. The free tier gives the user the complete Operis daily, the full 1,680-room card library (read-only), the navigation graph, and the Operis audio via the automotive layer. Nothing in the content layer is withheld. The user can read every workout, browse every deck, follow every Junction recommendation, and listen to Wilson read every edition — for free, forever.

What the paid tiers add is personal context. Tier 1 ($10/month) adds: the superscript weight suggestion (computed from the user's 1RM history and today's Order load ceiling), the subscript recency marker (days since last performed), room bloom state (personal visit history and depth tracking), saved rooms, workout logging, and personal exercise history. Tier 2 ($25-30/month) adds: coaching features on the community floor, advanced rotation customization, and Wilson's personalized Note.

The thing being sold is not content access. It is the system's accumulated knowledge of the user — the personal context layer that makes the content more precise over time. A new Tier 1 subscriber on day one gets modest value from the superscript (limited history to compute from). The same subscriber at month six gets high-precision weight suggestions because the system has six months of logged sets. At month twelve, the system knows their strength curve across all five Types, their preferred Colors, their bloom depth across dozens of rooms, and their seasonal performance patterns.

This is earned retention. The longer the user trains with the system, the more valuable the system becomes to them — not because they are locked in by sunk cost, but because the system genuinely knows them better. The cost of leaving is the cost of rebuilding that knowledge somewhere else, which is a real cost, not an artificial one. The user's data is fully exportable (see seeds/data-ethics-architecture.md). They can leave with everything. The retention is earned, not manufactured.

Implementation constraint: no feature in the content layer (cards, Operis editions, navigation graph, card library browsing, automotive audio) may be gated behind a paywall. The paywall gates personal context, not content. Any future feature proposal that gates content must be rejected or restructured to gate the personalization layer instead.

### Property 2 — System Health and User Health Are the Same Measurement

In advertising-driven fitness apps, the ideal user opens the app 47 times a day, watches ads between sets, shares achievements to social media for viral growth, and maintains a streak that creates anxiety when broken. System health (engagement, ad impressions, viral coefficient) and user health (training consistency, progressive overload, recovery) are decoupled. The system can thrive while the user stagnates or burns out.

PPL± cannot have this decoupling because of how its economics are structured. The system's revenue comes from subscriptions. Subscriptions retain when users get genuine value. Users get genuine value when they train consistently (3-5 sessions/week), navigate intelligently between zip codes (using Junction and the rotation engine), see their bloom levels rise across rooms (evidence of depth), and occasionally read the Operis (staying connected to the publication rhythm). That user profile — consistent, intentional, deepening — is simultaneously the ideal training profile and the ideal subscription profile.

A user who trains obsessively (7+ days/week, no rest, ignoring Restoration orders) generates noisy data, risks injury, and eventually churns from burnout. That user is bad for the system and bad for themselves. The system should gently redirect them through the rotation engine (which naturally schedules Restoration and Balance orders) and the Junction recommendations (which suggest recovery zips after high-CNS sessions). The system's self-interest and the user's self-interest are identical: sustainable training frequency, appropriate order variation, and progressive depth.

A user who never trains but keeps their subscription is economically harmless but eudaimonically empty. The system should not optimize for passive subscribers. The Operis serves this function — it is a daily touchpoint that invites action without demanding it. The automotive layer extends this invitation into the commute. The bloom system makes visible what the user has built and what rooms are waiting. These are invitations, not guilt mechanisms. The vocabulary standard (scl-deep/vocabulary-standard.md) prohibits streak language, urgency language, and loss-aversion framing.

Implementation constraint: no notification, prompt, or UI element may use streak mechanics, loss-aversion framing, or guilt language. The system invites. It does not pressure. The rotation engine and Junction recommendations are the system's voice — they suggest what comes next based on training logic, not engagement logic. The Operis is published on its rhythm regardless of whether any individual user reads it.

### Property 3 — The Economics Must Work at Every Scale Simultaneously

A system that requires venture-scale growth to survive is not Eudaimonic because it borrows against a future that may not arrive. The economic model must be solvent at three scales: building (now), publishing (Operis-active), and production (users). If any scale requires the next scale to subsidize it, the system is structurally fragile.

## Three-Scale Economics

### Scale 1 — Building (Phase 2-3, Current)

Primary input: Jake's time + AI compute costs (Claude Code sessions, Codex container execution, temp architect sessions).

Primary output: the 1,680-card library, the architecture (42+ seed documents, middle-math specifications, scl-deep reference layer), the validation infrastructure (scripts, linters, audit pipeline), and the Codex container execution plan.

The economic question at this scale: what is the minimum viable rate of production that keeps the project alive without burning out the builder or accumulating quality debt?

The answer is in the infrastructure-before-content principle. Every validation script, every deck identity document, every linting rule reduces the per-card cost of quality for every subsequent card. The 32 Codex containers (CX-00A through CX-31) are sequenced to build the computation layer (weight vectors, exercise selection, navigation graph) that eventually automates the deterministic portions of card generation. The investment in infrastructure is not a delay — it is the mechanism that makes the remaining 1,600 cards economically feasible.

The Operis generation pressure mechanism (13 rooms/day forcing card generation) ties production to editorial cadence rather than arbitrary sprint targets. The system produces cards because today's edition needs them, not because a backlog demands velocity. This is sustainable production — the rhythm of a daily publication, not the sprint of a startup.

Cost structure at this scale: AI compute is the primary variable cost. It is spent on quality infrastructure (scripts, specs, validators) and content generation (cards, Operis editions). The ratio should favor infrastructure early and shift toward content as the infrastructure matures. The current 80/1,680 card count with a mature validation pipeline and 32 scoped Codex containers is the right ratio for this phase.

### Scale 2 — Publishing (Phase 4-5, Operis Active)

Primary input: AI generation costs for the 4-prompt Operis pipeline (Researcher, Content Architect, Editor, Builder), hosting costs (Vercel, Supabase free tiers), and Jake's editorial oversight.

Primary output: daily Operis editions, continued card generation (via the construction vehicle pipeline), historical events database growth, and cosmogram substrate enrichment.

The economic question at this scale: does the Operis create more value than it costs, even if no one subscribes?

The answer must be yes. The Operis is the engine that builds the library. Every edition forces up to 13 card generations. Over 40 days, one deck's 40 cards can be fully generated by Operis pressure alone. Over 229 days at 7 new cards/day average, the remaining 1,600 rooms complete. The Operis is not marketing content that drives conversion. It is the production mechanism that builds the asset base. The fact that it is also the primary free-tier touchpoint and conversion surface is a structural bonus.

This is the almanac model. The Old Farmer's Almanac (1792-present) works because the act of publishing is itself valuable — it forces the publisher to observe, research, compile, and produce on a rhythm. The subscription revenue sustains the operation, but the operation has intrinsic value independent of the revenue. Every Operis edition leaves the system richer: more cards generated, more historical events recorded, more cosmogram substrate populated, more envelopes stamped for future retrieval. The cost of production is simultaneously investment in the asset base. Production is self-enriching.

Cost structure at this scale: the 4-prompt AI pipeline cost per edition is the primary variable. Hosting is near-zero on free tiers during early publishing. Jake's editorial time is the scarcest resource — the pipeline is designed to minimize editorial overhead by automating the deterministic portions (rotation engine output, Color sibling generation, department activation matrix) and concentrating editorial judgment on the 5 Content Rooms and the prose.

Break-even consideration: if the Operis costs X per edition in AI compute, and each edition generates 7 new cards that are permanent assets, then the per-card cost of Operis-driven generation is X/7. This should be compared against the per-card cost of dedicated Claude Code generation sessions. If the Operis pathway is cost-competitive with direct generation while also producing a daily publication, it is the dominant strategy.

### Scale 3 — Production (Phase 6-7, Users)

Primary input: infrastructure costs (Vercel, Supabase, Stripe transaction fees), continued AI costs for Operis and cosmogram production, and operational overhead.

Primary output: subscription revenue (Tier 1 at $10/month, Tier 2 at $25-30/month), a growing envelope corpus, community content, and almanac depth.

The economic question at this scale: what is the relationship between user longevity and unit economics?

In most SaaS, long-tenured users are either the most profitable (they keep paying without support costs) or the least profitable (they use the most compute and storage). In PPL±, long-tenured users are the most valuable across every dimension. To themselves: they have the deepest bloom state, the most accurate superscript predictions, and the richest training history. To the system: they produce the cleanest data, the most training signal for aggregate patterns, and the most community content (enveloped observations that enrich the almanac). To the business: they have the lowest churn risk because the system's knowledge of them is genuinely useful and non-transferable (even with full data export, the contextual computation requires the PPL± engine).

This creates the eudaimonic virtuous cycle: the system thrives precisely when its users thrive. There is no tension between profit and wellbeing. There is no moment where the business would benefit from the user training more obsessively, engaging more superficially, or becoming dependent rather than autonomous.

Cost structure at this scale: fixed costs (card library, architecture, infrastructure code) amortize across the entire user base. A card generated once serves every user forever. An Operis edition published once is archived and retrievable by envelope for every future user. The envelope corpus appreciates with every addition — nothing goes stale because the retrieval engine surfaces content by condition, not by date. Variable costs (Supabase compute per user, Vercel edge invocations, Stripe's 2.9% + $0.30 per transaction) scale linearly. The crossover point — where subscription revenue exceeds total operating costs — depends on the ratio of Tier 1 to Tier 2 subscribers and the hosting cost at scale.

Rough unit economics: at $10/month Tier 1, Stripe takes ~$0.59, leaving $9.41. Supabase per-user cost at moderate usage is approximately $0.50-1.00/month. Vercel per-user edge compute is approximately $0.10-0.30/month. Net margin per Tier 1 user: approximately $8.00-8.80/month. At Tier 2 ($25/month), net margin per user: approximately $22-24/month. The system becomes self-sustaining for infrastructure costs at a relatively low subscriber count. The primary ongoing cost is AI compute for Operis and cosmogram production, which amortizes across all users and decreases per-user as the subscriber base grows.

## The Convergence Metric

A single composite measurement that captures whether system health and user health are moving together.

Eudaimonic Health Index (EHI) = Training Consistency × Library Depth × Earned Retention

Component definitions:

Training Consistency: the percentage of active subscribers who logged at least 3 sessions in the trailing 14 days. This measures whether users are actually training, not just subscribed. A healthy system has high training consistency. A system optimizing for passive subscribers would have low training consistency and wouldn't care.

Library Depth: the percentage of the 1,680 card library at CANONICAL status multiplied by the average bloom level across active rooms (rooms with at least one visit in 90 days). This measures whether the content is being built and used. A healthy system has a growing library that users actually visit. An empty library or an unvisited one indicates a production or relevance problem.

Earned Retention: the 90-day rolling retention rate for subscribers who have logged at least 10 sessions. This filters out trial subscribers and measures whether users who actually use the system stay. Retention driven by genuine value (the system knows them, the superscript is accurate, their bloom is deep) is earned. Retention driven by guilt, sunk cost, or forgetting to cancel is not — but it also would not correlate with 10+ logged sessions, so the filter distinguishes them.

When all three components are rising, the system is eudaimonically healthy — users are training, the library is growing and being used, and people who actually use the system stay. When any component falls, something is misaligned: either users aren't training (the system isn't motivating action through invitation), or the library isn't growing (production has stalled), or users are leaving despite using the system (the value proposition isn't landing).

The EHI is not a vanity metric. It is an operational diagnostic. Each component points to a specific system layer when it falls: Training Consistency → rotation engine and Operis invitation quality. Library Depth → card generation velocity and room navigation quality. Earned Retention → personal context layer value and subscription tier design.

## Longevity Constraints — What the System Refuses

These are economic constraints, not ethical aspirations. Each one eliminates a revenue strategy that would decouple system health from user health.

No data sales. User training data, exercise preferences, bloom state, and community content are never sold, shared with third parties, or used for advertising targeting. The business model is subscriptions. The user is the customer. (See seeds/data-ethics-architecture.md for the full architecture.)

No gamified streaks. Streak mechanics create anxiety about breaking the streak, which pressures users to train when they should rest. The rotation engine schedules Restoration and Balance orders. A streak mechanic would penalize users for following the system's own recovery recommendations. The system cannot simultaneously recommend rest and punish the user for resting.

No manufactured urgency. No "limited time offers," no "your streak is at risk," no "X users just completed this workout." The Operis publishes on its rhythm. The rooms are always there. The system is a library, not an auction house.

No recovery content behind paywalls. Restoration order cards (🖼), Balance order cards (⚖), and all Mindful color variants (⚪) are free-tier accessible in read-only form like all other cards. Gating recovery behind payment would create a perverse incentive: the system benefits when users need recovery they can't access. This is the clearest test of Eudaimonic alignment — if the business would benefit from the user's suffering, the alignment is broken.

No session-length optimization. The system does not benefit from longer sessions. A Performance order workout (🏟) is 3-4 blocks: test, record, leave. The system should not add filler to extend the session. Time spent in the app is not a KPI. Effective training is.

No dark patterns in cancellation. Full data export available at any time (JSON). Account deletion is a single action that cascades through all tables. No "are you sure?" guilt screens. No retention offers triggered by cancellation intent. If the user wants to leave, the system makes it clean. Earned retention means the user stays because the system is valuable, not because leaving is difficult.

No engagement notifications. The system does not send "you haven't trained in 3 days" or "your friends just worked out" notifications. The Operis publishes daily — that is the system's invitation. Push notifications, if implemented, are limited to: Operis publication (opt-in), and functional alerts (subscription renewal, data export ready). The system does not chase the user.

## The Almanac Economics — Why Nothing Goes Stale

The envelope architecture (seeds/scl-envelope-architecture.md) has a direct economic consequence: every piece of content ever created remains economically active forever.

In conventional content businesses, content depreciates. A blog post published today has peak traffic this week and decays toward zero. A social media post has a half-life measured in hours. Content businesses must constantly produce new content to replace the declining value of old content. This is the content treadmill — production costs are ongoing and the asset base does not compound.

In PPL±, the envelope system makes content retrieval condition-based, not date-based. A fishing observation from March 2027 resurfaces in March 2028 — not because the date matches, but because the SCL conditions match (seasonal position, lunar phase, daylight hours, regional context). A planting guide from year one appears alongside year two and year three guides when the conditions align, creating layered almanac depth. A workout card generated today is retrieved by the same mechanism — when a user's live vector is similar to the card's envelope, the card surfaces.

This means the content asset base compounds. Every Operis edition, every community pin, every user observation, every cosmogram entry is permanently retrievable. The library does not decay. The almanac grows richer every year. The retrieval engine serves more relevant content to each user as the corpus deepens. The marginal cost of serving old content is near-zero (it is already stored and indexed). The marginal value of old content increases over time (more data points at similar conditions create richer pattern visibility).

The economic implication: PPL± has decreasing marginal cost of content per user over time. Early users subsidize library building through their subscriptions. Later users inherit a richer library at the same subscription price. This is the economics of a public library, not a content mill. The investment compounds. The returns increase. The system gets cheaper to operate per user as it ages, not more expensive.

## Cost Constraints by Phase

### Phase 2-3 (Current — Building)

Acceptable costs: Claude Code sessions for card generation and infrastructure. Codex container execution for automation. Temp architect sessions for research and planning. GitHub free tier for hosting, Actions, and Pages.

Unacceptable costs: paid hosting before functional prototype exists. Database provisioning before schema is materialized. Domain registration before content is ready. Any external service that creates recurring cost before revenue exists.

### Phase 4-5 (Publishing — Operis Active)

Acceptable costs: Vercel free tier for Next.js hosting. Supabase free tier for database and auth. AI compute for Operis pipeline (4 prompts per edition). Domain registration (one-time + annual).

Unacceptable costs: paid advertising. Paid growth hacking. Analytics services. Any third-party service that tracks users or sells data.

### Phase 6-7 (Production — Users)

Acceptable costs: Vercel paid tier when traffic requires it. Supabase paid tier when storage or compute requires it. Stripe transaction fees (unavoidable cost of payment processing). AI compute for continued Operis production and cosmogram research. Customer support tooling.

Unacceptable costs: engagement consultants. A/B testing frameworks optimizing for session length. Retention dark patterns. Any cost whose purpose is to increase engagement rather than increase training quality.

## How This Document Is Read

This seed is a design constraint, not a deliverable. It does not produce artifacts. It constrains how artifacts are designed.

Any session that touches the following systems should read this document:

- Stripe integration (seeds/stripe-integration-pipeline.md) — tier gating decisions, what is free vs paid
- Bloom engine (CX-24) — bloom as genuine depth signal, not gamification
- Vote weight integration (CX-25) — votes as relevance refinement, not popularity ranking
- Superscript/subscript system (CX-27) — Tier 1 value proposition, earned retention through precision
- Floor routing (CX-22) — tier gating at the floor level, content-free paywall-free principle
- Operis production pipeline — self-enriching production, almanac economics
- Notification design — invitation, not pressure
- Onboarding design — newspaper → room → building → navigator progression, not trial-to-conversion funnel
- Any UI/UX work — vocabulary standard compliance, no streak/urgency/loss-aversion patterns

The document is referenced in CLAUDE.md as a design constraint alongside seeds/data-ethics-architecture.md. Both documents share the same enforcement mechanism: they eliminate options rather than prescribing solutions. The system designer's job is to find solutions that satisfy the constraints. If no solution satisfies the constraints, the feature is wrong, not the constraint.

## Relationship to Existing Architecture

This document does not replace or modify any existing seed. It adds a philosophical and economic foundation underneath them.

seeds/data-ethics-architecture.md defines what the system will not do with data. This document defines why — and extends the principle beyond data to encompass engagement, retention, production, and pricing.

seeds/platform-architecture-v2.md defines the business model ($10/$25-30 tiers). This document defines the economic philosophy that makes those tiers legitimate — value accrues through use, personal context is the product, content is free.

seeds/stripe-integration-pipeline.md defines the payment mechanics. This document constrains what is gated — personal context, not content.

seeds/operis-architecture.md defines the publication system. This document frames the Operis as a self-enriching production engine whose value exceeds its cost even at zero subscribers.

seeds/scl-envelope-architecture.md defines the content retrieval system. This document identifies the economic consequence — the almanac economics where nothing depreciates and the asset base compounds.

seeds/almanac-room-bloom.md defines the bloom mechanic. This document constrains bloom to be a genuine depth marker rather than a gamification lever.

middle-math/user-context/ defines the personal context layer. This document identifies that layer as the actual product being sold.

## Open Questions

- What is the minimum subscriber count for self-sustaining Operis production? This requires: estimated AI cost per edition, estimated hosting cost, and the Tier 1/Tier 2 subscriber ratio assumption. Current lean: model this during CX-08 (SQL schema materialization) when the database cost structure becomes concrete.

- Should the EHI be computed and displayed internally (team dashboard) or also exposed to users? Current lean: internal only. Users see their own bloom and training history. The system-level health metric is an operational tool, not a user-facing feature.

- How does the Eudaimonic model handle a user who is clearly undertrained (1 session/month) but maintains their subscription? The system should not guilt them, but the rotation engine could gently surface lower-barrier entries (🟢 Bodyweight, 🐂 Foundation, ⚪ Mindful) in their Operis and Junction recommendations. Invitation without pressure. The subscription is their choice. The system's job is to make the next session as accessible as possible.

- At what scale does the self-enriching production model break? If the system grows to millions of users, the community content volume may exceed useful retrieval density. The envelope similarity threshold handles this (only condition-matched content surfaces), but the raw storage and indexing cost may require content archival policies. Current lean: defer this question until the envelope corpus exceeds 100,000 items. The problem is a good one to have.

🧮
