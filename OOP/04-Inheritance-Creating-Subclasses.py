# ###### Inheritance - Creating Subclasses ######

# =================================
# ### Objectives ###
# 1. Creating Subclasses
# =================================
# inheritance - Inheritance allows us to inherit attributes and methods from parent class
# By this we can create subclasses and get all of the functionalities of parent class and then we can overwrite and write completely new functionlities without affecting the parent class
# =================================
# Employee Class
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
# =================================
# Creating another class --> Developer Class
# Developer class will inherit from Employee class, since alot of features of Developer class will be same as that of Employee class

# Inside the parenthese we write the name of class from where are inheriting
class Developer(Employee):
    pass
# ---------------------------------    
# Here both the developers are created and we can access the attributes in our parent class
dev_1 = Developer('John', 'Cena', 100000)    
dev_2 = Developer('Randy', 'Ortan', 90000)

print(dev_1.email)
print(dev_2.email)
# ---------------------------------
# Here when we instantiated our developers it first looked in our Developer class and it couldn't find there anything since it's currently empty and then Python will walk into chain of inheritance and find what it is looking for 
# This chain is called "method resolution order"
# ---------------------------------
# To visualize this inheritance use "help" method
print(help(Developer))    
# =================================
# Changing attributes of Employee class for our Developer class

# Here we have changed the raise_amount
class Developer(Employee):
    raise_amount = 1.10

dev_1 = Developer('John', 'Cena', 100000)    
dev_2 = Developer('Randy', 'Ortan', 90000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
# =================================
# Sometimes we need to specify language of that developer

# To keep code dry and clean, instead of pasting code for first,last,pay we will let Employee class to handel first,last,pay and Developer class to handel prog_lang
# This can be done by using --> super().__init__()
# We can do same thing with --> Employee.__init__(self, first, last, pay), but super().__init__() is more maintainable       

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):        
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
# super().__init__() to make your call, which is concise and does not require you to reference the parent OR class names explicitly, which can be handy

dev_1 = Developer('John', 'Cena', 100000, 'Python')    
dev_2 = Developer('Randy', 'Ortan', 90000, 'JavaScript')

print(dev_1.email)
print(dev_1.prog_lang)
# =================================
# Creating another subclass Manager

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
# Why didn't we pass in empty list as default argument in __init__ instead of None, because you never want to pass mutable data types like list/dictonary as default arguments
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('---> ' + emp.fullname())
            
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
# =================================
# Python has built-in functions called isinstance and issubclass
# isinstance() is used to check if an object is an instance of a certain class or any of its subclass
# issubclass() is used to check if a class type is the subclass of a different class

print(issubclass(Manager, Developer))
print(issubclass(Developer, Manager))
print(isinstance(mgr_1, Developer))
print(isinstance(dev_1, Developer))
