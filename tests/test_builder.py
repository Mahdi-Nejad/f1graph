from f1graph.graph.builder import constructor_nodes, driver_nodes, drove_for_edges


def test_driver_nodes_uses_driver_id_as_key():
    drivers = [
        {
            "driverId": "albon",
            "givenName": "Alexander",
            "familyName": "Albon",
            "code": "ALB",
            "nationality": "Thai",
        },
    ]

    nodes = driver_nodes(drivers)

    assert set(nodes) == {"albon"}
    assert nodes["albon"]["label"] == "Alexander Albon"
    assert nodes["albon"]["code"] == "ALB"


def test_constructor_nodes_uses_constructor_id_as_key():
    constructors = [
        {
            "constructorId": "red_bull",
            "name": "Red Bull",
            "nationality": "Austrian",
        },
    ]

    nodes = constructor_nodes(constructors)

    assert set(nodes) == {"red_bull"}
    assert nodes["red_bull"]["label"] == "Red Bull"


def test_drove_for_edges_emits_one_edge_per_constructor():
    standings = [
        {
            "Driver": {"driverId": "verstappen"},
            "Constructors": [{"constructorId": "red_bull"}],
        },
        {
            "Driver": {"driverId": "bearman"},
            "Constructors": [
                {"constructorId": "ferrari"},
                {"constructorId": "haas"},
            ],
        },
    ]

    edges = drove_for_edges(standings)

    assert len(edges) == 3
    assert {"source": "verstappen", "target": "red_bull", "type": "DROVE_FOR"} in edges
    assert {"source": "bearman", "target": "haas", "type": "DROVE_FOR"} in edges