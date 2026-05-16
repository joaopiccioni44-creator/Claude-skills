#!/usr/bin/env python3
"""Aggregate per-video analyses into a single brief.json consumable by ugc-video-auto.

Usage:
    brief.py --run-dir <run-dir>
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analyze import call_claude, extract_json  # noqa: E402

RECREATION_PROMPT = """You are a UGC scriptwriter. Given a viral video's analysis + transcript,
produce a recreation brief in Portuguese (PT-BR) that a single-person avatar pipeline can shoot.

INPUT (via stdin): a JSON object with the original analysis + transcript_excerpt + original_meta.

OUTPUT: a single JSON object only, no prose, no fences:
{
  "suggested_hook_pt": "1-2 sentence opening that adapts the original hook to PT-BR talking-head",
  "script_skeleton": "outline of the spoken script (Fagulha/Afirmação/Linha-do-tempo/Argumento/Reforço bullets)",
  "shot_list_suggestion": ["talking head close-up", "b-roll: ..."],
  "duration_target_s": 45
}

Rules:
- The script_skeleton must be shorter than the original (avatar pipeline favors 30-60s).
- Preserve the viral lever identified in viral_hypothesis.
- shot_list_suggestion: 3-6 entries, concrete and shootable solo.
"""


def per_video_brief(rank: int, source_meta: dict, analysis: dict, transcript: str) -> dict:
    return {
        "rank": rank,
        "source": {
            "platform": source_meta.get("platform"),
            "url": source_meta.get("url"),
            "author_handle": (source_meta.get("author") or {}).get("handle"),
            "views": (source_meta.get("metrics") or {}).get("views"),
            "posted_at": source_meta.get("posted_at"),
        },
        "hook": analysis.get("hook"),
        "structure": analysis.get("structure"),
        "visual": analysis.get("visual"),
        "cta": analysis.get("cta"),
        "viral_hypothesis": analysis.get("viral_hypothesis"),
        "transcript_excerpt": transcript[:500],
        "ugc_recreation_brief": None,
    }


def recreation_brief(entry: dict) -> dict | None:
    payload = json.dumps({
        "analysis": {
            "hook": entry["hook"],
            "structure": entry["structure"],
            "visual": entry["visual"],
            "cta": entry["cta"],
            "viral_hypothesis": entry["viral_hypothesis"],
        },
        "transcript_excerpt": entry["transcript_excerpt"],
        "original_meta": entry["source"],
    }, ensure_ascii=False)
    try:
        raw = call_claude(RECREATION_PROMPT, payload, timeout=180)
        return extract_json(raw)
    except Exception as e:
        sys.stderr.write(f"[brief] recreation failed for rank={entry['rank']}: {e}\n")
        return None


def build_brief(run_dir: Path, *, skip_recreation: bool = False) -> dict:
    filtered_path = run_dir / "filtered.json"
    if not filtered_path.exists():
        raise RuntimeError(f"missing {filtered_path}")
    filtered = json.loads(filtered_path.read_text())

    candidates: list[dict] = []
    for rank, item in enumerate(filtered, start=1):
        platform = item["platform"]
        vid = item["video_id"]
        safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in vid)
        vdir = run_dir / "videos" / f"{platform}-{safe}"
        analysis_path = vdir / "analysis.json"
        meta_path = vdir / "meta.json"
        trans_path = vdir / "transcript.txt"
        if not (analysis_path.exists() and meta_path.exists() and trans_path.exists()):
            sys.stderr.write(f"[brief] skipping {platform}/{vid}: missing artifacts in {vdir}\n")
            continue
        meta = json.loads(meta_path.read_text())
        analysis = json.loads(analysis_path.read_text())
        transcript = trans_path.read_text()
        entry = per_video_brief(rank, meta, analysis, transcript)
        if not skip_recreation:
            entry["ugc_recreation_brief"] = recreation_brief(entry)
        candidates.append(entry)

    manifest_path = run_dir / "manifest.json"
    theme = None
    theme_slug = None
    if manifest_path.exists():
        m = json.loads(manifest_path.read_text())
        theme = m.get("theme")
        theme_slug = m.get("theme_slug")

    brief = {
        "theme": theme,
        "theme_slug": theme_slug,
        "run_id": run_dir.name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    (run_dir / "brief.json").write_text(json.dumps(brief, indent=2, ensure_ascii=False))
    return brief


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--skip-recreation", action="store_true",
                    help="Don't call Claude for ugc_recreation_brief (faster, cheaper)")
    args = ap.parse_args()
    brief = build_brief(args.run_dir, skip_recreation=args.skip_recreation)
    print(json.dumps({
        "run_dir": str(args.run_dir),
        "candidate_count": brief["candidate_count"],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
