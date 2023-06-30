from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Interface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quiz App")
        # self.window.minsize(width=400,height=700)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score = Label(text=f"Score: 0",font=('bold'), bg=THEME_COLOR, fg="white")
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Questions",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
            )
        self.canvas.grid(row=1,column=0,columnspan=2, pady=20)

        right_image = PhotoImage(file="C:/Users/IT/Desktop/Python projects/Quiz GUI/images/true.png")
        wrong_image = PhotoImage(file="C:/Users/IT/Desktop/Python projects/Quiz GUI/images/false.png")

        self.right_button = Button(image=right_image, highlightthickness=0,command=self.right) 
        self.right_button.grid(row=2,column=0)

        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2,column=1)

        self.get_question() 

        self.window.mainloop()


    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():  
            self.score.config(text=f"Score: {self.quiz.score}")
            next_question= self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=next_question)
        else:
            self.canvas.itemconfig(self.question, text="You have completed the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_question)
       