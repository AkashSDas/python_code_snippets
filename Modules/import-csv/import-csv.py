# ###### import csv ######

# =================================
# csv stands for "comma(,) separated values"
# =================================
# ### Objectives ###
# 1. Read CSV Files
# 2. Parse CSV Files
# 3. Write CSV Files
# =================================
# CSV files allow us to put some data in a plane text and use some type of delimiter usually comma(,) to separate different fields
# We can also use other types of dilimters
# =================================
# Importing csv module
import csv 
# =================================
# ### Reading a CSV file ###

# Using the reader method to read the content of the csv file
# In the background that reader method is using something called dialect that has some preset parameters of it expects the format of csv file, so by default it is expecting values to be separated by comma(,)  
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Since our csv file data is simple we don't need to pass extra arguments   
    print(csv_reader) 
    # If we print it just like this then it will return just an object in the memory
# ---------------------------------
# We have to iterate over the csv_reader variable that we created to get each line in the csv file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
        # This will print list for each line where the elements will be comma separated values
# ---------------------------------
# To print just emails in our csv file whose index is 2
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line[2])
# ---------------------------------
# To step over the first line which contains our header we'll use the next() method
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_file)
    for line in csv_reader:
        print(line[2])
    # Now the first line will not be printed and our csv_reader will be iterated from second line
# =================================
# ### Writing to a CSV file ###

# We will write the content of names.csv to new_names.csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('new_names.csv', 'w') as new_file:
        # We will use the writer method to write to a file
        csv_writer = csv.writer(new_file, delimiter='-')
        # If we didn't specifiy the delimiter then by default the values will be separated by comma(,)

        for line in csv_reader:
            csv_writer.writerow(line)
            # This will write each line of names.csv into new_names.csv
      
# We will see that by default qoutes are added around the values having dash(-), to tell difference between values and delimiters 
# =================================
# ### Using someother delimiter ###

# Here we have use '\t' that is tab as delimiter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('new_names2.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)
# =================================
# ### To read a csv file whose delimiter is different than comma(,) we have to use delimiter argument in the reader() method ###

# Here we have a csv file where values are separated by dash(-)
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="-")  
    for line in csv_reader:
        print(line)        
# =================================
# So far we have been working with csv files using the reader and writer methods
# But Dictonary Reader and Writer Methods are prefered so that we can parse data easily and it also increase code readability        
# =================================
# ### Dictonary Reader and Writer Methods ###

with open('names.csv', 'r') as csv_file:
    # To read the content of csv file we use the DictReader method
    csv_reader = csv.DictReader(csv_file)
    with open('new_names3.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']      
        # To write to a csv file we use the DictWriter method
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        # Here passing the fieldnames list that we created to fieldnames argument to set the headers for different columns

        # To write the header names (if you need) use the writeheader method
        csv_writer.writeheader()

        for line in csv_reader:
            # To delete the email row using the del keyword
            del line['email']
            # Using the writerow method to write rows to the specified file
            csv_writer.writerow(line)
