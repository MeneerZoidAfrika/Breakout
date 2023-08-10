import tkinter as tk

from scoreboard import Scoreboard
from ball import Ball
from brick import Brick
from constants import *
from paddle import Paddle


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


###########################################################################

# Initializing GUI
root = tk.Tk()
root.title("Breakout Modernized")

root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# Setting the background of the Window
root.configure(bg="white")

# Setting the icon
root.iconbitmap("images/favicon.ico")

# Creating a canvas
canvas = tk.Canvas(
    root,
    width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
    bg=BACKGROUND_COLOR, highlightthickness=0,
    borderwidth=0, highlightbackground=BACKGROUND_COLOR
)
canvas.pack()

# Initializing Scoreboard
scoreboard = Scoreboard(root=root, canvas=canvas)
scoreboard.increase_score()
scoreboard.update_scoreboard()

# Creating Bricks
brick_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4,
                COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]
bricks = []

for i in range(12):
    x_increase = i * 99  # Separate variable for x_increase
    for j in range(8):
        y_increase = j * 35
        brick = Brick(canvas,
                      10 + x_increase, 25 + y_increase,
                      BRICK_WIDTH + x_increase, BRICK_HEIGHT + y_increase,
                      fill=brick_colors[::-1][j])
        bricks.append(brick)

# Creating the paddle in the middle
paddle = Paddle(canvas=canvas, root=root)


# Initializing Ball
ball = Ball(root=root, canvas=canvas, bricks=bricks)
ball.move_ball()


if __name__ == '__main__':
    center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
    root.mainloop()
