# Servidor
import socket, random

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999

# Associa a porta
socket_servidor.bind((host, porta))

# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

# Aceita alguma conexão
(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a:", str(addr))
while True:
    msg = socket_cliente.recv(1024)
    # Decodifica mensagem em UTF-8:
    if '$' == msg.decode('utf-8'):  # Termino do cliente
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    elif '?' in msg.decode('utf-8'):  # Verifica se é uma pergunta
        resp = random.randint(0, 1)  # Sorteia um número entre 0 e 1
        msg = "Sim\n"
        if resp == 0:  # Se 1, é Sim; se 0, é Não
            msg = "Não\n"
    else:
        msg = "Ok... " + msg.decode('utf-8')  # Resposta padrão
    socket_cliente.send(msg.encode('utf-8'))  # Envia resposta

# Fecha conexão do servidor
socket_servidor.close()
input("Pressione qualquer tecla para sair...")
