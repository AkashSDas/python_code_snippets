# ###### import itertools ######

# =================================
# Importing itertools module
import itertools
# =================================
# ### itertools.count() ###

# It returns an iterator which simply counts
# ---------------------------------
# If no argument is given then it will start with zero and it will increment it's count by 1 in each iteration
counter = itertools.count()

# It is an infinite loop
for num in counter:
    print(num)

# Instead of looping we are printing only one item at a time by using next method
print(next(counter))    
print(next(counter))
print(next(counter))
print(next(counter))
# ---------------------------------
# Sometime we don't know how many items are there in our list and we want to give index to them, at that time count method is very useful

data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data)) 
# zip function ends when shortest iterable is exhausted
print(daily_data)
# count method can work with any size of data
# ---------------------------------
# Passing arguments to the count method

counter = itertools.count(start=5, step=-2.5)
# counter is versatile it can count in both way (front and backward)

print(next(counter))    
print(next(counter))
print(next(counter))
print(next(counter))
# =================================
# ### itertools.zip_longest() ###

# Using the zip function
data = [100, 200, 300, 400]
daily_data = list(zip(range(10), data))
print(daily_data)  

# But if we use the zip_longest function then it will count till the largest iterable is exhausted
data = [100, 200, 300, 400]
daily_data = list(itertools.zip_longest(range(10)), data)
# Since our list is exhausted the other values from range function will be paired with None
print(daily_data)

# zip_longest function ends when longest iterable is exhausted
# itertools.count() cannot be used with zip_longest because we are converting it to a list and since count goes forever then we will run out of memory
# =================================
# ### itertools.cycle() ###

# cycle method also returns an iterator which goes on forever. 
# Basically it takes an iterable as an argument and will cycle through those values over and over
# ---------------------------------
nums = [1, 2, 3]

counter = itertools.cycle(nums)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# ---------------------------------
counter = itertools.cycle(["On", "Off"])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# =================================
# ### itertools.repeat() ###

# repeat method will repeat only as many time as it is given, if we continue repeating beyond the times you had set then we will get an StopIteration Error
# We are using the try an except block so that once the iteration is over the error that we will get will be handled
# If we were using for loop then that error will have taken care of by for loop itself

try:
    counter = itertools.repeat(1, times=3)
    # The first argument is what we want to repeat
    # Second argument(times) is how many times to repeat the first argument
    
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))
except:
    print("There is an StopIteration Error which is handeled by for loop but not by itertools.repeat()")
# ---------------------------------
# Examples of itertools.repeat()

squares = map(pow, range(10), itertools.repeat(2))  
# map is passing iterable to function(pow)
print(list(squares))

squares = map(pow, range(10),itertools.repeat(2, times=3))
print(list(squares)) 
# It will give of squares of three number since times argument is set to 3
# =================================
# ### itertools.starmap() ###

# It is similar to map but instead of taking argument through iterables like the map does, it takes argument that are already put together as tuples
squares = itertools.starmap(pow, [(0,2), (1,2), (2,2), (3,2), (4,2)])
# First argument is the function and second argument is an iterable
print(list((squares)))
# =================================
# ### Combinations and Permutations ###

# ---------------------------------
# combinations and permutations do not repeat values
# ---------------------------------
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)
for item in result:
    print(item)

result = itertools.permutations(letters, 2)
for item in result:
    print(item)
# =================================
# ### itertools.product() ###

# It gives cartesian product and we can also repeat values
numbers = [0, 1, 2, 3]

result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)
# =================================
# ### itertools.combinations_with_replacement() ###

# To get combinations with repeated values

numbers = [0, 1, 2, 3]
result = itertools.combinations_with_replacement(numbers, 4)
for item in result:
    print(item)
# =================================
# ### itertools.chain() ###

# It allows to chain iterable so that it can go through all the itmes in first iterable and then through the second iterable and so on

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# We can also chain values by using this code
combined = letters + numbers + names
# But this is not a good way, If the lists were too long or we have generators then this not efficient way

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)  
# =================================    
# ### itertools.islice() ###

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.islice(range(10), 1, 5, 2)
for item in result:
    print(item)

# It is useful when iterator is too big, and you want to grab only few values, there islice() is useful    
# ---------------------------------
# If we have a text file and we want few starting lines without loading the entire file in memory then islice method is useful
# Files are themselves an iterable

# Let say our data is in filenamed file.log
# Data
"""
Date: 2018-11-08
Author: Corey
Description: This is a sample log file

Okay, so this is a sample entry.
I'm going to write a few more lines here.
For the sake of this video, let's pretend this log file is thousands and thousands of lines... okay?
"""

with open('file.log', 'r') as f:
    header = itertools.islice(f, 3)
    
    for line in header:
        print(line)
        
# This code will give first three lines of the file, i.e. Date, Author, Description 
# =================================
# ### itertools.compress() ###

# It is used in DataScience problems to filter the data

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)
# We pass an iterable and selector to compress method and it is returning a new iterable that only contains the items that correspond to True value

for item in result:
    print(item)
# ---------------------------------    
# This is kind of similar to buit-in filter function
# filter function uses function to determine whether something is True or False while in compress method those values are passed in as an iterable

# Example:
# filter function
def lt_2(n):
    if n < 2:
        return True
    return False

numbers = [0, 1, 2, 3]
result = filter(lt_2, numbers)
for item in result:
    print(item)  
# =================================
# ### itertools.filterfalse() ###

# It returns value which are False
def lt_2(n):
    if n < 2:
        return True
    return False

numbers = [0, 1, 2, 3]
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)
# ---------------------------------
def lt_2(n):
    if n < 2:
        return True
    return False

numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)  
    
# All values > 1 are filtered out  
# =================================
# ### itertools.dropwhile() ###

def lt_2(n):
    if n < 2:
        return True
    return False

numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item) 
    
# Once it hit values > 1 it will return rest of iterables
# =================================
# ### itertools.takewhile() ###

# It is opposite of dropwhile

def lt_2(n):
    if n < 2:
        return True
    return False

numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.takewhile(lt_2, numbers)
for item in result:
    print(item)
# =================================
# ### itertools.accumulate() ###

# It add values to the previous iterable item

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

result = itertools.accumulate(numbers) 
# returns ==> 0, 0+1, 0+1+2, 0+1+2+3

for item in result:
    print(item)    
# ---------------------------------
# To multiple
import operator

numbers = [1, 2, 3, 4, 5, 0]

result = itertools.accumulate(numbers, operator.mul)
for item in result:
    print(item)    
# =================================    
# ### itertools.groupby() ###

# Make an iterator that returns consecutive keys and groups from the iterable. The key is a function computing a key value for each element. If not specified or is None, key defaults to an identity function and returns the element unchanged.

# Our iterator
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

# ---------------------------------
# Group people name by their state name

def get_state(person):
    return person['state']
    
person_group = itertools.groupby(people, get_state)
# The first argument of groupby is key and second argument is iterable

for key, group in person_group:
    print(key, group)
# ---------------------------------    
# For people from same place
for key, group in person_group:
    print(key)
    for person in group:
        print(person)
# ---------------------------------
# Number of people from same place
for key, group in person_group:
    print(key, len(list(group)))
# ---------------------------------
# groupby excepts the initial iterable to be sorted so that it can group properly 
# people were sorted by state 
# if someone from NY were added on to the end of the list then it wounldn't include them in the first group of people from that state
# groupby is different from sql version of groupby, it needs values to be sorted before it is handled
# =================================
# ### Replicate an iterator ###

# It can be hard but itertool makes it easy
# The tee() function can be used to create any number of independent iterators from a single iterable. 
# The tee() function takes two arguments: the first is an iterable inputs and the second is the number(n) of independent iterators over inputs to return (by default, n is set to 2). The iterators are returned in a tuple of length n .

person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

for key, group in copy1:
    print(key, len(list(group)))

# copy1 and copy2 are their own individual iterables
# If we want more copies then we can pass an argument to tee function and return however many we like
# You should no longer use the original iterator after you copy it since it can have unintended consequences of exhausting the items in the replicates
# ---------------------------------
# Example
# In this example we should only use these copies of copy1 and copy2 and not use this original person_group iterator after we made copies or it can have unintended consequences of exhausting the items in the replicates

for key, group in copy2:
    print(key, len(list(group)))
    
# Here our items in the replicates are exhausted by using other copy

for key, group in person_group:
    print(key, len(list(group)))

# Now if you use copy2, person_group it won't return any thing since the items in the list is exhausted
