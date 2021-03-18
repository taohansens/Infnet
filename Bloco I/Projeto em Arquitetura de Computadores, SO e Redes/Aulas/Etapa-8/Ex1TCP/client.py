# Cliente
import socket, sys

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 9999))
except Exception as erro:
    print(str(erro))
    # Termina o programa
    sys.exit(1)

print("Para encerrar, digite '$'")
msg = input()

# Envia mensagem codificada em bytes ao servidor
s.send(msg.encode('utf-8'))

while msg != '$':
    msg = s.recv(1024)
    print(msg.decode('utf-8'))
    msg = input()
    # Envia mensagem codificada em bytes ao servidor
    s.send(msg.encode('utf-8'))
# Fecha conexão com o servidor
s.close()
