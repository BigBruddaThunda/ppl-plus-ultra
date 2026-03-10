# Negotiosum — Ppl± Active Work Board

Last updated: 2026-03-10
Phase: 3.1 — Quality Rebuild Campaign + Web App Foundation
Cards: 1,680 / 1,680 (ALL 42 DECKS COMPLETE ✅ — audit score: 91.1/100, format: 100, 2,255 flags resolved)
Exercise Library: v.1.1 (2,085 exercises, 18 movement patterns, 55 scl_types corrected, 21/21 integration checks)
Web App: Next.js 16 — Wave 3 complete (auth, payments, onboarding, logging, saved rooms — all user features live)
Seeds: 49 | Scripts: 35
CX Containers: 44 defined, 40 complete, 4 open

For development history, see `session-log.md`.

---

## ⚫ Ordo Operis — Order of the Work

Teach, scaffold, define. Output that stands alone for any reader.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-00A | Systems glossary | — | scl-deep/systems-glossary.md |
| DONE | CX-02 | Historical events scaffold (366 files) | — | scripts/operis/scaffold_historical_events.py |
| DONE | CX-05 | Markdownlint configuration | — | .github/linters/.markdownlint-cli2.jsonc |
| DONE | CX-06 | Frontmatter schema + validator | — | card-frontmatter-schema.json + validator script |
| DONE | CX-01 | Codex agent task architecture | — | Governance finalized, completion summary added. Session 037. |
| DONE | CX-19 | Agent boundaries document | — | .claude/AGENT-BOUNDARIES.md — 5-agent matrix, escalation rules, Jake zones. Session 037. |
| DONE | CX-34 | Codespaces dev container | — | .devcontainer/ + docs/codespaces-quickstart.md |
| DONE | — | Update README.md project status to 102/1,680 | — | Already updated in prior Codex runs |
| DONE | — | Update README.md repo structure (new directories, files) | — | sql/, session-log.md, docs/ added |
| DONE | CX-39 | External Reference Dock | — | Session 038: `external-refs.json` (2,085 null docks) + `seeds/exrx-partnership-brief.md` |

---

## 🟢 Natura Operis — Nature of the Work

Self-contained, zero-dependency. Runs in airplane mode.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-03 | Zip converter + registry (1,680 JSON) | — | zip_converter.py, zip_registry.py, zip-registry.json |
| DONE | CX-13 | Exercise library parser (~2,185 JSON) | — | parse_exercise_library.py, exercise-library.json |
| DONE | CX-36 | Exercise Identity Registry | — | Session 038: `scripts/build-exercise-registry.py` + `middle-math/exercise-registry.json` (2,085 entries, EX-0001–EX-2085) |
| DONE | — | Fix compile-abacus.py: natural sorting + DLC packs | — | Removed force-assignment, 12 DLC packs from ~89 free-agent zips, --report flag, 100% coverage |
| OPEN | CX-17 | Ralph Loop validation + batch orchestrator | CX-03 ✓ | validate-pod.py, ralph-batch.sh |
| OPEN | — | Deck 07 Ralph pod review (prototype approval) | — | Jake must review deck-07-pods.md before batch |

---

## 🔵 Architectura Operis — Architecture of the Work

Systematic, templated, institutional. Follow the pattern.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-04 | Inventory + progress truth tables | — | inventory.py, deck-readiness.py, exercise-usage-report.py |
| DONE | CX-07 | CI lint workflow | — | .github/workflows/lint.yml |
| DONE | CX-08 | SQL schema materialization (7 migrations) | — | sql/001-007 + README — Session 033 |
| DONE | CX-16 | Deck identity scaffolds (Decks 10–12) | CX-03 ✓ | PR #67 — deck-identity-scaffold.py + 3 identity docs |
| DONE | — | Deck identity scaffolds (Decks 01–06) | CX-03 ✓ | Session 039 |
| DONE | CX-33 | GitHub Pages progress dashboard | CX-03 ✓, CX-04 ✓ | Built PR #90 (2026-03-05) — docs/dashboard/ + scripts/build-dashboard-data.py. Reconciled this session. |
| DONE | CX-40 | Exercise Registry SQL Migration | — | Session 038: `sql/009-exercise-registry.sql`, `sql/010-exercise-knowledge.sql`, `sql/README.md` updated |
| DONE | — | Deck 07 retrofit regen queue (18 cards) | — | DONE — Deck 07 debt cleared, all 40 cards meet V2 standard. |
| OPEN | — | Operis Contract A/B URL enforcement | — | P1 missing source URLs, P2 missing per-lane URLs |
| OPEN | — | Re-run Operis V4 pipeline test (2024-07-26) | Contract A/B fix | After URL/schema patching |
| DONE | — | Next.js 16 web app initialized | — | web/ — React 19.2, Tailwind 4, Framer Motion 12, Zustand 5, TypeScript 5 |
| DONE | — | City Compiler batch compilation | — | middle-math/compiled/ → 1,680 zip JSONs + 42 deck JSONs + 35 abacus JSONs |
| DONE | — | SCL TypeScript parser (scl.ts) | — | 61 emoji mappings, zip↔numeric conversion, operator derivation, polarity detection |
| DONE | — | Design token system | — | tokens.ts (8 Color palettes) + design-system.ts (7 Order D-module proportions) |
| DONE | — | App routing scaffold | — | /zip/[code], /deck/[number], /operis/[date], /tools, /login, /signup, /subscribe, /me |
| DONE | — | Room rendering pipeline | — | .md → compiled JSON → 4-floor room (time, community, deep, personal) |
| DONE | — | Rotation engine (rotation.ts) | — | Deterministic daily zip: Order×weekday, Type×rolling-5-day, Axis×month, Color×week-mod-8 |
| DONE | — | API resolve endpoint | — | /api/resolve/[zip] — GET → compiled JSON, 4-digit validation, aggressive caching |
| DONE | — | Auth UI scaffolding | — | /login, /signup, /me, /subscribe pages + Supabase stubs + zustand auth store + PaywallGate |
| DONE | — | Session 0: Supabase + Stripe config | — | .env.local with 8 keys, profiles table + RLS + trigger, Stripe test products created |
| DONE | — | Session D: Supabase auth wiring | — | signup, login, logout, session middleware, auth callback, /me shows user + tier |
| DONE | — | Session F: Stripe subscriptions | — | Checkout → Stripe → verify → tier update. Library Card ($10) + Community Pass ($25). Webhook handler built. |
| DONE | — | Homepage with Operis awareness | — | TodayHero + WeekStrip + month context + Order picker + navigation links |
| DONE | — | Navigation components | — | Breadcrumb, HomeButton, ZipDial, DialPanel, CardSkeleton, loading/error states |
| DONE | — | Session E: Onboarding flow | — | 3-step wizard (equipment/region/summary), /me/settings, signup→onboarding redirect, sql/011 migration |
| DONE | — | Session G: Workout logging | — | LogOverlay on exercise lines, set_logs + workout_sessions tables, SessionSummary, /me/history |
| DONE | — | Session H: Saved rooms + library | — | SaveRoomButton, TrackVisit, VisitCount, /me/library with random picker, zip_visits table |
| DONE | — | Session C-2: Voice parser | — | 3-layer keyword scoring (160+ keywords), VoiceInput with Web Speech API, auto-route on high confidence, on homepage |
| DONE | — | Session M: Data export + deletion | — | GET /api/user/export, DELETE /api/user/delete with Stripe cancel + cascade, confirmation typing, on /me/settings |
| OPEN | — | Session K: Pinch-zoom canvas | — | Zoom levels: 1x normal, 0.5x block chips, 0.25x deck map. @use-gesture/react installed. |
| OPEN | — | Session L: Community floor | Jake moderation decisions | Supabase Realtime, community_posts/replies tables, Tier 2 gating |
| OPEN | CX-44 | Build Sequence V2 — multi-agent workflow contracts | — | `seeds/claude-code-build-sequence-v2.md` — 20 sessions, 5 waves, 3 Jake sessions, supersedes V1 |

---

## 🟣 Profundum Operis — The Deep Work

Precision, multi-file reasoning, cascading consequences.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-09 | Axis weight declarations (6 Axes) | CX-00A ✓ | DRAFT — all 6 axes populated, PR #64 |
| DONE | CX-10 | Type + Color weight declarations (5+8) | CX-00A ✓ | DRAFT — type-weights.md + color-weights.md, PR #65 |
| DONE | CX-11 | Block weight declarations (22+SAVE) | CX-09 ✓, CX-10 ✓ | DRAFT — 790-line working draft confirmed on disk |
| DONE | CX-12 | Operator weight declarations (12) | CX-09 ✓, CX-10 ✓ | DRAFT — 502-line working draft confirmed on disk |
| DONE | CX-14 | Weight vector computation engine | CX-09–12 all ✓, CX-03 ✓ | weight_vector.py + weight-vectors.json — 1,680 vectors, 61 dims, --validate passes. Session 034. |
| DONE | CX-15 | Exercise selection prototype | CX-13 ✓, CX-14 ✓ | exercise_selector.py — GOLD gate, load ceiling, tier, --validate, --stats. Sprint 035. |
| DONE | CX-18 | Design tokens + WeightCSS spec | — | middle-math/design-tokens.json + middle-math/weight-css-spec.md. Session 037. |
| DONE | CX-20 | Room schema extension | CX-08 ✓ | sql/008-room-schema-extension.sql — 4 tables + RLS |
| DONE | CX-21 | Content type registry (109 types JSON) | CX-00A ✓ | content-type-registry.json — 109 types, 6 axes, cross-floor appearances, operator affinities. Session 034. |
| DONE | CX-22 | Floor routing spec | CX-03 ✓, CX-20 ✓, CX-21 ✓ | middle-math/floor-routing-spec.md — 109 types × 6 floors. Unblocks CX-29. Sprint 035. |
| DONE | CX-23 | Navigation graph builder (1,680 × 4 edges) | CX-03 ✓, CX-04 ✓, CX-08 ✓ | middle-math/navigation-graph.json — 6,720 edges |
| DONE | CX-24 | Bloom state engine | CX-20 ✓, CX-03 ✓ | bloom_engine.py — 6 levels, no decay, eudaimonic. Sprint 035. |
| DONE | CX-25 | Vote weight integration | CX-20 ✓, CX-14 ✓ | vote_weight_adjuster.py — tanh signal, ±0.8 cap, --validate 5/5. Session 036. |
| DONE | CX-26 | Operis room manifest generator | CX-03 ✓, CX-04 ✓ | generate_room_manifest.py — 13-room Sandbox from date. Sprint 035. |
| DONE | CX-27 | Superscript/subscript data model | CX-20 ✓, CX-08 ✓ | compute_superscript.py — system suggestions + user overrides. Sprint 035. |
| DONE | CX-28 | Cosmogram content scaffold (42 stubs) | CX-04 ✓ | scaffold_cosmograms.py + 42 stubs written. Session 034. |
| DONE | CX-29 | Wilson audio route specification | CX-22 ✓ | middle-math/wilson-audio-spec.md — 3-layer scoring, ~2,260 keywords, voice registers by floor. Session 036. |
| DONE | CX-30 | Envelope schema + stamping prototype | CX-08 ✓, CX-14 ✓, CX-03 ✓ | envelope_stamper.py — atomic retrieval unit, --anonymous + --full + --deck modes. Session 036. |
| DONE | CX-31 | Envelope similarity function + retrieval | — | envelope_retrieval.py — cosine sim, Tier 1–4 profiles, --validate 5/5. Wave 5 capstone. Session 037. |
| DONE | CX-38 | Exercise Relationship Graph | — | Session 038: `family-trees.json` (15 families/2,085 members), `substitution-map.json`, `sport-tags.json`, `anatomy-index.json` |
| DONE | CX-43 | Exercise Selector V2 (registry-aware) | CX-36 ✓, CX-38 ✓, CX-15 ✓ | Session 041: selector upgraded to registry + family diversity + substitutions (`scripts/middle-math/exercise_selector.py`) |

---

## 🔴 Fervor Operis — The Heat of the Work

Maximum output, full capacity. Measure throughput.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | — | First Operis edition (2026-03-02) | — | PR #27 — operis-editions/2026/03/2026-03-02.md |
| DONE | — | Deck 07 generation (40 cards) | — | 18 flagged REGEN-NEEDED |
| DONE | — | Deck 08 generation (40 cards) | — | GENERATED-V2 complete |
| DONE | — | Deck 09 generation (40 cards) | — | 102/1,680 total |
| DONE | CX-37 | Exercise Knowledge Template + First Batch | — | Session 038: `scripts/generate-exercise-content.py` + 197 files in `exercise-content/` + `exercise-content/README.md` |
| DONE | CX-41 | Exercise Content Batch 2 (201–500) | CX-37 ✓ | Session 039: `python scripts/generate-exercise-content.py --batch 500` → +298 files (495 total in `exercise-content/`) |
| DONE | CX-42 | Exercise Content Batch 3 (501–1000) | CX-37 ✓ | Session 040: `python scripts/generate-exercise-content.py --batch 1000` → +498 files (993 total in `exercise-content/`) |
| DONE | — | Exercise Content Batch 4 (1001–1500) | CX-37 ✓ | Session 042: `python scripts/generate-exercise-content.py --batch 1500` → +493 files (1,486 total in `exercise-content/`) |
| DONE | — | Exercise Content Batch 5 FINAL (1501–2085) | CX-37 ✓ | Session 045: `python scripts/generate-exercise-content.py --batch 2085` → +599 files (2,085 total in `exercise-content/`) |
| DONE | — | Deck 07 regen (18 cards) | — | DONE — Deck 07 debt cleared — all 40 cards meet V2 standard. |
| DONE | — | Deck 10 generation (40 cards) | — | ⛽🪐 Strength Challenge complete (40/40) |
| DONE | — | Deck 11 generation (40 cards) | — | ⛽⌛ Strength Time — complete (batch gen PR #116) |
| DONE | — | Deck 12 generation (40 cards) | — | ⛽🐬 Strength Partner complete (40/40) |
| OPEN | — | Historical events population (366 dates) | CX-02 ✓ | Research-intensive — ~180 hours total, builds incrementally |
| DONE | — | All 42 decks generated (1,680/1,680) | — | 100% room coverage — PR #116 batch generation |
| DONE | — | Layer 3 quality audit script | — | scripts/audit-deck-quality.py — 6 dimensions, CSV/JSON output |
| DONE | — | Quality audit baseline report | — | reports/deck-quality-audit-2026-03-08.csv + .json — 88/100 avg |
| DONE | — | Rebuild 🟠 Circuit cards (barbell fixes) | audit-deck-quality.py | 15 Circuit + 25 Bodyweight cards: barbell→dumbbell substitution. ARAM+Sandbox already present in all cards. |
| DONE | — | Rebuild ⚪ Mindful cards (tempo cues) | audit-deck-quality.py | 180 cards: added "(4s eccentric, breath-paced)" to exercise lines missing tempo cues. |
| DONE | — | Fix audit false positives (flanking emojis) | audit-deck-quality.py | Bug: counted unique type emojis not occurrences. All 1,680 cards already correct. 1,680 false flags eliminated. |
| DONE | — | Fix exercise-registry scl_types (55 exercises) | fix-exercise-types.py | 10 explicit + 45 catch-all corrections via movement_pattern routing. Zero 5-type catch-alls remain. |
| DONE | — | Add operator calls to 260 cards | fix-card-format.py | Restoration decks 37-42 + Deck 09 half. Inline operator after first block header. |
| DONE | — | Remove barbell violations from 🟢/🟠 cards | fix-card-format.py | 40 cards fixed. FORBIDDEN_BARBELL: 34→0 flags. |
| OPEN | — | Fix Exercise-Type misroutes (1,636 flags) | rebuild-cards.py | Real generation errors: exercises in wrong card Types. Top: Kettlebell Swing (385), Jump Rope (211). Needs card rebuild. |
| OPEN | — | Fix content depth (1,320 LIGHT + 180 THIN) | rebuild-cards.py | 72.6% cards under 50 lines. Needs AI regeneration for deeper content. |
| OPEN | — | Deduplicate identical Intentions across decks | audit-deck-quality.py | Generic "Drive clean reps" in 40+ cards |

---

## 🟠 Nuntius Operis — The Messenger of the Work

Sweep, audit, report, deliver. Touch everything, miss nothing.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-00B | Systems language audit | CX-00A ✓ | scl-deep/systems-language-audit.md |
| DONE | CX-35 | Whiteboard Negotiosum validator | CX-03 ✓, CX-04 ✓ | scripts/validate-negotiosum.py |
| DONE | — | Run deck-readiness.py and commit output | — | reports/deck-readiness-2026-03-06.md committed. Session 037. |
| DONE | — | Run exercise-usage-report.py on 102 cards | — | reports/exercise-usage-2026-03-06.md committed. Session 037. |
| OPEN | — | Ralph Loop batch: populate 41 remaining deck pods | Deck 07 pod review | Blocked on Jake approval of prototype |
| DONE | — | Exercise library version bump to v.1 | — | v.1: 18 patterns, 1,163 reclassified, card index (99.2%), 21/21 integration |
| DONE | — | Audit pipeline: audit-deck-quality.py | — | Layer 3 quality scorer — Color, Type, Params, Blocks, Depth, Format |
| DONE | — | Coverage database: CSV + JSON reports | — | reports/deck-quality-audit-2026-03-08.{csv,json} — 1,680 rows |
| DONE | — | Quality rebuild: audit fixes + format batch | — | Session 047: 4 new scripts, 55 registry fixes, 444 cards patched, 2,255 flags resolved |
| DONE | — | Quality comparison report | — | compare-audits.py: before/after audit diff tool |
| OPEN | — | Whiteboard DONE-task archive pass | — | Periodic ⚪ task: trim completed rows |

---

## 🟡 Lusus Operis — The Play of the Work

Creative exploration, discovery. Surprising AND useful.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-32 | Mermaid CX dependency graph | — | docs/cx-dependency-graph.md |
| DONE | — | Systems eudaimonics seed | — | seeds/systems-eudaimonics.md |
| DONE | — | Color pipeline posture seed | — | seeds/color-pipeline-posture.md |
| DONE | — | SCL envelope architecture | — | seeds/scl-envelope-architecture.md |
| DONE | — | Cosmogram first pass (all 42 decks, Codex scaffold) | — | 42 v2 cosmograms set to DRAFT with 61/61 branch subject scaffolds; no web deposits |
| DONE | — | Cosmogram 61-branch architecture spec | — | scl-deep/cosmogram-architecture.md committed |
| DONE | — | Cosmogram scaffold script v2 | — | scripts/scaffold-cosmograms-v2.py — generates 42 v2 files pre-seeded from weight vectors |
| DONE | — | Cosmogram contract prompt v1 | — | seeds/cosmogram-contract-prompt-v1.md — replaces domain-based research prompt for v2 format |
| OPEN | — | Operis editorial voice prototype | — | Write one edition in full creative register |
| OPEN | — | Deck campaign naming pass (Deck 09 titles) | — | Review operator + title quality across 40 cards |
| DONE | — | Abacus architecture seed | — | seeds/abacus-architecture.md — 35 training archetypes × 48 zips |
| DONE | — | City Compiler architecture + implementation | — | Seed → built: web/src/lib/city-compiler.ts reads compiled JSON from middle-math/compiled/ (1,680 zips, 42 decks, 35 abaci) |
| OPEN | — | Platform architecture V3 (if V2 needs update) | — | After enough infrastructure lands |

---

## ⚪ Eudaimonia Operis — The Flourishing of the Work

Review, reflect, slow down. Does this serve flourishing?

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| OPEN | — | First CANONICAL review (Deck 08) | — | Jake reads 40 cards as a user. Gemba test. |
| OPEN | — | Vocabulary standard audit on Decks 07–09 | — | Check banned words in 102 generated cards |
| OPEN | — | Eudaimonics compliance review of Stripe seed | — | Does tier gating match Property 1? |
| OPEN | — | Publication standard compliance on Deck 09 | — | Voice check against scl-deep/publication-standard.md |
| OPEN | — | Whiteboard pruning session | — | Monthly: archive DONE rows, promote notes to tasks |

---

## Notes

Active observations, open questions, and emergent ideas. When a note becomes a task, move it to the appropriate Color section. When a note becomes a seed, commit it and remove from here.

- **Wave 4 partial (2026-03-10) — Sessions C-2, M complete.** Voice parser: `web/src/lib/voice-parser.ts` — 160+ keywords across 4 dials (Order/Axis/Type/Color), `VoiceInput.tsx` with Web Speech API mic button, auto-routes on >85% confidence, added to homepage. Data export: `GET /api/user/export` — full JSON download of all user data. Data deletion: `DELETE /api/user/delete` — cancels Stripe subscription, cascades all table deletions, removes auth user. Requires typing "DELETE MY ACCOUNT". Both added to `/me/settings`. Remaining Wave 4: Session K (pinch-zoom canvas) and Session L (community floor, needs Jake moderation decisions). After Wave 4: Session N (production deploy).
- **Wave 3 (2026-03-10) — Sessions E, G, H complete.** Onboarding: 3-step flow (equipment tiers 0-5, region picker, summary) with `user_equipment` table and `onboarding_complete` + `region` columns on profiles. Signup redirects to onboarding; existing users redirected on next /me visit. Logging: `LogOverlay` on exercise lines (├─), `workout_sessions` + `set_logs` tables, `SessionSummary` at card bottom. History at `/me/history`. Saved rooms: `SaveRoomButton` + `TrackVisit` + `VisitCount` on room pages, `saved_rooms` + `zip_visits` tables, `/me/library` with random room picker. Settings at `/me/settings` (equipment + region editor). Dashboard upgraded with links to all three. SQL migration 011 covers all 5 new tables + 2 profile columns. Wave 3 Quality Gate: signup → onboarding → first room → log a set → save room flow works end-to-end. Next: Wave 4 (voice parser, pinch-zoom, community, data export) or card quality work.
- **Session D+F (2026-03-10) — Auth + Payments Live.** Merged web app branch to main. Supabase auth wired: signup, login, logout, middleware, /me dashboard with tier display. Stripe wired: checkout sessions for Library Card ($10/mo) and Community Pass ($25/mo), webhook handler, post-checkout verify endpoint. Full flow tested: signup → subscribe → Stripe Checkout → tier updates in Supabase → /me shows correct tier. Profiles table with auto-create trigger, RLS policies, stripe_customer_id and stripe_subscription_id columns. Web app runs from `web/` directory. `.env.example` committed. Build Sequence V2 Sessions 0, D, and F complete. Next: Wave 2 remaining (Operis pipeline) or Wave 3 (onboarding, logging, saved rooms).
- **Web App Sessions A–J + Wave 1.5 (2026-03-09/10) — Next.js Foundation Complete.** Full web scaffold built on branch `claude/ppl-phase-0-start-Agzzj`. 16 commits. Tech: Next.js 16.1.6, React 19, Tailwind 4, Framer Motion, Zustand, TypeScript. Key systems: (1) City Compiler — batch-compiled 1,680 zip JSONs + 42 deck + 35 abacus JSONs from middle-math into `middle-math/compiled/`. TypeScript resolver with in-memory caching. (2) SCL parser (`web/src/lib/scl.ts`) — all 61 emoji mappings, zip↔numeric conversion, operator derivation, polarity detection. (3) D-Module design system — 7 Order proportions mapped to classical architecture (Tuscan→Palladian), 8 Color palettes with light/dark registers. (4) Room rendering — compiled JSON → 4-floor tabs (⌛ time, 🐬 community, 🪐 deep, 🌹 personal). Block sections with exercise lines. (5) Rotation engine (`web/src/lib/rotation.ts`) — deterministic daily zip from date (3-gear: Order×weekday, Type×rolling-5-day, Axis×month, Color×week-mod-8). Powers homepage TodayHero + WeekStrip. (6) Auth scaffolding — Supabase stubs (`lib/supabase/`), zustand auth store, login/signup/subscribe/profile pages, PaywallGate component. All ready for credential wiring. (7) Navigation — breadcrumbs, 4-dial zip navigator bottom sheet, loading skeletons, error boundaries, not-found pages. (8) API — `/api/resolve/[zip]` endpoint wrapping city compiler. All routes functional at `localhost:3000`. No Supabase env vars yet (stubs only). Next: merge to main, then Wave 2 (credential wiring, deeper homepage, content quality).
- **Session 047 CLOSED (2026-03-09) — Quality Rebuild Campaign: Phase 1-4.** Major infrastructure improvements to the audit and exercise-type systems. (1) Fixed audit-deck-quality.py flanking emoji bug: was counting unique type emojis instead of occurrences — eliminated 1,680 false positive flags. (2) Corrected 55 exercise-registry.json scl_types: 10 explicit (Turkish Get-Up→Plus, Jump Rope→Ultra, etc.) + 45 catch-all→correct via movement_pattern routing. Zero 5-type catch-alls remain. (3) Improved audit fuzzy matching: equipment prefix stripping, suffix patterns, word-boundary prefix matching. (4) Built fix-card-format.py: unified batch fixer — added operator calls to 260 cards (Restoration decks), tempo cues to 180 Mindful cards, barbell→dumbbell in 40 Circuit/Bodyweight cards. (5) Built diagnose-type-misroutes.py and fix-exercise-types.py for registry diagnosis and correction. (6) Built compare-audits.py for before/after comparison. Results: format 91.9→100.0, color 99.5→100.0, 2,255 flags resolved, 1,147 new real TYPE_MISMATCH flags revealed by improved detection. Net: 4,794→3,686 flags (-1,108). Remaining: 1,636 TYPE_MISMATCH (real generation errors needing card rebuild), 1,500 content depth flags.
- **Session 038 CLOSED (2026-03-06) — Exercise Library Expansion: Wave 6 complete (5/5).** CX-36: `middle-math/exercise-registry.json` — 2,085 exercises, globally unique EX-0001–EX-2085, 16-pattern vocabulary, anatomy inference, family linkage, axis/order affinity. CX-37: `scripts/generate-exercise-content.py` + 197 files in `exercise-content/` (push/pull/legs/plus/ultra). CX-38: 4 engine files in `middle-math/exercise-engine/` (family-trees, substitution-map, sport-tags, anatomy-index). CX-39: `external-refs.json` (2,085 null docks) + `seeds/exrx-partnership-brief.md`. CX-40: `sql/009-exercise-registry.sql` + `sql/010-exercise-knowledge.sql` + README updated. Wave 7 (CX-41, CX-42, CX-43) fully unblocked. Known data issue: `movement_pattern` catch-all assigns ~1,256 exercises to `core-stability` — carry/conditioning pattern disambiguation deferred to CX-43 Selector V2.
- **Session 039 CLOSED (2026-03-06) — Exercise Content Batch 2:** CX-41 DONE via `scripts/generate-exercise-content.py --batch 500`; +298 new files generated (202 skipped), bringing `exercise-content/` to 495 files total across push/pull/legs/plus/ultra. Spot check completed on 3 random files (464–480 words each).
- **Session 040 CLOSED (2026-03-06) — Exercise Content Batch 3:** CX-42 DONE via `scripts/generate-exercise-content.py --batch 1000`; +498 new files generated (502 skipped), bringing `exercise-content/` to 993 files total across push/pull/legs/plus/ultra. Spot check completed on 3 random files (441–478 words each).
- **Session 044 CLOSED (2026-03-06) — Deck 12 complete:** Deck identity built in `deck-identities/deck-12-identity.md`, all 40 cards generated under `cards/⛽-strength/🐬-partner/`, validators passed, and **⛽ Strength Order complete — 240/1,680 rooms filled**.
- **Session 041 CLOSED (2026-03-06) — CX-43 Selector V2 complete:** `scripts/middle-math/exercise_selector.py` upgraded to registry-aware selection (`exercise-registry.json`), octave-scale affinity scoring, family diversity enforcement (cross-block x0.3 penalty + in-block family uniqueness on output), substitution chain output (`--show-subs` via `exercise-engine/substitution-map.json`), catch-all movement_pattern preprocessing override (83 applied, logged to stderr), and V1 compatibility via `--v1`. Full sweep validation passed: 1,680/1,680 zips.
- **Deck generation priority:** Continue ⛽ Order sweep (10→11→12) or pivot to 🐂 Foundation Order (01→06)? Jake's call.
- **First CANONICAL review:** Jake has reviewed 0 decks to CANONICAL. When does this happen? Deck 08 is the candidate.
- **Exercise library v.1 SHIPPED (2026-03-07).** Movement pattern vocabulary expanded 16→18 (added: isolation, mobility). 1,163 exercises reclassified from core-stability catch-all. Exercise-card cross-reference index built (99.2% match, 253 unique exercises used across 1,680 cards, 1,832 unused). Integration validation: 21/21 checks. Section P scl_types gap fixed (85 exercises). Scripts: reclassify-movement-patterns.py, build-exercise-card-index.py, validate-exercise-integration.py.
- **Cosmogram sessions:** Require Genspark (web access). Schedule independently from generation. Priority candidates: Deck 07 (cards exist), Deck 01 (system origin), Deck 05 (history seed drafted).
- **Operis V4 pipeline:** Contract A/B URL enforcement gaps remain open. Must fix before re-run. Contract C parser hardening ✅ already committed.
- **Deck 07 Deck Campaign Table:** Deck 07 ✅ 40 cards (debt cleared, identity V2 ✅). Deck 08 ✅ 40 cards (identity V2 ✅). Deck 09 ✅ 40 cards (identity ✅). Decks 10–12 ⬜.
- **Deck 05 historical research seed:** Janus (Roman time/doorways), Imbolc (Celtic purification, Feb 1–2), Lupercalia (Roman purification, Feb 15), Ishango bone (20,000 BCE timekeeping), Benedictine horarium (canonical hours as temporal grammar), seven-day week (Babylonian/planetary). Feeds cosmogram when Deck 05 gets researched.
- **Monthly operator mapping confirmed:** Jan=📍pono, Feb=🧲capio, Mar=🧸fero, Apr=👀specio, May=🥨tendo, Jun=🤌facio, Jul=🚀mitto, Aug=🦢plico, Sep=🪵teneo, Oct=🐋duco, Nov=✒️grapho, Dec=🦉logos
- **Rotation engine:** Order by weekday (7-day), Type by rolling 5-day calendar from Jan 1, Axis by monthly operator. 5 and 7 are coprime — same Order-Type pairing doesn't repeat for 35 days.
- **4-dial elevator model:** Order=building, Axis=floor, Type=wing, Color=room. 1,680 rooms. Piano nobile stack: 🔨 ground → 🏛 noble → ⌛ 2nd → 🐬 3rd → 🌹 4th → 🪐 5th. Scroll on phone is inverse of building direction. Progressive disclosure IS the architecture.
- **Sprint 035 cascade:** CX-22 (floor routing) DONE → CX-29 (Wilson audio route) NOW UNBLOCKED. CX-15 (exercise selector) DONE → CX-25 (vote weight) and CX-30 (envelope stamping) critical path clear. Next session: CX-25 or CX-30.
- **Session 037 close (2026-03-06) — Architecture Capstone:** CX-31 DONE — envelope_retrieval.py (cosine similarity engine, Tier 1–4 retrieval profiles, --query/--deck/--operis/--validate/--stats flags, 5/5 validation). CX-01 DONE — TASK-ARCHITECTURE.md governance finalized, completion summary added. CX-19 DONE — .claude/AGENT-BOUNDARIES.md (5-agent matrix, escalation rules, Jake-reserved zones). CX-18 DONE — middle-math/design-tokens.json (8 Colors × 7 Orders) + middle-math/weight-css-spec.md (61-dim vector → CSS custom properties). Audit reports committed to reports/. 33/36 containers complete. CX architecture 92% done. Only CX-17 remains (blocked on Jake pod review). Project pivots to content generation.
- **Session 036 close (2026-03-06):** CX-25 DONE — vote_weight_adjuster.py (tanh signal, ±0.8 cap, eudaimonic interlock, --validate 5/5). CX-30 DONE — envelope_stamper.py (atomic retrieval unit, --anonymous + --full + --deck modes, all layers integrated). CX-29 DONE — middle-math/wilson-audio-spec.md (3-layer keyword scoring, ~2,260 entries, Wilson registers by floor). 29/36 containers complete. CX-31 (Envelope Retrieval) now FULLY UNBLOCKED — both blockers met (CX-30 ✓, CX-21 ✓). Wave 5 capstone is next.
- **The Operis is the front door** the system was missing. Solves cold start, onboarding, room circulation. Automatable once historical DB + cosmograms + calendar data are populated.
- **Programs are guided tours** — sequences of zip code addresses, not sequences of workouts. The rooms already exist. The program is the itinerary.
- **Publication standard constraint:** No "it's not X, it's Y" framing. The publication is informational. Independent of Party or Faction. Committed to Useful Knowledge.
- **The Negotiosum structure is new** (planted 2026-03-05). First pruning pass should evaluate whether Color assignments feel right after 2 weeks of use.
- **Session 046 (2026-03-08) — HTML Foundation + Systems Architecture.** Six contracts executed from Genspark architect handoff. (1) Ppl± rename: PPL± → Ppl± across 2,206 .md files via scripts/rename-ppl-styling.py. (2) Anti-Pasta systems review protocol: template + first report + seed + CLAUDE.md command. (3) HTML foundation: rendering pipeline seed, weight-vector-to-css.py bridge script, room.html prototype rendering 🐂🏛🛒⚫, floor-stack wireframe. (4) Almanac calendar seed: Temporitas floor as personal calendar/PDA with integration layer. (5) Digital city architecture seed: full thesis of Ppl± as traditional city. (6) Public-facing docs: what-is-ppl, how-the-abacus-works, the-operis (DRAFT status). Key insight: the abacus layer is what made the entire programming system coherent — 35 archetypes × 48 zips = 1,680 workouts organized as neighborhoods in a digital city.
- **Reconciliation session (2026-03-05):** ~25 PRs (#27–#84) merged to main between Sessions 030–033 with no session log entries. This session reconciled all container statuses, backfilled evidence in TASK-ARCHITECTURE.md, and updated the Negotiosum. Deck 09 (40 cards) was generated entirely across unlogged Codex runs.
- **Wave 3 unlock (2026-03-05):** CX-09 and CX-10 completion unlocked CX-11 (Block weights) and CX-12 (Operator weights). Both were already populated as working drafts in prior unlogged Codex runs. Engine coupling session confirmed on disk and registered as DONE. CX-14 (Weight Vector Engine) is now fully unblocked — all 5 dependencies met.
- **Stale seed audit (2026-03-05):** 8 files flagged with stale card counts or status references. Update opportunistically when each file is next touched: seeds/claude-code-build-sequence.md, seeds/platform-architecture-v2.md, seeds/operis-architecture.md, seeds/operis-prompt-pipeline.md, .codex/NEXT-ROUND-HANDOFF.md, AGENTS.md, cards/AGENTS.md, middle-math/ARCHITECTURE.md. Jake-blocked items (require Jake's input): platform-v1-archive body paste, color-context-vernacular vocabulary update, order-parameters vocabulary update.
- **Graph Parti note:** Needs scl-macro-reference.md at root — condensed emoji macros for Graph Parti context. Not blocking.
- **Color-tagging overhead:** Justified when it aids routing. Break-even at second human on project. The tags cost little now; they pay when the team grows.
- **SCL-Deep expansion complete:** emoji-macros.md, order-specifications.md, block-specifications.md, vocabulary-standard.md, publication-standard.md all committed. These are reference docs — they deepen generation quality but don't block it.
- **Middle-math status:** All 5 weight categories now DRAFT: Order ✓, Axis ✓, Type ✓, Color ✓, Block ✓, Operator ✓. Exercise family trees DRAFT (8 families). Selection algorithm spec written. CX-14 is the next step — weight vector computation engine.
- **Git-worktree pattern:** Seed planted (seeds/git-worktree-pattern.md). Adopt when parallel branch work becomes frequent enough to justify. Currently one branch at a time is sufficient.
- **Engine coupling session (2026-03-05):** CX-11 + CX-12 confirmed on disk as working drafts (790 and 502 lines) — registered as DONE. CX-20 (Room Schema Extension) written: sql/008-room-schema-extension.sql with 4 tables, RLS, indexes, 1,680-row population. CX-23 (Navigation Graph) computed: 1,680 nodes × 4 edges = 6,720 edges in middle-math/navigation-graph.json. CX-33 (Progress Dashboard) built: docs/dashboard/ with dark-theme static HTML and Python build script. 4 new containers registered (CX-32–35), 3 already done from prior Codex runs. CX-14 fully unblocked — the bus is bussing.
- **Macro system notes (planted 2026-03-05):** Color as conversational tone modifier (Phase 7+): Colors can signal intent in digital communication. "This is a 🟣 question" = I need precision. "This is a 🟡 question" = I'm exploring. Potential community floor feature. GitHub Project Board as visual Negotiosum: Create a Project board with a Color custom field, populate from whiteboard.md. Whiteboard auto-update enforcement: CX-35 partially covers this; consider adding CI check that verifies whiteboard.md was updated in any PR marking a CX container DONE.
- **Session 034 critical path advance (2026-03-06):** CX-33 reconciled (PR #90, built 2026-03-05). CX-14 DONE — weight_vector.py computes all 1,680 vectors (61 dimensions, octave scale [-8,+8]). CX-21 DONE — content-type-registry.json (109 types, 6 axes). CX-28 DONE — 42 cosmogram stubs generated. Cascade unlock: CX-15, CX-22, CX-25, CX-30 all fully unblocked. CX-15 is critical path next.
- **Wave 4 unblocked (2026-03-06):** CX-15 (Exercise Selection Prototype) — CX-13 ✓, CX-14 ✓. CX-22 (Floor Routing) — CX-03 ✓, CX-20 ✓, CX-21 ✓. CX-25 (Vote Weight Integration) — CX-20 ✓, CX-14 ✓. CX-30 (Envelope Schema) — CX-08 ✓, CX-14 ✓, CX-03 ✓.
- **DONE: Cosmogram first pass — 42 v2 files generated via Codex (subject scaffold, no web deposits) [2026-03-07].**
- **ACTIVE: Cosmogram enrichment — web research sessions needed for deposits, cross-deck mapping, and subject validation.**
- **Abacus architecture planted (2026-03-08).** 35 training archetypes × 48 zip codes. Math: 1,680 ÷ 48 = 35 exactly. 35 working slots + 13 bonus/junction zips per abacus. The 35-session super-cycle comes from 7 Orders × 5 Types (coprime). Overlapping zips across abaci collapse on merge. Non-overlapping working slots: 35 × 35 = 1,225 working + 455 bonus = 1,680 exactly. The math may not be a coincidence. Next steps: define the 35 archetype zip assignments, build overlap map, validate coverage. See `seeds/abacus-architecture.md`.
- **Intercolumniation layer needed.** The abacus rotation needs a middle-math weight system that factors in time-between-sessions. Recovery dynamics differ by Order (⛽ needs more recovery than 🐂). This is the reverse-weight resolution applied to program context. Sports science / ExRx consultation branch.
- **Abacus sorting fixed (2026-03-08).** compile-abacus.py no longer force-assigns orphan zips. Natural sorting puts ~1,591 zips in the 35 main abaci (94%). ~89 free-agent zips cluster into 12 DLC expansion packs (primarily 🏟 Performance, 🌾 Full Body, ⚖ Balance, 🖼 Restoration niche combos). 100% total coverage. Full sorted report: `reports/abacus-sort-report-2026-03-08.md`. DLC packs in `middle-math/abacus-registry.json`. Next: review DLC pack clustering quality, consider whether some packs need manual curation, wire in exercise library toggle logic, 12× operator layer (deferred).
- **Hero's Almanac v8 seed planted (2026-03-09).** DLC status. 7 Dares × 61 questions = 427 total. 12 Houses (operators as guilds, NOT calendar months). 1,680 archetypes (personal vector → zip-code cosine similarity). Multi-classing via ranked operator similarity. XP as vector accumulation. Intercolumniation as recovery profile layer. Legacy PDFs (Outside System, Hero's Almanac v7, Farmer's Almanac v4) mined for concepts; implementation discarded. Critical open: question mapping needs dedicated design sessions, all naming needs publication standard proofing. Operators serve dual function — guild identity (Almanac) and ambient monthly filter (Operis) — documentation must be explicit about which context applies. Intercolumniation section appended to `seeds/abacus-architecture.md`. Placeholder seeds planted for Outside System v2 and Cathedral Cup. See `seeds/heros-almanac-v8-architecture.md`.

---

## ARCHIDECK LAYER (branch: claude/build-archideck-layer-V47rx)

Status: Infrastructure initialized 2026-03-07. Branch created. No merge to main yet.

The `archideck/` directory contains the meta-architectural operating system:
- `archideck/KERNEL.md` — Compressed SCL seed (~2,800 words, project-agnostic)
- `archideck/CONTRACTS.md` — Cross-project Negotiosum switchboard
- `archideck/AGENT-CONTRACT.md` — Universal agent operating instructions
- `archideck/CLAUDE.md` — Ppl± vs Archideck routing layer
- `archideck/intake/` — Raw idea landing zone
- `archideck/projects/` — Project index

New project scaffolds created (intake phase):
- `projects/graph-parti/` — Graph Parti semantic canvas
- `projects/story-engine/` — Narrative architecture (intake needed)
- `projects/civic-atlas/` — Urban design layer (intake needed)
- `shared/` — Cross-project tools and SCL reference directory

GSD v1.22.4 installed to `.claude/commands/gsd/` and `.codex/skills/` (additive, no existing files overwritten).

Ppl± card generation continues on main as normal. When the Archideck branch is stable and tested, it merges to main as an additive layer.
See: `archideck/CONTRACTS.md` for cross-project switchboard.

---

🧮
