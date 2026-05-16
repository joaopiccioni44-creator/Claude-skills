"""YouTube Data API v3 adapter.

Two-step flow: search.list returns video IDs, videos.list returns statistics
(view count) + contentDetails (duration) in one batch.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib import config  # noqa: E402

API_BASE = "https://www.googleapis.com/youtube/v3"


def _get(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read())


def _parse_iso8601_duration(d: str) -> int | None:
    """PT1M30S -> 90."""
    if not d:
        return None
    m = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d)
    if not m:
        return None
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


def search(
    theme: str,
    *,
    limit: int = 25,
    min_views: int = 500_000,
    region: str = "BR",
    language: str = "pt",
    **_: object,
) -> list[dict]:
    api_key = config.get("YOUTUBE_API_KEY", required=True)

    # Step 1: search.list — returns video IDs ordered by relevance.
    # We over-fetch (2x limit) since most won't pass the view threshold.
    search_params = {
        "key": api_key,
        "part": "snippet",
        "q": theme,
        "type": "video",
        "maxResults": str(min(50, max(limit * 2, 10))),
        "regionCode": region,
        "relevanceLanguage": language,
        "order": "viewCount",
    }
    search_url = f"{API_BASE}/search?{urllib.parse.urlencode(search_params)}"
    search_resp = _get(search_url)
    items = search_resp.get("items", [])
    if not items:
        return []

    ids = [it["id"]["videoId"] for it in items if it.get("id", {}).get("videoId")]
    if not ids:
        return []

    # Step 2: videos.list — batch fetch statistics + contentDetails.
    videos_params = {
        "key": api_key,
        "part": "snippet,statistics,contentDetails",
        "id": ",".join(ids),
        "maxResults": "50",
    }
    videos_url = f"{API_BASE}/videos?{urllib.parse.urlencode(videos_params)}"
    videos_resp = _get(videos_url)

    results: list[dict] = []
    for v in videos_resp.get("items", []):
        stats = v.get("statistics", {})
        snippet = v.get("snippet", {})
        details = v.get("contentDetails", {})
        views = int(stats.get("viewCount", "0") or 0)
        if views < min_views:
            continue
        vid = v["id"]
        results.append({
            "platform": "youtube",
            "video_id": vid,
            "url": f"https://www.youtube.com/watch?v={vid}",
            "title": snippet.get("title"),
            "caption": snippet.get("description"),
            "author": {
                "handle": snippet.get("channelTitle"),
                "followers": None,
            },
            "metrics": {
                "views": views,
                "likes": int(stats["likeCount"]) if stats.get("likeCount") else None,
                "comments": int(stats["commentCount"]) if stats.get("commentCount") else None,
                "shares": None,
            },
            "posted_at": snippet.get("publishedAt"),
            "duration_seconds": _parse_iso8601_duration(details.get("duration", "")),
            "thumbnail_url": (snippet.get("thumbnails", {}).get("high", {}).get("url")
                              or snippet.get("thumbnails", {}).get("default", {}).get("url")),
            "language": snippet.get("defaultAudioLanguage") or snippet.get("defaultLanguage"),
            "source_quality": "full",
        })

    results.sort(key=lambda r: r["metrics"]["views"], reverse=True)
    return results[:limit]


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--min-views", type=int, default=500_000)
    p.add_argument("--region", default="BR")
    p.add_argument("--language", default="pt")
    args = p.parse_args()
    out = search(args.theme, limit=args.limit, min_views=args.min_views,
                 region=args.region, language=args.language)
    print(json.dumps(out, indent=2, ensure_ascii=False))
