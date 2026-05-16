"""TikTok Apify adapter stub. Activates with --use-apify + APIFY_API_TOKEN.

Recommended actor: clockworks/tiktok-scraper. When ready, replace the
NotImplementedError with the actor call + result mapping.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib import config  # noqa: E402


def search(theme: str, *, limit: int = 25, min_views: int = 500_000, **_: object) -> list[dict]:
    token = config.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError(
            "TikTok Apify adapter requires APIFY_API_TOKEN in ~/.config/viral-scout/.env"
        )

    # TODO: wire actor input + run + dataset fetch.
    # Sketch:
    #   1. POST run-sync-get-dataset-items to actor clockworks~tiktok-scraper
    #      with body { "hashtags": [theme_slug], "resultsPerPage": limit*2 }
    #   2. Map each item to the unified schema (item['playCount'] -> views, etc.)
    #   3. Filter by min_views, return top `limit` sorted by views.
    raise NotImplementedError(
        "tiktok_apify is a stub. Implement the clockworks/tiktok-scraper call when ready."
    )
