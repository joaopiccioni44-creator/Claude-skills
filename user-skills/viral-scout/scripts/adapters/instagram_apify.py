"""Instagram Apify adapter stub. Recommended actor: apify/instagram-scraper."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib import config  # noqa: E402


def search(theme: str, *, limit: int = 25, min_views: int = 500_000, **_: object) -> list[dict]:
    token = config.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError(
            "Instagram Apify adapter requires APIFY_API_TOKEN in ~/.config/viral-scout/.env"
        )
    raise NotImplementedError(
        "instagram_apify is a stub. Implement the apify/instagram-scraper call when ready."
    )
