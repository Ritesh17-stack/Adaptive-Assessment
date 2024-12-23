from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from config import MODEL_ID, MAX_LENGTH, TEMPERATURE

class LLMHandler:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
    def generate_question(self, subject: str, difficulty: int, previous_questions: list) -> dict:
        prompt = self._create_prompt(subject, difficulty, previous_questions)
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_length=MAX_LENGTH,
            temperature=TEMPERATURE,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return self._parse_response(response)
    
    
    def _parse_response(self, response: str) -> dict:
        # Extract JSON from response and parse it
        # Implementation depends on actual model output format
        # This is a simplified version
        import json
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "question": "Error generating question",
                "options": ["Error"] * 4,
                "correct_answer": 0,
                "explanation": "Error in question generation"
            }