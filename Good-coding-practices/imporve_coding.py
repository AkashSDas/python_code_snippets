# 1. Indentation
# Always keep "translate tabs to space" on because it will give IndentationError. Use an editior that can do this.

# 2. Naming Mistakes

# Don't name your python modules same as something that are importing. If you don't do this then your module with the same name will take higher priority then the module that you are trying to import from standard libary

# If the below script was in a your module whose name was math then you will get an error
from math import radians, sin

rads = radians(90)
print(sin(rads))

# Another naming mistake can occur while naming the variable
radians = radians(45)
print(sin(radians))
# The above code will work perfectly

# But after that the below code will give error
try:
    rad60 = radians(60)
    print(sin(rad60))
except:
    print("TypeError: 'float' object is not callable")
# Above we have assigned a radians variable to radians method but after that whenever we are using the radians method we will be using the radians variable and not the actual method.

# 3. Issues with Mutable Default Arguments

# Here the employee list has a default agrument that if we don't pass the employee then new list will be created.
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['Corey', 'John']

# Here the employee will be added to the list emps
add_employee('Jane', emps)

# Trying add_employee function without providing any list
# This will create a new list
add_employee('Rock')
# This employe "John" will be added to the list created by above line which shows the problem with using the mutable default arguments
add_employee('John')
# "Brock" will also be added to list rather than creating an empty list an then adding to it
add_employee('Brock')

# In python default arguments are evaluated once at the time it creates function. So each time it is not creating a new empty list. This is not an issue with Immutable datatypes but it a problem with mutable datatypes.

# To make sure that you get an empty list each time
def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

emps = ['Corey', 'John']

add_employee('Rock')
add_employee('John')
add_employee('Brock')
add_employee('Goldberg', emps)

# There can also be other places where default arguments won't give desired results
import time
from datetime import datetime

def display_time(time=datetime.now()):
    print(time.strftime("%B %d, %Y %H:%M:%S"))

# Not providing any arguments, so now it should give us different time
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
# But three times we got the same, here also we have the same issue of default arguments

# Instead we do this like this
def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime("%B %d, %Y %H:%M:%S"))

# Now our problem is solved
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# 4. Iterators

# Iterators can be echaustive that is we can loop through value and can access them one at a time, Python 3 does not returns the entire. We use generators and iterators to get those value or simply cast them to list where list loop through all values and exhaust the iterator

Supersarts = ['John', 'Randy', 'Finn', 'Shinshuke']
Brand = ['WWE', 'Raw', 'NXT', 'SmackDown']

relations = zip(Supersarts, Brand)
print(relations)

# Casting the object to list
relations = list(zip(Supersarts, Brand))
print(relations)

# 5. Mistakes during import

import os

os.rename('filename')
# For every function from os module we have to use os.<function_name>

# But we can also import functions one at a time a don't need to use os.<function_name>

from os import rename, remove
rename("filename")
remove("filename")

# We can use asterisk(*) to import everything as still not use os.<function_name>
from os import *
rename("filename")
remove("filename")

# It's a bad practice unless we don't know what we are doing, But still it is a Bad Practice

# If we are importing two modules which have same function names then those function names will be overwritten

from html import *
from glob import *

# escape method is there in html and also in html with different purpose
print(help(escape))
# So escape method of html module will be overwritten by escape method of glob module
# Also we can face lot of issues while debugging

# If you want to import both of them
from html import escape as h_escape
from glob import escape as g_escape

# While you import entire module you don't need to worry about these issues
import html
import glob

print(html.escape)
print(glob.escape)
# This the best way to work
