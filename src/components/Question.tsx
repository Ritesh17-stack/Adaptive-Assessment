import React from 'react';
import { Question as QuestionType } from '../types';

interface QuestionProps {
  question: QuestionType;
  onAnswer: (answerIndex: number) => void;
  showFeedback: boolean;
  isCorrect: boolean | null;
}

export const Question: React.FC<QuestionProps> = ({
  question,
  onAnswer,
  showFeedback,
  isCorrect,
}) => {
  return (
    <div className="space-y-6">
      <div className="p-6 bg-white rounded-lg shadow-md">
        <div className="flex justify-between items-center mb-4">
          <span className="text-sm text-gray-500">
            Difficulty: {question.difficulty}/3
          </span>
        </div>
        <h3 className="text-xl font-semibold text-gray-900 mb-4">{question.text}</h3>
        <div className="space-y-3">
          {question.options.map((option, index) => (
            <button
              key={index}
              onClick={() => onAnswer(index)}
              className={`w-full p-4 text-left rounded-lg transition-all ${
                showFeedback
                  ? index === question.correctAnswer
                    ? 'bg-green-100 border-green-500'
                    : 'bg-red-100 border-red-500'
                  : 'bg-gray-50 hover:bg-gray-100'
              } border`}
              disabled={showFeedback}
            >
              {option}
            </button>
          ))}
        </div>
        {showFeedback && (
          <div className={`mt-4 p-4 rounded-lg ${
            isCorrect ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
          }`}>
            {isCorrect
              ? "Correct! Well done!"
              : `Incorrect. The correct answer was: ${
                  question.options[question.correctAnswer]
                }`}
          </div>
        )}
      </div>
    </div>
  );
};