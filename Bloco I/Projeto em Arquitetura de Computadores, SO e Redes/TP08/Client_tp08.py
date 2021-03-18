import socket
import pickle

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Server iniciado na AWS
    s.connect((host, 5001))
except ConnectionRefusedError as error:
    print(error)


s.send(b"Ola")
memory = pickle.loads(s.recv(10000))
print(memory)
s.close()
