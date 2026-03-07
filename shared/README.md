# Shared

Cross-project tools, scripts, and references used across all Archideck projects.

**Rule:** Anything in `shared/` must be project-agnostic. If a tool only works for PPL±, it lives in the PPL± scripts directory, not here.

---

## Contents

| Directory | Purpose |
|-----------|---------|
| `scl-reference/` | Full SCL specifications. The kernel is the compressed version; these are the uncompressed source documents. |

---

## Adding Shared Tools

When a script, utility, or reference document is used in two or more projects:
1. Move or copy it to the appropriate `shared/` subdirectory.
2. Update both project docs to reference the shared location.
3. Note the addition in `archideck/CONTRACTS.md` if it represents a meaningful infrastructure change.
