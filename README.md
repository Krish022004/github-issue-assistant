# GitHub Issue Assistant 🚀

## 📌 Project Overview
This AI-powered assistant fetches and analyzes any **public GitHub issue** and returns a clean, structured JSON that matches the **Seedling Labs Craft Case** specification exactly. It combines **FastAPI** (backend), **LangChain + Gemini** (AI analysis), and **Streamlit** (frontend) — all documented for quick setup and developer friendliness.

## ✅ Submission Note
Hello Seedling Labs Team,

I am pleased to submit my completed **AI-Powered GitHub Issue Assistant**. It has been tested end-to-end and meets all points of the submission checklist and rubric:

- ✔️ JSON strictly matches `summary`, `type`, `priority_score` (with justification), `suggested_labels` (2–3 only), and `potential_impact` (sentence for bugs, `'null'` for non-bugs).
- ✔️ Robust backend with post-cleanup to ensure valid JSON.
- ✔️ Easy-to-follow instructions so any developer can run it in **under 5 minutes**.
- ✔️ Clean, user-friendly UI with a working **Copy JSON** button.

**Author:**  
**G Krishna Teja**

Thank you for reviewing my submission!

## ⚙️ Requirements
- Python 3.10+
- Gemini API key stored securely in `.env`

## ⚡️ Quick Setup (Run in Under 5 Minutes)

1️⃣ **Clone this repository:**
```bash
git clone <your-repo-url>
cd github-issue-assistant
```

2️⃣ **Add your Gemini API key:**
```bash
cp .env.example .env
# Open .env and paste your actual API key
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

4️⃣ **Run the FastAPI backend:**
```bash
uvicorn main:app --reload
```

5️⃣ **Run the Streamlit frontend:**
```bash
streamlit run app.py
```

6️⃣ **Open in your browser:**
Visit [http://localhost:8501](http://localhost:8501). Enter any **public GitHub repo URL** and **issue number**, then click **Analyze Issue**.

## 🧩 Example Usage
**Example:**  
- Repository URL: `https://github.com/facebook/react`  
- Issue Number: `1`  
Click **Analyze Issue** — you’ll get a clean JSON summary that you can view and copy.

## ✅ JSON Output Format
```json
{
  "summary": "One-sentence summary of the issue.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "Score from 1–5 with justification in parentheses.",
  "suggested_labels": ["2–3 relevant GitHub labels"],
  "potential_impact": "Sentence describing impact if bug, else 'null' as a string"
}
```

## 🔐 Security & .env
- `.env` **must never be pushed** — `.gitignore` ensures your API key stays private.
- `.env.example` is included to guide other developers.

## 🛠️ Troubleshooting
- If you see an API quota error, it means your free tier limit was reached — wait a few minutes or check your Gemini usage in your Google Cloud dashboard.
- Make sure the repo URL and issue number are valid and public.

## ✅ Additional Notes
- Works with **any public GitHub issue**.
- Handles large comments and multiple issue replies.
- Clean error handling for invalid input and rate limits.

✅ **Thank you, Seedling Labs Team, for the opportunity! Looking forward to your feedback.** 🚀✨
