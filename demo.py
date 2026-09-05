"""
demo.py
-------
Simple CLI demo for TrendPilot (Demo Option A in the task brief).

Run with:
    python demo.py
"""

from app.main import run_agent
from app.ollama_client import DEFAULT_MODEL


def main():
    print("=" * 60)
    print(" TrendPilot — Local Agentic AI Assistant (Ollama)")
    print("=" * 60)

    topic = input("Enter your topic: ").strip()
    print("Choose platform: [1] LinkedIn  [2] Instagram Reels  [3] X/Twitter "
          "[4] YouTube Shorts  [5] Facebook")
    platform_choice = input("Platform number: ").strip()
    platform_map = {
        "1": "LinkedIn", "2": "Instagram Reels", "3": "X/Twitter",
        "4": "YouTube Shorts", "5": "Facebook",
    }
    platform = platform_map.get(platform_choice, "LinkedIn")

    tone = input("Choose tone (e.g. Professional, Funny, Motivational): ").strip() or "Professional"
    model = input(f"Model to use [{DEFAULT_MODEL}]: ").strip() or DEFAULT_MODEL

    result = run_agent(topic=topic, platform=platform, tone=tone, model=model)

    if "error" in result:
        print("\n Something went wrong:")
        print(result["error"])
        return

    print("\n" + "=" * 60)
    print(" FINAL CONTENT PLAN")
    print("=" * 60)
    print(f"Title: {result['title']}")
    print(f"\nHook:\n{result['hook']}")
    print(f"\nCaption:\n{result['caption']}")
    print(f"\nHashtags:\n{' '.join(result['hashtags'])}")
    print(f"\nReel Script:\n{result['reel_script']}")
    print(f"\nThumbnail Text: {result['thumbnail_text']}")
    print(f"\nReview:\n{result['review']}")
    print(f"\nSaved to: {result['saved_file']}")


if __name__ == "__main__":
    main()
