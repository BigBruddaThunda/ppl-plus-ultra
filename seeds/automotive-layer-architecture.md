---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 7+
blocks: nothing in Phase 2-6
depends-on: seeds/experience-layer-blueprint.md, seeds/numeric-zip-system.md, seeds/operis-architecture.md, seeds/voice-parser-architecture.md, seeds/data-ethics-architecture.md
connects-to: seeds/platform-architecture-v2.md, seeds/wilson-voice-identity.md, seeds/regional-filter-architecture.md
---

# 🚗 Automotive Layer Architecture — Android Auto, CarPlay, and the Free-Tier Funnel

🟡🔨 — fun + functional

## One Sentence

The car is PPL±'s sixth screen — a free-tier daily touchpoint where the Operis is read aloud with Wilson's voice, zip codes are navigated by speech, and curated playlists surface for every workout mood, converting commuters into subscribers through familiarity, not friction.

---

## Why The Car Works for PPL±

The car is the most under-addressed surface in fitness apps. It is where people:
- Commute to the gym (10-30 minutes of latent attention)
- Process yesterday's session (what worked, what to do next)
- Decide what today's training looks like
- Listen to workout programming while driving to the park, the track, or the box

The car is not where people log sets. It is where people prime for the session, get the Operis context, hear Wilson describe the day's focus, and queue up their playlist. The car turns a dead-time commute into a pre-session brief.

PPL± has unique natural advantages for the car:
- The Operis is designed to be read aloud (the Wilson Note format)
- Zip code navigation is voice-friendly (4 dial positions = 4 spoken concepts)
- The 7 Orders map cleanly to days of the week (natural spoken context)
- The playlist layer pairs directly with every zip code mood

---

## Free-Tier Car Experience

No login required. No subscription required. Available to anyone who installs the app.

### Daily Commute Flow

**Morning → gym:**
1. Open app in Android Auto or CarPlay
2. "Today's Operis" auto-queues
3. Wilson reads the Operis intro: date, Order for the day, today's zip recommendation, context paragraph
4. Operis ends with: "Today's room is ⛽🏛🪡🔵 — Heavy Classic Pulls. Tap to preview."
5. User taps → Wilson reads 45-second workout preview (title, INTENTION, block list)
6. Commute ends. User walks into gym knowing the plan.

**Post-session → home:**
1. Open app
2. "Operis review" — 60-second reflection content (what today's training builds toward, what to eat, what tomorrow's order likely is)
3. Playlist suggestion for the drive home (recovery mood from today's zip)

### Free-Tier Audio Content Available in Car

- Today's Operis (full text, Wilson voice)
- Zip audio previews (title + INTENTION + block list, ~45 seconds)
- Deck overview audio (brief description of the deck, what it's for)
- Almanac seasonal framing (what month/phase we're in, training context)
- Regional Operis framing (if region is set — no GPS required, user-declared)

### Free-Tier Car Content NOT Available

- Full workout read-aloud (Tier 1)
- Personal history context ("Last time you did this, you hit 225×5") (Tier 1)
- Junction suggestions personalized to user's history (Tier 1)
- Session timer with audio cues (Tier 1)
- Playlist deep links to Spotify/Apple Music (Tier 1)

---

## Subscriber Car Experience (Tier 1+)

### Full Workout Read-Aloud

Wilson reads the complete workout card, block by block:
1. INTENTION — one sentence, quoted, delivered as a framing statement
2. Each block — name, exercises, sets/reps/rest
3. Block transitions — brief connecting sentence
4. SAVE — closing principle

The workout read-aloud is the car's primary Tier 1 value. Users who drive to the gym hear the entire session before they arrive. No fumbling with phone in the gym.

### Personal History Context

If the user has logged this zip before, Wilson surfaces a brief context before the workout begins:
> "You've trained this room 4 times. Your best set was 245 × 5 on Romanian deadlifts, logged November 3rd. Today's structure is identical — the load is yours to determine."

This is a simple database query (most recent log for this zip). No ML, no inference. Just context.

### Junction Suggestions

At the Operis read-aloud end:
> "Based on your recent sessions, tomorrow could benefit from ⚖🏛🪡🔵 — Balance Basics Pull. You've been training heavy pulls frequently. A lighter corrective session fills the gap."

The Junction algorithm from `middle-math/rotation/junction-algorithm.md` runs on the user's history and surfaces the recommendation. Car audio surfaces the top pick.

### Session Timer With Audio Cues

For timed workouts (⌛ Time axis, ⚫ Teaching rest periods), the app can voice-cue rest intervals:
> "Rest period. 3 minutes. Two minutes remaining." [tone]

This keeps the user heads-up during timed sessions instead of checking the phone.

---

## Voice Navigation Via Parser

The voice parser from `seeds/voice-parser-architecture.md` is the car's primary navigation input. Users speak to navigate.

### Natural Language Examples

| User says | App routes to |
|-----------|--------------|
| "Heavy legs" | ⛽🏛🍗 + highest confidence Color |
| "Restoration pull" | 🖼🌹🪡 + highest confidence Color |
| "Today's workout" | Today's Operis zip |
| "Bodyweight push no equipment" | ⛽🟢🛒🟢 (bodyweight) |
| "What did I do last Tuesday" | /me/history + filter by date |
| "Play recovery playlist" | Playlist for 🖼 order mood |
| "Strength basics this week" | ⛽🏛 filtered view |

### Car-Specific Parsing Adjustments

In car mode, the parser's confidence threshold is higher before navigating (0.90 vs 0.85 in app). The stakes of a wrong navigation are higher when driving. Low-confidence parses prompt for confirmation: "Did you mean Heavy Classic Pulls? Say yes to confirm."

### Steering Wheel Button Mapping

| Button | Function |
|--------|----------|
| Next track button | Next block in workout read-aloud |
| Previous track button | Replay current block |
| Play/pause | Pause/resume Wilson |
| Voice button | Open voice parser |
| Mode button | Switch: Operis / Workout / Playlist |

---

## Car Screen Layout

**Android Auto / CarPlay touchscreen:**

```
┌─────────────────────────────────────┐
│  🏋 PPL±   [Today: ⛽]  [🔍 Voice] │
├─────────────────────────────────────┤
│                                     │
│  Today's Operis                     │
│  ⛽🏛🪡🔵 Heavy Classic Pulls      │
│                                     │
│  [▶ Play Operis]  [🎵 Playlist]    │
│                                     │
├─────────────────────────────────────┤
│  Recent Rooms                       │
│  ⛽🔨🛒🔵  ⛽🏛🍗🟣  🖼🌹🪡⚪    │
└─────────────────────────────────────┘
```

Simplified. Large tap targets. Minimal reading required. The screen reinforces what Wilson is saying, not the other way around.

---

## Playlist Layer — 56 Mood Profiles

Every zip code has a workout mood derived from Order × Color. 7 Orders × 8 Colors = 56 profiles.

### Mood Derivation Logic

```
Order = energy level (low → high: 🖼 < 🐂 < ⚖ < 🌾 < 🦋 < ⛽ < 🏟)
Color = texture (mellow → intense: ⚪ < 🟢 < ⚫ < 🟡 < 🔵 < 🟠 < 🟣 < 🔴)
Mood = Order × Color compound label + music characteristics
```

### Sample Mood Profiles

| Zip pattern | Order | Color | Mood label | Music character |
|-------------|-------|-------|-----------|-----------------|
| ⛽🔴 | High energy | Intense | **Drive** | High BPM (140-160), aggressive, hip-hop/metal |
| ⛽🔵 | High energy | Structured | **Focus** | Moderate BPM (120-130), instrumental, electronic |
| 🦋🔴 | Moderate-high | Intense | **Pump** | High BPM (130-145), pop, hip-hop |
| 🖼⚪ | Low energy | Mindful | **Restore** | Low BPM (60-80), ambient, acoustic |
| 🖼🌹 | Low energy | Aesthetic | **Unwind** | Low BPM (70-90), jazz, lo-fi |
| 🏟🟣 | Max | Technical | **Compete** | High BPM (150+), electronic, cinematic |
| 🌾🟡 | Moderate | Fun | **Play** | Variable BPM, genre-mix, energy-following |
| ⚖⚫ | Moderate | Teaching | **Reset** | Moderate BPM (100-115), jazz, soul |

### Playlist Database

```sql
CREATE TABLE mood_playlists (
  id              SERIAL PRIMARY KEY,
  order_position  SMALLINT NOT NULL CHECK (order_position BETWEEN 1 AND 7),
  color_position  SMALLINT NOT NULL CHECK (color_position BETWEEN 1 AND 8),
  mood_label      TEXT NOT NULL,
  mood_bpm_low    SMALLINT,
  mood_bpm_high   SMALLINT,
  spotify_query   TEXT,
  apple_query     TEXT,
  spotify_playlist_id TEXT,
  apple_playlist_id   TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW()
);
```

56 rows — one per Order × Color combination. Queries built from mood characteristics. Specific playlist IDs populated when available.

### Streaming Deep Links

```
Spotify: spotify:playlist:[id] (if known) or spotify:search:[encoded_query]
Apple Music: music://music.apple.com/playlist/ or music://search?term=[encoded_query]
```

---

## TTS Architecture

### Voice Selection

Wilson's voice is recorded by Jake Berry and cloned via ElevenLabs (or equivalent). ~30 minutes of clean speech recording is sufficient for high-quality cloning. The recorded voice is Wilson.

If voice cloning is not available for launch: use ElevenLabs' "Adam" voice (authoritative, measured pace) as a proxy. Replace with cloned voice when recording is complete.

### SSML Pipeline

Card content → Markdown stripper → SSML formatter → TTS API → MP3 → Supabase Storage

```xml
<!-- Wilson's block transition pattern -->
<speak>
  <p>
    <s>Warm-up. <break time="300ms"/> Eight minutes.</s>
    <s>Start with two minutes of general movement. <break time="200ms"/>
       Then thirty seconds of band pull-aparts. <break time="200ms"/>
       Then thirty seconds of hip circles. <break time="200ms"/>
       Repeat three times.</s>
  </p>
  <break time="500ms"/>
  <p>
    <s>Moving to the Primer.</s>
  </p>
</speak>
```

**SSML rules for Wilson:**
- Sentence-level pauses after each exercise: `<break time="300ms"/>`
- Block transition pauses: `<break time="500ms"/>`
- Set/rep announcements spoken without punctuation flair: "Five sets. Four to six reps."
- No exclamation tone. No upward inflection on sets/reps.
- Numbers spoken as numbers, not words where possible: "85%" = "eighty-five percent"

### Caching Strategy

Generated audio cached per card version (zip_code + card_status). GENERATED and CANONICAL status both cache. Cache invalidated on card content update (card transitions from GENERATED → CANONICAL with content changes).

Storage path: `audio/zip/{zipcode}/{status}.mp3`
Operis audio: `audio/operis/{date}.mp3`
Preview audio: `audio/zip/{zipcode}/preview.mp3`

---

## Android Auto Technical Requirements

- Android Auto SDK (latest)
- Media3 library (MediaBrowserService)
- Register app as media app in Android Auto developer console
- Test with Android Auto Desktop Head Unit (DHU) during development
- Compliance review required before Play Store publication
- Minimum car screen: 960×540 (standard), optimize for 1920×720 (wide)

**MediaBrowserService structure:**

```
Root
├── Today's Operis
│   ├── [Play Operis Audio]
│   └── Today's Zip Preview
├── Saved Rooms (requires auth)
│   ├── [Room 1]
│   ├── [Room 2]
│   └── ...
├── Browse by Order
│   ├── 🐂 Foundation
│   ├── ⛽ Strength
│   └── ...
└── Recent Sessions (requires auth)
```

---

## Apple CarPlay Technical Requirements

- CarPlay Entitlement from Apple (application required — music/audio category)
- CPListTemplate for browse, CPNowPlayingTemplate for playback
- Minimum deployment target: iOS 14
- Background audio capability required
- Test with CarPlay Simulator (included in Xcode)

---

## Tier Structure Evolution

**At launch:**
- Free: Operis audio (car + web), zip previews, almanac, deck audio overviews
- Tier 1 ($10): Full workout audio, personal history context, junction suggestions, timer cues
- Tier 2 ($25-30): Everything in Tier 1 + community floor + program builder

**Post-launch V2 consideration:**
- Tier 0.5 (Car-only: $4): Operis + full workout audio, no web interactive rooms
  This converts commuters who don't use the web app. Reduces friction for pure audio users.
  Decision: evaluate after 6 months of launch data.

---

## Revenue Model — Car as Funnel

The free Operis audio in the car serves one conversion function: familiarity.

A user who hears the Operis 5 days a week for 3 weeks has internalized the PPL± vocabulary. They know what ⛽ means. They know Wilson's voice. They know the block structure. When they upgrade to Tier 1, the app is not new — it's familiar. The learning curve is already climbed. The conversion is from "this is interesting" to "I use this every day, I should pay for it."

**Projected funnel:**
- Car app installs → Web signups: 15-25% (users look it up after hearing the Operis)
- Web signups → Tier 1: 20-30% (standard subscription conversion)
- Effective car → paid conversion: ~4-8%

At 10,000 car installs: ~400-800 paid subscribers. At $10/month: $4,000-8,000 MRR from the car funnel alone.

The car app has no CAC. It is passive familiarity marketing built into the product.

---

## Build Sessions

Sessions V-Z from `seeds/claude-code-build-sequence.md`:
- **V:** TTS pipeline + Wilson voice
- **W:** Playlist layer + mood profiles
- **X:** Android Auto integration
- **Y:** Apple CarPlay integration
- **Z:** Free-tier audio funnel + conversion tracking

---

🧮
