import socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ENDERECO = (socket.gethostname(), 9991)

print("USED  |  FREE")
udp.sendto(b"Ola", ENDERECO)
info_bytes = udp.recv(1024)
print(info_bytes.decode('ascii'))

udp.close()
