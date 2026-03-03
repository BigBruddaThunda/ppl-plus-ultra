# PPL± Operis — Historical Events Database

This directory will contain 365 files, one per calendar day, providing the pre-built historical events pool for the Operis Researcher prompt (Prompt 1).

---

## File Convention

Path: `operis-editions/historical-events/[MM-DD].md`

Files are date-indexed with month and day only — no year. They are reused annually. February 29 is included for leap years (366 files total when complete).

Example: `operis-editions/historical-events/03-03.md` contains historical events for March 3rd of any year.

---

## File Format

Each file contains 5–15 historical events for that calendar day, formatted as:

```markdown
Historical Events — [Month Day]

[Event Title]
- Year: [YYYY]
- Detail: [3–5 sentences of factual detail. Names, places, specific numbers.]
- Domain: [Architecture/Agriculture/Sport/Medicine/Civic/Education/Astronomy/Music/Labor/Exploration/Engineering]
- Source: [URL]
- Body connection: [One sentence or "No direct body connection."]

[Event Title]
[same format, repeat for all events]
```

---

## How Prompt 1 Uses This Directory

Prompt 1 (the Researcher) checks for a file at this path before doing web research for Beat 1 (Historical Events). If the file exists, Prompt 1 loads its events as the starting pool and may supplement with web research to verify, update, or find additional events. If the file does not exist, Prompt 1 proceeds with full web research.

As the Operis runs, each Prompt 1 execution is an opportunity to contribute events to this database. Events verified through web research can be saved here for future reuse, reducing research time as the database populates.

---

## Status

EMPTY — directory planted, no files populated yet.

Estimated build effort: approximately 180 hours of research for the full 366-file database. This will populate incrementally as the Operis pipeline operates.

---

## Domain Priority

Events are prioritized from these domains: architecture and construction, agriculture and food systems, sport and physical culture, medicine and anatomy, civic infrastructure, education, astronomy, music, labor history, exploration, engineering. Celebrity births/deaths, purely political events, and pop culture milestones are deprioritized unless they connect directly to the body, architecture, or physical culture.

---

## Quality Standard

Each event should have enough factual substance to support a 200–500 word newspaper feature article. If the event can only be described in one sentence, it is too thin for this database.
