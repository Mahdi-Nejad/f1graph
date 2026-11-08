"""Download F1 data for one season and save it to data/raw/."""

import argparse
import json
import sys
from pathlib import Path

from f1graph.io.jolpica import JolpicaError, fetch

OUT_DIR = Path("data/raw")

# type -> (endpoint, table key, list key) in the Jolpica payload
ENDPOINTS = {
    "drivers": ("drivers", "DriverTable", "Drivers"),
    "constructors": ("constructors", "ConstructorTable", "Constructors"),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("season", help="season year, e.g. 2026")
    parser.add_argument("--type", choices=ENDPOINTS, default="drivers")
    args = parser.parse_args()

    endpoint, table_key, list_key = ENDPOINTS[args.type]

    try:
        data = fetch(f"{args.season}/{endpoint}/")
        items = data[table_key][list_key]
    except (JolpicaError, KeyError) as exc:
        print(f"failed: {exc}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{args.type}_{args.season}.json"
    out_path.write_text(json.dumps(items, indent=2))

    print(f"{len(items)} {args.type} -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())