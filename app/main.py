"""
main.py
-------
Programmatic entry point for TrendPilot. Both demo.py (CLI) and
streamlit_app.py (web UI) import `run_agent` from here so there is a
single source of truth for how a request is executed.
"""

from app.agent import TrendPilotAgent
from app.ollama_client import DEFAULT_MODEL


def run_agent(topic: str, platform: str = "LinkedIn", tone: str = "Professional",
              model: str = DEFAULT_MODEL) -> dict:
    """
    Run the full TrendPilot agent workflow for a single request.

    Returns a dict with all generated fields plus 'saved_file', or a
    dict with an 'error' key if Ollama could not be reached.
    """
    agent = TrendPilotAgent(model=model)
    return agent.run(topic=topic, platform=platform, tone=tone)


if __name__ == "__main__":
    # Quick manual smoke test
    output = run_agent(
        topic="I built a YOLOv8 object detection project",
        platform="LinkedIn",
        tone="Professional and exciting",
    )
    if "error" not in output:
        print("Caption:\n", output["caption"])
