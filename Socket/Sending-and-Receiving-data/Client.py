# ###### Client Side ######

# =================================   
# Importing socket module
import socket
# ---------------------------------
# Creating our socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Often is the case that our client is going to be remote to our server it is won't be on the same machine, so with sockets we can communicte to-and-fro python programmes on the same machine or locally networked set of machines or remotely networked machines, So it doesn't matter because in most cases we are not going to use socket.gethostname we will actually connect to local IP or public IP or something like that
# ---------------------------------
# This socket rather than binding it need to be connected
s.connect((socket.gethostname(), 1234)) 
# =================================        
# Accepting the message that was send
msg = s.recv(1024)

# We pass in a buffer (here it is 1024), the TCP socket (socket.SOCK_STREAM) is a stream of data so since we have a stream we have to decide how big chunk of the data we want to receive at a time.
# What we want to pass really depends on what we are trying to do

print(msg.decode("utf-8"))

# Here how the sockets are communicating atleast for type-socket that we established here is of byte-stream, so receivers have sended bytes we have received bytes and we are decoding bytes
# Due to this block our socket will be just open and get closed but that not what we want
# =================================        
# To solve above problem i.e. to buffer the entire data sent

# while True:
#     msg = s.recv(8)
#     print(msg.decode("utf-8"))
# =================================        
# To buffer the entire data we can also use the below logic but for this we have to close the socket (clientsocket.close()) in our server side code

# full_msg = ""
# while True:
#     msg = s.recv(8)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
# 
# print(full_msg)
