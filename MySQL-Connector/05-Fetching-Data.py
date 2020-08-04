# ###### Fetching Data ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="testing")

# Creating cursor
my_cursor = mydb.cursor()
# =================================
# Executing our query
my_cursor.execute("SELECT name FROM employee")

# ### fetchone ###
results = my_cursor.fetchone()

print(results)

for result in results:
    print(result)
# =================================
# Executing our query
my_cursor.execute("SELECT * FROM employee")

# ### fetchall ###
results = my_cursor.fetchall()

print(results)

for result in results:
    print(result)
# =================================
# Closing the database connection
mydb.close()
