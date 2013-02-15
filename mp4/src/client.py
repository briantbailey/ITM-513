"""
Brian T. Bailey
ITM 513 - MP4
Client program file
"""

import sys
from socket import *
from  mp4domain.crypto import *
import mp4domain.ioutils


# Configure client for server address
server_hostname = 'localhost'
server_port = 48001

# Process Message File and send to server
if len(sys.argv) > 1:
    messageobj = mp4domain.ioutils.load_message(sys.argv[1])
    key = key_gen(sys.argv[2])
    encrypted_message = bb_encrypt(messageobj.message_text, key)
        
    socketobj = socket(AF_INET, SOCK_STREAM)
    socketobj.connect((server_hostname, server_port))
    print('Client: Connected to server ' + server_hostname + '...')
    
    socketobj.send(key)
    socketobj.sendall(encrypted_message)
    socketobj.close()
    print('Client: Message data sent to server ' + server_hostname)
else:
    print('No Arguments to Specify Message File and Encryption Password')