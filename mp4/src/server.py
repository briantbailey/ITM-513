"""
Brian T. Bailey
ITM 513 - MP4
Server program file
"""

from socket import *
from mp4domain.crypto import *
from mp4domain.ioutils import *


# Configure Server
HOSTNAME = ''
PORT = 48001

# Create Socket Object, bind to host/port, listen for connections
socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.bind((HOSTNAME, PORT))
socketobj.listen(5)

# Infinite loop to listen for connections and process connections
loop_counter = 0
while True:
    connection, address = socketobj.accept()
    print('Server: Client connected to from ' + str(address))
    message_buffer = ''
    while True:
        data = connection.recv(1024)
        if not data: break
        message_buffer += data
    
    print('Server: Message Received from ' + str(address))
    decrypted_message = bb_decrypt(message_buffer[32:], message_buffer[:32])
    
    # Write Message Log
    f = open(('serverdata/server_message' + str(loop_counter) + '.txt'), 'w')
    write_file_header(f, len(decrypted_message), len(message_buffer[32:]))
    write_data(f, decrypted_message)
    f.write('\n\n\n')
    write_encrypted_data(f, message_buffer[32:])
    f.close()
    
    loop_counter += 1
    connection.close()