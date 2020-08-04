# ###### Open Files Dialog Box ######

# =================================
# Importing module
import tkinter as tk

# To open any file using tkinter we have to first import filedialog
from tkinter import filedialog
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================
# askopenfilename method won't open a file, it will just return the filenames and their locations
root.filename = filedialog.askopenfilename(initialdir="/Desktop/code_snippets/Python/Tkinter", title="Select a file", filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))

# In "initialdir" parameter we have to specify what in which directory we are searching
# "title" parameter will have the title of the box that will popup when we run askopenfilename method
# In "filetypes" parameter we specify what types of file to show
# Value passed to filetypes parameter is the tuple of tuples of value where the first value is the description which will come with the popup and second value is the type of file like .png, .py or even all files using regular expressions
# =================================
# Opening a file

root.filename = filedialog.askopenfilename(initialdir="/Desktop/code_snippets/Python/Tkinter", title="Images", filetypes=(("Images", "*.png"), ("Python Files", "*.py")))
label = tk.Label(root, text=root.filename).pack()
img = ImageTk.PhotoImage(Image.open(root.filename))
img_label = tk.Label(image=img).pack()
# =================================
# Our dialog box pop's up as soon as we run the program, it is not very helpful
# So we have to solve it


def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="/Desktop/code_snippets/Python/Tkinter", title="Images", filetypes=(("Images", "*.png"), ("Python Files", "*.py")))
    label = tk.Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = tk.Label(image=img).pack()


button = tk.Button(root, text="Open File", command=open).pack()
# =================================
root.mainloop()
