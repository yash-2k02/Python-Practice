from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)

inputs = tokenizer("Explain what is fastapi", return_tensors="pt", return_attention_mask=True)

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)

