from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_list = []

for items in question_data:
    obj = Question(items["text"],items["answer"])
    question_list.append(obj)

quiz_game = Quiz(question_list)

while quiz_game.still_have_questions():
    quiz_game.input_answer()

    
print("You have completed the quiz!")
print(f"Your's final score is {quiz_game.score}/{quiz_game.question_number}")