# ###### Class Vairables ######

# =================================
# ### Objectives ###
# 1. difference between instance variables and class variables
# 2. when to use each of one
# =================================
# 1. instance variables - Used for data which is unique to each instance, they are automatically set using "self" keyword
# 2. class variables - Variables that are shared among all instances of a class
# While instance variables can be unique for each instance, class variables are same for each instance
# =================================
# What kind of data we want to share among users ?
# Since company gives a annual raises every year and what ever that amount will be that will be same for each employee

# First we will see why class variables is a better option
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    # To check why class variables will be a better use-case for our question
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
        
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

# Things wrong with this apply_raise method:
# 1. It would be better if we could access raise amount by doing something like --> emp_1.raise_amount
# 2. Also if it is going to be applied to entire class we should also be able to do this --> Employee.raise_amount
# raise_amount attribute doesn't exist now 
# 3. Also what if you want to easily update that raise amount
# =================================
# Using class variable

class Employee:
    
    # class variable
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # When we access the class variables we need to access them through class itself or the instance of the class
        self.pay = int(self.pay * self.raise_amount)
        # We can also do this --> self.pay = int(self.pay * Employee.raise_amount)
        
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
# ---------------------------------
# To clarify that why class variables can be accessed by instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# When we try to access an attribute on an instance it will first check if the instance contain that attribute and if that doesn't then it will check if any class or class that it inherits from, contains that attribute
# ---------------------------------
# Printing the namespace
print(emp_1.__dict__)
print(Employee.__dict__)
# ---------------------------------
# This will change the raise_amount for class and for all the instances
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# ---------------------------------
# This will change the raise_amount for given instances only
emp_1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Now emp_1 will have raise_amount in its name sapce
print(emp_1.__dict__)
# ---------------------------------
# This clearly tells how class variables work

# Setting it as self.raise_amount in --> self.pay = int(self.pay * self.raise_amount) will give us better control to change something like raise_amount for certain employees rather than using this --> self.pay = int(self.pay * Employee.raise_amount)
# Also using self will allow any subclass to overwrite any constant
# =================================
# Another example of using class variables can be keeping track of how many employees we have, number of employees will be same for each instance 

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
print(Employee.num_of_emps)

emp_1 = Employee('John', 'Cena', 100000)    
print(Employee.num_of_emps)

emp_2 = Employee('Randy', 'Ortan', 90000)
print(Employee.num_of_emps)

# When a new employee will be created num_of_emps will be incremented by 1
