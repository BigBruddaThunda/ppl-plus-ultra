# Ppl± Production Deployment Guide

## Prerequisites

- Vercel account (free tier works for launch)
- Supabase production project (separate from dev)
- Stripe account switched to live mode
- Custom domain (optional but recommended)

---

## Step 1: Supabase Production Setup

1. Create a new Supabase project for production
2. Run all SQL migrations in order in the SQL Editor:

```
sql/001-create-exercise-library.sql
sql/002-create-exercise-families.sql
sql/003-create-user-ledger.sql
sql/004-create-user-profile.sql
sql/005-create-user-toggles.sql
sql/006-create-zip-metadata.sql
sql/007-populate-zip-metadata.sql
sql/008-room-schema-extension.sql
sql/009-exercise-registry.sql
sql/010-exercise-knowledge.sql
sql/011-wave3-tables.sql
```

3. Verify tables exist: profiles, user_equipment, workout_sessions, set_logs, saved_rooms, zip_visits
4. Verify the `handle_new_user` trigger is active (creates profile row on signup)
5. Copy the production Supabase URL, anon key, and service role key

### Supabase Auth Config

In Supabase Dashboard > Authentication > URL Configuration:
- Site URL: `https://your-domain.com`
- Redirect URLs: `https://your-domain.com/auth/callback`

---

## Step 2: Stripe Live Mode

1. In Stripe Dashboard, switch to live mode (toggle at top)
2. Create two products matching dev:
   - **Library Card** — $10/month recurring
   - **Community Pass** — $25/month recurring
3. Copy the live price IDs for both products
4. Create a webhook endpoint:
   - URL: `https://your-domain.com/api/stripe/webhook`
   - Events to listen for:
     - `checkout.session.completed`
     - `customer.subscription.updated`
     - `customer.subscription.deleted`
5. Copy the webhook signing secret

---

## Step 3: Vercel Deployment

1. Go to vercel.com/new
2. Import the GitHub repo
3. Set the root directory to `web`
4. Framework preset: Next.js (auto-detected)
5. Add all environment variables from `.env.production.example` with real values:

| Variable | Source |
|----------|--------|
| NEXT_PUBLIC_SUPABASE_URL | Supabase Dashboard > Settings > API |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | Supabase Dashboard > Settings > API |
| SUPABASE_SERVICE_ROLE_KEY | Supabase Dashboard > Settings > API |
| STRIPE_SECRET_KEY | Stripe Dashboard > Developers > API keys |
| NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY | Stripe Dashboard > Developers > API keys |
| STRIPE_WEBHOOK_SECRET | Stripe Dashboard > Developers > Webhooks |
| STRIPE_TIER1_PRICE_ID | Stripe Dashboard > Products |
| STRIPE_TIER2_PRICE_ID | Stripe Dashboard > Products |
| NEXT_PUBLIC_STRIPE_TIER1_PRICE_ID | Same as STRIPE_TIER1_PRICE_ID |
| NEXT_PUBLIC_STRIPE_TIER2_PRICE_ID | Same as STRIPE_TIER2_PRICE_ID |

6. Deploy

---

## Step 4: Custom Domain (Optional)

1. Vercel Dashboard > Project > Settings > Domains
2. Add your domain
3. Update DNS records as instructed by Vercel
4. SSL is automatic

After domain is live, update:
- Supabase Auth > URL Configuration > Site URL
- Supabase Auth > URL Configuration > Redirect URLs
- Stripe webhook endpoint URL

---

## Step 5: Smoke Test

Run through each flow on the production URL:

- [ ] Homepage loads with today's room
- [ ] Navigate to a room (/zip/2123)
- [ ] Room renders workout card content
- [ ] Pinch-zoom shows block chips and deck map
- [ ] Signup creates account
- [ ] Onboarding flow completes (equipment + region)
- [ ] Dashboard shows after onboarding
- [ ] Subscribe to Library Card ($10) via Stripe checkout
- [ ] Tier updates after payment (check /me)
- [ ] Log a set on an exercise
- [ ] Session summary appears
- [ ] Save a room, verify in /me/library
- [ ] Voice parser routes correctly ("heavy pull day")
- [ ] Data export downloads JSON (/me/settings)
- [ ] Week strip navigates between days
- [ ] Deck page shows 40-room grid
- [ ] Mobile viewport works on phone

---

## Troubleshooting

**Webhook not firing:** Check Stripe Dashboard > Developers > Webhooks > Recent events. Verify the endpoint URL matches your production domain exactly.

**Auth redirect fails:** Verify Supabase redirect URL includes `/auth/callback` and matches your domain.

**Tier not updating after payment:** Check that `client_reference_id` is being passed in the checkout session. Verify webhook events are reaching the endpoint.

**Build fails on Vercel:** Run `npm run build` locally first. Check that all env vars are set in Vercel (missing vars cause build-time errors for NEXT_PUBLIC_ vars).
