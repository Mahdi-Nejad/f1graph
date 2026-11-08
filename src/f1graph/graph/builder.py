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

# TODO: switch to networkx when relations come in.