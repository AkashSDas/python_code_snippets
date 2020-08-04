# ###### Server Side ######

# =================================
# ### Setting Up Server ###

# To set up a server, it must perform the sequence of methods socket, bind, listen, and accept

# - socket() creates a new socket given the address family and a socket type
# - bind() binds our socket object to a particular address composed of a host and port number
# - listen() allows the server to start accepting connections and takes in an argument, backlog, which is the number of unaccepted connections that the system can allow before refusing all new connections
# - accept() accepts incoming connections and returns a a tuple of (conn, address) where conn is a new socket that can be used to send and receive messages from the connection and address is the address bound to the socket on the other end of the connection
# - close() marks the socket as closed and can no longer accept connections
# =================================
# ### Server Side Code ###

import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
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

# 1. We initialize a socket object, sock by passing in the address family ( socket.AF_INET) and socket type ( socket.SOCK_STREAM) to the socket.socket() function.
# 2. Next, we bind the socket object to an address of the form ('localhost',10000) — bind to localhost on port 10000 , using the bind() method.
# 3. Listen for incoming connections with a backlog of 1.
# 4. Continuously wait for and accept connections by calling sock.accept() and unpacking the return value into connection and client_address .
# 5. Call recv(16) on the returned connection to receive the data on chunks of 16.
# 6. If data as been received, then we transmit the received data back to the sender by calling the method sendall(data) on the connection, otherwise we print out a statement indicating no data has been received.
# 7. Finally when communication with the client is complete — all the chunks of the message have been transmitted, we call close() on the connection object. We use a try/finally block to ensure that close() is called even in the event of an error when transmitting messages.        
