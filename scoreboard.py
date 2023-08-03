
from tkinter import Label

class Scoreboard(Label):
    def __init__(self, root):
        super().__init__()
        self.score = 0
        self.root = root
        self.label = Label(bg="white")

    def increase_score(self):
        self.score += 1







