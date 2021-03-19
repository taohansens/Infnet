import pickle
import platform
import socket
import psutil
from cpuinfo import cpuinfo

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 5000
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > host: {host} porta: {porta}")


def processador():
    info_cpu = cpuinfo.get_cpu_info()
    dict_cpu = {
        'conexao': "OK",
        'name': info_cpu['brand_raw'],
        'system': f"{platform.system()} ({platform.platform()})",
        'freq': f"{psutil.cpu_freq().max}",
        'arc': info_cpu['arch'],
        'word': f"{info_cpu['bits']}",
        'threads': psutil.cpu_count(),
        'cores': psutil.cpu_count(logical=False)
    }
    print(psutil.cpu_count())
    return dict_cpu


executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão estabelecida com: ", str(addr))
    mensagem = socket_cliente.recv(2048).decode('ascii')
    if mensagem == "CPU":
        dados = pickle.dumps(processador())
        socket_cliente.send(dados)
    else:
        dados = {'conexao': 'ERROR'}
        socket_cliente.send(pickle.dumps(dados))

# socket_servidor.close()
