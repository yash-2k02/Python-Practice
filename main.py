from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import LangChainException, OutputParserException
import os
import shutil
from src.settings import logger

PERSIST_DIRECTORY = "./chroma-data"
UPLOAD_DIR = "./uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatOllama(model="llama3")

vector_store = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embeddings,
    collection_name="my_docs"
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context:
{context}

Question: {question}

Answer:
""")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

app = FastAPI(title="Chat with Documents API")


@app.post("/embed")
def embed_document(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file upload request: {file.filename}")

        if not file.filename.endswith(".pdf"):
            logger.warning(f"Rejected non-PDF file: {file.filename}")
            raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"Saved file to {file_path}")

        loader = PyPDFLoader(file_path)
        documents = loader.load()
        logger.info(f"Loaded {len(documents)} pages from {file.filename}")


        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        docs = text_splitter.split_documents(documents)

        vector_store.add_documents(docs)
        logger.info(f"Embedded document: {file.filename}")


        return {"message": f"Document '{file.filename}' embedded."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/chat")
def chat_with_doc(question: str):
    try:
        logger.info(f"Received chat request: {question}")

        def response():
            try:
                for chunk in rag_chain.stream(question):
                    yield chunk
            except OutputParserException:
                logger.error("Output parsing error.")
                yield "\n[Error] Output parsing error."
            except LangChainException:
                logger.error("LangChain chain error.")
                yield "\n[Error] LangChain chain error."
            except Exception as e:
                logger.exception("Unexpected error during chat response.")
                yield f"\n[Error] {str(e)}"

        return StreamingResponse(response())

    except Exception as e:
        logger.exception("Error handling chat request.")
        raise HTTPException(status_code=500, detail=str(e))
