"""Load raw json files and print a graph summary."""

import argparse
import json
import sys
from pathlib import Path

from f1graph.graph.builder import constructor_nodes, driver_nodes, drove_for_edges

RAW_DIR = Path("data/raw")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("season", help="season year, e.g. 2026")
    args = parser.parse_args()

    driver_path = RAW_DIR / f"drivers_{args.season}.json"
    if not driver_path.exists():
        print(f"missing {driver_path}, run ingest first", file=sys.stderr)
        return 1

    drivers = json.loads(driver_path.read_text())
    nodes = driver_nodes(drivers)
    print(f"{len(nodes)} driver nodes")
    for node_id, attrs in list(nodes.items())[:3]:
        code = attrs["code"] or "—"
        print(f"  {node_id}: {attrs['label']} ({code})")

    constructor_path = RAW_DIR / f"constructors_{args.season}.json"
    if constructor_path.exists():
        constructors = json.loads(constructor_path.read_text())
        c_nodes = constructor_nodes(constructors)
        print(f"\n{len(c_nodes)} constructor nodes")
        for node_id, attrs in list(c_nodes.items())[:3]:
            print(f"  {node_id}: {attrs['label']}")

    standings_path = RAW_DIR / f"standings_{args.season}.json"
    if standings_path.exists():
        standings = json.loads(standings_path.read_text())
        edges = drove_for_edges(standings)
        print(f"\n{len(edges)} DROVE_FOR edges")
        for e in edges[:3]:
            print(f"  {e['source']} -> {e['target']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())