planted: 2026-03-04
status: SEED
phase-relevance: Phase 4/5 (Experience Layer), Phase 6 (User Accounts + Almanac), Phase 7+ (Community, Automotive, Maps)
blocks: nothing in Phase 2-3
depends-on:
  - middle-math/weights/weight-system-spec.md
  - middle-math/weights/interaction-rules.md
  - middle-math/weights/order-weights.md
  - seeds/regional-filter-architecture.md
  - seeds/default-rotation-engine.md
  - seeds/almanac-room-bloom.md
  - seeds/operis-architecture.md
  - seeds/content-types-architecture.md
  - middle-math/user-context/
  - middle-math/schemas/zip-metadata-schema.md
connects-to:
  - seeds/elevator-architecture.md
  - seeds/axis-as-app-floors.md
  - seeds/operis-sandbox-structure.md
  - seeds/community-content-architecture.md (planned)
  - seeds/live-operis-architecture.md (planned)
  - seeds/room-as-knowledge-node.md (planned)
  - seeds/wilson-voice-identity.md
  - seeds/automotive-layer-architecture.md
  - seeds/mobile-ui-architecture.md
  - seeds/exercise-superscript.md
  - middle-math/rotation/reverse-weight-resolution.md
  - middle-math/rendering/operis-weight-derivation.md
  - scl-deep/vocabulary-standard.md
  - scl-deep/publication-standard.md
supersedes: nothing (first specification of this concept)
📍 SCL Envelope Architecture — The Weight Vector as Universal Content Metadata

🔵🟣 — structured + precise

One Sentence

Every piece of content in the PPL± system — editorial, community, almanac, audio, observational — carries a frozen SCL weight vector snapshot called an envelope, and the system surfaces that content not by calendar date but by vector similarity to today's live conditions, making the 61-emoji language a universal retrieval index for a self-organizing library.

The Problem This Solves

PPL± is a library with 1,680 addresses. Content accumulates at those addresses from multiple sources: workout cards, Operis editions, cosmogram research, community submissions, user observations, audio recordings, educational material. As the library grows, the problem shifts from generation to retrieval. A user standing in a room needs to see the content that matters right now — not everything that has ever been filed here, but the material whose context matches today's context.

Calendar-based retrieval is the obvious approach and the wrong one. A fishing observation tagged "March 4" resurfaces every March 4 regardless of whether the conditions match. A planting guide tagged "early spring" resurfaces on a fixed date even if spring arrived three weeks early in one region and two weeks late in another. Calendar retrieval treats time as the only context variable. PPL± has 61 context variables. The system already computes a weight vector that describes the state of the world at any given address on any given day. That vector is the retrieval key.

The Envelope

An envelope is a frozen weight vector attached to a piece of content at the moment of creation. It captures the full SCL state — the 61-value weight vector, the regional context, and the temporal position — so the system knows what the world looked like when this content was made.

Envelope Format
envelope:
  vector: [61 float values, -8.0 to +8.0]
  primary_zip: "2123"
  order: 3
  axis: 1
  type: 2
  color: 3
  deck: 13
  operator: "plico"
  region: "southeast-us"
  season: "late-winter"
  lunar_phase: "waxing-gibbous"
  lunar_illumination: 0.72
  daylight_hours: 11.6
  daylight_delta: "+2m"
  solstice_distance: 73
  monthly_operator: "fero"
  day_of_week_order: 3
  timestamp: "2026-03-04T14:23:00Z"
  source_type: "user-pin"
  content_type_id: 92
The vector is the primary retrieval field. The remaining fields are denormalized convenience columns that support filtering without recomputing the vector. The vector is the truth. The columns are indexes.

What Carries an Envelope

Every piece of content in the system that is not a permanent structural document carries an envelope. Structural documents — CLAUDE.md, scl-directory.md, exercise-library.md, the publication standard — are infrastructure. They do not have envelopes because they are not time-contextual. Everything else does.

Content that carries an envelope, organized by source:

System-generated content. Operis editions (one envelope per edition, stamped at publication). Workout cards (one envelope per card, stamped at generation — reflects the SCL state at the time the card was written, not the card's zip code address). Cosmogram entries (stamped at research session). Deck identity documents (stamped at creation). Historical events database entries (stamped with a synthetic envelope derived from the event's date and the SCL state that date would produce via the rotation engine).

User-generated content. Workout logs (stamped at session completion). Personal notes on rooms (stamped at writing). 📍 Pins (stamped at drop). Community thread posts (stamped at posting). Audio submissions (stamped at upload). Blog posts, essays, recipes, educational submissions (stamped at publication). Form videos (stamped at upload). Junction votes and follow-up choices (stamped at the moment of choice).

Observational content. Fishing reports (stamped at observation). Planting observations (stamped at observation). Weather annotations (stamped at observation). Traffic reports (stamped at observation). Local event notices (stamped at posting). Seasonal food or market observations (stamped at observation).

The envelope is automatic. The user does not choose it. The system reads the current SCL state — today's rotation engine output, the user's region, the astronomical data — and stamps the envelope at the moment the content is created. The user's only input is the content itself and, optionally, the zip code address where it is filed. The envelope does the rest.

The Retrieval Engine

Content surfaces when its envelope is close to the current live state. Closeness is measured by vector similarity — the distance between the content's frozen envelope and today's live weight vector.

The Live Vector

At any moment, the system can compute a live weight vector. The rotation engine produces today's default zip code. The weight system computes the 61-value vector for that zip code. The regional filter adjusts seasonal and astronomical values. The temporal layer adds the day-of-week and monthly operator nudges. The result is a 61-value vector that describes right now for this user in this region.

This live vector is already computed for workout rendering and exercise selection. The retrieval engine consumes the same vector. No new computation is required for the core signal. The live vector is a byproduct of existing infrastructure.

Similarity Measurement

The distance between two envelopes is a weighted cosine similarity across the 61 dimensions. Not all dimensions contribute equally to retrieval relevance.

Tier 1 dimensions (highest retrieval weight). Order position, Axis position, seasonal operator, solstice distance. These are the broadest context markers. Content from the same Order and season is the most likely to be relevant regardless of finer details.

Tier 2 dimensions. Type position, Color position, lunar phase, daylight hours. These narrow the match. A fishing report filed under ➖ Ultra (endurance, outdoor activity) with a specific lunar phase is more relevant when today shares that Type and lunar range.

Tier 3 dimensions. Block-level weights, operator affinities, regional specifics. These are fine-grained context that separates near-matches from exact matches. A planting guide filed during 🐂 Foundation (on-ramp, basics) with the monthly operator fero (carry, transfer) is a stronger match when today also carries 🐂 and fero than when only the season matches.

Tier 4 dimensions (lowest retrieval weight). Individual exercise weights, equipment tier specifics, GOLD gate status. These matter for workout content retrieval but are mostly irrelevant for almanac, community, and observational content.

The tier weights are configurable per content type. Workout log retrieval weights Tier 4 heavily. Fishing report retrieval weights Tier 1 and Tier 2 heavily and ignores Tier 4. The retrieval engine accepts a content-type-specific weight profile that adjusts which dimensions matter most for that query.

Similarity Threshold

Content surfaces when its similarity score exceeds a configurable threshold. The threshold varies by floor and content type.

On the 🏛 Firmitas floor (the arrival surface), the threshold is high — only the closest matches surface. The Operis front page shows only today's most relevant content. Noise is excluded.

On the ⌛ Temporitas floor (the almanac), the threshold is moderate — content from similar seasonal positions in prior years surfaces even if the daily details differ. The almanac is retrospective. It tolerates looser matches because the value is in the pattern across years, not the precision of today's context.

On the 🐬 Sociatas floor (the community), the threshold is low — community content surfaces broadly because social relevance is harder to predict from weight vectors alone. The community floor supplements vector retrieval with recency and engagement signals.

On the 🪐 Gravitas floor (the deep layer), the threshold is moderate-to-high — cosmogram content and deep research surface when the deck-level context matches, not just the daily zip.

The Retrieval Query

A retrieval query takes three inputs: the live weight vector, the floor context (which sets the threshold and tier weights), and an optional zip code filter (to retrieve content filed at a specific address). The output is a ranked list of content items sorted by similarity score.
retrieve(
  live_vector: [61 floats],
  floor: "temporitas",
  zip_filter: "2123" | null,
  content_type_filter: [92, 94, 95] | null,
  limit: 20
) → [
  { content_id, similarity_score, envelope, preview },
  ...
]
When no zip filter is provided, the engine searches across all zip code addresses. When a zip filter is provided, only content filed at that address (or whose envelope's primary_zip matches) is considered. This supports both "show me everything relevant to today" and "show me what has happened at this specific room."

Condition-Based Resurfacing vs. Calendar-Based Resurfacing

This is the architectural distinction that separates the envelope system from a conventional content calendar.

Calendar-based: "Show this fishing report every March 4." The report surfaces on a fixed date. It surfaces in Tennessee and Minnesota on the same day. It surfaces in a warm March and a cold March identically. The date is the only retrieval key.

Condition-based: "Show this fishing report when the SCL state is similar to the state when it was filed." The report surfaces when the seasonal position, lunar phase, regional weather pattern, and daylight hours are within range of the original conditions. In a warm year, the report surfaces in late February. In a cold year, it surfaces in mid-March. In Tennessee it surfaces before Minnesota because the regional filter shifts the seasonal weight. The conditions are the retrieval key.

Calendar retrieval is a special case of condition-based retrieval where the only weighted dimension is solstice distance (time of year). The envelope system generalizes this to all 61 dimensions plus regional context.

The system does not abandon calendar awareness. The timestamp in the envelope is always available. An "on this day" feature can use raw date matching for anniversary-style content. But the default retrieval path for almanac, observational, and community content is condition-based. The calendar is one signal among 61.

Regional Divergence

The regional filter (see seeds/regional-filter-architecture.md) is an opt-in, user-selected setting. No GPS. No tracking. The user picks a region from a menu. The region adjusts seasonal weights in the live vector.

When retrieval runs, the live vector already contains the regional adjustment. A user in the Pacific Northwest has a different live vector in early March than a user in the Gulf Coast — different daylight hours, different seasonal position, different planting zone context. Content envelopes that match the Pacific Northwest's early March conditions surface for Pacific Northwest users. Content envelopes that match the Gulf Coast's conditions surface for Gulf Coast users.

The same fishing report, filed by a user in Georgia, carries a Georgia-context envelope. It surfaces for other Georgia-region users when conditions match. It can also surface for Tennessee-region users if the conditions are close enough — the similarity threshold allows for geographic proximity when the ecological conditions overlap. A bass spawning observation from Georgia is relevant in northern Alabama when the water temperatures align, even if the calendar dates differ by two weeks.

The regional divergence is automatic. No editorial curation is required. The envelope carries the context. The live vector carries the current conditions. The similarity engine does the matching. Regional content curation is a byproduct of the weight system, not a separate editorial operation.

The Almanac as Accumulated Envelopes

The Farmer's Almanac tradition works because it accumulates observations across years and surfaces them when conditions recur. PPL± is building the same structure, but the observations are tagged with 61 dimensions of context instead of one (date).

Year one: the system publishes Operis editions, users file observations, community content accumulates. Every piece carries an envelope. The almanac layer (⌛ Temporitas floor) is thin — limited historical depth.

Year two: the retrieval engine has a full year of envelopes to search. When today's live vector is computed, the engine finds last year's content whose envelopes match. The almanac surfaces that content. A planting guide from March 2027 appears for a user in March 2028 not because the date matches but because the conditions match. The user sees it alongside this year's content, with a year marker.

Year five: the almanac is rich. Multiple years of observations at similar conditions create depth. The retrieval engine returns content from years two, three, and four — each from the moment when conditions were closest to today. The user sees a layered almanac: what was happening at this zip code under these conditions across multiple years. Patterns emerge. Fishing runs that recur under specific lunar and temperature conditions. Planting windows that shift with climate variation. Workout performance patterns that correlate with seasonal position.

The cosmogram is the editorial seed that starts this process. The accumulated envelopes are the soil it grows in. The retrieval engine is the water. Time is the sun. The library grows itself.

The 📍 Pin as Content Primitive

The simplest unit of user-contributed content is the pin. A pin is a geographic point with an SCL envelope, a content type tag, and a brief annotation.

Pin format:
pin:
  id: uuid
  user_id: uuid
  zip_code: "2123" | null
  location:
    lat: 35.9606
    lon: -83.9207
    region: "southeast-us"
  envelope: { ... full envelope ... }
  content_type_id: 92
  tag: "📍"
  annotation: "Smallmouth bass, 4.2 lb, spinner bait, water 58°F, slight current"
  media: [ ] | [ image_url, audio_url ]
  visibility: "public" | "members" | "private"
  votes: { up: 12, down: 1, net: 11 }
  created_at: "2026-03-04T14:23:00Z"
The pin inherits its SCL context automatically. The user drops the pin, writes a short annotation, optionally attaches a photo or audio clip, and sets visibility. The system stamps the envelope. The pin is now retrievable by condition matching for every future user whose live vector approaches the same conditions.

The pin's zip code field is optional. If the user is inside a room (viewing a specific zip code), the pin files at that address. If the user drops a pin from the map layer or from the automotive interface, the zip code is null and the pin is retrievable only by vector similarity and geographic proximity. The pin exists in condition-space even without a room address.

The scl emoji 📍 is already an operator (pono — place, position, assign). The pin is the literal expression of pono: placing content at a position in the system.

SCL Emojis as Condition Tags

Beyond the automatic envelope, users and the system can attach explicit SCL emoji tags to content as supplemental condition markers. These tags are not the envelope — they are human-readable annotations that reinforce or specify the envelope's context.

A fishing report tagged with 🖼⌛➖⚪ says: Restoration conditions, Time axis, Ultra (endurance/outdoor), Mindful (slow, patient). That tag is a partial zip code — a filter that narrows retrieval beyond what the automatic envelope provides. The user is saying "this content belongs in the world described by these four emojis." The tag is a filing instruction expressed in the system's own language.

Partial tags are valid. A recipe tagged with 🐂🟢 says: Foundation (basics, on-ramp) and Bodyweight (no special equipment, accessible). The tag describes the content's character without specifying all four dials. The retrieval engine treats partial tags as additional weight boosts on the tagged dimensions — they narrow the match without excluding content that lacks the tag.

This is the same logic the workout system uses. A zip code with 4 emojis fully specifies a room. A partial zip (2 or 3 emojis) specifies a region of rooms. Content tags work the same way. Full tags are precise. Partial tags are directional. The retrieval engine handles both because it is already designed to work with weight vectors of varying specificity.

Community Voting as Weight Refinement

Users vote ➕ or ➖ on content. Votes adjust the content's effective retrieval weight — its position in the ranked results when the envelope matches.

Voting does not change the envelope. The envelope is a frozen snapshot. It does not change because users agree or disagree with it. The conditions at the time of creation are historical fact.

Voting changes the relevance score applied after similarity matching. Two pieces of content with identical similarity to today's live vector are ranked by their net vote score. The highly-voted fishing report surfaces above the poorly-voted one. The community signal is a tiebreaker within the similarity-matched result set.

This prevents voting from distorting the retrieval logic. A heavily upvoted piece of content does not surface when conditions do not match, no matter how popular it is. Popularity does not override relevance. Conditions come first. Votes rank within conditions.

At the system level, aggregate voting patterns across all content at a zip code address produce a signal about what the community values at that address. This signal feeds into the community-aggregate weight adjustment described in the vote-weight integration system (see CX-25 scope). The per-content vote ranks content. The aggregate vote adjusts the zip code's position in the rotation and recommendation systems. Two layers. Same input. Different consumers.

Content Type Retrieval Profiles

Each of the 109 content types (see seeds/content-types-architecture.md) carries a retrieval profile — a set of tier weights and threshold settings that govern how the retrieval engine handles that content type.

Workout cards (Type 1). Tier weights: heavy on all tiers (the workout card is the most fully-specified content type — every dimension matters). Threshold: high. Cards surface only when the zip code match is exact or near-exact. A workout card is not an approximate match — it is a specific address.

Operis editions (Type 2). Tier weights: heavy on Tier 1 (Order, season, operator). Threshold: moderate. Past editions surface on the almanac floor when the seasonal context is similar, even if the daily details differ. The editorial content has seasonal relevance beyond its publication date.

Community thread posts (Type 99). Tier weights: moderate on Tier 1 and 2, light on Tier 3 and 4. Threshold: low. Community content surfaces broadly. The social signal (votes, recency, engagement) supplements the vector match.

Observational pins (user-submitted, Types 92-97 range). Tier weights: heavy on Tier 1 and 2 (season, lunar, daylight, regional), light on Tier 3 and 4. Threshold: moderate. Observations surface when the natural-world conditions match. Exercise-specific dimensions are irrelevant for a fishing report.

Audio content (Wilson readings, user podcasts). Tier weights: moderate across tiers. Threshold: moderate. Audio surfaces when the context matches and the floor supports audio display (all floors support audio, but the ⌛ and 🐬 floors feature it most prominently).

The retrieval profile is metadata on the content type, not on individual content items. All fishing pins share one retrieval profile. All workout cards share another. The profiles are defined in the content type registry (see CX-21 scope) and consumed by the retrieval engine.

The Map as Envelope Visualization

The 🔨 Utilitas floor includes a map layer. The map is a geographic surface where pinned content appears as markers. The markers are SCL emojis — the content's primary tag or the operator emoji from its envelope.

At high zoom (street level): individual pins are visible with their annotations. A 📍 fishing pin shows the emoji, the annotation preview, and the vote score. A 🌾 farming observation shows the seasonal tag and the planting note.

At medium zoom (county/region level): pins aggregate into clusters. Clusters show the dominant SCL emoji in the cluster and a count. A region with many 📍 fishing pins clustered together shows 📍 ×23 and the aggregate vote score. Tapping the cluster zooms in.

At low zoom (state/multi-state level): the map shows condition zones. Regions where today's live vector produces similar seasonal states share a color wash. The user can see which regions are in similar conditions — useful for fishing, farming, and seasonal content relevance.

The map renders in the noli plan figure-ground style described in seeds/art-direction.md. Built structures are solid figures. Open ground is empty. Roads and waterways are drawn as architectural line work. The aesthetic is classical cartography, not satellite imagery. SCL emoji markers sit on the map like stamps on an architectural plate.

The map does not use GPS for tracking. It uses the user's selected region for center positioning and condition adjustment. If the user has not selected a region, the map opens at a continental default view. The pin's latitude and longitude are stored for geographic positioning on the map, but the system never reads the user's live location. The user places themselves by choice (region selection) or not at all.

In the automotive layer (Android Auto, CarPlay), the map is the primary visual surface. The voice parser (see seeds/voice-parser-architecture.md) allows the driver to query by condition: "What's biting near me?" triggers a retrieval of fishing pins whose envelopes match the current conditions and whose geographic coordinates are within a radius of the user's selected region center. Wilson reads the results. The map shows the pins. No touch interaction is required.

The Automotive Layer Integration

The envelope system is the automotive layer's content engine. When a user is driving, the system reads today's Operis aloud (Wilson voice), and the content that Wilson reads is condition-matched.

The weather report is not generic — it is regional, stamped with today's envelope, and relevant to the user's selected region. The almanac observations Wilson reads are enveloped content from prior years that match today's conditions. The fishing report Wilson mentions is a community pin whose envelope is similar to the current live vector.

The car experience is the free-tier daily touchpoint (see seeds/automotive-layer-architecture.md). The Operis audio is free. The almanac and community content read-outs are free. The conversion happens when the user wants to do the workout, log the session, drop a pin, or access the personal floor — actions that require the app and a subscription. The car is the shop window. The envelope system makes the window display contextually relevant every single day without editorial curation.

Relationship to Existing Architecture

The envelope does not replace any existing system. It adds a metadata layer and a retrieval layer that consume what already exists.

Middle-math weight system. The envelope's vector is computed by the existing weight system. No changes to the weight computation are required. The envelope is a snapshot of the output that already exists.

Rotation engine. The rotation engine's daily output is the seed of the live vector. The envelope system consumes the rotation engine's output. It does not modify the rotation logic.

Regional filter. The regional filter adjusts the live vector before retrieval. The envelope captures the regional context at creation time. The filter and the envelope are complementary — one describes now, the other describes then.

Room Bloom. Room Bloom tracks per-user visit depth. The envelope system tracks per-content condition context. They are orthogonal: Bloom describes the user's relationship to a room. The envelope describes the content's relationship to the world. Both contribute to what the user sees when they enter a room — Bloom determines how much personal data is visible, the envelope determines which community and almanac content surfaces.

Content types architecture. The 109 content types gain retrieval profiles. The content type registry (CX-21 scope) needs a retrieval_profile field added per type. This is an extension, not a modification.

Operis architecture. The Operis is the most prominent consumer of envelope-based retrieval. The Historical Desk articles carry envelopes. The almanac box data is condition-derived. The Wilson Note can reference enveloped community content. The Operis does not change its structure — it gains a richer pool of content to draw from as envelopes accumulate.

Superscript/subscript portal system. The citation portals (see seeds/exercise-superscript.md for the exercise-level system; the navigation portal extension is planted in seeds/room-as-knowledge-node.md [planned]) link content across rooms. An enveloped piece of content at one zip code can carry a superscript citation pointing to related content at another zip code. The envelope similarity between the two pieces of content is the basis for the citation — the system suggests cross-references between content whose envelopes are close. The user or editor can approve or reject the suggestion. Over time, the citation graph grows organically from envelope proximity.

Relationship to the Cosmogram

The deck cosmogram (see deck-cosmograms/README.md) is currently conceived as a single deep-research document per deck — 42 documents total, each a cultural and historical exploration of one Order×Axis combination.

The envelope system reframes the cosmogram. The research document remains the seed — the editorial foundation planted by the researcher. But the living cosmogram is the accumulated body of all enveloped content whose weight vectors fall within the deck's weight space.

Deck 07 (⛽🏛, Strength × Basics) has a weight space defined by: Order ⛽ primary at +8, Axis 🏛 primary at +8, with their respective affinity and suppression cascades. Any content whose envelope vector is within similarity threshold of this weight space is part of Deck 07's living cosmogram — regardless of whether it was filed at a Deck 07 zip code address.

A fishing report filed at a different zip code but carrying an envelope that strongly weights ⛽ (heavy, demanding conditions) and 🏛 (fundamental, classic approach) contributes to Deck 07's cosmogram. The filing address is not the only organizing principle. The weight vector is.

This means cosmograms grow without editorial curation. The research document is the deliberate seed. The enveloped content is the organic growth. The retrieval engine harvests the growth when a user visits the deck's cosmogram page. Over years, each deck's cosmogram becomes a deep, self-organized body of knowledge — part editorial research, part community observation, part almanac accumulation, part user contribution. The weight system is the librarian.

Implementation Phases

The envelope system builds incrementally. Early phases use the existing weight system output. Later phases add retrieval infrastructure.

Phase A — Envelope stamping. Every new piece of content in the system receives an envelope at creation. This requires: computing the live vector (already exists), capturing regional and astronomical context (partially exists via rotation engine), and storing the envelope as a JSONB field alongside the content. This is a schema addition and a creation-pipeline hook. No retrieval logic yet. Content is stamped but not yet retrieved by condition.

Phase B — Similarity function. A PostgreSQL function or application-layer utility that computes weighted cosine similarity between two 61-value vectors. This is a pure math function. It does not require any content or editorial work. It can be tested against the existing weight system's output for known zip codes.

Phase C — Retrieval query. A retrieval endpoint that accepts a live vector, a floor context, and optional filters, and returns ranked content. This is the core product: content that surfaces by condition rather than by date. The ⌛ Temporitas floor is the first consumer — the almanac page that shows condition-matched content from prior periods.

Phase D — Community contribution pipeline. Users can submit pins, posts, audio, and other content with automatic envelope stamping. The 🐬 Sociatas floor becomes the contribution surface. Moderation, attribution, and visibility rules are defined in seeds/community-content-architecture.md (planned).

Phase E — Map layer. The 🔨 Utilitas floor renders pinned content on a geographic surface. The automotive layer consumes the same data via audio. The map is a visualization of enveloped content in geographic space.

Phase F — Cross-reference citation graph. The superscript/subscript portal system links content across rooms based on envelope similarity. The citation graph grows organically as the retrieval engine identifies close envelopes across different zip code addresses.

Each phase produces working functionality. The system does not require all phases to deliver value. Phase A alone makes every piece of content machine-retrievable by condition in the future. Phase C alone makes the almanac floor functional. The phases are additive, not sequential — B and C can begin before D, E, and F.

Database Schema Implications

The envelope system requires additions to the database schema defined in middle-math/schemas/.

New canonical table: content_items. Columns: id (UUID PK), source_table (TEXT CHECK IN ('workout_cards','workout_logs','community_posts','room_threads','audio_entries','observational_pins')), source_id (UUID), content_type_id (INTEGER, FK to content type registry), created_at (TIMESTAMPTZ). Constraint: UNIQUE (source_table, source_id). Every content-bearing table registers one row here so downstream links always target a single enforceable parent.

New table: content_envelopes. Columns: id (UUID PK), content_item_id (UUID NOT NULL, FK → content_items.id ON DELETE CASCADE), zip_code (CHAR(4), nullable, FK to zip_metadata), envelope_vector (VECTOR(61) or JSONB — the 61-value weight vector), region (TEXT), season (TEXT), lunar_phase (TEXT), lunar_illumination (NUMERIC(3,2)), daylight_hours (NUMERIC(4,1)), solstice_distance (INTEGER), monthly_operator (TEXT), day_of_week_order (INTEGER), scl_tags (TEXT[] — optional explicit SCL emoji tags), created_at (TIMESTAMPTZ), vote_score (INTEGER DEFAULT 0). Constraint: UNIQUE (content_item_id) so each content item has at most one immutable envelope.

Indexes: GIN or IVFFLAT index on envelope_vector for similarity search (if using pgvector extension). In content_items, composite index on (content_type_id, source_table). In content_envelopes, composite index on (region, season), index on (zip_code), index on (created_at DESC), and index on (vote_score DESC).

New table: content_pins. Columns: id (UUID PK), user_id (UUID FK → auth.users), envelope_id (UUID FK → content_envelopes), latitude (NUMERIC(10,7)), longitude (NUMERIC(10,7)), annotation (TEXT), media_urls (TEXT[]), visibility (TEXT CHECK IN ('public','members','private') DEFAULT 'public'). RLS: public pins readable by all authenticated users; members pins readable by subscribers; private pins readable by owner only. Writes restricted to owner.

Extension to existing tables. Any table that holds content (workout_logs, community_posts, room_threads, etc.) gains an envelope_id (UUID FK → content_envelopes, nullable). Existing rows without envelopes are valid — the envelope is optional until Phase A is deployed, at which point all new rows receive one automatically.

pgvector consideration. If Supabase supports the pgvector extension (it does as of 2025), the envelope_vector column should use the VECTOR(61) type for native similarity search via `<=>` (cosine distance) or `<->` (L2 distance) operators. If pgvector is not available, the vector is stored as JSONB and similarity is computed application-side. The schema should be written to support both paths.

Constraints

The envelope is immutable after creation. Conditions at the time of content creation are historical fact. Votes, edits to the content body, and changes to visibility do not alter the envelope. If the content is deleted, the envelope is deleted. The envelope is not a living document. It is a fossil record.

The retrieval engine never surfaces content that the user's subscription tier does not permit. Tier gating is enforced at the retrieval layer, not the envelope layer. All content has envelopes regardless of tier. Tier determines what the user sees in the results, not what the engine searches.

The regional filter is opt-in. Users who do not select a region receive a default live vector without regional adjustment. Their retrieval results are not regionally biased. Content pinned with geographic coordinates is still retrievable for them — it just ranks by vector similarity without the regional proximity boost.

Voting does not alter the envelope vector. Voting alters the content's ranking within similarity-matched results. The envelope is the address. The vote is the reputation at that address. The two are independent.

The system does not infer user location from IP, device sensors, or any other passive source. Geographic positioning in the system comes from three sources only: the user's selected region (opt-in), the latitude/longitude of a pin the user explicitly drops (voluntary), and the user's text/voice input (parsed, not tracked). See seeds/data-ethics-architecture.md.

SCL emoji tags on content are optional and user-applied. The system does not auto-tag content with SCL emojis beyond the automatic envelope. The envelope is the machine-readable context. The emoji tags are the human-readable context. Both exist. Neither overwrites the other.

Open Questions

How does envelope similarity interact with the reverse-weight resolution algorithm? The reverse-weight system (see middle-math/rotation/reverse-weight-resolution.md) triangulates today's featured room between yesterday's fatigue and tomorrow's stimulus. Should envelope retrieval also consider the user's yesterday-envelope and tomorrow-predicted-envelope, surfacing content that fits the arc rather than just the moment?

Should the system support user-edited envelopes? The current design makes envelopes immutable and automatic. A power user might want to adjust the SCL tags or even the weight vector on their own content. This would allow more precise filing but introduces the risk of users gaming the retrieval system. Current position: envelopes are immutable. Tags are editable. If this proves too rigid, revisit.

What is the minimum envelope density before condition-based retrieval outperforms calendar-based retrieval? In year one, the envelope corpus is thin. Calendar retrieval may be more useful until enough envelopes accumulate for similarity matching to produce meaningful results. Should the system fall back to calendar retrieval when the envelope corpus is below a threshold? Current lean: yes, with the threshold defined empirically after Phase C deployment.

Should envelopes be versioned? The weight system may evolve — new emojis added, weight scales recalibrated. A version field on the envelope would allow the retrieval engine to normalize old envelopes against the current system. Current lean: yes, add an envelope_version field (INTEGER DEFAULT 1) to support future migrations.

How does the envelope system interact with the construction vehicle pipeline? The Operis forces card generation for featured zip codes. Should the Operis also force envelope stamping for the historical events it features — retroactively computing envelopes for historical content that predates the system? Current lean: yes, the historical events database (366 files) should be seeded with synthetic envelopes computed from each date's rotation engine output. This is a one-time batch operation in Phase A.

🧮
