# ###### Property Decorators - Getters, Setters and Deleters ######

# =================================
# ### Objectives ###
# 1. How to use Property Decorators
# 2. Getter, Setter, Deleter
# =================================
# Employee class

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('John', 'Cena')    
emp_1.first = 'Randy'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# Here the attribute first for emp_1 is getting changed but not the email attribute for emp_1, but fullname has no issue since it grabs the current first name attribute
# =================================
# ### Bad way ###

# To change email also
# We can create a method which can change email but this will break our code for everyone using the class, so we have to go every where and change email attribute to method

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def email(self):
        return '{}{}.@WWE.com'.format(self.first, self.last)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('John', 'Cena')    
emp_1.first = 'Randy'

print(emp_1.first)
print(emp_1.email())
print(emp_1.fullname())

# This is not the ideal way
# =================================
# ### Getter ###

# To continue to access email atrribute as attribute and not method
# This is done by just adding @property decorator

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{}{}.@WWE.com'.format(self.first, self.last)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('John', 'Cena')    
emp_1.first = 'Randy'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
# =================================
# Adding @property decorator to the fullname method so that we can access it like a attribute

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{}{}.@WWE.com'.format(self.first, self.last)
    
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('John', 'Cena')    
emp_1.first = 'Randy'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# If you want ability to set emp_1.fullname = 'Brock Lesnar'
# Just doing(emp_1.fullname = 'Brock Lesnar') this will give an error
# For this we have to use a Setter
# =================================
# ### Setter ###

class Employee:    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{}{}.@WWE.com'.format(self.first, self.last)
    
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
emp_1 = Employee('John', 'Cena') 
emp_1.fullname = 'Brock Lesnar'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# =================================
# ### Deleter ###

# To delete our employee

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{}{}.@WWE.com'.format(self.first, self.last)
    
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None    
        
emp_1 = Employee('John', 'Cena') 
emp_1.fullname = 'Brock Lesnar'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# Deleting emp_1
del emp_1.fullname
