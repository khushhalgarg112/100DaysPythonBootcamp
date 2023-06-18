class Quiz:
    def __init__(self, question_list) :
        self.question_number =0
        self.question_list = question_list
        # self.a = ""
        self.score =0

    

    def input_answer(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        # self.a = input(f"Q{self.question_number}; {current_question} (True/False)? ")
        a = input(f"Q{self.question_number}; {current_question.q_text} (True/False)? ")
        self.check_answer(a,current_question.ans)

    def still_have_questions(self):
        length = len(self.question_list)
        if self.question_number < length:
            return True
        return False
        
    def check_answer(self,user_ans,current_ans):
            # if self.a == self.question_list[self.question_number-1].ans:
            #     print("Your Answer is right")
            #     self.score +=1
            #     print(f"Your score is {self.score}/{self.question_number}")
            # else:
            #     print("Your Answer is wrong")
            #     print(f"Your score is {self.score}/{self.question_number}")
            if user_ans == current_ans:
                print("Your Answer is right")
                self.score +=1
            else:
                print("Your Answer is wrong")
            print(f"Your score is {self.score}/{self.question_number}")
        
            