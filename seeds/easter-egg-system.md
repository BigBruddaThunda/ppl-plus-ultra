# Easter Egg System

**Planted:** 2026-03-09
**Status:** SEED
**Depends on:** Exercise Library, Cosmograms, Guild Campaign Architecture, Zip Registry
**Blocks:** Nothing

---

## What This Is

Hidden content, riddles, and collectibles scattered across the 1,680 zip codes. Some are permanent fixtures. Some rotate with the campaign cycle. Some require knowledge gained from the exercise library, cosmograms, or Operis editions to find.

The Easter egg system turns the entire Ppl± region into an explorable world where curiosity is rewarded and the library is the map.

---

## Egg Categories

### 1. Zip Fossils (Permanent)

Hidden facts embedded in specific zip codes. Always there. Discoverable by visiting the room and looking.

Examples:
- ⛽🏛🪡🔵 (2123) contains a note about the historical origin of the barbell row
- 🖼🌹➖⚪ (7358) contains a breathing technique from a 19th century restoration manual
- 🏟🪐🛒🔴 (4415) contains the date and weight of a famous bench press world record

**Source:** Cosmogram research deposits. When a cosmogram is populated for a deck, fossils are planted in its 40 zip codes. The cosmogram's deep research naturally produces historical fragments that become fossils.

**Discovery mechanic:** User visits the zip code. If bloom level >= 2 (regular visitor), the fossil is revealed in a collapsible section of the room UI. First-time visitors see only the workout. Return visitors discover the depth.

### 2. Riddle Chains (Campaign-Rotated)

Multi-step riddles that span multiple zip codes. Solving one step reveals a clue pointing to the next zip. The final step reveals the answer.

**Structure:**
```
Riddle Chain: "The Path of the Carrier" (5 steps)

Step 1: Clue planted in 🧸 fero operator's guild hall zip
        "Where the foundation carries weight through the full range,
         find the room where bodyweight meets the pull."
        → Answer: 🐂🔨🪡🟢 (1222) — Foundation/Functional/Pull/Bodyweight

Step 2: Clue in 1222
        "The muscle that connects your shoulder blade to your arm
         has a section named for it. Find its heaviest room."
        → Answer: Exercise library → Lats → 🪡 Pull → ⛽🏛🪡🔵 (2123)

Step 3: Clue in 2123
        ...continues...

Step 5: Final answer reveals a campaign bonus (guild XP, access unlock, etc.)
```

**Generation:** Riddle chains are deterministically generated from campaign_date + chain_id. Each 35-day campaign has 5-10 active chains. Different guilds may see different starting clues.

**Knowledge requirement:** Solving riddles requires reading the exercise library, understanding SCL structure, or recalling facts from Operis editions. The system teaches through puzzles.

### 3. Collection Events (Weekly)

Small collectibles scattered across zip codes during a campaign week. Like a scavenger hunt.

**Mechanic:**
- Each week, 8 "fragments" are placed in 8 zip codes (one per Color)
- Fragments are visible only when you log a session in that zip code (not just visit)
- Collecting all 8 fragments = one complete artifact
- Artifacts contribute to party quest completion and personal octave

**Fragment placement:** Deterministic from week_start_date. Fragments always land in zips matching their Color (a 🔵 fragment is always in a 🔵 zip code). The Order, Axis, and Type vary weekly.

### 4. Anti-Zip Discoveries

Every zip has a cosine-farthest zip (its "anti-zip" — resolved by city_compiler.py). Visiting both your most-similar and most-dissimilar zips within the same campaign unlocks a hidden comparison view.

**Mechanic:**
- System tracks your most-visited zip and computes its anti-zip
- When you log a session in the anti-zip, you unlock a "Polarity Report"
- The report shows how the two zips differ across all 61 dimensions
- This teaches SCL structure through direct experience

### 5. Library Keys

Specific exercises in the exercise library have hidden cross-references to other zip codes.

**Mechanic:**
- When a user logs a session that includes a specific exercise for the 5th time, a "key" appears
- The key contains a fragment of lore about that exercise's history or biomechanics
- Collecting 5 keys from the same exercise section (e.g., Section D: Back) unlocks a "Section Master" badge
- Section Masters get early access to new cosmogram deposits for that section's related decks

---

## The Library as Map

The exercise library (~2,185 exercises across 17 sections) is the primary knowledge base for the Easter egg system. Riddle clues reference:
- Exercise names and their section letters
- Muscle group mappings
- Equipment tier ranges
- GOLD-gated status
- Movement patterns

Users who read and understand the library will solve riddles faster. Users who just log sessions will still find fossils and fragments through exploration. Both paths are valid. The library path is faster.

---

## Density and Pacing

Not every zip code has an egg at all times. Scarcity matters.

```
Permanent eggs (fossils):     ~200 zip codes (12% of 1,680)
Active riddle chains:         5-10 per campaign (spanning ~30-50 zips)
Weekly fragments:             8 per week (1 per Color)
Anti-zip discoveries:         1 per user per campaign (personalized)
Library keys:                 ~100 exercises with keys (5% of library)
```

At any given time, a user might encounter an egg in roughly 1 in 8 zip codes they visit. Rare enough to be exciting. Common enough to keep looking.

---

## Scoring Integration

Easter egg discoveries feed into the octave scoring system:

| Discovery | Personal Octave | Guild Octave |
|-----------|----------------|--------------|
| Fossil found | +0.25 | — |
| Riddle step solved | +0.5 | +0.25 |
| Riddle chain completed | +2.0 | +1.0 |
| Weekly fragment collected | +0.25 | — |
| Full artifact (8 fragments) | +1.0 | +0.5 |
| Anti-zip polarity report | +0.5 | — |
| Library key unlocked | +0.25 | — |
| Section Master badge | +1.0 | +0.5 |

---

## Technical Architecture

**Egg storage:** Each egg is a JSON record in an egg registry:
```json
{
  "egg_id": "fossil-2123-001",
  "type": "fossil",
  "zip": "2123",
  "content": "The barbell row appeared in strength training...",
  "visibility": {
    "min_bloom": 2,
    "campaign": null,
    "week": null
  },
  "source": "deck-07-cosmogram"
}
```

**Discovery is event-sourced:**
- User logs session → event
- System checks: does this zip have an active egg? Is user eligible?
- If yes: discovery event emitted → projection updates user's collection

**No client-side hiding:** Eggs are not hidden in the UI code. They are server-resolved based on user state + zip state. You cannot inspect-element your way to an egg. The server decides what you see based on your bloom level, campaign state, and discovery history.

---

## Open Questions

- Should egg content be user-generated? (e.g., a cosmogram researcher plants a fossil as part of their research deposit)
- Should there be "dark eggs" that are only visible in cathedral (dark) register?
- Should riddle chains have time limits? Or persist for the full 35-day campaign?
- Should fossil density increase as cosmograms are populated? (Natural growth model)
- Can guilds "claim" zip codes by planting their guild's banner egg?

---

## Relationship to Other Seeds

- **guild-campaign-architecture.md** — Campaign cycle drives rotational egg placement
- **party-formation-engine.md** — Party quests can reference egg collection
- **cosmogram-research-prompt.md** — Cosmogram research deposits become fossil content
- **operis-architecture.md** — Operis editions can reference active riddle chains
- **elevator-architecture.md** — Restricted floors could hide exclusive eggs
- **content-types-architecture.md** — Easter egg content is a content type (mapped to Axes)
