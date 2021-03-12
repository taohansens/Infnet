import socket, sys, os
from psutil._common import bytes2human

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nome_arq = input("Digite o nome do arquivo para download: ")


def status_download(by_tes, tamanho):
    texto = f"Baixando... {bytes2human(by_tes)} de {bytes2human(tamanho)}"
    print(texto)


try:
    s.connect((socket.gethostname(), 9000))
except ConnectionRefusedError as error:
    print(error)
    raise

try:
    s.send(nome_arq.encode('ascii'))
    msg = s.recv(12)
    tamanho = int(msg.decode('ascii'))
    # Arquivo a ser baixado
    PATH = 'c://texto.txt'

    if tamanho >= 0:
        # Gera o arquivo na pasta download
        if not os.path.exists("Download"):
            os.makedirs("Download")
        arq = open("Download/"+os.path.basename(nome_arq), "wb")
        soma = 0
        bytes = s.recv(4096)
        while bytes:
            arq.write(bytes)
            soma += len(bytes)
            status_download(soma, tamanho)
            bytes = s.recv(4096)
        arq.close()
    else:
        print("Arquivo não encontrado no servidor.")
except Exception as error:
    print(str(error))

s.close()
