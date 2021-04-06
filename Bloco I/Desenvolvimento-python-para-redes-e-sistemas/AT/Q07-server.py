import socket
import psutil
from psutil._common import bytes2human


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((socket.gethostname(), 8888))

while True:
    pacote, dest = udp.recvfrom(1024)
    print("Mensagem recebida de um cliente: ", pacote.decode('utf-8'), dest)
    mtotal = bytes2human(psutil.virtual_memory().total)
    mfree = bytes2human(psutil.virtual_memory().free)
    msg_servidor = f"TOTAL: {mtotal} | LIVRE: {mfree}"
    udp.sendto(msg_servidor.encode('utf-8'), dest)
