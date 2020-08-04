# ###### Pillow Libary ######

# =================================
# Pillow libary is a powerful python libary for image manipulation
# =================================
import os

# To work with Pillow Libary importing from PIL
from PIL import Image
# =================================
# ### open ###

# Creating an image object
image1 = Image.open('image1.jpeg')
# =================================
# ### show ###

# Displaying the image using the show method
image1.show()
# =================================
# ### save ###

# To save that image as we are using the save method

# To save that image as .png
image1.save("image1.png")
# =================================
# ### Working with multiple images ###

# Working with multiple images is where pillow libary comes handy
# =================================
# Lets say we want to make multiple images to .png

for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        print(f)
        i = Image.open(f)
        file_name, file_extension = os.path.splitext(f)
        print(file_name, file_extension)
        i.save(f'{file_name}.png')
# =================================
# Resizing the images keeping the aspect ratio same so that our images don't get distorted

size_300 = (300, 300)
for f in os.listdir():
    if f.endswith('.jpeg'):
        i = Image.open(f)
        file_name, file_extension = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save(f'{file_name}.{file_extension}')
# =================================
# Resizing images to have multiple size images

size_300 = (300, 300)
size_700 = (700, 700)
for f in os.listdir():
    if f.endswith('.jpeg'):
        i = Image.open(f)
        file_name, file_extension = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save(f'{file_name}.{file_extension}')

        i.thumbnail(size_700)
        i.save(f'{file_name}.{file_extension}')
# =================================
# We can also rotate images, make them black and white, we can blur images and we can also do other things too
# =================================
image1 = Image.open('image1.jpeg')

# ---------------------------------
# ### rotate ###

# To rotate the image we are using the rotate method
image1.rotate(90).save('image1-mod.jpg')
# ---------------------------------
# ### convert ###

# To covert to black and white we are using the convert method with 'L' mode
image1.convert(mode='L').save('image1-mod.jpg')
# ---------------------------------
# ### To blur image ###

# For this we have to import ImageFilter from PIL
from PIL import ImageFilter

# We are doing a GaussianBlur

# This blur will be with default values since we haven't passed any value to the GaussianBlur method
image1.filter(ImageFilter.GaussianBlur()).save('image1-mod.jpg')

# To blur image with value of 15 we are passing 15 as value to the GaussianBlur method
image1.filter(ImageFilter.GaussianBlur(15)).save('image1-mod.jpg')
