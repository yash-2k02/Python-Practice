from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.exceptions import LangChainException, OutputParserException, TracerException
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="LLM Parameters")

llm = ChatOllama(
    model="llama3",
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    num_predict=300
)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer the following clearly:\n\nQuestion: {question}\nAnswer:"
)

chain = prompt | llm | parser


class Query(BaseModel):
    prompt: str
    
class Multiquery(BaseModel):
    prompts: List[str]



@app.post("/chat")
async def chaining_invoke(query:Query):
    try:
        
        response = await chain.ainvoke(query.prompt)
        return {"response": response}

    except OutputParserException as e:
        raise HTTPException(status_code=422, detail=f"Output parsing failed: {str(e)}")

    except TracerException as e:
        raise HTTPException(status_code=500, detail=f"Tracing error: {str(e)}")

    except LangChainException as e:
        raise HTTPException(status_code=500, detail=f"LangChain error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")    