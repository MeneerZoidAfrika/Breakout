from tkinter import Canvas
from constants import *


class Paddle(Canvas):
    def __init__(self, canvas, root):
        super().__init__(canvas)
        self.canvas = canvas
        self.root = root
        self.paddle = self.canvas.create_rectangle(
            WINDOW_WIDTH/2 - PADDLE_WIDTH/2, PADDLE_POS_FROM_TOP,  # X, Y coordinates
            WINDOW_WIDTH/2 + PADDLE_WIDTH/2, PADDLE_POS_FROM_TOP + PADDLE_HEIGHT,  # X, Y coordinates
            fill="white"
        )
        self.coords = self.canvas.coords(self.paddle)
        self.canvas.bind("<Motion>", self.move_paddle)  # Allowing the canvas to get the position of the mouse


    def move_paddle(self, event):
        """Moves the paddle in the x-axis relative to where the mouse is pointing"""

        """Tried simplifying the code with a simple return statement, but when the user swipes too fast and goes out of
        the window, the paddle freezes without reaching the end of the window. This method constantly places the paddle
        in the right spot even when the mouse is out of the window."""

        self.coords = self.canvas.coords(self.paddle)  # Updating the coordinates
        # print(self.coords)

        # When touching the LEFT wall
        if event.x < 0 + (PADDLE_WIDTH / 2):  # The mouse is 1/2 paddle widths away when the paddle touches the wall
            # print("Touches left")
            self.canvas.coords(
                self.paddle,
                0, PADDLE_POS_FROM_TOP,
                PADDLE_WIDTH, PADDLE_POS_FROM_TOP + PADDLE_HEIGHT
            )

        # When touching the RIGHT wall
        elif event.x > WINDOW_WIDTH - (PADDLE_WIDTH / 2):
            # print("Touches right")
            self.canvas.coords(
                self.paddle,
                (WINDOW_WIDTH - PADDLE_WIDTH), PADDLE_POS_FROM_TOP,
                WINDOW_WIDTH, (PADDLE_POS_FROM_TOP + PADDLE_HEIGHT)
            )

        # JESUS THIS TOOK ME SO LONG TO FIND THE FUCKING MISCALCULATION
        # Moving the Paddle in the x-axis
        else:
            self.canvas.coords(
                self.paddle,
                event.x - (PADDLE_WIDTH / 2), PADDLE_POS_FROM_TOP,  # Y stays constant,  X changes
                event.x + (PADDLE_WIDTH / 2), PADDLE_POS_FROM_TOP + PADDLE_HEIGHT
            )


