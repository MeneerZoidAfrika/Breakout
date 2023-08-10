from tkinter import Canvas, font
from constants import *


class Scoreboard(Canvas):
    def __init__(self, root, canvas):
        super().__init__(canvas)  # Initialize as Label with canvas as master
        self.canvas = canvas
        self.score = 10
        self.root = root
        self.custom_font = font.Font(size=60)

        self.canvas.create_text(
            WINDOW_WIDTH/2 - 13,  # X coord
            WINDOW_HEIGHT/2,  # Y coord
            fill="gray",
            font=self.custom_font,
            text=str(self.score)
        )

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        """Updating the scoreboard"""
        self.root.after(100, self.update_scoreboard)
