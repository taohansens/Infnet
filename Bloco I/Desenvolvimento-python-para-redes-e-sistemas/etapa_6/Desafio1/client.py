import socket
from time import sleep

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((socket.gethostname(), 9000))
except ConnectionRefusedError as error:
    print(error)
    raise

try:
    print("%-5s %5s" % ("%CPU", "%MEM"))
    for i in range(10):
        s.send(b"Iniciar")
        info = s.recv(1024)
        print(info.decode('ascii'))
        sleep(2)
    s.send(b'fim')
    s.close()

except Exception as erro:
    print(erro)
    raise
