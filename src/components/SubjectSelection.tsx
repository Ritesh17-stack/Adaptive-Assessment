import React from 'react';
import { BookOpen } from 'lucide-react';
import { subjects } from '../data/subjects';

interface SubjectSelectionProps {
  onSelectSubject: (subject: string) => void;
}

export const SubjectSelection: React.FC<SubjectSelectionProps> = ({ onSelectSubject }) => {
  return (
    <div className="space-y-6">
      <div className="text-center">
        <BookOpen className="w-12 h-12 mx-auto text-blue-600" />
        <h2 className="mt-4 text-2xl font-bold text-gray-900">Select a Subject</h2>
        <p className="mt-2 text-gray-600">Choose a subject to begin your adaptive assessment</p>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        {subjects.map((subject) => (
          <button
            key={subject}
            onClick={() => onSelectSubject(subject)}
            className="p-6 text-left transition-all bg-white rounded-lg shadow-md hover:shadow-lg"
          >
            <h3 className="text-lg font-semibold text-gray-900 capitalize">{subject}</h3>
            <p className="mt-2 text-sm text-gray-600">
              Take an adaptive assessment in {subject}
            </p>
          </button>
        ))}
      </div>
    </div>
  );
};