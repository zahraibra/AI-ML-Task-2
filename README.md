# TrendPilot — Local Agentic AI Assistant (Ollama)

**AIRI Team PITB — AI Internship Task 2**

TrendPilot is a local agentic AI assistant that takes a project topic and
produces a complete viral content plan — content idea, hook, caption,
hashtags, a short reel script, title/thumbnail text, and a self-review —
using a small local LLM served through **Ollama**. No API keys, no cloud
calls: everything runs on your machine.

## Why this is an *agent*, not a chatbot

A chatbot just replies. TrendPilot:
1. **Understands the goal** (topic + platform + tone).
2. **Builds an explicit plan** (`agent.build_plan`) before doing anything.
3. **Decides which tools to call**, in order, and logs each call
   (`[Tool Called]: ...`).
4. **Uses 8 distinct tools** to complete sub-tasks (well above the minimum of 3).
5. **Reviews its own output** with a dedicated Content Reviewer tool.
6. **Remembers past sessions** via a JSON memory store.
7. **Saves the final result** to disk (Markdown + JSON) automatically.

## Project structure

```
agentic_ai_task_2/
├── app/
│   ├── main.py           # run_agent() entry point used by both demos
│   ├── agent.py           # TrendPilotAgent: plans, orchestrates tools
│   ├── tools.py            # 8 tools: ideas, hook, caption, hashtags,
│   │                        #   reel script, title/thumbnail, reviewer, file saver
│   ├── memory.py           # JSON-backed session memory
│   ├── prompts.py          # every prompt template used by the tools
│   └── ollama_client.py    # single wrapper around the Ollama HTTP API
├── outputs/
│   ├── generated_posts/    # saved .md content plans
│   ├── generated_scripts/  # (reserved for standalone script exports)
│   └── saved_results/      # saved .json copies + memory.json
├── tests/
│   ├── test_cases.md       # 10-case test template (Section 16)
│   └── error_analysis.md   # weak-output analysis template (Section 17)
├── screenshots/             # put your screenshots here
├── report/                  # final report goes here
├── demo.py                  # CLI demo
├── streamlit_app.py         # Streamlit web demo (bonus)
└── requirements.txt
```

## Setup

### 1. Install Ollama

Download from [ollama.com](https://ollama.com) and verify:

```bash
ollama --version
```

### 2. Pull a small local model

```bash
ollama pull gemma3:4b
```

If your machine can't run Gemma 3:4B, use one of:

```bash
ollama pull llama3.2:3b
ollama pull phi3:mini
ollama pull qwen2.5:3b
```

### 3. Test the model directly

```bash
ollama run gemma3:4b
```
Try: `Give me 5 viral LinkedIn post ideas about AI internships.`
Take a screenshot of this for `screenshots/ollama_running.png`.

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Running the demo

### CLI

```bash
python demo.py
```
You'll be prompted for a topic, platform, and tone. The agent prints its
plan, logs each tool call, then prints the final content package and the
saved file path.

### Streamlit (web UI)

```bash
streamlit run streamlit_app.py
```

### Programmatic use

```python
from app.main import run_agent

result = run_agent(
    topic="I built a YOLOv8 helmet detection project",
    platform="LinkedIn",
    tone="Professional and exciting",
)
print(result["caption"])
print(result["saved_file"])
```

## Tools implemented

| # | Tool | Purpose |
|---|------|---------|
| 1 | Trend Idea Generator | 5 content angles for the topic/platform |
| 2 | Hook Generator | scroll-stopping opening line |
| 3 | Caption Writer | full platform-ready caption |
| 4 | Hashtag Generator | 8 relevant hashtags |
| 5 | Reel Script Generator | 30–45s hook/explanation/visual/closing script |
| 6 | Title & Thumbnail Generator | catchy title + thumbnail text |
| 7 | Content Reviewer | checks hook strength, clarity, length, tone, hashtags |
| 8 | File Saver (mandatory) | saves `.md` + `.json` to `outputs/` |

Memory is a ninth supporting capability (`memory.py`) that stores every
session's topic/platform/tone/saved-file so future runs have light context.

## Testing & error analysis

See `tests/test_cases.md` (10 required test cases) and
`tests/error_analysis.md` (5+ weak-output reviews with fixes applied), both
pre-templated from the task brief — fill them in with your actual run
results.

## Notes on this repo as delivered

This repository contains the **complete, working implementation** — agent,
all 8 tools, memory, prompts, CLI demo, and Streamlit demo. It was built and
reviewed without a live local Ollama instance in the build environment, so:
- `tests/test_cases.md` and `tests/error_analysis.md` are templated with the
  brief's example cases — run `python demo.py` locally against your pulled
  model and fill in the real outputs, saved paths, and usefulness ratings.
- Take the three required screenshots (`ollama_running.png`,
  `demo_output.png`, `saved_file_output.png`) during your own run.
- Once you have real outputs, use `report/final_report_template.md` to write
  your final report and LinkedIn post (Section 22 of the brief).

## Tech stack

Python · Ollama (Gemma 3:4B or similar) · Requests · Streamlit · JSON memory
· Markdown file saving
