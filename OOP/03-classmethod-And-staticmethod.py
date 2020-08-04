# ###### Class method And Static method ######

# =================================
# ### Objectives ###
# 1. difference between regular method, class method and static method
# =================================
# ### Classmethod ###
# =================================
# Regular methods in a class automatically takes instance as the first argument i.e. self(by convention)
# To make it to take class as argument automatically we have to use class method
# =================================
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
        
    # Turning a regular method to class method we have to add "classmethod" decorator at the top of the method
    # Use "cls" keyword for the first argument to class methods. We cannot use "class" since it is already a special keyword in Python
    # "cls" is just a naming convention like "self"
    @classmethod
    def set_raise_amt(cls, amount):        
        # Here we are working with class instead of instance
        cls.raise_amount = amount
        
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# ---------------------------------
# To set raise_amount to 5%
Employee.set_raise_amt(1.05)

# This has same meaning as 
Employee.raise_amount = 1.05 

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# ---------------------------------
# We can run class method from instances as well, but it is not much used

emp_1.set_raise_amt(1.06)
print(emp_1.raise_amount)
# =================================
# People often say that they use class methods as alternative constructors
# Which means that you can use these class methods in order to provide multiple ways of creating the objects
# ---------------------------------
# Example:- I'm getting employee information in the string that are separated by hyphens(-) and I need to constantly parse the string before I create new employees

# Employee information
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Simit-30000'
emp_str_3 = 'Jane-Doe-90000'
# ---------------------------------
# Using usual way

first, last, pay = emp_str_1.split('-')

# Creating new employee
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
# ---------------------------------
# Using classmethod as a constructor

# Instead of doing that, we will create a classmethod so that we can pass them the string and can create a new employee 

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
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    # Usally the name of method start's with "from" while using class method as a constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # Creating a new employee
        return cls(first, last, pay)
    
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
# =================================
# ### Staticmethod ###
# =================================
# In staticmethod we don't pass anything automatically, we don't pass neither class nor the instance
# Turning a regular method to static method we have to add "staticmethod" decorator(@staticmethod) at the top of the method
# =================================
# Real world example of staticmethod using datetime module

# Let's say we need a simple function that would take in a date and return whether it was a workday or not
# It has logical connection with our Employee class but does not depends on particular instance or class

import datetime

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
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

my_date = datetime.date(2019, 7, 10)

print(Employee.is_workday(my_date))
# =================================
# Note:
# Somethime people write staticmethod as classmethod or regularmethod
# If you don't want to access a method with the instance or class then it is a staticmethod
