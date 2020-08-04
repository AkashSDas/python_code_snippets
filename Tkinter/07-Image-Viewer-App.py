# ###### Image Viewer App ######

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

my_label = tk.Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)
# =================================
# To go forward we create a foward function


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # grid_forget method will delelte our label from the screen
    my_label.grid_forget()

    # After deleting the image we have to add the next image to the screen
    my_label = tk.Label(image=image_list[image_number - 1])
    button_forward = tk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = tk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = tk.Button(root, text=">>", state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


# To go backward we create a back function
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

# =================================
# Our buttons

# Since the first time we will be at the first image so we cannot go backward therefore we are just passing function directly without arguments
button_back = tk.Button(root, text="<<", command=back, state=tk.DISABLED)
button_exit = tk.Button(root, text="Exit Program", command=root.quit)
button_forward = tk.Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
# =================================
root.mainloop()
