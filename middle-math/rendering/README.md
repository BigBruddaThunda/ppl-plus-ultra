# Rendering Layer

How the 61-weight vector becomes what the user sees.

The weight system is not only an exercise selection mechanism. Every weight in the vector has a downstream rendering implication: a color palette shift, a typographic choice, a tonal register adjustment, a layout density change.

The zip code is a complete rendering instruction. ORDER AXIS TYPE COLOR contains enough information to derive the visual character of the workout before any exercise is named.

## What Rendering Does Not Do

Rendering does not invent visual decisions. It derives them from weights that already exist. The same SCL rules that exclude certain exercises at certain addresses also inform the palette at that address. The constraint system extends all the way to the screen.

## Status

All rendering specification files are SEED-LEVEL. They define the interface between the middle-math computation layer and the Phase 4/5 design system. They specify what inputs go in and what outputs come out — without implementing the visual design itself.

The design system (typography choices, specific color hex values, motion specs) lives in Phase 4/5 work and the art direction seeds. Rendering specs here are the mathematical bridge to that work.

## Files

- `ui-weight-derivation.md` — Zip code weight vector → UI color, typography, tone, layout, background (SEED-LEVEL)
- `operis-weight-derivation.md` — Daily zip code weights → Operis editorial decisions (SEED-LEVEL)
- `progressive-disclosure.md` — Floor stack weight response (SEED-LEVEL)

🧮
