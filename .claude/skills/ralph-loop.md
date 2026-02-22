# Ralph Loop Skill

## Trigger

User says "run a Ralph loop", `/ralph`, "Ralph loop on this", or "run Ralph".

## Behavior

1. **Check for required files:**
   - If `scripts/ralph/prd.json` does not exist: tell the user "No prd.json found. Create a PRD first in scripts/ralph/"
   - If `scripts/ralph/RALPH-PROMPT.md` does not exist: tell the user "No RALPH-PROMPT.md found. Create the prompt file first."
   - If either is missing, stop here.

2. **Read `scripts/ralph/prd.json`**

3. **Find the next incomplete story:**
   - Filter to stories where `passes: false`
   - Sort by `priority` ascending
   - Take the first result
   - If none: tell the user "All stories complete. Nothing to Ralph." and stop.

4. **Report the selected story:**
   - Print: "Starting: [Story ID] — [Story Title]"
   - Print: "Priority: [priority] | Stories remaining: [count]"

5. **Read `scripts/ralph/RALPH-PROMPT.md`** for full instructions

6. **Execute that single story** following all RALPH-PROMPT.md instructions:
   - Read required files (zip-web-rules.md, zip-web-signatures.md, zip-web-registry.md)
   - Open the stub pod file for the target deck
   - Populate all 40 pods with N/E/S/W neighbor assignments and coaching rationale
   - Run the validation checklist for every pod before writing
   - Commit the changes
   - Update prd.json: set `passes: true` for the completed story
   - Append session log to progress.txt

7. **Report completion:**
   - Print: "Complete: [Story ID] — [Story Title]"
   - Print remaining story count
   - Print: "Run /ralph again for the next story."

## Important Notes

- Each `/ralph` invocation does **ONE story only**
- The user runs `/ralph` again for the next story
- This provides human checkpoints between deck iterations
- For fully autonomous operation without checkpoints, use `ralph.sh` instead:
  ```
  bash scripts/ralph/ralph.sh
  ```
- The quality bar for all pod work is `zip-web/zip-web-pods/deck-07-pods.md`
- All validation rules are in `zip-web/zip-web-rules.md`
