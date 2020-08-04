# ###### Client Side ######

# =================================        
# ### Setting Up Client ###
        
# Unlike a server, a client only needs to execute the sequence of socket and connect methods.        

# - connect method connects the socket to an address
# =================================
# ### Client Side Code ###

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

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

# 1. We initialize a socket object as in the server.
# 2. Next we connect the socket to the same address that the server is listening on, in this case, ('localhost',10000) , using the connect(address) method.
# 3. In a try/finally block, we compose our message as a byte string and use sendall() method on the socket object with the message as an argument.
# 4. We then set up variables amount_received with an initial value of 0 and amount_expected which is just the length of our message, to keep track of the message chunks as we receive them.
# 5. Calling recv(16) on the socket object allows us to receive the message from our server in chunks of 16, and we keep receiving until amount_received is equal to amount_expected .
# 6. Finally we mark the socket as closed.
