from tkinter import Label
from tkinter import font
from constants import *


class Scoreboard(Label):
    def __init__(self, root, canvas):
        super().__init__()
        self.canvas = canvas
        self.score = 10
        self.root = root
        self.custom_font = font.Font(size=60)

        self.score_label = Label(self.canvas, text=str(self.score), bg=BACKGROUND_COLOR, font=self.custom_font,
                                 fg="gray")
        self.score_label.place(relx=0.5, rely=0.5, anchor="center")  # Position label at the center of the canvas

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        """Updating the scoreboard"""
        self.score_label = Label(self.canvas, text=str(self.score), bg=BACKGROUND_COLOR)
        self.root.after(100, self.update_scoreboard)
