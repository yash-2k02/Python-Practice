from transformers import pipeline
from langchain_huggingface.llms import HuggingFacePipeline

class LangChainHFModel:
    
    _cache = {}
        
    def __init__(self, model_name: str, max_length: int = 200):

        if model_name in self._cache:
            self.llm = self._cache[model_name]
            print("Model and pipeline loaded from cache")
        else:
            print("Model and pipeline initialized")
            pipe = pipeline("text-generation", model=model_name, max_length=max_length)
            llm = HuggingFacePipeline(pipeline=pipe)
            self._cache[model_name] = llm
            self.llm = llm

    def invoke(self, prompt: str):
        return self.llm.invoke(prompt)


if __name__ == "__main__":
    # lc_model = LangChainHFModel("microsoft/phi-2")
    
    lc_model = LangChainHFModel("Qwen/Qwen3-0.6B")
    lc_model1 = LangChainHFModel("Qwen/Qwen3-0.6B")
    
    print(lc_model.invoke("Tell me about FastAPI.")) 
    print(lc_model1.invoke("Tell me about cricket."))
    
    