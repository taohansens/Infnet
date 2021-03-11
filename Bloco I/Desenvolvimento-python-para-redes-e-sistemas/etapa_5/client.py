import socket

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((socket.gethostname(), 9000))
    msg = "Enviei essa mensagem via porta 9000."
    s.send(msg.encode('ascii'))
    print("Mensagem enviada.")
    s.close()
except Exception as erro:
    print(erro)
    raise
