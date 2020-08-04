# ###### Sorting Lists,Tuples and Objects ######

# =================================
# ### Sorting Lists ###

# ---------------------------------
# ### .sorted() ###

li = [7,3,9,2,1,8,4]

# sorted method returns a new list
sorted_li = sorted(li) 
print(sorted_li)

# Making reverse=True returns a sorted list where elements are in decending order
sorted_li = sorted(li,reverse=True) 
print(sorted_li)

# To sort list with their absolute values, we use the "key" argument
# abs --> absolute
li = [-6,-5,-4,1,2,3]
sorted_li = sorted(li,key=abs)
print(sorted_li)
# ---------------------------------
# ### .sort() ###

li = [7,3,9,2,1,8,4]

# sort method make changes to the original list
li.sort() 
print(li)

# Making reverse=True sorts the list in decending order
li.sort(reverse=True)
print(li)
# =================================
# ### Sorting Tuples ###

# Tuples don't have a sort function

# ### .sorted() ###

tup = (5,8,9,3,7,1,4) 

sorted_tup = sorted(tup)
print(sorted_tup)
# sorted method will return a sorted list

# If we want a tuple then we can cast list into tuple
sorted_tup = tuple(sorted(tup))
print(sorted_tup)
# ================================
# ### Sorting Dictionaries ###

# ### .sorted() ###

dictionary = {'name':'elon','job':'ceo','age':51} 

sorted_dict = sorted(dictionary)
print(sorted_dict)
# This returns a sorted list which has keys of the dictionary

# To sort values of the dictionary 
dictionary = {'name':'elon','job':'ceo','age':'51'} 
# Note that while sorting the values, the value of "age" should be of type string, otherwise we will get an error since we are trying to compare strings with integer

sorted_dict = sorted(dictionary.values())
print(sorted_dict)
# ================================
# ### Sorting Objects ###

class employee():
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)
        
emp_1 = employee('elon',51,50000)
emp_2 = employee('bill',71,70000)
emp_3 = employee('jeff',68,90000)

employees_list = [emp_1,emp_2,emp_3]
# ---------------------------------
# Using custom functions

# Sorting by name
def emp_sort(emp):
    return emp.name

sort_employees = sorted(employees_list,key=emp_sort)
print(sort_employees)

sort_employees = sorted(employees_list,key=emp_sort, reverse=True)
print(sort_employees)

# As per your sorting requirements functions can be more complex
# If you have a complicated sort function than its good to break them into separate functions
# ---------------------------------
# Using lambdas

sort_employees = sorted(employees_list,key=lambda emp: emp.name)
print(sort_employees)
# ---------------------------------
# Using attrgetter

from operator import attrgetter

# Sorting by age
# attrgetter is used as "key" and list is sorted by age
sort_employees = sorted(employees_list,key=attrgetter('age'))
print(sort_employees)
# ---------------------------------
# Knowing how to sort with custom functions and using lambdas will help you to more flexible when you want to sort more complicated items
# ================================
# ### attrgetter ###

# operator.attrgetter(attribute)
# operator.attrgetter(*attributes)

# Return a callable object that fetches attr from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots. 

# For example:
# After f = attrgetter('name'), the call f(b) returns b.name.
# After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
# After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).
