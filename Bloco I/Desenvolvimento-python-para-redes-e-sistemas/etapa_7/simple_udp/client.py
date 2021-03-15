import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.sendto(b'ola', (socket.gethostname(), 5000))
print("Mensagem enviada")
udp.close()
