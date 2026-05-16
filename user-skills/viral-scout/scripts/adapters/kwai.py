"""Kwai adapter via Firecrawl. Scrapes hashtag/discover pages and parses tiles.

Kwai has no public API. We use Firecrawl on hashtag pages, then parse the
markdown output for /short-video/ links plus their abbreviated view counts.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.metrics import parse_count  # noqa: E402
from _lib.slug import slugify  # noqa: E402

from . import _firecrawl  # noqa: E402

VIDEO_URL_RE = re.compile(r"https?://(?:www\.)?kwai\.com/(?:@[^/]+/)?(?:video|short-video)/(\w+)")


def _hashtag_url(theme: str) -> str:
    tag = re.sub(r"[^a-z0-9]+", "", slugify(theme).replace("-", ""))
    return f"https://www.kwai.com/search/video?searchKey={tag}"


def search(
    theme: str,
    *,
    limit: int = 25,
    min_views: int = 500_000,
    **_: object,
) -> list[dict]:
    url = _hashtag_url(theme)
    try:
        resp = _firecrawl.scrape(url, formats=["markdown"])
    except Exception as e:
        print(f"[kwai] scrape failed: {e}", file=sys.stderr)
        return []

    body = resp.get("data", {}).get("markdown") or ""
    if not body:
        return []

    # Parse tiles: video links sometimes followed by a view-count token (e.g. "1.2M views").
    seen: dict[str, dict] = {}
    for vid_match in VIDEO_URL_RE.finditer(body):
        vid_id = vid_match.group(1)
        if vid_id in seen:
            continue
        # Look ahead 200 chars for a view count.
        window = body[vid_match.end(): vid_match.end() + 300]
        view_match = re.search(r"([\d.,]+\s*(?:K|M|Mi|Mil|B)?)\s*(?:views?|visualiza|reprodu)",
                               window, re.IGNORECASE)
        views = parse_count(view_match.group(1)) if view_match else None
        if views is None or views < min_views:
            continue
        seen[vid_id] = {
            "platform": "kwai",
            "video_id": vid_id,
            "url": vid_match.group(0),
            "title": None,
            "caption": None,
            "author": {"handle": None, "followers": None},
            "metrics": {"views": views, "likes": None, "comments": None, "shares": None},
            "posted_at": None,
            "duration_seconds": None,
            "thumbnail_url": None,
            "language": None,
            "source_quality": "degraded",
        }

    results = sorted(seen.values(), key=lambda r: r["metrics"]["views"], reverse=True)
    return results[:limit]


if __name__ == "__main__":
    import argparse
    import json
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--min-views", type=int, default=500_000)
    args = p.parse_args()
    print(json.dumps(search(args.theme, limit=args.limit, min_views=args.min_views),
                     indent=2, ensure_ascii=False))
