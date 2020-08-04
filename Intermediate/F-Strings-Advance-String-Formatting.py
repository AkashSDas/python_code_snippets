# ###### F-Strings - Advance String Formatting ######

# Can be used in python 3.6 and higher versions of python

# =================================
# 1.
first_name = "James"
last_name = "Gunn"

sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)
# =================================
# 2.
person = {'name':'Robert', 'age':49}

sentence = f"My name is {person['name']} and age is {person['age']}" 
# Take care of double and single quotes
print(sentence)
# =================================
# 3.
calculations = f'4 time 11 is {4*11}'
print(calculations)
# =================================
# 4. To add leading 0's
for n in range(1,11):
    sentence = f'The value is {n:03}'
    print(sentence)
# =================================
# 5. To format till a specific decimal point
pi = 3.14159265

sentence = f'Value of pi is {pi:.4f}'
print(sentence)
# =================================
# 6.
from datetime import datetime

birthday = datetime(1769, 4 ,7)

sentence = f'Mirror had a birthday at {birthday:%B %d %Y}'
print(sentence)
