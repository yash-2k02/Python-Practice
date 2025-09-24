from langsmith import Client
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT
# from langsmith.evaluation import run_evaluator
from dotenv import load_dotenv

load_dotenv()

client = Client()

dataset = client.create_dataset(dataset_name="Test_dataset-5")

examples = [
    {
        "inputs": {"question": "Which country is Mount Kilimanjaro located in?"},
        "outputs": {"answer": "Mount Kilimanjaro is located in Tanzania."},
    },
    {
        "inputs": {"question": "What is Earth's lowest point?"},
        "outputs": {"answer": "Earth's lowest point is The Dead Sea."},
    },
]

client.create_examples(dataset_id=dataset.id, examples=examples)

llm = ChatOllama(model="llama3")

prompt = ChatPromptTemplate.from_template(
    "Answer the following question accurately: {question}"
)

parser = StrOutputParser()

chain = prompt | llm | parser

def target(inputs: dict):
    response = chain.invoke(inputs)
    return {"answer": response}

judge_llm = ChatOllama(model="deepseek-r1:8b")

# @run_evaluator
def correctness_evaluator(run, example):
    evaluator = create_llm_as_judge(
        prompt=CORRECTNESS_PROMPT,
        judge=judge_llm,
        feedback_key="correctness"
    )
    return evaluator(
        inputs=example.inputs,
        outputs=run.outputs,
        reference_outputs=example.outputs
    )

experiment_results = client.evaluate(
    target,
    data=dataset.id,
    evaluators=[correctness_evaluator],
    experiment_prefix="ollama-llama3-eval-semantic",
    max_concurrency=2,
)

print(experiment_results)