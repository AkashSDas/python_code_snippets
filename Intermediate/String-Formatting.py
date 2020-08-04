# ###### String Formatting ######

# =================================
person = {'name':'john','age':23}

# ---------------------------------
# 1. String Concatenation

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old ' 
print(sentence)

# Not a good way for String Formatting
# ---------------------------------
# 2. Using the format method

sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])
print(sentence)
# ---------------------------------
# 3. Explicitly numbering the placeholder

sentence = 'My name is {0} and I am {1} years old'.format(person['name'],person['age']) 
print(sentence) 

# Useful when you want placeholder where values need to be repeated
# Example:
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)
# ---------------------------------
# 4. Access the dictionary items

sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person,person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)
# ---------------------------------
# 5. Access list items

list = ['robert',49]

sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(list)
print(sentence)
# ---------------------------------
# 6. Access the attributes

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Person('jack','34')

sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)
# ---------------------------------
# 7.
sentence = 'My name is {name} and I am {age} years old'.format(name='jenn',age='30')
print(sentence)
# ---------------------------------
# 8. For unpacking dictionary

person = {'name':'undertaker','age':63}

sentence = 'My name is {name} and I am {age} years old'.format(**person) # unpacking the dictionary
print(sentence)
# ---------------------------------
# 9. To add leading 0's

for i in range(0,11):
    sentence = 'The value is {}'.format(i)
    print(sentence)
    
for i in range(0,11):
    sentence = 'The value is {:02}'.format(i)  # by 02 means format upto 2 decimal 
    print(sentence)
    
for i in range(0,11):
    sentence = 'The value is {:03}'.format(i)  # by 03 means format upto 3 decimal 
    print(sentence)
# ---------------------------------
# 10. To format till a specific decimal place

pi = 3.1413453

sentence = 'Pi is equal to {:.2f}'.format(pi) 
print(sentence)
# .2f displays upto 2 decimal 
# .3f will display upto 3 decimal
# ---------------------------------
# 11. Add some delimiter

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)  # comma(,) separated
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
# ---------------------------------
# 12. Example

import datetime

my_date = datetime.datetime(2019,8,1,10,22,45)
print(my_date)

sentence = '{:%B %d %Y}'.format(my_date)  # its ok to not know the % value , just go to python documentation
print(sentence)

sentence = '{0:%B %d %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
