# ###### Blocking and Timeouts ######

# =================================        
# By default, sockets operate in a blocking mode. This means that sending or receiving data pauses execution of the program until the the socket that’s receiving or sending data is ready. Sometimes, this mode of operation can result in a dreadlock whereby both endpoints are waiting for the other to send or receive data.

# ### setblocking ###
# To try and overcome this challenge, sockets have an option to unset blocking, using the method socket.setblocking() , which has a default value of 1, i.e blocking is on. To disable blocking we call socket.setblocking(0). However, this presents yet another challenge; if a socket is not ready for an operation with blocking disabled, then a socket.error is raised.

# ### settimeout ###
# Another solution therefore, involves setting a timeout, using socket.settimeout(float) to a number(float) of seconds during which blocking is on before evaluating whether the socket is ready or not. This timeout method is applicable in most cases since it acts as a compromise between blocking and not blocking.
