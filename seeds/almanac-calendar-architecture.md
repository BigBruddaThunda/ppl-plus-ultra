---
title: Almanac Calendar Architecture
status: SEED
planted: 2026-03-08
category: experience-layer
depends-on: seeds/abacus-architecture.md, seeds/elevator-architecture.md, seeds/operis-architecture.md
connects-to: middle-math/rotation/reverse-weight-resolution.md, seeds/experience-layer-blueprint.md
---

# Almanac Calendar — The Temporitas Floor as Daily Driver

## Concept

The ⌛ Temporitas floor, when viewed from the user's home/dashboard level (not inside a specific zip code), becomes their personal calendar. A daily planner that integrates training, editorial, community, and natural-world context through the same SCL lens that organizes their workouts.

This makes Ppl± the daily organizational tool on the user's phone — not just the workout app they open when it's time to train. The calendar becomes the surface that ties everything together.

## What Already Exists

The system already generates most of the calendar's content:

- **Training calendar** — The abacus rotation produces a deterministic training schedule. Which workout, which day, based on selected programs and the 3-gear rotation engine (Order by weekday, Type by rolling 5-day calendar, Axis by monthly operator).
- **Operis publication calendar** — The daily Operis follows a deterministic editorial schedule. One edition per day, content driven by Order of the Day.
- **Community events** — Events at specific zip codes already have timestamps.
- **Envelope context** — Seasonal and astronomical context per day (daylight hours, lunar phase, regional events).

## What's Missing

The **personal layer** — user-created calendar entries, reminders, notes, timestamps that live alongside the system-generated calendar. And the **rendering** — presenting all of this as a cohesive daily/weekly/monthly view that the user interacts with as their primary calendar.

## Data Model Extension

Extend `user_context` with calendar entries:

```
calendar_entries:
  - id: uuid
  - user_id: uuid
  - date: date
  - time: time (nullable — some entries are day-level)
  - title: text
  - body: text (nullable)
  - zip_code: char(4) (nullable — entry can be tied to a specific room)
  - source: enum (user | abacus | operis | community | integration)
  - integration_ref: jsonb (nullable — external calendar ID, Notion page ID, etc.)
  - color: enum (the 8 SCL colors — user assigns cognitive posture to their entry)
  - created_at: timestamptz
  - updated_at: timestamptz
```

## Integration Layer

### MVP Integrations (Phase 6+)

- **CalDAV / iCal** — Two-way sync with Apple Calendar, Google Calendar. Training schedule exports as calendar events. External events import as Temporitas entries.
- **Notion** — Page linking. A Ppl± calendar entry can reference a Notion page. The Notion page can embed a zip code room via iframe or API.
- **Google Drive** — Document linking to training logs, program notes.

### MVP+1 Integrations

- **Smart fitness tools** — Apple Watch, Fitbit, Whoop, Oura Ring. Heart rate, sleep, recovery scores feed into the envelope system. The rotation engine can adjust tomorrow's zip code based on last night's recovery data.
- **Smart watches** — Workout display on wrist. Current block, current set, timer, rest countdown. Minimal chrome, maximum signal.
- **Fit rings** — Passive recovery data. Morning readiness score adjusts the day's recommended intensity.

### Social & Content Integrations

- **YouTube linking** — Exercise demonstration videos linked to specific exercises in the library. Community members can submit their own form videos at specific zip codes.
- **Social media sharing** — Share a workout card as a screenshot (screenshot mode). Share an Operis excerpt. Share a zip code room as a link.
- **Discord / Twitch** — Community floor integration. Discord channels mapped to specific decks or abaci. Twitch streams from specific zip codes (training sessions).

## MySpace Principle — Zip Code Customization

Each zip code is potentially a user's canvas. The room's visual appearance is driven by the weight vector and CSS custom properties, but users could mod their own rooms:

- Change the gradient
- Adjust the typography
- Add their own background or texture
- Custom color overrides within the 8-color system

This is the MySpace principle: your page is your expression, but within a shared infrastructure. The SCL guarantees structural coherence even when users customize.

### Wilson as AI Design Assistant

Future extension: Wilson (the Ppl± voice) could serve as an AI design assistant for zip customization:

> "Wilson, make this room feel more like a garage gym."
> "Wilson, I want this to look like a boxing ring."
> "Wilson, make this feel calmer — more ⚪ Mindful."

Wilson interprets the request, generates weight vector overrides and CSS custom property adjustments, and applies them. This is RAG + design system — the AI understands the visual vocabulary and can compose within it.

## Relationship to Native Phone Calendar

**Complement, not replace.** The Ppl± calendar does not try to be the user's only calendar. It is the training-and-wellness layer that integrates with their existing calendar infrastructure. Training events sync out to their phone calendar. Personal events from their phone calendar can sync in (with permission) to provide context for training decisions.

The goal is presence in the user's daily view, not displacement of their existing tools.

## Open Questions

1. How deep should integration go? Full two-way CalDAV sync is complex. One-way export (Ppl± → phone calendar) is simpler and may be sufficient for MVP.
2. Should user-created calendar entries have their own notification system, or should notifications route through the native phone OS?
3. How does the calendar interact with the rotation engine? If a user marks a rest day on their calendar, does the rotation engine skip that day and push the schedule forward?
4. Modding scope: can users customize rooms they don't "own" (haven't visited), or only rooms they've trained in? Is there a progression system for unlocking customization?
5. Wilson AI budget: real-time design assistance requires inference. Is this a premium feature? Does it consume a monthly AI budget?

---

🧮
