"""
memory.py
---------
Simple Memory Tool (Tool 8 in the brief).

Stores previous topics, platforms, tones, and a pointer to the saved
output file, in a local JSON file. This gives the agent basic
conversation/history memory without needing a database.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "outputs", "saved_results", "memory.json"
)


def _ensure_file():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def load_memory() -> list:
    """Return the full list of past memory entries (most recent last)."""
    _ensure_file()
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_memory_entry(topic: str, platform: str, tone: str, saved_file: str) -> dict:
    """
    Append a new entry to memory and persist it.

    Returns the entry that was saved.
    """
    entries = load_memory()
    entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "topic": topic,
        "platform": platform,
        "tone": tone,
        "saved_file": saved_file,
    }
    entries.append(entry)
    _ensure_file()
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
    return entry


def get_recent_context(n: int = 3) -> str:
    """
    Return a short human-readable summary of the last n memory entries,
    used to give the agent light awareness of prior sessions.
    """
    entries = load_memory()[-n:]
    if not entries:
        return "No previous sessions recorded yet."
    lines = []
    for e in entries:
        lines.append(
            f"- Previous topic: {e['topic']} | Platform: {e['platform']} | "
            f"Tone: {e['tone']} | Saved to: {e['saved_file']}"
        )
    return "\n".join(lines)
