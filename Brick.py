
import tkinter as tk
from tkinter import ttk


class Brick(tk.Canvas):
    def __init__(self, root, color, row, column, x1, y1, x2, y2):
        super(Brick, self).__init__()

        self.root = root
        self.color = color
        self.row = row
        self.column = column
        self.canvas = tk.Canvas(root, width=200, height=80)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.has_collided = False



