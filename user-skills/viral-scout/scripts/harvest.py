#!/usr/bin/env python3
"""Download video + thumbnail + transcript for a single URL.

Transcript cascade: subtitles from yt-dlp (when available) → whisper.cpp local → OpenAI Whisper API (optional fallback).

Usage:
    harvest.py --url "https://..." --out-dir <dir>
    harvest.py --meta-from <video-dir>/meta.json   # use existing meta.json
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import config  # noqa: E402


def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=False, capture_output=True, text=True, **kw)


def download_video(url: str, out_dir: Path) -> dict:
    """yt-dlp: video + thumbnail + info.json + auto-subs in one pass.

    Returns the parsed info.json dict, or {} if it wasn't created.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # Pass 1 (critical): video + thumbnail + info.json. No subs here — sub fetches often 429.
    video_cmd = [
        "yt-dlp",
        "-f", "bv*[height<=1080]+ba/b[height<=1080]/b",
        "--merge-output-format", "mp4",
        "--write-thumbnail",
        "--convert-thumbnails", "jpg",
        "--write-info-json",
        "--no-progress", "--no-warnings",
        "-o", str(out_dir / "video.%(ext)s"),
        url,
    ]
    res = _run(video_cmd)
    has_video = any(out_dir.glob("video.mp4")) or any(out_dir.glob("video.mkv")) \
                or any(out_dir.glob("video.webm"))
    if res.returncode != 0 and not has_video:
        sys.stderr.write(f"[harvest] yt-dlp failed:\n{res.stderr}\n")
        raise RuntimeError("yt-dlp download failed")

    # Pass 2 (best-effort): subtitles. Failures here just push us onto whisper.
    sub_cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-auto-sub", "--write-sub", "--sub-lang", "pt.*,en.*",
        "--sub-format", "vtt/srt/best",
        "--no-abort-on-error", "--ignore-no-formats-error",
        "--no-progress", "--no-warnings",
        "-o", str(out_dir / "video.%(ext)s"),
        url,
    ]
    sub_res = _run(sub_cmd)
    if sub_res.returncode != 0:
        sys.stderr.write(f"[harvest] subtitle fetch failed (will fall back to whisper): "
                         f"{sub_res.stderr[-200:]}\n")

    info_path = out_dir / "video.info.json"
    if info_path.exists():
        return json.loads(info_path.read_text())
    return {}


def find_subtitle_file(out_dir: Path) -> Path | None:
    for ext in ("vtt", "srt"):
        for lang in ("pt", "pt-BR", "en"):
            f = out_dir / f"video.{lang}.{ext}"
            if f.exists() and f.stat().st_size > 100:
                return f
    candidates = list(out_dir.glob("video.*.vtt")) + list(out_dir.glob("video.*.srt"))
    return next((c for c in candidates if c.stat().st_size > 100), None)


_INLINE_TAG_RE = re.compile(r"<[^>]+>")
_HTML_ENT_RE = re.compile(r"&(nbsp|amp|lt|gt|quot|#\d+);")


def subtitles_to_text(sub_path: Path) -> str:
    """Strip VTT/SRT timing + cue numbers + inline timing tags, return clean body."""
    lines: list[str] = []
    for raw in sub_path.read_text(encoding="utf-8", errors="replace").splitlines():
        s = raw.strip()
        if not s or s == "WEBVTT" or s.isdigit() or "-->" in s:
            continue
        if s.startswith(("NOTE", "STYLE", "Kind:", "Language:")):
            continue
        # Strip inline <00:00:00.960><c>...</c> word-level timing tags.
        s = _INLINE_TAG_RE.sub("", s).strip()
        if not s:
            continue
        s = _HTML_ENT_RE.sub(" ", s)
        lines.append(s)
    # Dedupe consecutive AND remove lines fully contained in the previous line
    # (YouTube auto-subs repeat each line twice as it grows).
    deduped: list[str] = []
    for line in lines:
        if deduped and (line == deduped[-1] or line in deduped[-1]):
            continue
        deduped.append(line)
    return "\n".join(deduped).strip()


def extract_audio_16k(video_path: Path) -> Path:
    audio_path = video_path.parent / "audio.wav"
    cmd = ["ffmpeg", "-y", "-i", str(video_path),
           "-ar", "16000", "-ac", "1", "-f", "wav", str(audio_path)]
    res = _run(cmd)
    if res.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {res.stderr[-500:]}")
    return audio_path


def whisper_cpp_transcribe(audio_path: Path, *, language: str | None = None) -> str | None:
    model_path = config.get("WHISPER_MODEL_PATH")
    if not model_path or not Path(model_path).exists():
        return None
    binary = shutil.which("whisper-cli") or shutil.which("whisper-cpp")
    if not binary:
        return None
    prefix = audio_path.with_suffix("")
    cmd = [binary, "-m", model_path, "-f", str(audio_path),
           "--output-txt", "--output-file", str(prefix), "-nt"]
    if language:
        cmd.extend(["-l", language])
    res = _run(cmd, timeout=60 * 30)
    if res.returncode != 0:
        sys.stderr.write(f"[harvest] whisper.cpp failed:\n{res.stderr[-500:]}\n")
        return None
    txt_path = prefix.with_suffix(".txt")
    if not txt_path.exists():
        return None
    return txt_path.read_text(encoding="utf-8").strip()


def whisper_api_transcribe(audio_path: Path) -> str | None:
    api_key = config.get("OPENAI_API_KEY")
    if not api_key:
        return None
    boundary = "----viralscout"
    body_parts: list[bytes] = []

    def field(name: str, value: str) -> bytes:
        return (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n").encode()

    body_parts.append(field("model", "whisper-1"))
    body_parts.append(field("response_format", "text"))
    body_parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
        f"filename=\"{audio_path.name}\"\r\nContent-Type: audio/wav\r\n\r\n".encode()
    )
    body_parts.append(audio_path.read_bytes())
    body_parts.append(f"\r\n--{boundary}--\r\n".encode())
    body = b"".join(body_parts)

    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception as e:
        sys.stderr.write(f"[harvest] OpenAI Whisper API failed: {e}\n")
        return None


def transcript_cascade(out_dir: Path, *, language: str | None = None) -> tuple[str, str]:
    """Return (transcript_text, source_label)."""
    sub = find_subtitle_file(out_dir)
    if sub:
        text = subtitles_to_text(sub)
        if len(text) > 50:
            return text, "subtitles"

    video_path = out_dir / "video.mp4"
    if not video_path.exists():
        # mkv/webm fallback
        for cand in out_dir.glob("video.*"):
            if cand.suffix in (".mp4", ".mkv", ".webm", ".m4a"):
                video_path = cand
                break
    if not video_path.exists():
        raise RuntimeError("no video file found to transcribe")

    audio_path = extract_audio_16k(video_path)
    text = whisper_cpp_transcribe(audio_path, language=language)
    if text:
        return text, "whisper.cpp"

    text = whisper_api_transcribe(audio_path)
    if text:
        return text, "whisper.api"

    raise RuntimeError("transcript cascade exhausted (subs/whisper.cpp/openai all failed)")


def build_meta(info: dict, *, url: str) -> dict:
    """Map yt-dlp info.json into our unified schema."""
    return {
        "platform": info.get("extractor_key", "").lower() or _platform_from_url(url),
        "video_id": info.get("id"),
        "url": info.get("webpage_url", url),
        "title": info.get("title"),
        "caption": info.get("description"),
        "author": {
            "handle": info.get("uploader_id") or info.get("channel_id"),
            "followers": info.get("channel_follower_count"),
        },
        "metrics": {
            "views": info.get("view_count"),
            "likes": info.get("like_count"),
            "comments": info.get("comment_count"),
            "shares": None,
        },
        "posted_at": info.get("upload_date"),
        "duration_seconds": info.get("duration"),
        "thumbnail_url": info.get("thumbnail"),
        "language": info.get("language"),
        "source_quality": "full",
    }


def _platform_from_url(url: str) -> str:
    if "youtube" in url or "youtu.be" in url:
        return "youtube"
    if "tiktok" in url:
        return "tiktok"
    if "instagram" in url:
        return "instagram"
    if "kwai" in url:
        return "kwai"
    return "unknown"


def harvest(url: str, out_dir: Path, *, language: str | None = None) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    info = download_video(url, out_dir)
    meta = build_meta(info, url=url)
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    # normalize thumbnail filename
    for cand in list(out_dir.glob("video.jpg")) + list(out_dir.glob("video.*.jpg")):
        target = out_dir / "thumbnail.jpg"
        if cand != target and not target.exists():
            cand.rename(target)
            break

    transcript, source = transcript_cascade(out_dir, language=language or meta.get("language"))
    (out_dir / "transcript.txt").write_text(transcript)
    (out_dir / "transcript.meta.json").write_text(json.dumps({"source": source}, indent=2))

    # cleanup intermediates
    for noise in ("audio.wav",):
        p = out_dir / noise
        if p.exists():
            p.unlink()

    return {
        "out_dir": str(out_dir),
        "meta": meta,
        "transcript_chars": len(transcript),
        "transcript_source": source,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", help="Video URL")
    ap.add_argument("--out-dir", type=Path, help="Where to write video/transcript/meta")
    ap.add_argument("--meta-from", type=Path, help="Path to existing meta.json to harvest from")
    ap.add_argument("--language", default=None, help="Force language for whisper (pt, en, ...)")
    args = ap.parse_args()

    if args.meta_from:
        meta = json.loads(Path(args.meta_from).read_text())
        url = meta["url"]
        out_dir = Path(args.meta_from).parent
    elif args.url and args.out_dir:
        url = args.url
        out_dir = args.out_dir
    else:
        ap.error("provide --meta-from OR (--url + --out-dir)")
        return 2

    result = harvest(url, out_dir, language=args.language)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
