import json
import os
import socket

from psutil._common import bytes2human

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
porta = 5000

socket_servidor.bind((host, porta))
socket_servidor.listen()
print(f" Servidor Iniciado > host: {host} porta: {porta}")


def obtem_arquivos(diretorio):
    dict_files = {}
    if os.path.exists(diretorio):
        l_arquivos = os.listdir(diretorio)
        for arquivo in l_arquivos:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            arquivo_stat = os.stat(caminho_arquivo)
            tamanho = arquivo_stat.st_size
            if os.path.isfile(caminho_arquivo):
                dict_files[arquivo] = bytes2human(tamanho)
    return dict_files


executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    mensagem = socket_cliente.recv(1024).decode('ascii')
    print(f"{str(addr[0])}:{str(addr[1])} está SOLICITANDO o diretório: {mensagem}")
    xdict = obtem_arquivos(mensagem)
    try:
        dados = json.dumps(xdict)
        socket_cliente.send(str.encode(dados))
        print(f"CONEXÃO ENCERRADA | ENVIADOS {bytes2human(dados.__sizeof__())} para {str(addr[0])}:{str(addr[1])}")
        socket_cliente.close()
    except Exception:
        print(Exception)
    break
