# ###### Server Side ######

# =================================        
# ### Server Code ###

import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'

# Make sure file doesn't exist already
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# Bind the socket to the port
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()
# =================================        
# ### Explanation ###        

# 1. Here we alter the server_address variable in the script to a file system path, in this case ./socket_file .
# 2. Since we also need to make sure the node doesn’t already exist when starting the server, we use a try/except block to delete the file using os.unlink() if it exists.
