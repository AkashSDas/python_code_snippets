# ###### Tips for writing better code ######

# 1. Ternary operator

# This can save you from writing a lot of unecessary code

condition = True
if condition:
    x = 1
else:
    x = 0

print(x)

# Above operation can be done in one line only
x = 1 if condition else 0

print(x)

# Our code should be easy to read

# 2. Working with large numbers

# While working with large numbers it becomes difficult to keep track of them
# We can use commas(,) to separate them but you can't use commas directly

num1 = 10000000000
num2 = 100000000

# But we can add underscores(_) to separate the

num1 = 10_000_000_000
num2 = 100_000_000

# This will save you from making mistakes
# The underscores won't affect your program

total = num1 + num2

# The output won't have separaters, to include separaters we have to string formatting
print(f"{total:,}")
# This F'String Formatting

# 3. When you are manually managing resources of something see to that are there any better way to do that same work

# 4. enumerate function

names = ['John', 'Brock', 'Sting', 'Randy']

# To get to know on what number you are on use

# instead of doing this
index = 0
for name in names:
    print(index, name)
    index += 1

# do this
for index, name in enumerate(names):
    print(index, name)

# You can also add a starting point
for index, name in enumerate(names, start=1):
    print(index, name)

# 5. zip function

names = ['Peter Parker', 'Clark Kent', 'Tony Stark', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Ironman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero}")
# ---------------------------
# Instead of using enumerate function use the zip function
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")
# ---------------------------
# We can use zip for more than two loops

names = ['Peter Parker', 'Clark Kent', 'Tony Stark', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Ironman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} as {hero} belong to {universe}")
# ---------------------------
# In the above case all the list are of the same length but if they are not then zip will stop after the shortest list is exhausted if you want to go to the longest iterable then you have to use zip_longest function from itertools libary

import itertools

names = ['Peter Parker', 'Clark Kent', 'Tony Stark', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Ironman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'Marvel', 'DC', 'Marvel', 'DC', 'DC']

for name, hero, universe in itertools.zip_longest(names, heroes, universes):
    print(f"{name} as {hero} belong to {universe}")
# Here the names and universe lists are exhausted therefore we are getting None
# ---------------------------
# Here
for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} as {hero} belong to {universe}")
# zip is returning tuple of three items but we are unpacking them by setting three different variables(name, hero, universe)
# But we can access the single tuple
for value in zip(names, heroes, universes):
    print(value)

# 6. How unpacking works

# Normal tuple
items = (1, 2)
print(items)

# Upacking values
a, b = (1, 2)
print(a)
print(b)

# Whenever you want to ignore a variable then name that variable as underscore(_)
a, _ = (1, 2)
print(a)
print(b)

# When are trying to unpack less values with more variables then we have we will get error
try:
    a, b, c = (1, 2)
    print(a)
except ValueError:
    print("Not enough values to unpack")

# When are trying to unpack more values with less variables then we have we will get error
try:
    a, b, c = (1, 2, 3, 4, 5)
    print(a)
except ValueError:
    print("Too many values to unpack")

# We can do something like this
a, b, *c = (1, 2, 3, 4, 5)
# Here a and b are the first two values respectively and *c will make all the remaining values equal to c
print(a)
print(b)
print(c)

# If you are not using the remaining values
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)

# Advance unpacking

# Here a & b are the first two values respectively then c is all the remaining value except for the last value, d is the last value
a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)

a, b, *c, d = (1, 2, 3, 4, 5, 6, 8)
print(a)
print(b)
print(c)
print(d)

# To ignore multiple values
a, b, *_, d = (1, 2, 3, 4, 5, 6, 8)
print(a)
print(b)
print(d)

# 7. Getting and Setting attributes on cretain objects

class Person:
    pass

person = Person()

# We can dynamically add attributes to our objects
person.first = "Corey"
person.last = "Schafer"

print(person.first)
print(person.last)

# What if we want to set attribute whose value is value of another variable
first_key = 'first'
first_val = 'Corey'

# We want to take first_key variable value and use it as attribute for our object and we want to set the value of that attribute as value of first_val
# Simple that means that we can run print(person.first) again

# For this we can't just do
person.first_key = first_val
# Because this will set an attribute known as first_key and we don't want that, we want that value of first_key should be the name of that attribute

# So in-order to this type of operations we will use built-in functions called getattr() and setattr()

# getattr() - This function is used to access the attribute value of an object and also give an option of executing the default value in case of unavailability of the key.
# setattr() - It is used to assign the object attribute its value. Apart from ways to assign values to class variables, through constructors and object functions, this method gives you an alternative way to assign value.

setattr(person, 'first', 'Corey')
# The frist argument is the object, the second one is the name of the attribute and third one is its value
print(person.first)

# Now we can use
setattr(person, first_key, first_val)
print(person.first)

# To get an value we will use getattr

first = getattr(person, first_key)
# First argument is the object name and second one it what value you want to get
print(first)

# To set attributes
person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

# If we just want to get those attributes
for key in person_info.keys():
    print(getattr(person, key))

# 8. Inputting secret information

# Keeping sensitive information in the eniviroment variables is good practice
# But what if you need to type-in a password for your script

# For this python has built-in module called getpass which has function called getpass and that will help us

# Bad way of doing this
username = input("Username: ")
password = input("Password: ")

print("Logging in...")
# When we run the script the password input will be typed on the screen which most users won't want

# Good way
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

print("Logging in...")
# Now when the user we input the password, the password won't show up in the screen

# 9. help() function

import random

# To get help on something
print(help(random))

# If you don't want all of the information and want to get information on certain methods then we will use the dir function
print(dir(random))
# This is give all of the valid attributes and methods for the object that you pass in

# If you don't know which are methods and which are attributes you can look for it
