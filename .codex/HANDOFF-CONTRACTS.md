# Codex Handoff Contracts

This file defines agent interlocks, read/write boundaries, and handoff payload format.
Use these contracts as a poka-yoke layer for multi-agent runs.

## Agent Boundary Matrix

| Agent | Read Scope | Write Scope | Never Touch |
|---|---|---|---|
| generator | `AGENTS.md`, `whiteboard.md`, `scl-directory.md`, `exercise-library.md`, `deck-identities/`, task target files | Task target file set only (typically `cards/` for generation tasks, or container-specific write list) | Any file outside the active container write scope; SCL rule definitions; unrelated seeds |
| validator | Generated artifacts, constraint references (`scl-directory.md`, `exercise-library.md`, deck identities), lint/schema specs | Reports only (stdout or designated report file in container scope) | Source mutation of generated artifacts |
| explorer | Entire repository read-only for discovery, dependency lookup, and evidence gathering | None | Any file edits |
| reviewer | PR diff, policy docs, constraints, source references needed for compliance checks | Review notes only (PR review summary artifacts if requested) | Direct code/content edits |

## Role Contracts

### 1) Generator Contract
- Resolve the active container and dependency preconditions before emitting changes.
- Keep writes constrained to the container's declared write scope.
- Include a validation checklist response in the handoff packet.

### 2) Validator Contract
- Execute scan cycle checks only; do not repair artifacts.
- Classify findings by severity defined in task instructions.
- Return pass/fail plus precise failing interlock.

### 3) Explorer Contract
- Provide evidence maps: file path, line anchors, and dependency status.
- Never infer completion without source evidence.
- Keep outputs concise and directly consumable by generator/validator.

### 4) Reviewer Contract
- Review against hard constraints first, then format/quality constraints.
- Flag only requested severity classes.
- Return merge readiness with blocking and non-blocking findings separated.

## Clean Handoff Packet Format

Use this structure for every agent-to-agent transfer:

```markdown
### Handoff Packet
- Container: CX-XX
- Dependency Check: PASS|FAIL (list)
- Scope Read: [paths]
- Scope Write: [paths]
- Artifacts Produced: [files]
- Validation Run: [commands + status]
- Open Interlocks: [none or list]
- Next Agent: generator|validator|explorer|reviewer
```

## Prohibited Actions (All Agents)

- Do not mutate files outside active write scope.
- Do not create new SCL rules or emoji systems.
- Do not bypass dependency order defined in `.codex/TASK-ARCHITECTURE.md`.
- Do not mark work complete without validation evidence.

## Routing Rules

- **explorer → generator** for dependency and evidence priming.
- **generator → validator** after emit.
- **validator → reviewer** when changes are ready for PR review.
- **reviewer → generator** only when blocking issues require rework.
