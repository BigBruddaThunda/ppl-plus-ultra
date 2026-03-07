# Structure

**Analysis Date:** 2026-03-07

## Directory Layout

```
ppl-plus-ultra/
│
├── CLAUDE.md                        # PPL± operating instructions (generation law)
├── scl-directory.md                 # Full SCL specification (execution authority)
├── exercise-library.md              # All valid exercises (~2,185, sections A–Q)
├── whiteboard.md                    # Active Negotiosum — current session state
├── session-log.md                   # Historical session archive
├── generation-philosophy.md         # V2 card generation philosophy
├── card-template-v2.md              # V2 card format template
│
├── archideck/                       # Meta-layer for cross-project coordination
│   ├── KERNEL.md                    # Compressed SCL seed — the language
│   ├── CONTRACTS.md                 # Negotiosum switchboard — cross-project state
│   ├── AGENT-CONTRACT.md            # Universal agent operating instructions
│   ├── CLAUDE.md                    # Archideck routing layer
│   ├── intake/                      # Raw idea landing zone (pre-Ralph Loop)
│   └── projects/                    # Non-PPL± project scaffolds
│       ├── graph-parti/
│       ├── story-engine/
│       └── civic-atlas/
│
├── cards/                           # 1,680 workout card files
│   ├── 🐂-foundation/
│   │   ├── 🏛-basics/
│   │   │   ├── 🛒-push/             # 8 cards (one per Color)
│   │   │   ├── 🪡-pull/
│   │   │   ├── 🍗-legs/
│   │   │   ├── ➕-plus/
│   │   │   └── ➖-ultra/
│   │   ├── 🔨-functional/
│   │   ├── 🌹-aesthetic/
│   │   ├── 🪐-challenge/
│   │   ├── ⌛-time/
│   │   └── 🐬-partner/
│   ├── ⛽-strength/                  # Decks 07–12 COMPLETE (240 cards)
│   ├── 🦋-hypertrophy/
│   ├── 🏟-performance/
│   ├── 🌾-full-body/
│   ├── ⚖-balance/
│   └── 🖼-restoration/
│
├── deck-identities/                 # Per-deck exercise mapping (18/42 populated)
│   ├── naming-convention.md         # Card title rules (authoritative)
│   ├── deck-01-identity.md
│   ├── deck-07-identity.md          # Pending V2 retrofit
│   ├── deck-08-identity.md          # V2 complete
│   ├── deck-09-identity.md          # V2 complete
│   └── ...
│
├── deck-cosmograms/                 # Deep research identity documents (42 decks)
│   ├── README.md
│   ├── deck-01-cosmogram.md         # V1 stub (historical)
│   ├── deck-01-cosmogram-v2.md      # V2 DRAFT (research-backed)
│   └── ... (84 files total: 42 v1 + 42 v2)
│
├── middle-math/                     # Computation engine specification
│   ├── ARCHITECTURE.md
│   ├── navigation-graph.json        # 1,680-node graph (COMPLETE)
│   ├── weight-vectors.json          # 61-dim weight vectors (COMPLETE)
│   ├── zip-registry.json            # 1,680 zip code registry
│   ├── exercise-library.json        # Parsed exercise library
│   ├── exercise-registry.json       # 2,085 globally unique exercises
│   ├── content-type-registry.json   # 109 content types × 6 axes
│   ├── design-tokens.json           # 8 Colors × 7 Orders design tokens
│   ├── exercise-engine/             # Substitution, family trees, sport tags
│   ├── rendering/                   # UI weight derivation, Operis scoring
│   ├── roots/                       # Almanac archive, octave logic
│   ├── rotation/                    # Fatigue model, junction algorithm
│   ├── schemas/                     # Database schema specs (Supabase target)
│   ├── user-context/                # User ledger, profile, toggle specs
│   └── weights/                     # Order/Axis/Type/Color/Block weight docs
│
├── seeds/                           # 51 architectural seed documents
│   ├── operis-*.md                  # Operis editorial pipeline (10 files)
│   ├── experience-layer-blueprint.md
│   ├── platform-architecture-v2.md
│   ├── mobile-ui-architecture.md
│   ├── voice-parser-architecture.md
│   ├── data-ethics-architecture.md
│   └── ... (all future-phase architecture)
│
├── scl-deep/                        # Deep specification layer
│   ├── color-context-vernacular.md
│   ├── order-parameters.md
│   ├── axis-specifications.md
│   ├── vocabulary-standard.md
│   ├── publication-standard.md
│   ├── systems-glossary.md
│   └── ... (stub files for blocks, operators, types)
│
├── operis-editions/                 # Daily editorial records
│   ├── historical-events/           # 366 date stubs (MM-DD.md, currently empty)
│   └── [YYYY]/[MM]/[YYYY-MM-DD].md  # Published editions
│
├── zip-web/                         # Zip-web pod navigation scaffolds
│   └── deck-07/                     # Populated; 41 decks as stubs
│
├── scripts/                         # Validation and automation tools
│   ├── validate-card.py             # Single-card SCL validator
│   ├── validate-deck.sh             # Deck-level batch validator
│   ├── progress-report.py           # Generation progress dashboard
│   ├── audit-exercise-coverage.py   # Duplicate primary exercise checker
│   ├── inventory.py                 # Deck and card inventory sweep
│   ├── deck-readiness.py            # Deck generation readiness check
│   ├── exercise-usage-report.py     # Exercise coverage across cards
│   ├── deck-identity-scaffold.py    # Deck identity document generator
│   ├── middle-math/                 # Middle-math computation scripts
│   │   ├── zip_converter.py         # Emoji ↔ numeric zip conversion
│   │   ├── zip_registry.py          # 1,680-entry registry builder
│   │   └── parse_exercise_library.py
│   └── operis/
│       └── scaffold_historical_events.py  # 366-date stub scaffolder
│
├── docs/                            # GitHub Pages dashboard
│   └── dashboard/
│       └── data/
│           └── progress.json        # Progress data (written by progress-report.py)
│
├── html/                            # Experience layer scaffold (Phase 4/5)
│   └── README.md                   # Scaffold only, non-functional
│
├── .planning/                       # GSD project planning (created this session)
│   └── codebase/                    # Codebase map documents
│       ├── STACK.md
│       ├── ARCHITECTURE.md
│       ├── CONVENTIONS.md
│       ├── TESTING.md
│       ├── INTEGRATIONS.md
│       ├── CONCERNS.md
│       └── STRUCTURE.md             # This file
│
├── .claude/                         # Claude Code configuration
│   ├── CLAUDE.md                    # Global Claude settings
│   ├── commands/gsd/                # 32 GSD slash commands
│   ├── get-shit-done/               # GSD framework (bin, workflows, references, templates)
│   ├── hooks/                       # PostToolUse and SessionStart hooks
│   ├── skills/                      # Multi-step skill workflows
│   │   ├── generate-card/
│   │   ├── build-deck-identity/
│   │   ├── progress-report/
│   │   └── retrofit-deck/
│   └── agents/                      # Subagent definitions
│
├── .codex/                          # Codex agent configuration (mirrors .claude/)
│
└── .github/                         # GitHub Actions CI (scaffold, not built)
    └── workflows/
```

## Key Locations

| What | Where |
|------|-------|
| Generation rules | `CLAUDE.md` (root) |
| Full SCL spec | `scl-directory.md` |
| Exercise authority | `exercise-library.md` |
| Active task board | `whiteboard.md` |
| Cross-project state | `archideck/CONTRACTS.md` |
| SCL language kernel | `archideck/KERNEL.md` |
| Card stub files | `cards/[order]/[axis]/[type]/[zip]±.md` |
| Complete card files | `cards/[order]/[axis]/[type]/[zip]±[op] [Title].md` |
| Deck identity docs | `deck-identities/deck-[XX]-identity.md` |
| Deck cosmograms | `deck-cosmograms/deck-[XX]-cosmogram-v2.md` |
| Navigation graph | `middle-math/navigation-graph.json` |
| Weight vectors | `middle-math/weight-vectors.json` |
| Card validator | `scripts/validate-card.py` |
| Progress dashboard | `scripts/progress-report.py` |
| GSD commands | `.claude/commands/gsd/[command].md` |
| Card generation skill | `.claude/skills/generate-card/SKILL.md` |
| Naming convention | `deck-identities/naming-convention.md` |

## Naming Conventions

### Card Files
- **Stub:** `[zip]±.md` — e.g., `⛽🏛🪡🔵±.md`
- **Complete:** `[zip]±[operator] [Title].md` — e.g., `⛽🏛🪡🔵±🤌 Bent-Over Barbell Row — Back Strength Log.md`
- The `±` is the semantic hinge: machine-readable left, human-readable right
- Title format: `[Movement/Equipment] — [Muscle/Focus, Context]` (phone-book style)
- No "The" prefix. No banned words: Protocol, Prescription, System, Routine, Playground, Full Send

### Deck Identity Files
- Pattern: `deck-identities/deck-[NN]-identity.md` (zero-padded two digits)

### Deck Cosmogram Files
- V1 (stub): `deck-cosmograms/deck-[NN]-cosmogram.md`
- V2 (active): `deck-cosmograms/deck-[NN]-cosmogram-v2.md`

### Milestone Context Files (GSD)
- Pattern: `.planning/milestones/M[N]-CONTEXT.md`

### Operis Edition Files
- Pattern: `operis-editions/[YYYY]/[MM]/[YYYY-MM-DD].md`

### Historical Event Stubs
- Pattern: `operis-editions/historical-events/[MM-DD].md` (366 files total)

### Script Output
- `docs/dashboard/data/progress.json` — written by `progress-report.py`

## Zip Code → File Path Derivation

Given zip `⛽🏛🪡🔵`:
1. Order emoji → folder name: `⛽-strength`
2. Axis emoji → folder name: `🏛-basics`
3. Type emoji → folder name: `🪡-pull`
4. Full path: `cards/⛽-strength/🏛-basics/🪡-pull/[filename].md`

Numeric alias: Order=2, Axis=1, Type=2, Color=3 → `2123`
Deck derivation: `(2-1) * 6 + 1 = 7` → Deck 07

---

*Structure analysis: 2026-03-07*
