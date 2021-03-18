import socket, sys, pickle

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o nome do arquivo do usuário:
msg = input("Entre com o nome do arquivo: ")

try:
    # Tenta se conectar ao servidor que
    # fica na mesma máquina:
    s.connect((socket.gethostname(), 9999))
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
    # Recebe até 100000 bytes
    bytes = s.recv(100000)
except Exception as erro:
    print(str(erro))
    sys.exit(1)  # Termina o programa

# Converte de bytes para lista
lista = pickle.loads(bytes)
# Apresenta o resultado:
if lista:
    for i in lista:
        print(i[0], i[1], "bytes")
else:
    print("Arquivo não encontrado...")

print("Terminou a busca no servidor...")
input("Pressione qualquer tecla para sair...")

# Fecha conexão com o servidor
s.close()