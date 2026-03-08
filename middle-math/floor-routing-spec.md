# Floor Routing Specification
## CX-22 — Content Types → Axis Floors

All 109 Ppl± content types mapped to their primary Axis floor, secondary floors,
cross-floor rules, and default landing behavior.

**Source:** `middle-math/content-type-registry.json`
**Unblocks:** CX-29 (Navigation Graph)

---

## Floor Map

The Ppl± building has 6 floors, one per Axis. Following the piano nobile principle
from `seeds/elevator-architecture.md`, 🏛 Basics is the principal floor — the main
entry point for all users.

| Floor Label | Axis | Axis Name | Character |
|-------------|------|-----------|-----------|
| Piano Nobile | 🏛 | Firmitas | Primary arrival floor. Workout cards, Operis, SCL reference. |
| Ground Floor | 🔨 | Utilitas | Tools, utilities, scripts, infrastructure, exercise library. |
| 2nd Floor | ⌛ | Temporitas | Calendar context, archives, history, seasonal and time data. |
| 3rd Floor | 🐬 | Sociatas | Community, partner content, coaching, social interactions. |
| 4th Floor | 🌹 | Venustas | Personal history, progress, saved rooms, logs, aesthetics. |
| 5th Floor | 🪐 | Gravitas | Deep architecture, cosmograms, seeds, research documents. |

---

## Routing Rules

### Default Landing Behavior

New users land on **Piano Nobile** (🏛). The elevator opens there.
Returning users land on their **last-visited floor** (restored from session context).
Deep links (`/zip/2123`, `/floor/functional`) route directly to the specified floor.
Unauthenticated users can browse Piano Nobile and Ground Floor. All other floors
require account creation (free).

### Adjacency Rule

Content may appear on adjacent floors only when the cross-floor appearance is
explicitly declared in the registry. Adjacency does not cascade: if CT-001 appears
on 🏛 and 🌹, it does NOT automatically appear on 🪐 or ⌛.

### Conditional Cross-Floor Rule

Content appears on secondary floors only when it has been contextually activated:
- A Workout Card (CT-001) appears on 🌹 only when the user has logged a session there.
- A Publication Standard (CT-076) appears on 🔨 (tools) AND 🪐 (deep reference).
- A Deck Cosmogram (CT-003) appears on 🪐 when opened in research context.

---

## Routing Table — All 109 Content Types

| ID | Name | Primary Floor | Axis | Secondary Floors | Default Landing | Depth Level |
|----|------|--------------|------|-----------------|----------------|-------------|
| CT-001 | The Workout Card | Piano Nobile | 🏛 | 🌹 (when logged) | `/zip/{code}` | trivium |
| CT-002 | The Operis Edition | Piano Nobile | 🏛 | — | `/operis/{date}` | trivium |
| CT-003 | The Deck Cosmogram | Piano Nobile | 🏛 | 🪐 (research context) | `/deck/{n}/cosmogram` | quadrivium |
| CT-004 | The Deck Identity | Piano Nobile | 🏛 | — | `/deck/{n}/identity` | trivium |
| CT-005 | The Zip Code Address | Piano Nobile | 🏛 | — | `/zip/{code}` | trivium |
| CT-006 | The Operator Definition | Piano Nobile | 🏛 | — | `/reference/operators/{op}` | trivium |
| CT-007 | The Block Definition | Piano Nobile | 🏛 | — | `/reference/blocks/{block}` | trivium |
| CT-008 | The Order Profile | Piano Nobile | 🏛 | — | `/reference/orders/{order}` | trivium |
| CT-009 | The Axis Profile | Piano Nobile | 🏛 | — | `/reference/axes/{axis}` | trivium |
| CT-010 | The Type Profile | Piano Nobile | 🏛 | — | `/reference/types/{type}` | trivium |
| CT-011 | The Color Profile | Piano Nobile | 🏛 | — | `/reference/colors/{color}` | trivium |
| CT-012 | The Deck Campaign Status | Piano Nobile | 🏛 | — | `/deck/{n}/status` | trivium |
| CT-013 | The Generation Log | Piano Nobile | 🏛 | — | `/admin/logs/generation` | trivium |
| CT-014 | The Validation Report | Piano Nobile | 🏛 | — | `/admin/logs/validation` | trivium |
| CT-015 | The Audit Report | Piano Nobile | 🏛 | — | `/admin/logs/audit` | trivium |
| CT-016 | The Progress Dashboard | Piano Nobile | 🏛 | — | `/admin/dashboard` | trivium |
| CT-017 | The CLAUDE.md | Piano Nobile | 🏛 | — | (agent-internal; no public route) | quadrivium |
| CT-018 | The Whiteboard | Piano Nobile | 🏛 | — | (agent-internal; no public route) | trivium |
| CT-019 | The README | Piano Nobile | 🏛 | — | `/about` | trivium |
| CT-020 | The Exercise Library Entry | Ground Floor | 🔨 | — | `/library/exercise/{id}` | trivium |
| CT-021 | The Section Header | Ground Floor | 🔨 | — | `/library/section/{letter}` | trivium |
| CT-022 | The Zip-Web Pod | Ground Floor | 🔨 | — | `/deck/{n}/pod` | trivium |
| CT-023 | The Zip-Web Signature | Ground Floor | 🔨 | — | `/zip/{code}/signature` | trivium |
| CT-024 | The Seed Document | Ground Floor | 🔨 | — | (agent-internal; no public route) | quadrivium |
| CT-025 | The Skill Definition | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-026 | The Subagent Definition | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-027 | The Hook Configuration | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-028 | The Script | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-029 | The Ralph Loop | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-030 | The Codex Agent Definition | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-031 | The SCL Directory | Ground Floor | 🔨 | — | `/reference/scl` | quadrivium |
| CT-032 | The Exercise Library Version | Ground Floor | 🔨 | — | `/library/changelog` | trivium |
| CT-033 | The Deck Identity Template | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-034 | The Naming Convention Document | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-035 | The Frontmatter Schema | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-036 | The Linter Configuration | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-037 | The CI Workflow | Ground Floor | 🔨 | — | (agent-internal; no public route) | trivium |
| CT-038 | The Cosmogram Research Prompt | Ground Floor | 🔨 | — | (agent-internal; no public route) | quadrivium |
| CT-039 | The Publication Standard | Ground Floor | 🔨 | 🪐 (research context) | `/reference/publication-standard` | quadrivium |
| CT-040 | The Emoji Macro Reference | Ground Floor | 🔨 | — | `/reference/emoji-macros` | quadrivium |
| CT-041 | The 1RM Calculator | Ground Floor | 🔨 | — | `/tools/1rm` | trivium |
| CT-042 | The Volume Calculator | Ground Floor | 🔨 | — | `/tools/volume` | trivium |
| CT-043 | The Plate Calculator | Ground Floor | 🔨 | — | `/tools/plates` | trivium |
| CT-044 | The Rest Timer | Ground Floor | 🔨 | — | `/tools/rest-timer` | trivium |
| CT-045 | The EMOM Timer | Ground Floor | 🔨 | — | `/tools/emom` | trivium |
| CT-046 | The AMRAP Timer | Ground Floor | 🔨 | — | `/tools/amrap` | trivium |
| CT-047 | The Stopwatch | Ground Floor | 🔨 | — | `/tools/stopwatch` | trivium |
| CT-048 | The Zip Dial UI | Ground Floor | 🔨 | — | `/navigate` | trivium |
| CT-049 | The Zip Search | Ground Floor | 🔨 | — | `/search` | trivium |
| CT-050 | The Workout Log | 4th Floor | 🌹 | — | `/me/logs/{log_id}` | trivium |
| CT-051 | The Set Log | 4th Floor | 🌹 | — | `/me/logs/{log_id}/sets` | trivium |
| CT-052 | The Saved Room | 4th Floor | 🌹 | — | `/me/saved` | trivium |
| CT-053 | The Collection Tag | 4th Floor | 🌹 | — | `/me/collections` | trivium |
| CT-054 | The Personal Note | 4th Floor | 🌹 | — | `/me/notes/{zip}` | trivium |
| CT-055 | The Session Rating | 4th Floor | 🌹 | — | `/me/logs/{log_id}/rating` | trivium |
| CT-056 | The Progress Photo | 4th Floor | 🌹 | — | `/me/photos` | trivium |
| CT-057 | The Trophy | 4th Floor | 🌹 | — | `/me/trophies` | trivium |
| CT-058 | The Streak Record | 4th Floor | 🌹 | — | `/me/streaks` | trivium |
| CT-059 | The Personal PR | 4th Floor | 🌹 | — | `/me/prs` | trivium |
| CT-060 | The Body Metric | 4th Floor | 🌹 | — | `/me/metrics` | trivium |
| CT-061 | The Aesthetic Goal | 4th Floor | 🌹 | — | `/me/goals` | trivium |
| CT-062 | The Room Bloom Entry | 4th Floor | 🌹 | — | `/me/bloom/{zip}` | trivium |
| CT-063 | The Custom Room Name | 4th Floor | 🌹 | — | `/me/rooms/{zip}/name` | trivium |
| CT-064 | The Program Enrollment | 4th Floor | 🌹 | — | `/me/programs` | trivium |
| CT-065 | The Program Progress Marker | 4th Floor | 🌹 | — | `/me/programs/{id}/progress` | trivium |
| CT-066 | The Personal Almanac | 4th Floor | 🌹 | — | `/me/almanac` | trivium |
| CT-067 | The Before/After Pair | 4th Floor | 🌹 | — | `/me/photos/compare` | trivium |
| CT-068 | The Training Volume Summary | 4th Floor | 🌹 | — | `/me/volume` | trivium |
| CT-069 | The Preferred Zip List | 4th Floor | 🌹 | — | `/me/preferred` | trivium |
| CT-070 | The Cosmogram Body | 5th Floor | 🪐 | — | `/deck/{n}/cosmogram/body` | quadrivium |
| CT-071 | The Cosmogram Annotation | 5th Floor | 🪐 | — | `/deck/{n}/cosmogram/annotations` | quadrivium |
| CT-072 | The Emoji Macro Entry | 5th Floor | 🪐 | — | `/reference/emoji/{emoji}` | quadrivium |
| CT-073 | The Order Science Document | 5th Floor | 🪐 | — | `/reference/scl-deep/orders` | quadrivium |
| CT-074 | The Axis Specification | 5th Floor | 🪐 | — | `/reference/scl-deep/axes` | quadrivium |
| CT-075 | The Color Context Entry | 5th Floor | 🪐 | — | `/reference/scl-deep/colors` | quadrivium |
| CT-076 | The Publication Standard | 5th Floor | 🪐 | 🔨 (tools context) | `/reference/publication-standard` | quadrivium |
| CT-077 | The Platform Architecture Document | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-078 | The Elevator Architecture Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-079 | The Operis Architecture Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-080 | The Default Rotation Engine Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-081 | The Almanac Macro Operators Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-082 | The Axis-as-App-Floors Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-083 | The Junction Community Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-084 | The Room Bloom Seed | 5th Floor | 🪐 | — | (agent-internal; no public route) | quadrivium |
| CT-085 | The Operis Edition Archive | 2nd Floor | ⌛ | — | `/archive/{year}/{month}` | trivium |
| CT-086 | The Season Report | 2nd Floor | ⌛ | — | `/calendar/seasons` | trivium |
| CT-087 | The Monthly Operator Summary | 2nd Floor | ⌛ | — | `/calendar/month/{month}` | trivium |
| CT-088 | The Weekly Cadence Display | 2nd Floor | ⌛ | — | `/calendar/week/{iso_week}` | trivium |
| CT-089 | The Training History View | 2nd Floor | ⌛ | — | `/me/history` | trivium |
| CT-090 | The Equinox/Solstice Notice | 2nd Floor | ⌛ | — | `/calendar/equinox` | trivium |
| CT-091 | The Moon Phase Display | 2nd Floor | ⌛ | — | `/calendar/moon` | trivium |
| CT-092 | The Historical Events Database Entry | 2nd Floor | ⌛ | — | `/almanac/{date}` | trivium |
| CT-093 | The Astronomical Data Feed | 2nd Floor | ⌛ | — | `/calendar/astronomy` | trivium |
| CT-094 | The Cultural Calendar Entry | 2nd Floor | ⌛ | — | `/calendar/cultural/{date}` | trivium |
| CT-095 | The Program Week View | 2nd Floor | ⌛ | — | `/me/programs/{id}/week/{n}` | trivium |
| CT-096 | The Seasonal Guide | 2nd Floor | ⌛ | — | `/calendar/seasonal` | trivium |
| CT-097 | The Training Age Estimate | 2nd Floor | ⌛ | — | `/me/training-age` | trivium |
| CT-098 | The Room Thread | 3rd Floor | 🐬 | — | `/community/zip/{code}/thread` | trivium |
| CT-099 | The Thread Post | 3rd Floor | 🐬 | — | `/community/zip/{code}/thread/{id}` | trivium |
| CT-100 | The Forum Channel | 3rd Floor | 🐬 | — | `/community/channels` | trivium |
| CT-101 | The Forum Post | 3rd Floor | 🐬 | — | `/community/posts/{id}` | trivium |
| CT-102 | The Forum Comment | 3rd Floor | 🐬 | — | `/community/posts/{id}/comments` | trivium |
| CT-103 | The Direct Message | 3rd Floor | 🐬 | — | `/community/messages` | trivium |
| CT-104 | The Coaching Note | 3rd Floor | 🐬 | — | `/community/coaching/{user_id}` | trivium |
| CT-105 | The Form Video | 3rd Floor | 🐬 | — | `/community/zip/{code}/videos` | trivium |
| CT-106 | The Station Rotation Prompt | 3rd Floor | 🐬 | — | `/community/zip/{code}/rotation` | trivium |
| CT-107 | The Partner Workout Agreement | 3rd Floor | 🐬 | — | `/community/agreements/{id}` | trivium |
| CT-108 | The Community Milestone | 3rd Floor | 🐬 | — | `/community/milestones` | trivium |
| CT-109 | The Coaching Program Template | 3rd Floor | 🐬 | — | `/community/programs/{id}` | quadrivium |

---

## Access Gate Summary

| Floor | Auth Required | Tier Required | Notes |
|-------|--------------|--------------|-------|
| Piano Nobile (🏛) | No (read-only) | Free | Workout cards and Operis front page visible to all |
| Ground Floor (🔨) | No (read-only) | Free | Exercise library and tools visible to all |
| 2nd Floor (⌛) | Yes (account) | Free | Calendar and history require account |
| 3rd Floor (🐬) | Yes (account) | Tier 1 ($10) | Community requires subscription |
| 4th Floor (🌹) | Yes (account) | Free | Personal history requires account |
| 5th Floor (🪐) | No (read-only) | Free | Deep reference visible to all |

---

## Agent-Internal Content

The following content types are operational tooling with no public-facing route.
They live in the agent's operating context (CLAUDE.md, whiteboard.md, scripts/, seeds/).

| IDs | Category |
|-----|----------|
| CT-017, CT-018 | Project memory (CLAUDE.md, Whiteboard) |
| CT-024–CT-030, CT-033–CT-038 | Agent tools, skill definitions, hooks, scripts, templates |
| CT-077–CT-084 | Architecture seeds (not published; inform design only) |
