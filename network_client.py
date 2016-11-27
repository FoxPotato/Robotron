import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = '192.168.1.10'
port = 12345

s.connect((address, port))

print(s.recv(1024))
s.close()
