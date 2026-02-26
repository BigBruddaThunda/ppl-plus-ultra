# User Context Layer

What a user brings to any given zip code.

Three data structures, each serving a distinct function:

1. **Exercise Ledger** — The raw log. One row per exercise per logged workout. Tagged with zip code context. The source of truth for all user data.

2. **Exercise Profile** — Derived from the ledger. Estimated 1RM, trend, history by order and color, last-seen date. The computed summary the engine uses for prescriptions.

3. **Toggle System** — The filter layer. Exercises, equipment tiers, movement patterns, and Types can be toggled off. Toggles are non-destructive: the exercise stays in the library, the weight becomes -8, the selection engine excludes it.

No user data informs the SCL rules. The rules are static. User context shapes which exercises the engine selects and what prescription the engine returns — not what the zip code means.

## Files

- `exercise-ledger-spec.md` — Table design and logging format
- `exercise-profile-spec.md` — Derived stats computation
- `toggle-system-spec.md` — Four toggle types and their effects
- `cross-context-translation.md` — How performance translates between zip codes

🧮
