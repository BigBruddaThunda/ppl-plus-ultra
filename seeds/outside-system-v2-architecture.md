---
planted: 2026-03-09
status: SEED — DLC
phase-relevance: Phase 6+ (Community, Activity Logging)
blocks: nothing currently — real-world activity layer
depends-on: scl-directory.md, seeds/heros-almanac-v8-architecture.md
connects-to: seeds/digital-city-architecture.md, seeds/experience-layer-blueprint.md
legacy-sources: THE OUTSIDE SYSTEM v0.4.pdf
---

# The Outside System v2 — Real-World Activity Logging

## Thesis

Real-world activities — hikes, hotel bodyweight sessions, sport participation, recreational movement, manual labor — get SCL-encoded as zip-code entries in the user's training history via the envelope stamper (`envelope_stamper.py`). The user describes what they did in plain language. The system finds the nearest zip-code match using cosine similarity against the 1,680 weight vectors. The activity is logged at that address.

This bridges the gap between structured gym training and everything else a body does. The personal weight vector (see `seeds/heros-almanac-v8-architecture.md`) evolves from ALL movement, not just prescribed workouts.

## Open Questions

- **Rotation engine interaction:** Does an outdoor activity "use" a rotation engine session slot, or does it sit alongside the rotation as supplemental data? If it uses a slot, the rotation engine needs to detect real-world entries and adjust the next suggestion. If it sits alongside, it still adjusts the personal vector but doesn't consume the daily zip.

- **SCL encoding fidelity:** How accurately can unstructured activity map to a 4-dial zip code? A trail run has a clear ➖ Ultra match. A pickup basketball game might split across multiple Types. Does the system assign one zip or multiple partial-weight entries?

- **Input mechanism:** Free text? Voice? Structured form with dropdown selectors? The Wilson voice layer (`seeds/wilson-voice-identity.md`) could handle natural language parsing. The voice parser (`seeds/voice-parser-architecture.md`) already has keyword-to-zip resolution logic.

- **Verification and trust:** Self-reported activity has no verification. The system should trust the user by default (consistent with the data ethics position in `seeds/data-ethics-architecture.md`). Over-reporting inflates the personal vector; under-reporting starves it. The system is self-correcting — inflated vectors produce poor recommendations, which users self-correct by answering more honestly.

- **r/outside legacy:** The original Outside System (v0.4) was a standalone real-world activity gamification layer. In v2, it is not standalone — it is a data input channel into the existing SCL bus. The gamification framing is dropped. The vector math framing replaces it.

---

🧮
