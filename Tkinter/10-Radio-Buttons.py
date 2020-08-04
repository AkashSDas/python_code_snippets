# ###### Radio Buttons ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Radio Buttons")
root.iconbitmap("icon_name.ico")
# =================================
# ### Tkinter Variables ###

# Tkinter has its own variables which are different from Python variables

var = tk.IntVar()
# Since we are passing integer as value we are using the IntVar method
# If we were passing string as value then we have to use the StringVar method

# This method(IntVar) allows Tkinter to keep track of changes over time for this variable and that's why we are using this instead of regular Python Variable
# =================================
# ### set ###

# Setting var variable to something
var.set("2")
# =================================


def clicked(value):
    label = tk.Label(root, text=value)
    label.pack()


radio_button_1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=lambda: clicked(var.get()))
radio_button_1.pack()
# We are assigning variable to each radio button so that if someone clicks on button then that value can be put on the variable assigned to it and then we can do different things with that
# The "variable" parameter holds the variable in which we want to store the value which is assigned to the "value" parameter in that variable

radio_button_2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=lambda: clicked(var.get()))
radio_button_2.pack()

button = tk.Button(root, text="Click Me!!", command=lambda: clicked(var.get())).pack()
# =================================
# ### Efficient Way of woking with buttons ###

pizza = tk.StringVar()
pizza.set("Pepperoni")

# If we have many buttons

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

for text, mode in MODES:
    tk.Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=tk.W)


def pizza_click(value):
    label = tk.Label(root, text=value)
    label.pack()


pizza_button = tk.Button(root, text="Which Pizza???", command=lambda: pizza_click(pizza.get())).pack()
# =================================
root.mainloop()
