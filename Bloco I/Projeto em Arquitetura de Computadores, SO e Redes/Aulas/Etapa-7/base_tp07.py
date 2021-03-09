## Crie uma ou mais funções que retornem ou apresentem as seguintes informações de redes: IP, gateway
# máscara de subrede.
# Utilizando PSutil
import psutil
import socket
import netifaces

cont = 1

list_of_adapters = []
for rede in psutil.net_if_addrs():
    list_of_adapters.append(rede)
    print(f"{cont}... {rede}")

    cont += 1
cont = 1
escolha = int(input("Digite qual interface de rede você deseja visualizar: "))
try:
    adapter = psutil.net_if_addrs().get(list_of_adapters[escolha-1])
except:
    print(ValueError)

for snicaddr in adapter:
    if snicaddr.family == socket.AF_INET:
        ipv4 = snicaddr.address
        netmask = snicaddr.netmask
    elif snicaddr.family == socket.AF_INET6:
        ipv6 = snicaddr.address
        if snicaddr.netmask is not None:
            netmask = snicaddr.netmask
    else:
        ipv4 = None
        ipv6 = None

try:
    gateway = netifaces.gateways()['default'][2][0]
except:
    gateway = None

print(ipv4, ipv6, netmask, gateway)
print("\n")


def family_type(family):
    if family == socket.AF_INET:
        return "IPv4"
    elif family == socket.AF_INET6:
        return "IPv6"
    elif family == socket.AF_UNIX:
        return "Unix"
    else:
        return '-'


def get_socket_type(sock):
    if sock == socket.SOCK_STREAM:
        return "TCP"
    elif sock == socket.SOCK_DGRAM:
        return "UDP"
    elif sock == socket.SOCK_RAW:
        return "IP"
    else:
        return "-"


for i in psutil.pids():
    p = psutil.Process(i)
    conn = p.connections()
    if len(conn) > 0:
        if conn[0].status.ljust(13) != "ESTABLISHED":
            endl = conn[0].laddr.ip.ljust(11)
            portl = str(conn[0].laddr.port).ljust(5)
            try:
                endr = conn[0].raddr.ip.ljust(13)
            except:
                endr = "-"
            try:
                portr = str(conn[0].raddr.port).ljust(5)
            except:
                portr = "-"
            print(str(i).ljust(5), "End.  Tipo   Status        Endereço L.   Porta L.     Endereço R.     "
                                   "Porta R.")
            print("     ", family_type(conn[0].family), " " + get_socket_type(conn[0].type),
                  "   " + conn[0].status.ljust(13),
                  endl, "  " + portl, "       " + endr, "  " + portr)



