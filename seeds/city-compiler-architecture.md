---
title: The City Compiler — SCL Universal Resolution Engine
status: SEED
planted: 2026-03-09
category: infrastructure
phase-relevance: Phase 3–7 (Middle-Math, Experience Layer, Personalization)
blocks: nothing currently — foundational system architecture
depends-on: middle-math/weight-vectors.json, middle-math/design-tokens.json, middle-math/weight-css-spec.md, seeds/archideck-color-architecture.md, seeds/digital-city-architecture.md, seeds/abacus-architecture.md, seeds/heros-almanac-v8-architecture.md, seeds/elevator-architecture.md, middle-math/rendering/ui-weight-derivation.md, middle-math/exercise-registry.json, middle-math/exercise-engine/family-trees.json, middle-math/navigation-graph.json, middle-math/abacus-registry.json
connects-to: seeds/operis-architecture.md, seeds/experience-layer-blueprint.md, seeds/mobile-ui-architecture.md, seeds/voice-parser-architecture.md, scl-deep/color-context-vernacular.md, scl-deep/cosmogram-architecture.md, middle-math/rotation/rotation-engine-spec.md
supersedes: nothing (first specification — synthesizes existing specs into unified resolution)
---

# The City Compiler — SCL Universal Resolution Engine

## Thesis

Every piece of the Ppl± system — workout generation, visual rendering, editorial tone, art direction, neighborhood identity, RPG archetype, community character, dark/light mode, animation behavior, sound design — already derives from the same 61-dimensional weight vector. But these derivations are scattered across 15+ specification documents, each handling its own slice. The City Compiler is the single resolution function that takes any SCL address (a zip code, an emoji, a deck number, an abacus ID) and returns every derived value in one object.

The compiler does not invent new math. It collects existing math into one place and adds three missing layers:

1. **Macro aggregation** — resolving abacus-level and deck-level identities by aggregating constituent zip vectors
2. **Dual register rendering** — dark mode as cathedral candlelight, light mode as watercolor wash (not a CSS toggle)
3. **Archetype personality** — the RPG class system wired to the 12 operator Houses and the 35 abacus neighborhoods

The compiler is a script. Its output is a JSON object. That object is the single source of truth for every downstream system. No downstream system needs to understand SCL rules — it reads the compiled object.

---

## Part I — What the Compiler Resolves

### Input Types

The compiler accepts any of these as input:

```
resolve("⛽🏛🪡🔵")      → full zip code (1,680 possible)
resolve("2123")            → numeric zip code (equivalent)
resolve("⛽")              → single emoji (61 possible)
resolve("deck:07")         → deck number (42 possible)
resolve("abacus:02")       → abacus ID (35 possible)
resolve("house:facio")     → operator House (12 possible)
resolve("type:pull")       → Type (5 possible)
resolve("color:structured") → Color (8 possible)
resolve("order:strength")  → Order (7 possible)
resolve("axis:basics")     → Axis (6 possible)
```

Single-emoji and category-level queries return the aggregate profile for that dimension across all zip codes where it's dominant.

### Output: The Resolution Object

The compiler returns a flat JSON object with every derived value. Downstream systems read only the fields they need. The object has 7 sections:

```json
{
  "address": { },          // Identity: what this IS
  "architecture": { },     // D-module: proportions, spacing, line weights
  "palette": { },          // Color: light register, dark register, accents
  "typography": { },       // Type: font, weight, tracking, scale
  "personality": { },      // Character: archetype, House, tonal register
  "connections": { },      // Graph: neighbors, junctions, abacus membership
  "metadata": { }          // System: deck, operator, blocks, exercise pool
}
```

---

## Part II — The Resolution Object Schema

### Section 1: Address

```json
{
  "address": {
    "zip_emoji": "⛽🏛🪡🔵",
    "zip_numeric": "2123",
    "order": { "emoji": "⛽", "name": "Strength", "index": 1, "classical": "Doric" },
    "axis":  { "emoji": "🏛", "name": "Basics",   "index": 0, "latin": "Firmitas" },
    "type":  { "emoji": "🪡", "name": "Pull",     "index": 1, "muscles": ["lats","rear delts","biceps","traps","erectors"] },
    "color": { "emoji": "🔵", "name": "Structured","index": 2, "tier": "2-3", "gold": false, "polarity": "expressive" },
    "operator": { "emoji": "🤌", "name": "facio", "latin": "execute/perform", "house": "The Executors" },
    "deck": 7,
    "url": "/zip/2123"
  }
}
```

### Section 2: Architecture (D-Module)

All values derived from the D-module system in `seeds/archideck-color-architecture.md`.

```json
{
  "architecture": {
    "D": "1rem",
    "column_ratio": 8,
    "intercolumniation": 2.75,
    "superposition": 0.85,
    "line_multiplier": 1.3,
    "material": {
      "name": "Pentelic marble",
      "hue": 220,
      "saturation": 5,
      "warmth": 0.3,
      "texture": "dense, polished",
      "shadow_character": "sharp, defined"
    },
    "atmosphere": {
      "brightness": 1.1,
      "hue_shift": 0,
      "sat_multiplier": 1.0,
      "warmth_modifier": 0
    },
    "shadow": {
      "depth_multiplier": 1.3,
      "hue": 30,
      "saturation": 8,
      "blur_character": "small blur, high opacity"
    },
    "spacing": {
      "xs": "calc(D * 0.25)",
      "sm": "calc(D * 0.5)",
      "md": "calc(D * 1.375)",
      "lg": "calc(D * 2.75)",
      "xl": "calc(D * 4.125)",
      "xxl": "calc(D * 5.5)"
    }
  }
}
```

### Section 3: Palette (Dual Register)

**This is the new layer.** Every zip code has TWO complete palettes — a light register and a dark register. These are not inverted copies. They are two different rendering philosophies applied to the same weight vector.

```json
{
  "palette": {
    "light_register": {
      "name": "watercolor",
      "philosophy": "Transparent glazed layers over a bright ground. Selective saturation. Paper showing through.",
      "primary": "#2E6BA6",
      "secondary": "#3A7EC0",
      "background": "#EDF4FB",
      "surface": "#FFFFFF",
      "text": "#143050",
      "accent": "#1E4F7D",
      "border": "#B8D4EC",
      "type_accent": "#3D6E8F",
      "operator_tint": "#4A5568",
      "saturation_level": 0.85,
      "contrast_ratio": 7.2
    },
    "dark_register": {
      "name": "cathedral",
      "philosophy": "Warm pools of light on dark surfaces. Selective illumination. Stone walls absorbing candlelight.",
      "primary": "#5B9BD5",
      "secondary": "#4A8BC2",
      "background": "#0D1117",
      "surface": "#161B22",
      "text": "#C9D1D9",
      "accent": "#7CB3E0",
      "border": "#21262D",
      "type_accent": "#5B8FAA",
      "operator_tint": "#8B949E",
      "saturation_level": 0.55,
      "contrast_ratio": 8.1
    },
    "color_wheel": {
      "hue": 209,
      "saturation": 57,
      "lightness": 42,
      "complement_hue": 29,
      "split_complements": [359, 59],
      "analogous": [179, 239]
    },
    "seasonal_modifier": {
      "current_month": "march",
      "current_operator": "🧸 fero",
      "season_phase": "inhale",
      "hue_shift": -3,
      "sat_modifier": 0.95,
      "temp_bias": -0.05
    }
  }
}
```

### Section 4: Typography

```json
{
  "typography": {
    "font_family": "'Inter', system-ui",
    "font_character": "Geometric sans-serif. Classical. Stable.",
    "body_size": "calc(D * 1)",
    "display_size": "calc(D * 8 * 0.25)",
    "h1_size": "calc(D * 8 * 0.2)",
    "font_weight_body": 500,
    "font_weight_header": 700,
    "letter_spacing": "normal",
    "line_height": 1.4,
    "numeric_style": "proportional-nums",
    "tonal_register": {
      "name": "planning",
      "character": "Calm, methodical, systematic",
      "voice": "The workout speaks to a competent adult. Direct, not flowery."
    }
  }
}
```

### Section 5: Personality (RPG Layer)

**This is the new layer.** Each zip code, abacus, and deck has a derived personality — a character class identity emerging from the SCL dimensions.

```json
{
  "personality": {
    "archetype_rank": 1,
    "archetype_name": null,
    "house": {
      "primary": { "emoji": "🤌", "name": "facio", "guild": "The Executors", "similarity": 0.94 },
      "secondary": { "emoji": "🚀", "name": "mitto", "guild": "The Launchers", "similarity": 0.78 },
      "tertiary": { "emoji": "🪵", "name": "teneo", "guild": "The Anchors", "similarity": 0.65 }
    },
    "neighborhood": {
      "abacus_memberships": [1, 2, 10],
      "primary_abacus": { "id": 1, "name": "General Strength", "domain": "Strength" },
      "district_character": "Heavy industry. Barbell district. Chalk dust and iron."
    },
    "city_position": {
      "building": "Strength Hall (Doric)",
      "floor": "Piano Nobile (Firmitas)",
      "wing": "Pull Wing",
      "room": "Structured Room",
      "neighborhood_density": "high",
      "foot_traffic": "heavy"
    },
    "difficulty_class": 4,
    "cns_demand": "high",
    "training_feel": "Heavy barbell pulls. Structured. Trackable. The room feels dense and purposeful."
  }
}
```

### Section 6: Connections (Graph)

```json
{
  "connections": {
    "neighbors": {
      "same_order": ["2113", "2133", "2143", "2153"],
      "same_axis": ["1123", "3123", "4123", "5123", "6123", "7123"],
      "same_type": ["2113", "2223", "2323", "2423", "2523", "2623"],
      "same_color": ["2121", "2122", "2124", "2125"]
    },
    "navigation_graph_edges": 4,
    "junction_suggestions": ["2124", "3123", "2223"],
    "abacus_membership": [
      { "id": 1, "name": "General Strength", "slot": "working", "slot_number": 3 },
      { "id": 2, "name": "Powerlifting", "slot": "working", "slot_number": 12 },
      { "id": 10, "name": "Athletic Hypertrophy", "slot": "bonus", "bonus_role": "variation" }
    ],
    "cosine_nearest_5": ["2124", "2223", "2133", "2122", "2113"],
    "cosine_farthest": "7358"
  }
}
```

### Section 7: Metadata

```json
{
  "metadata": {
    "deck": 7,
    "deck_name": "⛽🏛 Strength Basics",
    "status": "GENERATED",
    "card_path": "cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md",
    "operator_default": { "emoji": "🤌", "name": "facio" },
    "block_sequence": ["♨️", "▶️", "🧈", "🧩", "🪫", "🚂", "🧮"],
    "block_count": 7,
    "exercise_pool_size": 47,
    "weight_vector": [0, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
    "vector_magnitude": 16.0,
    "cosmogram_status": "DRAFT",
    "exercise_content_count": 12
  }
}
```

---

## Part III — Macro Aggregation (The New Math)

### Deck-Level Resolution

A deck is 40 zip codes (5 Types × 8 Colors) sharing the same Order × Axis. The deck's macro identity is the **centroid** of its 40 constituent weight vectors.

```python
def resolve_deck(deck_number: int) -> dict:
    zips = get_zips_for_deck(deck_number)
    vectors = [get_weight_vector(z) for z in zips]

    # Centroid: element-wise mean of all 40 vectors
    centroid = np.mean(vectors, axis=0)

    # The centroid IS the deck's weight vector
    # Feed it through the same resolution pipeline as a zip
    deck_identity = resolve_vector(centroid)

    # Add deck-specific fields
    deck_identity["macro"] = {
        "constituent_count": 40,
        "vector_spread": np.std(vectors, axis=0).mean(),  # How diverse are the zips?
        "dominant_colors": rank_by_weight(centroid, COLOR_INDICES),
        "dominant_operators": rank_operator_similarity(centroid),
        "art_style": derive_art_style(centroid),  # See Part V
        "neighborhood_character": derive_neighborhood(deck_number)
    }

    return deck_identity
```

The deck centroid naturally highlights the Order and Axis (they're shared across all 40 zips at +8) while averaging out Type and Color variation. This means the deck identity is dominated by its Order × Axis character — which is correct. A Strength × Basics deck feels like Strength × Basics regardless of which specific room you're in.

### Abacus-Level Resolution

An abacus is 48 zip codes drawn from across the system. Its centroid represents the training archetype's personality.

```python
def resolve_abacus(abacus_id: int) -> dict:
    zips = get_zips_for_abacus(abacus_id)
    vectors = [get_weight_vector(z) for z in zips]
    centroid = np.mean(vectors, axis=0)

    abacus_identity = resolve_vector(centroid)

    # Abacus-specific: which dimensions have the most variance?
    variance = np.var(vectors, axis=0)

    abacus_identity["macro"] = {
        "constituent_count": 48,
        "working_slots": 35,
        "bonus_slots": 13,
        "vector_spread": np.std(vectors, axis=0).mean(),
        "high_variance_dims": top_n_indices(variance, 10),   # Where does diversity live?
        "low_variance_dims": bottom_n_indices(variance, 10),  # What's consistent?
        "dominant_order_distribution": count_orders(zips),
        "dominant_color_distribution": count_colors(zips),
        "intercolumniation_demand": ABACUS_RECOVERY[abacus_id],
        "neighborhood_name": ABACUS_NAMES[abacus_id],
        "art_style": derive_art_style(centroid),
        "guild_affinity": rank_operator_similarity(centroid)  # Which House does this archetype belong to?
    }

    return abacus_identity
```

The abacus centroid captures the archetype's overall character. A Powerlifting abacus centroid will be heavy on ⛽ Strength, 🏟 Performance, 🏛 Basics, 🔵 Structured. A Yoga/Mobility abacus centroid will be heavy on 🖼 Restoration, 🌹 Aesthetic, ⚪ Mindful. The centroid IS the archetype's personality vector — and it feeds through the same resolution pipeline as a single zip.

### System-Level Resolution (The Full City)

The city itself has a centroid: the mean of all 1,680 vectors. This is the **neutral** identity — the system's resting state. It defines the fallback palette, the default typography, the baseline personality. Any zip code's character is measured as its deviation from this centroid.

```python
def resolve_city() -> dict:
    all_vectors = [get_weight_vector(z) for z in ALL_1680_ZIPS]
    city_centroid = np.mean(all_vectors, axis=0)

    # The city centroid should be near-zero on all primary dimensions
    # (each Order/Axis/Type/Color appears equally across 1,680 zips)
    # Non-zero values in derived dimensions reveal system-level biases

    return {
        "centroid": city_centroid.tolist(),
        "total_rooms": 1680,
        "buildings": 7,
        "floors": 6,
        "wings": 5,
        "rooms_per_wing": 8,
        "neighborhoods": 35,
        "districts": 42,
        "guilds": 12,
        "art_style": "The full city — all styles present, none dominant"
    }
```

---

## Part IV — Dual Register Rendering (Cathedral / Watercolor)

### The Principle

Dark mode and light mode are not the same design with inverted colors. They are two different rendering philosophies — two ways of seeing the same architectural space.

**Light Register: Watercolor**

The screen is a sheet of heavy watercolor paper. Colors are applied as transparent washes — layers of pigment over a bright ground. The paper shows through. Saturation is selective: the primary Color is a wash, everything else is pencil-gray tint. Shadows are cast by the light source, not by the UI framework.

This register is suited to: daytime use, outdoor reading, extended focus sessions, teaching contexts (⚫), restoration sessions (🖼⚪).

**Dark Register: Cathedral**

The screen is a stone interior lit by candlelight. The background is dark stone — not black, but the deep warm charcoal of basalt or slate. Colors appear as pools of warm light on dark surfaces — stained glass, gilded icons, illuminated manuscripts. The light is selective: it falls on what matters and leaves the rest in dignified shadow.

This register is suited to: evening use, focused intensity (🔴), technical precision (🟣), meditative work (⚪), performance testing (🏟).

### How the Weight Vector Drives Register Selection

The system does not ask the user to toggle dark mode. It suggests a register based on the zip code's weight vector and the time of day. The user can override.

```python
def suggest_register(zip_code: str, hour: int) -> str:
    vector = get_weight_vector(zip_code)

    # Time component: evening biases toward cathedral
    time_bias = 0.0
    if hour >= 20 or hour < 6:
        time_bias = 0.4  # Strong cathedral bias at night
    elif hour >= 17:
        time_bias = 0.2  # Moderate bias in evening

    # Color component: some Colors naturally suit cathedral
    cathedral_colors = {
        "🔴": 0.3,   # Intense — urgency reads better in candlelight
        "🟣": 0.25,  # Technical — precision against dark surface
        "⚪": 0.15,  # Mindful — contemplative darkness
        "⚫": 0.1,   # Teaching — blackboard aesthetic
    }
    watercolor_colors = {
        "🟢": 0.3,   # Bodyweight — outdoor light, paper
        "🟡": 0.25,  # Fun — brightness, curiosity
        "🟠": 0.15,  # Circuit — warmth, activity
        "🔵": 0.1,   # Structured — clean, systematic
    }

    color = parse_color(zip_code)
    color_bias = cathedral_colors.get(color, 0) - watercolor_colors.get(color, 0)

    # Order component: heavy orders suit cathedral, light orders suit watercolor
    order = parse_order(zip_code)
    order_bias = {
        "⛽": 0.15,   # Strength: weight, density → cathedral
        "🏟": 0.2,    # Performance: theatricality → cathedral
        "🐂": -0.15,  # Foundation: learning → watercolor (paper, pencil)
        "🖼": -0.1,   # Restoration: softness → watercolor (washes)
    }.get(order, 0)

    total = time_bias + color_bias + order_bias

    if total > 0.2:
        return "cathedral"
    elif total < -0.2:
        return "watercolor"
    else:
        return "user_preference"  # Ambiguous — defer to user setting
```

### Generating the Dark Register Palette

The dark register is NOT the light register with `filter: invert()`. It is architecturally generated:

```python
def generate_cathedral_palette(light_palette: dict, order_material: dict) -> dict:
    """
    Transform a light register palette into cathedral register.

    Principle: dark surfaces are the stone walls. Colors are candlelight
    falling on specific surfaces. The primary color becomes a warm pool
    of light, not a saturated background.
    """

    # Background: dark stone, not pure black
    # The Order's material hue tints the stone
    bg_hue = order_material["hue"]
    bg_sat = max(order_material["saturation"] * 0.5, 2)  # Very low sat, but not zero
    bg_light = 7  # Deep, but not black (preserves material identity)

    background = hsl(bg_hue, bg_sat, bg_light)
    surface = hsl(bg_hue, bg_sat, bg_light + 3)  # Slightly lighter stone for cards

    # Primary: the candlelight pool — warmer and lighter than the light register
    primary = shift_toward_warm(light_palette["primary"], amount=15)
    primary = adjust_lightness(primary, target=65)  # Glowing, not saturated

    # Text: warm parchment, not white
    text = hsl(35, 15, 82)  # Parchment — warm, readable, not clinical

    # Accent: gilded — shifted toward gold
    accent = shift_toward_warm(light_palette["accent"], amount=20)
    accent = adjust_saturation(accent, target=45)

    # Border: stone joint lines — barely visible
    border = hsl(bg_hue, bg_sat + 3, bg_light + 8)

    return {
        "name": "cathedral",
        "background": background,
        "surface": surface,
        "primary": primary,
        "text": text,
        "accent": accent,
        "border": border,
        "saturation_level": light_palette["saturation_level"] * 0.65,
        "contrast_ratio": ensure_wcag_aa(text, background)
    }
```

### Order Material in Cathedral Register

Each Order's classical building material defines its dark register character:

| Order | Light Register Material | Cathedral Register Character |
|-------|------------------------|------------------------------|
| 🐂 Foundation (Tuscan) | Rough-hewn travertine | Cave walls. Firelight on porous stone. The oldest rooms. |
| ⛽ Strength (Doric) | Pentelic marble | Polished obsidian. Cool candlelight on dark mirror. Sharp reflections. |
| 🦋 Hypertrophy (Ionic) | Carrara marble | Warm marble chapel. Votive candles in alcoves. Veining visible. |
| 🏟 Performance (Corinthian) | White marble + gilding | Grand cathedral nave. Spotlit altar. Maximum drama. |
| 🌾 Full Body (Composite) | Sandstone + terracotta | Crypt. Layered earth tones. Multiple lanterns. Organic warmth. |
| ⚖ Balance (Vitruvian) | Limestone | Scriptorium. Even desk-lamp lighting. Precise, calibrated. |
| 🖼 Restoration (Palladian) | Stucco + fresco | Dimmed fresco chapel. Frescoes barely visible in candlelight. Serene. |

---

## Part V — Art Direction by Aggregation Level

### The Insight

When you aggregate 40 zip vectors into a deck centroid, or 48 into an abacus centroid, the centroid's position in 61-dimensional space maps to an art style. Not randomly — the weight profile of the centroid describes visual qualities that correspond to art historical traditions.

### Deck Art Styles (42 decks)

The deck's Order × Axis intersection determines its dominant visual tradition. These are the art styles for deck-level views (0.25x zoom, browsing, discovery surfaces).

| Order × Axis | Art Direction | Rationale |
|-------------|--------------|-----------|
| 🐂🏛 (Deck 01) | **Tuscan workshop drawing** — charcoal on buff paper, teaching diagrams | Foundation + Basics = learning. Charcoal is the learning medium. |
| 🐂🔨 (Deck 02) | **Da Vinci anatomical study** — brown ink, mechanical precision | Foundation + Functional = body mechanics. Leonardo's Vitruvian Man. |
| 🐂🌹 (Deck 03) | **Matisse paper cut-out** — bold shapes, simple color, joyful | Foundation + Aesthetic = discovering beauty in basics. |
| ⛽🏛 (Deck 07) | **Doric temple elevation** — heavy line weight, marble, austere | Strength + Basics = classical power. The Parthenon. |
| ⛽🔨 (Deck 08) | **Soviet constructivist poster** — bold geometry, industrial | Strength + Functional = worker's power. Utilitarian strength. |
| ⛽🌹 (Deck 09) | **Greek bronze sculpture** — defined form, strong aesthetic | Strength + Aesthetic = sculpted power. Riace Bronzes. |
| 🦋🏛 (Deck 13) | **Renaissance proportion study** — golden ratios, human form | Hypertrophy + Basics = growth through classical means. |
| 🦋🌹 (Deck 15) | **Art Nouveau poster** — flowing organic line, ornamental | Hypertrophy + Aesthetic = the body as decorative art. |
| 🏟🏛 (Deck 19) | **Blueprint / technical drawing** — white on blue, precise | Performance + Basics = testing. The blueprint of capacity. |
| 🏟🪐 (Deck 22) | **Dramatic chiaroscuro** — Caravaggio lighting, peak moment | Performance + Challenge = the ultimate test. High contrast. |
| 🌾🏛 (Deck 25) | **Japanese ink wash (sumi-e)** — flow, integration, economy | Full Body + Basics = movement as calligraphy. |
| 🌾🔨 (Deck 26) | **Bauhaus functional design** — grid, module, unity | Full Body + Functional = integrated design system. |
| ⚖🏛 (Deck 31) | **Architectural section drawing** — precise, revealing hidden structure | Balance + Basics = exposing the hidden weakness. |
| 🖼🏛 (Deck 37) | **Watercolor landscape** — soft washes, open space, breath | Restoration + Basics = the gentlest room. |
| 🖼🌹 (Deck 39) | **Fresco — Pompeian wall painting** — warm earth, faded grandeur | Restoration + Aesthetic = somatic beauty. Ancient walls. |
| 🖼⚪ (cross) | **Mark Rothko field painting** — color and breath, nothing else | Restoration + Mindful = the deepest recovery. Pure field. |

The full 42-deck art direction table is populated by running the deck centroid through a style classifier trained on the weight dimensions:

```python
def derive_art_style(centroid: list) -> dict:
    """
    Map a centroid vector to an art direction.
    Uses dominant Order + Axis to select the tradition,
    then modulates by Color and Type distribution.
    """
    order = dominant_dim(centroid, ORDER_RANGE)
    axis = dominant_dim(centroid, AXIS_RANGE)

    base_style = ART_DIRECTION_MATRIX[order][axis]

    # Color distribution modulates the style
    color_profile = extract_range(centroid, COLOR_RANGE)
    if max_weight(color_profile, "intense") > 3:
        base_style["contrast"] = "high"
        base_style["saturation"] = "vivid"
    if max_weight(color_profile, "mindful") > 3:
        base_style["contrast"] = "low"
        base_style["saturation"] = "muted"

    return base_style
```

### Abacus Art Styles (35 neighborhoods)

The abacus centroid's art style represents the neighborhood's visual culture. Because abaci draw from across the deck system (multiple Orders, multiple Colors), their art direction is more varied and blended than a single deck's.

Example: The **Powerlifting abacus** centroid is heavy on ⛽ Strength and 🏟 Performance, with 🏛 Basics and 🔵 Structured dominant. Art direction: **Industrial steel and concrete** — heavy lines, minimal ornament, structural honesty, the aesthetic of a loading dock.

Example: The **Active Recovery abacus** centroid is heavy on 🖼 Restoration with ⚪ Mindful and 🌹 Aesthetic. Art direction: **Japanese garden** — negative space, stone, water, moss, deliberate emptiness.

---

## Part VI — The RPG Archetype System as City Infrastructure

### The 12 Guilds (Operator Houses)

The 12 operators already function as character classes. The compiler makes this explicit by resolving every zip code, deck, and abacus into its guild alignment.

```python
def resolve_guild_alignment(vector: list) -> dict:
    """
    Compute cosine similarity between input vector and all 12 operator profiles.
    Returns ranked guild affinity.
    """
    operator_profiles = load_operator_weight_profiles()

    similarities = {}
    for op_name, op_vector in operator_profiles.items():
        similarities[op_name] = cosine_similarity(vector, op_vector)

    ranked = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    return {
        "primary":   { "name": ranked[0][0], "similarity": ranked[0][1] },
        "secondary": { "name": ranked[1][0], "similarity": ranked[1][1] },
        "tertiary":  { "name": ranked[2][0], "similarity": ranked[2][1] },
        "anti":      { "name": ranked[-1][0], "similarity": ranked[-1][1] },
        "full_ranking": dict(ranked)
    }
```

### Guild Halls on the City Map

Each of the 12 guilds has a hall — a physical location on the city map. The guild hall is the zip code whose vector is most similar to the operator's weight profile. There are 12 guild halls in 1,680 rooms.

```python
def find_guild_halls() -> dict:
    """
    For each operator, find the zip code with highest cosine similarity.
    That zip is the guild hall — the operator's home address.
    """
    operator_profiles = load_operator_weight_profiles()
    all_vectors = load_all_weight_vectors()

    guild_halls = {}
    for op_name, op_vector in operator_profiles.items():
        best_zip = None
        best_sim = -1
        for zip_code, vector in all_vectors.items():
            sim = cosine_similarity(op_vector, vector)
            if sim > best_sim:
                best_sim = sim
                best_zip = zip_code
        guild_halls[op_name] = { "zip": best_zip, "similarity": best_sim }

    return guild_halls
```

### The Solo Leveling / RPG Archetype Naming Layer

Each zip code is a character in the city. Its archetype name emerges from:
1. Its dominant Order (class tier: Foundation=Apprentice, Strength=Warrior, etc.)
2. Its dominant Axis (specialization: Basics=Classic, Functional=Scout, etc.)
3. Its operator (guild: facio=Executor, mitto=Launcher, etc.)
4. Its Type (trade: Push=Smith, Pull=Mason, Legs=Runner, Plus=Alchemist, Ultra=Navigator)
5. Its Color (temperament: Teaching=Scholar, Intense=Berserker, Mindful=Monk, etc.)

The full archetype identity is a composite:

```
⛽🏛🪡🔵 → Warrior-Classic of the Executors Guild, Mason trade, Scholar temperament
                → short form: "The Disciplined Mason"
```

These names are NOT generated by combining random word lists. They are derived from the cosmogram research for each deck, grounded in cultural tradition per the publication standard. The compiler produces the raw classification. Cosmogram research produces the names.

### City Map — Figure and Ground

The figure-ground of the city is derived from the weight vectors of all 1,680 zips:

- **Dense districts** (high vector magnitude, many non-zero dimensions): ⛽ and 🏟 neighborhoods — heavy, complex, tightly packed
- **Open districts** (lower magnitude, more neutral dimensions): 🖼 and 🐂 neighborhoods — spacious, simple, breathing
- **Trade corridors** (high similarity between adjacent zips): Type-constant paths (all Pull rooms form a continuous street)
- **Guild quarters** (clusters of zips with similar operator affinity): The Executors cluster near ⛽🏛, the Anchors cluster near ⚖🪐

```python
def generate_city_map() -> dict:
    """
    Compute the full figure-ground of the Ppl± city.
    Returns density, clustering, corridors, and guild territories.
    """
    all_vectors = load_all_weight_vectors()

    # Density: magnitude of each vector
    densities = { z: np.linalg.norm(v) for z, v in all_vectors.items() }

    # Clustering: group by cosine similarity (DBSCAN or similar)
    clusters = cluster_by_similarity(all_vectors, threshold=0.85)

    # Corridors: sequences of high-similarity adjacent zips
    nav_graph = load_navigation_graph()
    corridors = find_high_similarity_paths(all_vectors, nav_graph)

    # Guild territories: which operator dominates each region
    guild_map = {}
    for z, v in all_vectors.items():
        guild_map[z] = resolve_guild_alignment(v)["primary"]["name"]

    return {
        "densities": densities,
        "clusters": clusters,
        "corridors": corridors,
        "guild_territories": guild_map
    }
```

---

## Part VII — The Compiler Script Specification

### Script Location

`scripts/middle-math/city_compiler.py`

### Dependencies

- `middle-math/weight-vectors.json` — 1,680 × 61-dim vectors
- `middle-math/design-tokens.json` — 8 Colors × 7 Orders visual tokens
- `middle-math/exercise-registry.json` — 2,085 exercises with SCL types
- `middle-math/exercise-engine/family-trees.json` — exercise families
- `middle-math/navigation-graph.json` — 6,720 edges
- `middle-math/abacus-registry.json` — 35 abaci × 48 zips
- `middle-math/weights/operator-weights.md` — 12 operator profiles
- `scripts/middle-math/weight_vector.py` — vector computation
- `scripts/middle-math/envelope_retrieval.py` — cosine similarity

### CLI Interface

```bash
# Resolve a single zip code
python scripts/middle-math/city_compiler.py ⛽🏛🪡🔵
python scripts/middle-math/city_compiler.py 2123

# Resolve a deck
python scripts/middle-math/city_compiler.py --deck 07

# Resolve an abacus
python scripts/middle-math/city_compiler.py --abacus 02

# Resolve a single emoji
python scripts/middle-math/city_compiler.py ⛽

# Resolve the full city (all 1,680 + 42 decks + 35 abaci)
python scripts/middle-math/city_compiler.py --city

# Output formats
python scripts/middle-math/city_compiler.py 2123 --format json    # Default
python scripts/middle-math/city_compiler.py 2123 --format css     # CSS custom properties
python scripts/middle-math/city_compiler.py 2123 --format summary # Human-readable

# Dark/light register
python scripts/middle-math/city_compiler.py 2123 --register cathedral
python scripts/middle-math/city_compiler.py 2123 --register watercolor
python scripts/middle-math/city_compiler.py 2123 --register auto   # Time-based suggestion

# Validation
python scripts/middle-math/city_compiler.py --validate            # Resolve all 1,680 and check consistency
```

### Output Files

```
middle-math/compiled/
├── city-resolution.json          # Full city: all 1,680 + 42 decks + 35 abaci resolved
├── deck-centroids.json           # 42 deck centroid vectors
├── abacus-centroids.json         # 35 abacus centroid vectors
├── guild-halls.json              # 12 guild hall zip codes
├── city-figure-ground.json       # Density, clustering, corridors, guild territories
├── art-direction-matrix.json     # 42 deck art styles
├── palette-registry-light.json   # 1,680 watercolor palettes
├── palette-registry-dark.json    # 1,680 cathedral palettes
└── archetype-classifications.json # 1,680 RPG class/guild/trade assignments
```

### Performance

The compiler processes all 1,680 zips + 42 decks + 35 abaci in a single batch. Expected runtime: <10 seconds on a modern machine. The output files are static JSON — they don't need recomputation unless the weight system changes. They are build artifacts, not runtime queries.

---

## Part VIII — How This Feeds Downstream Systems

### Experience Layer (Phase 4/5)

The compiled resolution object replaces ad-hoc style logic. A room page does:

```typescript
const resolution = await fetch(`/api/resolve/${zipNumeric}`);
const { architecture, palette, typography } = resolution;

// Apply as CSS custom properties
applyCSS(architecture);
applyCSS(palette[userRegister]);  // 'cathedral' or 'watercolor'
applyCSS(typography);
```

No style calculation at render time. The compiler has already done it.

### Operis (Editorial)

The daily Operis reads the day's zip resolution to determine:
- Art direction for the edition (from deck art style)
- Tonal register (from palette.typography.tonal_register)
- Featured neighborhoods (from connections.abacus_membership)
- Guild spotlight (from personality.house.primary)

### Wilson (Voice)

Wilson reads the resolution to determine:
- Tonal register for speech (from typography.tonal_register)
- Response density (from architecture.intercolumniation — wider spacing = slower, more spacious responses)
- Vocabulary register (from personality.difficulty_class — lower = simpler language)

### Abacus Selection UI

The abacus browser shows 35 neighborhoods, each with:
- Art style derived from the abacus centroid
- Guild affinity
- Color distribution pie chart
- Neighborhood character description (from personality.neighborhood.district_character)

### City Map View (0.1x zoom)

At maximum zoom-out, the city map renders from `city-figure-ground.json`:
- 7 buildings positioned by Order
- 42 districts colored by deck art style
- 35 neighborhoods overlaid as transparent zones
- 12 guild halls marked as landmarks
- Trade corridors (Type-constant paths) drawn as streets
- Density shown as building height / visual weight

---

## Part IX — Build Sequence

### Phase A: Core Compiler (scriptable now)

1. **Build `city_compiler.py`** — reads existing weight vectors, design tokens, and registries
2. **Implement zip resolution** — address + architecture + palette (light only) + typography + metadata
3. **Implement deck aggregation** — centroid computation for 42 decks
4. **Implement abacus aggregation** — centroid computation for 35 abaci
5. **Implement guild alignment** — cosine similarity against 12 operator profiles
6. **Implement connections** — read navigation graph, compute nearest neighbors
7. **Validate** — resolve all 1,680, check for consistency, WCAG compliance on palettes

### Phase B: Dark Register (requires design decisions)

8. **Implement cathedral palette generation** — the `generate_cathedral_palette` function
9. **Implement register suggestion** — time + zip → cathedral/watercolor
10. **Generate dual palette registry** — 1,680 × 2 = 3,360 palettes
11. **Test accessibility** — WCAG AA at every cathedral palette combination

### Phase C: Personality Layer (requires cosmogram research)

12. **Implement art direction matrix** — 42 deck styles from centroid analysis
13. **Implement archetype classification** — Order/Axis/Type/Color → class components
14. **Defer archetype naming** — names come from cosmogram research, not from the compiler
15. **Implement city figure-ground** — density, clustering, corridors, guild territories

### Phase D: Integration (requires experience layer)

16. **CSS custom property export** — compiler outputs CSS variables per zip
17. **API endpoint** — `/api/resolve/:zipNumeric` serving compiled JSON
18. **City map renderer** — SVG or Canvas rendering of the figure-ground
19. **Abacus browser art direction** — apply deck/abacus styles to UI

---

## Part X — Open Questions

1. **Art direction validation:** The 42-deck art style matrix needs human review. The compiler can suggest based on weight profiles, but Jake should approve the cultural associations. A Strength × Basics deck mapped to "Soviet constructivist poster" is a design decision, not a mathematical derivation.

2. **Cathedral palette warmth:** How warm should the candlelight be? Pure warm (all shadows warm-tinted) or varied by Color (🔵 Structured cathedral has cooler candlelight than 🔴 Intense cathedral)? The current spec varies by Color, but this needs visual testing.

3. **Archetype naming timeline:** The RPG archetype names require cosmogram research + publication standard proofing. The compiler produces the classification NOW. The names come LATER. This is correct — the math precedes the naming.

4. **City map as literal UI or conceptual model?** The figure-ground can be: (a) an actual rendered city map in the app (navigable, zoomable), or (b) a conceptual model that informs design decisions without being literally shown. Both are valid. The compiler supports either — it produces the data regardless.

5. **Abacus centroid stability:** When a user creates a custom abacus (adding/removing zips), the centroid shifts. Should the art direction and guild affinity update in real time? Or lock to the system abacus's identity?

6. **Intercolumniation as musical interval:** The classical intercolumniation types (Pycnostyle through Araeostyle) map to musical intervals. The D-module architecture already uses musical ratios for Palladian rooms. Should the spacing system formally adopt musical interval naming? 2D spacing = octave, 1.5D = fifth, etc.

7. **Seasonal art direction:** Should the art style shift by season? Spring editions of a Strength × Basics deck might feel different from autumn editions — same architectural identity, different light quality. The seasonal modifier in the palette section handles color temperature, but art direction is broader than color.

---

## Relationship to Existing Specifications

This seed **synthesizes** (does not replace) the following:

| Document | What This Seed Adds |
|----------|---------------------|
| `seeds/archideck-color-architecture.md` | Macro aggregation, dual register, art direction matrix, compiler script |
| `middle-math/weight-css-spec.md` | Compiler produces CSS variables directly |
| `middle-math/rendering/ui-weight-derivation.md` | Formalizes into Resolution Object schema |
| `seeds/digital-city-architecture.md` | Figure-ground computation, guild halls, density map |
| `seeds/abacus-architecture.md` | Abacus centroid computation, neighborhood personality |
| `seeds/heros-almanac-v8-architecture.md` | Guild alignment wired into resolution object |
| `seeds/elevator-architecture.md` | Superposition integrated into architecture section |
| `middle-math/design-tokens.json` | Extended with cathedral register and art direction tokens |
| `middle-math/navigation-graph.json` | Consumed by connections section |
| `middle-math/abacus-registry.json` | Consumed by macro aggregation |

---

🧮
