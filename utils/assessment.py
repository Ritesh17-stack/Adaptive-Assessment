from typing import List, Dict

class AdaptiveAssessment:
    def __init__(self, subject: str):
        self.subject = subject
        self.current_difficulty = 1.0
        self.score = 0
        self.questions_asked: List[Dict] = []
        self.current_question = None
        
    def update_difficulty(self, correct: bool):
        """Update difficulty based on answer correctness"""
        if correct:
            self.current_difficulty = min(3.0, self.current_difficulty + 0.3)
            self.score += 1
        else:
            self.current_difficulty = max(1.0, self.current_difficulty - 0.2)
    
    def add_question(self, question: dict):
        """Add a new question to the assessment"""
        self.current_question = question
        self.questions_asked.append(question)
    
    def get_stats(self) -> dict:
        """Get current assessment statistics"""
        return {
            "subject": self.subject,
            "current_difficulty": round(self.current_difficulty, 1),
            "score": self.score,
            "total_questions": len(self.questions_asked),
            "accuracy": f"{(self.score / len(self.questions_asked) * 100):.1f}%" if self.questions_asked else "0%"
        }