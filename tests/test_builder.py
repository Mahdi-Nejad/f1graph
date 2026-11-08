from f1graph.graph.builder import constructor_nodes, driver_nodes


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