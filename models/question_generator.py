from langchain_groq import ChatGroq
from config import MODEL_NAME, TEMPERATURE, GROQ_API_KEY
import json

class QuestionGenerator:
    def __init__(self):
        self.llm = ChatGroq(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            groq_api_key=GROQ_API_KEY
        )
    
    def generate_question(self, subject: str, difficulty: float) -> dict:
        prompt = self._create_prompt(subject, difficulty)
        response = self.llm.invoke(prompt)
        
        try:
            # Extract JSON from the response
            json_str = response.content
            return json.loads(json_str)
        except (json.JSONDecodeError, AttributeError):
            return self._create_fallback_question()
    
    def _create_prompt(self, subject: str, difficulty: float) -> str:
        return f"""Generate an independent and unique multiple-choice question for the subject "{subject}" at a difficulty level of {difficulty}/3. 
        Each question must meet the following criteria:
        - It should be entirely self-contained and unrelated to any previous or subsequent questions in terms of content, phrasing, or themes.
        - The difficulty should precisely match {difficulty}/3, targeting the knowledge level of a college student.
        - All four options must be plausible, with one correct answer clearly identifiable.

        Provide the response strictly in the following JSON format:
        {{
            "question": "Your self-contained and independent question here",
            "options": ["option1", "option2", "option3", "option4"],
            "correct_answer": 0,
            "explanation": "Detailed and educational explanation for the correct answer."
        }}
        
        Guidelines:
        1. Each question must be self-contained and require no context from other questions.
        2. Avoid repeating any concepts, phrasing, or themes from previous questions.
        3. Incorporate creativity and diversity in the topics, phrasing, and approach for each question.
        4. Ensure the explanation is clear, educational, and relevant to the correct answer.
        5. Questions should be engaging and aligned with a college student's level of understanding."""


    
    def _create_fallback_question(self) -> dict:
        return {
            "question": "An error occurred generating the question. Please try again.",
            "options": ["Error"] * 4,
            "correct_answer": 0,
            "explanation": "Please proceed to the next question."
        }