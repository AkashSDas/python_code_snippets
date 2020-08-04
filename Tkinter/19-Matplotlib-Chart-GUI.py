# ###### Matplotlib Chart GUI ######

# =================================
# Importing modules
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
# =================================
# Configuring our window

root = tk.Tk()
root.title("Matplotlib Chart GUI")
root.geometry("120x50")
# =================================


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, bins=200)
    plt.show()


button = tk.Button(root, text="Show the graph", command=graph)
button.pack()
# =================================
root.mainloop()
