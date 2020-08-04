# ###### import sqlite3 ######

# =================================
# SQLite is extremely useful when we need some database functionality and we don't want to spend up full fledged database.
# We can use SQLite for small to medium size applications where our database is just going to live on disk or we can use it for testing and prototyping out an application and then if we need to move to larger database then we can later port that over.
# It is extremly easy to use because our database can be a simple file or even it can be a in-memory database that just lives in RAM.
# =================================
# ### Part-1 ###
# =================================
# Importing sqlite3 module
import sqlite3
# ---------------------------------
# ### connect ###

# Using the connect method to create a connection object that represents our database
# Within the connect method we can either pass in a filename where we want to store our data or we can even make an in-memory database

# Passing in a filename in connect method
conn = sqlite3.connect('employees.db')
# The connect method creates the file if it doesn't exist but if the file exist then it just connects to that file


# To do an in-memory database we pass ':memory:' in the connect method
# conn = sqlite3.connect(':memory:')

# We cannot understand .db files, it will look gibberish but sqlite can work with that
# ---------------------------------
# ### cursor ###

# Creating a cursor which allow us to execute SQL commands
cur = conn.cursor()
# ---------------------------------
# ### execute ###

# After creating the cursor we can start running SQL commands using the execute method

# Creating an Employees table
cur.execute("""CREATE TABLE employees(
                first text,
                last text,
                pay integer
            );""")
# Using a doc-string to write sql commands since it allows to write a string that is of multiple lines without any special breaks

# SQLite has few datatypes that might be different to other databases
# ---------------------------------
# ### commit ###

# Using the commit method to commit the current transaction(changes)
conn.commit()
# ---------------------------------
# ### close ###

# Closing the connection to the database
conn.close()
# =================================
# ### Part-2 ###
# =================================
import sqlite3

conn = sqlite3.connect('employees.db')

cur = conn.cursor()
# ---------------------------------
# ### execute ###

# Adding an employee to the employees database
cur.execute("INSERT INTO employees VALUES('Corey', 'Schafer', 50000);")

conn.commit()
# ---------------------------------
# Querying the database

cur.execute("SELECT * FROM employees WHERE last='Schafer';")
# This SELECT statement will return some results that we can iterate through
# ---------------------------------
# To iterate through those query results we can use few different methods

# ### fetchone ###
# cur.fetchone()
# It will give the next row in our results and if no more rows are available then it just returns None

# ### fetchmany ###
# cur.fetchmany(5)
# fetchmany method takes an argument of number(integer) andd it will return that number of rows from results as a list and if no more results are available then it will return an empty list

# ### fetchall ###
# cur.fetchall()
# It will return a list containg the remaining rows and if there is no more rows then it wil return an empty list
# ---------------------------------
print(cur.fetchone())

conn.commit()
# ---------------------------------
conn.close()
# =================================
# ### Part-3 ###
# =================================
import sqlite3

conn = sqlite3.connect('employees.db')

cur = conn.cursor()

# Adding another employee to the employees database
cur.execute("INSERT INTO employees VALUES('Mary', 'Schafer', 70000);")

# Querying the database
cur.execute("SELECT * FROM employees WHERE last='Schafer';")

print(cur.fetchall())

conn.commit()

conn.close()
# =================================
# ### Part-4 ###
# =================================
# Until now we have been hard-coding values into the query statements but we are most likely to put values from a python variable to the query

# ---------------------------------
# Using the employees module

import sqlite3
from employees import Employee
# ---------------------------------
conn = sqlite3.connect('employees.db')

cur = conn.cursor()
# ---------------------------------
# Creating instances 

emp_1 = Employee('Brock', 'Lesnar', 80000)
emp_2 = Employee('John', 'Cena', 90000)
# ---------------------------------
# Inserting employees data to the table

# Using string formatting
cur.execute("INSERT INTO employees VALUES('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

# This is a bad practice to add values to our database not just sqlite3 but for any database we use
# If we are accepting any values from an end user from a website or something like that then this is venerable to SQL injection i.e. users can set values of variable to something that can break the entire database and reason for that is that it is not properly escaped
# ---------------------------------
# So there are two correct ways to do that
# ---------------------------------
# Frist way

cur.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

# Instead of using regular braces({}) we will use question marks(?) and we also will also no longer need quotes('') to specifiy it's a string it will know that by the values we are passing in
# Second argument that we will pass in will be a tuple of values for which the placeholders(?) are set
# Note that even if we are passing in only one value then also we need to use a tuple to pass that value
# ---------------------------------
# Second way

cur.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})
conn.commit()

# Instead of using a question mark as placeholder we use a colon(:) followed by a varible name, and the seecond argument that we pass in a dictonary where keys are those varible names that we have set and there values are those values that we want to set
# This is more readable
# ---------------------------------
# Querying the database

cur.execute("SELECT * FROM employees WHERE last='Schafer';")

print(cur.fetchall())

conn.commit()
# ---------------------------------
conn.close()
# =================================
# ### Part-5 ###
# =================================
import sqlite3
from employees import Employee

conn = sqlite3.connect('employees.db')

cur = conn.cursor()

# Creating instances 
emp_1 = Employee('Brock', 'Lesnar', 80000)
emp_2 = Employee('John', 'Cena', 90000)

# Querying the employees from the employees database

# Using the question mark as placeholder way for querying
cur.execute("SELECT * FROM employees WHERE last=?;", ('Schafer',))
# We need that comma(,) in the tuple for one value also otherwise we will get an error
print(cur.fetchall())

# Using the colon(:) as a placeholder
cur.execute("SELECT * FROM employee WHERE last=:last;", {"last": "Lesnar"})
print(cur.fetchall())

conn.commit()

conn.close()
# =================================
# ### Part-6 ###
# =================================
# Setting the connection to the memory
# This will give us a database that lives in RAM and this is useful for testing if we want a clean database in every run

import sqlite3
from employees import Employee

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

# Creating a table
cur.execute("""CREATE TABLE employees(
             first text,
             last text,
             pay integer
            )""")

# Creating instances 
emp_1 = Employee('Brock', 'Lesnar', 80000)
emp_2 = Employee('John', 'Cena', 90000)

# Inserting employees to the employees database

cur.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
conn.commit()

cur.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})
conn.commit()

# Querying the employees in the employees database

# Using the question mark placeholder way 
cur.execute("SELECT * FROM employees WHERE last=?;", ('Cena',))
# We need that comma(,) in the tuple for one value also otherwise we will get an error
print(cur.fetchall())

# Using the colon(:) as a placeholder
cur.execute("SELECT * FROM employees WHERE last=:last;", {"last": "Lesnar"})
print(cur.fetchall())

conn.commit()

conn.close()

# We can run this program multiple times and not get errors like the table exist since it will clean the previous database every time we run this program
# =================================
# ### Part-7 ###
# =================================
# Creating a mini application for our employees database

import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

# Creating a table
cur.execute("""CREATE TABLE employee(
             first text,
             last text,
             pay integer
            )""")

def insert_emp(emp):
    with conn:
        cur.execute("INSERT INTO employee VALUES(:first, :last, :pay);", {"first": emp.first, "last": emp.last, "pay": emp.pay})
    
def get_emps_by_name(lastname):
    cur.execute("SELECT * FROM employee WHERE last=:last;", {"last": lastname})
    # Since our select statement never needed to be commited so this doesn't needs to be inside a context manager
    return cur.fetchall()

def update_pay(emp, pay):
    with conn:
        cur.execute("""UPDATE employee SET pay=:pay
                       WHERE first=:first AND last=:last;""",
                   {"first": emp.first, "last":emp.last, "pay": pay})

def remove_emp(emp):
    with conn:
        cur.execute("DELETE from employee WHERE first=:first AND last=:last;", {"first":emp.first, "last":emp.last})

emp_1 = Employee("Brock", "Cena", 90000)
emp_2 = Employee("John", "Cena", 100000)        

insert_emp(emp_1)
insert_emp(emp_2)
        
emps = get_emps_by_name("Cena")    
print(emps)

update_pay(emp_2, 95000)

remove_emp(emp_1)
    
emps = get_emps_by_name("Cena")    
print(emps)    
    
conn.close()
