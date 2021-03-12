import socket, os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 9000
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > {host}:{porta}")

executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão iniciada com: ", str(addr))
    msg = socket_cliente.recv(2048)
    nome_arq = msg.decode('ascii')
    if os.path.isfile(nome_arq):
        # Verifica o tamanho do arquivo e envia para o cliente
        tamanho = os.stat(nome_arq).st_size
        socket_cliente.send(str(tamanho).encode('ascii'))
        print("Enviando o arquivo: ", os.path.abspath(nome_arq))
        # Abre o arquivo no modo leitura de bytes
        arq = open(nome_arq, 'rb')
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
