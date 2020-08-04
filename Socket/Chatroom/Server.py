# ###### Chatroom Server Side ######

# =================================        
import socket

import select
# The way we are going to manage many connections is with using the select module
# It gives us OS level IO capabilties keeping sockets in mind, so in Windows it will be different then in Linux and because of that Python has select that allows us to utilize that without needing to get into the details, so this code will run the same wethere you be on Mac/Linux/Windows

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# To not to again and again change port numbers to rerun things, one option is overcome this issue is setsockopt method and it takes 3 arguments (first is the thing that we want to set, second is what we want to set of that thing and third is setting the thing). Here 1 as third argument in setsockopt method is for True.
# This will allow us to reconnect

server_socket.bind((IP, PORT))
server_socket.listen()

# Managing list of sockets
sockets_list = [server_socket]
# The list can be empty but we already have one socket and that is server_socket
# We will also have clients in this list

# We can report the client to other clients other than their IP and PORT
# For that we can make a dictonary of clients
clients = {}
# Here the key will be clients socket and the value will be user data will be the value

# Receiving messages
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH) 
        
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip())
        # We don't need the strip function there it is just for undersatnding the conversion, but with Python we can get away without using the string function
        
        return {"header": message_header, "data": client_socket.recv(message_length)}
    
    except:
        return False
    
# By now we are able to receive messages

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    # select.select() takes three parameters first is read list(things that we want read in), second is write list and third one the sockets that we might error on
    
    # ### Our Main Logic ###
    
    for notified_socket in read_sockets:
        
        # If someone connects to accept that connection and handle for it
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            
            user = receive_message(client_socket)
            
            # If someone disconnected
            if user is False:
                continue
                
            sockets_list.append(client_socket)
            clients[client_socket] = user
            
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
            
        # There is a message we want to handle it     
        else:
            message = receive_message(notified_socket)
            
            if message is False:
                print(f"Close connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
                
            user = clients[notified_socket]
            print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
            
            # Sharing this message with everybody
            for client_socket in clients:
                # The below condition is not to send the message back to sender
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                    
    # For errors 
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
