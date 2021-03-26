import json
import os
import platform
import re
import socket
from datetime import datetime
from urllib.request import urlopen

import netifaces
import psutil
from cpuinfo import cpuinfo
from dateutil.tz import tz
from nmap import nmap
from psutil._common import bytes2human

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
        'freq_atual': f"{psutil.cpu_freq().current}",
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


def info_redes():
    dic_interfaces = psutil.net_if_addrs()
    names = list(dic_interfaces.keys())
    if "Wi-Fi" in dic_interfaces:
        INTERFACE_REDE = "Wi-Fi"
    elif "Ethernet" in dic_interfaces:
        INTERFACE_REDE = "Ethernet"
    elif 'eth0' in dic_interfaces:
        INTERFACE_REDE = "eth0"
    elif 'enpsl0' in dic_interfaces:
        INTERFACE_REDE = "enpsl0"
    else:
        INTERFACE_REDE = names[0]

    # Gateway
    try:
        gateway = netifaces.gateways()['default'][2][0]
    except:
        gateway = None

    # IPv4 e IPv6
    ipv4 = None
    net_ipv4 = None
    ipv6 = None
    net_ipv6 = None
    for snicaddr in dic_interfaces[INTERFACE_REDE]:
        if snicaddr.family == socket.AF_INET:
            ipv4 = snicaddr.address
            net_ipv4 = snicaddr.netmask
        if snicaddr.family == socket.AF_INET6:
            ipv6 = snicaddr.address
            net_ipv6 = snicaddr.netmask

    dict_network = {
        'public_ip': ip_publico(),
        'ipv4': ipv4,
        'netmask_4': net_ipv4,
        'ipv6': ipv6,
        'netmask_6': net_ipv6,
        'gateway': gateway
    }
    return dict_network


def ip_publico():
    try:
        data = str(urlopen('http://checkip.dyndns.com/').read())
        return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
    except Exception:
        return "Error."


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


def timestamp_converter(st_time):
    time = datetime.fromtimestamp(st_time, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    return time


def obtem_arquivos(diretorio):
    dict_files = {}
    if os.path.exists(diretorio):
        l_arquivos = os.listdir(diretorio)
        for arquivo in l_arquivos:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            arquivo_stat = os.stat(caminho_arquivo)
            tamanho = arquivo_stat.st_size
            dict_files[arquivo] = {
                'arquivo': arquivo,
                'tamanho': tamanho,
                'atime': timestamp_converter(os.stat(caminho_arquivo).st_atime),
                'mtime': timestamp_converter(os.stat(caminho_arquivo).st_mtime),
                'isfile': "FIL" if os.path.isfile(caminho_arquivo) else "DIR"
            }
    return dict_files


def processos():
    dict_process = {}
    for item in psutil.process_iter():
        dict_process[item.name()] = item.as_dict(attrs=['pid', 'status', 'memory_info'])
    for item in dict_process:
        dict_process[item] = {
            'memrss': dict_process[item]['memory_info'].rss,
            'memvms': dict_process[item]['memory_info'].vms,
            'pid': dict_process[item]['pid'],
            'status': dict_process[item]['status']
        }
    return dict_process


def ips_nmap():
    print("INICIANDO SCANNER DE REDE")
    ip = netifaces.gateways()['default'][2][0]
    nm = nmap.PortScanner()
    nm.scan(hosts=ip + "/25", arguments="-F -n")
    print("FINALIZADO...")
    ips_up = {}
    if nm.all_hosts():
        for host in nm.all_hosts():
            if nm[host].state() == 'up':
                try:
                    ips_up[host] = nm[host]['tcp']
                except:
                    ValueError()
    return ips_up, ip


def infor_adapters():
    list_of_adapters = []
    for rede in psutil.net_if_addrs():
        list_of_adapters.append(rede)
    dados = {}
    for adapter in list_of_adapters:
        for snicaddr in psutil.net_if_addrs().get(adapter):
            if snicaddr.family == socket.AF_INET:
                ipv4 = snicaddr.address
                netmask = snicaddr.netmask
            elif snicaddr.family == socket.AF_INET6:
                ipv6 = snicaddr.address
                if snicaddr.address is None:
                    ipv6 = "-"
                if snicaddr.netmask is not None:
                    netmask = snicaddr.netmask
            else:
                ipv4 = None
                ipv6 = None
        dados[adapter] = {'ip': ipv4, 'ip6': ipv6, 'netmask': netmask}
    return dados


executar = True
total = 0
while executar:
    (socket_cliente, addr) = socket_servidor.accept()
    mensagem = socket_cliente.recv(1024).decode('ascii')
    print(f"{str(addr[0])}:{str(addr[1])} está SOLICITANDO: {mensagem}")
    if mensagem == "CPU":
        dados = json.dumps(processador())

    elif mensagem == "MEMORY":
        dados = json.dumps(memoria_ram())

    elif mensagem == "DISKS":
        dados = json.dumps(verifica_discos())

    elif mensagem == "REDE":
        dados = json.dumps(info_redes())

    elif mensagem == "FILES":
        if platform.system() == "Windows":
            xdict = obtem_arquivos("C:"+os.environ['HOMEPATH'])
        elif platform.system() == "Linux":
            xdict = obtem_arquivos('/')
        else:
            xdict = obtem_arquivos(os.environ['PATH'])
        dados = json.dumps(xdict)

    elif mensagem == "PROCESSOS":
        dados = json.dumps(processos())

    elif mensagem == "NMAP_SCAN":
        dados = json.dumps(ips_nmap())

    elif mensagem == "INF_ADAPTERS":
        dados = json.dumps(infor_adapters())

    else:
        print("MENSAGEM NÃO RECONHECIDA. ENVIANDO ERROR.")
        dados = {'conexao': 'ERROR'}
        dados = json.dumps(dados)
    socket_cliente.send(str.encode(dados))
    print(f"ENVIADOS {bytes2human(dados.__sizeof__())} para {str(addr[0])}:{str(addr[1])}")
    total += dados.__sizeof__()
    print(f"TOTAL DE DADOS ENVIADOS DA SESSAO: {bytes2human(total)}")
# socket_servidor.close()
