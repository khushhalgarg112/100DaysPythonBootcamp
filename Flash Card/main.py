BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas as pd


curr = {}
try:
    french = pd.read_csv(
        "C:/Users/IT/Desktop/Python projects/Flash Card/data/words_to_learn.csv"
    )
except FileNotFoundError:
    new_french = pd.read_csv(
        "C:/Users/IT/Desktop/Python projects/Flash Card/data/french_words.csv"
    )
    data = new_french.to_dict(orient="records")
else:
    data = french.to_dict(orient="records")


def next_word():
    global curr, flip
    window.after_cancel(flip)
    curr = random.choice(data)
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr["French"], fill="black")
    flip = window.after(2000, func=change_to_eng)


def change_to_eng():
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr["English"], fill="white")


def is_known():
    data.remove(curr)
    word_to_learn = pd.DataFrame(data)
    word_to_learn.to_csv(
        "C:/Users/IT/Desktop/Python projects/Flash Card/data/words_to_learn.csv",
        index=False,
    )
    next_word()


window = Tk()
window.title("Flash Card")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

back_img = PhotoImage(
    file="C:/Users/IT/Desktop/Python projects/Flash Card/images/card_back.png"
)
front_img = PhotoImage(
    file="C:/Users/IT/Desktop/Python projects/Flash Card/images/card_front.png"
)
right = PhotoImage(
    file="C:/Users/IT/Desktop/Python projects/Flash Card/images/right.png"
)
wrong = PhotoImage(
    file="C:/Users/IT/Desktop/Python projects/Flash Card/images/wrong.png"
)


flip = window.after(2000, func=change_to_eng)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "normal"))
card_word = canvas.create_text(400, 250, text="", font=("Arial", 50, "bold"))

right_button = Button(
    image=right, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known
)
right_button.grid(row=1, column=0)

wrong_button = Button(
    image=wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=next_word
)
wrong_button.grid(row=1, column=1)

next_word()

window.mainloop()
