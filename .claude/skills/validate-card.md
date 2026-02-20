# Skill: Validate a Generated Workout Card

## When to Use
After generating a workout card, or when reviewing an existing GENERATED card for promotion to CANONICAL.

## Arguments
- Path to card file (e.g., `cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Heavy Classic Pulls.md`)

## Steps

1. Read the card file at the specified path
2. Parse the zip code from frontmatter
3. Load all constraints from `scl-directory.md` and `CLAUDE.md`
4. Run the full validation checklist from CLAUDE.md:

   **Order compliance:**
   - Load stays at or below Order ceiling
   - Rep ranges match Order parameters
   - Rest periods match Order parameters
   - Difficulty stays at or below Order maximum
   - Block count matches Order guidelines

   **Type accuracy:**
   - Exercises train the correct muscle groups
   - Movement patterns match the Type

   **Axis character:**
   - Exercise selection reflects the Axis bias
   - Would someone feel the Axis without being told?

   **Color constraints:**
   - All equipment within Color's tier range
   - No barbells in 🟢 or 🟠
   - GOLD exercises only in 🔴 or 🟣
   - Loop logic applied in 🟠 Circuit

   **Block structure:**
   - 🧈 present and carries most volume
   - Session flows Orient → Access → Transform → Retain
   - Ends with 🚂 Junction and 🧮 SAVE

   **Format:**
   - All 15 required elements present
   - Sub-block zip codes formatted correctly
   - Tree notation used
   - Tonal rules followed throughout

5. If `scl-deep/order-parameters.md` exists and is not a stub, also check:
   - Exercise attribute filters for the card's Order
   - Conflict detection rules (axial load, grip, CNS, shoulder, pattern, recovery, joint)
   - Volume position targets
   - Pairing permission matrix

6. Report all violations, warnings, and suggestions
7. **Do not modify the card — report only**

## Output Format
```
VALIDATION REPORT: [zip code]

✅ PASS: [check name]
⚠️ WARN: [check name] — [detail]
❌ FAIL: [check name] — [detail]

Summary: X pass, Y warnings, Z failures
```
