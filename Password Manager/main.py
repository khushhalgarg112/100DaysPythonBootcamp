from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def genrate_password():
    a = " a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    letters = a.split(" ")
    b = "1 2 3 4 5 6 7 8 9 0"
    numbers = b.split(" ")
    c = "! @ # $ % ^ & * ( ) _"
    characters = c.split(" ")

    no_of_letter = 9
    no_of_number = 3
    no_of_characters = 3

    password_list = []
    for i in range(0, no_of_letter):
        password_list.append(random.choice(letters))

    for j in range(0, no_of_number):
        password_list.append(random.choice(numbers))

    for k in range(0, no_of_characters):
        password_list.append(random.choice(characters))

    random.shuffle(password_list)

    password = ""

    count = len(password_list)
    for x in range(0, count):
        password += password_list[x]
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web = web_entry.get()
    e = email_entry.get()
    p = pass_entry.get()
    data_entry = {
        web: {
            "email": e,
            "password": p,
        }
    }

    if email_entry.get() == "" or web_entry.get() == "" or pass_entry.get() == "":
        messagebox.showinfo(title="Details", message="Every field is mandatory")
    else:
        try:
            with open("data.json", mode="r") as f:
                read_data = json.load(f)  # Read the data
                read_data.update(data_entry)  # Update the data
            with open("data.json", mode="w") as f:
                json.dump(read_data, f, indent=4)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(data_entry, f, indent=4)
            # Add the data
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# window.minsize(width=200,height=200)


canvas = Canvas(width=200, height=200)
images = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=images)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=("Arial", 10, "bold"))
website.grid(row=1, column=0)

email = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email.grid(row=2, column=0)

password = Label(text="Password:", font=("Arial", 10, "bold"))
password.grid(row=3, column=0)

web_entry = Entry(width=51)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

genrate_pass = Button(text="Generate Password", command=genrate_password)
genrate_pass.grid(row=3, column=2)

add = Button(text="Add", width=44, command=save_password)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
