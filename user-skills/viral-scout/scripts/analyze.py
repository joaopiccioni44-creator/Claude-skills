#!/usr/bin/env python3
"""Narrative breakdown of a harvested video via Claude CLI (headless).

Reads meta.json + transcript.txt from --video-dir, sends them to
`claude -p ... --output-format json`, writes analysis.json.

Usage:
    analyze.py --video-dir <path>
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
PROMPT_FILE = SKILL_DIR / "references" / "analysis-prompt.md"


def load_prompt() -> str:
    """Extract the system prompt body between the '---' markers in the reference."""
    raw = PROMPT_FILE.read_text()
    # The prompt body sits between the first and last '---' lines in the file.
    parts = raw.split("\n---\n")
    if len(parts) >= 3:
        return parts[1].strip()
    return raw


def build_user_message(meta: dict, transcript: str) -> str:
    meta_str = json.dumps({
        "platform": meta.get("platform"),
        "author": meta.get("author", {}).get("handle"),
        "views": meta.get("metrics", {}).get("views"),
        "posted_at": meta.get("posted_at"),
        "title": meta.get("title"),
        "caption": meta.get("caption"),
        "duration": meta.get("duration_seconds"),
        "language": meta.get("language"),
    }, ensure_ascii=False, indent=2)
    return f"META:\n{meta_str}\n\nTRANSCRIPT:\n{transcript}"


def call_claude(prompt: str, user_input: str, *, timeout: int = 180) -> str:
    """Run `claude -p ... --output-format json`, return the inner `.result` string."""
    if not shutil.which("claude"):
        raise RuntimeError("`claude` CLI not on PATH")
    cmd = ["claude", "-p", prompt, "--output-format", "json"]
    res = subprocess.run(cmd, input=user_input, capture_output=True, text=True, timeout=timeout)
    if res.returncode != 0:
        raise RuntimeError(f"claude CLI exit {res.returncode}: {res.stderr[-500:]}")
    try:
        envelope = json.loads(res.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"claude returned non-JSON envelope: {e}: {res.stdout[:300]}") from e
    result = envelope.get("result")
    if not result:
        raise RuntimeError(f"claude envelope missing .result: {envelope}")
    return result


def extract_json(text: str) -> dict:
    """Parse a JSON object out of a possibly-fenced Claude reply."""
    text = text.strip()
    # Strip ```json ... ``` fences if present.
    fence = re.match(r"^```(?:json)?\s*(.+?)\s*```$", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    # Find the outermost { ... } if there's still extra prose.
    if not text.startswith("{"):
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            text = m.group(0)
    return json.loads(text)


REQUIRED_KEYS = {"hook", "structure", "visual", "cta", "viral_hypothesis"}


def analyze(video_dir: Path, *, max_retries: int = 1) -> dict:
    meta = json.loads((video_dir / "meta.json").read_text())
    transcript = (video_dir / "transcript.txt").read_text()
    if len(transcript) < 30:
        raise RuntimeError(f"transcript too short ({len(transcript)} chars) — refusing to analyze")

    prompt = load_prompt()
    user_msg = build_user_message(meta, transcript)

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            raw = call_claude(prompt, user_msg)
            parsed = extract_json(raw)
            missing = REQUIRED_KEYS - parsed.keys()
            if missing:
                raise ValueError(f"missing required keys in analysis: {missing}")
            (video_dir / "analysis.json").write_text(
                json.dumps(parsed, indent=2, ensure_ascii=False)
            )
            return parsed
        except (json.JSONDecodeError, ValueError, RuntimeError) as e:
            last_err = e
            sys.stderr.write(f"[analyze] attempt {attempt + 1} failed: {e}\n")
            if attempt < max_retries:
                # Reinforce the JSON-only requirement on retry.
                user_msg = (
                    user_msg
                    + "\n\nPREVIOUS ATTEMPT FAILED. Return ONLY a single valid JSON object "
                      "matching the schema, no prose, no markdown fences."
                )
    raise RuntimeError(f"analyze failed after retries: {last_err}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video-dir", type=Path, required=True)
    args = ap.parse_args()
    result = analyze(args.video_dir)
    print(json.dumps({
        "video_dir": str(args.video_dir),
        "hook_type": result["hook"].get("type"),
        "framework": result["structure"].get("framework"),
        "viral_hypothesis": result["viral_hypothesis"],
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
