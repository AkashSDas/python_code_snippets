# ###### import json ######

# =================================
# json full form is JavaScript Object Notation
# It was inspired by JavaScript but now is independent of anyone language. Now a days every programming language have libaries for parsing and generating json data
# It is a very common data format for storing some information.
# We will see it when we are fetching data from online API's, in configuration files and different kinds of data that can be stored in our local machines
# json is a part of in-built libary in Python so no need to install it
# =================================
# Importing json module
import json
# =================================
# ### Converting json string to python object ###

# This is just a python string that looks like a valid json
people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "615-555-7164",
      "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
      "has_license": false
    },
    {
      "name": "Jane Doe",
      "phone": "560-555-5153",
      "emails": null,
      "has_license": true
    }
  ]
}
'''

# ---------------------------------
# ### loads ###

# To load json string to a Python Object so that we can work with data more easily 
data = json.loads(people_string)

print(data)

print(type(data))
# The json data is converted to python dictonary object
# ---------------------------------
"""
JSON string transition to Python objects
Whenever we convert a JSON string to Python object the respective types of JSON data are converted to respective types of Python data

JSON         | Python
=================================
object       | dict
array        | list
string       | str
number(int)  | int
number(real) | float
true         | True
flase        | False
null         | None
"""
# ---------------------------------
# All transitions had taken place
# Now we can access data from dictonary, list and so on
print(type(data['people']))

for person in data['people']:
  print(person['name'])
  
# Now we have loaded json string into python object so we can work with them easily
# =================================
# ### Converting python object to json string ###

# ---------------------------------
# ### dumps ###

# To convert python object to json string, for this we will use dumps method
# ---------------------------------
# Now let's say we want to remove the phone numbers and converted it back to json string
for person in data['people']:
  del person['phone']

print(data)
# Phone number data is removed
# ---------------------------------
# Converting python object to json string using the dumps method

new_string = json.dumps(data)
print(new_string)
# ---------------------------------
# Since it is a string it will be nice to format the string so that we can read it easily
# This is done by indent parameter of the dumps method
# indent = number of indentation per item in the string

new_string = json.dumps(data, indent=2)
print(new_string)
# ---------------------------------
# If you want to sort the keys

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
# =================================
# ### Loading json file into python objects ###

# ---------------------------------
# To load data from a json file there are two methods:
#   1. load method  - loads a json file into python object 
#   2. loads method - load a json string into python object
# ---------------------------------
# Using a context manager to work with states.json file

with open('states.json', 'r') as f:
  data = json.load(f)
# ---------------------------------
for state in data['states']:
  print(state)
# ---------------------------------
for state in data['states']:
  print(state['name'], state['abbreviation'])
# =================================
# ### Write python objects to json files ###

# ---------------------------------
# To write python objects to json file there are two methods:
#   1. dump method  - converts python object to json file
#   2. dumps method - converts python object to json string 
# ---------------------------------
# Removing a key from python dict

for state in data['states']:
  del state['area_codes']
# ---------------------------------
# Writing to json file

with open('new_states.json', 'w') as f:
  json.dump(data, f)
  # data --> what we want to dump
  # f --> where you want to dump
  
# In dump method the first parameter is what we want to dump and second parameter is where you want to dump
# ---------------------------------
# Since the data dumped is not easy to read so we will pass the indent parameter to dump method

with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)
# =================================
# Real World Example: Websites returns json from their api which we can be parsed

# ---------------------------------
# Using the requests libary to do the task

# Using requests libary to get json data from api
import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

response = requests.get(url=url, params=params)
# One common way to customize a GET request is to pass values through query string parameters in the URL. To do this using get(), you pass data to params.
# By passing the dictionary to the params parameter of .get(), you are able to modify the results that come back from the Search API.

data = response.json()

print(data)
print(type(data))
# ---------------------------------
# Using the urllib libary to do the task

# We can also use built-in urllib module to get json data from api and convert it to python object
from urllib.request import urlopen

url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"

with urlopen(url) as response:
  source = response.read()

print(source)

data = json.loads(source)
print(data)
print(type(data))
