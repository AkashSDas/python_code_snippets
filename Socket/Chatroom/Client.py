# ###### Chatroom Client Side ######

# =================================
# Our client does three things and those are:
#     1. On immediate connection they give their username
#     2. Send messages
#     3. Receive messages

import sys
import socket
import select

import errno
# To match some specific error codes we are using erron module
# We will try to receive messages until we can't and when we can't then we will get an error and we want to make sure that those are specific errors and not some other errors
# So we want to make sure that there is an error because message is not received and not because of something like there something wrong with message or code

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

# By doing this receive functionality won't be blocking
client_socket.setblocking(False)

# Sending the username to server
username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username) 
# Users can't change their names
# Since thats why this isn't in forever loop

while True:
    message = input(f"{my_username} > ")
    
    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message) 
        
    try:
        while True:
            # To receive the messages    
            username_header = client_socket.recv(HEADER_LENGTH)
            
            # If we didn't get any message
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
                
            # Getting the username    
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")
            
            # Getting the message
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")
            
            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("Reading error", str(e))
            sys.exit()            
        continue
    
    except Exception as e:
        print("General error", str(e))
        sys.exit()
