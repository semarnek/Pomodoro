import tkinter
from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 60 * 25
SHORT_BREAK_MIN = 60 * 5
LONG_BREAK_MIN = 60 * 25

reps = 0
timer = None
live_timer = 0



def reset_timer():
    global reps

    window.after_cancel(timer)
    title_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    check_mark.config(text="")
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    start_button.config(state=NORMAL)
    pause_button.config(state=DISABLED)
    continue_button.config(state=DISABLED)



def pause_timer():

    window.after_cancel(timer)
    pause_button.config(state=DISABLED)
    continue_button.config(state=NORMAL)



def continue_timer():
    global live_timer

    pause_button.config(state=NORMAL)
    continue_button.config(state=DISABLED)
    count_down(live_timer)


def start_timer():
    global reps

    reps += 1
    start_button.config(state=DISABLED)
    pause_button.config(state=NORMAL)
    continue_button.config(state=DISABLED)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break", fg=PINK)

    else:
        count_down(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)



def count_down(count):
    global reps
    global live_timer

    dakika = math.floor(count / 60)
    saniye = count % 60

    if saniye < 10:
        saniye = f"0{saniye}"

    if dakika < 10:
        dakika = f"0{dakika}"

    live_timer = count


    canvas.itemconfig(timer_text, text=f"{dakika}:{saniye}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # timerın sürekli yenilenmesi gerekiyor bunun için afterı kullanıyoruz. 1000 ms = 1 sn

    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark = mark + "✓"
        check_mark.config(text=f"{mark}")


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=1)


title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0, columnspan=2)

check_mark = Label(font=(FONT_NAME, 25, "bold"), fg=PINK, bg=YELLOW)
check_mark.grid(column=1, row=4, pady=50, columnspan=5)

start_button = Button(text="Start", bg=GREEN, font=(FONT_NAME, 15, "bold"), fg=WHITE, command=start_timer)
start_button.grid(column=0, row=1, padx=40)


reset_button = Button(text="Reset", bg=GREEN, font=(FONT_NAME, 15, "bold"), fg=WHITE, command=reset_timer)
reset_button.grid(column=4, row=1, padx=40)

pause_button = Button(text="Pause", bg=GREEN, font=(FONT_NAME, 15, "bold"), fg=WHITE, command=pause_timer, state=DISABLED)
pause_button.grid(column=1, row=2)

continue_button = Button(text="Continue", bg=GREEN, font=(FONT_NAME, 15, "bold"), fg=WHITE, command=continue_timer, state=DISABLED)
continue_button.grid(column=2, row=2)


canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(110, 100, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1, columnspan=2)


window.mainloop()