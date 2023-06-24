from tkinter import *

element = Tk()
element.title("Converter")
element.minsize(250, 150)
element.config(padx=30, pady=30)


"""def clicked():
    my_label["text"] = inputs.get()


my_label = Label(text="Helo Everyone")
my_label.grid(column=0, row=0)  # we don't pack and place when using grid
# my_label.place(x=30, y=70)    gives the position whereever we want
# my_label.pack(side="left")
# my_label.config(text = "hiiii")

inputs = Entry(width=10)
inputs.grid(column=1, row=1)

my_button = Button(text="Click me", command=clicked)
my_button.grid(column=2, row=2)"""

# Add as many argumrnts you want
"""
def argument(*args):  #Type of this argument is of a tuple and this * operator help ot collect unlimited
    count = 0         # Positional arguments
    for n in args:
        count += n
    print(f"Sum is {count}")
argument(1,2,3,4,5,6,7,8,9,10)
"""
#  Add as many keyword arguments

"""def keyargu(**kw):   #Type og thsi is a dictoniary 
    # print(kw.student)     we dont call it like this beacuse this is not an object
    # print(kw["classes"])
    # print(kw.get("marks"))  This is not giving key error beacuse using get it return none 
    # print(kw["roll no"]) This gives key error because we don't define roll no


keyargu(student="Henry", classes="Data Science" )
"""

# checkbox in python
"""def chechbtn():
    print(checkstate.get())

checkstate = IntVar()
check = Checkbutton(text="Is on?", variable=checkstate, command=chechbtn)
check.pack()
"""


def convert():
    ans["text"] = int(inputs.get()) * 1.609


inputs = Entry(width=15)
inputs.grid(column=1, row=0)

miles = Label(text="miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

ans = Label(text="0")
ans.grid(column=1, row=1)

kms = Label(text="Km")
kms.grid(column=2, row=1)

btn = Button(text="Convert", command=convert)
btn.grid(column=1, row=2)


element.mainloop()
