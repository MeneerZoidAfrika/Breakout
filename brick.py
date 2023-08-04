from tkinter import Canvas
from constants import *


class Brick(Canvas):
    def __init__(self, root, canvas):
        super().__init__()
        self.root = root
        self.canvas = canvas
        # self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.has_collided = False
        self.brick_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4,
                             COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]

    def draw_bricks(self):
        """Creating a 12x8 grid of Rectangles with different colors"""
        for i in range(12):
            x_increase = i * 99  # Separate variable for x_increase
            for j in range(8):
                y_increase = j * 35
                self.canvas.create_rectangle(10 + x_increase, 25 + y_increase,
                                             BRICK_WIDTH + x_increase, BRICK_HEIGHT + y_increase,
                                             fill=self.brick_colors[::-1][j])

    def destroy(self):
        self.has_collided = True
        self.config(highlightcolor=BACKGROUND_COLOR)

    def play_destroy_sound(self):
        pass
