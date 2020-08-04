# ###### Troubleshooting ######

# =================================    
# ### Error in our Code ###
# As we can all attest to, some times things don’t work and more often than not, it’s never obvious why. 
# It could be a issue with the code in which case looking at the errors and traceback could point us in the right direction. 
# In such cases, referring to the official documentation would be the first option.
# =================================    
# ### Other issues ###
# However, sometimes it could be configuration troubles on the client, server, or even the network infrastructure. To probe such issues we could use ping or netstat to identify the source of problems.

# ### ping ###
# ping — works directly with the TCP/IP stack, independent of any other application running on a host, to determine the status of the host, whether it’s up or not. ping works by sending ICMP echo request packets to the target host and waiting for an ICMP echo reply.

# ### netstat ###
netstat — gives information sockets and their current states. Let’s fire up the TCP echo server and observe the output of netstat . From this we can tell that our server is presently using thetcp protocol, listening (state of LISTEN) on port 10000 and host 127.0.0.1 .
