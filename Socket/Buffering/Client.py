# ###### Client Side ######

# =================================        
import socket

# Our header
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msg_length = int(msg[:HEADERSIZE])
            # In above conversion it contains some spaces but figures out but in other language we have strip to get rid of extra spaces
            new_msg = False
        
        full_msg += msg.decode("utf-8")
        
        if len(full_msg)-HEADERSIZE == msg_length:
            print("Full message received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
        
    print(full_msg)    
