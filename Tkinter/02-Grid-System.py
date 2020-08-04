# ###### Grid System ######

# Positioning With Tkinter's Grid System
# =================================
# Importing tkinter module
import tkinter as tk
# =================================
# Creating root widget
root = tk.Tk()
# =================================
# Creating a Label

myLabel_1 = tk.Label(root, text="Hello World!")
myLabel_2 = tk.Label(root, text="Hello Universe!!!")
myLabel_3 = tk.Label(root, text="Hello Multiverse!!!!!!")
# =================================
# Since the pack method does not gives much control on how we position things on window therefore we use tkinter's grid system
# Tkinter's Grids have columns and rows as normal grids do

myLabel_1.grid(row=0, column=0)
myLabel_2.grid(row=1, column=0)
myLabel_3.grid(row=2, column=1)

# Inside parenthese we specify where we want our thing to be using the row and column parameter
# =================================
# If we resize our root window our labels will remain as it is, they won't resize themselves
# =================================
# These positions are relative to each other

myLabel_4 = tk.Label(root, text="Far beyond Reality")
myLabel_4.grid(row=100, column=100)

# Since there are no columns and rows in between 3 to 99 so tkinter ignores it
# =================================
# Creating an event loop
root.mainloop()
