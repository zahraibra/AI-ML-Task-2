"""
streamlit_app.py
-----------------
Streamlit web demo for TrendPilot (Demo Option B in the task brief).

Run with:
    streamlit run streamlit_app.py
"""

import streamlit as st
from app.main import run_agent
from app.ollama_client import DEFAULT_MODEL
from app import memory

st.set_page_config(page_title="TrendPilot", page_icon="🚀", layout="centered")

st.title("🚀 TrendPilot")
st.caption("Local Agentic AI assistant for viral content ideas — powered by Ollama")

with st.form("content_form"):
    topic = st.text_input("Topic", placeholder="e.g. My YOLOv8 helmet detection project")
    platform = st.selectbox(
        "Platform",
        ["LinkedIn", "Instagram Reels", "TikTok", "YouTube Shorts", "X/Twitter", "Facebook"],
    )
    tone = st.selectbox(
        "Tone",
        ["Professional", "Funny", "Motivational", "Casual", "Exciting", "Humorous"],
    )
    model = st.text_input("Ollama model", value=DEFAULT_MODEL)
    submitted = st.form_submit_button("Generate ✨")

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Agent is planning, calling tools, and reviewing output..."):
            result = run_agent(topic=topic, platform=platform, tone=tone, model=model)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Saved to `{result['saved_file']}`")

            st.subheader(result["title"])
            st.markdown(f"**Hook:** {result['hook']}")

            st.markdown("### Caption")
            st.write(result["caption"])

            st.markdown("### Hashtags")
            st.write(" ".join(result["hashtags"]))

            st.markdown("### Reel Script")
            st.text(result["reel_script"])

            st.markdown("### Thumbnail Text")
            st.write(result["thumbnail_text"])

            st.markdown("### Agent Review")
            st.info(result["review"])

            with open(result["saved_file"], "rb") as f:
                st.download_button("⬇️ Download result (.md)", f, file_name=result["saved_file"].split("/")[-1])

st.divider()
st.subheader("🧠 Memory — recent sessions")
entries = memory.load_memory()
if entries:
    for e in reversed(entries[-5:]):
        st.write(f"**{e['topic']}** — {e['platform']} / {e['tone']} — `{e['saved_file']}`")
else:
    st.write("No sessions yet.")
