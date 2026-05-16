"""Instagram Reels free-tier adapter via Firecrawl on public hashtag pages."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.metrics import parse_count  # noqa: E402
from _lib.slug import slugify  # noqa: E402

from . import _firecrawl  # noqa: E402

REEL_URL_RE = re.compile(r"https?://(?:www\.)?instagram\.com/(?:reel|p)/([\w-]+)")


def _tag_url(theme: str) -> str:
    tag = re.sub(r"[^a-z0-9]+", "", slugify(theme).replace("-", ""))
    return f"https://www.instagram.com/explore/tags/{tag}/"


def search(theme: str, *, limit: int = 25, min_views: int = 500_000, **_: object) -> list[dict]:
    try:
        resp = _firecrawl.scrape(_tag_url(theme), formats=["markdown"])
    except Exception as e:
        print(f"[instagram_free] scrape failed: {e}", file=sys.stderr)
        return []

    body = resp.get("data", {}).get("markdown") or ""
    seen: dict[str, dict] = {}
    for m in REEL_URL_RE.finditer(body):
        rid = m.group(1)
        if rid in seen:
            continue
        window = body[m.end(): m.end() + 300]
        vm = re.search(r"([\d.,]+\s*(?:K|M|B)?)\s*(?:views?|plays?|visualiza|curtidas?|likes?)",
                       window, re.IGNORECASE)
        views = parse_count(vm.group(1)) if vm else None
        if views is None or views < min_views:
            continue
        seen[rid] = {
            "platform": "instagram",
            "video_id": rid,
            "url": m.group(0),
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
    return sorted(seen.values(), key=lambda r: r["metrics"]["views"], reverse=True)[:limit]


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
