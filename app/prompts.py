"""
prompts.py
----------
All prompt templates in one place. Keeping prompts separate from
tool logic makes it easy to tune wording during the error-analysis
phase (Section 17 of the task brief) without touching tools.py.
"""

TREND_IDEA_PROMPT = """You are a viral content strategist.

Topic: {topic}
Platform: {platform}
Tone: {tone}

Generate 5 distinct, specific content angles for a {platform} post about this topic.
Each angle should be one punchy sentence. Avoid generic advice like "share your journey".
Number them 1-5. Output ONLY the numbered list, nothing else.
"""

HOOK_PROMPT = """You are a copywriter specializing in scroll-stopping hooks.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Chosen content angle: {angle}

Write ONE strong opening hook (1-2 sentences) for a {platform} post on this angle.
The hook must create curiosity or tension in the first 8 words.
Output ONLY the hook text, nothing else.
"""

CAPTION_PROMPT = """You are a professional social media copywriter.

Topic: {topic}
Platform: {platform}
Tone: {tone}
Hook to build on: {hook}

Write a complete {platform} post caption (120-220 words) that:
- Opens with the given hook (you may lightly adapt it)
- Explains the project/topic clearly for a non-expert audience
- Includes a concrete detail or number if the topic implies one
- Ends with a soft call-to-action (question or invitation to comment)
Output ONLY the caption text, no markdown headers.
"""

HASHTAG_PROMPT = """Generate 8 relevant hashtags for a {platform} post about: {topic}

Rules:
- Mix broad hashtags (e.g. #AI, #MachineLearning) with specific ones related to the topic
- No spaces inside hashtags
- Output ONLY the hashtags separated by single spaces, nothing else
"""

REEL_SCRIPT_PROMPT = """You are a short-form video scriptwriter.

Topic: {topic}
Tone: {tone}

Write a 30-45 second vertical video script (Reels/TikTok/Shorts style) with exactly these
four labeled parts:
Opening Hook:
Main Explanation:
Visual Suggestion:
Closing Line:

Keep total spoken content under 100 words. Output in that exact labeled format.
"""

TITLE_THUMBNAIL_PROMPT = """Topic: {topic}

Generate:
1. A catchy video/post title (under 10 words)
2. Short thumbnail text (under 5 words, all caps style)

Output in exactly this format:
Title: <title>
Thumbnail Text: <text>
"""

REVIEWER_PROMPT = """You are a strict social media content reviewer.

Review the following {platform} content package and answer each question briefly:

CAPTION:
{caption}

HASHTAGS:
{hashtags}

REEL SCRIPT:
{reel_script}

Answer these in a short bullet list:
- Is the hook strong? (yes/no + why)
- Is the content clear? (yes/no + why)
- Is the post too long? (yes/no)
- Is the tone suitable for {platform}? (yes/no)
- Are hashtags relevant? (yes/no)
- Is it LinkedIn/Platform-ready? (yes/no)
Then give ONE concrete improvement suggestion in a final line starting with "Suggestion:".
"""
