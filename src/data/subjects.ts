export const subjects = ['mathematics', 'science'] as const;

export type Subject = typeof subjects[number];