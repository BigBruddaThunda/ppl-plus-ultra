---
planted: 2026-03-11
status: SEED
phase-relevance: Phase 5/6/7 (User Experience, Almanac, Community)
blocks: nothing currently — progression and identity layer
depends-on: seeds/heros-almanac-v8-architecture.md, seeds/home-screen-architecture.md, middle-math/weights/, scl-directory.md
connects-to: seeds/exploration-immersion-architecture.md, seeds/life-copilot-architecture.md, seeds/digital-city-architecture.md, seeds/exercise-superscript.md, seeds/outside-system-v2-architecture.md
extends: seeds/heros-almanac-v8-architecture.md (adds 8×7 skill matrix, vial mechanics, subclass rotation, RuneScape/GW2 design principles)
legacy-references: r/outside (life as RPG framing), Guild Wars 2 (horizontal progression), RuneScape (classless skill interconnection)
---

# Character Progression Architecture — The 8×7 Skill Matrix

🟡🟣 — exploratory + precise

## One Sentence

The Ppl± character progression is a classless, horizontal system where 8 Colors are stat groups, each containing 7 Order-based skills, governed by 12 operator Houses as emergent classes — with identity that shifts daily based on actual engagement, not a selection screen.

---

## Section 1 — Design Philosophy

Three games define the architectural constraints:

**Guild Wars 2:** No power creep. The stat ceiling is low and reached early. Progression after that is breadth — more options, more areas, more mastery of systems. Old content stays relevant. You inhabit the world. You don't climb a ladder that makes the bottom rungs disappear.

**RuneScape:** No class system. 24+ independent skills, all interconnecting. Your identity emerges from what you actually do — thousands of hours of play, not a menu selection. Total level (sum of all skills) rewards breadth. Quests gate content behind multi-skill requirements, preventing hyper-specialization.

**r/outside:** Real life has no class system either. Your "build" is the combination of what you've invested time in. A surgeon is someone who ground the Medicine skill tree for 12 years. A carpenter is someone who leveled Woodworking. Identity is behavioral, not categorical.

**Ppl± principle:** Your character is not who you say you are. Your character is what you do. The system watches what you engage with and derives your identity from that engagement. Where you start (Almanac cold data) is not where you end (warm behavioral data). The system grows with you.

---

## Section 2 — The 8 Stat Groups (Colors)

The 8 SCL Colors become 8 stat groups. Each Color represents a domain of human capacity — not just workout equipment tiers, but the full cognitive posture each Color carries (see `seeds/color-pipeline-posture.md`).

| Color | Stat Domain | What It Measures |
|-------|-------------|------------------|
| ⚫ Teaching | **Comprehension** | How well you understand and can teach what you know. Knowledge depth. Ability to explain. |
| 🟢 Bodyweight | **Self-Reliance** | Independence. Ability to function without external tools or dependencies. Resourcefulness. |
| 🔵 Structured | **Discipline** | Consistency. Adherence to systems. Tracking. Showing up on schedule. |
| 🟣 Technical | **Precision** | Quality of execution. Attention to detail. Craft mastery. Doing fewer things better. |
| 🔴 Intense | **Output** | Raw capacity. Volume. Throughput. How much you can produce at full effort. |
| 🟠 Circuit | **Adaptability** | Ability to rotate between tasks. Transition speed. Multi-domain competence. |
| 🟡 Fun | **Exploration** | Curiosity. Willingness to try new things. Breadth of experience. Discovery. |
| ⚪ Mindful | **Recovery** | Rest quality. Self-awareness. Balance. Ability to slow down and restore. |

These names and descriptions are working drafts — they need publication standard proofing. The stats should feel like they belong in an NPR segment about human development, not a fantasy game manual.

---

## Section 3 — The 7 Skills Per Stat (Orders)

Each of the 8 stat groups contains 7 skills — one per Order. The 7 Orders represent developmental phases, so each skill within a stat group measures that stat at a different depth level.

**The 8×7 matrix = 56 total skills.**

Example: the 🔵 Discipline stat group contains:

| Order | Skill Name (Working) | What It Tracks |
|-------|---------------------|----------------|
| 🐂 Foundation | Routine | Ability to establish basic habits and patterns |
| ⛽ Strength | Commitment | Ability to sustain effort under heavy load / high stakes |
| 🦋 Hypertrophy | Consistency | Volume of repeated engagement over time |
| 🏟 Performance | Benchmarking | Willingness to test and measure progress |
| 🌾 Full Body | Integration | Ability to maintain discipline across multiple domains simultaneously |
| ⚖ Balance | Correction | Ability to self-correct when discipline falters |
| 🖼 Restoration | Sabbath | Ability to rest WITHOUT guilt — disciplined rest |

Each Order brings a different lens to the same Color domain. 🐂 asks "can you start the habit?" while 🏟 asks "will you test whether it's working?" and 🖼 asks "can you discipline yourself to stop?"

### Skill Naming Convention

All 56 skill names must pass:
- **Publication standard** — informational, no fantasy taxonomy, no hype
- **Grandma test** — a grandmother would understand what this skill measures
- **E for everyone** — culturally inclusive, no faction, no party
- **NPR/PBS register** — adult, mature, respectful, candid

Working names above are placeholders. Final names emerge from cosmogram research and vocabulary standard proofing (`scl-deep/vocabulary-standard.md`).

---

## Section 4 — The Superscript/Subscript Scoring System

Each of the 56 skills has a ± score. This extends the exercise-row superscript/subscript system (`seeds/exercise-superscript.md`) to the character level.

### The Two Numbers

- **Superscript (+)** — your current top-end score. The best version of this skill as demonstrated by your engagement. The clean fluid in the vial.
- **Subscript (-)** — your current deficit/neglect score. How far the shadow side has grown. The sludge in the vial.

### The ± Balance

The gap between superscript and subscript is the ± balance for that skill.

```
Superscript: 74    Subscript: 2     → Total: 76, Balance: 72 (healthy)
Superscript: 74    Subscript: -54   → Total: 20, Balance: 128 gap (crisis)
```

**Goal:** Keep subscript close to 0. A high superscript means nothing if the subscript is deeply negative. The system rewards balance, not peak performance in isolation.

The subscript grows negative through neglect — time passing without engagement in that skill domain. The superscript grows through active engagement. Both numbers are constantly adjusting based on behavior.

### How Skills Roll Up Into Stat Vials

The 8 vials on the home screen (see `seeds/home-screen-architecture.md`) are the aggregate of their 7 skill scores:

```
Vial[Color] = Σ (skill_superscript[Order] + skill_subscript[Order]) for all 7 Orders

Clean fluid level = Σ skill_superscript[Order] / max_possible
Sludge level = |Σ skill_subscript[Order]| / max_possible (shown as dark fluid at bottom)
```

The shared fluid pool across all 8 vials means the total system is zero-sum at any given moment. Engagement in one Color domain draws capacity from the pool. This prevents infinite growth and forces the GW2-style horizontal balance.

---

## Section 5 — The 12 Houses (Operator Classes)

The 12 operators are the class system. But like RuneScape, you don't pick a class — it emerges from your behavior.

### House Sorting (from heros-almanac-v8-architecture.md)

The user's 61-dimensional personal vector is compared via cosine similarity to all 12 operator weight profiles. The highest match is their primary House. Top 3 matches define a multi-class blend.

### Houses as Character Archetypes

| House | Operator | Archetype Character |
|-------|----------|-------------------|
| 📍 pono | The Architects | Methodical. Positions before acting. Proven-ground builders. |
| 🧲 capio | The Receivers | Patient. Absorb before responding. Assessment-first. |
| 🧸 fero | The Carriers | Connective. Bridge domains. Transfer knowledge between contexts. |
| 👀 specio | The Observers | Perceptive. See what others miss. Form and detail oriented. |
| 🥨 tendo | The Extenders | Ambitious. Push boundaries. Stretch beyond current limits. |
| 🤌 facio | The Executors | Productive. Do the work. Output-oriented. Concentric force. |
| 🚀 mitto | The Launchers | Committed. All-in on attempts. Maximum intent. Explosive. |
| 🦢 plico | The Layerers | Synthetic. Combine elements. See connections between things. |
| 🪵 teneo | The Anchors | Persistent. Hold position under pressure. Duration masters. |
| 🐋 duco | The Conductors | Orchestrative. Manage complexity. Systems thinkers. |
| ✒️ grapho | The Scribes | Documentary. Record, log, prescribe. Knowledge preservers. |
| 🦉 logos | The Interpreters | Analytical. Find meaning in data. Pattern recognizers. |

### Subclass Rotation

Here's where Ppl± diverges from traditional RPGs: your subclass rotates.

The multi-class blend (top 3 operators) shifts based on recent engagement. The personal vector updates with every logged action. Cosine similarity against operator profiles recomputes. Your primary House might stay stable over months, but your secondary and tertiary Houses can rotate weekly or even daily.

**This is the daily subclass shift.** You wake up as a 🤌 facio / 🧸 fero / 📍 pono. Two days of heavy analytical work later, you're a 🤌 facio / 🦉 logos / 🧸 fero. The system reflects who you've been this week, not who you declared yourself to be.

The home screen header shows your current House badge. It changes. You notice it change. It becomes a mirror.

### Class × Stat Interaction

Your House influences which stat vials are naturally fuller. A 🤌 facio (Executor) naturally accumulates more in 🔴 Output and ⛽ Commitment. A 👀 specio (Observer) naturally accumulates more in 🟣 Precision and ⚪ Recovery.

But these are tendencies, not locks. The system rewards cross-domain engagement. A 🤌 facio who deliberately invests in ⚪ Recovery is building a more balanced profile — and the vials reflect that.

---

## Section 6 — What Feeds the System

Every user action adjusts the personal vector, which adjusts skill scores, which adjusts vial levels, which adjusts House sorting.

### Input Sources

| Action | Vector Adjustment | Weight |
|--------|-------------------|--------|
| Logged workout at a zip code | All 4 dial dimensions of that zip | High (primary signal) |
| Explored a room (visited, scrolled) | Lighter adjustment on zip dimensions | Low (presence signal) |
| Completed a floor within a room | That Axis dimension boosted | Medium |
| Read an Operis edition | That day's Order dimension | Low |
| Community contribution | 🐬 Sociatas dimension + zip context | Medium |
| Outside System activity log | Nearest zip-code match dimensions | Medium |
| Almanac Dare responses | Direct 61-dim cold-start data | High (decays over time) |
| Time-based neglect | Subscript grows on neglected dimensions | Passive (continuous) |

### The Decay Principle

From heros-almanac-v8-architecture.md: the Almanac's influence decays as logged data accumulates. Cold-start identity fades. Warm behavioral identity grows. Where you start is not where you end.

Subscript sludge accumulates passively on skills that aren't engaged. This is not punishment — it's physics. A muscle you don't use atrophies. A skill you don't practice decays. The system reflects reality.

---

## Section 7 — Progression Model (GW2 Horizontal)

### What Does NOT Happen

- **No level cap increases.** The skill ceiling is fixed. You can't grind to 999.
- **No power creep.** A veteran user and a new user in the same zip code have the same content. The veteran has more unlocked breadth, not more power.
- **No obsolescence.** 🐂 Foundation content is never "too easy" for an advanced user. Down-scaling keeps everything relevant — you revisit Foundation rooms for the same reasons a GW2 veteran revisits starter zones.
- **No leaderboard ranking.** There is no global #1. The only comparison is you vs. your own ± balance.

### What DOES Happen

- **Breadth unlocks.** As you visit more zip codes, more of the fog clears. You discover more content, more connections, more easter eggs. Progression IS exploration.
- **Mastery deepens.** Repeat visits to the same zip code reveal deeper layers — the almanac accumulates history, the community thread grows, your personal notes build up. Depth IS progression.
- **Balance improves.** The 8 vials approach equilibrium. Sludge recedes. The ± gap narrows. Balance IS the endgame.
- **House identity solidifies.** Over months, your primary House stabilizes as a genuine reflection of how you engage with the world. Identity IS emergent.
- **Access opens.** Some content requires conditions (see `seeds/exploration-immersion-architecture.md`). Meeting those conditions through organic engagement opens new rooms, new features, new layers. Access IS earned.

### The Total Level Equivalent

RuneScape's total level (sum of all skill levels) is the prestige metric. Ppl± equivalent: **total ± balance** — the sum of all 56 skill ± balances. This single number rewards breadth and balance. It's the only "score" that matters globally.

But even this is private by default. You see your own total. Others see your House badge and your recent engagement. The system does not rank humans.

---

## Section 8 — The Vial Interaction Loop

The home screen vials (from `seeds/home-screen-architecture.md`) are the character sheet rendered as a dashboard. Here's the full interaction loop:

```
User engages with content (workout, reading, community, exploration)
  ↓
Personal vector updates (61 dimensions adjust)
  ↓
56 skills recalculate (8 Colors × 7 Orders)
  ↓
8 vials redistribute fluid (shared pool rebalances)
  ↓
House sorting recomputes (cosine similarity against 12 operators)
  ↓
Home screen reflects new state (vials, badge, map fog)
  ↓
System recommends next engagement (rotation engine biased by current balance)
  ↓
User engages...
```

This is a feedback loop, not a linear progression. The system and the user co-evolve.

---

## Section 9 — DnD Stat Mapping Reference

For users familiar with RPG stat systems, the 8 Colors map loosely to expanded DnD-style attributes:

| DnD Stat | Closest Color(s) | Why |
|----------|-------------------|-----|
| STR (Strength) | 🔴 Output | Raw force, capacity, volume |
| DEX (Dexterity) | 🟠 Adaptability | Quick transitions, multi-task, agility |
| CON (Constitution) | ⚪ Recovery + 🟢 Self-Reliance | Endurance, health, independence |
| INT (Intelligence) | ⚫ Comprehension + 🟣 Precision | Knowledge depth, analytical quality |
| WIS (Wisdom) | 🔵 Discipline + ⚪ Recovery | Judgment, patience, self-awareness |
| CHA (Charisma) | 🟡 Exploration + 🟠 Adaptability | Curiosity, social versatility |

This is a loose mapping for conceptual orientation — not a 1:1 correspondence. The 8 Ppl± stats are broader and more life-applicable than the 6 DnD stats. The mapping helps onboard RPG-literate users without constraining the system.

---

## Section 10 — What This Is Not

- **Not gamification theater.** No arbitrary points, no fake levels, no badges for logging in 5 days in a row. Every number represents real engagement across real domains.
- **Not competitive.** No PvP. No rankings. No "who has the highest score." The only competition is your current self vs. your balanced self.
- **Not a personality test.** The Almanac is a cold-start scaffold, not an identity assignment. The system learns who you are from what you do, not what you say.
- **Not punitive.** Sludge accumulation is physics, not punishment. The system doesn't judge neglect — it reflects it so you can address it.
- **Not mandatory.** Users who ignore the RPG layer entirely still get full workout functionality. The progression system is a lens on the data, not a gate on the content.

---

## Section 11 — Open Questions

1. **Skill naming pass.** All 56 skills need names that pass publication standard, grandma test, NPR/PBS register. This is a dedicated creative session.
2. **Fluid pool size.** What's the total pool? Fixed number? Percentage-based? Does the pool grow with engagement (total capacity increases) or stay fixed (pure redistribution)?
3. **Sludge decay rate.** How fast does neglect accumulate? Linear? Exponential? Capped? Seasonal variation?
4. **Vial-to-content gating.** Do vial thresholds gate content access? ("You need 🟣 Precision above X to access this content.") If so, how to communicate this without feeling punitive?
5. **Cross-Color skill interconnection.** RuneScape's power is that skills feed each other. How do the 56 Ppl± skills interconnect? Does leveling 🔴⛽ (Output/Commitment) feed into 🔵⛽ (Discipline/Commitment)?
6. **House visual identity.** Each House needs a visual register. Art direction session needed.
7. **Subclass display.** How is the multi-class blend shown on the home screen? Badge stack? Blended icon? Tooltip?
8. **r/outside framing.** How much of the r/outside vocabulary do we adopt? The humor creates a safe container for vulnerability. But it needs to pass publication standard.
9. **Total ± balance display.** Where does the global balance number live? Always visible? On a stats page? Private only?
10. **Onboarding the RPG layer.** Do users discover the stat system gradually (fog of war on the character sheet itself) or see it immediately? Progressive disclosure suggests: vials appear early, skill names appear when tapped, House badge appears after first week.

---

🧮
