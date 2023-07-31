
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
window_width = 1280
root.geometry(f"{window_width}x{window_height}")

# Setting the background of the Window
root.configure(bg=COLOR1)

# Setting the icon
root.iconbitmap("images/favicon.ico")



if __name__ == '__main__':
    center_window(root, window_width, window_height)
    root.mainloop()












