# LangSmith Integration with LangChain + Ollama

This project demonstrates how to integrate **LangChain**, **LangSmith**, and **Ollama** for building, running, and evaluating LLM-powered applications.

It covers:
- Running inference with **Ollama LLMs**.
- Creating and managing **datasets in LangSmith**.
- Running **LLM-as-a-judge evaluations** with [OpenEvals](https://github.com/langchain-ai/openevals).
- Evaluating responses for **correctness** using a secondary judge LLM.

---

## Features

1. **Run LLM Chains with Ollama**
   - Uses `ChatOllama` with `LangChain` prompt templates.
   - Example:
     ```python
     chain = prompt | llm | parser
     response = chain.invoke({"question": "Why is cricket more popular in India than football?"})
     print(response)
     ```

2. **Dataset Creation in LangSmith**
   - Programmatically creates datasets and examples:
     ```python
     dataset = client.create_dataset(dataset_name="Test_dataset-5")
     client.create_examples(dataset_id=dataset.id, examples=examples)
     ```

3. **Evaluation with LLM-as-a-Judge**
   - Uses `openevals.llm.create_llm_as_judge` and correctness prompt.
   - Runs automated evaluations comparing model outputs vs. reference answers.

---

## Getting Started

### 1. Install Dependencies
This project uses [uv](https://github.com/astral-sh/uv) for Python dependency management.

```bash
uv sync
```
---

### 2. Set Environment Variables
Create a `.env` file in the root directory with the following values:

Replace `your_langsmith_api_key` with your actual LangSmith API key.

---

### 3. Run the Example
To run a simple LLM chain with Ollama:

```python eval.py```