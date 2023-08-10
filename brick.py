from tkinter import Canvas
from constants import *


class Brick(Canvas):
    def __init__(self, canvas, x1, y1, x2, y2, fill):
        super().__init__(canvas)
        self.canvas = canvas
        self.fill = fill
        self.has_collided = False
        self.brick_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4,
                             COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]
        self.brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.fill)
        self.coords = [x1, y1, x2, y2]

    def destroy(self):
        self.canvas.delete(self.brick)


    def play_destroy_sound(self):
        pass


