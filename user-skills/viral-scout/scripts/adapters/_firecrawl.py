"""Shared Firecrawl client (REST v1)."""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib import config  # noqa: E402

BASE = "https://api.firecrawl.dev/v1"


def scrape(url: str, *, formats: list[str] | None = None, timeout: int = 60) -> dict:
    """Returns the Firecrawl response body. Raises on HTTP errors."""
    api_key = config.get("FIRECRAWL_API_KEY", required=True)
    payload = {
        "url": url,
        "formats": formats or ["markdown", "html"],
        "onlyMainContent": False,
    }
    req = urllib.request.Request(
        f"{BASE}/scrape",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Firecrawl HTTP {e.code}: {body[:200]}") from e
