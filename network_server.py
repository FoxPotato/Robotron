import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
while True:
    # Find connections
    connection, client_address = sock.accept()
    try:
        data = connection.recv(999)
        print data

    except:
        connection.close()
