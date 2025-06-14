"""
FastAPI backend for Seedling Labs Craft Case.
Supports bulk GitHub issues, validates each, calls LangChain Gemini,
and returns clean JSON array with exact schema.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
import re
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import time

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=API_KEY
)

app = FastAPI()

class IssueRequest(BaseModel):
    repo_url: str
    issue_numbers: str  # support comma-separated list

@app.post("/analyze")
async def analyze_issues(data: IssueRequest):
    start = time.time()

    parts = data.repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    issue_numbers = [n.strip() for n in data.issue_numbers.split(',') if n.strip()]

    results = []

    async with httpx.AsyncClient() as client:
        for num in issue_numbers:
            try:
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
                content = re.sub(r"```json|```", "", result.content).strip()
                parsed = json.loads(content)

                if isinstance(parsed.get("suggested_labels"), dict):
                    parsed["suggested_labels"] = list(parsed["suggested_labels"].values())

                if len(parsed.get("suggested_labels", [])) > 3:
                    parsed["suggested_labels"] = parsed["suggested_labels"][:3]

                if parsed.get("type") != "bug":
                    parsed["potential_impact"] = "null"
                elif parsed.get("potential_impact") in [None, "", "null"]:
                    parsed["potential_impact"] = "null"

                results.append({"issue_number": num, "result": parsed})

            except httpx.HTTPStatusError as e:
                results.append({"issue_number": num, "error": f"GitHub API error: {e.response.status_code}"})
            except Exception as e:
                results.append({"issue_number": num, "error": str(e)})

    duration = round(time.time() - start, 2)
    return {"analysis_time_sec": duration, "results": results}
