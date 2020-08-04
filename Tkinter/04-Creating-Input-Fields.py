# ###### Creating Input Fields ######

# =================================
# Importing tkinter module
import tkinter as tk
# =================================
# Creating root widget
root = tk.Tk()
# =================================
# ### Creating an Entry widget ###

entry = tk.Entry(root)
# Since we want our entry widget in root that why we pass root as first argument

entry.pack()
# =================================
# ### Adding additional parameters to our Entry method ###

# 1. width
entry = tk.Entry(root, width=50)
entry.pack()

# 2. fg and bg
entry = tk.Entry(root, width=50, fg="blue", bg="black")
entry.pack()

# 3. highlightbackground
entry = tk.Entry(root, width=50, fg="blue", highlightbackground="black")
entry.pack()

# 4. borderwidth
entry = tk.Entry(root, width=50, borderwidth=5)
entry.pack()
# =================================
# ### get ###

# This get method gets whatvere we have typed inside the input field

entry = tk.Entry(root, width=50)
entry.pack()

def my_click():
    my_label = tk.Label(root, text=entry.get())
    my_label.pack()

my_button = tk.Button(root, text="Enter Your Name", command=my_click)
my_button.pack()
# =================================
# ### insert ###

# insert method will put some default text inside the input field

entry = tk.Entry(root, width=50)
entry.pack()

entry.insert(0, "Enter Your Name")
# 0 is the index number

def my_click():
    my_label = tk.Label(root, text=f"Hello {entry.get()}")
    my_label.pack()

my_button = tk.Button(root, text="Sumbit", command=my_click)
my_button.pack()
# =================================
# ### Understanding insert method ###

# The statement "makes a default string appear" is not quite true. While it can be used to insert default text, it more correctly is described simply as inserting text, period. It can be default text, replacement text, additional text, whatever you want.

# Any index that is before the first character is treated as 0 (zero). Any index that is after the last character is treated as being the end. When you insert something into an entry widget that is empty, every index is treated as 0. Thus, the index is mostly useful for inserting text somewhere into existing text.

entry_exmaple = tk.Entry(root)
entry_exmaple.pack()

entry_exmaple.insert(0, "hello")
entry_exmaple.insert("end", "world")
entry_exmaple.insert(5, ", ")
# =================================

root.mainloop()
