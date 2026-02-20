---
source: PPL± SCL Deep Specification — Junction Web v1.0
date: 2026-02-20
status: WORKING DRAFT
integration-target: cards/ (🚂 Junction blocks), seeds/default-rotation-engine.md
notes: |
  The 🚂 Junction block at the end of every workout contains follow-up zip code
  suggestions. This document specifies the logic underlying valid Junction links —
  what makes one zip code a valid next session from another, how the Junction Web
  forms a navigable graph across all 1,680 addresses, and how this becomes the seed
  of a programming and recommendation layer.
---

# JUNCTION WEB
## The Connection Graph Behind 🚂 Junction

Every workout ends with a 🚂 Junction block. The block does two things:
1. Provides a logging space — date, weights, splits, personal records, technical notes
2. Suggests 1–3 follow-up zip codes with brief rationale

The follow-up suggestions are not arbitrary. They form a directed graph — a web of valid transitions between workout addresses. This document specifies the rules for valid Junction links and the structure of the Junction Web as a programmatic layer.

---

## SECTION 1: WHAT MAKES A VALID JUNCTION LINK

A valid Junction link from zip code A to zip code B satisfies at least one of these relationship types:

### Relationship 1: Same Deck, Different Color (Intra-Deck Progression)

A = ⛽🏛🪡🔵 → B = ⛽🏛🪡🟣 (more precision, longer rest)
A = ⛽🏛🪡🔵 → B = ⛽🏛🪡🔴 (more intensity, reduced rest)
A = ⛽🏛🪡🔵 → B = ⛽🏛🪡⚫ (if form degraded, return to teaching format)

The Order, Axis, and Type are fixed. The Color shifts. This is a direct format progression — same work, different approach to it.

**Use this link when:** The session quality, the user's readiness, or the seasonal context calls for a different format on the same fundamental work.

### Relationship 2: Same Type, Adjacent Order (Inter-Order Progression)

A = ⛽🏛🪡🔵 → B = 🏟🏛🪡🔵 (test the strength just built)
A = 🦋🏛🛒🔴 → B = ⛽🏛🛒🟣 (transition from hypertrophy volume to strength precision)
A = 🐂🏛🍗⚫ → B = ⛽🏛🍗🔵 (pattern is owned, ready to load it)

The Type, Axis, and Color lock. The Order shifts. This is a training phase progression — same muscle group, different training phase.

**Use this link when:** The current Order has accomplished its purpose and the next phase is appropriate.

### Relationship 3: Same Order, Complementary Type (Agonist-Antagonist Pairing)

A = ⛽🏛🛒🔵 → B = ⛽🏛🪡🔵 (push → pull, same parameters)
A = ⛽🏛🍗🟣 → B = ⛽🏛🛒🟣 (lower → upper, same precision format)
A = 🦋🌹🛒🔴 → B = 🦋🌹🪡🔴 (hypertrophy push → hypertrophy pull, same aesthetic lens)

The Order, Axis, and Color lock. The Type shifts to its complement or balance pair.

**Use this link when:** Movement balance demands addressing the opposite pattern within the same training context.

### Relationship 4: Diagnostic Regression (Quality-Gate Link)

A = ⛽🏛🪡🔵 → B = 🐂🏛🪡⚫ (form degraded → return to Foundation Teaching)
A = ⛽🏛➖🟣 → B = ⛽🏛➖⚫ (rowing mechanics broke down → go to the teaching session)
A = 🦋🌹🛒🔴 → B = 🐂🌹🛒⚫ (isolation form collapsed under volume → return to pattern learning)

These are conditional links — "if [quality condition], go here." The condition is specified in the link's rationale line.

**Use this link when:** The session reveals a pattern quality gap that must be addressed before progressing. These are the most valuable Junction links because they prevent compounding errors.

**Diagnostic regression always goes toward lower Order + Teaching Color.** Never diagnose forward.

### Relationship 5: Operator-Based Contextual Link (Seasonal or Tonal Shift)

A = ⛽🏛🪡🟣 → B = ⛽🏛🪡⚪ (July Intense session → August Mindful variant to layer in recovery)
A = 🦋🏛🛒🔴 → B = 🦋🏛🛒🟡 (shift format for seasonal variety without changing Type or Order)

These links shift the Color to match a tonal or seasonal context without altering the training parameters meaningfully. They are the lightest Junction links — format pivots, not progression pivots.

**Use this link when:** The training phase is stable but the format needs to breathe.

---

## SECTION 2: JUNCTION LINK FORMATTING

In workout markdown, Junction links appear in the 🚂 block as:

```
Next →
- [zip] — [one-line reason]
- [zip] — [one-line reason]
- [zip] — [one-line reason]
```

Maximum 3 links per Junction block. Minimum 1.

**Writing the rationale line:**
- State the relationship type implicitly, not explicitly. Never write "Relationship 1:" or "Intra-deck progression."
- Write what changes and why it matters in training terms.
- Good: "same erg anchor, higher volume: 5 × 500m with 3 min rest"
- Good: "return here if stroke mechanics degraded in the final interval"
- Good: "test the strength you just built — one attempt, full recovery, log the number"
- Bad: "alternative workout option"
- Bad: "more challenging version"

---

## SECTION 3: THE JUNCTION WEB AS A DIRECTED GRAPH

The 1,680 zip codes form a directed graph. Each node has:
- **Out-edges:** 1–3 Junction links specified in the workout card (where this workout sends you)
- **In-edges:** all Junction links from other cards that point here (what sends you to this workout)

The graph is not fully connected. The constraints in Section 1 determine which edges are valid. Not every zip code connects to every other zip code.

### Node Connectivity Patterns

**High in-degree nodes (hubs):** Foundation Teaching addresses (🐂🏛[Type]⚫, 🐂🔨[Type]⚫, etc.) are natural hubs. Diagnostic regression links from across every deck point toward Foundation Teaching. Every beginner-state link and every quality-failure link converges here.

**Low in-degree nodes (terminals):** Performance addresses (🏟[Axis][Type][Color]) have few valid in-edges — you only test what you've built. A 🏟 node receives traffic from ⛽ nodes when the strength is ready to be tested. It sends traffic back toward ⛽ for the next training block.

**High out-degree nodes (dispatchers):** Full Body addresses (🌾[Axis][Type][Color]) function as dispatchers — they link outward to Type-specific nodes naturally. A 🌾 session that integrates squat and press can validly link to either the next 🍗 Legs or 🛒 Push session without losing coherence.

**Bridge nodes:** Balance addresses (⚖[Axis][Type][Color]) bridge corrective work back into progression. ⚖🏛🪡⚫ (Balance Basics Pull Teaching) sits between a failed form audit and the return to ⛽ loading.

---

## SECTION 4: THE JUNCTION WEB AS A PROGRAMMING LAYER

The Junction Web is the seed of two future features:

### 4.1 Session Recommendation Engine

When a user completes a session and logs it through the 🚂 Junction block, the system can surface the valid next-session options. Recommendation weights personalize based on:
- **Training history:** which Colors and Orders has this user used recently? What's underrepresented?
- **Seasonal density modifiers:** which Colors are in season this month?
- **Order rotation:** what does the default rotation engine prescribe for tomorrow?
- **Quality flags:** did the user log a technical degradation note? → Weight toward the diagnostic regression link.
- **Rest gap:** how many days since last session? → Longer rest gaps weight toward Foundation or Restoration.

### 4.2 Auto-Programming Layer

For users who want a generated multi-week program (not just a daily zip code), the Junction Web provides the edge set for a training graph. A basic algorithm:

1. Start from the default rotation zip code for Day 1
2. Follow Junction links forward for N days
3. Weight Relationship 1 (same-deck Color progression) for week-to-week consistency
4. Insert Relationship 3 (complementary Type) links every 2–3 sessions for balance
5. Insert diagnostic regression links after any logged quality degradation
6. Apply seasonal density weighting on Color links

The Junction Web is not a replacement for programming intelligence — it is the infrastructure that makes intelligent programming possible. The web of valid transitions is the constraint layer. The intelligence lives in the weighting algorithm.

---

## SECTION 5: JUNCTION WEB CLUSTER STRUCTURE

The 1,680 nodes cluster naturally by Order. Cross-cluster traffic follows predictable patterns:

| Cluster | Nodes | Primary in-traffic | Primary out-traffic |
|---------|-------|-------------------|---------------------|
| 🐂 Foundation | 240 | Diagnostic regression from all clusters | 🐂→⛽ (pattern → load) |
| ⛽ Strength | 240 | 🐂 progression, 🦋→⛽ phase shift | ⛽→🏟 (build → test), ⛽→⚖ (audit) |
| 🦋 Hypertrophy | 240 | Internal Color cycling | 🦋→⛽ (volume → intensity transition) |
| 🏟 Performance | 240 | ⛽ progression | 🏟→⛽ (test → rebuild) |
| 🌾 Full Body | 240 | Cross-Type dispatching | Any Type-specific node |
| ⚖ Balance | 240 | Audit traffic from ⛽ and 🦋 | ⚖→⛽ (corrected → reload) |
| 🖼 Restoration | 240 | Recovery traffic from any cluster | Any cluster (recovery resets → any direction) |

---

## SECTION 6: WHAT MAKES A JUNCTION LINK INVALID

A Junction link is invalid if:

- It links to a zip code that violates Order constraints at the destination (e.g., linking from a ⛽ session to a 🏟 session when the Type has not been developed at ⛽ level)
- It links forward past a required diagnostic step (e.g., linking from a session with logged form failure directly to a higher-intensity Color without offering the Teaching regression)
- The rationale line is absent or uninformative
- It links to a GOLD-gated zip code from a non-GOLD context without qualification

Invalid links are not catastrophic — they are just suboptimal. The Junction block is a suggestion, not a mandate. But invalid links reduce the value of the web.

---

## OPEN QUESTIONS

- Should the Junction Web be rendered as an explicit graph visualization in the app? A "where can I go from here" navigable network would make the web legible to users.
- Do Junction links need formal weighting beyond the 3-option manual suggestion? Automated weighting requires a recommendation model input layer.
- How does the Junction Web interact with user history? If a user has never visited a particular node, the system might deprioritize recommending it until they've explored nearby territory.
- Are there explicit prohibition rules needed? Currently the rules define what IS valid. A prohibition list (e.g., "do not link from 🏟 Performance directly to 🖼 Restoration without an intermediate session") might sharpen programming quality.
- Should the 🚂 Junction block log feed into a separate data layer (junction-history) that tracks which links users actually follow? Aggregated junction-following behavior would be the most reliable signal for improving link recommendations.
