import streamlit as st
from models.question_generator import QuestionGenerator
from utils.assessment import AdaptiveAssessment

def initialize_session():
    """Initialize or get session state variables"""
    if "assessment" not in st.session_state:
        st.session_state.assessment = None
    if "question_generator" not in st.session_state:
        st.session_state.question_generator = QuestionGenerator()
    if "feedback" not in st.session_state:
        st.session_state.feedback = None