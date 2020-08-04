# ###### Introduction to Socket ######

# =================================
# What is a socket?
#   A socket is one endpoint of a two-way communication link between two programs running on (a node in) a computer network
#   One socket (the server) listens on a particular port on and IP address, while another socket(the client) connects to the listening server to achieve communication
# =================================
# Server forms the listener socket while client reaches out to the server
# They are the real backbones behind web browsing 
# In simpler terms there is a server and a client
# =================================
# Primarily, the way sockets send data is controlled by two properties:
#   1. The address family, which determines the network layer protocol used
#   2. The socket type which determines the transport layer protocol used
# =================================
# Socket is just the endpoint (generally there are two endpoint for communication) that receives data, so it is just the endpoint that receives data, so with socket with send and receive data, so the socket is itself not a communication it is just an endpoint that recevies that communication and that enpoint sits on an IP and a PORT
