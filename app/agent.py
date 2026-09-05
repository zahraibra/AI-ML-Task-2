"""
agent.py
--------
The TrendPilot agent. This is what makes the project "agentic" rather
than a plain chatbot: it understands a goal, builds an explicit plan,
decides which tools to call and in what order, reviews its own output,
stores memory, and saves the final result — matching the workflow in
Section 5 and Section 13 of the task brief.
"""

from app import tools, memory
from app.ollama_client import OllamaError, DEFAULT_MODEL


class TrendPilotAgent:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    # -----------------------------------------------------------------
    def build_plan(self, topic: str, platform: str, tone: str) -> list:
        """Step 2 of the workflow: the agent creates an explicit plan."""
        plan = [
            "Understand the topic and goal",
            "Recall relevant memory from past sessions",
            "Generate content angles (Trend Idea Generator)",
            "Select the strongest angle",
            "Write a scroll-stopping hook",
            "Write the platform caption (Caption Writer)",
            "Generate hashtags (Hashtag Generator)",
            "Generate a reel/short-video script (Reel Script Generator)",
            "Generate a title and thumbnail text",
            "Review the full content package (Content Reviewer)",
            "Save the final result to a file (File Saver)",
            "Store this session in memory",
        ]
        return plan

    # -----------------------------------------------------------------
    def run(self, topic: str, platform: str, tone: str) -> dict:
        """
        Executes the full agentic workflow end-to-end and returns the
        final structured result (also saved to disk).
        """
        print(f"\n=== TrendPilot Agent starting run ===")
        print(f"Goal: create a {platform} content plan about '{topic}' ({tone} tone)\n")

        plan = self.build_plan(topic, platform, tone)
        print("[Agent Plan]")
        for i, step in enumerate(plan, 1):
            print(f"  {i}. {step}")
        print()

        try:
            # Step: recall memory (gives the agent light awareness of history)
            print("[Memory] Recalling recent sessions...")
            recent_context = memory.get_recent_context()
            print(recent_context, "\n")

            # Step: generate angles, pick the first (best-ranked) one
            ideas = tools.trend_idea_generator(topic, platform, tone, self.model)
            chosen_angle = ideas[0] if ideas else topic

            # Step: hook -> caption
            hook = tools.hook_generator(topic, platform, tone, chosen_angle, self.model)
            caption = tools.caption_writer(topic, platform, tone, hook, self.model)

            # Step: hashtags
            hashtags = tools.hashtag_generator(topic, platform, self.model)

            # Step: reel script
            reel_script = tools.reel_script_generator(topic, tone, self.model)

            # Step: title & thumbnail
            title_data = tools.title_thumbnail_generator(topic, self.model)

            # Step: self-review (agent "reviews its own output")
            review = tools.content_reviewer(platform, caption, hashtags, reel_script, self.model)

            result = {
                "topic": topic,
                "platform": platform,
                "tone": tone,
                "content_idea": chosen_angle,
                "all_ideas": ideas,
                "hook": hook,
                "caption": caption,
                "hashtags": hashtags,
                "reel_script": reel_script,
                "title": title_data["title"],
                "thumbnail_text": title_data["thumbnail_text"],
                "review": review,
            }

            # Step: save to file (mandatory tool)
            saved_path = tools.file_saver(result, topic)
            result["saved_file"] = saved_path

            # Step: store in memory
            memory.save_memory_entry(topic, platform, tone, saved_path)

            print(f"\n[Agent] Done. Final result saved to: {saved_path}\n")
            return result

        except OllamaError as exc:
            print(f"\n[Agent Error] {exc}\n")
            return {"error": str(exc)}
