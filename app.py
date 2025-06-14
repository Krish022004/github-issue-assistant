"""
✅ Modern Streamlit frontend for GitHub Issue Assistant.
Calls FastAPI backend deployed on Render.
"""

import streamlit as st
import requests
import json
import time

# === ✅ Page config ===
st.set_page_config(
    page_title="🐙 GitHub Issue Assistant",
    page_icon="🐙",
    layout="wide"
)

# === ✅ Top-right dark mode toggle ===
col1, col2 = st.columns([8, 1])
with col2:
    dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
    <style>
    html, body, .main, .stApp {
        background-color: #0e1117 !important;
        color: #c9d1d9 !important;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
    }
    input, textarea {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
    }
    .stButton>button, .stDownloadButton>button {
        background-color: #21262d !important;
        color: #c9d1d9 !important;
        border: 1px solid #30363d;
        transition: 0.3s;
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #30363d !important;
        transform: scale(1.02);
    }
    .card {
        background-color: #21262d !important;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# === ✅ Fancy title ===
st.markdown(
    "<h1 style='text-align: center;'>✨ <span style='color:#f63366;'>AI-Powered GitHub Issue Assistant</span> ✨</h1>",
    unsafe_allow_html=True
)
st.caption("Analyze & summarize multiple GitHub issues with style & animations.")

st.markdown("---")

# === ✅ Stylish Input Card ===
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔗 Repository Details")
    st.write("Enter a public GitHub repository and issue numbers (comma-separated):")
    repo_url = st.text_input(
        "Repository URL",
        value="https://github.com/facebook/react"
    )
    issue_numbers = st.text_input(
        "Issue Number(s)",
        value="1",
        help="E.g., 1, 2, 3"
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# === ✅ Analyze Button ===
# ✅ Check inputs first
if st.button("🚀 Analyze Issues"):
    if not repo_url.strip() or not issue_numbers.strip():
        st.warning("⚠️ Please enter both the repository URL and at least one issue number.")
        st.stop()

    progress = st.progress(0, text="Preparing analysis...")

    for pct in range(1, 80, 10):
        time.sleep(0.05)
        progress.progress(pct, text=f"🔍 Processing... {pct}%")

    payload = {
        "repo_url": repo_url,
        "issue_numbers": issue_numbers
    }

    backend_url = "https://github-issue-assistant.onrender.com/analyze"

    response = requests.post(backend_url, json=payload)

    progress.progress(100, text="✨ Finalizing...")

    if response.status_code == 200:
        data = response.json()
        st.success(f"✅ Done in {data['analysis_time_sec']} seconds!")
        st.toast("🎉 Analysis ready!")

        results = data["results"]

        for item in results:
            with st.expander(f"📂 Issue #{item['issue_number']}"):
                if "result" in item:
                    st.json(item["result"])
                    st.code(json.dumps(item["result"], indent=2), language="json")
                else:
                    st.error(f"⚠️ {item['error']}")

        st.download_button(
            "⬇️ Download All Results",
            data=json.dumps(results, indent=2),
            file_name="analysis_results.json",
            mime="application/json"
        )

    else:
        st.error(f"❌ Error: {response.status_code} - {response.text}")
        if response.status_code in [403, 404, 502]:
            st.info("👉 Ensure your FastAPI backend is deployed and awake on Render.")
        elif response.status_code == 500:
            st.error("⚠️ Internal server error. Please check your backend logs for details.")
        else:
            st.error("⚠️ Unexpected error. Please try again later or contact support.")


# === ✅ Footer ===
st.markdown("---")
st.caption("Built by G Krishna Teja | [GitHub Source](https://github.com/Krish022004/github-issue-assistant) | Powered by Streamlit + FastAPI + Gemini AI")
