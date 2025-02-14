# ###### Client Side ######

# =================================        
# ### Client Side Code ###

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:

    # Send data
    message = b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
# =================================        
# ### Explanation ###

# In this case, we also replace the server_address variable to the file path that has been bound to the server.
