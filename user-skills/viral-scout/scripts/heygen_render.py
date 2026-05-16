#!/usr/bin/env python3
"""Render HeyGen video clips from a script.json file.

Workflow:
    1. List available voices (filter by language/gender):
        heygen_render.py --list-voices --language Portuguese --gender male

    2. Smoke-test candidate voices on the first section's text:
        heygen_render.py --script recreation/script.json --smoke-test-voices \
            <voice_id_1> <voice_id_2> --out-dir recreation/voice-samples-heygen

    3. Render a single section to validate identity + lip-sync:
        heygen_render.py --script recreation/script.json --section A \
            --out-dir recreation/remotion/public/clips

    4. Render all sections:
        heygen_render.py --script recreation/script.json --all \
            --out-dir recreation/remotion/public/clips

    5. Probe durations and emit a SECTIONS-array snippet for Remotion:
        heygen_render.py --probe-clips recreation/remotion/public/clips

script.json shape:
    {
      "avatar": {"type": "talking_photo", "talking_photo_id": "..."},
      "voice_id": "...",
      "dimension": {"width": 720, "height": 1280},
      "speed": 1.0,
      "sections": [
        {"key": "A", "text": "..."},
        ...
      ]
    }
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import heygen, probe  # noqa: E402


# ---------- Commands ----------

def cmd_list_voices(args) -> int:
    voices = heygen.list_voices()
    filtered = heygen.filter_voices(voices, language=args.language, gender=args.gender)
    print(f"# {len(filtered)} voice(s) (of {len(voices)} total)")
    for v in filtered:
        print(json.dumps({
            "voice_id": v.get("voice_id"),
            "name": v.get("name"),
            "language": v.get("language"),
            "gender": v.get("gender"),
            "preview": v.get("preview_audio"),
        }, ensure_ascii=False))
    return 0


def cmd_list_avatars(args) -> int:
    resp = heygen.list_avatars()
    data = resp.get("data") or {}
    avatars = data.get("avatars") or []
    photos = data.get("talking_photos") or []
    print(f"# {len(avatars)} stock avatar(s), {len(photos)} talking photo(s)")
    for a in avatars:
        print(json.dumps({"type": "avatar",
                          "avatar_id": a.get("avatar_id"),
                          "name": a.get("avatar_name"),
                          "gender": a.get("gender")}, ensure_ascii=False))
    for p in photos:
        print(json.dumps({"type": "talking_photo",
                          "talking_photo_id": p.get("talking_photo_id"),
                          "name": p.get("talking_photo_name")},
                         ensure_ascii=False))
    return 0


def _load_script(path: Path) -> dict:
    if not path.exists():
        sys.exit(f"script not found: {path}")
    return json.loads(path.read_text())


def _character(script: dict) -> dict:
    char = script.get("avatar")
    if not char or "type" not in char:
        sys.exit("script.json must have an `avatar` dict with a `type` field "
                 "(e.g. {'type':'talking_photo','talking_photo_id':'...'})")
    return char


def cmd_smoke_test_voices(args) -> int:
    script = _load_script(args.script)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    char = _character(script)
    sections = script.get("sections") or []
    if not sections:
        sys.exit("script.json has no sections to smoke-test against")
    first = sections[0]
    text = first["text"]
    dim = script.get("dimension") or {"width": 720, "height": 1280}
    speed = float(script.get("speed", 1.0))

    results = []
    for vid in args.smoke_test_voices:
        dest = out_dir / f"sample-{vid}.mp4"
        print(f"[smoke] voice_id={vid} → {dest}")
        try:
            final = heygen.render_to_file(
                character=char, voice_id=vid, input_text=text,
                dest=dest, width=dim["width"], height=dim["height"], speed=speed,
            )
            results.append({"voice_id": vid, "ok": True,
                            "duration": final.get("duration"),
                            "path": str(dest)})
        except Exception as e:
            results.append({"voice_id": vid, "ok": False, "error": str(e)})
            print(f"[smoke] FAILED {vid}: {e}", file=sys.stderr)

    summary = out_dir / "smoke-summary.json"
    summary.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"[smoke] summary → {summary}")
    return 0 if all(r["ok"] for r in results) else 1


def _render_one(script: dict, section: dict, out_dir: Path) -> dict:
    char = _character(script)
    voice_id = script.get("voice_id")
    if not voice_id:
        sys.exit("script.json missing voice_id (run --smoke-test-voices first)")
    dim = script.get("dimension") or {"width": 720, "height": 1280}
    speed = float(script.get("speed", 1.0))
    dest = out_dir / f"{section['key']}.mp4"
    print(f"[render] section={section['key']} → {dest}")
    final = heygen.render_to_file(
        character=char, voice_id=voice_id, input_text=section["text"],
        dest=dest, width=dim["width"], height=dim["height"], speed=speed,
    )
    return {"key": section["key"], "path": str(dest),
            "duration": final.get("duration")}


def cmd_section(args) -> int:
    script = _load_script(args.script)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    match = next((s for s in script.get("sections", []) if s["key"] == args.section), None)
    if not match:
        sys.exit(f"section '{args.section}' not found in {args.script}")
    result = _render_one(script, match, out_dir)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def cmd_all(args) -> int:
    script = _load_script(args.script)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for section in script.get("sections", []):
        try:
            results.append(_render_one(script, section, out_dir))
        except Exception as e:
            results.append({"key": section["key"], "ok": False, "error": str(e)})
            print(f"[render] FAILED {section['key']}: {e}", file=sys.stderr)
    summary = out_dir / "render-summary.json"
    summary.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"[render] summary → {summary}")
    return 0 if all("error" not in r for r in results) else 1


def cmd_probe_clips(args) -> int:
    """Read mp4 durations from a clips dir; emit a SECTIONS array snippet for Remotion."""
    clips_dir = Path(args.probe_clips)
    mp4s = sorted(clips_dir.glob("*.mp4"))
    if not mp4s:
        sys.exit(f"no mp4s in {clips_dir}")
    cursor = 0.0
    lines = ["// pasted from heygen_render.py --probe-clips",
             "const SECTIONS = ["]
    for p in mp4s:
        dur = probe.duration_seconds(p)
        key = p.stem
        lines.append(f"  {{ key: '{key}', clip: '{p.name}', "
                     f"startS: {cursor:.3f}, durS: {dur:.3f} }},")
        cursor += dur
    lines.append("];")
    lines.append(f"// total: {cursor:.3f}s")
    print("\n".join(lines))
    return 0


# ---------- Argparse plumbing ----------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--script", type=Path,
                    help="Path to script.json (sections + avatar + voice)")
    ap.add_argument("--out-dir", default=".",
                    help="Where to write mp4 outputs")

    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--list-voices", action="store_true",
                   help="List voices (filterable with --language/--gender)")
    g.add_argument("--list-avatars", action="store_true",
                   help="List stock avatars + your trained talking photos")
    g.add_argument("--smoke-test-voices", nargs="+", metavar="VOICE_ID",
                   help="Render the first section in each given voice")
    g.add_argument("--section", metavar="KEY",
                   help="Render a single section by its key (A, B, ...)")
    g.add_argument("--all", action="store_true",
                   help="Render every section in the script")
    g.add_argument("--probe-clips", metavar="DIR",
                   help="Probe mp4 durations in DIR; print a SECTIONS array")

    ap.add_argument("--language", help="Filter for --list-voices (e.g. Portuguese)")
    ap.add_argument("--gender", help="Filter for --list-voices (male|female)")

    args = ap.parse_args()

    if args.list_voices:
        return cmd_list_voices(args)
    if args.list_avatars:
        return cmd_list_avatars(args)
    if args.probe_clips:
        return cmd_probe_clips(args)

    if not args.script:
        ap.error("--script is required for --smoke-test-voices / --section / --all")

    if args.smoke_test_voices:
        return cmd_smoke_test_voices(args)
    if args.section:
        return cmd_section(args)
    if args.all:
        return cmd_all(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
