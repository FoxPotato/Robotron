import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        message=raw_input('Message: ')
        if message=='quit':
            break
        sock.sendall(message)
    except:
        break
sock.close()
