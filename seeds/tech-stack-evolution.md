---
planted: 2026-03-12
status: SEED
phase-relevance: Phase 4 (current) through Phase 10+ (full platform)
blocks: nothing — informs all future technical decisions
depends-on: seeds/experience-layer-blueprint.md, seeds/life-copilot-architecture.md, seeds/home-screen-architecture.md, seeds/wilson-voice-identity.md
connects-to: seeds/art-direction-intaglio.md (procedural rendering), seeds/character-progression-architecture.md (weight computation), seeds/exploration-immersion-architecture.md (game engine), middle-math/ARCHITECTURE.md, seeds/data-ethics-architecture.md
extends: seeds/experience-layer-blueprint.md (evolves single-app stack into service mesh)
---

# Tech Stack Evolution — From Web App to Platform Architecture

🔵🟣 — systematic + precise

## One Sentence

Ppl± is not a Next.js app — it is a service mesh where TypeScript is the skin, Python is the brain, Rust is the muscle, PostgreSQL is the memory, and new domains plug in as independent services without disturbing what's already running.

---

## Section 1 — The Constraint That Informs the Stack

The SCL is 61 constraints that produce 1,680 rooms. The tech stack follows the same principle: constraints produce architecture. Choosing the right language for each layer isn't preference — it's constraint-driven design. The constraint is: what does this layer NEED to do, and what tool does that job without fighting it?

The system in 5–10 years is not a workout app. It is:
- A personal copilot with AI assistant (Wilson)
- A library/encyclopedia with search across massive content
- A weight computation engine running 61-dimensional vector math per user per zip code
- A procedural rendering system generating intaglio art from mathematical parameters
- A real-time community platform with proximity-based chat
- A game engine hosting puzzles, challenges, and interactive content
- A scientific computation layer (weather, astronomy, seasonal calculations)
- An almanac and calendar system aware of global temporal rhythms
- A career/finance/civics information platform
- A per-user database that grows for years (10,000 users × 10 years = billions of data points)

No single language or framework handles all of this. The architecture is polyglot by necessity.

---

## Section 2 — The Four Materials

Like a building uses different materials for different structural roles — steel for the frame, glass for the windows, concrete for the foundation, wood for the interior — Ppl± uses four primary languages, each for what it does best.

### TypeScript — The Skin

**What it does:** Everything the user sees and touches. The Relevator, the viewport, the terminal, the chat, the workout cards, the map, the vials. All UI rendering, client-side state, routing, and the API gateway that connects the skin to the services behind it.

**Why TypeScript:** It runs in every browser on every device. It's the only language that works on both the server (Next.js API routes) and the client (React components). One language for the entire surface layer means one mental model for the UI, one type system, one testing framework. The skin should be consistent.

**Current state:** Already built. Next.js 16, React 19, Tailwind 4, Framer Motion, Zustand. This is stable and stays.

**Grows into:**
- Progressive Web App (PWA) for offline access
- WebSocket client for real-time chat
- WASM host for Rust-compiled modules running in-browser
- Service worker for background sync and push notifications

### Python — The Brain

**What it does:** Intelligence, science, and data processing. Wilson (AI assistant), content generation pipelines (Operis), scientific computation (weather, astronomy, seasonal), exercise selection algorithms, data analysis, machine learning, and any domain where the ecosystem of libraries matters more than raw speed.

**Why Python:** The entire AI/ML world runs on Python. Claude's API, LangChain, vector databases, NumPy, SciPy, pandas, astropy — every tool Wilson needs is Python-native. The middle-math engine's scripts are already Python. The computation that drives the weight vectors, exercise selection, envelope retrieval, and bloom engine is already Python. This layer extends naturally.

**Current state:** 35 scripts in `scripts/`. Weight vector engine, exercise selector, envelope stamper/retrieval, bloom engine, abacus compiler, audit tools. All Python.

**Grows into:**
- Wilson AI service (RAG pipeline over content library + Claude API)
- Operis auto-generation pipeline (4-prompt sequence)
- Weather/astronomy microservice
- Content indexing and search pipeline
- Recommendation engine (rotation + personal vector + intercolumniation)
- Data export/analytics processing

**Note:** NumPy — the library that makes Python fast at math — is literally a Fortran wrapper underneath. When Python does matrix math, it's calling Fortran-era BLAS/LAPACK routines compiled to native code. The instinct toward Fortran's computational strength is already present in the stack through NumPy.

### Rust — The Muscle

**What it does:** Performance-critical computation that needs to run fast on servers OR in the browser via WebAssembly (WASM). Procedural rendering (guilloche generation, intaglio line computation), game engines, real-time physics for interactive content, heavy client-side computation, and any service where latency matters.

**Why Rust:** Fortran-class speed with modern safety guarantees. Compiles to native code for servers. Compiles to WASM for browsers. No garbage collector (predictable performance). Memory safety without runtime overhead. The modern answer to "I need C/Fortran speed but I also need this to run in a web browser."

**Current state:** Not yet in the stack. This is the next material to introduce when the procedural rendering or game layer begins.

**Grows into:**
- Procedural guilloche SVG generator (from weight vectors → intaglio patterns)
- Client-side WASM modules for interactive content (games, puzzles, visualizations)
- High-performance weight vector computation (if Python becomes a bottleneck at scale)
- Real-time multiplayer game server (if Cathedral Cup or competitive features launch)
- Content rendering pipeline (markdown → styled output at speed)

### PostgreSQL — The Memory

**What it does:** All persistent data. User profiles, workout logs, set data, personal vectors, community posts, chat history, content metadata, zip code state, fog of war progress, quicksave positions, vial history, subscription status. Everything that needs to survive a server restart.

**Why PostgreSQL:** Battle-tested at massive scale. Instagram, Discord, and Stripe all run on Postgres. Supabase wraps it with auth, real-time subscriptions, row-level security, and storage — all already integrated. Full-text search is built in. JSON columns handle flexible schema. The SQL migrations are already written (11 migration files).

**Current state:** Supabase PostgreSQL with 11 migrations, RLS policies, real-time enabled. Profiles, workout sessions, set logs, saved rooms, zip visits, community tables scaffolded.

**Grows into:**
- Billions of rows (10,000 users × 10 years of daily logs)
- Full-text search across cosmograms, almanac, exercise library, Operis archive
- Vector similarity search (pgvector extension) for personal vector → zip code matching
- Time-series partitioning for workout history (partition by year for query performance)
- Read replicas for scaling concurrent users
- Potentially Elasticsearch or Meilisearch as a dedicated search service if full-text search outgrows Postgres

---

## Section 3 — The Service Mesh

The four materials connect through a service mesh — independent backend services that the TypeScript skin calls through APIs.

```
┌─────────────────────────────────────────────────────┐
│                    USER DEVICE                       │
│  [Browser / PWA / Android Auto / CarPlay]            │
│  TypeScript: Next.js + React + WASM modules          │
└──────────────────────┬──────────────────────────────┘
                       │ HTTPS / WebSocket
                       ▼
┌─────────────────────────────────────────────────────┐
│              API GATEWAY (Next.js API Routes)        │
│  Routes requests to the correct backend service      │
│  Auth verification (Supabase JWT)                    │
│  Rate limiting, caching, request validation          │
└───┬────────┬────────┬────────┬────────┬─────────────┘
    │        │        │        │        │
    ▼        ▼        ▼        ▼        ▼
┌───────┐┌───────┐┌───────┐┌───────┐┌───────┐
│WILSON ││WEIGHT ││CONTENT││WEATHER││ GAME  │
│Python ││Python ││Search ││Python ││ Rust  │
│       ││Rust   ││Postgres││      ││→WASM  │
│Claude ││NumPy  ││Meili? ││astro  ││       │
│RAG    ││vectors││       ││APIs   ││puzzles│
└───┬───┘└───┬───┘└───┬───┘└───┬───┘└───┬───┘
    │        │        │        │        │
    └────────┴────────┴────────┴────────┘
                      │
                      ▼
        ┌──────────────────────┐
        │    PostgreSQL         │
        │    (Supabase)         │
        │    The single source  │
        │    of truth for all   │
        │    persistent data    │
        └──────────────────────┘
```

### How Services Are Added

New domains plug in as new services. The pattern is always the same:

1. Define the service's API contract (what it accepts, what it returns)
2. Build the service in whatever language fits (Python for AI/science, Rust for performance, TypeScript for simple CRUD)
3. Register the route in the API gateway
4. The frontend calls it like any other API

**Examples of future services:**

| Domain | Service | Language | Why |
|--------|---------|----------|-----|
| College tools | Study planning, course tracking | Python | Scheduling algorithms, recommendation |
| Financial literacy | Budget calculators, tax season guides | TypeScript | Simple computation, mostly content |
| Architecture tools | Proportion calculators, golden ratio | Rust→WASM | Visual computation in browser |
| Music integration | Playlist generation by Color mood | Python | Spotify API, mood mapping |
| Astrophysics layer | Star charts, planetary positions | Python | astropy library |
| Civic information | Local resource directories | TypeScript | Mostly content + search |
| Graph Parti | Semantic canvas rendering | Rust→WASM | Heavy interactive graphics |

Each service is independent. Adding a college tools service doesn't touch Wilson. Adding an astrophysics layer doesn't touch the workout engine. The skin (TypeScript) just gets a new API endpoint to call and a new viewport content type to render.

---

## Section 4 — Scaling Trajectory

### Phase 4–5 (Now → 6 months): Single Server

Everything runs on one Vercel deployment + one Supabase instance. TypeScript handles everything. Python scripts run as serverless functions or local tools. This is sufficient for launch and early users.

**Stack:** TypeScript + Python scripts + PostgreSQL
**Users:** 0–1,000
**Data:** Millions of rows

### Phase 6–7 (6 months → 2 years): Service Separation

Wilson becomes its own Python service. The weight computation engine moves to a dedicated service (Python/Rust hybrid). Content search gets its own index. Real-time chat scales through Supabase Realtime or a dedicated WebSocket service.

**Stack adds:** Python services, possibly Rust for hot paths
**Users:** 1,000–50,000
**Data:** Hundreds of millions of rows

### Phase 8–10 (2–5 years): Full Mesh

Each domain has its own service. WASM modules handle client-side computation. The game engine is Rust. Graph Parti and interactive tools are Rust→WASM. Multiple database read replicas. CDN for static content. Edge functions for low-latency API responses.

**Stack adds:** Rust services, WASM, search service, CDN, edge computing
**Users:** 50,000–500,000+
**Data:** Billions of rows, terabytes of content

### Phase 10+ (5–10 years): Platform

The service mesh is mature. New domains plug in without architectural changes. The system handles any add-on — astrophysics, engineering, education, civic tools — because the pattern for adding services is established and repeatable. The skin (TypeScript) is stable. The brain (Python) grows with AI capabilities. The muscle (Rust) handles whatever needs raw speed. The memory (PostgreSQL) is partitioned, replicated, and indexed for any query pattern.

---

## Section 5 — What This Means for Building Today

**Nothing changes about current development.** The Next.js app, the Python scripts, the Supabase database — all of this continues as-is. The service mesh is not something we build now. It's something the architecture grows INTO.

What changes is **awareness**:

1. **Keep services separable.** When writing Python scripts, keep them callable as standalone services (they already are). When writing API routes, keep them thin — they should route to logic, not contain it.

2. **Keep the database schema extensible.** New tables for new domains. Foreign keys to the zip code system where appropriate. The zip code (CHAR(4) numeric) is the universal join key.

3. **Keep the frontend API-driven.** The viewport renders whatever the API returns. It doesn't care whether the response came from a TypeScript function, a Python service, or a Rust WASM module. Content type in, rendered content out.

4. **When computation gets slow, that's the signal to introduce Rust.** Not before. Premature optimization with a new language adds complexity without solving a real problem. Python handles the current scale. When it doesn't, Rust is ready.

5. **WASM is the bridge.** When interactive content (games, procedural art, Graph Parti) needs to run in the browser at speed, Rust→WASM is the path. This is the modern answer to the Fortran instinct — computation-class speed in a web browser.

---

## Section 6 — The Fortran Instinct Was Right

The question "shouldn't this system have something more powerful than JavaScript?" is architecturally correct. The answer isn't Fortran specifically, but the instinct — that a flagship platform handling computation, AI, scientific data, procedural rendering, games, and millions of user records needs more than one language — is exactly right.

The constraint-driven answer: use each language for what it's best at. TypeScript for the skin. Python for the brain. Rust for the muscle. PostgreSQL for the memory. The constraints produce the architecture. Same principle as the SCL.

---

## Open Questions

1. **When does Wilson's first Python service deploy?** This is the first service separation milestone. Likely when RAG pipeline + Claude API integration begins.
2. **When does Rust enter the stack?** Likely when procedural guilloche rendering (from `seeds/art-direction-intaglio.md`) begins, or when a game/puzzle system needs WASM.
3. **Hosting for Python services.** Vercel serverless functions? Railway? Fly.io? AWS Lambda? The choice affects latency and cost.
4. **pgvector for similarity search.** When personal vector → zip code matching moves from Python scripts to live queries, pgvector (PostgreSQL extension) handles it natively. When to enable?
5. **WASM bundle size.** Rust→WASM modules add to the client download. How to keep initial load fast while loading WASM modules on demand?
6. **Service communication.** REST? gRPC? Message queue? For internal service-to-service calls, gRPC is faster. For frontend-to-service, REST is simpler.
7. **Monitoring and observability.** As services multiply, how do we track health, errors, and performance across the mesh? OpenTelemetry? Grafana?
8. **Jake's learning path.** TypeScript first (read and modify the skin). Python second (extend the brain). Rust when the muscle is needed. Each language opens a layer.

---

🧮
