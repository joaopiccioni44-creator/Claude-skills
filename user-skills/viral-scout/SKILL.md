---
name: viral-scout
description: Discovers and decomposes viral videos (>500k views) about a given theme across YouTube, TikTok, Instagram Reels and Kwai, then produces a brief consumable by the avatar pipeline (ugc-video-auto). Use whenever the user wants to find what's working on a topic, reverse-engineer viral hooks, build a swipe file from trending content, or feed a recreation pipeline. Triggers on phrases like "encontra vídeos virais sobre X", "o que está bombando em Y", "achar referências virais", "viral scout", "swipe file de virais", "varrer YouTube e TikTok sobre X", "quero recriar virais de Z". Outputs land in .context/viral-runs/<theme-slug>/<YYYY-MM-DD-HHMM>/.
metadata:
  type: workflow
---

# Viral Scout

Multi-platform viral video discovery + narrative decomposition + brief generation for the existing `ugc-video-auto` avatar pipeline.

## When to invoke

Invoke when the user wants to:
- Discover what's viral on a given theme across YouTube/TikTok/IG/Kwai
- Reverse-engineer viral hooks, structure, visual patterns
- Build a swipe file of references for recreation
- Hand off briefs to `ugc-video-auto` for avatar-based replication

Don't invoke for single-video analysis where the user already has the URL — go directly to `harvest.py` + `analyze.py` of this skill instead of `run_all`.

## Pre-flight (one-time setup)

Before first use, ensure all deps are healthy:

```bash
python3 scripts/doctor.py
```

This validates: `yt-dlp`, `whisper-cli`, `claude` CLI, `~/.config/viral-scout/.env` with `YOUTUBE_API_KEY` and `FIRECRAWL_API_KEY`, and presence of `ggml-large-v3.bin`.

If env file is missing, copy `assets/env.example` to `~/.config/viral-scout/.env` and fill in keys.

## Workflow

### Default (end-to-end)

```bash
python3 scripts/run_all.py --theme "compounding renda fixa" --limit 10 --min-views 500000
```

Output structure under `.context/viral-runs/<slug>/<YYYY-MM-DD-HHMM>/`:
- `manifest.json` — run metadata (theme, params, summary, cost)
- `discovery.raw.json` — raw per-platform results
- `filtered.json` — deduped, schema-unified, filtered by view threshold
- `videos/<platform>-<id>/` — per-video: meta, mp4, thumbnail, transcript, analysis
- `brief.json` — consolidated payload for `ugc-video-auto`

### Granular steps

```bash
# 1. Discovery only
python3 scripts/discover.py --theme "..." --min-views 500000 --limit 20

# 2. Harvest a single video (download + transcript)
python3 scripts/harvest.py --url "https://..." --out-dir <video-dir>

# 3. Analyze a harvested video (narrative breakdown)
python3 scripts/analyze.py --video-dir <video-dir>

# 4. Build brief from analyses
python3 scripts/brief.py --run-dir <run-dir>
```

### Platform selection

By default scans all four platforms. To restrict:

```bash
python3 scripts/discover.py --theme "..." --platforms youtube,kwai
```

### Apify upgrade for TikTok/IG

TikTok and Instagram free-tier scraping is degraded (Firecrawl + anti-bot). To use Apify (full coverage):

```bash
# Set APIFY_API_TOKEN in ~/.config/viral-scout/.env first
python3 scripts/discover.py --theme "..." --use-apify
```

## Architecture

- **scripts/_lib/** — shared config/paths/slug
- **scripts/adapters/** — one per source, all return the unified schema (see `assets/unified-schema.json`)
- **scripts/discover.py** — fans out to adapters, deduplicates, filters by views
- **scripts/harvest.py** — yt-dlp + transcript cascade (YouTube native → whisper.cpp local → OpenAI Whisper API fallback)
- **scripts/analyze.py** — calls `claude -p ... --output-format json` with the analysis prompt
- **scripts/brief.py** — flattens analyses into a payload `ugc-video-auto` understands
- **scripts/run_all.py** — orchestrates the full pipeline

## References (read on demand)

- `references/platform-quirks.md` — gotchas per platform (rate limits, anti-bot, transcript availability)
- `references/analysis-prompt.md` — the full prompt used by `analyze.py`
- `references/brief-schema.md` — schema of the final `brief.json` consumed by `ugc-video-auto`

## Cost & quota

- **YouTube Data API**: ~100 units per `search.list` + 1 per video in `videos.list`. Default quota 10k/day — discovery for 1 theme uses ~150 units.
- **Firecrawl**: ~1 credit per scrape. Hashtag pages on TT/IG/Kwai cost ~5-10 credits per theme.
- **Whisper.cpp local**: zero cost.
- **OpenAI Whisper API**: only on local failure, ~$0.006/min.
- **Claude CLI**: marginal zero (Max subscription).

## When NOT to use

- Single known URL → skip `discover`, run `harvest` + `analyze` directly.
- Long-form content (>15min) → whisper.cpp gets slow; consider truncating or using Whisper API.
- Live streams → not supported by yt-dlp's standard flow here.
