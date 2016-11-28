import socket
import sys
import arraysocket as ars
import numpy as np

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '192.168.1.27'
port = 12345

s.connect((address, port))

print(s.recv(1024))
s.close()
'''

array = np.random.rand(50,3)
print(array)
ars.startclient(array, '192.168.15.113')
