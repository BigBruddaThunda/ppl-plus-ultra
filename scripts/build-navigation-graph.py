#!/usr/bin/env python3
"""
CX-23 — Navigation Graph Builder
Computes the 4-directional navigation graph for all 1,680 PPL± zip codes.

Each zip code (O, A, T, C) has exactly 4 directional neighbors:
  N — Progression: builds on hub's state, forward momentum
  E — Balance: fills what the hub neglected (complementary Type)
  S — Recovery-aware: lower CNS demand, different tissue
  W — Exploration: different Axis, novel stimulus

TYPE EXCLUSION RULE (hard constraint from zip-web-rules.md):
  All 4 neighbors must have a different Type from the hub.
  All 4 neighbors must have different Types from each other.

Directional logic:
  N: Type changes to progression companion | Order shifts up by 1 (max 7)
  E: Type changes to balance companion     | Order stays same, Axis stays same
  S: Type changes to recovery companion    | Order shifts down by 1 (min 1)
  W: Type changes to exploration companion | Axis shifts by +1 (wraps 6->1)

Type assignment per hub Type (enforces Type Exclusion Rule):
  Hub=Push(1):  N=Plus(4), E=Pull(2), S=Ultra(5), W=Legs(3)
  Hub=Pull(2):  N=Plus(4), E=Push(1), S=Ultra(5), W=Legs(3)
  Hub=Legs(3):  N=Plus(4), E=Push(1), S=Ultra(5), W=Pull(2)
  Hub=Plus(4):  N=Legs(3), E=Push(1), S=Ultra(5), W=Pull(2)
  Hub=Ultra(5): N=Plus(4), E=Push(1), S=Legs(3),  W=Pull(2)

Rationale:
  Ultra(5) is the recovery-aware type — always in the S slot unless hub IS Ultra.
  Plus(4) is the progression companion (power/full-body) — always in N unless hub IS Plus.
  The antagonist pairing (Push<->Pull) goes in E (balance/complement).
  W gets the remaining Type as the exploration option.

Usage:
  python scripts/build-navigation-graph.py
  python scripts/build-navigation-graph.py --stats
  python scripts/build-navigation-graph.py --output path/to/output.json
"""

import json
import argparse
import sys
from pathlib import Path

# === Constants ===

REPO_ROOT = Path(__file__).parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
OUTPUT_PATH = REPO_ROOT / "middle-math" / "navigation-graph.json"

ORDER_MIN = 1
ORDER_MAX = 7
AXIS_MIN  = 1
AXIS_MAX  = 6

# Fixed Type assignment per hub Type position.
# Keys are hub Type positions (1-5). Values are {direction: neighbor_type_pos}.
# All 4 values in each row are distinct and none equals the key.
TYPE_DIRECTION_MAP = {
    1: {"N": 4, "E": 2, "S": 5, "W": 3},  # Push:  N=Plus, E=Pull, S=Ultra, W=Legs
    2: {"N": 4, "E": 1, "S": 5, "W": 3},  # Pull:  N=Plus, E=Push, S=Ultra, W=Legs
    3: {"N": 4, "E": 1, "S": 5, "W": 2},  # Legs:  N=Plus, E=Push, S=Ultra, W=Pull
    4: {"N": 3, "E": 1, "S": 5, "W": 2},  # Plus:  N=Legs, E=Push, S=Ultra, W=Pull
    5: {"N": 4, "E": 1, "S": 3, "W": 2},  # Ultra: N=Plus, E=Push, S=Legs,  W=Pull
}

TYPE_NAMES = {1: "Push", 2: "Pull", 3: "Legs", 4: "Plus", 5: "Ultra"}
ORDER_NAMES = {1: "Foundation", 2: "Strength", 3: "Hypertrophy", 4: "Performance",
               5: "Full Body", 6: "Balance", 7: "Restoration"}


def parse_zip(zip_code: str) -> tuple[int, int, int, int]:
    """Parse a 4-char numeric zip code into (order, axis, type, color)."""
    return int(zip_code[0]), int(zip_code[1]), int(zip_code[2]), int(zip_code[3])


def build_zip(order: int, axis: int, type_: int, color: int) -> str:
    """Construct a 4-char numeric zip code from dial positions."""
    return f"{order}{axis}{type_}{color}"


def compute_neighbors(zip_code: str) -> dict[str, str]:
    """
    Compute the 4 directional neighbors for a given zip code.

    Returns a dict with keys 'N', 'E', 'S', 'W' mapping to neighbor zip codes.
    """
    O, A, T, C = parse_zip(zip_code)

    type_map = TYPE_DIRECTION_MAP[T]

    # Order shifts: N goes up (progression), S goes down (recovery).
    # Clamped to valid range [1, 7] rather than wrapping, so boundaries stay usable.
    n_order = min(O + 1, ORDER_MAX)
    s_order = max(O - 1, ORDER_MIN)

    # Axis shift for W (exploration — different character, same zip address otherwise).
    # Wraps: 6 -> 1.
    w_axis = (A % AXIS_MAX) + 1

    neighbors = {
        "N": build_zip(n_order, A,      type_map["N"], C),
        "E": build_zip(O,       A,      type_map["E"], C),
        "S": build_zip(s_order, A,      type_map["S"], C),
        "W": build_zip(O,       w_axis, type_map["W"], C),
    }

    return neighbors


def validate_type_exclusion(zip_code: str, neighbors: dict[str, str]) -> list[str]:
    """
    Verify the Type Exclusion Rule: hub Type must not appear in any neighbor,
    and no two neighbors may share the same Type.
    Returns a list of violation messages (empty if valid).
    """
    O, A, T, C = parse_zip(zip_code)
    violations = []

    neighbor_types = {}
    for direction, nzip in neighbors.items():
        nO, nA, nT, nC = parse_zip(nzip)
        neighbor_types[direction] = nT
        if nT == T:
            violations.append(
                f"  Hub {zip_code} (Type={TYPE_NAMES[T]}) → {direction}={nzip} shares hub Type!"
            )

    type_counts = {}
    for direction, nT in neighbor_types.items():
        if nT in type_counts:
            violations.append(
                f"  Hub {zip_code}: directions {type_counts[nT]} and {direction} both have Type={TYPE_NAMES[nT]}!"
            )
        else:
            type_counts[nT] = direction

    return violations


def load_registry(path: Path) -> list[dict]:
    """Load the 1,680-entry zip registry JSON."""
    if not path.exists():
        print(f"ERROR: Registry not found at {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_graph(registry: list[dict]) -> dict[str, dict[str, str]]:
    """Build the complete navigation graph from the registry."""
    graph = {}
    for entry in registry:
        zip_code = entry["numeric_zip"]
        graph[zip_code] = compute_neighbors(zip_code)
    return graph


def validate_graph(graph: dict[str, dict[str, str]]) -> dict:
    """
    Run validation checks on the graph and return a stats dict.
    Checks:
      - All 1,680 nodes present
      - Each node has exactly 4 edges (N/E/S/W)
      - All neighbor zip codes are valid (exist in graph)
      - Type Exclusion Rule holds for every node
    """
    violations = []
    orphan_count = 0
    total_nodes = len(graph)
    all_zips = set(graph.keys())

    for zip_code, neighbors in graph.items():
        # Check edge count
        if len(neighbors) != 4:
            violations.append(f"  {zip_code}: expected 4 edges, got {len(neighbors)}")

        # Check all directions present
        for direction in ("N", "E", "S", "W"):
            if direction not in neighbors:
                violations.append(f"  {zip_code}: missing direction {direction}")

        # Check neighbor zip validity
        for direction, nzip in neighbors.items():
            if nzip not in all_zips:
                violations.append(f"  {zip_code} → {direction}={nzip}: neighbor not in graph!")
                orphan_count += 1

        # Check Type Exclusion Rule
        type_violations = validate_type_exclusion(zip_code, neighbors)
        violations.extend(type_violations)

    return {
        "total_nodes": total_nodes,
        "total_edges": total_nodes * 4,
        "violations": violations,
        "valid": len(violations) == 0,
    }


def print_stats(stats: dict, graph: dict) -> None:
    """Print graph statistics to stdout."""
    print(f"\nNavigation Graph Statistics")
    print(f"===========================")
    print(f"Total nodes:  {stats['total_nodes']}")
    print(f"Total edges:  {stats['total_edges']}")
    print(f"Valid:        {stats['valid']}")

    if stats["violations"]:
        print(f"\nViolations ({len(stats['violations'])}):")
        for v in stats["violations"][:20]:  # cap output
            print(v)
        if len(stats["violations"]) > 20:
            print(f"  ... and {len(stats['violations']) - 20} more")
    else:
        print(f"\nAll {stats['total_nodes']} nodes pass Type Exclusion Rule check.")

    # Sample output
    print(f"\nSample (first 5 nodes):")
    for zip_code in list(graph.keys())[:5]:
        O, A, T, C = parse_zip(zip_code)
        n = graph[zip_code]
        print(f"  {zip_code} ({ORDER_NAMES[O][:5]} {TYPE_NAMES[T][:5]}) → "
              f"N={n['N']} E={n['E']} S={n['S']} W={n['W']}")


def main():
    parser = argparse.ArgumentParser(
        description="Build the 1,680-node navigation graph for PPL± zip codes."
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Print validation statistics after building."
    )
    parser.add_argument(
        "--output", type=str, default=str(OUTPUT_PATH),
        help=f"Output path for navigation-graph.json (default: {OUTPUT_PATH})"
    )
    args = parser.parse_args()

    output_path = Path(args.output)

    print(f"Loading zip registry from {REGISTRY_PATH}...")
    registry = load_registry(REGISTRY_PATH)
    print(f"  Loaded {len(registry)} entries.")

    print(f"Building navigation graph...")
    graph = build_graph(registry)
    print(f"  Computed {len(graph)} nodes × 4 directions = {len(graph) * 4} edges.")

    if args.stats:
        stats = validate_graph(graph)
        print_stats(stats, graph)
        if not stats["valid"]:
            print("\nERROR: Graph has violations. Fix before committing.", file=sys.stderr)
            sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, separators=(",", ":"))
    print(f"\nOutput written to {output_path}")
    print(f"File size: {output_path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
