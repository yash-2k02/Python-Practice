# Hugging Face Transformers + LangChain Integration

This project demonstrates how to load and run **Hugging Face LLMs** using both the `transformers` library and a class-based LangChain wrapper.  

It demonstrates:  
- Direct model inference with **Transformers**.  
- Class-based initialization with **LangChain HuggingFacePipeline**.  
- Basic caching to avoid reloading the same model multiple times.
 
---

## Features

- Generate text using `microsoft/phi-2`/`Qwen/Qwen3-0.6B` model.  
- Class-based structure for easier integration with LangChain pipelines.  
- Flexible prompt handling and max-length configuration.  

---

## Requirements

- Python 3.10+  
- PyTorch (`torch`)  
- Transformers (`transformers`)  
- LangChain Hugging Face integration (`langchain_huggingface`) 

---