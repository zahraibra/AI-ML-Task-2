# TrendPilot — Error Analysis

Review at least 5 weak or failed responses from real runs and fill in this
table (examples from the task brief are shown — replace with your actual
findings once you've run the agent).

| Test Case | Problem Found | Possible Reason | Fix Applied |
|-----------|---------------|------------------|-------------|
| AI internship topic | Output was too generic | Prompt was not specific enough | Added tone and audience to prompt |
| Meme caption | Not funny enough | Model did not understand meme style | Added examples in prompt |
| Reel script | Too long | No time limit specified | Added 30–45 second limit to prompt |
| Hashtags | Irrelevant hashtags | Tool prompt was weak | Improved hashtag tool prompt |
| File saving | File not created | Path issue | Fixed output directory handling |

## Suggested Improvements

1. **Better prompts** — add explicit target audience and platform constraints to every prompt template in `prompts.py`.
2. **Add examples to prompts** (few-shot) — especially for humor/meme tone, which small local models struggle with zero-shot.
3. **Add validation checks** — e.g. reject hashtag output that doesn't start with `#`, or captions over a word-count limit, and auto-retry.
4. **Platform-specific rules** — X/Twitter needs a hard character limit (280); LinkedIn tolerates longer posts. Encode this per-platform in `prompts.py`.
5. **Add a user feedback loop** — let the user say "make it funnier" and re-run just the caption tool with an adjusted prompt.
6. **Try a larger local model** — Mistral 7B (if hardware allows) generally follows formatting instructions more reliably than 3B-class models.
