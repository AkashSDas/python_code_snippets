# ###### import collections ######

# =================================
# ### Named Tuple ###

# ---------------------------------
from collections import namedtuple

# ---------------------------------
# namedtuple can be thought of light-weight object that work's like a regular tuple but is more readable
# namedtuple increases readability
# ---------------------------------
# Example: Say we want to write RGB color values

# ---------------------------------
# Using tuple

color = (55,155,255)
print(color[0]) 
# This is less readable
# ---------------------------------
# Using dictonary

dict_color = {'red':55, 'green':155, 'blue':255}
print(dict_color['red'])
# ---------------------------------
# Here there is alot of code and to add new color you have to again write alot of code
# ---------------------------------
# Using namedtuple

# Syntax used for namedtuple
Color = namedtuple('Color', ['red','green','blue']) 
# -----------------------------
# namedtuple is kind of compromise between tuple and dictonary,dictonary having functionality of tuple
# -----------------------------
color = Color(55,155,255) # Color is name of our namedtuple

print(color.red)

# Adding new color
white = Color(22,55,77)
print(white.blue)

# As we can see adding new colors is really easy
# -----------------------------
# We can also explictly name values to know what this values are 

color = Color(red=55,green=155,blue=255) 

print(color.red)

# Adding new color
white = Color(22,55,77)
print(white.blue)
