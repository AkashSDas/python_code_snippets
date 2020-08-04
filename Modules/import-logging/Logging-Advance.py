# ###### Logging Advance ######

# =================================
# Run each block separatly, running the entire script at once will give result of the starting only and others will not be shown.
# =================================
# ### Objectives ###
# 1. Loggers
# 2. Handlers
# 3. Formatters
# =================================
# ### Inside log-sample.py ###

import logging

logging.basicConfig(filename='sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

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

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# =================================
# ### Inside employee.py ###

import logging

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
# =================================
# root - It means that since we haven't specified a specific logger, we are working with the root looger  
# Working with root logger is a bad thing with working with specific files or applicatiob
# All loggers are descendants of the root logger
# Best practice is to logging to specific loggers that can all be configured spearately
# =================================
# Why working with root logger is not a good practice can be understood by below sample code

# ### Inside log-sample.py ###

import logging
import employee

logging.basicConfig(filename='sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

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

logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))

# When we import a module it runs code from that module
# So now it sould go to the employee module make Employees

# After running the code from log-sample.py you will see that employee.log file is created but the smaple.log file specified here isn't there 
# It didn't created the sample.log file

# The Reason it didn't do that is that when we set the logger function in Employee class it configured the filename, level and format with the basicConfig in the employee.py file, all that setup first because we imported the employee and that module is sharing that root logger with this script 
# So when we start configuring in this file the root logger is already configured so it (basicConfig of log-sample.py) doesn't do anything. It doesn't overwrite those initial configuration.

# Only reason our log statements of log-sample.py isn't logging is that our root logger got set to INFO level in our employee module and so debugging doesn't hit that level 

# Now if you change from debug to info level in log-sample.py then it will be exceuted since it was set to info level from the employee module
logging.info("Add: {} + {} = {}".format(num_1, num_2, add_result))
logging.info("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logging.info("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logging.info("Div: {} / {} = {}".format(num_1, num_2, div_result))

# It is still a mess since we are still sharing the root logger, we are not getting the root file that we want, we are not getting the root level that we wantand we are not getting the formatting that we want 
# =================================
# To solve the above problem we have to get new logger for each of our modules so that we can configure both of logs separatly

# ### Inside employee.py ###

import logging

logger = logging.getLogger(__name__)
# We can hardcode any name we want inside the parenthese but the convention when naming logger is to use __name__ method/variable
# If this logger doesn't exist then it will be created

# While executing this file directly the __name__ == '__main__'
# While importing and executing __name__ == that_filename_in_which_it_is_executed_or_imported_in

# NOTE!!!
# Now when we are having logger variable and working with specific logger, now we should use this to run log methods

# Loggers are within hierarchy that is if this employee logger doesn't have something set then it will fall to root logger
# Even now when we are using the new logger variable, it still doesn't print to the console it will create an employee log file 
# But now it will tell us that we are using __main__ logger and not the root logger

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(message)s')

class Employee:
  def __init__(self, first, last):
    self.first = first 
    self.last = last

    logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Cena')
emp_2 = Employee('Brock', 'Lesnar') 
emp_3 = Employee('Randy', 'Ortan')
# =================================
# Here we are still configuring the root looger:- filename, log level and format 
# Configuring our specific logger and leaving our root logger alone

# ### Inside employee.py ###

import logging

logger = logging.getLogger(__name__)

# Setting the log level
logger.setLevel(logging.INFO)

# Adding the formatting to file handler and not the logger
formatter = logging.Formatter('%(asctime)s:%(message)s')

# Specifing the employee log file that we want to log to we have to add file handler and pass our log filename
file_handler = logging.FileHandler('employee.log')

# Adding the formatter to file handler
file_handler.setFormatter(formatter)

# Now when we are having our file handler it need to be added 
logger.addHandler(file_handler)

# Now we don't need basicConfig

class Employee:
  def __init__(self, first, last):
    self.first = first 
    self.last = last

    logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

  @property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Cena')
emp_2 = Employee('Brock', 'Lesnar') 
emp_3 = Employee('Randy', 'Ortan')
# =================================
# Setting a logger in log-sample.py so that we are not using the root logger there either

# ### Inside log-sample.py ###

import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

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

logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# =================================
# Now we have got flexibility due to the hierarchy 

# If say we want to set level as debug but we want our errors to get log to the file that is we just want to capture Errors

# ### Inside log-sample.py ###

import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler = logging.FileHandler('sample.log')

file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    logger.error('Tried to divide by zero')
  else:
    return result

num_1 = 10 
num_2 = 0

logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# =================================
# To include Traceback

# logger.exception('Tried to divide by zero')

# ### Inside log-sample.py ###

import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler = logging.FileHandler('sample.log')

file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    logger.exception('Tried to divide by zero')
  else:
    return result

num_1 = 10 
num_2 = 0

logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result)
)
# =================================
# Now it is easy to add multiple handler to a logger 

# Let's say we want to see debug statements but only want to display it on the console for this we have to create a handler which is a stream handler but not the file handler

# ### Inside log-sample.py ###

import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(message)s')

file_handler = logging.FileHandler('sample.log')

file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
# It is not going to take any argument and we don't need to set the log level since it is already set

stream_handler.setFormatter(formatter)
# Setting a formatter for our stream handler

logger.addHandler(file_handler)

# Adding stream_handler to the logger
logger.addHandler(stream_handler)

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    logger.exception('Tried to divide by zero')
  else:
    return result

num_1 = 10 
num_2 = 0

logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
