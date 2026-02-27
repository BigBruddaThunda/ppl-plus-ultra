---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 6+
blocks: nothing in Phase 2-5
depends-on: seeds/platform-architecture-v2.md, seeds/data-ethics-architecture.md, seeds/operis-architecture.md
connects-to: seeds/automotive-layer-architecture.md, seeds/voice-parser-architecture.md
---

# 🌍 Regional Filter Architecture — Opt-In Seasonal Content, No GPS, No Tracking

🔵⚪ — structured + mindful

## The Principle

The user tells the system where they are. The system does not find out.

No GPS. No IP geolocation. No device locale interrogation. No inferred region from browser language or timezone. The user opens a two-level picker and selects a region. That selection is stored in their profile. It can be changed at any time. It can be left blank. Blank means no regional context — Operis is written in universal language, no seasonal framing.

This is the same data ethics position applied specifically to geography: the user is the source of all data. Nothing is detected, inferred, or tracked. The user is in control.

---

## What The Region Changes

Regional setting adjusts content that is contextually tied to geography and season. It does not change workout content. The SCL system is geographically universal — a hip hinge is a hip hinge in Oslo and Nairobi. The zip code is unchanged.

**What adjusts with region:**

| Content area | How region affects it |
|-------------|----------------------|
| Seasonal Operis framing | "Late winter in the Northeast" vs "Dry season begins" |
| Almanac content | Which of the 12 operators maps to the current month's seasonal reality |
| Historical desk context | Regional agricultural and historical references in Operis departments |
| Wilson's Operis intro | Brief environmental observation ("A cold morning." / "The light is lengthening.") |
| Restoration notes | Regional relevance for outdoor movement, nature exposure, seasonal rhythm |

**What does NOT change with region:**

| Content area | Reason |
|-------------|--------|
| Zip codes | Universal 4-digit addressing, geography-independent |
| Exercise library | Exercises are not regional |
| Workout content | Sets, reps, cues, blocks — all universal |
| Operator definitions | SCL vocabulary is fixed |
| Stripe pricing | Single global pricing |
| Subscription tiers | Same worldwide |
| Community content | User-generated, not regionally filtered |

The region is a content lens, not a content gate. Users without a region set still have full access to everything. They just receive Operis in universal language instead of regionally-framed language.

---

## How The User Sets Region

**Two-level picker (in onboarding and /me/settings):**

**Level 1 — Broad region (required if using region feature):**
- North America
- Latin America
- Europe (Northern)
- Europe (Mediterranean)
- Sub-Saharan Africa
- North Africa / Middle East
- South Asia
- East Asia
- Southeast Asia
- Oceania / Pacific

**Level 2 — Sub-region (optional, refines seasonal specificity):**

For North America:
- Pacific Coast
- Mountain West
- Great Plains / Midwest
- Gulf Coast / Southeast
- Mid-Atlantic
- New England / Maritime Northeast
- Ontario / Great Lakes
- Prairies
- Pacific Northwest (Canada)
- Alaska / Far North

For other Level 1 regions: similar sub-region lists with 8-12 options each. Sub-regions map to meaningful seasonal distinctions within the broader region.

**UI implementation:** Standard two-step select, not a map. No visual map needed. The user knows where they live. "Select your region" → dropdown → "Select sub-region (optional)" → dropdown.

---

## Database Columns

```sql
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS
  region       TEXT,      -- e.g. 'north_america'
  sub_region   TEXT;      -- e.g. 'new_england'
```

No validation constraints on these columns — future regions may be added without migration. The content pipeline validates the values. Invalid or unknown values fall back to universal language.

---

## Content Pipeline Implications

### What Needs Regional Variants

The Operis publishing pipeline generates one version of each piece of regionally-sensitive content per region × month combination.

**Volume estimate:**
- 10 broad regions × 12 months = 120 base seasonal sentences (Operis intro context)
- 15 sub-regions × 12 months × 3 Operis departments with seasonal framing = 540 sentences
- Historical desk: ~100 regional references per broad region = 1,000 entries

Total authored content with regional variants: ~1,700 sentences across 10 regions.

This is a manageable authoring scope. It does not scale with zip codes (which are universal). It scales with regions × months, which is a fixed and bounded set.

### What Does NOT Need Regional Variants

- Workout card content (1,680 cards, all universal)
- Exercise library (universal)
- Operator definitions (universal)
- Block descriptions (universal)
- SCL vocabulary (universal)

Regional content is a thin layer on top of universal content. The vast majority of the system is unchanged.

---

## Tier Implications

**Recommended: Include regional filter in Tier 1 (Library Card).**

Rationale:
- Regional framing adds meaningful value to the Operis reading experience
- It differentiates the experience without requiring additional infrastructure beyond profile columns and content variants
- Free-tier Operis is written in universal language — regional Operis is a Tier 1 enhancement
- The car layer (Operis read-aloud) benefits from regional framing because it makes the content feel specifically relevant to the user's morning

**Option B (considered, not recommended): Include in Free Tier.**
Regional framing as a free feature has conversion benefits (more personalization early), but reduces the premium feel of Tier 1. Recommendation: keep it as a Tier 1 feature and mention it explicitly in the upgrade CTA ("Your Operis, tuned to where you are").

---

## Build Session

**Session E-2** — A sub-session of Session E (Onboarding).

When building Session E:
1. Add region picker as Step 2 of onboarding (after equipment selection)
2. Store region and sub_region to profiles
3. Display region setting in /me/settings with quick-change capability
4. Wire Operis content pipeline to region value (at Session I — Operis implementation)

The region columns are created in Session E. The content pipeline that uses them is implemented in Session I (Operis). They are decoupled — creating the preference does not require the pipeline to be built simultaneously.

---

## Privacy Audit Notes

Per `seeds/data-ethics-architecture.md`:
- Region is stored as user-provided text, not detected data
- Sub-region is optional — blank is a valid state
- Export endpoint (`/api/user/export`) includes region and sub_region fields
- Deletion endpoint removes them as part of the profiles row deletion
- No third-party service receives the region value
- The region is not used for any purpose other than content framing

This is the minimum viable regional personalization: maximum content relevance, zero privacy cost.

---

🧮
