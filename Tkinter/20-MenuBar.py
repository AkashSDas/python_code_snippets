# ###### MenuBar ###

# =================================
from tkinter import *

# Normal Cofiguration
root = Tk()
root.title('MenuBar in MunniBar')
root.geometry('500x500')

# Creating a menubar instance
menubar = Menu(root)

# Adding that menubar instance to our root window using the config method
root.config(menu=menubar)

# Creating a filemenu instance where all our menu items will be shown
filemenu = Menu(menubar)

# Our first menu item is --> File
# Adding that menu item to our menubar using the add_cascade method
menubar.add_cascade(label="File", menu=filemenu)
# In parameter menu we are specifing filemenu that is where our menu item will be displayed

# Adding options which will be displayed when menu item File is clicked
filemenu.add_command(label="New")
filemenu.add_command(label="Open")

# Adding a line to separate above and below content
filemenu.add_separator()

# command parameter specifies what will happen when we click that option in menu item
filemenu.add_command(label="Exit", command=root.quit)

# quit will quit the window, root.quit will quit the root window

# Creating another menu item
menubar.add_cascade(label="Help", menu=filemenu)

# Our event loop
root.mainloop()
