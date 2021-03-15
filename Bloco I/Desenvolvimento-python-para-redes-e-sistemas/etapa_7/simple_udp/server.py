import socket
# SOCK_DGRAM = UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 5000

orig = (host, port)
udp.bind(orig)

print('Esperando conexão na porta: ', port)

while True:
    (msg, cliente) = udp.recvfrom(4)
    print("Mensagem recebida de um cliente: ", msg.decode('ascii'), cliente)
udp.close()
