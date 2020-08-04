# ###### Using Icons, Images and Exit Buttons ######

# =================================
# Importing modules
import tkinter as tk
from PIL import ImageTk, Image
# =================================
root = tk.Tk()
root.title("Using Icons, Images and Exit Buttons")
# =================================
# ### iconbitmap ###

# To add icons to our windows we use the iconbitmap
root.iconbitmap("icon_name.ico")
# =================================
# Adding Images

my_image = ImageTk.PhotoImage(Image.open("image_name.png"))
my_label = tk.Label(image=my_image)
my_label.pack()
# =================================
# ### quit ###

# Creating an Exit Button
exit_button = tk.Button(root, text="Exit Program", command=root.quit)

# The quit attribute stops the mainloop which in turn stops our program

exit_button.pack()
# =================================
root.mainloop()
