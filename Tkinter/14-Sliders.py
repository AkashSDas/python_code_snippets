# ###### Sliders ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================
# ### geometry ###

# We can designate how big our window should be
root.geometry("400x400")
# =================================
# ### Scale ###

vertical = tk.Scale(root, from_=0, to=400)
vertical.pack()

# In "from_" parameter we have to specify from where the slide is starting
# In "to" parameter we have to specify upto which range our slider can slide

# Note: We should not do this --> vertical = tk.Scale(root, from_=0, to=200).pack()
# =================================
# ### Horizontal Slider ###

horizontal = tk.Scale(root, from_=0, to=400, orient=tk.HORIZONTAL)
horizontal.pack()

# Slider are by default vertical

# Slider method returns a number whenever we slide the silde and that number is the current location of that silder
# =================================


def slide():
    label = tk.Label(root, text=horizontal.get()).pack()
    root.geometry(f"{vertical.get()}x{horizontal.get()}")


button = tk.Button(root, text=f"Click Me!!!", command=slide).pack()
# =================================
# Updating geometry while slide is slided


def update(var):
    label = tk.Label(root, text=horizontal.get()).pack()
    root.geometry(f"{vertical.get()}x{another_horizontal.get()}")


# We have to explicitly assign an argument to update method without that our update function won't work
another_horizontal = tk.Scale(root, from_=0, to=400, orient=tk.HORIZONTAL, command=update)
another_horizontal.pack()

button_another = tk.Button(root, text=f"Click Me!!!", command=update).pack()
# =================================
root.mainloop()
