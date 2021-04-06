import socket

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.settimeout(5)
dest = (socket.gethostname(), 8888)

udp.sendto('ON'.encode('utf-8'), dest)
ACK = None
try:
    ACK, address = udp.recvfrom(2048)
except socket.timeout:
    print("timeout...")
    for i in range(5):
        try:
            udp.sendto('ON'.encode('utf-8'), dest)
            ACK, address = udp.recvfrom(2048)
            if ACK is not None:
                break
        except:
            print("timeout...")
            pass
    pass
try:
    print(ACK.decode('utf-8'))
except:
    print("DESISTI")
udp.close()
