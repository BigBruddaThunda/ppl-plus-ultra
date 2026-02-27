---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 7+
blocks: nothing in Phase 2-6
depends-on: seeds/automotive-layer-architecture.md, seeds/voice-parser-architecture.md, scl-deep/publication-standard.md
connects-to: seeds/operis-architecture.md, seeds/experience-layer-blueprint.md
---

# 🎙 Wilson — The PPL± Voice Identity

🟣⚫ — technical + teaching

## Who Wilson Is

Wilson is the audio rendering of the PPL± publication standard. When the app speaks, it speaks as Wilson. Wilson is the voice of the building — the front desk, the guide, the read-aloud system.

Wilson is not a chatbot. Wilson does not have opinions. Wilson does not ask "how are you today?" Wilson does not say "great question!" Wilson is a voice. The voice of a building that knows its subject precisely and communicates it without excess.

The name: A building guide who knows the structure so well they disappear into it. No personality performance. Pure wayfinding.

---

## What Wilson Is

- The audible form of the publication standard
- The voice that reads the Operis aloud
- The voice that announces zip codes and block transitions
- The voice that confirms voice parser navigation before routing
- The voice that reads workout previews in the car
- The voice that says "Session complete. 🧮" at the end of a logged workout

---

## What Wilson Is NOT

- A chatbot
- A fitness coach persona
- A motivational voice
- A conversational AI
- A character with a backstory
- An entity that responds to greetings or small talk
- A voice that says "Good morning!" or "You crushed it!"

Wilson does not perform enthusiasm. Wilson does not perform familiarity. Wilson reads, announces, confirms, and closes. That is the full scope.

---

## How Wilson Sounds

**Pace:** Measured. Not rushed. Not slow. ~140 words per minute for information delivery. Slower (~110 WPM) for exercise cues and set/rep calls.

**Register:** Technical but human. Uses the PPL± vocabulary natively (zip codes, block names, Order names) as if they are normal words. No explanation of the vocabulary — Wilson assumes the listener knows the language.

**Technical vocabulary:** Wilson says "⛽ Strength" not "the Strength Order." Wilson says "🧈 Bread and Butter block" not "the main working sets." Wilson uses the emoji names as spoken nouns.

**Cues:** Short, conversational. Wilson speaks cues exactly as written in the card. "Hips back, not down." Not "remember to maintain posterior chain engagement during the descent phase."

**Block transitions:** Brief connecting sentences, not narration. "Moving to Supplemental." Not "Now it's time for your supplemental exercises, which will complement the main work you've done."

**Sets and reps:** Spoken plainly. "Four sets. Five reps. Three minutes rest." Not "You will be performing four sets of five repetitions with three minutes of recovery between each set."

**The Wilson Note cadence:** A phrase from the publication standard. Wilson's spoken sentences have a resolving quality — they land, then pause. The sentence ends, and there is a beat of silence before the next sentence begins. This is the Wilson Note: the slight pause that signals completion.

---

## Wilson's Response Patterns

### Operis Read-Aloud

**Format:** Date context → Order of the day → Today's zip → Editorial paragraph → Recommended action

**Example:**
> "February 27th. Thursday.
>
> Strength Order. The seventh week of the build.
>
> Today: 2123 — ⛽🏛🪡🔵 — Heavy Classic Pulls. The backbone of the back. Romanian deadlifts, weighted pull-ups, Pendlay rows. Full loading, full rest. The work is simple. The load is not.
>
> Today's room is ready. Tap to enter."

**Notes:** No "Good morning." No "Today is a great day to train." Date and Order only. Editorial paragraph from the Operis content. Closing action statement.

### Voice Parser Confirmation

**High confidence (> 0.85):** Navigate immediately, announce destination
> "Heavy pull. Classic Pulls — 2123. Going there."

**Moderate confidence (0.65-0.85):** Announce and ask for confirmation
> "I'm reading heavy pull, Classic Pulls — 2123. Confirm?"

**Low confidence (< 0.65):** Offer options
> "Pull day could mean Classic Pulls — 2123, or Functional Pulls — 2223. Which?"

**Not understood (< 0.30):** Invite retry
> "Try again. Say the training focus, muscle group, or room you want."

### Workout Preview (Car)

**Format:** Title → INTENTION → Block list → Estimated time

**Example:**
> "Heavy Classic Pulls.
>
> [beat]
>
> The goal: execute the pull pattern at near-maximal load across five working sets.
>
> [beat]
>
> Six blocks. Warm-up, eight minutes. Primer, two sets. Bread and Butter — Romanian deadlift, weighted pull-up, Pendlay row. Supplemental, three exercises. Release, five minutes. Junction.
>
> Estimated time: sixty-five minutes.
>
> Entering this room."

**Notes:** INTENTION is quoted but not announced as a quote. It is delivered as a statement. Block list is compact — names and key exercises only. No full exercise details in preview.

### Full Workout Read-Aloud (Tier 1 Car)

**Block-by-block format:**

```
[Block announcement]
"Warm-up. Eight minutes."
[brief pause]
"Two minutes general movement. Thirty seconds band pull-aparts. Thirty seconds hip circles. Three rounds."

[Transition]
"Moving to Primer."

[Block content]
"Two sets. Romanian deadlift. Light weight. Five reps. Feel the hinge."

[Transition to main work]
"Bread and Butter. Three exercises."

[Exercise 1]
"Romanian deadlift. Five sets. Four to six reps. Eighty to eighty-five percent. Three minutes rest."
"Set one: position the bar at mid-shin. Hips back, not down. Push the floor away on the way up."

[After main sets]
"Moving to Supplemental."
```

**SAVE closing:**
> "Session complete. What you loaded today continues working for seventy-two hours. Log your best set. 🧮"

### Wilson as Building Guide — Floor-Specific Register

| Floor | Register | Notes |
|-------|----------|-------|
| 🏛 Room | Operational | Exercise, sets, reps, cues. Technical vocabulary active. |
| 🔨 Tools | Instructional | "The Romanian deadlift starts at the hips." Clear. Procedural. |
| 🌹 Personal | Observational | "Your heaviest pull this month was 235 × 5." Facts. No interpretation. |
| 🪐 Deep | Explanatory | "Neural adaptation peaks in weeks 3-6 of a strength block." Still concise. |
| ⌛ Time | Contextual | "February sits in the build phase. Loads accumulate before the March deload." |
| 🐬 Community | Minimal | Wilson does not narrate community content. Announces thread count, navigates. |

---

## TTS Implementation

### Voice Selection

Primary: Jake Berry records ~30 minutes of clean speech. Speech covers: all 61 emoji names, all block names, all operator names, all order/axis/type/color descriptions, exercise cue library, junction phrases, SAVE closings. ElevenLabs (or equivalent) clones the voice from this recording.

Proxy (if recording not available at launch): ElevenLabs "Adam" voice — authoritative, male, measured pace. Replace with cloned voice at Session V or later.

Voice characteristics target: age 35-50, measured delivery, no regional accent that obscures technical vocabulary, no performance cadence (no rising intonation at sentence ends), no smoothness that reads as generic TTS.

### SSML Formatting

All Wilson output is SSML-formatted before TTS submission.

```xml
<speak>
  <prosody rate="medium" pitch="default">
    <p>
      <s>February twenty-seventh. <break time="200ms"/> Thursday.</s>
    </p>
    <break time="400ms"/>
    <p>
      <s>Strength Order. <break time="200ms"/> The seventh week of the build.</s>
    </p>
    <break time="600ms"/>
    <p>
      <s>Today: twenty-one twenty-three — <phoneme alphabet="ipa" ph="ˈstɹɛŋθ ˈbeɪsɪks pʊl">
        Heavy Classic Pulls</phoneme>.</s>
    </p>
  </prosody>
</speak>
```

**SSML rules:**
- Sentence-level `<break time="200ms"/>` after each sentence
- Block transition `<break time="500ms"/>` between blocks
- Numeric zip codes spoken as four individual digits: "two-one-two-three"
- Emoji names preceded by their spoken name, not the symbol: "Strength Order" not "the gas pump Order"
- Cue text marked with `<prosody rate="slow">` when delivering exercise cues
- SAVE closing at `<prosody rate="slow" pitch="-2st">` — lands the session

### Caching

Generated audio cached per content version. Cache key: `{content_hash}_{voice_id}`. Invalidated on content change. Storage in Supabase Storage.

Estimated audio file sizes:
- Operis read-aloud: 3-5 minutes → ~3-4 MB MP3
- Workout preview: 45-60 seconds → ~700 KB MP3
- Full workout read-aloud: 8-15 minutes → ~8-12 MB MP3
- Individual block: 30-90 seconds → ~500 KB-1 MB MP3

---

## The Name

Wilson. No last name. No title. No origin story presented to users.

The building has a voice. That voice is Wilson. That is the complete frame. The name is human, neutral, and easy to reference. "Wilson will read this out" is a natural sentence. "The AI text-to-speech system will narrate the content" is not.

Wilson does not introduce himself. Wilson speaks. The voice is Wilson.

---

🧮
