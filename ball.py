from tkinter import Canvas
from constants import *


class Ball(Canvas):
    def __init__(self, canvas, root):
        super().__init__(canvas)
        self.canvas = canvas
        self.root = root
        self.x_vel = -3
        self.y_vel = -3

        self.ball = self.canvas.create_oval(
            WINDOW_WIDTH/2, WINDOW_HEIGHT/2,  # X, Y coordinates
            WINDOW_WIDTH/2 + BALL_SIZE, WINDOW_HEIGHT/2 + BALL_SIZE,   # X, Y coordinates
            fill="white"
        )

        self.coords = self.canvas.coords(self.ball)


    def move_ball(self):
        # print(self.canvas.coords(self.ball))
        self.coords = self.canvas.coords(self.ball)

        # Changing the X axis when touching the LEFT and RIGHT walls
        if self.coords[2] >= WINDOW_WIDTH or self.coords[0] <= 0:
            self.x_vel *= -1

        # Changing Y axis when touching TOP and BOTTOM walls
        if self.coords[1] <= 0 or self.coords[3] >= WINDOW_HEIGHT:
            self.y_vel *= -1


        self.canvas.move(
            self.ball,
            self.x_vel,
            self.y_vel
        )
        self.root.after(10, self.move_ball)


    def increase_velocity(self):
        """Increases the velocity of the ball as the user destroys more bricks"""

        # X Velocity
        if self.x_vel < 0:
            self.x_vel -= 0.2
        else:
            self.x_vel += 0.2

        # Y Velocity
        if self.y_vel < 0:
            self.y_vel -= 0.2
        else:
            self.y_vel += 0.2










