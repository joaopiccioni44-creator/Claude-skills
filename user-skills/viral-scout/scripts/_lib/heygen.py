"""HeyGen REST client — stdlib only.

API docs: https://docs.heygen.com/reference

Auth: `X-Api-Key` header. Get key at https://app.heygen.com/settings?nav=API

Endpoints used:
- GET  https://api.heygen.com/v2/voices                 — list voices
- GET  https://api.heygen.com/v2/avatars                — list stock avatars + talking photos
- POST https://api.heygen.com/v2/video/generate         — submit a job, returns {video_id}
- GET  https://api.heygen.com/v1/video_status.get       — poll job status
"""
from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from . import config

BASE = "https://api.heygen.com"
DEFAULT_TIMEOUT = 30
POLL_INTERVAL_S = 5
POLL_TIMEOUT_S = 60 * 15  # 15 min hard ceiling per job


class HeyGenError(RuntimeError):
    pass


def _headers() -> dict[str, str]:
    api_key = config.get("HEYGEN_API_KEY", required=True)
    return {
        "X-Api-Key": api_key,
        "Accept": "application/json",
    }


def _request(method: str, path: str, *, params: dict | None = None,
             body: dict | None = None, timeout: int = DEFAULT_TIMEOUT) -> dict:
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = _headers()
    data: bytes | None = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body_txt = e.read().decode("utf-8", errors="replace")[:500]
        raise HeyGenError(f"HTTP {e.code} {method} {path}: {body_txt}") from e
    if not raw:
        return {}
    return json.loads(raw)


# ---------- Voices ----------

def list_voices() -> list[dict]:
    """Return raw voice list. Each item has voice_id, language, gender, name, preview_audio, ..."""
    resp = _request("GET", "/v2/voices")
    return (resp.get("data") or {}).get("voices") or []


def filter_voices(voices: list[dict], *, language: str | None = None,
                  gender: str | None = None) -> list[dict]:
    """Case-insensitive substring filter on language/gender. Returns matches."""
    out = []
    for v in voices:
        if language and language.lower() not in (v.get("language") or "").lower():
            continue
        if gender and gender.lower() != (v.get("gender") or "").lower():
            continue
        out.append(v)
    return out


# ---------- Avatars / Photo Avatars ----------

def list_avatars() -> dict:
    """Return full /v2/avatars payload: {data: {avatars: [...], talking_photos: [...]}}."""
    return _request("GET", "/v2/avatars")


# ---------- Video generation ----------

def build_video_input(*, character: dict, voice_id: str, input_text: str,
                      speed: float = 1.0) -> dict:
    """Construct one `video_inputs[]` entry.

    `character` is the full character dict — caller decides type:
      - {"type": "avatar", "avatar_id": "...", "avatar_style": "normal"}
      - {"type": "talking_photo", "talking_photo_id": "..."}
    """
    return {
        "character": character,
        "voice": {
            "type": "text",
            "input_text": input_text,
            "voice_id": voice_id,
            "speed": speed,
        },
    }


def generate_video(*, video_inputs: list[dict],
                   width: int = 720, height: int = 1280,
                   caption: bool = False) -> str:
    """Submit a render job. Returns video_id (poll with poll_status)."""
    body = {
        "video_inputs": video_inputs,
        "dimension": {"width": width, "height": height},
        "caption": caption,
    }
    resp = _request("POST", "/v2/video/generate", body=body)
    video_id = (resp.get("data") or {}).get("video_id") or resp.get("video_id")
    if not video_id:
        raise HeyGenError(f"no video_id in response: {resp}")
    return video_id


def get_status(video_id: str) -> dict:
    """Returns {status: 'pending'|'processing'|'completed'|'failed', video_url, error, ...}."""
    resp = _request("GET", "/v1/video_status.get", params={"video_id": video_id})
    return resp.get("data") or {}


def poll_status(video_id: str, *,
                interval_s: int = POLL_INTERVAL_S,
                timeout_s: int = POLL_TIMEOUT_S,
                on_tick=None) -> dict:
    """Block until completed/failed/timeout. Returns final status dict.

    on_tick(status_dict) called after each poll (for logging).
    """
    deadline = time.monotonic() + timeout_s
    while True:
        st = get_status(video_id)
        if on_tick:
            on_tick(st)
        state = st.get("status")
        if state == "completed":
            return st
        if state == "failed":
            raise HeyGenError(f"video {video_id} failed: {st.get('error')}")
        if time.monotonic() > deadline:
            raise HeyGenError(f"video {video_id} timed out after {timeout_s}s "
                              f"(last status: {state})")
        time.sleep(interval_s)


def download(url: str, dest: Path, *, timeout: int = 300) -> Path:
    """Stream a completed video_url to disk."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=timeout) as resp, open(dest, "wb") as f:
        while chunk := resp.read(64 * 1024):
            f.write(chunk)
    return dest


# ---------- Convenience: full render ----------

def render_to_file(*, character: dict, voice_id: str, input_text: str,
                   dest: Path, width: int = 720, height: int = 1280,
                   speed: float = 1.0, log=print) -> dict:
    """Submit + poll + download. Returns final status dict (includes video_url, duration)."""
    vi = build_video_input(character=character, voice_id=voice_id,
                           input_text=input_text, speed=speed)
    video_id = generate_video(video_inputs=[vi], width=width, height=height)
    log(f"[heygen] submitted video_id={video_id}")

    def _tick(st):
        log(f"[heygen] {video_id} status={st.get('status')}")

    final = poll_status(video_id, on_tick=_tick)
    url = final.get("video_url")
    if not url:
        raise HeyGenError(f"completed but no video_url: {final}")
    download(url, dest)
    log(f"[heygen] downloaded → {dest}")
    final["local_path"] = str(dest)
    return final
