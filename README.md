# GitHub Issue Assistant 🚀

## 📌 Overview
This public GitHub repository is my complete solution for the Seedling Labs Craft Case. It includes a robust FastAPI backend, LangChain with Gemini for AI processing, and a simple Streamlit UI. **Anyone can clone, set up, and run it in under 5 minutes** — demonstrating clear documentation and developer empathy.

## ✅ Submission Note
Hello Seedling Labs Team,

I’m submitting this fully working project, tested to match all rubric points:
- ✔️ JSON output: strict format with `summary`, `type`, `priority_score` (with justification), `suggested_labels` (2–3 only), `potential_impact` (sentence for bugs, `'null'` for non-bugs)
- ✔️ Reliable backend logic and post-cleaning for valid output
- ✔️ Easy local setup instructions in this README
- ✔️ Clear UI with copy button for the JSON

**Author:**  
**G Krishna Teja**

Thank you for reviewing my submission!

## ⚙️ Requirements
- Python 3.10+
- Gemini API key saved securely in `.env`

## ⚡️ Quick Setup (Run in under 5 minutes)

1️⃣ **Clone:**
```bash
git clone <your-repo-url>
cd github-issue-assistant
```

2️⃣ **Add API key:**
```bash
cp .env.example .env
# then open .env and paste your actual Gemini API key
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

4️⃣ **Run backend:**
```bash
uvicorn main:app --reload
```

5️⃣ **Run frontend:**
```bash
streamlit run app.py
```

6️⃣ **Open:**  
Visit [http://localhost:8501](http://localhost:8501), input a repo URL and issue number, click **Analyze**, and copy the JSON output.

## ✅ JSON Output Format
```json
{
  "summary": "One-sentence summary of the issue.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "Score from 1–5 with short justification in parentheses.",
  "suggested_labels": ["2–3 relevant GitHub labels"],
  "potential_impact": "Impact sentence if bug, else 'null' as string"
}
```

## 🔐 Security
- `.env` must **never** be pushed; `.gitignore` enforces this.
- `.env.example` shows how to set up your key.

## ✅ Notes
- Handles public issues only.
- Gracefully informs users if API quota is exceeded.

✅ Thanks again, Seedling Labs — looking forward to your feedback! 🚀✨
