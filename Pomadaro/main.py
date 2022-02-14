from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # * pink
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
    ''' Resets the timer to the original state. once reset button is pressed.'''
    window.after_cancel(timer)  # * cancels the timer
    timer_label.config(text='Timer', fg='GREEN')  # * resets the label
    canvas.itemconfig(timer_text, text='00:00')  # * resets the timer text
    check_label.config(text='')  # * resets the check mark
    global reps  # * resets the reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    ''' Starts the timer. when the start button is pressed.'''
    global reps  # * sets the reps to 0
    reps += 1  # * increments the reps

    work_sec = WORK_MIN * 60  # * sets the work time in seconds
    # * sets the short break time in seconds
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60  # * sets the long break time in seconds

    if reps % 8 == 0:
        #* if the reps is divisible by 8, it will be a long break
        countdown(long_break_sec)  # * starts the long break
        # * changes the label to break
        timer_label.config(text='Break', fg=RED)

    elif reps % 2 == 0:  # * if the reps is divisible by 2, it will be a short break
        countdown(short_break_sec)  # * starts the short break
        # * changes the label to break
        timer_label.config(text='Break', fg=PINK)
    else:
        #* if the reps is not divisible by 2 or 8, it will be a work session
        countdown(work_sec)  # * starts the work session
        # * changes the label to work
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    ''' Counts down the timer.'''
    global timer  # * sets the timer to global
    count_min = math.floor(count / 60)  # * sets the minutes
    count_sec = count % 60  # * sets the seconds
    if count_sec < 10:
        #* if the seconds are less than 10, it will add a 0 in front of it
        count_sec = f"0{count_sec}"
    # * changes the timer text to the minutes and seconds
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        #* if the count is greater than 0, it will continue to count down
        timer = window.after(1000, countdown, count - 1)
    else:
        #* if the count is 0, it will reset the timer and start the next session
        start_timer()

        mark = " "  # * sets the mark to nothing
        # * sets the work sessions to the reps divided by 2
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            #* for every work session, it will add a check mark
            mark += "✔"
        # * changes the check mark to green and adds the check mark
        check_label.config(text=mark, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # * creates the window
window.title('Pomodoro')  # * sets the title for the window
# * sets the padding and background color of the window
window.config(padx=100, pady=50, bg=YELLOW)

#* creates the canvas which will hold the image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#* creates the image which will be displayed on the canvas by reading the file
img = PhotoImage(file='tomato.png')

#* creates the image on the canvas and aligns it to the center
canvas.create_image(100, 112, image=img)

#* creates the timer text which will be displayed on the canvas and aligns it to the center
timer_text = canvas.create_text(100, 130, text='00:00', fill='white' font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)  # * places the canvas on the window using grid

#* creates the label which will be displayed on the window
timer_label = Label(text='Timer', font=(
    FONT_NAME, 50, 'normal'), fg=GREEN, bg=YELLOW)
# * places the label on the window using grid
timer_label.grid(row=0, column=1)

#* creates start button which will be displayed on the window
start_button = Button(text='Start', command=start_timer)
# * places the button on the window using grid
start_button.grid(row=2, column=0)


#* creates reset button which will be displayed on the window
reset_button = Button(text='Reset', command=reset_timer)
# * places the button on the window using grid
reset_button.grid(row=2, column=2)

check_mark = '✔'
#* creates the check mark label which will be displayed on the window
check_label = Label(fg=GREEN, bg=YELLOW)
# * places the label on the window using grid
check_label.grid(row=3, column=1)

window.mainloop()  # * starts the window
