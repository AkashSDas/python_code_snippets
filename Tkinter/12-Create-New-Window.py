# ###### Create New Window ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Message Boxes")
root.iconbitmap("icon_name.ico")
# =================================
# ### Toplevel ###

# Toplevel method will create a new window
top = tk.Toplevel()

# We are passing the "top" variable as new parameter which will will show the label in the new window
label = tk.Label(top, text="Hello There!!!").pack()

img = ImageTk.PhotoImage(Image.open("image_name.png"))
img_label = tk.Label(top, image=img).pack()

# We can also add title and root.title("Create New Window")
top.title("Image Window")
top.iconbitmap("icon_name.ico")
# =================================
# ### Controlling when new window should appear ###

# By default the new window appears as soon as we run the program
# To control when new window should appear we have to add some logic

def open():

    # If we don't set img variable to global then our image won't be shown in the new window when we click the button
    # Since img is a local to open fucntion that we created therefore we have to img variable as global
    global img

    # This is werid way doing thing since below specified variables are local to the function but still are working

    top = tk.Toplevel()
    label = tk.Label(top, text="Hello There!!!").pack()
    img = ImageTk.PhotoImage(Image.open("image_name.png"))
    img_label = tk.Label(top, image=img).pack()
    top.title("Image Window")
    top.iconbitmap("icon_name.ico")

    button_destroy = tk.Button(top, text="Close Window", command=top.destroy).pack()

tk.Button(root, text="Open New Window", command=open).pack()

# =================================
# Note: If some variables don't work in a program then try to make them global and see if it sloves the problem
# =================================
root.mainloop()
