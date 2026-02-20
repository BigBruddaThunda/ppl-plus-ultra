---
planted: 2026-02-20
status: SEED
phase-relevance: Phase 4/5 (Design + HTML)
blocks: nothing in Phase 2-3
connects-to: seeds/art-direction.md, html/components/block-column.html
---

# Superposed Order UI — Bottom-Up Block Expansion

## One Sentence

Workout blocks stack like architectural stories and expand upward from the bottom, reversing the traditional top-down list paradigm to match the metaphor of climbing a building.

## The Concept

Classical architecture: superposed order = stacking different column types in successive vertical stories (Doric on ground, Ionic above, Corinthian on top). PPL± applies this to the workout card.

Blocks are listed bottom-to-top. ♨️ Warm-Up at the bottom (ground floor). 🚂 Junction near the top (upper story). 🧮 SAVE anchors at the very bottom as the foundation stone.

The expand toggle sits on the right thumb rail. Tapping a block pushes content upward. The user starts at the bottom and works up through the building. The card IS the building.

## Interaction Model

- **Compressed state:** full-screen mobile card showing all blocks as collapsed rows
- **Expand:** tap right-side toggle, block content pushes upward
- **Scroll:** primarily upward, matching session progression
- **🧮 SAVE:** always visible at the very bottom, the literal foundation
- **Top of card:** zip header, title, intention — the pediment, read-only

## Thumb Ergonomics

- **Right thumb rail:** structural controls — expand/collapse blocks, navigation, block toggles
- **Left thumb rail:** logging and checking — mark sets complete, log weights, check off exercises
- **Top of screen:** read-only presentation — zip code, title, intention. No reaching required.
- Designed for single-handed portrait-mode operation. Two hands = typing or multi-field entry.

## Why This Works

It reverses the assumption that content = scrolling down. A workout is a building. You climb it. The foundation is first. The capstone is last. The information reads upwards, not down. Traditional workout lists check off from top to bottom. PPL± builds from the ground up.

## Open Questions

- Does the bottom-up model create disorientation for first-time users?
- Should there be a "flip" option for users who prefer traditional top-down?
- How does the superposed model render in landscape mode?
