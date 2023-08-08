from tkinter import Canvas
from constants import *


class Ball(Canvas):
    def __init__(self, canvas, root):
        super().__init__()
        self.canvas = canvas
        self.root = root
        self.x_vel = -10
        self.y_vel = 10
        self.ball_size = BALL_SIZE

        self.ball = self.create_oval(
            WINDOW_WIDTH/2,  # X coordinate
            WINDOW_HEIGHT/2,  # Y coordinate
            WINDOW_WIDTH/2 + BALL_SIZE,   # X coordinate + BALL_SIZE
            WINDOW_HEIGHT/2 + BALL_SIZE,  # Y coordinate + BALL_SIZE
            fill="red"
        )

    def move_ball(self):
        self.canvas.move(
            self.ball,
            self.x_vel,
            self.y_vel
        )
        self.root.after(10, self.move_ball)

    def wall_bounce(self):
        """Changes the direction the ball is going when colliding with a Wall"""
        pass

    def brick_bounce(self):
        """Changes direction of the ball when colliding with a Brick"""
        pass

    def increase_velocity(self):
        """Increases the velocity of the ball as the user destroys more bricks"""
        pass







