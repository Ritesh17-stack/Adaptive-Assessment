import React from 'react';
import { SubjectSelection } from './components/SubjectSelection';
import { Question } from './components/Question';
import { useAssessment } from './hooks/useAssessment';

function App() {
  const { assessment, showFeedback, isCorrect, startAssessment, answerQuestion } = useAssessment();

  if (!assessment) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
        <div className="w-full max-w-2xl">
          <SubjectSelection onSelectSubject={startAssessment} />
        </div>
      </div>
    );
  }

  const currentQuestion = assessment.questions[assessment.currentQuestion];

  if (assessment.currentQuestion >= assessment.questions.length) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
        <div className="w-full max-w-2xl text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Assessment Complete!</h2>
          <p className="text-lg text-gray-700 mb-6">
            Your score: {assessment.score} out of {assessment.questions.length}
          </p>
          <button
            onClick={() => startAssessment(assessment.subject)}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            Start New Assessment
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="w-full max-w-2xl">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 capitalize">{assessment.subject} Assessment</h1>
          <p className="text-gray-600">
            Question {assessment.currentQuestion + 1} of {assessment.questions.length}
          </p>
        </div>
        <Question
          question={currentQuestion}
          onAnswer={answerQuestion}
          showFeedback={showFeedback}
          isCorrect={isCorrect}
        />
      </div>
    </div>
  );
}

export default App;