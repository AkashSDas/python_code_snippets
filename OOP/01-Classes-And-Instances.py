# ###### Classes And Instances ######

# =================================
# ### Objectives ###
# 1. create simple class
# 2. difference between class and instance of that class
# 3. initializing class attributes and methods
# =================================
# Learning OOP's concepts by making a Employee Class and working with that
# =================================
# Creating a class
class Employee:
    pass

# Our Employee class is a blueprint for creating instances and each unique employee we create using Employee class will be instance of that class    
# With pass keyword, we indicate a "null" block
# ----------------------------------
# Creating Instances

# Both are Employee objects and both are unique
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
# ----------------------------------
# Instance Variables

# instance variables - It contain data that are unique to each instance

# Manually creating each instance variable for employees
emp_1.first = 'John'
emp_1.last = 'Cena'
emp_1.email = 'JohnCena@WWE.com'
emp_1.pay = 100000

emp_2.first = 'Randy'
emp_2.last = 'Ortan'
emp_2.email = 'RandyOrtan@WWE.com'
emp_2.pay = 90000

print(emp_1.email)
print(emp_2.email)

# We should create these instance variables for each employee when they are created rather then doing it manually, since creating it manually may prone to mistakes and it is alot of code
# For this we use the __init__ method which is also known as intialize/constructor
# =================================
# When we create a methods within a class they receive instance as the first argument automatically and by convetion the instance is called "self" but we can call it whatever we want

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        # self.fname = first <-- this is also valid
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'

# Whenever we say that self is the instance what we mean is that when we set self.first = first, it is going to be the same thing as emp_1.first = 'John' except now instead of doing it manually it'll be done automatically whenever we create new employee objects        
# ----------------------------------        
# When we create our employee, now instance is passed automatically so we can leave off self, we only need to provide other arguments
# We have to pass the argument in the same order as we have specified in the method
emp_1 = Employee('John', 'Cena', 100000)

# When emp_1(our employee) we create the init method will run automatically, so emp_1 will be passed in as self and then it will set all of these attributes
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1.email)
print(emp_2.email)
# ----------------------------------
# If we want the ability to perform some kind of action then to do that we can add methods to our class

# Actions like to show fullname of the employee

# We can do this manually:
print('{} {}'.format(emp_1.first, emp_1.last))
# But this is alot of code and for every other employee the code has to be changed
# =================================
# Creating methods inside our class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@WWE.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        # We have to use self as first parameter so that the method works with all instances

emp_1 = Employee('John', 'Cena', 100000)    
emp_2 = Employee('Randy', 'Ortan', 90000)

print(emp_1.fullname())
# Here we need parentheses since fullname is a method instead of an attribute

# Without parentheses it will print the method object
print(emp_1.fullname)

# Since our instance(emp_1 and emp_2) are getting automatically passed to fullname so self is necessary

# We can also run these methods using class names, it tells us what's going in the background
print(Employee.fullname(emp_1))
# ----------------------------------
# Note:
Employee.fullname(emp_1)
emp_1.fullname()

# Both the lines do exactly the same work
# When we call a method on instance we don't need to pass instance, "self" does it automatically
# When we call a method on class we need to pass in instance on which we want to run the method
