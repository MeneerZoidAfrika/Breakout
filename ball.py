from tkinter import Canvas
from constants import *


class Ball(Canvas):
    def __init__(self, canvas, root, bricks):
        super().__init__(canvas)
        self.canvas = canvas
        self.root = root
        self.x_vel = -2
        self.y_vel = 0

        self.ball = self.canvas.create_oval(
            WINDOW_WIDTH/2, WINDOW_HEIGHT/2,  # X, Y coordinates
            WINDOW_WIDTH/2 + BALL_SIZE, WINDOW_HEIGHT/2 + BALL_SIZE,   # X, Y coordinates
            fill="white"
        )



    def move_ball(self):
        print(self.canvas.coords(self.ball))
        coordinates = self.canvas.coords(self.ball)

        # Changing the X axis when touching the wall
        if coordinates[2] >= WINDOW_WIDTH or coordinates[0] <= 0:
            self.x_vel *= -1
            self.y_vel *= -1

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







