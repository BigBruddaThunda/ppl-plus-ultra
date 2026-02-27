---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 6/7
blocks: nothing in Phase 2-5
depends-on: seeds/platform-architecture-v2.md
connects-to: seeds/stripe-integration-pipeline.md, seeds/experience-layer-blueprint.md, seeds/regional-filter-architecture.md
---

# 🛡 Data Ethics Architecture — PPL± Privacy and User Data Specification

🔵⚫ — structured + teaching

## Preamble

PPL± is not affiliated with any political party, faction, or ideology. Jake Berry, the creator, is not PPL± itself. The system's position on data is a technical architecture decision that matches the character of the system: the user is the customer, not the product.

This document is technical architecture. It is not a marketing position. The constraints it specifies are enforced at the infrastructure level — not as policy, but as implementation.

---

## What PPL± Collects

PPL± collects only what the user explicitly provides through their own deliberate action. No passive collection. No inferred data. No behavioral fingerprinting.

**Collected:**

| Category | Data | Why |
|----------|------|-----|
| Account essentials | Email, password hash | Login and account recovery |
| Subscription state | Stripe customer ID, tier, billing dates | Gate access, manage billing |
| Workout logs | Zip code, date, sets logged, notes | Session history and personalization |
| Navigation history | Zip codes visited, floors accessed | Personal library and rotation engine |
| Equipment profile | User-declared toggles | Exercise filtering |
| Community contributions | Posts, replies (if user creates them) | Community floor content |
| Region preference | User-selected region, sub-region (text only) | Seasonal content framing |

**All collection is opt-in by action.** The user logs a workout → a log entry is created. The user selects a region → a region is stored. The user never acts → nothing is collected beyond the account essentials needed to operate the subscription.

---

## What PPL± Does NOT Collect

**No analytics fingerprinting.**
No session replay. No heatmaps. No click tracking. No scroll depth. No A/B test assignment. No cohort segmentation. No conversion funnel analysis.

**No third-party tracking cookies.**
No advertising pixels. No retargeting tags. No cross-site tracking identifiers.

**No behavioral profiling.**
No inference from behavior. No "users like you" modeling. No engagement scoring. No churn prediction against external datasets.

**No location data.**
No GPS. No IP geolocation beyond coarse country-level for fraud prevention (Stripe-handled, not stored). No timezone inference. Region is user-declared, not detected.

**No passive device signals.**
No device fingerprinting. No browser fingerprinting. No user agent logging beyond server-standard access logs. No battery status, accelerometer, gyroscope, camera, or microphone access outside of explicit user-initiated voice input.

**SDKs that are never initialized in the PPL± codebase:**

- Google Analytics (any version)
- Mixpanel
- Amplitude
- Segment
- Heap
- FullStory
- Hotjar
- LogRocket
- Intercom (tracking mode)
- Facebook Pixel
- Twitter/X Pixel
- TikTok Pixel
- Any advertising network SDK
- Any cross-site identity resolution SDK

If a future dependency inadvertently includes one of the above, it is removed before deployment. This is a hard constraint, not a soft preference.

---

## What PPL± Gives Back

### Full Data Export

Any user can request a complete export of all their data at any time. No waiting period. No customer support ticket. The export endpoint is available from the account settings page.

Export format: JSON. Contents: account metadata, subscription history, all workout logs, navigation history, equipment toggles, community contributions, region setting.

```
GET /api/user/export
Authorization: Bearer [user token]
Response: 200 OK, application/json
```

The export contains every row in every table where the user's ID appears. Nothing is omitted.

### Full Data Deletion

Any user can delete their account and all associated data at any time. No retention period. No "deactivation" that preserves data. Deletion is deletion.

```
DELETE /api/user/delete
Authorization: Bearer [user token]
Body: { "confirm": "DELETE MY ACCOUNT" }
Response: 200 OK — deletion cascade complete
```

The deletion cascade covers: auth.users (Supabase Auth), profiles, workout_logs, zip_visits, saved_workouts, program_sequence, community posts, community replies. Stripe subscription is cancelled via webhook before database deletion begins.

### Transparent Data Model

The schema is open. The tables are documented in `middle-math/schemas/`. Any user who wants to understand exactly what is stored can read the schema definitions. There are no hidden tables, hidden columns, or shadow profiles.

---

## Technical Implementation

### No Tracking Middleware

The Next.js middleware layer contains no analytics instrumentation. No page view events are fired to third-party services. The Vercel access logs (standard server logs, not user-behavioral analytics) are the only passive collection, and they are not stored beyond standard retention for debugging.

```typescript
// middleware.ts — what it does NOT contain
// ❌ analytics.track('page_view', { path, userId })
// ❌ segment.page({ name: path })
// ❌ gtag('event', 'page_view', { page_path: path })

// What it DOES contain
export function middleware(request: NextRequest) {
  // Auth token validation
  // Tier-based route protection
  // Nothing else
}
```

### Export Endpoint

```typescript
// /api/user/export/route.ts
export async function GET(req: Request) {
  const user = await getAuthUser(req);
  if (!user) return new Response('Unauthorized', { status: 401 });

  const [profile, logs, visits, saved, posts, toggles] = await Promise.all([
    supabase.from('profiles').select('*').eq('id', user.id).single(),
    supabase.from('workout_logs').select('*').eq('user_id', user.id),
    supabase.from('zip_visits').select('*').eq('user_id', user.id),
    supabase.from('saved_workouts').select('*').eq('user_id', user.id),
    supabase.from('community_posts').select('*').eq('user_id', user.id),
    supabase.from('user_exercise_toggles').select('*').eq('user_id', user.id),
  ]);

  return Response.json({
    exported_at: new Date().toISOString(),
    account: profile.data,
    workout_logs: logs.data,
    zip_visits: visits.data,
    saved_workouts: saved.data,
    community_posts: posts.data,
    exercise_toggles: toggles.data,
  });
}
```

### Deletion Endpoint

```typescript
// /api/user/delete/route.ts
export async function DELETE(req: Request) {
  const user = await getAuthUser(req);
  const body = await req.json();
  if (body.confirm !== 'DELETE MY ACCOUNT') {
    return new Response('Confirmation required', { status: 400 });
  }

  // 1. Cancel Stripe subscription
  await stripe.subscriptions.cancel(user.stripe_subscription_id);

  // 2. Delete all user data (cascade order matters)
  const tables = [
    'community_replies', 'community_posts',
    'user_exercise_toggles', 'program_sequence',
    'saved_workouts', 'zip_visits', 'workout_logs', 'profiles'
  ];
  for (const table of tables) {
    await supabase.from(table).delete().eq('user_id', user.id);
  }

  // 3. Delete auth record
  await supabase.auth.admin.deleteUser(user.id);

  return new Response('Account deleted', { status: 200 });
}
```

### RLS as Ethical Infrastructure

Supabase Row Level Security is not just an access control mechanism — it is the architectural guarantee that data isolation is enforced at the database level, not just at the application level. Even if application code has a bug, the database will not return another user's data.

```sql
-- profiles: users can only read/write their own row
CREATE POLICY "users_own_profile"
  ON profiles FOR ALL
  USING (auth.uid() = id);

-- workout_logs: users can only access their own logs
CREATE POLICY "users_own_logs"
  ON workout_logs FOR ALL
  USING (auth.uid() = user_id);

-- zip_metadata: public read, no write from application
CREATE POLICY "zip_metadata_public_read"
  ON zip_metadata FOR SELECT
  TO authenticated, anon
  USING (true);

-- community_posts: readable by tier, writable by own user
CREATE POLICY "community_posts_read"
  ON community_posts FOR SELECT
  TO authenticated
  USING (true);

CREATE POLICY "community_posts_write"
  ON community_posts FOR INSERT
  WITH CHECK (auth.uid() = user_id);
```

No service role key is exposed to the client. All writes go through the authenticated user's JWT, which Supabase validates against RLS policies before any mutation completes.

---

## Business Model Explanation

PPL± earns revenue through subscriptions: Tier 1 Library Card ($10/month) and Tier 2 Residency ($25-30/month). The subscription pays for the infrastructure, the content, and the ongoing development. The user's data is not a revenue source. There is no advertising product. There is no data licensing agreement. There is no investor whose interests conflict with the user's interests at the data layer.

This is why the ethics position is architecturally stable: the incentive structure supports it. Subscriptions require user trust. User trust requires data integrity. The architecture enforces what the business model requires.

---

## This Document's Scope

This document specifies technical constraints. It is not a legal privacy policy (that is a separate document, written by a lawyer). It is not a marketing statement. It is not a brand value declaration.

It is the blueprint that Session D (auth + profiles) and Session M (data export/deletion) will implement. When those sessions build, they build from this spec. The ethics are not bolted on after — they are specified before construction begins.

---

🧮
