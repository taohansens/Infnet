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
        'cores': psutil.cpu_count(logical=False),
        'uso_cpu': psutil.cpu_percent(percpu=True),
        'uso_cpu_todos': psutil.cpu_percent()
    }
    return dict_cpu


def memoria_ram():
    memoria = psutil.virtual_memory()
    dict_memory = {
        'conexao': "OK",
        'percent': memoria.percent,
        'total': memoria.total,
        'used': memoria.used,
        'free': memoria.free
    }
    return dict_memory


def verifica_discos():
    # verifica a quantidade de discos
    qtd_discos = len(psutil.disk_partitions())
    discos = []
    espaco_total = 0
    espaco_usado = 0
    espaco_livre = 0

    # Faz a iteração sobre os retornos do disk_partitions e disk_usage.
    for partition in psutil.disk_partitions():
        discos.append(partition[1])
        espaco_total += psutil.disk_usage(partition[1])[0]
        espaco_usado += psutil.disk_usage(partition[1])[1]
        espaco_livre += psutil.disk_usage(partition[1])[2]

    string_discos = ""
    for i in range(len(discos)):
        string_discos += discos[i] + " "

    # Calcula a porcentagem do uso total.
    percent_usado = round(espaco_usado / espaco_total * 100, 1)
    return qtd_discos, string_discos, espaco_total, espaco_usado, espaco_livre, percent_usado




executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão estabelecida com: ", str(addr))
    mensagem = socket_cliente.recv(2048).decode('ascii')
    if mensagem == "CPU":
        dados = pickle.dumps(processador())
        socket_cliente.send(dados)
    if mensagem == "MEMORY":
        dados = pickle.dumps(memoria_ram())
        socket_cliente.send(dados)
    if mensagem == "DISKS":
        dados = pickle.dumps(verifica_discos())
        socket_cliente.send(dados)
    else:
        dados = {'conexao': 'ERROR'}
        socket_cliente.send(pickle.dumps(dados))

# socket_servidor.close()
