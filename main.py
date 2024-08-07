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
reps = 0  # Track the number of repetitions
timer = None  # Store the timer reference


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """
      Reset the timer to its initial state.
      """
    window.after_cancel(timer)  # Cancel the running timer
    title_label.config(text="Timer")  # Reset the title
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text
    check_mark.config(text="")  # Clear the check marks
    global reps
    reps = 0  # Reset the repetition count
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """
    Start the timer and update the UI based on the current session (work/break).
    """
    global reps
    reps += 1
    if reps % 8 == 0:  # Every 8th repetition is a short break
        title_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 0:  # Every 2nd repetition is a long break
        title_label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    else:  # Otherwise, it's a work session
        title_label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """ Perform the countdown and update the timer text. """
    count_min = math.floor(count / 60)  # Calculate minutes
    count_sec = count % 60  # Calculate seconds
    if count_sec < 10:  # Add a leading zero if seconds are less than 10
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update the timer display
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""  # Start the next session
        work_session = math.floor(reps/2)  # Calculate the number of work sessions completed
        for _ in range(work_session):
            marks += "✔"  # Add check marks for each completed work session
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Load the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Place the tomato image on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0,
                      command=reset_timer)
reset_button.grid(column=2, row=3)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

window.mainloop()  # Run the Tkinter event loop
