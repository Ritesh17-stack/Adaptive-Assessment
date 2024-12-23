import streamlit as st
from utils.session import initialize_session
from config import MAX_QUESTIONS

def display_subject_selection():
    st.title("🎯 Adaptive Assessment System")
    st.markdown("""
    This system adapts to your knowledge level by adjusting question difficulty 
    based on your performance.
    """)
    
    subjects = ["Mathematics", "Science", "History", "Geography"]
    subject = st.selectbox("📚 Select a subject:", subjects)
    
    if st.button("Start Assessment", type="primary"):
        from utils.assessment import AdaptiveAssessment
        st.session_state.assessment = AdaptiveAssessment(subject.lower())
        # st.experimental_rerun()
        st.rerun()

def display_question():
    assessment = st.session_state.assessment
    
    # Generate new question if needed
    if not assessment.current_question:
        question = st.session_state.question_generator.generate_question(
            assessment.subject,
            assessment.current_difficulty
        )
        assessment.add_question(question)
    
    # Display progress
    progress = len(assessment.questions_asked)
    st.progress(progress / MAX_QUESTIONS)
    st.markdown(f"**Question {progress}/{MAX_QUESTIONS}** | Difficulty: {assessment.current_difficulty:.1f}/3")
    
    # Display question
    st.markdown(f"### {assessment.current_question['question']}")
    
    # Display options
    answer = st.radio(
        "Select your answer:",
        assessment.current_question["options"],
        key=f"q_{progress}"
    )
    
    # Add answer submission state
    if "answer_submitted" not in st.session_state:
        st.session_state.answer_submitted = False
    
    # Handle submission
    if not st.session_state.answer_submitted and st.button("Submit Answer", type="primary"):
        correct = (
            assessment.current_question["options"].index(answer) ==
            assessment.current_question["correct_answer"]
        )
        assessment.update_difficulty(correct)
        st.session_state.answer_submitted = True
        
        # Show feedback
        if correct:
            st.success("✨ Correct! Well done!")
        else:
            st.error("❌ Incorrect!")
            correct_answer = assessment.current_question["options"][
                assessment.current_question["correct_answer"]
            ]
            st.markdown(f"**Correct answer:** {correct_answer}")
        
        st.info(f"📝 **Explanation:** {assessment.current_question['explanation']}")
        
        # Check if assessment is complete
        if len(assessment.questions_asked) >= MAX_QUESTIONS:
            st.session_state.feedback = assessment.get_stats()
            # st.experimental_rerun()
            st.rerun()
    
    # Show Next Question button only after submission
    if st.session_state.answer_submitted:
        if st.button("Next Question", type="primary"):
            assessment.current_question = None
            st.session_state.answer_submitted = False
            # st.experimental_rerun()
            st.rerun()

def display_results():
    st.title("🎉 Assessment Complete!")
    stats = st.session_state.feedback
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Final Score", f"{stats['score']}/{stats['total_questions']}")
    with col2:
        st.metric("Accuracy", stats['accuracy'])
    
    st.markdown(f"""
    ### Performance Summary
    - **Subject:** {stats['subject'].title()}
    - **Final Difficulty Level:** {stats['current_difficulty']}/3
    """)
    
    if st.button("Start New Assessment", type="primary"):
        st.session_state.assessment = None
        st.session_state.feedback = None
        st.session_state.answer_submitted = False
        # st.experimental_rerun()
        st.rerun()

def main():
    initialize_session()
    
    if st.session_state.feedback:
        display_results()
    elif st.session_state.assessment is None:
        display_subject_selection()
    else:
        display_question()

if __name__ == "__main__":
    main()