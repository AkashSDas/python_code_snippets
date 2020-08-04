# ###### Client Side ######

# =================================        
# ### Setting Up Client ###

# Client is similar to the Server side, only that it doesn’t bind the socket to any address. 
# Instead, the it uses sendto() to send messages to the server’s address.
# =================================        
# ### Client Side Code ###

import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is our message. It will be sent all at once'

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
# =================================        
# ### Explanation ### 

# 1. We instantiate a sock object as in the server above.
# 2. We then compose a message as a byte string, and define a server_address as a tuple of the host and the port number bound to the server we wish to send messages to.
# 3. Inside a try/finally block, we send the message and wait for a response, printing the the data in both cases.
# 4. Finally we mark the socket as closed.
