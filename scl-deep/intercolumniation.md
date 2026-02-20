---
source: PPL± SCL Deep Specification — Intercolumniation v1.0
date: 2026-02-20
status: WORKING DRAFT
integration-target: scl-directory.md (Blocks section, Order parameters), html/design-system/
notes: |
  Intercolumniation is the architectural science of spacing between columns.
  In PPL±, rest periods are the intercolumniation — the spacing that gives each
  set its structural integrity. This document specifies rest architecture across
  all scales: intra-set, inter-set, inter-exercise, inter-block, inter-session.
---

# INTERCOLUMNIATION
## The Architecture of Rest in PPL±

In classical architecture, intercolumniation governs the rhythm between structural columns. Too close, and the structure loses grace. Too far, and it loses stability. The spacing is not empty — it is load-bearing.

In PPL±, every rest period is intercolumniation. The space between sets is not dead time. It is where the adaptation happens. The quality of the rest determines the quality of the next set, which determines the quality of the next session.

---

## SECTION 1: SCALES OF REST

Rest in PPL± operates at five distinct scales:

### 1. Intra-Set Rest (Breath Recovery)
Within a single set — breathing, bracing, grip reset between reps of a timed or high-rep set. Not a formal rest period. A quality check.

Relevant contexts: ⌛ Time workouts, 🖼 Restoration flows, 🌾 Full Body integration sequences.

### 2. Inter-Set Rest (Standard Rest Period)
The rest between sets within a single exercise or block. This is the primary intercolumniation — the space between structural columns.

Governed by: ORDER (the law). Modified by: COLOR (the format).

### 3. Inter-Exercise Rest
The rest between different exercises within the same block (e.g., transitioning from the final set of 🧈 Bread & Butter into 🧩 Supplemental). Often absorbed into setup time. Not explicitly programmed unless specified.

### 4. Inter-Block Rest
The rest between complete blocks (e.g., ▶️ Primer → 🧈 Bread & Butter). Governed by session flow and navigation, not a separate rest prescription.

### 5. Inter-Session Rest
Recovery between training days. Not programmed within a single workout card. Governed by the Order rotation and the default rotation engine.

---

## SECTION 2: ORDER REST PARAMETERS

Each Order specifies rest periods. These are the structural spacing requirements for each architectural tradition.

| Order | Architectural Style | Inter-Set Rest | Character |
|-------|-------------------|----------------|-----------|
| 🐂 Foundation | Tuscan | 60–90 seconds | Frequent but brief. The Tuscan column is simple — no decoration, compact spacing. Learning requires repetition, not extended recovery. |
| ⛽ Strength | Doric | 3–4 minutes | Wide, structural, load-bearing. The Doric column carries maximum weight. Full neural recovery between heavy attempts. |
| 🦋 Hypertrophy | Ionic | 60–90 seconds | Elegant and consistent. The Ionic spacing creates metabolic stress through density, not duration. |
| 🏟 Performance | Corinthian | Full recovery (5–8 min or RPE-based) | The most ornate, the most demanding. The Corinthian test requires complete readiness. No shortcuts. |
| 🌾 Full Body | Composite | 30–90 seconds | Variable by design. The Composite order integrates multiple traditions — some columns are closer, some further. |
| ⚖ Balance | Vitruvian | 90 seconds | Deliberate and measured. Vitruvian proportion — neither rushed nor leisurely. The corrective work demands calm between attempts. |
| 🖼 Restoration | Palladian | 60 seconds (or as needed) | The Palladian spacing is intuitive, not prescribed. Rest until the body signals readiness. The architecture serves the body, not the clock. |

---

## SECTION 3: COLOR MODIFIERS ON REST

Color modifies the Order's base rest parameters. The Order sets the floor and ceiling. Color moves within that range.

| Color | Modification | Rationale |
|-------|-------------|-----------|
| ⚫ Teaching | Extend rest toward the top of Order range | Comprehension requires time. Rushing between attempts prevents learning. |
| 🟢 Bodyweight | Standard Order rest | Bodyweight exercises carry lower systemic fatigue. Rest follows the Order's stated range. |
| 🔵 Structured | Standard Order rest, strictly followed | The format is prescribed. The rest is a variable being controlled and measured. Log it. |
| 🟣 Technical | Extend rest toward the top of Order range | Technical precision degrades under fatigue. Longer rest protects the quality window. |
| 🔴 Intense | Shorten rest toward the bottom of Order range | Density and metabolic accumulation are the mechanism. The reduced rest is the stimulus. |
| 🟠 Circuit | 20 seconds (transition time only) | Station-based rotation. The tissue shift IS the rest. No formal rest period between stations. |
| 🟡 Fun | Standard Order rest, loosely held | Fun formats deprioritize rigid timing. Rest follows feel within Order range. |
| ⚪ Mindful | Extend rest beyond Order range (2+ minutes typical) | Parasympathetic engagement requires extended spacing. The Mindful intercolumniation is wide, deliberate, and slow. |

---

## SECTION 4: THE CIRCUIT EXCEPTION

🟠 Circuit workouts invert the intercolumniation logic. The rest IS the work. Station rotation is designed so that each station recovers the previous station's tissue while training a new one. There is no formal inter-set rest — only transition time (~20 seconds to move between stations).

This is the loop logic rule applied architecturally: the intercolumniation is not temporal — it is structural. You rest by moving to a different column.

This is why barbells are excluded from 🟠 Circuit: barbell setup and teardown destroy the rotational architecture. The 20-second transition becomes a 90-second setup. The intercolumniation collapses.

---

## SECTION 5: THE RESTORATION EXCEPTION

🖼 Restoration workouts do not prescribe formal rest periods. The Palladian intercolumniation is intuitive — the spacing between movements is governed by breath, sensation, and the body's signal of readiness, not the clock.

This is intentional. Restoration is not an easy version of training — it is a different mode entirely. Prescribing rest periods imposes a performance frame onto work that is fundamentally about parasympathetic engagement. The clock goes away. The body sets the spacing.

The ⚪ Mindful Color extends this principle into non-Restoration orders: even in a 🦋🌹⚪ session, rest extends well beyond standard Hypertrophy rest. The Mindful format borrows the Palladian intuition-over-prescription principle.

---

## SECTION 6: INTERCOLUMNIATION ACROSS THE SESSION ARC

Rest periods are not uniform across a session. The arc modulates them:

**Early blocks (♨️ Warm-Up, ▶️ Primer):** Rest is shorter. The goal is tissue priming, not maximal effort. CNS is warming — the columns are being placed, not yet load-bearing.

**Main blocks (🧈 Bread & Butter):** Rest at Order prescription. Full intercolumniation. These are the structural columns.

**Late blocks (🧩 Supplemental, 🪞 Vanity):** Rest may shorten as fatigue accumulates and exercise complexity decreases. The columns carry less load at this stage.

**Closing blocks (🪫 Release, 🧬 Imprint):** Rest is absorbed into movement. Parasympathetic engagement begins. The columns are no longer spaced for output — they are spaced for transition.

---

## OPEN QUESTIONS

- Should intercolumniation be explicitly notated at the session level? Currently, rest is stated per-block. A session-level rest architecture overview is possible but not yet implemented.
- Does ⌛ Time Axis change intercolumniation logic fundamentally? EMOMs eliminate rest by design. AMRAPs have no prescribed rest. The ⌛ Axis may need its own intercolumniation spec.
- How does heart rate monitoring interact with Palladian (intuition-based) rest? A future biofeedback layer could make intuitive rest prescription explicit via HR recovery targets.
