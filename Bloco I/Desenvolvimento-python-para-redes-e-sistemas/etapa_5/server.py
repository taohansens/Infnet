import socket

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
porta = 9000

socket_servidor.bind((host, porta))

socket_servidor.listen()
print(f" Servidor Iniciado > {host}:{porta}")

while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conexão iniciada com: ",str(addr))
    msg = socket_cliente.recv(1024)
    print("Mensagem recebida> ", msg.decode('ascii'))
    socket_cliente.close()
    print("Conexão encerrada com: ", str(addr))
