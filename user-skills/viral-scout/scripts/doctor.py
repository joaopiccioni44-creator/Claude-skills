#!/usr/bin/env python3
"""Validate that viral-scout's dependencies + env are healthy.

Usage:
    doctor.py
"""
from __future__ import annotations

import json
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import config  # noqa: E402

CHECKS: list[tuple[str, str]] = []
OK, WARN, FAIL = "✅", "⚠️ ", "❌"


def add(status: str, msg: str) -> None:
    CHECKS.append((status, msg))


def check_binary(name: str, *, required: bool = True) -> None:
    path = shutil.which(name)
    if path:
        add(OK, f"{name} → {path}")
    elif required:
        add(FAIL, f"{name} not on PATH (required)")
    else:
        add(WARN, f"{name} not on PATH (optional)")


def check_env(name: str, *, required: bool = True) -> None:
    val = config.get(name)
    if val:
        add(OK, f"env {name} present ({len(val)} chars)")
    elif required:
        add(FAIL, f"env {name} missing (set in ~/.config/viral-scout/.env)")
    else:
        add(WARN, f"env {name} missing (optional)")


def check_file(label: str, path: str | None, *, required: bool = True) -> None:
    if not path:
        if required:
            add(FAIL, f"{label}: path not set")
        else:
            add(WARN, f"{label}: path not set (optional)")
        return
    p = Path(path).expanduser()
    if p.exists():
        size_mb = p.stat().st_size / 1_000_000
        add(OK, f"{label} → {p} ({size_mb:.0f} MB)")
    elif required:
        add(FAIL, f"{label}: {p} not found")
    else:
        add(WARN, f"{label}: {p} not found (optional)")


def check_firecrawl_reachable() -> None:
    """Probe API with a HEAD-like cheap call."""
    api_key = config.get("FIRECRAWL_API_KEY")
    if not api_key:
        return  # already reported by check_env
    req = urllib.request.Request(
        "https://api.firecrawl.dev/v1/scrape",
        headers={"Authorization": f"Bearer {api_key}"},
        method="OPTIONS",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            add(OK, f"Firecrawl reachable (HTTP {resp.status})")
    except urllib.error.HTTPError as e:
        if e.code in (200, 204, 401, 403, 405):
            add(OK, f"Firecrawl reachable (HTTP {e.code})")
        else:
            add(WARN, f"Firecrawl HTTP {e.code}")
    except Exception as e:
        add(WARN, f"Firecrawl probe failed: {type(e).__name__}: {e}")


def check_youtube_reachable() -> None:
    api_key = config.get("YOUTUBE_API_KEY")
    if not api_key:
        return
    url = f"https://www.googleapis.com/youtube/v3/videos?part=id&id=dQw4w9WgXcQ&key={api_key}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
            if data.get("items"):
                add(OK, "YouTube API key works (test query returned data)")
            else:
                add(WARN, f"YouTube API responded but empty: {data}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:200]
        add(FAIL, f"YouTube API HTTP {e.code}: {body}")
    except Exception as e:
        add(WARN, f"YouTube API probe failed: {type(e).__name__}: {e}")


def main() -> int:
    config.load()

    add(OK if (Path.home() / ".config" / "viral-scout" / ".env").exists() else WARN,
        f"~/.config/viral-scout/.env "
        f"{'present' if (Path.home() / '.config' / 'viral-scout' / '.env').exists() else 'MISSING — copy from skill assets/env.example'}")

    check_binary("yt-dlp", required=True)
    check_binary("ffmpeg", required=True)
    check_binary("whisper-cli", required=False)
    check_binary("whisper-cpp", required=False)
    check_binary("claude", required=True)

    check_env("YOUTUBE_API_KEY", required=True)
    check_env("FIRECRAWL_API_KEY", required=True)
    check_env("WHISPER_MODEL_PATH", required=True)
    check_env("OPENAI_API_KEY", required=False)
    check_env("APIFY_API_TOKEN", required=False)

    check_file("Whisper model", config.get("WHISPER_MODEL_PATH"), required=True)

    check_firecrawl_reachable()
    check_youtube_reachable()

    for status, msg in CHECKS:
        print(f"{status} {msg}")

    failures = sum(1 for s, _ in CHECKS if s == FAIL)
    warnings = sum(1 for s, _ in CHECKS if s == WARN)
    print()
    print(f"Summary: {len(CHECKS) - failures - warnings} ok, {warnings} warn, {failures} fail")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
