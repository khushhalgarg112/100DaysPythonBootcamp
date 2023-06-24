from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(clock_text,text="00:00")
    tick.config(text="")
    title.config(text="Timer")
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    global rep
    rep +=1
    work_sec = WORK_MIN*60
    short_sec = SHORT_BREAK_MIN*60
    long_sec = LONG_BREAK_MIN*60
    if rep %8 ==0:
        count_down(long_sec)
        title.config(fg=RED, text="Break")
    elif rep %2 ==0:
        count_down(short_sec)
        title.config(fg=PINK, text="Break")
    else:
        count_down(work_sec)
        title.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer 
    minutes = math.floor(count/60)
    seconds = count % 60
    if count < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(clock_text,text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_time()
        marks =""
        work_check = math.floor(rep/2)
        for _ in range(work_check):
            marks += "✔"
        tick.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window  = Tk()
window.config(padx=50,pady=20,bg=YELLOW)
window.title("Pomodoro GUI")

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME,40,'bold'),bg=YELLOW)
title.grid(row=0,column=1)

canvas  = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
clock_text = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME, 30,'bold' ))
canvas.grid(row=1,column=1)

start = Button(text="Start",width=6, command=start_time)
start.grid(row=2,column=0)

reset = Button(text="Reset",width=6, command=reset)
reset.grid(row=2,column=2)

tick = Label(text="", fg=GREEN, bg=YELLOW)
tick.grid(row=3,column=1)

window.mainloop()