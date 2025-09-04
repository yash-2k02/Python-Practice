# LangChain Chaining Demo (FastAPI + Ollama)

This project demonstrates how to build a simple **FastAPI API** that uses **LangChain** with an **Ollama LLM (Llama 3)**.  
It showcases **chaining** in LangChain with:

- **Prompt** → `ChatPromptTemplate`
- **LLM** → `ChatOllama`
- **Output Parser** → `StrOutputParser`

---

## Requirements

- Python **3.12+**
- [Ollama](https://ollama.com) installed and running locally or remotely
- Dependencies (installed automatically with `uv sync` or `pip install [below dependencies]`):
  - `fastapi`
  - `uvicorn`
  - `langchain`
  - `langchain-ollama`

---

## Setup Guide

Run these commands in order to set up and start the project:

```bash
1. Install Ollama
(Download from https://ollama.ai if not installed)

ollama --version

2. Pull the LLaMA 3 model
ollama pull llama3

3. Start the Ollama server (keep this running in a terminal)
ollama serve

4. Test Ollama directly
ollama run llama3

5. Clone this repository
git clone https://github.com/yash-2k02/python-practice.git
cd your-repo-name

6. Install dependencies

Using uv
  uv sync

OR using pip
  pip install fastapi uvicorn langchain langchain-ollama

7. Run FastAPI server
uvicorn main:app --reload

8. Open Swagger UI to test
Open in browser: http://127.0.0.1:8000/docs
