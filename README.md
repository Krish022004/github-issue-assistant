# ✅ FINAL README.md

# GitHub Issue Assistant 🚀

AI-powered GitHub Issue summarizer using **FastAPI**, **LangChain + Gemini**, and **Streamlit**.

---

## 📌 Submission Note

Hello Seedling Labs Team,

I’m submitting my completed **AI-Powered GitHub Issue Assistant** as per the Craft Case instructions.

✅ **Key Highlights:**
- Implements a FastAPI backend that fetches any public GitHub issue and uses LangChain with Gemini to generate a structured JSON output.
- The JSON output strictly matches the required schema: `summary`, `type`, `priority_score` (with justification), `suggested_labels` (2–3 labels), and `potential_impact` (real sentence for bugs, "null" string otherwise).
- Robust post-processing guarantees valid JSON, even with LLM quirks.
- Clean, user-friendly Streamlit frontend that displays the JSON clearly and provides a reliable Copy JSON button (using modern clipboard API).
- Handles API errors, quota limits, and invalid inputs gracefully.
- Uses `.env` for secure API key management; `.env.example` provided.

✅ **How to run:**
1. Clone the repo  
2. Create `.env` from `.env.example` and add your Gemini API key  
3. `pip install -r requirements.txt`  
4. Run backend: `uvicorn main:app --reload`  
5. Run frontend: `streamlit run app.py`  
6. Test at [http://localhost:8501](http://localhost:8501)

I have carefully verified that it aligns with the submission checklist and rubric.

Thank you for reviewing my submission — I look forward to your feedback!

**Best regards,**  
G Krishna Teja

---

## ✅ Features

- Clean AI-generated JSON matching Seedling Labs spec  
- Handles `bug` vs non-bug `potential_impact`  
- Copy JSON button (browser-native, works everywhere)  
- Runs locally with clear instructions

## ⚙️ Requirements

- Python 3.10+
- Gemini API Key (store in `.env`)

## 🔑 .env variables

| Key | Description |
| --- | --- |
| `GOOGLE_API_KEY` | Your Gemini API key |

## ✅ Output JSON Format

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
- Handles API quota errors gracefully.

✅ Happy coding & good luck with Seedling Labs! 🚀
