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

# === ✅ Action Button with animation ===
if st.button("🚀 Analyze Issues"):
    progress = st.progress(0, text="Preparing analysis...")

    # Simulate animation steps
    for pct in range(1, 80, 10):
        time.sleep(0.1)
        progress.progress(pct, text=f"🔍 Processing... {pct}%")

    payload = {
        "repo_url": repo_url,
        "issue_numbers": issue_numbers
    }
    response = requests.post("https://YOUR-FASTAPI-URL.onrender.com/analyze", json=payload)


    progress.progress(100, text="✨ Finalizing...")

    if response.status_code == 200:
        data = response.json()
        st.success(f"✅ Analysis done in {data['analysis_time_sec']} seconds!")
        st.toast("🎉 Done! JSON ready to copy or download.")

        results = data["results"]

        for item in results:
            with st.expander(f"📂 Issue #{item['issue_number']} Details"):
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

# === ✅ Footer ===
st.markdown("---")
st.caption("Built by G Krishna Teja | Source code: [GitHub](https://github.com/Krish022004/github-issue-assistant) | Powered by Streamlit and AI")
