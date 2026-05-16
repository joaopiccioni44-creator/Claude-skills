"""Filesystem layout for viral-runs."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .slug import slugify


def workspace_context_dir() -> Path:
    """Resolve .context/ in the current workspace. Falls back to CWD/.context."""
    cwd = Path.cwd()
    for parent in [cwd, *cwd.parents]:
        candidate = parent / ".context"
        if candidate.is_dir():
            return candidate
    fallback = cwd / ".context"
    fallback.mkdir(exist_ok=True)
    return fallback


def viral_runs_root() -> Path:
    root = workspace_context_dir() / "viral-runs"
    root.mkdir(parents=True, exist_ok=True)
    return root


def new_run_dir(theme: str, *, when: datetime | None = None) -> Path:
    when = when or datetime.now()
    stamp = when.strftime("%Y-%m-%d-%H%M")
    run = viral_runs_root() / slugify(theme) / stamp
    (run / "videos").mkdir(parents=True, exist_ok=True)
    return run


def video_dir(run: Path, platform: str, video_id: str) -> Path:
    safe_id = "".join(c if c.isalnum() or c in "-_" else "_" for c in video_id)
    d = run / "videos" / f"{platform}-{safe_id}"
    d.mkdir(parents=True, exist_ok=True)
    return d
