"""Download driver data for one season and save it to data/raw/."""

import argparse
import json
import sys
from pathlib import Path

from f1graph.io.jolpica import JolpicaError, fetch

OUT_DIR = Path("data/raw")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("season", help="season year, e.g. 2026")
    args = parser.parse_args()

    try:
        data = fetch(f"{args.season}/drivers/")
        drivers = data["DriverTable"]["Drivers"]
    except (JolpicaError, KeyError) as exc:
        print(f"failed: {exc}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"drivers_{args.season}.json"
    out_path.write_text(json.dumps(drivers, indent=2))

    print(f"{len(drivers)} drivers -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())


# TODO: parameterize the entity type (drivers, constructors, races).