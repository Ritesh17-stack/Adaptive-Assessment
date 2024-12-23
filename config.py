import os
from dotenv import load_dotenv

load_dotenv()

# Model Configuration
MODEL_NAME = "llama-3.1-70b-versatile"
TEMPERATURE = 0.7

# API Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Assessment Configuration
MAX_QUESTIONS = 10
DIFFICULTY_LEVELS = {
    1: "basic",
    2: "intermediate",
    3: "advanced"
}