# 🚀 GitHub Issue Assistant

## 📌 Project Overview
**AI-powered assistant** that fetches and analyzes **any public GitHub issue** and returns a clean, structured JSON — exactly matching the **Seedling Labs Craft Case** schema.  
It combines **FastAPI** (robust backend), **LangChain + Gemini** (AI analysis), and **Streamlit** (modern frontend) — with clear documentation for developers to run it in **under 5 minutes**.

---

## ✅ Submission Note

Hello Seedling Labs Team,

I’m excited to submit my completed **AI-Powered GitHub Issue Assistant**.  
It has been tested end-to-end and fully aligns with the submission checklist and rubric:

- ✅ JSON strictly matches the required schema: `summary`, `type`, `priority_score` (with justification), `suggested_labels` (2–3 only), and `potential_impact` (sentence for bugs, `'null'` for others).
- ✅ Robust FastAPI backend with strict validation and cleanup to guarantee valid JSON.
- ✅ Quick-start instructions — run the project **locally or on Render in under 5 minutes**.
- ✅ Clean, user-friendly Streamlit UI with **Copy JSON** & **Download JSON** options.
- ✅ Supports **multiple issue analysis** in one go.

**Author:**  
**G Krishna Teja**

Thank you for reviewing my submission!

---

## ⚙️ Requirements

- Python **3.10+**
- A valid **Gemini API key**, securely stored in `.env`

---

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

6️⃣ **Open your browser:**  
Visit [http://localhost:8501](http://localhost:8501).  
Enter a **public GitHub repository URL** and one or more **issue numbers** (comma-separated). Click **🚀 Analyze Issues** to get clean, ready-to-use JSON.

---

## 🧩 Example Usage

| Field | Example |
|-------|---------|
| **Repository URL** | `https://github.com/facebook/react` |
| **Issue Numbers** | `1, 2, 3` |

Click **Analyze Issues** → view & copy the AI-generated JSON summary for each issue!

---

## ✅ JSON Output Format

Below is the guaranteed output format for each issue:
```json
{
  "summary": "One-sentence summary of the issue.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "Score from 1–5 with justification in parentheses.",
  "suggested_labels": ["2–3 relevant GitHub labels"],
  "potential_impact": "Sentence describing impact if bug; else 'null' as a string"
}
```

---

## 🔐 Security & .env

- **`.env`** is **never pushed** — `.gitignore` protects your API key.
- **`.env.example`** is included so others can set up easily.

---

## 🛠️ Troubleshooting

- **403/422/502 errors?** Make sure:
  - Your FastAPI backend is running and reachable (local or Render).
  - You use a valid **public** GitHub repo and issue numbers.
  - Your Gemini API key is correct and has quota.
- **Render goes to sleep:** If you use free Render deployment, the backend may sleep — just wait a moment, then retry.
- **API quota limits:** Free Gemini API usage may hit rate limits — check your Google Cloud usage.

---

## ✅ Additional Highlights

- 🔗 **Works with any public GitHub issue.**
- 🗂️ **Handles multiple issues at once.**
- 🎨 **Modern UI with dark mode & animations.**
- 📋 **One-click copy & download for JSON.**
- ⚙️ **Deploy easily on Render or run locally.**

---

## 🙏 Thank You

✅ **Thank you, Seedling Labs Team, for this exciting challenge!**  
I look forward to your valuable feedback and next steps. 🚀✨

---

## 🔗 Useful Links

- **Frontend (Streamlit)**: [https://github-issue-assistant-1.onrender.com](https://github-issue-assistant-1.onrender.com)
- **Backend (FastAPI)**: [https://github-issue-assistant.onrender.com/analyze](https://github-issue-assistant.onrender.com/analyze)
- **Source Code**: [GitHub Repo](https://github.com/Krish022004/github-issue-assistant)

---

## 📝 License

MIT — free to fork and build on!
