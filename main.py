"""
FastAPI backend for Seedling Labs Craft Case.
Supports bulk GitHub issues, validates each, calls LangChain Gemini,
and returns clean JSON array matching the exact schema.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
import re
import json
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=API_KEY
)

app = FastAPI()

# Request schema
class IssueRequest(BaseModel):
    repo_url: str
    issue_numbers: str  # Comma-separated
@app.get("/")
async def root():
    return {
        "message": "🚀 GitHub Issue Assistant API is live!",
        "usage": "POST JSON with { repo_url, issue_numbers } to /analyze"
    }


@app.post("/analyze")
async def analyze_issues(data: IssueRequest):
    start_time = time.time()

    # Parse repo
    parts = data.repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]

    # Parse issue numbers
    issue_numbers = [n.strip() for n in data.issue_numbers.split(",") if n.strip()]

    results = []

    async with httpx.AsyncClient() as client:
        for num in issue_numbers:
            try:
                # Fetch issue & comments
                issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{num}"
                comments_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{num}/comments"

                issue_resp = await client.get(issue_url)
                if issue_resp.status_code == 404:
                    results.append({"issue_number": num, "error": f"Issue #{num} not found."})
                    continue

                issue_resp.raise_for_status()
                issue = issue_resp.json()

                comments_resp = await client.get(comments_url)
                comments_resp.raise_for_status()
                comments = comments_resp.json()
                comments_text = " ".join([c["body"] for c in comments])

                # Build prompt
                prompt = f"""
You are an AI assistant. Analyze the GitHub issue below. Output ONLY raw JSON in this EXACT format:
{{
  "summary": "A one-sentence summary.",
  "type": "One of: bug, feature_request, documentation, question, other.",
  "priority_score": "1–5 with brief justification in parentheses.",
  "suggested_labels": ["2–3 relevant GitHub labels."],
  "potential_impact": "A brief sentence if bug, else 'null'."
}}
Title: {issue['title']}
Body: {issue['body']}
Comments: {comments_text}
"""

                # Call Gemini
                result = llm.invoke(prompt)
                content = re.sub(r"```json|```", "", result.content).strip()
                parsed = json.loads(content)

                # Sanitize labels
                labels = parsed.get("suggested_labels")
                if isinstance(labels, dict):
                    parsed["suggested_labels"] = list(labels.values())
                elif isinstance(labels, str):
                    parsed["suggested_labels"] = [labels]
                if len(parsed["suggested_labels"]) > 3:
                    parsed["suggested_labels"] = parsed["suggested_labels"][:3]

                # Fix impact
                if parsed.get("type") != "bug":
                    parsed["potential_impact"] = "null"
                elif not parsed.get("potential_impact"):
                    parsed["potential_impact"] = "null"

                results.append({"issue_number": num, "result": parsed})

            except httpx.HTTPStatusError as e:
                results.append({"issue_number": num, "error": f"GitHub API error: {e.response.status_code}"})
            except Exception as e:
                results.append({"issue_number": num, "error": str(e)})

    duration = round(time.time() - start_time, 2)
    return {"analysis_time_sec": duration, "results": results}
