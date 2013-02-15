"""
Brian T. Bailey
ITM 513 - MP4
ServerThread Class File
"""

from socket import *
import threading
from crypto import *
from ioutils import *


class ServerThread(threading.Thread):
    """Runable server thread to process messages from clients
    
    A runnable thread class that allows the server program to be run as a
    thread.
    """
    
    def __init__(self):
        """Initializes the ServerThread Class"""
        # Configure Server
        self.HOSTNAME = ''
        self.PORT = 48001
        
        # Create Socket Object, bind to host/port, listen for connections
        self.socketobj = socket(AF_INET, SOCK_STREAM)
        self.socketobj.bind((self.HOSTNAME, self.PORT))
        self.socketobj.listen(5)
        self.loop_counter = 0
        threading.Thread.__init__(self)

    def run(self):
        # Infinite loop to listen for connections and process connections
        while True:
            connection, address = self.socketobj.accept()
            print('Server: Client connected to from ' + str(address))
            message_buffer = ''
            while True:
                data = connection.recv(1024)
                if not data: break
                message_buffer += data
    
            print('Server: Message Received from ' + str(address))
            decrypted_message = bb_decrypt(message_buffer[32:], message_buffer[:32])
    
            # Write Message Log
            f = open(('serverdata/server_message' + str(self.loop_counter) + '.txt'), 'w')
            write_file_header(f, len(decrypted_message), len(message_buffer[32:]))
            write_data(f, decrypted_message)
            f.write('\n\n\n')
            write_encrypted_data(f, message_buffer[32:])
            f.close()
    
            self.loop_counter += 1
            connection.close()