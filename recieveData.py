# This is a test file to show the successful transfer of multiple data types and array formats
# Run simultaneously with baseStation_test.py on the Pi
# 
# To use, enter the computer's IPv4 address as an argument when running the file
# If no argument is entered, it will ask you for the IPv4 address before running anyways.

import socket
import struct
import sys
from numpy import array
import compTalk as ct

pi = ct.CompTalk( '192.168.42.11')
pi.buffer = 24

while True:

    content = pi.getData(showRawData=False)
    
    print('Recieved: ', content)