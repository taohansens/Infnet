import socket
import pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 5000
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > host: {host} porta: {porta}")

executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão estabelecida com: ", str(addr))
    msg = socket_cliente.recv(2048)
    print(f"Mensagem recebida: {msg}")
    executar = False
socket_servidor.close()
