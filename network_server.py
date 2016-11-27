import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345

s.bind(('', port))
print("Socket bound to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    client, addr = s.accept()
    print("Established connection with %s" % str(addr))

    client.send("Connection acknowledged")
    client.close()
