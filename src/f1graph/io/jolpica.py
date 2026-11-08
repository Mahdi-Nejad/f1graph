"""Client for the Jolpica F1 API."""

import httpx

BASE_URL = "https://api.jolpi.ca/ergast/f1"
TIMEOUT = 30.0


class JolpicaError(Exception):
    """Something went wrong talking to Jolpica."""


def fetch(endpoint: str) -> dict:
    """Fetch one endpoint and return its payload."""
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    try:
        response = httpx.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise JolpicaError(f"GET {url} failed") from exc

    if "MRData" not in payload:
        raise JolpicaError(f"unexpected shape from {url}")
    return payload["MRData"]
