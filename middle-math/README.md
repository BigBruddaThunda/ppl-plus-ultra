# 🧮 Middle-Math — PPL± Computation Engine

The deterministic bridge between the SCL architecture and the rendered user experience.

## What This Is

Middle-math is the computation layer where:
- 61 SCL emojis become weighted values at each zip code address
- Exercise selection resolves procedurally from templates, not AI generation
- User history translates between zip code contexts via system weights
- The rotation engine produces deterministic daily zip codes
- UI rendering (color, typography, tone) derives from zip code weight vectors
- Operis editorial decisions derive from the daily weight profile

## What This Is Not

- Not workout content (that lives in `cards/`)
- Not SCL rules (that lives in `scl-directory.md`)
- Not exercise data (that lives in `exercise-library.md`)
- Not editorial content (that lives in `operis-editions/`)
- Not user-facing features (those live in `seeds/` for future phases)

Middle-math is pure logic. Rules expressed as computable weights. Algorithms expressed as specifications. The math that makes the building think.

## Directory Structure

```
weights/           — The 61-emoji weight system (-8 to +8 octave scale)
exercise-engine/   — Procedural exercise selection pipeline
user-context/      — User data layer (ledger, profiles, toggles)
rotation/          — Date → zip code deterministic engine
rendering/         — How weights become visual and editorial output
roots/             — Hero's Almanac primitives preserved as system math
schemas/           — Database table definitions for the computation layer
```

## Relationship to Other Directories

- `scl-directory.md` defines the rules → `middle-math/weights/` makes them computable
- `exercise-library.md` lists the exercises → `middle-math/exercise-engine/` selects from them
- `cards/` holds master templates → `middle-math/exercise-engine/` fills the roles
- `seeds/` describes future features → `middle-math/` provides the engine underneath
- `operis-editions/` holds published content → `middle-math/rendering/` shapes the editorial weights
- `scl-deep/` holds deep specifications → `middle-math/roots/` holds the math primitives derived from the Almanac system

## Status

Phase: Architecture planted. Weight declarations in first-draft for Orders.
Remaining categories (Axes, Types, Colors, Blocks, Operators) are stubbed.

The middle-math layer does not block card generation. It is infrastructure
for the procedural workout engine that will eventually render workouts
from templates + user context instead of static card content.

Current card generation (fully-specified workout cards) continues. The
template-based format is an evolution, not a replacement. Both formats
will coexist — existing cards remain valid, new cards can use either format.

See `ARCHITECTURE.md` for the complete system overview.

🧮
