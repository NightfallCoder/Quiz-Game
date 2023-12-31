from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(que_text=question_text,que_answer=question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")