import socket
from time import sleep

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ENDERECO = (socket.gethostname(), 5000)

print("Aguardando...")
print("MEM% | CPU%")
for i in range(5):
    udp.sendto(b"Ola", ENDERECO)
    info_bytes = udp.recv(1024)
    print(info_bytes.decode('ascii'))
    sleep(2)

udp.sendto(b"fim", ENDERECO)
udp.close()
