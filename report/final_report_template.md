# TrendPilot — A Local Agentic AI Assistant Using Ollama
### Final Report — AIRI Team PITB, AI Internship Task 2

> Fill in the bracketed sections after running the agent locally and
> collecting real outputs, screenshots, and test results.

## 1. Project Overview
I built **TrendPilot**, a local Agentic AI assistant using Ollama and
[model name, e.g. Gemma 3:4B]. The agent helps users generate viral
LinkedIn posts, reel scripts, hashtags, and content ideas from any project
topic. It uses eight tools — trend idea generator, hook generator, caption
writer, hashtag generator, reel script generator, title/thumbnail
generator, content reviewer, and file saver — orchestrated by an explicit
plan-then-act agent loop, going well beyond a simple chatbot response.

## 2. Tools and Technologies Used
Python, Ollama, [Gemma 3:4B / Llama 3.2 / Phi-3 Mini / Qwen — whichever you
used], Streamlit, JSON memory, Markdown file saving, GitHub.

## 3. Agent Workflow
The agent understands the user's topic, platform, and tone, then builds an
explicit plan before acting. It generates content angles, picks the
strongest one, writes a hook and caption, generates hashtags, writes a
reel script, produces a title and thumbnail text, reviews the full
package for quality, and saves the final result as a Markdown + JSON file
— logging every tool call along the way.

## 4. Tools Implemented
- **Trend Idea Generator** — produces 5 distinct content angles for the topic/platform.
- **Hook Generator** — writes a scroll-stopping opening line.
- **Caption Writer** — expands the hook into a full platform-ready caption.
- **Hashtag Generator** — produces 8 relevant hashtags.
- **Reel Script Generator** — writes a structured 30–45s short-video script.
- **Title & Thumbnail Generator** — produces a catchy title and thumbnail text.
- **Content Reviewer** — checks hook strength, clarity, length, tone, and hashtag relevance.
- **File Saver** — saves the final package to disk (mandatory tool).
- **Memory Tool** — stores topic/platform/tone/saved-file across sessions.

## 5. Demo and Outputs
[Describe how your demo runs — CLI or Streamlit — with a real example
input/output and a reference to your saved screenshots, e.g.
`screenshots/demo_output.png`.]

Example saved output: `outputs/generated_posts/[your_file].md`

## 6. Testing
I tested the agent on 10 different topics, covering technical project
posts (YOLOv8, computer vision), career posts (internship experience,
open-source contributions), and different tones (professional, funny,
motivational). [Summarize which categories performed well vs. needed more
prompt tuning — see `tests/test_cases.md` for full results.]

## 7. Error Analysis
[Summarize your findings from `tests/error_analysis.md` — what failed, why,
and what you changed. Example: some outputs were too generic in the first
version; I improved the prompts by adding target audience, tone, and
platform-specific instructions, and added a reviewer tool to check clarity
and relevance.]

## 8. What I Learned
- Learned how to run local LLMs using Ollama.
- Learned the difference between a chatbot and an AI agent.
- Learned how to connect tools with an LLM through structured prompts.
- Learned prompt design for structured, parseable outputs.
- Learned how to save and persist agent results.
- Learned basic memory handling with JSON.
- Learned how to test and iteratively improve an agentic workflow.

## 9. Future Improvements
- Add a web search tool for real-time trend grounding.
- Add a multi-agent workflow (separate planner, writer, and reviewer agents).
- Add voice input / text-to-speech.
- Export output as PDF in addition to Markdown.
- Move memory from JSON to SQLite for larger histories.
- Add a user feedback loop ("make it funnier") that re-runs a single tool.
- Try a larger local model (e.g. Mistral 7B) for more reliable formatting.

## 10. LinkedIn Post

```
Today, I completed AIRI Team PITB - AI Internship Task 2, where I built an
end-to-end Agentic AI assistant using a local LLM through Ollama.

For this task, I developed TrendPilot, an AI agent that takes a user topic
and generates structured outputs such as content ideas, LinkedIn posts,
hashtags, reel scripts, and saved Markdown files.

This project helped me understand how agentic AI systems work beyond
simple chatbot responses. I learned how to design an agent workflow,
connect tools, add memory, save outputs, test different prompts, and
analyze weak responses.

Tools used: Python, Ollama, [Model Name], Streamlit, JSON/Markdown, and
GitHub.

Key learning: Agentic AI is not only about generating text. It is about
planning, using tools, storing useful information, improving outputs, and
completing tasks in a structured way.

#AgenticAI #Ollama #LocalLLM #Gemma #Python #ArtificialIntelligence #AIRI
#PITB #AIInternship #MachineLearning #GenerativeAI
```
