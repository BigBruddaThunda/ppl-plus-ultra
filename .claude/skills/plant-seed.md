# Skill: Plant a New Seed

## When to Use
When Jake provides a new architectural idea that needs to be recorded as a seed file.

## Steps

1. Create a new file at `seeds/[seed-name].md`
2. Use this frontmatter template:
```
planted: [TODAY'S DATE]
status: SEED
phase-relevance: [determine from context]
blocks: [what this does NOT block]
depends-on: [related files, if any]
connects-to: [related seeds, if any]
```
3. Write the seed body with these sections:
   - **One Sentence** — single sentence summary
   - **The Concept** — full description
   - **Architectural Implications** — how it connects to existing systems
   - **Open Questions** — at least 2-3 unresolved questions
4. Update `seeds/README.md` — add the new entry to the Planted Seeds table
5. Update the Phase Relevance Map in `seeds/README.md` if the new seed affects phase planning
6. Commit with message: `feat: plant seed — [seed-name]`

## Do NOT
- Promote seeds to active work without explicit instruction
- Modify existing seeds while planting new ones
- Add seeds to whiteboard.md (seeds live in seeds/)
