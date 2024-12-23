import { useState, useCallback } from 'react';
import { Question, Assessment } from '../types';
import { questionsData } from '../data/questions';

export const useAssessment = () => {
  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [showFeedback, setShowFeedback] = useState(false);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);

  const startAssessment = useCallback((subject: string) => {
    setAssessment({
      subject,
      currentQuestion: 0,
      score: 0,
      difficulty: 1,
      questions: questionsData[subject as keyof typeof questionsData],
      answers: []
    });
    setShowFeedback(false);
    setIsCorrect(null);
  }, []);

  const answerQuestion = useCallback((answerIndex: number) => {
    if (!assessment) return;

    const currentQuestion = assessment.questions[assessment.currentQuestion];
    const correct = answerIndex === currentQuestion.correctAnswer;

    setIsCorrect(correct);
    setShowFeedback(true);

    // Update assessment state after a brief delay to show feedback
    setTimeout(() => {
      setAssessment(prev => {
        if (!prev) return null;

        const newAnswers = [...prev.answers];
        newAnswers[prev.currentQuestion] = answerIndex;

        let newDifficulty = prev.difficulty;
        if (correct) {
          newDifficulty = Math.min(3, newDifficulty + 0.5);
        } else {
          newDifficulty = Math.max(1, newDifficulty - 0.5);
        }

        return {
          ...prev,
          currentQuestion: prev.currentQuestion + 1,
          score: correct ? prev.score + 1 : prev.score,
          difficulty: newDifficulty,
          answers: newAnswers
        };
      });
      setShowFeedback(false);
      setIsCorrect(null);
    }, 2000);
  }, [assessment]);

  return {
    assessment,
    showFeedback,
    isCorrect,
    startAssessment,
    answerQuestion
  };
};