from f1graph.graph.builder import driver_nodes


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