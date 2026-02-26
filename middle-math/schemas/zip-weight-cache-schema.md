# Zip Weight Cache Schema

Status: OPTIONAL — Pre-computed weight vector table. The system can derive weights on the fly from the weight declaration files; this table caches the results for performance.

---

## When to Use This Table

The weight vector for any given zip code is deterministic: same zip = same vector every time. There are 1,680 possible zip codes. Pre-computing all 1,680 weight vectors once and caching them eliminates per-request computation.

**Use this table when:**
- The weight computation (loading 7 weight files, cascading weights, resolving interactions) becomes a measurable performance bottleneck
- The 1,680-row table is cheaper than per-request computation at scale

**Skip this table when:**
- Early development: compute weights on the fly for ease of iteration
- Weight declarations change frequently: cached values become stale on each update

This is a performance optimization, not an architectural requirement.

---

## Table: zip_weight_cache

```sql
CREATE TABLE zip_weight_cache (
  zip_code              TEXT PRIMARY KEY,           -- "⛽🏛🪡🔵"

  -- The 61-emoji weight vector (stored as JSONB for flexibility)
  weight_vector         JSONB NOT NULL,
  -- Example:
  -- {
  --   "🐂": -2, "⛽": 8, "🦋": -3, "🏟": -3, "🌾": -3, "⚖": -3, "🖼": -4,
  --   "🏛": 8, "🔨": 2, "🌹": -3, "🪐": 4, "⌛": -2, "🐬": -1,
  --   "🛒": -2, "🪡": 8, "🍗": -2, "➕": -2, "➖": -3,
  --   "⚫": 2, "🟢": -4, "🔵": 8, "🟣": 3, "🔴": -3, "🟠": -4, "🟡": -2, "⚪": -4,
  --   "♨️": 7, "▶️": 7, "🧈": 8, "🧩": 6, "🪫": 5, "🚂": 7, ...
  -- }

  -- Metadata
  computed_at           TIMESTAMP DEFAULT NOW(),
  weight_spec_version   TEXT NOT NULL,             -- Which version of the weight declarations produced this
  is_valid              BOOLEAN NOT NULL DEFAULT true
);
```

---

## Cache Invalidation

When weight declaration files change (e.g., when axis-weights.md is populated with full data), the cache must be invalidated and recomputed:

```sql
-- Invalidate all cached vectors (trigger recomputation)
UPDATE zip_weight_cache
SET is_valid = false, computed_at = NOW()
WHERE weight_spec_version != $1;  -- $1 = new weight spec version

-- Recompute (application code, not SQL)
-- Run the weight computation for all 1,680 zip codes
-- INSERT ... ON CONFLICT DO UPDATE for each
```

---

## Temporal Weight Separation

The zip_weight_cache does NOT store temporal weights (the ±1 date-derived nudges). Temporal weights are applied at request time on top of the cached static vector.

```
cached_static_vector = zip_weight_cache[zip_code]
temporal_nudge = compute_temporal_weights(current_date)
final_vector = merge(cached_static_vector, temporal_nudge)
```

This keeps the cache stable (valid for all time regardless of date) while still applying the temporal layer at runtime.

---

## All 1,680 Zip Code Coverage

All 7 × 6 × 5 × 8 = 1,680 valid zip codes have entries in this table once populated. Invalid zip codes (e.g., emojis from the wrong category in the wrong position) are not included.

---

🧮
