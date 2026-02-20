# Skill: Verify or Rebuild HTML Directory Structure

## When to Use
When the html/ directory needs to be checked against the current SCL architecture, or after new SCL categories are added.

## Steps

1. Read the current SCL architecture from `scl-directory.md` to confirm:
   - Number of Orders (currently 7)
   - Number of Axes (currently 6)
   - Number of Types (currently 5)
   - Number of Blocks (currently 22)
   - Number of Operators (currently 12)

2. Verify that all expected files exist:
   - 7 Order CSS files in `html/design-system/orders/`
   - 6 Axis CSS files in `html/design-system/axes/`
   - 5 Type CSS files in `html/design-system/types/`
   - Block and operator CSS files
   - All component templates in `html/components/`
   - 6 floor directories in `html/floors/`
   - Asset directories with `.gitkeep` files

3. Report any missing files or structural issues
4. Create missing files with standard scaffold headers if confirmed

## Do NOT
- Overwrite existing files that have content beyond scaffold headers
- Add functional CSS or HTML (scaffold only)
- Create files for SCL categories that don't exist yet
