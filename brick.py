
from tkinter import Canvas


class Brick(Canvas):
    def __init__(self, root, color, row, column, canvas, x1, y1, x2, y2):
        super(Brick, self).__init__()
        self.root = root
        self.color = color
        self.row = row
        self.column = column
        self.canvas = canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.has_collided = False

