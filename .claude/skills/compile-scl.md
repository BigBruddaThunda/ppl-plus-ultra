# Skill: Compile SCL Directory from Deep Specs

## When to Use
When deep specification documents in `scl-deep/` have been updated and the operational `scl-directory.md` needs to reflect those changes.

## Steps

1. Read all documents in `scl-deep/` that have status other than STUB
2. Compare their content against the current `scl-directory.md`
3. Identify any layers, rules, or specifications in `scl-deep/` that are not yet reflected in the operational `scl-directory.md`
4. Output a diff summary of what needs to be added or updated
5. **Do NOT automatically rewrite scl-directory.md** — present the changes for review first
6. Only apply changes after Jake confirms

## Priority Order
1. Color tonal register layer (from color-context-vernacular.md)
2. Order periodization details (from order-parameters.md)
3. Axis deep specs (from axis-specifications.md)
4. Block behavioral specs (when written)
5. Operator semantic specs (when written)
6. Type routing specs (when written)

## Do NOT
- Rewrite scl-directory.md without presenting changes first
- Remove existing content from scl-directory.md (add to, don't replace)
- Modify scl-deep/ source files during compilation
