
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
rect_colors = [COLOR2, COLOR3, COLOR4, COLOR5]

for i in range(12):
    # if i > 3:
    #     color_choice = rect_colors[i-4]
    # else:
    #     color_choice = rect_colors[i]


    x_increase = i * 100 # Separate variable for x_increase
    for j in range(12):
        y_increase = j * 35
        canvas.create_rectangle(10 + x_increase, 25 + y_increase, 100 + x_increase, 50 + y_increase, fill=random.choice(rect_colors))



if __name__ == '__main__':
    center_window(root, window_width, window_height)
    root.mainloop()












