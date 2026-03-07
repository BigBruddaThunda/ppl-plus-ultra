# Coding Conventions

**Analysis Date:** 2026-03-07

---

## Card File Naming

**Stub (awaiting generation):**
```
[zip]±.md
```
Example: `⛽🏛🪡🔵±.md`

Rule: Filename ends exactly at `±`. No space, no operator, no title after the `±`.

**Complete (workout generated):**
```
[zip]±[operator emoji] [Title].md
```
Example: `⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`

Rule: After `±` comes exactly one operator emoji, one space, then the human-readable title.

**Lint guard** (`scripts/lint-scl-rules.py`): Filename violation detected by regex `±\S+\s+.+` — operator and title segment must be present in generated files.

**Title conventions (from `deck-identities/naming-convention.md`):**
- Never start with "The"
- Never use: Protocol, Prescription, Playground, Full Send, or vibe-speak
- Format: `[Movement/Equipment] — [Muscle/Focus, Context]`
- Two parts separated by em dash (—), not hyphen

---

## Directory Structure for Cards

```
cards/
└── [order-folder]/      # e.g., ⛽-strength/
    └── [axis-folder]/   # e.g., 🏛-basics/
        └── [type-folder]/  # e.g., 🪡-pull/
            └── [zip]±.md or [zip]±[op] [Title].md
```

Folder names: `[emoji]-[lowercase-name]` pattern. Example: `⛽-strength`, `🏛-basics`, `🪡-pull`.

---

## Frontmatter Schema

Every card file opens with YAML frontmatter between `---` markers. Required fields and their formats:

```yaml
---
zip: ⛽🏛🪡🔵
operator: 🤌 facio | execute/perform
status: GENERATED-V2
deck: 07
order: ⛽ Strength | 75–85% | 4–6 reps | 3–4 min rest | CNS: High
axis: 🏛 Basics | Bilateral, barbell-first, proven classics
type: 🪡 Pull | Lats, rear delts, biceps, traps, erectors
color: 🔵 Structured | Tier 2–3 | GOLD: No | Prescribed sets/reps/rest
blocks: ♨️ → ▶️ → 🧈 → 🧩 → 🪫 → 🚂
---
```

**Field rules:**
- `zip`: 4 emojis, ORDER AXIS TYPE COLOR order, no spaces
- `operator`: emoji + latin name + `|` + meaning phrase
- `status`: One of `EMPTY`, `GENERATED`, `GENERATED-V2`, `CANONICAL`, `REGEN-NEEDED`, `GENERATED-V2-REGEN-NEEDED`
- `deck`: Two-digit number string (e.g., `07`)
- `order`, `axis`, `type`, `color`: emoji + Name + `|` + detail string
- `blocks`: emoji sequence joined with ` → ` arrows

**Frontmatter parsing** (used in all scripts): Manual `key: value` split using Python's `line.partition(':')`. No YAML library dependency.

---

## Card Body Format — 15 Required Elements

All 15 must be present in every generated card:

1. **Title** with flanking Type emojis: `# 🪡 Title Here 🪡`
2. **Subtitle**: training modality, targets, honest time estimate (e.g., `Structured intervals | Cardiovascular system | 50–60 min`)
3. **CODE line**: `CODE: ⛽🔨➖🔵`
4. **🎯 INTENTION**: blockquote, one sentence, active voice: `> "Frame the work here."`
5. **Numbered BLOCKS** with emoji names and heavy border separators: `## 1. ♨️ WARM-UP`
6. **Heavy border separator** between blocks: `═══════════════════════════════════════`
7. **Operator call** inline after block header: `🥨 tendo — extend readiness to full operational range`
8. **Sub-block zip codes**: BLOCK+TYPE+AXIS+COLOR format with parenthetical expansion:
   `🔵🔨➖🔵 (Warm-Up | Cardiovascular | Functional | Structured)`
9. **Tree notation**: `├─` for items, `│` for continuation, `└─` for last item
10. **Reps before exercise name**: `10 🍗 Squat` not `🍗 Squat × 10`
11. **Type emoji before exercise name**: `5 🪡 Barbell Row`
12. **Cues in parentheses**, 3–6 words, conversational: `(brace, pull to lower ribs)`
13. **Sets on individual lines** with Order emoji: `Set 1: ⛽ 80% × 5 (controlled concentric)`
14. **Rest specified** for every block
15. **🚂 JUNCTION** with logging space and next-session bridge:
    ```
    Next → [zip] — [one-line reason]
    ```
    Logging space uses fenced code block with fill-in-the-blank fields.

Plus final `## 🧮 SAVE` closing block with 1–2 sentence principle (not praise).

---

## Tonal Rules

These are content constraints, not style suggestions:

**Do:**
- Direct, technical, conversational
- Cues: `"Hips back, not down."` / `"Hold the weight in the bottom."`
- 🎯 Intention: frames the work, does not hype it
- 🧮 SAVE: transfers the lesson, does not praise the user

**Do not:**
- Motivational filler: no "You got this!", no "Crush it today!"
- Clinical language: no "optimize neuromuscular recruitment"
- Vibe-speak in titles: no Protocol, Prescription, Playground, Full Send

---

## Block Formatting Patterns

**Block header format:**
```markdown
## [N]. [emoji] [BLOCK NAME]
[operator emoji] [operator name] — [session-specific action phrase]

[sub-block zip] ([Block | Muscle | Bias | Equipment])

├─ [exercise line]
│  [continuation line]
└─ [last item line]

Rest: [period]
```

**Circuit (🎱 ARAM) format uses box notation:**
```markdown
```
┌────────────────────────────────────────┐
│  STATION A  →  STATION B  →  STATION C  │
│  [tissue]      [tissue]      [tissue]   │
└────────────────────────────────────────┘
```
```

**Set line format:**
```
Set 1: ⛽ 80% × 5 (context cue)
```

**Junction format:**
```
Next →
- [zip] — [one-line reason]
- [zip] — [one-line reason]
```

Or inline: `Next → [zip] — [reason]`

---

## Python Script Conventions

All scripts in `scripts/` follow these patterns:

**Shebang and docstring:**
```python
#!/usr/bin/env python3
"""
script-name.py — PPL± Short Description
Usage: python scripts/script-name.py <args>

Input contract: [what it takes]
Output contract: [what it emits, exit codes]
"""
```

**Exit codes:** `sys.exit(0)` for pass, `sys.exit(1)` for hard failure. Contract-stub scripts exit `2` with `--require-implementation`.

**Emoji sets defined as module-level constants:**
```python
ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES   = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES  = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']
```

**Frontmatter parser pattern** (duplicated across scripts, no shared import):
```python
def parse_frontmatter(content):
    lines = content.split('\n')
    if not lines[0].strip() == '---':
        return None, content
    # find closing ---, extract key: value pairs
    fm = {}
    for line in fm_lines:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    return fm, body
```

**Zip parser pattern** (greedy prefix matching, used across scripts):
```python
def parse_zip(zip_str):
    s = zip_str.strip()
    for emoji_set in [ORDERS, AXES, TYPES, COLORS]:
        for emoji in emoji_set:
            if s.startswith(emoji):
                s = s[len(emoji):]
                break
    # s should be empty on success
```

**Output format:** Human-readable stdout with `✅` for pass, `❌` for failure, `⚠️` for warnings. Scripts support `--format json` where machine-readable output is needed (`lint-scl-rules.py`, `check-card-schema.py`).

**Markdown table output** (used by reporting scripts):
```python
def markdown_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(row) + " |")
    return "\n".join(out)
```

**Import style:** stdlib only. No external dependencies. Common imports: `sys`, `os`, `re`, `json`, `argparse`, `pathlib.Path`, `collections.defaultdict/Counter`.

**Path resolution** (scripts find repo root relative to themselves):
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
```

Or using `pathlib`: `Path(__file__).resolve().parents[1]`

**AGENTS.md skip pattern** (consistent across all scripts scanning `cards/`):
```python
if fname == 'AGENTS.md':
    continue
```

---

## Bash Script Conventions

**Header pattern:**
```bash
#!/usr/bin/env bash
# script-name.sh — Short Description
# Usage: bash scripts/script-name.sh <args>
```

**Error handling:** `set -uo pipefail` (not `set -e` — allows capturing exit codes from subprocesses). `run-full-audit.sh` uses `set -euo pipefail`.

**Delegate to Python:** Bash wrappers loop over files and call `python scripts/validate-card.py` per file. They collect pass/fail counts and summarize.

**Separator line style:**
```bash
echo "════════════════════════════════════════"
```

---

## Status Lifecycle

```
EMPTY → GENERATED → GENERATED-V2 → CANONICAL
                 ↓
          REGEN-NEEDED / GENERATED-V2-REGEN-NEEDED
```

- `EMPTY`: Stub, no workout content
- `GENERATED`: First-pass generation complete
- `GENERATED-V2`: Regenerated to current standard (V2)
- `CANONICAL`: Reviewed and approved, master version
- `REGEN-NEEDED`: Content exists but pre-dates current identity/standard

---

## Authoritative Sources

- SCL rules: `scl-directory.md` (root)
- Exercise catalog: `exercise-library.md` (root)
- Deck identity: `deck-identities/deck-[NN]-identity.md`
- Cosmogram: `deck-cosmograms/deck-[NN]-cosmogram.md`
- Naming convention: `deck-identities/naming-convention.md`

---

*Convention analysis: 2026-03-07*
