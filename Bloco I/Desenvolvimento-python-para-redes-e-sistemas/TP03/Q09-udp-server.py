import os
import psutil
import socket

from psutil._common import bytes2human

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = socket.gethostname()
PORT = 9991

udp_server.bind((HOST, PORT))

print(f" Esperando conexão na porta: {PORT}")


def disk():
    if psutil.WINDOWS:
        diretorio, caminho = os.path.splitdrive(os.path.abspath('.'))
        info = psutil.disk_usage(diretorio)
        return info


while True:
    try:
        (msg, cliente) = udp_server.recvfrom(4)
        print(f"Cliente {cliente[0]} conectado.")
        msg_servidor = f"{bytes2human(disk().used)} | {bytes2human(disk().free)}"
        udp_server.sendto(msg_servidor.encode('ascii'), cliente)
        print(f"Mensagem enviada com sucesso.")
    except Exception:
        print("Ocorreu algum erro no servidor...")
        raise
