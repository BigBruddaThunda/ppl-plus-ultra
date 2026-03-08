# Ppl± Audit Reports

Auto-generated audit snapshots. Do not edit manually — regenerate using the scripts below.

## Contents

| File | Script | Description |
|------|--------|-------------|
| `deck-readiness-YYYY-MM-DD.md` | `python scripts/deck-readiness.py` | Deck generation readiness matrix — cosmograms, identities, generated/empty/canonical counts |
| `exercise-usage-YYYY-MM-DD.md` | `python scripts/exercise-usage-report.py` | Exercise coverage across generated cards — usage counts, duplicates, gaps |

## Regenerate

```bash
python scripts/deck-readiness.py > reports/deck-readiness-$(date +%Y-%m-%d).md
python scripts/exercise-usage-report.py > reports/exercise-usage-$(date +%Y-%m-%d).md
```

## Note

Snapshots are date-stamped. Old snapshots are kept for comparison. The most recent file in each series is the current state.
