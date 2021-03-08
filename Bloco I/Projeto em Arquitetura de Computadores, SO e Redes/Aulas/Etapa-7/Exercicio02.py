import psutil
import socket


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
