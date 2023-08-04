
from tkinter import Canvas
from constants import *


class Scoreboard(Canvas):
    def __init__(self, root, canvas):
        super().__init__(canvas)
        self.score = 10
        self.root = root
        self.canvas = canvas

    def increase_score(self):
        self.score += 1

    def draw_scoreboard(self):
        self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,
                                anchor="nw", font=("Helvetica", 70),
                                text=self.score, fill="grey")

