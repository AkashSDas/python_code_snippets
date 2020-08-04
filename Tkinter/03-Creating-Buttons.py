# ###### Creating Buttons ######

# =================================
# Importing tkinter module
import tkinter as tk
# =================================
# Creating root widget
root = tk.Tk()
# =================================
# ### Creating a button ###

my_button = tk.Button(root, text="Click Me")
my_button.pack()
# =================================
# ### state ###

disabled_button = tk.Button(root, text="You Can't Click Me", state=tk.DISABLED)
disabled_button.pack()
# =================================
# ### Changing size of our button ###

sized_button = tk.Button(root, text="Don't Click Me", padx=50)
sized_button.pack()

sized_button = tk.Button(root, text="Don't Click Me", pady=50)
sized_button.pack()

sized_button = tk.Button(root, text="Don't Click Me", padx=50, pady=50)
sized_button.pack()
# =================================
# ### Make button do something ###

# To make a button do something when we click it we have to first make a function and put thing that we want to be done when we click the button then we have to put that function equal to command parameter


def my_click():
    my_label = tk.Label(root, text="Look! Who clicked me")
    my_label.pack()


# To make button do something after it's clicked we have to put our function equal to command parameter of Button method

# Note: If we put parenthese then our button won't do things specified in function that we created i.e. button won't be functional
my_button = tk.Button(root, text="Functional Button", command=my_click)
my_button.pack()

my_button = tk.Button(root, text="Non Functional Button", command=my_click())
my_button.pack()
# =================================
# ### Customizing our button ###

# 1. fg parameter changes font color
my_button = tk.Button(root, text="Hit me as hard as you can!!!", command=my_click, fg="blue")
my_button.pack()

# 2. bg parameter changes background color of the button
my_button = tk.Button(root, text="Hit me as hard as you can!!!", command=my_click, fg="blue", bg="#000000")
my_button.pack()

# We can also use hex-colors

# On Mac button can't be colored i.e. bg parameter has no effects
# To avoid this issue use the highlightbackground parameter
my_button = tk.Button(root, text="Hit me as hard as you can!!!", command=my_click, highlightbackground="#000000")
my_button.pack()
# =================================

root.mainloop()
