import socket
import numpy as np
from cStringIO import StringIO

def startserver(server_address=''):
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((server_address, port))
    server_socket.listen(1)

    print("Waiting for connection")
    (client_connection, client_address) = server_socket.accept()
    print("Connection to %s on port %s" % (client_address, port))

    total_buffer = ''

    while True:
        recv_buffer = client_connection.recv(1024)

        if not recv_buffer:
            break

        total_buffer += recv_buffer
        print("-")

    array = np.load(StringIO(total_buffer))['frame']
    client_connection.close()
    server_socket.close()

    print("Frame received")
    return array

def startclient(server_address, array):
    if not isinstance(array, np.ndarray):
        print("Not a valid numpy array")
        return

    client_socket = socket.socket()
    port = 12345

    try:
        client_socket.connect((server_address, port))
        print("Connected to %s on port %s" % (server_address, port))
    except socket.error, e:
        print("Connection to %s on port %s failed" % (server_address, port))
        print(e)
        return

    f = StringIO()
    np.savez_compressed(f, frame=array)
    f.seek(0)
    out = f.read()
    client_socket.sendall(out)
    client_socket.shutdown(1)
    client_socket.close()

    print("Array sent")
