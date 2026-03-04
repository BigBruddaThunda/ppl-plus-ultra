# Container Directory

## Dependency Map (excerpt)

- **CX-00A** — bootstrap container baseline.  
  **Depends on:** None.
- **CX-00B** — post-bootstrap stabilization.  
  **Depends on:** CX-00A.
- **CX-01** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-02** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-03** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-04** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-05** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-06** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-07** — Phase 1 container.  
  **Depends on:** CX-00A.
- **CX-08** — Phase 1 container.  
  **Depends on:** CX-00A.

Any container with `Depends on: CX-00A` must not run until CX-00A is merged to main.

## Wave Plan

| Wave | Containers |
|---|---|
| Wave 0 | CX-00A |
| Wave 1 | CX-00B, CX-01, CX-02, CX-03, CX-04, CX-05, CX-06, CX-07, CX-08 |

## Dependency Check

- No wave includes both a container and its prerequisite.
- `CX-00A` is isolated in Wave 0.
- All containers that depend on `CX-00A` are placed in Wave 1.
