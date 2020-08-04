# ###### Server Side ######

# ==========================
# ### Serialization in python ###

# Pickling or Serialization or Flattening in Python is we are converting the python object that we want to send into bytes
# We can send and receive things we pickled in python via sockets. We can pickle objects in python and object are everything in python
# We can also save pickles as files so we don't only transmit pickleed data between two programs, many times we are going to save that Python Object using pickle
# ==========================
# Importing moduels
import time 
import socket 
import pickle 
# ==========================
# ### Basic pickling example ###

# dictonary = {1: "Hey", 2: "There"}
# msg = pickle.dumps(dictonary)
# print(msg)
# ==========================
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} is established!")
    
    data = {1: "Hey", 2: "There"}
    msg = pickle.dumps(data)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg
    
    clientsocket.send(msg)    
