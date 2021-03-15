import socket
import psutil

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 5000

orig = (host, port)
udp.bind(orig)

print('Esperando conexão na porta: ', port)

while True:
    (msg, cliente) = udp.recvfrom(4)
    print("Mensagem recebida de um cliente: ", msg.decode('ascii'), cliente)

    if msg.decode('ascii') == 'fim':
        break

    mem_percent = psutil.virtual_memory().percent
    cpu_percent = psutil.cpu_percent()
    msg_servidor = f"{round(mem_percent, 2)} | {round(cpu_percent, 2)}"
    udp.sendto(msg_servidor.encode('ascii'), cliente)
udp.close()
