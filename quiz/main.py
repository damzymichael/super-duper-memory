from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# question_bank = []
# for question in question_data:
#     question_bank.append(Question(question["text"], question["answer"]))

# One liner replacement
question_bank = [Question(question["text"], question["answer"]) for question in question_data]

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")
