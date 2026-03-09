# Ppl± Local Development Operations Manual

**Planted:** 2026-03-09
**Status:** SEED — Reference document. Follow it step by step.
**Audience:** Jake Berry (project creator, non-coder, ADHD-friendly format)
**Purpose:** Everything needed to go from "I have ideas in documentation" to "I can click an icon on my PC and see my project running"

---

## The Big Picture (30 seconds)

```
Your brain        → Claude Code (builds it)
Claude Code       → Your local machine (runs it)
Your local machine → GitHub (stores it)
GitHub            → Vercel (hosts it live)
Vercel            → The internet (people use it)
```

You already have the first two. This document gets you the rest.

---

## Phase 0: What You Already Have

- [x] Claude Max subscription (Claude Code access included)
- [x] GitHub account (BigBruddaThunda)
- [x] Ppl± repository (ppl-plus-ultra)
- [x] Complete SCL architecture (CLAUDE.md, scl-directory.md, 60+ seeds)
- [x] Middle-math computation engine (weight vectors, exercise selector, city compiler)
- [x] 102 generated workout cards
- [x] Claude Code experience via web (claude.ai/code)

What you do NOT have yet (this document fixes these):
- [ ] Claude Code running locally on your PC
- [ ] Node.js / development environment
- [ ] Next.js project initialized
- [ ] Supabase database
- [ ] Vercel deployment
- [ ] Stripe integration
- [ ] Local development server ("click icon, see project")

---

## Phase 1: Your Windows PC Setup (15 minutes)

### Step 1: Install Git for Windows

Git is the version control system. You need it before anything else.

1. Go to: https://git-scm.com/downloads/win
2. Download the installer
3. Run it. Accept all defaults. Click Next through everything.
4. When done, open PowerShell and type: `git --version`
5. You should see something like `git version 2.44.0`

### Step 2: Install Claude Code

Open PowerShell (search "PowerShell" in Start menu) and paste:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Wait for it to finish. Then type:

```powershell
claude --version
```

You should see a version number. Claude Code is installed.

### Step 3: Connect Claude Code to Your Account

```powershell
claude login
```

This opens your browser. Log in with your existing Claude Max account. Done.

### Step 4: Clone Your Repository Locally

Pick a folder on your PC where you want your project to live. Example: `C:\Projects\`

```powershell
mkdir C:\Projects
cd C:\Projects
git clone https://github.com/BigBruddaThunda/ppl-plus-ultra.git
cd ppl-plus-ultra
```

### Step 5: Run Claude Code in Your Project

```powershell
claude
```

That's it. You're now running Claude Code locally with full access to your repository. Everything you can do in the web version, you can do here. Faster. With file system access.

### Step 6: Verify Everything Works

Inside Claude Code, try:

```
python scripts/middle-math/city_compiler.py 2123 --format summary
```

If you see the zip code resolution output, everything is connected.

---

## Phase 2: Install Node.js (5 minutes)

Node.js is the runtime that Next.js (your web framework) runs on.

1. Go to: https://nodejs.org
2. Download the **LTS** version (not Current)
3. Run the installer. Accept all defaults.
4. Restart PowerShell, then verify:

```powershell
node --version    # Should show v20.x or v22.x
npm --version     # Should show 10.x+
```

---

## Phase 3: Project Initialization (Claude Code does this for you)

Once Node.js is installed, you tell Claude Code to initialize the Next.js project. You do not need to know how — Claude Code knows.

From your project directory in Claude Code:

```
Initialize the Next.js project for Ppl± using the experience-layer-blueprint.md
and platform-architecture-v2.md specs. Set up:
- Next.js 14+ with App Router and TypeScript
- Tailwind CSS with our design tokens from middle-math/design-tokens.json
- The /zip/[code] dynamic route
- Basic project structure matching our seed architecture
```

Claude Code will create the files, install dependencies, and configure everything.

---

## Phase 4: The "Click Icon, See Project" Setup

After the Next.js project is initialized:

### Start the development server:

```powershell
cd C:\Projects\ppl-plus-ultra
npm run dev
```

This starts a local server. Open your browser to: **http://localhost:3000**

You see your project. Running. On your machine.

### Create a desktop shortcut:

1. Right-click your Desktop → New → Shortcut
2. Location: `powershell.exe -Command "cd C:\Projects\ppl-plus-ultra; npm run dev; Start-Process http://localhost:3000"`
3. Name it: "Ppl± Dev"
4. Click icon → project opens

---

## Phase 5: External Services (Create Accounts)

These are the services your project will use. Create accounts now. Configure later (Claude Code handles the configuration).

### Must-Have (before first deploy):

| Service | URL | What It Does | Free Tier? | When You Need It |
|---------|-----|-------------|------------|------------------|
| **Vercel** | https://vercel.com | Hosts your website live on the internet | Yes (generous) | When you want to show anyone |
| **Supabase** | https://supabase.com | Database, user accounts, authentication | Yes (500MB) | When you add user accounts |

### Need Soon (before payment features):

| Service | URL | What It Does | Free Tier? | When You Need It |
|---------|-----|-------------|------------|------------------|
| **Stripe** | https://stripe.com | Subscription payments ($10/$25 tiers) | Yes (test mode) | When you add paid tiers |
| **Resend** | https://resend.com | Sends emails (welcome, receipts) | Yes (100/day) | When you add email |

### Nice-to-Have (can wait):

| Service | URL | What It Does | When |
|---------|-----|-------------|------|
| **Sentry** | https://sentry.io | Error tracking | After launch |
| **PostHog** | https://posthog.com | Privacy-friendly analytics | After launch |

### Account Creation Checklist:

- [ ] Vercel — sign up with GitHub (automatic repo connection)
- [ ] Supabase — sign up, create a project named "ppl-plus-ultra"
- [ ] Stripe — sign up, enable test mode
- [ ] Resend — sign up, verify domain later

Save all credentials in a password manager. Never paste them into files that get committed to GitHub.

---

## Phase 6: Deploy to the Internet (Vercel)

Once you have a Vercel account connected to your GitHub:

1. Go to https://vercel.com/dashboard
2. Click "Add New Project"
3. Import your ppl-plus-ultra repository
4. Vercel auto-detects Next.js. Click Deploy.
5. Your project is live at: `https://ppl-plus-ultra.vercel.app` (or similar)

Every time you push code to GitHub, Vercel automatically redeploys. No manual step.

---

## Phase 7: Connect Supabase (Database)

When you're ready for user accounts and data:

1. Go to https://supabase.com/dashboard
2. Create a new project: "ppl-plus-ultra"
3. Copy the Project URL and anon key from Settings → API
4. In your project, create a `.env.local` file (Claude Code can do this):

```
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

**IMPORTANT:** `.env.local` is in `.gitignore` — it never gets committed to GitHub. Your keys stay private.

---

## Tool Reference Card

Quick reference for everything installed and where to find it.

### On Your PC:

| Tool | What It Is | How to Run | Where It Lives |
|------|-----------|------------|----------------|
| Git | Version control | `git` in PowerShell | Program Files |
| Claude Code | AI coding assistant | `claude` in PowerShell | Auto-installed |
| Node.js | JavaScript runtime | `node` in PowerShell | Program Files |
| npm | Package manager | `npm` in PowerShell | Comes with Node |
| Python | Script runner | `python` or `python3` | May need install |

### In Your Repository:

| Path | What It Is |
|------|-----------|
| `CLAUDE.md` | Claude Code's operating instructions for your project |
| `whiteboard.md` | Current session state and active tasks |
| `scl-directory.md` | Complete SCL language reference |
| `exercise-library.md` | All 2,185 exercises |
| `cards/` | The 1,680 workout cards (102 generated, 1,578 stubs) |
| `seeds/` | 60+ architectural seed documents |
| `scripts/` | Automation tools (validators, generators, compilers) |
| `middle-math/` | Computation engine (weight vectors, registries, JSON data) |
| `deck-identities/` | Per-deck identity documents |
| `deck-cosmograms/` | Deep research identity documents |

### Scripts You Can Run:

```powershell
# Progress dashboard
python scripts/progress-report.py

# Validate a card
python scripts/validate-card.py cards/path/to/card.md

# City compiler (resolve any zip)
python scripts/middle-math/city_compiler.py 2123 --format summary

# Exercise coverage audit
python scripts/exercise-usage-report.py

# Inventory sweep
python scripts/inventory.py
```

### In Claude Code (slash commands):

```
/generate-card ⛽🌹🛒🔵    # Generate a workout card
/build-deck-identity 09     # Build deck identity document
/progress-report            # Run progress dashboard
/retrofit-deck 07           # Upgrade old deck to V2
```

---

## How to Talk to Claude Code

Claude Code understands natural language. You do not need to write code. Examples:

**Starting a work session:**
```
Read whiteboard.md and tell me what needs to happen next.
```

**Building something:**
```
Initialize the Next.js project following seeds/experience-layer-blueprint.md.
Set up the /zip/[code] route that renders workout cards.
```

**Fixing something:**
```
The build is broken. Fix whatever is causing the error.
```

**Exploring ideas:**
```
Read seeds/guild-campaign-architecture.md and tell me what
infrastructure we'd need to build the party formation system.
```

**Generating cards:**
```
Generate the next 5 cards in Deck 10.
```

Claude Code reads your CLAUDE.md automatically. It knows your project structure, your naming conventions, your validation rules. You give it the intent. It does the work.

---

## Android Setup

The official Claude Android app includes Claude Code functionality:

1. Install the Claude app from Google Play
2. Log in with your Max account
3. You can start tasks, monitor progress, and issue commands from your phone

For more hands-on mobile development, check out Happy (https://happy.engineering/) — a free open-source mobile client for Claude Code.

Mobile is best for:
- Reviewing what Claude Code built while you're away from your PC
- Starting long-running tasks (card generation, deck audits) remotely
- Reading seeds and documentation
- Quick questions about your project

Your PC is best for:
- Running the local dev server
- Building and testing the web app
- Heavy generation sessions
- Anything that involves seeing the UI in a browser

---

## The ADHD-Friendly Workflow

Your setup is designed for minimal friction:

1. **Sit down at PC.** Open PowerShell. Type `claude` in your project folder.
2. **Tell Claude Code what you want to work on.** Natural language. No commands to memorize.
3. **Claude Code reads whiteboard.md** and knows what's active, what's blocked, what's next.
4. **Work happens.** Claude Code writes code, generates cards, runs validators.
5. **When done,** Claude Code commits to GitHub. Vercel auto-deploys. You see it live.
6. **Walk away.** Your progress is saved. Next session picks up where you left off.

No context switching. No "what was I doing?" The whiteboard remembers. Claude Code remembers. The system holds state so you don't have to.

---

## What You Do NOT Need to Learn

- **HTML/CSS** — Claude Code writes this
- **JavaScript/TypeScript** — Claude Code writes this
- **SQL** — Claude Code writes this
- **Git commands** — Claude Code handles commits and pushes
- **Server configuration** — Vercel handles this
- **Database management** — Supabase handles this
- **Payment integration** — Stripe + Claude Code handles this

**What you DO bring:**
- The architecture (you already built this)
- The design intent (you know what it should feel like)
- The domain expertise (training, SCL, the zip code system)
- Decision-making (when Claude Code needs direction, you decide)

You are the architect. Claude Code is the builder. The tools are the materials.

---

## Troubleshooting

**"claude: command not found"**
→ Restart PowerShell after installation. If still fails, run the installer again.

**"Permission denied" on git push**
→ Run `git config --global credential.helper manager` and try again. GitHub will prompt you to log in.

**"npm: command not found"**
→ Restart PowerShell after installing Node.js.

**Claude Code seems slow or unresponsive**
→ Type `/status` to check your usage. Max plan has limits that refresh.

**"I don't know what to do next"**
→ Tell Claude Code: "Read whiteboard.md and tell me the current state of the project and what I should work on."

---

## Quickstart Checklist (The Shortest Path)

If you want to be up and running as fast as possible:

```
[ ] Install Git for Windows         — git-scm.com/downloads/win
[ ] Install Claude Code             — irm https://claude.ai/install.ps1 | iex
[ ] Login                           — claude login
[ ] Clone repo                      — git clone https://github.com/BigBruddaThunda/ppl-plus-ultra.git
[ ] Enter project                   — cd ppl-plus-ultra
[ ] Launch Claude Code              — claude
[ ] Install Node.js                 — nodejs.org (LTS)
[ ] Create Vercel account           — vercel.com (sign up with GitHub)
[ ] Create Supabase account         — supabase.com
```

Everything else, Claude Code builds for you when you're ready.
