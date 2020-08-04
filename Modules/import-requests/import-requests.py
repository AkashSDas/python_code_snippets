# ###### import requests ######

# =================================
# Request Libary is great for getting information from websites but it's not meant to parse that information
# =================================
# Importing requests module
import requests
# =================================
# ### response ###

# ---------------------------------
# 1. get()

# We are sending a GET request, pass the website link to the get method of requests
# The get method gives the response (r --> response) from the website

r = requests.get('http://xkcd.com/353/')
print(r)
# ---------------------------------
# 2. text

# text attribute give the content of response in unicode
print(r.text) 
# It gives html of the page given
# ---------------------------------
# 3. content

r = requests.get('http://imgs.xkcd.com/comics/python.png')

# content attribute give content of response in bytes
print(r.content)
# It prints out the byte from image

# Saving the image
with open('comic.png', 'wb') as f:
    f.write(r.content)
# This is going to save the image in file
# ---------------------------------
# 4. status_code

# To check the status code of the response
print(r.status_code)

# http status code
"""
200 - Success
300 - Redriect
400 - Client Error
500 - Server Error
"""
# ---------------------------------
# 5. ok

# To check errors use the ok attribute 
print(r.ok) 
# For 400 and 500 it gives False
# ---------------------------------
# 6. headers

print(r.headers)
# It gives all the headers of that the page's link that is given
# =================================
# ### params ###

# ---------------------------------
r = requests.get('http://httpbin.org/get?page=2&count=25') 

# You can pass url parameters directly but it can prone to mistakes
# requests libary help us to pass parameter as a dictonary
# ---------------------------------
# 1. params

# Dictonary of parameters
payload = { 'page': 2, 'count': 25} # get parameters
r = requests.get('http://httpbin.org/get', params=payload)

print(r.text)
print(r.url) # urls that was requested
# ---------------------------------
# 2. post()

payload = {'username': 'john', 'password': 'testing'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
# ---------------------------------
# 3. json()

# We are getting json response from httpbin website, json response is very common on working with certain API's

print(r.json()) 
# It created a python dictonary from that json response

r_dict = r.json()
print(r_dict['form'])
# =================================
# ### Basic Authentication ###

# ---------------------------------
# Many web services that require authentication accept HTTP Basic Auth. 
# This is the simplest kind, and requests supports it straight out of the box.
# ---------------------------------
from requests.auth import HTTPBasicAuth

# Making requests with HTTP Basic Auth is very simple
# ---------------------------------
requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
# Response 200
# ---------------------------------
# In fact, HTTP Basic Auth is so common that Requests provides a handy shorthand for using it

requests.get('https://api.github.com/user', auth=('user', 'pass'))
# Response 200
# Providing the credentials in a tuple like this is exactly the same as the HTTPBasicAuth example above
# ---------------------------------
# Sending the username and password
payload = {'username': 'john', 'password': 'testing'}
r = requests.post('http://httpbin.org/post', data=payload)

# Requesting the username='john' with password='testing'
r = requests.get('http://httpbin.org/basic-auth/john/testing', auth=('john', 'testing'))
print(r.text)
print(r) # 200 i.e. Success
# ---------------------------------
r = requests.get('http://httpbin.org/basic-auth/john/testing', auth=('brock', 'testing'))
print(r.text) # there would be no response text
print(r) # 401 unauthorised response code
# =================================
# ### timeout ###

# ---------------------------------
# Set a time timeout if possible, because if you don't set a timeout it would wait indefinitely for ever for request
r = requests.get('http://httpbin.org/basic-auth/akash/testing', timeout=3)
# ---------------------------------
r = requests.get('http://httpbin.org/delay/1', timeout=3)
# Above one has a delay of 1 second and timeout of of 3 second
print(r)
# ---------------------------------
r = requests.get('http://httpbin.org/delay/6', timeout=3)
# above one has a delay of 6 second and timeout of of 3 second
print(r)
# This would create an exception since it will the hit timeout in 3 seconds and there is a delay of 6 second
