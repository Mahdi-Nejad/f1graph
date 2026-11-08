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


# TODO: switch to networkx when relations come in.