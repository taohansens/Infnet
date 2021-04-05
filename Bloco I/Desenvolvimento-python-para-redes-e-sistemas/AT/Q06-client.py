import json
import socket
from pprint import pprint

host = socket.gethostname()
porta = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dados = {'conexao': 'ERROR'}
try:
    s.connect((host, porta))
    diretorio = input("Digite um diretório do servidor: ")
    s.send(f"{diretorio}".encode('ascii'))
    request = b''
    while True:
        data = s.recv(1024)
        request = request + data
        try:
            dados = json.loads(request)
            break
        except Exception:
            continue
    s.close()
    informacoes = dados


except ConnectionRefusedError as error:
    informacoes = [dados, (host, porta)]
    print(error)

pprint(informacoes)