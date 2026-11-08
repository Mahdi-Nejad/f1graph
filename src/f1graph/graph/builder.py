def driver_nodes(drivers: list[dict]) -> dict[str, dict]:
    """Build one node per driver, keyed by driverId."""
    return {
        d["driverId"]: {
            "label": f"{d['givenName']} {d['familyName']}",
            "code": d.get("code"),
            "nationality": d.get("nationality"),
        }
        for d in drivers
    }


def constructor_nodes(constructors: list[dict]) -> dict[str, dict]:
    """Build one node per constructor, keyed by constructorId."""
    return {
        c["constructorId"]: {
            "label": c["name"],
            "nationality": c.get("nationality"),
        }
        for c in constructors
    }


def drove_for_edges(standings: list[dict]) -> list[dict]:
    """Build DROVE_FOR edges from driver standings.

    Each driver can appear with multiple constructors in a season
    (mid-season replacement), so we emit one edge per constructor.
    """
    edges = []
    for entry in standings:
        driver_id = entry["Driver"]["driverId"]
        for c in entry["Constructors"]:
            edges.append(
                {
                    "source": driver_id,
                    "target": c["constructorId"],
                    "type": "DROVE_FOR",
                }
            )
    return edges


# TODO: switch to networkx when relations come in.