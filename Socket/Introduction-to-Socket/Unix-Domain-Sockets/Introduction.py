# ###### Unix Domain Sockets ######

# These are largely similar to TCP sockets with basically two exceptions:
#   1. The socket address in this case is a path on the file system such as ./socket_file unlike in the TCP sockets where the address was a tuple of a host name and a port number.
#   2. Since the node created to represent the socket is a file, it persists even after the socket is closed, and as such it’s supposed to be removed whenever the server starts up.
