import math
import sys
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 1
# SHORT_BREAK_MIN = 5
SHORT_BREAK_MIN = 2
# LONG_BREAK_MIN = 20
LONG_BREAK_MIN = 3
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        print(count_down)
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
        timer_label.grid(column=1, row=0)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 45))
        timer_label.grid(column=1, row=0)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 45))
        timer_label.grid(column=1, row=0)
    else:
        sys.exit()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # adds additional check marks to the check mark label
        add_check = ""
        work_sessions = math.floor(reps / 2)
        for n in range(work_sessions):
            add_check += "✔"
        check_mark.config(text=add_check)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
timer_label.grid(column=1, row=0)

check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
