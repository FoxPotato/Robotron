import socket
import sys
import arraysocket as ars
import numpy as np

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '192.168.1.27'
port = 12345
print(address)

s.bind((address, port))
print("Socket bound to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    (client, addr) = s.accept()

    
    print("Established connection with %s" % str(addr))

    client.send("Connection acknowledged")
    client.close()
'''

array = ars.startserver()
print(array)


