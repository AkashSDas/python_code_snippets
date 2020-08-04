# ###### Server Side ######

# ================================= 
# Importing socket module
import socket

# ---------------------------------
# Creating our socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket family type is AF_INET and actual type of socket is SOCK_STREAM
# AF_INET corresponds to ipv4 and SOCK_STREAM corresponds to TCP
# This is going to be a streaming socket
# ---------------------------------
# Binding our socket object to a tuple
s.bind((socket.gethostname(), 1234))

# The tuple can be different based on cases but here owing to the type of socket it is, it is just going to contain an IP and a PORT
# Here we are hosting the server on the same machine where the code is, So we are binding to socket.gethostname() (basically localhost) and PORT we are using is 1234 (we can use any of the 4 digit PORT)
# ---------------------------------
# This is a server and we are going to make some connections so the server has to be prepared for incoming connections
s.listen(5)

# This server is going to prepare and leave a queue of 5
# If multiple connections are coming so fast that it can't response quickly enough and start stacking up then we will have a queue of 5
# ---------------------------------
# Listening forever for connections

while True:
    clientsocket, address = s.accept()
    # Anybody can connect
    # We are storing clientsocket object in clientsocket variable and address is where are the conncetions coming from this would be there IP address basically
    # clientsocket object is just like any other socket object, like s(The scoket object we created). We can send information to this socket and this socket will receive information
    
    print(f"Connection from {address} has been established!")
    
    # We are sending information to the client socket, clientsocket object is a socket object but it is a foreign socket object
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    # We are passing what we want to sent to clientsocket in the send method
# ================================= 
# To buffer the entire data

# while True:
#     clientsocket, address = s.accept() 
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))
#     clientsocket.close()
