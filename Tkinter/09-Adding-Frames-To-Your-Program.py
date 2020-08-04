# ###### Adding Frames To Your Program ######

# =================================
# Importing module
import tkinter as tk
# =================================
# Configuring our window

root = tk.Tk()
root.title("Adding Frames To Your Program")
root.iconbitmap("icon_name.ico")
# =================================
# ### LabelFrame ###

# To create a new frame we use the LabelFrame method
frame = tk.LabelFrame(root, text="This is a frame...", padx=50, pady=50)
# Here the padding given effect the inside of the frame

frame.pack(padx=10, pady=10)
# This padding is outside the frame

# Note: With grid and pack, we cannot do them together but with frame this is not true
button_1 = tk.Button(frame, text="Don't Click Here!")
button_1.grid(row=0, column=0)
button_2 = tk.Button(frame, text="I'm Here!!!")
button_2.grid(row=1, column=1)
# =================================
# We can also remove the text parameter

new_frame = tk.LabelFrame(root, padx=50, pady=50)
new_frame.pack(padx=20, pady=20)

button_3 = tk.Button(new_frame, text="You are been seen!!")
button_3.grid(row=0, column=0)
# =================================
root.mainloop()
