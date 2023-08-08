
from tkinter import Canvas
from constants import *



class Scoreboard(Canvas):
    def __init__(self, root, canvas):
        super().__init__()
        self.score = 10
        self.root = root
        self.canvas = canvas

    def increase_score(self):
        self.score += 1

    def draw_scoreboard(self):
        """Displaying the scoreboard"""

        self.canvas.create_text(WINDOW_WIDTH/2 - 60, WINDOW_HEIGHT/2,  # had to play around with the X&Y
                                anchor="nw", font=("Helvetica", 70),
                                text=self.score, fill="grey")

