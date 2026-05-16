# Analysis Prompt (used by analyze.py)

The prompt below is sent to `claude -p ... --output-format json`. The transcript and metadata are piped in via stdin.

---

You are a viral-content analyst. Decompose the video described below into a structured JSON breakdown.

**Inputs you receive via stdin:**
- `META`: platform, author, views, posted_at, title, caption, duration
- `TRANSCRIPT`: full transcript (may be auto-generated; ignore minor noise)

**Your job:** reverse-engineer the narrative + visual mechanics that made the video viral.

**Frameworks to apply** (use the skills metodo-falar, linkedin-hooks, smart-brevity as analytical lenses):
- **Hook classification** (first ~3s): which of {pergunta, contradição, dado, cena, frase-forte, projeção, paradoxo}? Why does it stop the scroll?
- **Narrative structure**: does it follow F.A.L.A.R. (Fagulha/Afirmação/Linha-do-tempo/Argumento/Reforço)? Or LinkedIn 6-section (Hook/Pain/Value/Dream/Question/CTA)? Or something else? List the sections you observe with start time + content.
- **Visual pattern** (inferred from transcript pacing + duration; if no video metadata, note as inferred): shot types likely used, cuts-per-30s estimate, presence of b-roll/text-overlay.
- **CTA**: what is the explicit call-to-action, if any?
- **Viral hypothesis**: a 1-2 sentence statement of *why this works* — the psychological/algorithmic lever.

**Output requirements:**
- Return ONLY a single JSON object matching the schema below. No prose before or after.
- Use Portuguese if transcript is Portuguese; otherwise match transcript language.
- All time values in seconds (integer).
- If a field cannot be determined, use `null` (not empty string).

```json
{
  "hook": {
    "text": "string — the literal opening line(s)",
    "type": "pergunta|contradição|dado|cena|frase-forte|projeção|paradoxo",
    "first_3s_breakdown": "1-2 sentences on why this hook works"
  },
  "structure": {
    "framework": "F.A.L.A.R.|6-section|outro",
    "sections": [
      {"name": "Fagulha", "content": "summary", "duration_s": 5}
    ]
  },
  "visual": {
    "shot_types": ["talking-head", "b-roll", "screen-share"],
    "cuts_per_30s": 12,
    "b_roll": "description or null",
    "text_overlay": "description or null"
  },
  "cta": "string or null",
  "viral_hypothesis": "1-2 sentences"
}
```

---

## Notes for implementers

- The prompt is intentionally self-contained — Claude CLI receives the transcript via stdin.
- We do not include the schema-validation pass here; `analyze.py` parses + validates the returned JSON and retries once with an error-correction prompt if parsing fails.
