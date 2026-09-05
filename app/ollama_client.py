"""
ollama_client.py
-----------------
Thin wrapper around the local Ollama HTTP API.

Every tool and the agent itself calls the LLM through the single
`ask_ollama()` function defined here, so the model name, timeout,
and error handling only need to live in one place.
"""

import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma3:4b"   # fallback: llama3.2:3b, phi3:mini, qwen2.5:3b


class OllamaError(Exception):
    """Raised when the local Ollama server can't be reached or errors out."""
    pass


def ask_ollama(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.7) -> str:
    """
    Send a prompt to the local Ollama model and return the raw text response.

    Parameters
    ----------
    prompt : str
        The full prompt text to send to the model.
    model : str
        Ollama model tag, e.g. "gemma3:4b", "llama3.2:3b", "phi3:mini".
    temperature : float
        Sampling temperature passed through Ollama's `options`.

    Returns
    -------
    str
        The model's text response.

    Raises
    ------
    OllamaError
        If Ollama is not running or the request fails.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
    except requests.exceptions.ConnectionError as exc:
        raise OllamaError(
            "Could not connect to Ollama at http://localhost:11434. "
            "Make sure Ollama is installed and running (`ollama serve`), "
            f"and that you've pulled a model (`ollama pull {model}`)."
        ) from exc
    except requests.exceptions.RequestException as exc:
        raise OllamaError(f"Ollama request failed: {exc}") from exc

    try:
        data = response.json()
        return data["response"].strip()
    except (json.JSONDecodeError, KeyError) as exc:
        raise OllamaError(f"Unexpected response format from Ollama: {exc}") from exc


def ask_ollama_json(prompt: str, model: str = DEFAULT_MODEL) -> dict:
    """
    Ask Ollama for a response and parse it as JSON.
    Useful for tools that need structured output (e.g. hashtag lists).
    Strips markdown code fences if the model wraps its JSON in them.
    """
    raw = ask_ollama(prompt, model=model, temperature=0.4)
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json\n", "", 1).replace("json", "", 1)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        # Fall back: return raw text under a single key so callers don't crash
        return {"raw_text": raw}
