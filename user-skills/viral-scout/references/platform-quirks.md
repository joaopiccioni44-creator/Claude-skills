# Platform Quirks

## YouTube
- Default Data API v3 quota: 10,000 units/day.
- `search.list` costs **100 units** per call; `videos.list` costs **1 unit** per call (batches of up to 50 IDs).
- Discovery for one theme typically uses ~150 units.
- `viewCount` returned as a string — cast to int.
- Shorts use the same video IDs as standard videos; URL prefix is `/shorts/<id>` but `/watch?v=<id>` works too.
- Native transcripts via `youtube-transcript-api` Python package; not always available (creator can disable).
- Region bias: API returns globally; use `regionCode=BR` + `relevanceLanguage=pt` for Brazilian-Portuguese themes.

## Kwai
- No official public API.
- Firecrawl scrape of `kwai.com/@user` and hashtag pages works; views often shown as "1.2M" → must parse to int.
- Sometimes view counts are absent on hashtag-page tiles — fallback: scrape the video page itself.
- All metric parsing should accept `K`, `M`, `Mil`, `Mi`, `B` suffixes (PT-BR variants).

## TikTok (free)
- Anti-bot is aggressive; Firecrawl works on ~40-60% of hashtag/discover pages.
- Always mark `source_quality: "degraded"`.
- View counts on tiles are often abbreviated and rounded.
- No reliable transcript without downloading + whisper.

## TikTok (Apify)
- Recommended actor: `clockworks/tiktok-scraper`.
- Requires `APIFY_API_TOKEN`; ~$0.001-0.01 per video result depending on plan.
- Returns full metrics + transcript not included (still need whisper).

## Instagram (free)
- Same caveats as TikTok free-tier; arguably worse.
- Hashtag pages now require login most of the time.
- When scrape returns 0, log to manifest and move on — do not retry aggressively.

## Instagram (Apify)
- Recommended actor: `apify/instagram-scraper`.
- Reels endpoint returns plays/likes/comments reliably.

## yt-dlp
- Works for all four platforms.
- TikTok: use `--cookies-from-browser firefox` if rate-limited.
- For audio-only extraction (whisper): `-x --audio-format wav --postprocessor-args "-ar 16000 -ac 1"`.
- Use `--no-warnings --no-progress` for clean JSON output in scripts.

## whisper.cpp
- `whisper-cli` (homebrew binary; legacy alias `whisper-cpp`).
- Requires 16kHz mono WAV.
- Model `ggml-large-v3.bin` ~3GB.
- Apple Silicon Metal: ~0.3x realtime for large-v3 (3 min video ≈ 1 min transcription).
- Auto-detects language; can force with `-l pt`.

## Claude CLI
- `claude -p "<prompt>" --output-format json` returns a JSON envelope with the actual response inside `.result`.
- For long inputs, pipe via stdin: `cat transcript.txt | claude -p "..." --output-format json`.
- The skill `metodo-falar`, `linkedin-hooks`, `smart-brevity` are auto-loaded based on prompt content — write the prompt so it mentions hook decomposition + narrative structure.
