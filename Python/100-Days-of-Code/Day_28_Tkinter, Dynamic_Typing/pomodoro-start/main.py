from tkinter import *
from time import sleep
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50, "bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50, "bold"))
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
label.grid(column=1, row=0)
check_marks = Label(text="✔", fg=GREEN, bg= YELLOW)
check_marks.grid(column=1,row=3)

# Button
start = Button(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", font=(FONT_NAME, 12, "normal"), command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
