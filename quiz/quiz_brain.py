class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0 
        self.question_list = question_list
    
    def next_question(self):
        self.question_number += 1
        current_question = self.question_list[self.question_number - 1]
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
 