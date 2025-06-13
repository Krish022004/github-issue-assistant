"""
Streamlit frontend for Seedling Labs Craft Case.
Calls FastAPI backend and displays result.
"""

import streamlit as st
import requests
import json
import streamlit.components.v1 as components

st.set_page_config(page_title="GitHub Issue Assistant")

st.title("🧑‍💻 AI-Powered GitHub Issue Assistant")

repo_url = st.text_input("Repository URL", placeholder="https://github.com/facebook/react")
issue_number = st.number_input("Issue Number", min_value=1, step=1)

if st.button("Analyze Issue"):
    with st.spinner("Analyzing..."):
        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"repo_url": repo_url, "issue_number": issue_number}
        )
        if response.status_code == 200:
            result = response.json()["analysis"]
            json_str = json.dumps(result, indent=2)

            st.json(result)

            components.html(
                f"""
                <textarea id="json-output" style="width: 100%; height: 300px;">{json_str}</textarea><br>
                <button onclick="navigator.clipboard.writeText(document.getElementById('json-output').value); alert('Copied to clipboard!');">📋 Copy JSON</button>
                """,
                height=350,
            )

        else:
            st.error(f"Error: {response.status_code} - {response.text}")

        # Display success message
        st.success("Analysis completed successfully!")
# This code is a simple Streamlit app that interacts with the FastAPI backend to analyze GitHub issues.
#         if "suggested_labels" in parsed and isinstance(parsed["suggested_labels"], str):
#             parsed["suggested_labels"] = [parsed["suggested_labels"]]
#
#         if "potential_impact" not in parsed:      
#             parsed["potential_impact"] = "null"
#         return parsed     
#     except Exception as e:
#         st.error(f"Error: {e}")           
#         st.error("Failed to analyze the issue. Please check the repository URL and issue number.")
# This app allows users to input a GitHub repository URL and an issue number, then sends a request to the FastAPI backend to analyze the issue.
# The response is displayed in a formatted JSON output with a copy button.
# Note: Ensure the FastAPI backend is running at http://localhost:8000/analyze for this to work.
# This code is a simple Streamlit app that interacts with the FastAPI backend to analyze GitHub issues.
# This app allows users to input a GitHub repository URL and an issue number, then sends a request to the FastAPI backend to analyze the issue.
# The response is displayed in a formatted JSON output with a copy button.
# Note: Ensure the FastAPI backend is running at http://localhost:8000/analyze for this to work.
