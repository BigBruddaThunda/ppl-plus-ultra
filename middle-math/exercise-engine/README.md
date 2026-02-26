# Exercise Selection Engine

The procedural pipeline that fills template roles with specific exercises based on zip code constraints and user context.

## What This Solves

Static card generation names specific exercises. One user, one exercise per role. The procedural engine separates the role from the exercise: the template defines what kind of movement goes here (movement pattern, compound/isolation, bilateral/unilateral, block position), and the engine selects the best match for the specific user in the specific context.

Two users at the same zip code on the same day get different exercises based on their ledger history, equipment access, and toggles. The zip code's weight vector ranks all valid candidates. The user's context filters and re-ranks. The top result fills the role.

## Relationship to Existing Cards

Fully-specified workout cards (the current format — named exercises throughout) remain valid. The template format is an evolution, not a replacement. The engine handles both:

- Fully-specified card: engine returns the named exercise directly (user context may adjust prescription but not selection)
- Template card: engine runs the full selection pipeline and fills each role dynamically

During Phase 2 (card generation), all new cards are fully-specified. The template format will be phased in as Phase 3 validation and Phase 4/5 infrastructure come online.

## Files

- `selection-algorithm.md` — The 6-step query → rank → select pipeline with pseudocode
- `family-trees.md` — Movement family hierarchies with transfer ratios (DRAFT)
- `transfer-ratios.md` — How performance projects across exercises within a family (DRAFT)
- `substitution-rules.md` — How the system replaces toggled-off exercises
- `template-spec.md` — How master cards define roles, not exercises

🧮
