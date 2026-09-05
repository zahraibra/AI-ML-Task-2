"""
tools.py
--------
The agent's tools. Each function is a standalone, callable "tool" the
agent can invoke. This satisfies the "at least three tools" requirement
several times over (8 tools implemented here, matching Section 6 of
the brief).

Every tool prints a [Tool Called] log line so the agent's tool-use is
visible during a run, as required in Section 13, Step 3.
"""

import os
import json
from datetime import datetime

from app.ollama_client import ask_ollama
from app import prompts

OUTPUT_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs"
)


def _log(tool_name: str):
    print(f"[Tool Called]: {tool_name}")


# ---------------------------------------------------------------------
# Tool 1: Trend Idea Generator
# ---------------------------------------------------------------------
def trend_idea_generator(topic: str, platform: str, tone: str, model: str) -> list:
    _log("Trend Idea Generator")
    prompt = prompts.TREND_IDEA_PROMPT.format(topic=topic, platform=platform, tone=tone)
    raw = ask_ollama(prompt, model=model)
    ideas = [line.strip(" .") for line in raw.split("\n") if line.strip()]
    # keep only lines that look like "1. ..." etc, fall back to raw split
    cleaned = []
    for line in ideas:
        stripped = line.lstrip("0123456789. )")
        if stripped:
            cleaned.append(stripped)
    return cleaned[:5] if cleaned else [raw]


# ---------------------------------------------------------------------
# Hook generator (feeds into caption writer)
# ---------------------------------------------------------------------
def hook_generator(topic: str, platform: str, tone: str, angle: str, model: str) -> str:
    _log("Hook Generator")
    prompt = prompts.HOOK_PROMPT.format(topic=topic, platform=platform, tone=tone, angle=angle)
    return ask_ollama(prompt, model=model)


# ---------------------------------------------------------------------
# Tool 3: Caption Writer
# ---------------------------------------------------------------------
def caption_writer(topic: str, platform: str, tone: str, hook: str, model: str) -> str:
    _log("Caption Writer")
    prompt = prompts.CAPTION_PROMPT.format(topic=topic, platform=platform, tone=tone, hook=hook)
    return ask_ollama(prompt, model=model)


# ---------------------------------------------------------------------
# Tool 2: Hashtag Generator
# ---------------------------------------------------------------------
def hashtag_generator(topic: str, platform: str, model: str) -> list:
    _log("Hashtag Generator")
    prompt = prompts.HASHTAG_PROMPT.format(topic=topic, platform=platform)
    raw = ask_ollama(prompt, model=model)
    tags = [t for t in raw.split() if t.startswith("#")]
    return tags if tags else raw.split()


# ---------------------------------------------------------------------
# Tool 4: Reel Script Generator
# ---------------------------------------------------------------------
def reel_script_generator(topic: str, tone: str, model: str) -> str:
    _log("Reel Script Generator")
    prompt = prompts.REEL_SCRIPT_PROMPT.format(topic=topic, tone=tone)
    return ask_ollama(prompt, model=model)


# ---------------------------------------------------------------------
# Tool 5: Title and Thumbnail Text Generator
# ---------------------------------------------------------------------
def title_thumbnail_generator(topic: str, model: str) -> dict:
    _log("Title and Thumbnail Text Generator")
    prompt = prompts.TITLE_THUMBNAIL_PROMPT.format(topic=topic)
    raw = ask_ollama(prompt, model=model)
    title, thumb = "", ""
    for line in raw.split("\n"):
        if line.lower().startswith("title:"):
            title = line.split(":", 1)[1].strip()
        elif line.lower().startswith("thumbnail text:"):
            thumb = line.split(":", 1)[1].strip()
    return {"title": title or raw, "thumbnail_text": thumb}


# ---------------------------------------------------------------------
# Tool 7: Content Reviewer Tool
# ---------------------------------------------------------------------
def content_reviewer(platform: str, caption: str, hashtags: list, reel_script: str, model: str) -> str:
    _log("Content Reviewer")
    prompt = prompts.REVIEWER_PROMPT.format(
        platform=platform,
        caption=caption,
        hashtags=" ".join(hashtags),
        reel_script=reel_script,
    )
    return ask_ollama(prompt, model=model)


# ---------------------------------------------------------------------
# Tool 6: File Saver Tool (mandatory)
# ---------------------------------------------------------------------
def file_saver(result: dict, topic: str) -> str:
    """
    Saves the final content package to a Markdown file under
    outputs/generated_posts/ and returns the file path.
    """
    _log("File Saver")
    os.makedirs(os.path.join(OUTPUT_ROOT, "generated_posts"), exist_ok=True)

    slug = "".join(c if c.isalnum() else "_" for c in topic.lower())[:40].strip("_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{slug}_{timestamp}.md"
    filepath = os.path.join(OUTPUT_ROOT, "generated_posts", filename)

    md = f"""# {result.get('title', topic)}

**Topic:** {result['topic']}
**Platform:** {result['platform']}
**Tone:** {result['tone']}

## Content Idea
{result['content_idea']}

## Hook
{result['hook']}

## Caption
{result['caption']}

## Hashtags
{' '.join(result['hashtags'])}

## Reel Script
{result['reel_script']}

## Thumbnail Text
{result.get('thumbnail_text', '')}

## Review
{result['review']}

---
*Generated by TrendPilot on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)

    # Also drop a machine-readable JSON copy in saved_results/
    os.makedirs(os.path.join(OUTPUT_ROOT, "saved_results"), exist_ok=True)
    json_path = os.path.join(OUTPUT_ROOT, "saved_results", f"{slug}_{timestamp}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    return filepath
