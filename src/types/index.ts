export interface Question {
  id: number;
  text: string;
  options: string[];
  correctAnswer: number;
  difficulty: number;
}

export interface Assessment {
  subject: string;
  currentQuestion: number;
  score: number;
  difficulty: number;
  questions: Question[];
  answers: (number | null)[];
}