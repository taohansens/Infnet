import socket

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, 5000))
except ConnectionRefusedError as error:
    print(error)

s.send(b"Inicio")
s.close()
