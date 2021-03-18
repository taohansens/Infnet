import platform
import socket
import pickle
from cpuinfo import cpuinfo
import psutil
from psutil._common import bytes2human

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 5001
socket_servidor.bind((host, porta))

socket_servidor.listen()

print(f" Servidor Iniciado > no host: {host} porta: {porta}")


def memory_info():
    dic_memory = {}
    memoria = psutil.virtual_memory()
    dic_memory['porcentagem'] = "{}%".format(memoria.percent)
    dic_memory['total'] = bytes2human(memoria.total)
    dic_memory['usada'] = bytes2human(memoria.used)
    dic_memory['free'] = bytes2human(memoria.free)
    return dic_memory


def cpu_info():
    dict_processor = {}
    info_cpu = cpuinfo.get_cpu_info()
    dict_processor['name'] = info_cpu['brand_raw']
    dict_processor['system'] = platform.system() + " " + platform.platform()
    dict_processor['clock'] = psutil.cpu_freq().current / 1000
    dict_processor['word'] = info_cpu['bits']
    dict_processor['arch'] = info_cpu['arch']
    dict_processor['freq_atual'] = psutil.cpu_freq().current
    dict_processor['freq_max'] = psutil.cpu_freq().max
    dict_processor['threads'] = psutil.cpu_count()
    dict_processor['cores'] = psutil.cpu_count(logical=False)
    dict_processor['uso_cpu'] = "{}%".format(psutil.cpu_percent())
    return dict_processor


executar = True
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conexão iniciada com: ", str(addr))
    msg = socket_cliente.recv(2048)
    informacoes = {}
    if msg:
        informacoes['memory'] = memory_info()
        informacoes['processor'] = cpu_info()
        dados = pickle.dumps(informacoes)
        socket_cliente.send(dados)
executar = False
socket_servidor.close()
