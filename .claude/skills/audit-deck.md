# Skill: Audit a Deck for Completeness

## When to Use
To check how many cards in a deck have been generated and identify any issues.

## Arguments
- Deck number (01-42) or deck identifier (e.g., "⛽🏛" or "Deck 07")

## Steps

1. Identify the Order × Axis combination for this deck number (reference CLAUDE.md deck table)
2. Determine the correct directory path: `cards/[order-folder]/[axis-folder]/`
3. Find all card files across the 5 Type subdirectories (5 Types × 8 Colors = 40 cards expected)
4. For each card file found, check:
   - Frontmatter `status` field (EMPTY, GENERATED, or CANONICAL)
   - Filename format compliance (stub format or complete format)
   - Correct deck number in frontmatter
5. Report:
   - Total files found (expected: 40)
   - Files with `status: EMPTY`
   - Files with `status: GENERATED`
   - Files with `status: CANONICAL`
   - Any missing files
   - Any naming convention violations
   - Any files with incorrect deck assignment in frontmatter

## Output Format
```
DECK AUDIT: Deck [XX] — [Order][Axis] [Order Name] [Axis Name]

Total files: XX/40
EMPTY:     XX
GENERATED: XX
CANONICAL: XX
MISSING:   XX

Issues: [list any problems found]
```
