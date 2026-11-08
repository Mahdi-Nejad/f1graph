"""Load the driver file and print a graph summary."""

import argparse
import json
import sys
from pathlib import Path

from f1graph.graph.builder import driver_nodes

RAW_DIR = Path("data/raw")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("season", help="season year, e.g. 2026")
    args = parser.parse_args()

    path = RAW_DIR / f"drivers_{args.season}.json"
    if not path.exists():
        print(f"missing {path}, run ingest first", file=sys.stderr)
        return 1

    drivers = json.loads(path.read_text())
    nodes = driver_nodes(drivers)

    print(f"{len(nodes)} driver nodes")
    for node_id, attrs in list(nodes.items())[:3]:
        code = attrs["code"] or "—"
        print(f"  {node_id}: {attrs['label']} ({code})")

    return 0


if __name__ == "__main__":
    sys.exit(main())