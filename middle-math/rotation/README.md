# Rotation Engine

The deterministic date → zip code engine. Given a date and a user's Color preference, the system produces a zip code without any additional input.

## The Three Gears

1. **Order by weekday** — Fixed 7-day cycle. Monday = 🐂, Tuesday = ⛽, Wednesday = 🦋, Thursday = 🏟, Friday = 🌾, Saturday = ⚖, Sunday = 🖼.

2. **Type by rolling calendar** — 5-day cycle from January 1, never resetting for the week. Monday may be 🛒, Tuesday 🪡, etc., but the cycle rolls regardless of day-of-week. The coprime relationship between 5 and 7 means the same Order × Type pairing doesn't repeat for 35 days.

3. **Axis by monthly operator** — 12 shifts per year. Each month aligns to one Axis via its Operator. March = 🔨 Functional (fero), June = ⌛ Time (grapho), etc.

**Color = User Choice.** The three gears are deterministic. The fourth dial is human.

## Files

- `rotation-engine-spec.md` — Complete date-to-zip formula with coprime math
- `junction-algorithm.md` — Procedural computation of 🚂 Junction follow-up suggestions
- `fatigue-model.md` — RPE/volume heuristic for session-to-session fatigue inference

🧮
