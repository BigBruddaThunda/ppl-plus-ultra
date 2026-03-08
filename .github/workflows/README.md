# Ppl± GitHub Actions

GitHub Actions workflows for repository-level validation and CI checks.

---

## Active Workflows

### `lint.yml`

Primary lint/audit workflow for card validation using the existing scripts in `scripts/`.

#### Triggers

- Push to `main`
- Pull requests targeting `main`

#### Jobs

1. **`baseline-audit`**
   - Detects deck folders under `cards/` that contain generated cards (`status: GENERATED`, `GENERATED-V2`, or `CANONICAL`)
   - Runs baseline audit orchestration per generated deck via:
     - `bash scripts/run-full-audit.sh <deck-path>`
   - Rebuilds inventory artifacts via:
     - `python scripts/index-card-inventory.py --cards-root cards --strict-status ...`
   - Uploads `scripts/.artifacts/` as workflow artifact `audit-artifacts` (30-day retention)

   **Intent:** informational full-deck context. This job can surface pre-existing deck issues while still preserving PR-specific hard gating in the second job.

2. **`pr-changed-cards`** (PR events only)
   - Identifies changed card files with:
     - `git diff --name-only origin/main...HEAD -- 'cards/'`
   - For each changed card, runs:
     - `python scripts/check-card-schema.py --card <file>`
     - `python scripts/lint-scl-rules.py --card <file>`

   **Intent:** hard gate for changed cards. Failures here should block merge.

---

## How to Read Results

- Use **`pr-changed-cards`** to determine whether changed card files are merge-safe.
- Use **`baseline-audit`** to inspect overall deck health and artifact outputs.
- Download `audit-artifacts` from the workflow run to inspect generated inventory files.

---

## Run Locally

Run baseline audit for a specific deck folder:

```bash
bash scripts/run-full-audit.sh <deck-path>
```

Example:

```bash
bash scripts/run-full-audit.sh cards/⛽-strength/🏛-basics
```

---

## Notes

- `lint.yml` wires existing validation scripts only; it does not add new lint logic.
- The workflow is read-only with respect to source content and is intended for validation + audit artifact generation.

🧮
