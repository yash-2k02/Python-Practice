from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatOllama(model="llama3", num_predict=300)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer the following clearly:\n\nQuestion: {question}\nAnswer:"
)

chain = prompt | llm | parser

response = chain.invoke("why is cricket more popular in India than football")

print(response)