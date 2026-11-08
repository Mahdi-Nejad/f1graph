"""Tests for the Jolpica client."""

import httpx
import pytest

from f1graph.io import jolpica


def test_fetch_unwraps_mrdata(monkeypatch):
    payload = {"MRData": {"DriverTable": {"Drivers": []}}}

    def fake_get(url, **_):
        request = httpx.Request("GET", url)
        return httpx.Response(200, json=payload, request=request)

    monkeypatch.setattr(httpx, "get", fake_get)

    result = jolpica.fetch("2024/drivers/")

    assert result == {"DriverTable": {"Drivers": []}}


def test_fetch_raises_on_bad_shape(monkeypatch):
    def fake_get(url, **_):
        request = httpx.Request("GET", url)
        return httpx.Response(200, json={"something": "else"}, request=request)

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(jolpica.JolpicaError):
        jolpica.fetch("2024/drivers/")


# TODO: cover httpx errors (network fail, 500, bad JSON).