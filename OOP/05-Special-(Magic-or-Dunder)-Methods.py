# ###### Special (Magic/Dunder) Methods ######

# =================================
# ### Objectives ###
# 1. using Special Methods in our classes 
# 2. these Special Methods are also called Magic/Dunder Methods
# =================================
# Special Methods allow us to emulate some built-in behavior within Python and it's also how we implement operator overloading

# Meaning: 

# 1. adding two integers
print(1 + 2)
# Output --> 3

# 2. adding two strings
print('a' + 'b')
# Output --> 'ab'

# As you can see when we add two integers and two strings behaviours are different
# =================================
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)
# ---------------------------------
print(emp_1)
# Here we get vague Employee object 
# It would be nice if we could change this behavior to print out something user-friendly and that's what these Special Methods will allow us to do

# This is what we're going to use to solve problem of printing out vague Employee object when we print emp_1 instance
repr(emp_1)
str(emp_1)
# repr ---> it is meant for unambiguous represntation of object and should be used for debugging and logging and things like like that. It's really ment to be seen by other developers
# str --->  it is meant to be more of a readable represntation of an object and is meant to be used as display to the end-user 
# =================================
# Now adding the __repr__ method to our Employee class

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    # First we want to be sure to atleast have an repr method because if we have this without an str then calling str on a employee we'll just use the repr as a fallback so it's good to have this minimum 
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
            
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1)
print(repr(emp_1))
# =================================
# Now adding the __str__ method to our Employee class

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
           
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
        
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())
# =================================
# Other Special Methods

print(1 + 2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

# So here we can customize the way __add__ worked
# =============================================
# To add salaries of two employees

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
        
    def __add__(self, other):
        return self.pay + other.pay
    
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1 + emp_2)

# Without that __add__ we will get an error
# =================================
# len ---> also Special Method

print(len('test'))
print('test'.__len__())
# =================================
# To get length of employees names so that if someone is writing documents and needs to know how much characters the employees name will take

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
        
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(len(emp_1))
