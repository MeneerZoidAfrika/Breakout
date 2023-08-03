
import tkinter as tk
import time
import random
from ball import Ball
from scoreboard import Scoreboard
from constants import *


################################ FUNCTIONS ################################

def center_window(window, width, height):
    """Function to center the main window"""
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def get_shape_coordinates(shape):
    shape_coords = canvas.coords(shape)
    print(shape_coords)

    return shape_coords


def move_paddle(event):
    """Moves the paddle in the x-axis relative to where the mouse is pointing"""

    # Tried simplifying the code with a simple return statement, but when the user swipes too fast and goes out of
    # the window, the paddle freezes without reaching the end of the window. This method constantly places the paddle
    # in the right spot even when the mouse is out of the window.

    # paddle_coords = get_shape_coordinates(paddle)
    # When touching the LEFT wall
    if event.x < 0 + (PADDLE_WIDTH / 2):
        print("Touches left")
        canvas.coords(
            paddle,
            0, PADDLE_POS_FROM_TOP,
            PADDLE_WIDTH, (PADDLE_POS_FROM_TOP + PADDLE_HEIGHT)
        )

    # TODO fix this, still not working
    # When touching the RIGHT wall
    if event.x > WINDOW_WIDTH - (PADDLE_WIDTH / 2):  # The mouse is 1/2 paddle widths away when the paddle touches the wall
        print("Touches right")
        canvas.coords(
            paddle,
            (WINDOW_WIDTH - PADDLE_WIDTH), PADDLE_POS_FROM_TOP,
            WINDOW_WIDTH, (PADDLE_POS_FROM_TOP + PADDLE_HEIGHT)
        )


    # Moving the Paddle in the x-axis
    if not (event.x < 0 + PADDLE_WIDTH/2) or (event.x > WINDOW_WIDTH - PADDLE_WIDTH/2):
        canvas.coords(
            paddle,
            event.x - (PADDLE_WIDTH / 2), PADDLE_POS_FROM_TOP + (PADDLE_HEIGHT / 2),
            event.x + (PADDLE_WIDTH / 2), PADDLE_POS_FROM_TOP - (PADDLE_HEIGHT / 2)
        )


###########################################################################

# Initializing GUI
root = tk.Tk()
root.title("Breakout Modernized")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Setting the background of the Window
root.configure(bg=COLOR1)

# Setting the icon
root.iconbitmap("images/favicon.ico")


# Creating a canvas
canvas = tk.Canvas(root, width=WINDOW_WIDTH+100, height=WINDOW_HEIGHT+100, bg=COLOR1, highlightthickness=0,
                   borderwidth=0, highlightbackground=COLOR1)
canvas.bind("<Motion>", move_paddle)  # Allowing the canvas to get the position of the mouse
canvas.pack()

canvas.create_oval(100, 100, 100, 100, fill="white")

# Initializing Ball
ball = Ball(root=root, canvas=canvas)
ball.draw_ball()

# Initializing Scoreboard
scoreboard = Scoreboard(root)
scoreboard.increase_score()

# Making a 12x8 grid of Rectangles with different colors
rect_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4, COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]

x_increase = 0
y_increase = 0

for i in range(12):
    x_increase = i * 99  # Separate variable for x_increase
    for j in range(8):
        y_increase = j * 35
        canvas.create_rectangle(10 + x_increase, 25 + y_increase, BRICK_WIDTH + x_increase, BRICK_HEIGHT + y_increase, fill=rect_colors[::-1][j])

# Creating the paddle in the middle
paddle = canvas.create_rectangle(WINDOW_WIDTH/2 - PADDLE_WIDTH/2, PADDLE_POS_FROM_TOP,
                                 WINDOW_WIDTH/2 + PADDLE_WIDTH/2, PADDLE_POS_FROM_TOP + PADDLE_HEIGHT,
                                 fill="white")




if __name__ == '__main__':
    center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
    root.mainloop()












