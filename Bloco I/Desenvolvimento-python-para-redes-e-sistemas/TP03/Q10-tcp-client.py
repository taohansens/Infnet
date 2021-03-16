import os
import socket

from psutil._common import bytes2human

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arq = input("Digite o nome do arquivo para download: ")


def status_download(by_tes, tamanho):
    texto = f"Baixando... {bytes2human(by_tes)} de {bytes2human(tamanho)}"
    print(texto)


try:
    s.connect((socket.gethostname(), 8881))
except ConnectionRefusedError as error:
    print(error)
    raise

try:
    s.send(nome_arq.encode('ascii'))
    msg = s.recv(12)
    tamanho = int(msg.decode('ascii'))
    if tamanho >= 0:
        # Gera o arquivo na pasta de download
        if not os.path.exists("Resources//DownloadClient"):
            os.makedirs("Resources//DownloadClient")
        arq = open("Resources//DownloadClient//" + os.path.basename(nome_arq), "wb")
        soma = 0
        tam_bytes = s.recv(4096)
        while tam_bytes:
            arq.write(tam_bytes)
            soma += len(tam_bytes)
            status_download(soma, tamanho)
            tam_bytes = s.recv(4096)
        arq.close()
    else:
        print("Arquivo não encontrado no servidor.")
except Exception as error:
    print(str(error))

s.close()
