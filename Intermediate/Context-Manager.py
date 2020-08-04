# ###### Context Manager ######

# =================================
# Context manager allows us to properly manage rescources so that we can specify exactly what we want to setup and teardown when working with certain objects
# =================================
# ### Woking with file objects ###
# =================================
# ### Without context manager working with file object ###

f = open("file.txt", "w")
f.write("Hello World")
f.close()

# Using the context manager
with open("file.txt", "w") as f:
    f.write("Hello World")

# Using a context manager we no longer have to close the file once we are done with working with the file object

# Also if we throw an error when working with this file then too the file will be closed properly.
# That is why context manager are so useful since it handels the teardown of the resources for us so that we don't have to remmember to do it, the more that is handel for us automatically the better
# =================================
# Context manager is great for working with file object but it is also useful for so many different resources
#   1.  We use this to connect to and close the database connections automatically
#   2.  We can aquire and release locks
#   etc.
# =================================
# ### Creating our own context manager ###
# =================================
# ### Creating our own context manager using a class ###

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()
        # The extra parameter in the exit method are there so that if we throw an exception we can use that to excess those information

with Open_File("file.txt", "w") as f:
    f.write("Testing")

# To check that the file was closed outside the context manager
print(f.closed)

# Understanding whats going on
# 1. Since we are using --> Open_File("file.txt", "w") --> it comes to the __init__ method and sets the attributes
# 2. Since we are using --> with statment --> with Open_File("file.txt", "w") --> it enters the __enter__ method and open's the file if exits otherwise it creates that file and that file is returned and our --> f --> variable is set to that file object that we have returned in the __enter__ method
# 3. Now in the context manager we can work with the file object
# 4. When we exit the context manager block that is when the __exit__ method is runed and our file is closed and that is why f.closed returns True
# =================================
# ### Creating our own context manager using a function ###

# ---------------------------------
# To work with context manager using a function we have to use the contextlib module and import the contextmanager decorator and we can use the contextmanager decorator to decorate the generator function
# ---------------------------------
from contextlib import contextmanager

# This the open_file context manager that is equivalent to Open_File class
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()

# Everything above the yield statment is equivalent to the __enter__ method (i.e. it is our setup of our context manager)
# Everything after the yield statment is equivalent to the __exit__ method (i.e. it is the teardown of our context manager)

with open_file("file.txt", "a") as f:
    f.write("Testing")

# open_file("file.txt", "a") --> this will run everything before the yield statement
# The it will yield the the file object which we will set up to f variable
# Once we leave the context manager block the statments after the yield statement will be runed

print(f.closed)
# ---------------------------------
# Using the try and execpt block so that even if we get some error our file must be closed properly

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()
# =================================
# ### Some pratical examples ###

# Changing directory example

import os
# ---------------------------------
# Without using the context manager

cwd = os.getcwd()
os.chdir("Sample-Dir-One")
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir("Sample-Dir-Two")
print(os.listdir())
os.chdir(cwd)

# As we can see we have to write the same code whenever we want to do that work again and again

# As we can see that saving the current destination and switiching to other directory is setting up for the work that needs to be done
# i.e. --> cwd = os.getcwd() and os.chdir("Sample-Dir-Two") --> are the are our setup
# Switching back to current directory is our teardown
# So this is a good candidate for using a context manager
# ---------------------------------
# While setting a context manager note to put our setup in the try block and teardown in the finally block

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
        # Since we are not working with any variable(object) inside our context manager so we don't have to yield anything, we can just say yield
    finally:
        os.chdir(cwd)

# Since we are not working with any variable therefore we haven't put --> as  variable_name
with change_dir('Sample-Dir-One'):
    # Now inside this context mangaer we can do whatever we want
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())

# Now we don't have to worry about setup and teardown that is managed by our context manager
