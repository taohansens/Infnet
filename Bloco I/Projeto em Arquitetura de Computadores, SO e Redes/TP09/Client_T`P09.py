import json
import pickle
import socket

# host = socket.gethostname()
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.connect((host, 5000))
# except ConnectionRefusedError as error:
#     print(error)


def get_server(solicitacao):
    host = socket.gethostname()
    porta = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, porta))
        s.send(f"{solicitacao}".encode('ascii'))
        dados = json.loads(s.recv(1024))
        s.close()
        informacoes = [dados, (host, porta)]
    except ConnectionRefusedError as error:
        dados = {'conexao': 'ERROR'}
        informacoes = [dados, (host, porta)]
        print(error)
    return informacoes


print(get_server("MEMORI"))

# s.close()
