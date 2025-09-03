'''
OllamaLLM
It's a stateless LLM wrapper.
It only takes a single string prompt and produces a single string output.

ChatOllama
It's a chat model wrapper (like ChatOpenAI).
It supports structured messages (HumanMessage, AIMessage, SystemMessage).
Integrates well with LangChain's memory classes (ConversationBufferMemory, ConversationSummaryMemory, VectorStoreRetrieverMemory, etc.).


OllamaLLM  - single-shot text generation (summarization, completion, rewriting).
ChatOllama - when you want conversations with memory and context retention.

'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.exceptions import OutputParserException, LangChainException, TracerException 
from langchain_core.messages import HumanMessage

app = FastAPI(title="Langchain demo", docs_url="/swagger")

llm = ChatOllama(model="llama3")


class Query(BaseModel):
    prompt: str = Field(min_length=5)
    
class MultiQuery(BaseModel):
    prompts: list[str] = Field(min_items=1)



@app.post("/chat")
async def chat(query: Query):
    try:
        response = await llm.ainvoke([HumanMessage(content=query.prompt)])

        if not response or not response.content:
            raise HTTPException(status_code=500, detail="Empty response from LLM.")
        
        return {"response": response.content}
    
    except OutputParserException as e:
        raise HTTPException(status_code=422, detail=f"Output parsing failed: {str(e)}")

    except TracerException as e:
        raise HTTPException(status_code=500, detail=f"Tracing error: {str(e)}")

    except LangChainException as e:
        raise HTTPException(status_code=500, detail=f"LangChain error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
    
    
@app.post("/chat/generate")
async def generate(m_query:MultiQuery):
    try:
        prompts = [[HumanMessage(content=p)] for p in m_query.prompts]
        responses = await llm.agenerate(prompts)
        
        if not responses or not responses.generations:
                raise HTTPException(status_code=500, detail="Empty response from LLM.")

        # results = [ gen[0].message.content for gen in responses.generations]
        # return {"responses": results}
        
        return {"responses": responses}
        
        
    except OutputParserException as e:
        raise HTTPException(status_code=422, detail=f"Output parsing failed: {str(e)}")

    except TracerException as e:
        raise HTTPException(status_code=500, detail=f"Tracing error: {str(e)}")

    except LangChainException as e:
        raise HTTPException(status_code=500, detail=f"LangChain error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
   

@app.post("/chat/batch")
async def batch(m_query:MultiQuery):
    try:
        prompts = [[HumanMessage(content=p)] for p in m_query.prompts]
        responses = await llm.abatch(prompts)
        
        if not responses:
                raise HTTPException(status_code=500, detail="Empty response from LLM.")
            
        # results = [resp.content for resp in responses]
        # return {"responses": results}
        
        return {"responses": responses}
        
        
    except OutputParserException as e:
        raise HTTPException(status_code=422, detail=f"Output parsing failed: {str(e)}")

    except TracerException as e:
        raise HTTPException(status_code=500, detail=f"Tracing error: {str(e)}")

    except LangChainException as e:
        raise HTTPException(status_code=500, detail=f"LangChain error: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")