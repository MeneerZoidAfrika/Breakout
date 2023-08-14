import tkinter as tk

from scoreboard import Scoreboard
from ball import Ball
from brick import Brick
from constants import *
from paddle import Paddle


def center_window(window, width, height):
    """Function to center the main window"""
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def check_collisions():
    global bricks
    game_over = False

    # Collision Detection
    paddle_x1 = paddle.coords[0]
    paddle_y1 = paddle.coords[1]
    paddle_x2 = paddle.coords[2]
    paddle_y2 = paddle.coords[3]

    if not ball.coords:
        game_over = True

    if not game_over:
        ball_x1 = ball.coords[0]
        ball_y1 = ball.coords[1]
        ball_x2 = ball.coords[2]
        ball_y2 = ball.coords[3]

        # Ball and Brick collision
        for brick in bricks:
            brick_x1 = brick.coords[0]
            brick_y1 = brick.coords[1]
            brick_x2 = brick.coords[2]
            brick_y2 = brick.coords[3]

            if (brick_x1 <= ball_x1 <= brick_x2) and (ball_y1 <= brick_y2+5):
                print("Brick destroyed")
                brick.destroy()
                bricks.remove(brick)
                ball.y_vel *= -1

                scoreboard.increase_score()
                ball.increase_velocity()

        # Bouncing the Ball off of the Paddle
        if (paddle_x1 <= ball_x2 <= paddle_x2) and (paddle_y1 <= ball_y2 <= paddle_y2):
            print("Ball bounce")
            ball.y_vel *= -1

        # Going past the paddle means Game Over
        if ball_y2 >= paddle_y2:
            print("Game over")
            ball.destroy()
            scoreboard.game_over()



def main_loop():
    check_collisions()

    scoreboard.update_scoreboard()

    canvas.after(20, main_loop)

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

# Creating Bricks
brick_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4,
                COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]
bricks = []

for i in range(12):
    x_increase = i * 99  # Separate variable for x_increase
    for j in range(8):
        y_increase = j * 35
        brick = Brick(canvas,
                      (10 + x_increase), (25 + y_increase),  # X, Y Coordinates
                      BRICK_WIDTH + x_increase, BRICK_HEIGHT + y_increase,  # X, Y Coordinates
                      fill=brick_colors[::-1][j])
        bricks.append(brick)

# Creating the Paddle in the middle
paddle = Paddle(canvas=canvas, root=root)

# Initializing Ball
ball = Ball(root=root, canvas=canvas)
ball.move_ball()


if __name__ == '__main__':
    center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
    root.after(150, main_loop)
    root.mainloop()
