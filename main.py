from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#519259"
YELLOW = "#FFEBCC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        mark_sessions = math.floor(reps//2)
        for _ in range(mark_sessions):
            marks += "✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# timer_canvas = Canvas(width=200, height=130, bg=YELLOW, highlightthickness=0)
# timer_canvas.create_text(100, 65, text="Timer", fill=GREEN, font=("Solomon Sans", 45, "bold"))
# timer_canvas.grid(column=1, row=0)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# check_mark = Canvas(width=20, height=20, bg=YELLOW, highlightthickness=0)
# check_mark.create_text(10, 10, text="✔", fill=GREEN, font=("Solomon Sans", 15, "bold"))
# check_mark.grid(column=1, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

window.mainloop()
