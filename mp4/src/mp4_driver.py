"""
Brian T. Bailey
ITM 513 - MP4
MP4 Main Driver
"""

from ftplib import FTP
import subprocess
from mp4domain.ftpconfig import *
from mp4domain.ioutils import print_file_terminal
from mp4domain.ServerThread import ServerThread


# Start the server thread
server = ServerThread()
server.daemon = True
server.start()
print('\nMP4 Driver: Server Thread Started...\n')

# Use subprocess module to call client scripts with arguments
# This simulates someone running the client script from the terminal window
# Client script requires 2 arguments, message file and encryption password
subprocess.call(['python', 'client.py', 'clientdata/client_message0.txt', 
                'a password'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message1.txt', 
                'a different password'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message2.txt', 
                'S54kq!^skU3'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message3.txt', 
                'S5@3#q!^ssDD3'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message4.txt', 
                'ITM513-mp4'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message5.txt', 
                'jiYY8&%jp!v'])
print(' ')
subprocess.call(['python', 'client.py', 'clientdata/client_message6.txt', 
                'BBBu**a12ka7'])
print(' ')

# Use ftplib to download log files server process produces
print('MP4 Driver: Proceeding to download server logs with FTP\n')
ftp = FTP(FTPHOST, FTPUSER, FTPPSSWD)
ftp.cwd('/mp4/serverdata')
filelist = []
ftp.retrlines('NLST', lambda x: filelist.append(x))
for i in filelist:
    f = open(('ftpreceived/' + i), 'wb')
    ftp.retrbinary(('RETR ' + i), f.write)
    f.close()
    print('MP4 Driver: Downloaded ' + i + ' from server.')
ftp.quit()
print('MP4 Driver: Finished downloading server log files.')

# Show files downloaded by ftp
for i in filelist:
    print_file_terminal('ftpreceived', i)
    print(' ')

print(' ')
print('MP4 Driver: Application Terminating...Server exiting...\n')