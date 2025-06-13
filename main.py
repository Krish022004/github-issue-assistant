# ✅ FINAL main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
import re
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env.example file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=API_KEY
)

app = FastAPI()

class IssueRequest(BaseModel):
    repo_url: str
    issue_number: int

@app.post("/analyze")
async def analyze_issue(data: IssueRequest):
    try:
        parts = data.repo_url.rstrip("/").split("/")
        owner, repo = parts[-2], parts[-1]

        issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{data.issue_number}"
        comments_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{data.issue_number}/comments"

        async with httpx.AsyncClient() as client_http:
            issue_resp = await client_http.get(issue_url)
            issue_resp.raise_for_status()
            issue = issue_resp.json()

            comments_resp = await client_http.get(comments_url)
            comments_resp.raise_for_status()
            comments = comments_resp.json()
            comments_text = " ".join([c['body'] for c in comments])

        prompt = f"""
You are an AI assistant. Analyze the following GitHub issue and output ONLY valid JSON with this EXACT structure:

{{
  "summary": "A one-sentence summary of the user's problem or request.",
  "type": "Classify the issue as: bug, feature_request, documentation, question, or other.",
  "priority_score": "A score from 1 (low) to 5 (critical), with a brief justification in parentheses.",
  "suggested_labels": ["An array of 2-3 relevant GitHub labels."],
  "potential_impact": "A brief sentence if bug; else the STRING 'null'."
}}

Do NOT include any ```json or markdown. Output raw JSON only.

Title: {issue['title']}
Body: {issue['body']}
Comments: {comments_text}
"""

        result = llm.invoke(prompt)
        content = result.content

        clean = re.sub(r"```json|```", "", content).strip()
        parsed = json.loads(clean)

        labels = parsed.get("suggested_labels")
        if isinstance(labels, dict):
            parsed["suggested_labels"] = list(labels.values())

        if isinstance(parsed["suggested_labels"], list) and len(parsed["suggested_labels"]) > 3:
            parsed["suggested_labels"] = parsed["suggested_labels"][:3]

        if parsed.get("type") != "bug":
            parsed["potential_impact"] = "null"
        elif parsed.get("potential_impact") in [None, "", "null"]:
            parsed["potential_impact"] = "null"

        return {"analysis": parsed}

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"GitHub API error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # This code defines a FastAPI application that analyzes GitHub issues using the Google Generative AI model.
# It retrieves issue details and comments, constructs a prompt for the model, and returns a structured JSON response.
# The response includes a summary, issue type, priority score, suggested labels, and potential impact.
# Ensure you have the necessary environment variables set in a .env file:
# GOOGLE_API_KEY=your_google_api_key_here
# Make sure to install the required packages:
# pip install fastapi httpx langchain-google-genai python-dotenv
# To run the FastAPI app, use:
# uvicorn main:app --reload
