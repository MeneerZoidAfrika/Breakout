from tkinter import Canvas
import random
import time
from constants import *


class Ball(Canvas):
    def __init__(self, canvas, root):
        super().__init__(canvas, bg="white", highlightthickness=1)
        self.canvas = canvas
        self.root = root
        self.vel = 100
        self.ball_size = 10

        self.starting_x = WINDOW_WIDTH / 2
        self.starting_y = WINDOW_HEIGHT / 2
        self.ball = self.create_oval(self.starting_x, self.starting_y, self.starting_x+10, self.starting_y+10, fill="white")

    def draw_ball(self):
        self.create_oval(self.starting_x, self.starting_y, self.starting_x+BALL_SIZE, self.starting_y+BALL_SIZE, fill="white")
        self.starting_x -= 10
        self.canvas.coords(self.ball,
                           self.starting_x, self.starting_y,
                           self.starting_x + self.vel, self.starting_y + self.vel)

        self.root.after(10, self.draw_ball)

    def bounce(self):
        """Changes the direction the ball is going when colliding with a Brick or Wall"""
        pass

    def increase_velocity(self):
        """Increases the velocity of the ball as the user destroys more bricks"""
        pass







