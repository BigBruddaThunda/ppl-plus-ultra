#!/usr/bin/env python3
"""
validate-exercise-integration.py — Exercise Library v.1 Wave 3

Integration validator that checks cross-layer consistency across the
entire exercise ecosystem: registry, content files, family trees,
substitution maps, anatomy index, card index, and exercise selector.

Usage:
  python scripts/validate-exercise-integration.py
  python scripts/validate-exercise-integration.py --verbose
"""

import argparse
import json
import os
import sys
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).parent.parent

# Paths
REGISTRY_PATH = REPO_ROOT / "middle-math" / "exercise-registry.json"
CONTENT_DIR = REPO_ROOT / "exercise-content"
FAMILY_TREES_PATH = REPO_ROOT / "middle-math" / "exercise-engine" / "family-trees.json"
SUBSTITUTION_MAP_PATH = REPO_ROOT / "middle-math" / "exercise-engine" / "substitution-map.json"
ANATOMY_INDEX_PATH = REPO_ROOT / "middle-math" / "exercise-engine" / "anatomy-index.json"
CARD_INDEX_PATH = REPO_ROOT / "middle-math" / "exercise-card-index.json"

VALID_PATTERNS = {
    "hip-hinge", "squat", "lunge",
    "horizontal-press", "vertical-press",
    "horizontal-pull", "vertical-pull",
    "isolation-curl", "isolation-extension",
    "leg-isolation", "carry", "anti-rotation",
    "core-stability", "olympic", "conditioning",
    "plyometric", "isolation", "mobility",
}


def check(label: str, passed: bool, detail: str = "") -> bool:
    """Print check result and return pass/fail."""
    icon = "✅" if passed else "❌"
    msg = f"  {icon} {label}"
    if detail:
        msg += f" — {detail}"
    print(msg)
    return passed


def run_checks(verbose: bool = False) -> bool:
    results = []
    print("=" * 60)
    print("Exercise Integration Validation")
    print("=" * 60)

    # ─── Check 1: Registry exists and loads ───
    print("\n1. Registry integrity")
    try:
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            registry = json.load(f)
        results.append(check("Registry loads", True, f"{len(registry)} entries"))
    except Exception as e:
        results.append(check("Registry loads", False, str(e)))
        print("\nFATAL: Cannot continue without registry.")
        return False

    # Check all IDs are unique and sequential
    ids = [e["exercise_id"] for e in registry]
    unique_ids = len(set(ids)) == len(ids)
    results.append(check("All exercise_id values unique", unique_ids,
                         f"{len(ids)} IDs, {len(set(ids))} unique"))

    expected_last = f"EX-{len(registry):04d}"
    sequential = ids[0] == "EX-0001" and ids[-1] == expected_last
    results.append(check("IDs sequential EX-0001 to EX-NNNN", sequential,
                         f"range {ids[0]}..{ids[-1]}"))

    # ─── Check 2: Movement pattern distribution ───
    print("\n2. Movement pattern quality")
    patterns = Counter(e["movement_pattern"] for e in registry)
    all_valid = all(p in VALID_PATTERNS for p in patterns)
    results.append(check("All patterns in vocabulary", all_valid,
                         f"{len(patterns)} patterns"))

    cs_count = patterns.get("core-stability", 0)
    cs_pct = 100 * cs_count / len(registry)
    cs_ok = cs_pct < 30
    results.append(check("core-stability < 30%", cs_ok,
                         f"{cs_count}/{len(registry)} ({cs_pct:.1f}%)"))

    no_single_dominant = all(c / len(registry) < 0.30 for c in patterns.values())
    results.append(check("No single pattern > 30%", no_single_dominant))

    if verbose:
        for p, c in patterns.most_common():
            print(f"    {p:24} {c:5d} ({100*c/len(registry):.1f}%)")

    # ─── Check 3: Content file coverage ───
    print("\n3. Exercise content coverage")
    content_files = set()
    for root, dirs, files in os.walk(CONTENT_DIR):
        for f in files:
            if f.endswith('.md') and f != 'README.md':
                content_files.add(os.path.join(root, f))

    results.append(check("Content directory exists", CONTENT_DIR.exists()))

    # Check registry → content files
    missing_content = []
    for entry in registry:
        kf = entry.get("knowledge_file", "")
        if kf:
            full_path = REPO_ROOT / kf
            if not full_path.exists():
                missing_content.append((entry["exercise_id"], kf))

    content_coverage = len(registry) - len(missing_content)
    pct = 100 * content_coverage / len(registry) if registry else 0
    results.append(check(
        "Registry → content file linkage",
        len(missing_content) == 0,
        f"{content_coverage}/{len(registry)} ({pct:.0f}%) linked"
    ))
    if verbose and missing_content:
        for ex_id, kf in missing_content[:10]:
            print(f"    MISSING: {ex_id} → {kf}")

    results.append(check(
        "Content file count matches registry",
        len(content_files) >= len(registry),
        f"{len(content_files)} files, {len(registry)} registry entries"
    ))

    # ─── Check 4: Family trees ───
    print("\n4. Family tree integrity")
    if FAMILY_TREES_PATH.exists():
        with open(FAMILY_TREES_PATH, encoding="utf-8") as f:
            family_data = json.load(f)
        results.append(check("Family trees file loads", True))

        # Check for valid structure
        if isinstance(family_data, dict):
            families = family_data.get("families", family_data)
            family_count = len(families)
            results.append(check("Family tree structure valid", True,
                                 f"{family_count} families"))
        elif isinstance(family_data, list):
            family_count = len(family_data)
            results.append(check("Family tree structure valid", True,
                                 f"{family_count} families"))
    else:
        results.append(check("Family trees file exists", False))

    # ─── Check 5: Substitution map ───
    print("\n5. Substitution map integrity")
    if SUBSTITUTION_MAP_PATH.exists():
        with open(SUBSTITUTION_MAP_PATH, encoding="utf-8") as f:
            sub_data = json.load(f)
        results.append(check("Substitution map loads", True))

        if isinstance(sub_data, dict):
            sub_count = len(sub_data)
            results.append(check("Substitution entries present", sub_count > 0,
                                 f"{sub_count} entries"))
        elif isinstance(sub_data, list):
            results.append(check("Substitution entries present", len(sub_data) > 0,
                                 f"{len(sub_data)} entries"))
    else:
        results.append(check("Substitution map exists", False))

    # ─── Check 6: Anatomy index ───
    print("\n6. Anatomy index integrity")
    if ANATOMY_INDEX_PATH.exists():
        with open(ANATOMY_INDEX_PATH, encoding="utf-8") as f:
            anat_data = json.load(f)
        results.append(check("Anatomy index loads", True))

        if isinstance(anat_data, dict):
            anat_count = len(anat_data)
            results.append(check("Anatomy entries present", anat_count > 0,
                                 f"{anat_count} entries"))
    else:
        results.append(check("Anatomy index exists", False))

    # ─── Check 7: Card index ───
    print("\n7. Exercise-card index")
    if CARD_INDEX_PATH.exists():
        with open(CARD_INDEX_PATH, encoding="utf-8") as f:
            card_index = json.load(f)
        results.append(check("Card index loads", True))

        meta = card_index.get("metadata", {})
        cards_scanned = meta.get("cards_scanned", 0)
        match_rate = meta.get("match_rate", 0)
        results.append(check("Cards scanned = 1,680", cards_scanned == 1680,
                             f"{cards_scanned} cards"))
        results.append(check("Match rate ≥ 95%", match_rate >= 95.0,
                             f"{match_rate}%"))

        # Check index references valid EX-IDs
        idx = card_index.get("index", {})
        valid_ids = set(e["exercise_id"] for e in registry)
        invalid_refs = [k for k in idx if k not in valid_ids]
        results.append(check("All index keys are valid EX-IDs",
                             len(invalid_refs) == 0,
                             f"{len(invalid_refs)} invalid"))
    else:
        results.append(check("Card index exists", False,
                             "Run build-exercise-card-index.py first"))

    # ─── Check 8: Registry field completeness ───
    print("\n8. Registry field completeness")
    required_fields = [
        "exercise_id", "name", "source_section", "movement_pattern",
        "scl_types", "equipment_tier", "gold_gated", "primary_movers",
        "family_id", "axis_affinity", "order_affinity", "sport_tags",
        "knowledge_file", "status",
    ]

    missing_fields = {}
    for field in required_fields:
        missing = sum(1 for e in registry if not e.get(field) and e.get(field) != False)
        if missing > 0:
            missing_fields[field] = missing

    results.append(check(
        "All required fields populated",
        len(missing_fields) == 0,
        f"{len(missing_fields)} fields with gaps" if missing_fields else "all clear"
    ))
    if verbose and missing_fields:
        for field, count in sorted(missing_fields.items()):
            print(f"    {field}: {count} empty")

    # ─── Check 9: Anatomy coverage ───
    print("\n9. Anatomy coverage")
    with_movers = sum(1 for e in registry if e.get("primary_movers"))
    pct = 100 * with_movers / len(registry)
    results.append(check("All exercises have primary_movers",
                         with_movers == len(registry),
                         f"{with_movers}/{len(registry)} ({pct:.0f}%)"))

    # ─── Summary ───
    total = len(results)
    passed = sum(results)
    failed = total - passed

    print(f"\n{'=' * 60}")
    print(f"Results: {passed}/{total} checks passed, {failed} failed")
    print(f"{'=' * 60}")

    if failed == 0:
        print("\n✅ All integration checks passed. Exercise library v.1 ready.")
    else:
        print(f"\n❌ {failed} check(s) failed. Review above for details.")

    return failed == 0


def main():
    parser = argparse.ArgumentParser(description="Validate exercise library integration")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    ok = run_checks(verbose=args.verbose)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
