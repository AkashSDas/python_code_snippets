# ###### Server Side ######

# =================================        
import time
import socket

# We need to handel sockets that exceed our buffer because we don't want to close our connection because we want to keep our stream open. Generally we will use header
# We can do a lot of things with header
# Header is going to notify our program on how long is our message and maybe it will give some extra information about our message

# We are using a fixed length header which is a good practice

"""
msg = "Welcome to the server!"
print(f"{len(msg):<10}"+msg)
"""

# Our buffer should be always more than enough to handel our header size
# =================================
# Our header
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    
    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}" + msg
    
    clientsocket.send(bytes(msg, "utf-8"))
    
    while True:
        time.sleep(3) 
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        clientsocket.send(bytes(msg, "utf-8"))        
