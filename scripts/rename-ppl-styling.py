#!/usr/bin/env python3
"""
Ppl± Rename Script
Replaces PPL± → Ppl± and standalone PPL → Ppl across all .md files.

Preserves:
  - ppl-plus-ultra in URLs, file paths, repo references
  - PPL/PPL± inside fenced code blocks (``` ... ```)
  - Variable names, CSS selectors, JSON keys containing PPL
  - The GitHub repo name

Usage:
  python scripts/rename-ppl-styling.py          # dry run (default)
  python scripts/rename-ppl-styling.py --apply   # apply changes
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Patterns to skip (file paths, not content)
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv'}


def find_md_files(root):
    """Find all .md files in the repo, skipping irrelevant dirs."""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Remove skip dirs from traversal
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return sorted(md_files)


def process_content(content):
    """Replace PPL± → Ppl± and standalone PPL → Ppl outside code blocks."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    total_replacements = 0

    for line in lines:
        # Track fenced code blocks
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        original = line

        # Replace PPL± → Ppl± (the primary target)
        line = line.replace('PPL±', 'Ppl±')

        # Replace PPL+ → Ppl+ (alternate styling)
        line = line.replace('PPL+', 'Ppl+')

        # Replace standalone PPL → Ppl (but not ppl-plus-ultra, --ppl-, etc.)
        # Match PPL that is:
        #   - at word boundary
        #   - NOT followed by - (which would be ppl-plus-ultra in a URL/path)
        #   - NOT preceded by -- (which would be a CSS var like --ppl-)
        line = re.sub(r'(?<!--)(?<!\w)PPL(?![\w-])', 'Ppl', line)

        if line != original:
            total_replacements += 1

        result.append(line)

    return '\n'.join(result), total_replacements


def main():
    apply_mode = '--apply' in sys.argv
    mode_label = "APPLYING" if apply_mode else "DRY RUN"
    print(f"Ppl± Rename Script — {mode_label}")
    print("=" * 50)

    md_files = find_md_files(REPO_ROOT)
    print(f"Found {len(md_files)} .md files\n")

    files_changed = 0
    total_replacements = 0

    for filepath in md_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except (UnicodeDecodeError, IOError):
            continue

        new_content, replacements = process_content(content)

        if replacements > 0:
            rel_path = os.path.relpath(filepath, REPO_ROOT)
            print(f"  {rel_path}: {replacements} line(s) changed")
            files_changed += 1
            total_replacements += replacements

            if apply_mode:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    print(f"\n{'=' * 50}")
    print(f"Files changed: {files_changed}")
    print(f"Lines with replacements: {total_replacements}")
    if not apply_mode:
        print("\nThis was a dry run. Use --apply to write changes.")


if __name__ == '__main__':
    main()
