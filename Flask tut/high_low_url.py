from flask import Flask
import random

app = Flask(__name__)

num = random.randint(1, 10)


def make_bold(func):
    def made():
        return f"<b>{func()}</b>"

    return made


def make_italic(func):
    def made():
        return f"<em>{func()}</em>"

    return made


def make_underline(func):
    def made():
        return f"<u>{func()}</u>"

    return made


@app.route("/")
@make_bold
@make_italic
@make_underline
def hi():
    return (
        "<h1>Guess the number</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='None'/>"
    )


@app.route("/<int:number>/")
def ans(number):
    if number < num:
        return (
            "<h1 style=' color: red'>Too Low</h1>"
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='None'/>"
        )

    elif number > num:
        return (
            "<h1 style=' color: purple'>Too High</h1>"
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='None'/>"
        )
    else:
        return (
            "<h1 style=' color: green'>Congrats, correct Number</h1>"
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='None'/>"
        )


if __name__ == "__main__":
    app.run(debug=True)


# class hi:

#     def __init__(self,name) :
#         self.name = name
#         self.is_login = False

# def login(function):
#     def wrapper(*args):
#         if args[0].is_login == True:
#             function(args[0])
#     return wrapper

# @login
# def cal(user):
#     print(f"HI {user.name}, how are you")

# user = hi("khushhal")
# user.is_login=True
# cal(user)
