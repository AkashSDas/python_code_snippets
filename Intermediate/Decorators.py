# ###### Decorators ######

# A decorator is a function that takes another function as an argument, adds some kind of functionality to it and then return another function without altering the source code of original function you passed in

# =================================
# ### Closures ###

# To see why decorators are better than closures below are some examples

# ---------------------------------
# 1.
def outer_func():
    msg = 'Hi'          
    # Here msg is a free variable since inner_func can access it
    def inner_func():
        print(msg)  
    return inner_func
    
outer_func()   
# it gives no output

my_func = outer_func()
my_func()
# ---------------------------------
# 2.
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func
    
hi_func = outer_func('hi')
bye_func = outer_func('bye')

hi_func()    
bye_func()
# =================================    
# ### Decorators ###

# ---------------------------------
# 1.
# ---------------------------------
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function    
    
def display():
    print('display function ran')
    
decorated_display = decorator_function(display)
decorated_display()
# ---------------------------------
# Adding functionality to the display function without modifying the display function code

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function    
    
def display():
    print('display function ran')
    
decorated_display = decorator_function(display)
decorated_display()
# ---------------------------------
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function    

# This is how we usually see decorators in Python
@decorator_function 
def display():
    print('display function ran')

# This --> @decorator_function, is the same thing as setting our display function to decorator_function and our original function passed in    
display = decorator_function(display)

# If you just run the display now then it will have our wrapper code added to our original function
display()

# So,
# 1. 
# @decorator_function 
# def display():

# 2. 
# display = decorator_function(display)

# 1. and 2. both have same meaning
# ---------------------------------
# 2.
# ---------------------------------
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
    
@decorator_function
def display():
    print('display function ran')
    
@decorator_function
def display_info(name,age):
    print('display_info ran ran with arguments ({}, {})'.format(name,age))
    
    
display_info('john',25)
    
display()
# =================================    
# ### Classes As Decorators ###

class decorator_class(object):
    
    def __init__(self, original_function):
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('display function ran')
    
@decorator_class
def display_info(name,age):
    print('display_info ran ran with arguments ({}, {})'.format(name,age))
        
display_info('john',25)
    
display()
# =================================
# ### Decorators with arguments ###

# For example of decorators taking arguments we will use flask module

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/about")
def about():
  return "About Page"

if __name__ == '__main__':
   app.run()

# Here routes are definied using app.route decorators and strings that are passed in are the URL paths
# So passing arguments in decorators can be useful
# =================================
# ### Another example of decorators with arguments ###

def decorator_function(original_function):
  def wrapper_function(*args, **kwargs):
    print('Executed Before', original_function.__name__)
    result = original_function(*args, **kwargs)
    print('Executed After', original_function.__name__, '\n')
    return result
  return wrapper_function

@decorator_function
def display_info(name, age):
  print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 51)
display_info('Brock', 47)
# ---------------------------------
# In this example let say we want a customizing prefix to all of these print statements
# For this we can use arguments which are passed through decorator function

def prefix_decorator(prefix):
  def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
      print(prefix, 'Executed Before', original_function.__name__)
      result = original_function(*args, **kwargs)
      print(prefix, 'Executed After', original_function.__name__, '\n')
      return result
    return wrapper_function
  return decorator_function

@prefix_decorator('TESTING:')
def display_info(name, age):
  print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 51)
display_info('Brock', 47)

@prefix_decorator('LOG:')
def display_info(name, age):
  print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 51)
display_info('Brock', 47)
# =========================================    
# This is not something that you are going to use quite often but it's good to know this if you ran in some situation where you would need this, Also in frameworks like Flask where they are used, So you can have an idea of what it is doing
