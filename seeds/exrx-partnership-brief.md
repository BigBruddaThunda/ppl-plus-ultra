# ExRx.net Partnership Brief

Status: SEED
Author: Jake Berry, PPL±
Date: 2026-03-06

---

## Overview

PPL± is a semantic training language and workout generation system producing 1,680 unique workouts across 42 training decks. As of March 2026, the system has 2,085 exercises catalogued in a structured registry (`middle-math/exercise-registry.json`) with globally unique identifiers (EX-0001 through EX-2085), SCL type tags, movement pattern classification, and anatomy data.

Each exercise in the registry has an `external_ref` field reserved for ExRx.net URL mapping. This brief describes the integration architecture and the proposed partnership.

---

## Integration Architecture

Every exercise card in PPL± has an inline knowledge section rendered at workout time. When a user taps an exercise name during a workout session, they see:

1. PPL± coaching cues (setup, execution, common faults)
2. A "Learn More" link — pointing to the exercise's ExRx.net page

The `external_ref` field in the registry holds this link:

```json
{
  "EX-0437": {
    "exrx_url": "https://exrx.net/WeightExercises/GluteMaximus/BBDeadlift",
    "exrx_muscle_page": "https://exrx.net/Muscles/GluteMaximus",
    "video_url": null,
    "research_urls": [],
    "partner_status": "mapped"
  }
}
```

Currently all 2,085 `exrx_url` values are `null`. Populating them is the goal of the partnership.

---

## Traffic Flow Model

```
User opens workout
  → taps exercise name (e.g., "Barbell Deadlift")
    → PPL± coaching panel opens
      → user reads setup/execution cues
        → taps "Learn More at ExRx.net"
          → lands on exrx.net exercise page
```

This is qualified traffic: users in an active workout session, specifically interested in the exercise they just tapped. The intent signal is strong — they are mid-rep, mid-session, at a point of maximum relevance.

PPL± does not scrape or reproduce ExRx content. The link opens ExRx in a new tab.

---

## What PPL± Provides

- **Qualified traffic** from users mid-workout. Not random clicks from search.
- **Exercise-specific routing** — each link targets the correct ExRx exercise page, not the homepage.
- **Subscription user base** — PPL± is a paid subscription service ($10–30/mo). These are serious training users.
- **Attribution** — PPL± can display "Powered by ExRx.net" on exercise knowledge panels for partner exercises.
- **Technical readiness** — the integration dock is built. Mapping populates a JSON file; no further architecture work needed.

---

## What PPL± Requests

**Option A (preferred):** A URL mapping file or database API. For each exercise name or ExRx exercise ID, return the direct exercise page URL. PPL± can map 2,085 exercises in a single batch operation.

**Option B:** Permission to construct URLs using ExRx's existing URL structure. Many ExRx exercise pages follow a pattern (`/WeightExercises/{MuscleGroup}/{EquipmentPrefix}{ExerciseName}`). If the structure is stable and ExRx consents, PPL± can infer most URLs programmatically and verify by HTTP HEAD check.

**Option C:** Selective partnership. Map the top 291 exercises currently in use across 102 generated workout cards. These are the exercises users encounter most frequently. Expand from there.

---

## Technical Readiness

| Component | Status |
|-----------|--------|
| Exercise registry (2,085 EX-IDs) | BUILT — `middle-math/exercise-registry.json` |
| External ref dock (2,085 null entries) | BUILT — `middle-math/exercise-engine/external-refs.json` |
| Knowledge file template | BUILT — `exercise-content/` |
| "Learn More" UI component | PLANNED — Phase 4/5 (HTML layer) |
| URL population script | READY TO BUILD once mapping received |

---

## Contact

Jake Berry — [to be filled in]
PPL± project — https://github.com/[repo]

---

*This is a seed document. It becomes active when Jake promotes it to a direct outreach task.*

🧮
