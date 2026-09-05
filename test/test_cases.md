# TrendPilot — Test Cases

Run each row through `python demo.py` (or the Streamlit app) with the given
topic/platform/tone, then fill in **Tools Used**, **Saved File Path**, and
**Useful? (Y/N)** from the actual run. This file is a template — 10 rows are
pre-filled from the task brief's example set; replace the last three columns
with your real results.

| # | Topic | Platform | Tone | Expected Output | Tools Used | Saved File Path | Useful? |
|---|-------|----------|------|------------------|------------|------------------|---------|
| 1 | YOLOv8 helmet detection | LinkedIn | Professional | Post + hashtags | | | |
| 2 | AI internship experience | LinkedIn | Motivational | Post | | | |
| 3 | Python learning journey | Instagram Reels | Funny | Reel script | | | |
| 4 | Machine learning project | X/Twitter | Short and catchy | Short post | | | |
| 5 | Data annotation struggles | LinkedIn | Humorous | Post | | | |
| 6 | Model failed in production | Instagram Reels | Meme style | Reel script | | | |
| 7 | Final year project | LinkedIn | Professional | Portfolio post | | | |
| 8 | Computer vision project | YouTube Shorts | Exciting | Video script | | | |
| 9 | Debugging FastAPI | X/Twitter | Funny | Short post | | | |
| 10 | Open-source contribution | LinkedIn | Inspirational | Post | | | |

## How to record a result

For each test, capture:
1. The exact input prompt/topic used.
2. Which tools the agent logged as `[Tool Called]: ...`.
3. The final output (paste the generated caption/hook, or link to the saved `.md` file).
4. The saved file path printed by the agent.
5. Whether the result was actually usable (Y/N) and a one-line reason why/why not.

Paste screenshots of each run into `/screenshots/demo_output.png` (or numbered
variants) as required by Section 20 of the task brief.
