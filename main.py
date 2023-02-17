from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# for hex codes below . . . thank you colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
OLIVE = "#8B9A46"
#YELLOW = "#000000"     # this is black. needed to see the border!
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
POMODORO = "✓"

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro Technique")
window.config(padx=100, pady=50)  #gimme space around the window
window.config(bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0)  # hilitethickness to eliminate border line
canvas.config(bg=YELLOW)  # after the fact. if window bg is yellow, then this too!
img_tomato = PhotoImage(file="tomato.png")  # image it avail
canvas.create_image(100, 112, image=img_tomato)  #the x, the y (half the width and the height)
                                                 #then i pushed a little more than 100
                                                 #cause png was a little cut off.
canvas.create_text(100, 130, text="00:00", fill="white",         #fill is text color
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# row 0
lbl_timer = Label(text="Timer")
lbl_timer.config(font=(FONT_NAME, 35, "bold"))
lbl_timer.config(fg=GREEN)
lbl_timer.grid(row=0, column=1)

# row 2
but_start = Button(text="Start")
but_start.grid(row=2, column=0)
but_start.config(borderwidth=0)
but_start.config(font=("Arial", 15, "normal"))
but_start.config(bg=RED, fg="white")

but_pause = Button(text="Pause")
but_pause.grid(row=2, column=1)
but_pause.config(borderwidth=0)
but_pause.config(font=("Arial", 15, "normal"))
but_pause.config(bg=RED, fg="white")

but_reset = Button(text="Reset")
but_reset.grid(row=2, column=2)
but_reset.config(borderwidth=0)
but_reset.config(font=("Arial", 15, "normal"))
but_reset.config(bg=RED, fg="white")

# row 3
lbl_pomodoros = Label()
lbl_pomodoros.config(text=POMODORO)
lbl_pomodoros.config(font=(("Arial", 20, "bold")))
lbl_pomodoros.config(fg=OLIVE)
lbl_pomodoros.grid(row=3,column=1)



window.mainloop()