# ###### Server Side ######

# =================================        
# ### Setting Up Server ###

# Here, we’ll only execute the socket() and bind() sequence since, there isn’t really a connection to listen for. 
# Instead we only need to bind the socket to a particular address and wait for incoming messages. 
# We will then read the incoming messages using the recvfrom() method and send them back with sendto().

# - recvfrom() receives data from a socket and return a tuple of (bytes, address) where bytes is a bytes object containing the received data and address is the address of the sender.
# - sendto(bytes,address) sends data(given by bytes) to a socket bound to the address as defined by address .
# =================================        
# ### Server Side Code ###

import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
# =================================        
# ### Explanation ###

# 1. We create a socket object using socket.socket(socket.AF_INET,socket.SOCK_DGRAM). Please note that here we use the socket.socket_DGRAM socket type since we are using UDP.
# 2. Next we bind the socket to the ('localhost',10000) and wait for incoming messages.
# 3. When a message arrives, we proceed to read it with recvfrom(4096), where 4096 is the number of bytes to be read, and unpack the return value in to data and address .At this point we can print out the length of data.
# 4. If some data has been received, we send it back to the sender using the sendto() method and print out the length of the return value — which is the sent data.
