# ###### Regular Expression (Regex) in Python ######

# =================================
import re

# raw string is a string prefix with r, it tells python not to treat backslah(\) in a special way
# Example:
# print('\tTab') 
# print(r'\tTab') ---> raw string 
# =================================
# Text to perform operations

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789
Ha HaHa
Metacharacter (Need to be escaped):
. ^ $ * + { } [ ] \ | ( )
akashdas.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
bat
"""

sentence = "Start a sentence and then bring it to an end"
# =================================
# To get pattern that you want

# compile(pattern, repl, string): We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search a pattern again without rewriting it.
pattern = re.compile(r'.')

# finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
matches = pattern.finditer(text_to_search) 

for match in matches:
    print(match)
# =================================
"""
 Types of character that can be matched
 
.   : Any character except new line
\d  : Digit (0-9)
\D  : Not a Digit (0-9)
\w  : Word Character (a-z, A-Z, 0-9, _)
\W  : Not a word Character
\s  : Whitespace (space, tab, newline)
\S  : Not Whitespace (space, tab, newline)

Anchors: They don't match any character but rather invisible positions before or after characters
\b  : Word boundary
\B  : Not a word boundary
^   : Beginning of a string
$   : End of a string 
[]  : Matches Characters in brackets, character set only matches one character from given characters 
[^ ]: Matches Characters NOT in brackets

Quantifiers:
*     : 0 or More
+     : 1 or More
?     : 0 or 1
{3}   : Exact Number
{3,4} : Range of Numbers (Minimum, Maximum)
|   : Either or
()  : Group

### Sample Regex ###
 [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""    
# =================================
#  Examples of searching patterns 

pattern = re.compile(r'.')
pattern = re.compile(r'\.')
pattern = re.compile(r'\d')
pattern = re.compile(r'\D')
pattern = re.compile(r'\w')
pattern = re.compile(r'\W')
pattern = re.compile(r'\s')
pattern = re.compile(r'\S')
pattern = re.compile(r'\bHa')
pattern = re.compile(r'\BHa')
pattern = re.compile(r'^Start')
pattern = re.compile(r'^sentence')
pattern = re.compile(r'end$')
pattern = re.compile(r'a$')
pattern = re.compile(r'\d\d\d')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') 
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[1-5]')
pattern = re.compile(r'[a-zA-Z]')
pattern = re.compile(r'[^a-zA-Z]')
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# =================================
# ### findall ###

# Use the patterns with findall method

# findall() returns the matches as list of strings

# If it matches groups it will only return groups
# If there are multiple groups it will return a tuple
# If there are no groups then it will return all of the matches

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # it will return just the group
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 

matches = pattern.findall(text_to_search)
# =================================
# ### finditer ###

# finditer() method returns match object with extra information and extra functionalities
# ================================= 
# ### match ###

# Use the patterns with match method

# match() method attempts to match pattern to whole string. The re.match() function returns a match object on success, None on failure.

pattern = re.compile(r'Start') 
pattern = re.compile(r'sentence') # returns NONE

matches = pattern.match(text_to_search)
# =================================  
# ### search ###

# Use these patterns with search method 

pattern = re.compile(r'Start') 
pattern = re.compile(r'sentence')
pattern = re.compile(r'dne')  # dne doesn't exit 

# It print's out the first match it found
matches = pattern.search(text_to_search) 
# =================================  
# ### Flags ###
 
pattern = re.compile(r'[Ss][Tt][Aa][Rr][Tt]') 
pattern = re.compile(r'start',re.IGNORECASE)
pattern = re.compile(r'start',re.I) # shorthand for IGNORECASE

# There are other flags also
# =================================  
# Example:

emails = """
johnjones@gmail.com
john.jones@gmail.edu
john-321-jones@my-work.net
"""

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
# =================================  
# Example:

urls = """
https://www.google.com
http://akashdas.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')  # same as above

matches = pattern.finditer(urls)

for match in matches:
    print(match)

for match in matches:
    print(match.group(0))  # 0 gives everything    
    
for match in matches:
    print(match.group(1))

for match in matches:
    print(match.group(3))

subbed_url = pattern.sub(r'\2\3',urls)  # back reference to reference our back reference    
print(subbed_url)    
# =================================
# ### Difference between re.search() and re.match() ###

# There is a difference between the use of both functions. Both return first match of a substring found in the string, but re.match() searches only in the first line of the string and return match object if found, else return none. But if a match of substring is found in some other line other than the first line of string (in case of a multi-line string), it returns none.
# While re.search() searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string.
