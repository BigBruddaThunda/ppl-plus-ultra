# SCL Reference

Full SCL specifications for cross-project use.

The kernel (`archideck/KERNEL.md`) is the compressed version — what any agent reads first.
These are the uncompressed source documents — what agents read when they need to execute, not just understand.

---

## Primary References (at repository root)

| File | Purpose |
|------|---------|
| `/scl-directory.md` | Complete 61-emoji SCL specification. All polysemic behaviors, generation rules, validation. |
| `/exercise-library.md` | All 2,085+ valid exercises for Ppl± generation. |
| `/scl-deep/` | Deep specification layer. Vocabularies, standards, uncompressed source. |

These files remain at the repository root for Ppl± compatibility. This directory will house cross-project SCL extensions as they develop — vocabulary that applies to Story Engine, Civic Atlas, or Graph Parti but doesn't belong in the Ppl±-specific root documents.

---

## Cross-Project Extensions (future)

As projects develop their own SCL vocabulary extensions, they will be documented here:

- `story-engine-types.md` — (future) Type extensions for narrative domains
- `civic-atlas-types.md` — (future) Type extensions for urban/civic domains
- `graph-parti-axes.md` — (future) Axis extensions for spatial/design domains

Extensions must be proposed via `archideck/intake/` and ratified through a kernel review session before being added here.
