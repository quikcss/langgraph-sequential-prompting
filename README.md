# 🧠 langgraph-sequential-prompting

A minimal example of using **Sequential Prompting** with [LangGraph](https://github.com/langchain-ai/langgraph) — a powerful pattern for chaining reasoning steps in a linear, modular way.

---

## 🚀 What is Sequential Prompting?

Sequential prompting breaks down a task into a series of logical steps where each step’s output becomes the input for the next.  
This makes it easier to:

- Debug individual steps  
- Build modular workflows  
- Ensure consistent reasoning in LLM pipelines  

---

## 📂 Project Structure

```bash
.
├── main.py              # Entry point with sequential LangGraph logic
├── .env                 # Environment variables (e.g., GROQ_API_KEY)
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Lock file (if using uv)
└── README.md            # This file

---

## ⚙️ Setup
1. ### Clone the rpository:
git clone https://github.com/vaibhav23244/langgraph-sequential-prompting.git
cd langgraph-sequential-prompting

2. ### Create a virtual environment and activate it:
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

3. ### Install dependencies using uv (or pip):
uv pip install -r requirements.txt
# OR
uv venv && uv pip install -e .

4. ### Add your Groq API key to a .env file:
GROQ_API_KEY=your_groq_api_key_here

## 📦 Dependencies
All core packages used:
-langgraph
-langchain
-langchain-groq
-grandalf
-python-dotenv
