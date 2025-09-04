# LLM Parameters  

This project provides a simple **FastAPI service** that integrates with **LangChain** and **Ollama** to interact with a large language model (LLM). It allows you to send prompts to a model (`llama3`) with configurable parameters like temperature, top-p, top-k, and number of predictions.  

---

## Features
- **Chat API** endpoint (`/chat`) for sending single queries.  
- Uses **LangChain pipeline** (`Prompt → LLM → Output Parser`).  
- **Configurable generation parameters**:  
  - `temperature` → controls randomness  
  - `top_p` → nucleus sampling  
  - `top_k` → limits sampling to top-k tokens  
  - `num_predict` → max tokens to generate  

---

## Requirements
- Python 3.9+  
- FastAPI  
- LangChain  
- Ollama (running locally with the `llama3` model pulled)