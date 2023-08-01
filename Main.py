
import tkinter as tk
import time
import random


################################ FUNCTIONS ################################

def center_window(window, width, height):
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")






###########################################################################

# COLOR PALETTES
COLOR1 = "#2C3333"
COLOR2 = "#395B64"
COLOR3 = "#A5C9CA"
COLOR4 = "#E7F6F2"
COLOR5 = "#FF52A2"

COLOR_LEVEL1 = "#FFE5AD"
COLOR_LEVEL2 = "#3E001F"
COLOR_LEVEL3 = "#982176"
COLOR_LEVEL4 = "#F11A7B"
COLOR_LEVEL5 = "#FF5EAA"  # Bubblegum Pink
COLOR_LEVEL6 = "#FFCB47"  # Lemon Yellow
COLOR_LEVEL7 = "#5F9EA0"  # Cadet Blue
COLOR_LEVEL8 = "#E56B6F"  # Coral Red


# Initializing GUI
root = tk.Tk()
root.title("Breakout Modernized")

# Setting the Width + Height of the Window
window_height = 800
window_width = 1210
root.geometry(f"{window_width}x{window_height}")

# Setting the background of the Window
root.configure(bg=COLOR1)

# Setting the icon
root.iconbitmap("images/favicon.ico")

# Creating a canvas
canvas = tk.Canvas(root, width=window_width+50, height=window_height+50, bg=COLOR1, highlightthickness=0,
                   borderwidth=0, highlightbackground=COLOR1)
canvas.pack()

# Making a 12x12 grid of Rectangles with different colors
x_increase = 0
y_increase = 0
rect_colors = [COLOR_LEVEL1, COLOR_LEVEL2, COLOR_LEVEL3, COLOR_LEVEL4, COLOR_LEVEL5, COLOR_LEVEL6, COLOR_LEVEL7, COLOR_LEVEL8]

for i in range(12):
    x_increase = i * 100  # Separate variable for x_increase
    for j in range(8):
        y_increase = j * 35
        canvas.create_rectangle(10 + x_increase, 25 + y_increase, 100 + x_increase, 50 + y_increase, fill=rect_colors[::-1][j])

# Creating the paddle
paddle = canvas.create_rectangle(100, 200, 400, 300, fill="white")

if __name__ == '__main__':
    center_window(root, window_width, window_height)
    root.mainloop()












