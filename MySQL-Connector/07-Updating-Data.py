# ###### Updating Data ######

# =================================
# Importing mysql.connector
import mysql.connector
# =================================
# Creating our connect object
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="testing")

# Creating cursor
my_cursor = mydb.cursor()
# =================================
# Query
query = "UPDATE employee SET salary=2000000 WHERE name='babu rao'"

# Executing the query
my_cursor.execute(query)

# Commiting changes
mydb.commit()
# ===============================
# Retriving data
my_cursor.execute("SELECT * FROM employee")
results = my_cursor.fetchall()
print(results)

for result in results:
    print(result)
# =================================
# Closing the database connection
mydb.close()
