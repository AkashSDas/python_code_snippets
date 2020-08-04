# ###### Dropdown Menus ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================
var = tk.StringVar()
# =================================
# Since by default no value is selected in the dropdown menu we setting some value using thr set method
var.set("Monday")
# =================================
# ### OptionMenu ###

drop = tk.OptionMenu(root, var, "Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "Saturday", "Sunday")
# The second parameter is the variable in which we want to store the value which is selected in the drop down menu
# Here in our case it is "var"
drop.pack()


def show():
    label = tk.Label(root, text=var.get()).pack()


button = tk.Button(root, text="Show Selection", command=show).pack()
# ==================================
# If we have a lot of items then we will list

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "Saturday", "Sunday"]

var.set(options[0])
drop = tk.OptionMenu(root, var, *options)
drop.pack()


def show():
    label = tk.Label(root, text=var.get()).pack()


button = tk.Button(root, text="Show Selection", command=show).pack()
# ==================================
root.mainloop()
