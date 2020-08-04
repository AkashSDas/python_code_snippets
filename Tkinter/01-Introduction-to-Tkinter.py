# ###### Introduction to Tkinter ######

# =================================
# Importing tkinter module
import tkinter as tk
# =================================
# In tkinter everything is widget like button widget, text widget, frame widget, etc

# The first widget that we create is sort of root widget (it is window or main frame for GUI)
root = tk.Tk()
# =================================
# ### Process ###

# To create anything in tkinter is a two step process:
#   1. Define the thing i.e. create it
#   2. Put that thing onto the screen
# =================================
# ### Label ###

# 1. Step 1
# Creating a Label Widget
myLabel = tk.Label(root, text="Hello World!")
# Since we want our Label widget to go our root widget therefore we pass first parameter as root

# 2. Step 2
# Placing our Label widget onto the root widget
myLabel.pack()

# There different way of putting something onto the screen with tkinter
# pack method is one of the way
# It put our thing into the first available space, it will be of the size it is
# =================================
# Creating an Event Loop
root.mainloop()

# When we have GUI it is constantly looping and that's how it figures out what's going on. One of the example is when we use mouse the GUI knows the the mouse is going, it's due to continues looping. Normally when the program end that time that loop ends.
# When we close the tkinter application program thats when the mainloop is terminated
# A Tkinter application runs most of its time inside an event loop, which is entered via the mainloop method. It waiting for events to happen. Events can be key presses or mouse operations by the user. Tkinter provides a mechanism to let the programmer deal with events.
