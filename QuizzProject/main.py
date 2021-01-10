from question_model import Question
from data import question_data
from quiz_brain import quizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_cuestion = Question(text,answer)
    question_bank.append(new_cuestion)

quiz = quizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()