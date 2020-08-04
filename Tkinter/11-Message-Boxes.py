# ###### Message Boxes ######

# =================================
# Importing module
import tkinter as tk

# Message box is just like a popup box
# To use message box we have to import messagebox from tkinter
from tkinter import messagebox
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================


def popup():
    messagebox.showinfo("This is my Popup!!", "Hello there!!!")
    # The first parameter of showinfo method is the title bar that we want to show and second parameter is the actual message in the popup

tk.Button(root, text="Popup", command=popup).pack()
# =================================
# ### Different types of message boxes ###

# 1. showinfo
# 2. showwarning
# 3. showerror
# 4. askquestion
# 5. askokcancel
# 6. askyesno
# =================================
# ###showinfo ###

def info():
    messagebox.showinfo("This info popup!!", "Info Popup")

tk.Button(root, text="info popup", command=info).pack()
# =================================
# ### showwarning ###

def info():
    messagebox.showwarning("This warning popup!!", "Warning Popup")

tk.Button(root, text="warning popup", command=info).pack()
# =================================
# ### showerror ###

def info():
    messagebox.showerror("This error popup!!", "Error Popup")

tk.Button(root, text="error popup", command=info).pack()
# =================================
# ### askquestion ###

def info():
    messagebox.askquestion("This askquestion popup!!", "Ask Question Popup")

tk.Button(root, text="askquestion popup", command=info).pack()
# =================================
# ### askokcancel ###

def info():
    messagebox.askokcancel("This askokcancel popup!!", "Ask Ok Cancel Popup")

tk.Button(root, text="askokcancel popup", command=info).pack()
# =================================
# ### askyesno ###

def info():
    messagebox.askyesno("This askyesno popup!!", "Ask Yes No Popup")

tk.Button(root, text="askyesno popup", command=info).pack()
# =================================
# ### Values returned when we response a popup ###

# showinfo
def info():
    response = messagebox.showinfo("This info popup!!", "Info Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="info popup", command=info).pack()

# showwarning
def info():
    response = messagebox.showwarning("This warning popup!!", "Warning Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="warning popup", command=info).pack()

# showerror
def info():
    response = messagebox.showerror("This error popup!!", "Error Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="error popup", command=info).pack()

# askquestion
def info():
    response = messagebox.askquestion("This askquestion popup!!", "Ask Question Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="askquestion popup", command=info).pack()

# askokcancel
def info():
    response = messagebox.askokcancel("This askokcancel popup!!", "Ask Ok Cancel Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="askokcancel popup", command=info).pack()

# askyesno
def info():
    response = messagebox.askyesno("This askyesno popup!!", "Ask Yes No Popup")
    tk.Label(root, text=response).pack()

tk.Button(root, text="askyesno popup", command=info).pack()
# =================================
# We can use these response to create more functionality to our program
# =================================
root.mainloop()
