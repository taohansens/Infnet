import socket
import nmap

def obter_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


print("Scanner de Rede")
print("Escolha o IP:")
print("1. Meu IP\n2. Desejo digitar outro ip.")
try:
    escolha = int(input("Digite o que você deseja: "))
except:
    print("Tente novamente.")
    escolha = int(input("Digite o que você deseja: "))

ip = {"meu_ip": obter_ip_local()}
if escolha == 1:
    print("IP:", ip['meu_ip'])
if escolha == 2:
    ip_digitado = input("Digite o endereço ip desejado: ")
    ip = {"meu_ip": ip_digitado}

subnet = input('Digite a máscara de sub-rede CIDR (padrão=25): ')

nm = nmap.PortScanner()
nm.scan(hosts=ip['meu_ip']+"/"+subnet, arguments="-F -n")

ips_up = {}
if nm.all_hosts():
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            try:
                ips_up[host] = nm[host]['tcp']
            except:
                ValueError()
else:
    print("não encontrado")
for ip in ips_up:
    print("IP: ", ip)
    for port in ips_up[ip]:
        print(f"{port} - {ips_up[ip][port]['state']} - {ips_up[ip][port]['name']}")
    print("=========")
