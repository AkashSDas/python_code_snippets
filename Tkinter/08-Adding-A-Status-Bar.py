# ###### Adding A Status Bar ######

# =================================
# Importing modules
import tkinter as tk
from PIL import ImageTk, Image
# =================================
# Configuring our window

root = tk.Tk()
root.title("Image Viewer App")
root.iconbitmap("icon_name.ico")
# =================================
# Images

my_img_1 = ImageTk.PhotoImage(Image.open("image_1_name.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("image_2_name.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("image_3_name.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("image_4_name.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("image_5_name.png"))

image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]
# =================================
# ### relief and anchor ###

status = tk.Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=tk.SUNKEN, anchor=tk.E)

# bd parameter add a border
# The relief parameter of a widget refers to certain simulated 3-D effects around the outside of the widget
# relief=tk.SUNKEN will make the our label look a sunken
# To shift our label we can use the anchor parameter
# =================================
# ### sticky ###

status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)
# To strech our label we have to add "sticky" parameter to the grid method
# grid and pack method have a navigational system and it is based on compass system where N(North), S(South), W(West) and E(East)
# =================================
my_label = tk.Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)
# =================================
# Button functionalities


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = tk.Label(image=image_list[image_number - 1])
    button_forward = tk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = tk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = tk.Button(root, text=">>", state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = tk.Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = tk.Label(image=image_list[image_number - 1])
    button_forward = tk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = tk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = tk.Button(root, text="<<", state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = tk.Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=tk.SUNKEN, anchor=tk.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


# =================================
# Putting button on screen

button_back = tk.Button(root, text="<<", command=back, state=tk.DISABLED)
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
# =================================
root.mainloop()
