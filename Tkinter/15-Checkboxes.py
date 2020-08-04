# ###### Checkboxes ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================
var = tk.IntVar()
# We have to choose the IntVar method for check box since by default if checkbox is ticked then it returns 1 otherwise it returns 0

check = tk.Checkbutton(root, text="Check Me Out!!!", variable=var)
check.pack()


def show():
    label = tk.Label(root, text=var.get()).pack()


button = tk.Button(root, text="Show Selection", command=show).pack()
# =================================
# ### Glitch program ###

var = tk.StringVar()

check = tk.Checkbutton(root, text="Check Me Out!!!", variable=var, onvalue="On", offvalue="Off")
check.pack()


def show():
    label = tk.Label(root, text=var.get()).pack()


button = tk.Button(root, text="Show Selection", command=show).pack()
# =================================
# ### Solution to glitch program ###

var = tk.StringVar()

check = tk.Checkbutton(root, text="Check Me Out!!!", variable=var, onvalue="On", offvalue="Off")
# deselect method will make the check deselect the checkbox by default

# ### deselect ###
check.deselect()

check.pack()


def show():
    label = tk.Label(root, text=var.get()).pack()


button = tk.Button(root, text="Show Selection", command=show).pack()
# =================================
root.mainloop()
