---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 6
blocks: nothing in Phase 2-5
depends-on: seeds/platform-architecture-v2.md, seeds/data-ethics-architecture.md
connects-to: seeds/experience-layer-blueprint.md
---

# 💳 Stripe Integration Pipeline — Subscription Products, Checkout, Webhooks, RLS Gating

🔵🟣 — structured + technical

## One Sentence

PPL± runs two Stripe subscription products — Tier 1 Library Card ($10/month) and Tier 2 Residency ($25-30/month) — with Stripe Checkout for purchase, Customer Portal for self-service management, and a webhook handler that updates Supabase profile tier on every subscription lifecycle event, with Supabase RLS enforcing access gating at the database level.

---

## Subscription Products

### Tier 1 — Library Card

**Price:** $10/month (or ~$96/year if annual offered)
**Stripe product name:** `ppl_library_card`
**Stripe price ID:** `price_[id]` (set in environment)

**Access unlocks:**
- All 1,680 room interactives (workout rendering + logging)
- Personal workout history and statistics
- Saved rooms library
- Equipment toggle system
- Exercise substitution engine
- Regional content filter
- Session timer

**Does not unlock:**
- Community floor (🐬) — Tier 2 only
- Coaching integration — Tier 2 only
- Program builder — Tier 2 only

### Tier 2 — Residency

**Price:** $25-30/month (final price TBD before launch)
**Stripe product name:** `ppl_residency`
**Stripe price ID:** `price_[id]` (set in environment)

**Access unlocks:** Everything in Tier 1, plus:
- Community floor (🐬) — posts, replies, threads
- Program builder (custom multi-week sequences)
- Coaching mode (log sharing, progress export for coaches)
- Priority junction suggestions (personalized rotation recommendations)
- Early access to new decks and features

### Free Tier (no subscription)

**Access:**
- Operis read (web + car audio)
- Zip code previews (workout title, block list, time estimate — no full content)
- Exercise library browse (names and descriptions — no workout context)
- Almanac (seasonal framing only)
- Regional Operis audio

---

## Complete Signup → Access Flow

```
1. User lands on /subscribe
2. Selects Tier 1 or Tier 2
3. Redirected to Stripe Checkout (hosted page)
4. Stripe processes payment
5. Stripe fires checkout.session.completed webhook
6. PPL± webhook handler:
   a. Verifies Stripe signature
   b. Looks up user by email (supabase.auth.admin.listUsers)
   c. Updates profiles: { stripe_customer_id, tier, subscription_id, subscription_status: 'active' }
7. User redirected to /me (success URL)
8. On next request, Supabase RLS sees tier = 1 (or 2)
9. User accesses full room content
```

---

## Webhook Events Table

| Stripe Event | PPL± Action |
|-------------|------------|
| `checkout.session.completed` | Set tier, store customer_id + subscription_id |
| `customer.subscription.updated` | Update tier (upgrade/downgrade), update status |
| `customer.subscription.deleted` | Set tier = 0, status = 'cancelled' |
| `invoice.payment_succeeded` | Update subscription_period_end |
| `invoice.payment_failed` | Set status = 'past_due', trigger email via Resend |
| `customer.subscription.paused` | Set status = 'paused' |
| `customer.subscription.resumed` | Set status = 'active' |

No other Stripe events require PPL± action. Ignore all others with a 200 OK response.

---

## Webhook Handler

```typescript
// /api/stripe/webhook/route.ts
import Stripe from 'stripe';
import { createClient } from '@supabase/supabase-js';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);
const supabaseAdmin = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!
);

export async function POST(req: Request) {
  const body = await req.text();
  const sig = req.headers.get('stripe-signature')!;

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
  } catch (err) {
    return new Response('Webhook signature verification failed', { status: 400 });
  }

  switch (event.type) {
    case 'checkout.session.completed': {
      const session = event.data.object as Stripe.Checkout.Session;
      const customerId = session.customer as string;
      const subscriptionId = session.subscription as string;
      const email = session.customer_details?.email;
      const tier = session.metadata?.tier === '2' ? 2 : 1;

      // Find user by email
      const { data: { users } } = await supabaseAdmin.auth.admin.listUsers();
      const user = users.find(u => u.email === email);
      if (!user) break;

      await supabaseAdmin.from('profiles').update({
        stripe_customer_id: customerId,
        stripe_subscription_id: subscriptionId,
        subscription_status: 'active',
        tier,
      }).eq('id', user.id);
      break;
    }

    case 'customer.subscription.updated': {
      const sub = event.data.object as Stripe.Subscription;
      const tier = sub.metadata?.tier === '2' ? 2 : 1;
      await supabaseAdmin.from('profiles').update({
        subscription_status: sub.status,
        tier: sub.status === 'active' ? tier : 0,
        subscription_period_end: new Date(sub.current_period_end * 1000).toISOString(),
      }).eq('stripe_customer_id', sub.customer);
      break;
    }

    case 'customer.subscription.deleted': {
      const sub = event.data.object as Stripe.Subscription;
      await supabaseAdmin.from('profiles').update({
        subscription_status: 'cancelled',
        tier: 0,
      }).eq('stripe_customer_id', sub.customer);
      break;
    }

    case 'invoice.payment_failed': {
      const invoice = event.data.object as Stripe.Invoice;
      await supabaseAdmin.from('profiles').update({
        subscription_status: 'past_due',
      }).eq('stripe_customer_id', invoice.customer);
      // TODO: trigger Resend email
      break;
    }
  }

  return new Response('OK', { status: 200 });
}
```

---

## Profiles Table — Stripe Columns

```sql
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS
  stripe_customer_id       TEXT UNIQUE,
  stripe_subscription_id   TEXT UNIQUE,
  subscription_status      TEXT DEFAULT 'free'
    CHECK (subscription_status IN ('free','active','past_due','cancelled','paused')),
  tier                     SMALLINT NOT NULL DEFAULT 0
    CHECK (tier IN (0, 1, 2)),
  subscription_period_end  TIMESTAMPTZ;
```

**tier values:**
- 0 = Free
- 1 = Library Card
- 2 = Residency

---

## RLS Gating Tiers

```sql
-- Public content: visible to all (including unauthenticated)
CREATE POLICY "zip_previews_public"
  ON zip_metadata FOR SELECT
  TO anon, authenticated
  USING (true);

-- Tier 1+ content: full room access
CREATE POLICY "workout_content_tier1"
  ON workout_logs FOR ALL
  TO authenticated
  USING (
    auth.uid() = user_id
    AND EXISTS (
      SELECT 1 FROM profiles
      WHERE id = auth.uid() AND tier >= 1
    )
  );

-- Tier 2 only: community posts
CREATE POLICY "community_tier2_read"
  ON community_posts FOR SELECT
  TO authenticated
  USING (
    EXISTS (
      SELECT 1 FROM profiles
      WHERE id = auth.uid() AND tier >= 2
    )
  );

CREATE POLICY "community_tier2_write"
  ON community_posts FOR INSERT
  TO authenticated
  WITH CHECK (
    auth.uid() = user_id
    AND EXISTS (
      SELECT 1 FROM profiles
      WHERE id = auth.uid() AND tier >= 2
    )
  );
```

---

## Environment Variables

```bash
# Stripe keys (never expose to client)
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Stripe product price IDs
STRIPE_PRICE_TIER1_MONTHLY=price_...
STRIPE_PRICE_TIER2_MONTHLY=price_...

# Stripe publishable key (safe for client)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...

# Supabase (service role key — never expose to client)
SUPABASE_SERVICE_ROLE_KEY=eyJ...

# Supabase (anon/public key — safe for client)
NEXT_PUBLIC_SUPABASE_URL=https://[project].supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
```

**Security notes for Claude Code sessions:**
- Never log `STRIPE_SECRET_KEY` or `SUPABASE_SERVICE_ROLE_KEY` in console output
- Never include either in client-side code or Next.js page props
- The webhook handler must verify the Stripe signature before processing any event
- The `supabaseAdmin` client (using service role key) is only instantiated in server-side API routes
- Test webhooks via `stripe listen --forward-to localhost:3000/api/stripe/webhook` during development

---

## Customer Portal

Stripe Customer Portal handles all subscription management: upgrade, downgrade, cancel, update payment method. PPL± does not build any of this UI.

```typescript
// /api/stripe/portal/route.ts
export async function POST(req: Request) {
  const user = await getAuthUser(req);
  const profile = await supabase.from('profiles')
    .select('stripe_customer_id').eq('id', user.id).single();

  const session = await stripe.billingPortal.sessions.create({
    customer: profile.data.stripe_customer_id,
    return_url: `${process.env.NEXT_PUBLIC_BASE_URL}/me/settings`,
  });

  return Response.json({ url: session.url });
}
```

The `/me/settings` page includes a "Manage Subscription" button that calls this endpoint and redirects to the Stripe-hosted portal.

---

## Build Session Reference

This pipeline is implemented in **Session F** of `seeds/claude-code-build-sequence.md`.

Pre-Session F dependencies: Session D (auth + profiles table) must be complete before Stripe columns can be added to profiles.

---

🧮
