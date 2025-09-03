# LangChain + FastAPI + Ollama Demo

This project demonstrates how to integrate **LangChain’s `ChatOllama` wrapper** with a **FastAPI** backend.  
It provides REST endpoints for interacting with **Ollama LLMs** (`llama3`) using different invocation methods:  

- **`invoke` / `ainvoke`** → Single prompt request-response (LCEL style)  
- **`generate` / `agenerate`** → Multiple prompts with structured generations (pre-LCEL style)  
- **`batch` / `abatch`** → Efficient batch inference (LCEL style)  

---

## Features
- FastAPI-powered REST endpoints  
- Integration with **LangChain’s ChatOllama**  
- Exception handling with clean HTTP errors  
- Demonstrates **pre-LCEL** and **LCEL** usage  

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

