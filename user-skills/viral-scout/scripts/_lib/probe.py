"""ffprobe wrapper — read media duration without external deps."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


def duration_seconds(path: Path) -> float:
    """Return container duration in seconds. Raises if ffprobe missing or file unreadable."""
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe not on PATH (install ffmpeg)")
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "json",
        str(path),
    ]
    res = subprocess.run(cmd, check=True, capture_output=True, text=True)
    data = json.loads(res.stdout)
    return float(data["format"]["duration"])


def durations(paths: list[Path]) -> dict[str, float]:
    """Map filename → seconds for a batch."""
    return {p.name: duration_seconds(p) for p in paths}
