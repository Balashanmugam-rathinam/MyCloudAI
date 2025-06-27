import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMEngine:
    def __init__(self, model_name='mistralai/Mistral-7B-Instruct-v0.1'):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def query(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            output = self.model.generate(**inputs, max_new_tokens=150)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == '__main__':
    engine = LLMEngine()
    print(engine.query("Who are you?"))