# ###### Client Side ######

# =================================        
import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New message length: {msg[:HEADERSIZE]}")
            msg_length = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg)-HEADERSIZE == msg_length:
            print("Full message received")
            print(full_msg[HEADERSIZE:])
            
            # Unpickling the full_msg (message)
            data = pickle.loads(full_msg[HEADERSIZE:])
            print(data)
            
            new_msg = True
            full_msg = b''
            
print(full_msg)            
