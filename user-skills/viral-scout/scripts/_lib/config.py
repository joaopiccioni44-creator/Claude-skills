"""Load configuration from ~/.config/viral-scout/.env with fallback to os.environ."""
from __future__ import annotations

import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "viral-scout"
ENV_FILE = CONFIG_DIR / ".env"

_loaded = False


def load() -> dict[str, str]:
    """Load env file once; return current resolved env dict (env file overrides os.environ when set)."""
    global _loaded
    if not _loaded and ENV_FILE.exists():
        for raw in ENV_FILE.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value and key not in os.environ:
                os.environ[key] = value
        _loaded = True
    return dict(os.environ)


def get(key: str, default: str | None = None, required: bool = False) -> str | None:
    load()
    value = os.environ.get(key, default)
    if required and not value:
        raise RuntimeError(
            f"Missing required env var {key}. Set it in {ENV_FILE} or your shell."
        )
    return value
