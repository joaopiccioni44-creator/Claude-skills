#!/usr/bin/env python3
"""Multi-platform discovery router.

Usage:
    discover.py --theme "..." [--min-views 500000] [--limit 10]
                [--platforms youtube,tiktok,instagram,kwai] [--use-apify]
                [--run-dir <existing>] [--region BR] [--language pt]
"""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.paths import new_run_dir  # noqa: E402

ADAPTER_MAP = {
    "youtube": "adapters.youtube",
    "kwai": "adapters.kwai",
    "tiktok_free": "adapters.tiktok_free",
    "tiktok_apify": "adapters.tiktok_apify",
    "instagram_free": "adapters.instagram_free",
    "instagram_apify": "adapters.instagram_apify",
}


def resolve_adapters(platforms: list[str], use_apify: bool) -> list[tuple[str, str]]:
    """Return list of (label, module_path)."""
    out: list[tuple[str, str]] = []
    for p in platforms:
        if p == "youtube":
            out.append(("youtube", ADAPTER_MAP["youtube"]))
        elif p == "kwai":
            out.append(("kwai", ADAPTER_MAP["kwai"]))
        elif p == "tiktok":
            out.append(("tiktok", ADAPTER_MAP["tiktok_apify" if use_apify else "tiktok_free"]))
        elif p == "instagram":
            out.append(("instagram", ADAPTER_MAP["instagram_apify" if use_apify else "instagram_free"]))
        else:
            print(f"[discover] unknown platform: {p}", file=sys.stderr)
    return out


def run_one(label: str, module_path: str, kwargs: dict) -> tuple[str, list[dict] | None, str | None]:
    try:
        mod = importlib.import_module(module_path)
        return label, mod.search(**kwargs), None
    except Exception as e:
        return label, None, f"{type(e).__name__}: {e}"


def discover(
    theme: str,
    *,
    platforms: list[str],
    min_views: int,
    limit: int,
    use_apify: bool,
    region: str = "BR",
    language: str = "pt",
    run_dir: Path | None = None,
) -> dict:
    run_dir = run_dir or new_run_dir(theme)
    adapters = resolve_adapters(platforms, use_apify)
    kwargs = {"theme": theme, "limit": limit, "min_views": min_views,
              "region": region, "language": language}

    raw: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=min(4, len(adapters) or 1)) as ex:
        futures = {ex.submit(run_one, lbl, mod, kwargs): lbl for lbl, mod in adapters}
        for fut in as_completed(futures):
            label, items, err = fut.result()
            raw[label] = {
                "items": items or [],
                "error": err,
                "count": len(items) if items else 0,
            }
            status = "ok" if err is None else f"ERR {err}"
            print(f"[discover] {label}: {raw[label]['count']} items ({status})", file=sys.stderr)

    # Dedup across platforms by (platform, video_id) and filter by views.
    seen: set[tuple[str, str]] = set()
    filtered: list[dict] = []
    for label, payload in raw.items():
        for item in payload["items"]:
            key = (item["platform"], item["video_id"])
            if key in seen:
                continue
            if item.get("metrics", {}).get("views", 0) < min_views:
                continue
            seen.add(key)
            filtered.append(item)
    filtered.sort(key=lambda r: r["metrics"]["views"], reverse=True)

    (run_dir / "discovery.raw.json").write_text(
        json.dumps(raw, indent=2, ensure_ascii=False)
    )
    (run_dir / "filtered.json").write_text(
        json.dumps(filtered, indent=2, ensure_ascii=False)
    )

    return {"run_dir": str(run_dir), "raw": raw, "filtered": filtered}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", required=True)
    ap.add_argument("--min-views", type=int, default=500_000)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--platforms", default="youtube,tiktok,instagram,kwai")
    ap.add_argument("--use-apify", action="store_true")
    ap.add_argument("--region", default="BR")
    ap.add_argument("--language", default="pt")
    ap.add_argument("--run-dir", type=Path, default=None)
    args = ap.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    started = datetime.now()
    result = discover(
        args.theme,
        platforms=platforms,
        min_views=args.min_views,
        limit=args.limit,
        use_apify=args.use_apify,
        region=args.region,
        language=args.language,
        run_dir=args.run_dir,
    )

    print(json.dumps({
        "run_dir": result["run_dir"],
        "discovered": sum(p["count"] for p in result["raw"].values()),
        "filtered": len(result["filtered"]),
        "elapsed_s": round((datetime.now() - started).total_seconds(), 2),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
