import socket
import os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > {host}:{porta}")

executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão iniciada com: ", str(addr))
    msg = socket_cliente.recv(2048)
    nome_arq = msg.decode('ascii')
    # Diretorio para busca do arquivo
    path = ".//Resources//"+nome_arq
    if os.path.isfile(path):
        # Verifica o tamanho do arquivo e envia para o cliente
        tamanho = os.stat(path).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        print("Enviando o arquivo: ", os.path.abspath(path))
        # Abre o arquivo no modo leitura de bytes
        arq = open(path, 'rb')
        # Envia os dados
        arq_bytes = arq.read(4096)
        while arq_bytes:
            socket_cliente.send(arq_bytes)
            arq_bytes = arq.read(4096)
        arq.close()
    else:
        print("Servidor não encontrou o arquivo", nome_arq)
        socket_cliente.send('-1'.encode('ascii'))
    socket_cliente.close()
    executar = False
socket_servidor.close()
