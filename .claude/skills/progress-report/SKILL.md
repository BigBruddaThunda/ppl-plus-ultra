---
name: progress-report
description: Run the progress report script and display the Ppl± generation dashboard.
allowed-tools: Bash
---

Run the progress report:

```bash
python scripts/progress-report.py
```

Display the results.

If there are any anomalies (deck with partial progress, unexpected counts, totals that don't add up), flag them explicitly.

Expected state reference:
- Total cards in system: 1,680
- Completed decks as of last known state: Deck 07 (⛽🏛) and Deck 08 (⛽🔨)
- Active generation phase: Phase 2

If the script is not found, report:
"Progress report script not found — run infrastructure sprint first."
