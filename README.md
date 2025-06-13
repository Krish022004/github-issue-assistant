# GitHub Issue Assistant 🚀

## 📌 Overview
A simple, robust AI-powered GitHub Issue Analyzer that summarizes any public issue and classifies it, following the Seedling Labs Craft Case specifications exactly.

## ✅ Features
- Produces JSON with `summary`, `type`, `priority_score` (with justification), `suggested_labels` (2–3 labels), and `potential_impact` (sentence for bugs, "null" string otherwise).
- Uses FastAPI for backend, LangChain with Gemini for AI, and Streamlit for a clean UI.
- Shows clear JSON output and a working Copy JSON button.
- Handles rate limits and API errors gracefully.

## ⚙️ Requirements
- Python 3.10+
- Gemini API Key (store in `.env`)

## 🚀 How to Run Locally

1️⃣ **Clone this repo:**
```bash
git clone <your-repo-url>
cd github-issue-assistant
```

2️⃣ **Set up `.env`:**
```
cp .env.example .env
# Edit .env and paste your Gemini API key
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

4️⃣ **Start the FastAPI backend:**
```bash
uvicorn main:app --reload
```

5️⃣ **Start the Streamlit frontend:**
```bash
streamlit run app.py
```

6️⃣ **Open the app:**
Go to [http://localhost:8501](http://localhost:8501) and test your repo URL and issue number.

## 🔑 Environment Variables
- `GOOGLE_API_KEY`: your Gemini API key

## ✅ Output JSON Format (as per Craft Case)
```json
{
  "summary": "A one-sentence summary.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "Score 1-5 with justification in parentheses.",
  "suggested_labels": ["label1", "label2"],
  "potential_impact": "Sentence for bugs, or 'null' string for non-bugs"
}
```

## 📝 Notes
- Only public GitHub issues are supported.
- Handles API quota errors with clear messages.
- Fully meets Seedling Labs submission & rubric requirements.

✅ Happy coding & good luck with your Craft Case! 🚀
