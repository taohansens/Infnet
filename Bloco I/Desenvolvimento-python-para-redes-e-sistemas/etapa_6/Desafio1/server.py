import socket
import psutil

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 9000
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > {host}:{porta}")

(socket_cliente, addr) = socket_servidor.accept()
print("Conexão iniciada com: ", str(addr))


def info_psutil():
    proc = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return proc, mem


def format_info(cpu, mem):
    template = "%-5s %5s"
    return template % (cpu, mem)


while True:
    msg = socket_cliente.recv(1024)
    if msg.decode('ascii') == 'fim':
        print("Conexão encerrada por ", str(addr))
        break
    try:
        processador, memoria = info_psutil()
        socket_cliente.send(format_info(processador, memoria).encode('ascii'))
    except Exception:
        print("Ocorreu um erro na [Linha 35]")
        socket_cliente.send("Ocorreu um problema no servidor...".encode('ascii'))
socket_cliente.close()
socket_servidor.close()
