# ###### Introduction to Socket Module ######

# =================================
# Primarily, the way sockets send data is controlled by two properties:
#   1. The address family, which determines the network layer protocol used
#   2. The socket type which determines the transport layer protocol used
# =================================
# ### Socket Types ###

# Depending on the transport layer protocol used, sockets can either be:
#   1. SOCK_DGRAM for message-oriented datagram transport. These sockets are usually associated with the User Datagram Protocol (UDP) which provides an unreliable delivery of individual messages. Datagram sockets are commonly used when the order of messages is not important, such as when sending out the same data to multiple clients.
#   2. SOCK_STREAM for stream-oriented transport often associated with the Transmission Control Protocol (TCP). TCP provides a reliable and ordered delivery of byte between two host, with error handling and control, making it useful for implementing applications that involve transfer of large amounts of data.
# =================================
# Python sockets supports a number of address families under the network layer protocol, mainly:
#   1. AF_INET — This is the most common, and uses IPv4 for network addressing. Most of the internet networking is presently done using IPv4.
#   2. AF_INET6 — This is the next generation of the internet protocol using IPv6 and provides a number of features not available under IPv4.
#   3. AF_UNIX — This is the address family for Unix Domain Sockets (UDS), an inter-process communication protocol available on POSIX-compliant systems. This implementation allows passing of data between processes on an operating system without going through the network.
# =================================
# Importing socket module
import socket
# =================================
# ### Network related services ###

# Methods that provide access to network related tasks
# ---------------------------------
# ### gethostname ###

# We can use gethostname method to get the official name of the current host

print(socket.gethostname())
# ---------------------------------
# ### gethostbyname ###

# gethostbyname converts the name of a server into its numerical address by consulting the operating system’s DNS configuration.

print(socket.gethostbyname("google.com"))
# ---------------------------------
# ### gethostbyname_ex ###

# We can use gethostbyname_ex method to get more naming information about a server

name, aliases, addresses = socket.gethostbyname_ex("google.com")
print(f"Name: {name}, Aliases: {aliases}, Addresses: {addresses}")
# ---------------------------------
# ### gethostbyaddr and getfqdn ###

# We can use gethostbyaddr method to perform a reverse lookup for a domain’s name
# We can use getfqdn method to convert a partial domain into a fully qualified domain name
