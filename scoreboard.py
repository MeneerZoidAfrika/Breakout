from tkinter import Label
from constants import *


class Scoreboard(Label):
    def __init__(self, root):
        super().__init__(root)
        self.score = 10
        self.root = root
        self.score_label = Label(font=("Helvetica", 70), text=self.score)

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        """Updating the scoreboard"""
        self.score_label.pack()
