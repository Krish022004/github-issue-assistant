"""
Modern Streamlit frontend with animations & styling.
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
col1, col2 = st.columns([8, 1], gap="small")
with col2:
    dark_mode = st.toggle("🌙 Dark Mode")

# === ✅ Strong dark mode styling ===
if dark_mode:
    st.markdown("""
    <style>
    html, body, .main, .stApp { background-color: #0e1117 !important; color: #c9d1d9 !important; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; }
    input, textarea { background-color: #161b22 !important; color: #c9d1d9 !important; }
    .stButton>button, .stDownloadButton>button {
        background-color: #21262d !important; color: #c9d1d9 !important; border: 1px solid #30363d;
        transition: 0.3s; 
    }
    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #30363d !important; transform: scale(1.02);
    }
    .stCodeBlock, pre, code { background-color: #161b22 !important; color: #c9d1d9 !important; }
    .card {
        background-color: #21262d !important;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# === ✅ Fancy title with animation ===
st.markdown(
    "<h1 style='text-align: center;'>✨ <span style='color:#f63366;'>AI-Powered GitHub Issue Assistant</span> ✨</h1>",
    unsafe_allow_html=True
)
st.caption("Analyze & summarize GitHub issues instantly with animations & style.")

st.markdown("---")

# === ✅ Stylish Input Card ===
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔗 Repository Details")
    st.write("Enter a public GitHub repository and an issue number:")
    repo_url = st.text_input(
        "Repository URL",
        value="https://github.com/facebook/react"
    )
    issue_number = st.number_input(
        "Issue Number",
        min_value=1,
        step=1,
        value=1
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# === ✅ Action Button with animation ===
if st.button("🚀 Analyze Issue"):
    progress = st.progress(0, text="Preparing analysis...")

    for pct in range(1, 80, 10):
        time.sleep(0.1)
        progress.progress(pct, text=f"🔍 Processing... {pct}%")

    payload = {
        "repo_url": repo_url,
        "issue_number": issue_number  # ✅ single number
    }

    # ✅ CORRECT backend URL:
    BACKEND_URL = "https://github-issue-assistant.onrender.com/analyze"

    response = requests.post(BACKEND_URL, json=payload)

    progress.progress(100, text="✨ Finalizing...")

    if response.status_code == 200:
        result = response.json()["analysis"]

        st.success(f"✅ Analysis complete!")
        st.toast("🎉 Done! JSON ready to copy or download.")

        st.json(result)
        st.code(json.dumps(result, indent=2), language="json")

        st.download_button(
            "⬇️ Download JSON",
            data=json.dumps(result, indent=2),
            file_name=f"issue_{issue_number}_analysis.json",
            mime="application/json"
        )

    else:
        st.error(f"❌ Error: {response.status_code} - {response.text}")

# === ✅ Footer ===
st.markdown("---")
st.caption("Built by G Krishna Teja | [GitHub Repo](https://github.com/Krish022004/github-issue-assistant) | Powered by Streamlit & FastAPI")
