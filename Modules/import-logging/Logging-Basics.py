# ###### Logging Basics ######

# =================================
# Run each block separatly, running the entire script at once will give result of the starting only and others will not be shown.
# =================================
# ### Objectives ###
# 1. Replacing print statements with log statments 
# 2. Set different log statements
# 3. Log information to files
# =================================
# Logging is a means of tracking events that happen when some software runs. 
# Logging is important for software developing, debugging and running

# People use print statements to catch problems easily, but we have to use logging once our application grows beyound basic project. 
# Having good logs will allow us to look at behaviour and errors and give an overall picture of whats going on, also we can pipe in into some visualiztation software to get a better prespective
# =================================
# ### For understanding basics ###

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

num_1 = 10 
num_2 = 5
# ---------------------------------
# After execution of these lines they run successfully with no error but gives no output

add_result = add(num_1, num_2)
sub_result = subtract(num_1, num_2)
mul_result = multiply(num_1, num_2)
div_result = divide(num_1, num_2) 
# ---------------------------------
# Using print function

print("Add: {} + {} = {}".format(num_1, num_2, add_result))
print("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
print("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
print("Div: {} / {} = {}".format(num_1, num_2, div_result))
# ---------------------------------
# Using logging module

import logging

"""
Logging levels allow us to specify exactly what we want to log by separating these by categories

Logging Levels in order of increasing severity:
1. DEBUG: Detailed information, typically of interest only when diagnosing problem
2. INFO: Confirmation that things are working as expected
3. WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected
4. ERROR: Due to a more serious problem, the software has been able to perform some function
5. CRITICAL: A serious error, indicating that program itself maybe unable to continue running

The default level for logging is set to WARNING, that means it will capture WARNING, ERROR, and CRITICAL and ignore DEBUG and INFO
""" 
# ---------------------------------
# Converting print statements to debug logging statments 
# The default behaviour for this logging statement is to log this to console so right now these are very similar to print statements

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))

# After we run this nothing will happen since the default logging level is WARNING and it is only going to logout warnigs and above 
# ---------------------------------
# Using warning instead of debug

logging.warning("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.warning("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.warning("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.warning("Div: {} / {} = {}".format(num_1, num_2, div_result))

# This has more information than our print statements
# =================================
# ### Changing Logging Levels ###

logging.basicConfig(level=logging.DEBUG)

# The DEBUG here is different than our debug method, its just a constant integer in the background 

# Level     |  Numeric value
# ---------------------------------
# CRITICAL  |  50
# ERROR     |  40
# WARNING   |  30
# INFO      |  20
# DEBUG     |  10
# NOTSET    |  0

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# =================================
# ### Creating a Log File ###

logging.basicConfig(filename='test.log', level=logging.DEBUG)

# filename --> where we want to save our logs

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))

# These logs are saved to file test.log
# =================================
# ### Changing the format ###

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# There are many formats avialable in the Python Documentation

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# =================================
# ### An example of using logging ###

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(message)s')

class Employee:
  def __init__(self, first, last):
    self.first = first 
    self.last = last
    logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Cena')
emp_2 = Employee('Brock', 'Lesnar') 
emp_3 = Employee('Randy', 'Ortan')
