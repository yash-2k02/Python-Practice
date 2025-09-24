# Chat with Documents API

This is a FastAPI-based application that allows users to upload PDF documents, embed them into a vector store using embeddings, and chat with the content using a RAG (Retrieval-Augmented Generation) approach. It integrates LangChain, Chroma, HuggingFaceEmbeddings, and ChatOllama.

Features:

- Upload PDF documents for embedding.
- Split documents into chunks for efficient retrieval.
- Store document embeddings in a persistent Chroma vector store.
- Ask questions about uploaded documents using a RAG chain.
- Streaming responses from the model.
- Logging of all actions including uploads and chat requests.

---
API Endpoints:

1. Embed Document
- Endpoint: /embed
- Method: POST
- Description: Upload a PDF document and embed it into the vector store.
- Request: file (PDF file to upload)
- Responses:
  - 200 OK: {"message": "Document '<filename>' embedded."}
  - 400 Bad Request: Only PDF files are supported
  - 500 Internal Server Error: Error while embedding the document

Example using curl:
```
curl -X POST "http://localhost:8000/embed" -F "file=@example.pdf"
```

2. Chat with Document
- Endpoint: /chat
- Method: POST
- Description: Ask a question about the uploaded documents. Returns a streaming response.
- Request Parameters: question (string) - The question to ask about the documents
- Responses:
  - 200 OK: Streaming response containing the answer
  - 500 Internal Server Error: Error while generating the response

Example using curl:
```
curl -X POST "http://localhost:8000/chat" -d "question=What is the summary of the document?"
```

---
Project Structure:

```
.
├── main.py                 # Main FastAPI application
├── src
│   └── settings.py         
│       └── logging.py      # Logging setup
├── chroma-data             # Directory for persistent vector store
├── uploads                 # Directory to store uploaded PDF files
└── README.md
```
---

Installation:

1. Clone the repository:
```
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Running the App:

Start the FastAPI server:
```
uvicorn main:app --reload
```