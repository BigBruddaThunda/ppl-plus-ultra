# Scripts Audit Workflow

This folder contains card validation and audit automation for the Codex expansion track.

## One-command full audit

```bash
bash scripts/run-full-audit.sh cards/⛽-strength/🏛-basics
```

The orchestrator runs:
1. `scripts/lint-scl-rules.py`
2. `scripts/validate-deck.sh`
3. `scripts/audit-exercise-coverage.py`
4. `scripts/check-card-schema.py`
5. `scripts/validate-junction-bridges.py`
6. `scripts/index-card-inventory.py`

Artifacts are written to `scripts/.artifacts/`.

## Checklist matrix and coverage map

See `scripts/audit-checklist-matrix.md` for the extracted check matrix from:
- `seeds/codex-audit-agents-friendly-expansion.md`

The matrix maps each proposed check to:
- existing automation,
- partial coverage,
- or a newly defined `scripts/` entry point.

## Newly defined entry points (contract-first)

Implemented baseline:
- `scripts/lint-scl-rules.py`
- `scripts/check-card-schema.py`
- `scripts/validate-junction-bridges.py`
- `scripts/index-card-inventory.py`
- `scripts/run-full-audit.sh`

Contract stubs (CLI locked for future implementation):
- `scripts/check-weight-declarations.py`
- `scripts/check-exercise-family-tree.py`
- `scripts/run-selector-prototype.py`
- `scripts/check-fatigue-model.py`
- `scripts/build-canonicalization-pack.py`
- `scripts/validate-agent-handoffs.py`
- `scripts/run-agent-fixtures.py`
- `scripts/validate-session-templates.py`

Each stub supports `--require-implementation` and exits non-zero when invoked with it.

## Operis pipeline contract validator

Validate all three Operis pipeline artifacts in one pass:

```bash
python3 scripts/validate-operis-contracts.py operis-editions/test-results/2024-07-26/
```

What it enforces:
1. `contract-a-research-brief.md`
   - Every historical event has at least one explicit source URL.
   - Required sky-time fields (`Sunrise`, `Sunset`, `Moonrise`, `Moonset`) exist and include exact times.
2. `contract-b-content-brief.md`
   - Every content lane includes an explicit source URL list with at least one URL.
3. `contract-c-operis-edition.md` frontmatter
   - `sandbox-zips` exists and is structurally valid.
   - `sandbox-total` exists and equals `13`.
   - Legacy key `rooms` is rejected.

Behavior:
- Exits non-zero on the first contract violation.
- Prints a human-readable `ERROR:` line for the failing contract rule.
