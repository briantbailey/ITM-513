"""
Brian T. Bailey
ITM 513 - MP4
IO Utils Module
"""

import datetime
from message import Message


def load_message(path):
    """Loads Message File into Message Object
  
    Loads from disk a text based message file into a Message Object 
  
    Args:
        path: Path to the message file to load_message
        
    Returns:
        A Message object
    """
    f = open(path, 'r')
    data = f.read()
    f.close()
    messageobj = Message(data)
    return messageobj

    
def write_data(fileptr, data):
    """Writes supplied data to supplied file pointer
    
    Method writes data argument to file described by open fileptr argument.
    
    Args:
        fileptr: A file pointer to a open and writable file
        data: String data you want to write to the file
    """
    fileptr.write(data)


def write_file_header(fileptr, de_size, en_size):
    """Writes top header lines of the server log file
    
    Method to write the top header and data to the server log file.
    
    Args:
        fileptr: A file pointer to a open and writable file
        de_size: An Integer representing the byte size of the decrypted data
        en_size: An Integer representing the byte size of the encrypted data
    """
    d = datetime.datetime.now()
    stringdate = d.strftime('%a %b %d, %Y %H:%M:%S')
    fileptr.write('Message Received at: ' + stringdate + '\n')
    fileptr.write('Total Encryped Message Size: ' + str(en_size) + ' bytes\n')
    fileptr.write('Total Decryped Message Size: ' + str(de_size) + ' bytes\n')
    fileptr.write(('-' * 60) + '\n')
    fileptr.write('DECRYPTED MESSAGE CONTENT\n')
    fileptr.write(('-' * 60) + '\n\n')

    
def write_encrypted_data(fileptr, data):
    """Writes encrypted data header and encrypted data to file
    
    Method to write the encrypted data header and encrypted data to log file.
    
    Args:
        fileptr: A file pointer to a open and writable file
        data: String data you want to write to the file
    """
    fileptr.write(('-' * 60) + '\n')
    fileptr.write('ENCRYPTED MESSAGE CONTENT\n')
    fileptr.write(('-' * 60) + '\n\n')
    fileptr.write(data)


def print_file_terminal(path, filename):
    """Prints a given text file's contents to the terminal console
    
    Args:
        path: A String representing the path to the file (no trailing slash)
        filename: A String representing the filename
    """
    print('-' * 60)
    print('File name: ' + filename)
    print('-' * 60)
    for line in open((path + '/' + filename), 'r'):
        print(line)
    print('\n')