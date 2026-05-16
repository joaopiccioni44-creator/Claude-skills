#!/usr/bin/env python3
"""End-to-end orchestrator: discover → harvest → analyze → brief.

Usage:
    run_all.py --theme "..." [--limit 10] [--min-views 500000]
               [--platforms youtube,tiktok,instagram,kwai] [--use-apify]
               [--skip-recreation] [--max-harvest N]
"""
from __future__ import annotations

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.paths import new_run_dir, video_dir  # noqa: E402
from _lib.slug import slugify  # noqa: E402
from discover import discover  # noqa: E402
from harvest import harvest  # noqa: E402
from analyze import analyze  # noqa: E402
from brief import build_brief  # noqa: E402


def run(theme: str, *, platforms: list[str], min_views: int, limit: int,
        use_apify: bool, region: str, language: str,
        max_harvest: int | None, skip_recreation: bool) -> dict:
    run_dir = new_run_dir(theme)
    started = datetime.now(timezone.utc)
    errors: list[dict] = []
    by_platform: dict[str, int] = {}

    print(f"[run_all] theme={theme!r} run_dir={run_dir}", file=sys.stderr)

    # 1. Discover
    disc = discover(theme, platforms=platforms, min_views=min_views, limit=limit,
                    use_apify=use_apify, region=region, language=language, run_dir=run_dir)
    filtered = disc["filtered"]
    print(f"[run_all] discovered={sum(p['count'] for p in disc['raw'].values())} "
          f"filtered={len(filtered)}", file=sys.stderr)

    targets = filtered if max_harvest is None else filtered[:max_harvest]
    harvested = 0
    analyzed = 0

    # 2. Harvest + 3. Analyze per video
    for item in targets:
        platform = item["platform"]
        vid = item["video_id"]
        url = item["url"]
        vdir = video_dir(run_dir, platform, vid)
        # seed meta.json with the discovery payload so harvest can enrich it
        (vdir / "meta.json").write_text(json.dumps(item, indent=2, ensure_ascii=False))
        try:
            print(f"[run_all] harvest {platform}/{vid}", file=sys.stderr)
            harvest(url, vdir, language=item.get("language"))
            harvested += 1
        except Exception as e:
            errors.append({"stage": "harvest", "platform": platform, "video_id": vid,
                           "error": f"{type(e).__name__}: {e}"})
            sys.stderr.write(f"[run_all] harvest failed for {platform}/{vid}: {e}\n")
            traceback.print_exc(file=sys.stderr)
            continue
        try:
            print(f"[run_all] analyze {platform}/{vid}", file=sys.stderr)
            analyze(vdir)
            analyzed += 1
            by_platform[platform] = by_platform.get(platform, 0) + 1
        except Exception as e:
            errors.append({"stage": "analyze", "platform": platform, "video_id": vid,
                           "error": f"{type(e).__name__}: {e}"})
            sys.stderr.write(f"[run_all] analyze failed for {platform}/{vid}: {e}\n")

    # 4. Write manifest
    finished = datetime.now(timezone.utc)
    manifest = {
        "theme": theme,
        "theme_slug": slugify(theme),
        "run_id": run_dir.name,
        "started_at": started.isoformat(),
        "finished_at": finished.isoformat(),
        "params": {
            "min_views": min_views,
            "limit": limit,
            "platforms": platforms,
            "use_apify": use_apify,
            "language": language,
            "region": region,
        },
        "summary": {
            "discovered": sum(p["count"] for p in disc["raw"].values()),
            "filtered": len(filtered),
            "harvested": harvested,
            "analyzed": analyzed,
            "by_platform": by_platform,
        },
        "cost_estimate_usd": 0.0,
        "errors": errors,
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    # 5. Brief
    if analyzed > 0:
        print(f"[run_all] brief ({analyzed} candidates, skip_recreation={skip_recreation})",
              file=sys.stderr)
        build_brief(run_dir, skip_recreation=skip_recreation)
    else:
        sys.stderr.write("[run_all] no analyses available — skipping brief.json\n")

    return {"run_dir": str(run_dir), "manifest": manifest}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", required=True)
    ap.add_argument("--min-views", type=int, default=500_000)
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--platforms", default="youtube,tiktok,instagram,kwai")
    ap.add_argument("--use-apify", action="store_true")
    ap.add_argument("--region", default="BR")
    ap.add_argument("--language", default="pt")
    ap.add_argument("--max-harvest", type=int, default=None,
                    help="Cap how many discovered videos to actually download (defaults to all filtered)")
    ap.add_argument("--skip-recreation", action="store_true")
    args = ap.parse_args()

    platforms = [p.strip() for p in args.platforms.split(",") if p.strip()]
    out = run(args.theme, platforms=platforms, min_views=args.min_views, limit=args.limit,
              use_apify=args.use_apify, region=args.region, language=args.language,
              max_harvest=args.max_harvest, skip_recreation=args.skip_recreation)
    print(json.dumps({
        "run_dir": out["run_dir"],
        "summary": out["manifest"]["summary"],
        "error_count": len(out["manifest"]["errors"]),
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
