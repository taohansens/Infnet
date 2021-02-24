# Q15 Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário,
# o tempo de criação e o uso de memória em KB.

# Importa o módulo psutil.
import time

import psutil

# Mostra os pids disponíveis.
print('PIDs Disponíveis: ', psutil.pids())

# Aguarda input de um número existente.
numero_pid = int(input("Digite o número PID: "))

# Se não existir, entrará em loop, até entrar com valor válido.
while not psutil.pid_exists(numero_pid):
    print("Esse processo não existe.")
    numero_pid = int(input("Digite outro número PID: "))

# Digitando o valor válido, com o process_iter, exibirá as informações.
for processo in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'create_time']):
    if numero_pid == processo.info['pid']:
        # Sem permissões ao user:
        if str(processo.info['username']) == 'None':
            usuario = "Sem permissão"
        else:
            usuario = str(processo.info['username'])

        # Formatacao no terminal
        print('{0: <15}'.format('Processo'), "|",
              '{0: <20}'.format('Usuario'), "|",
              '{0: <18}'.format('Data de Criação'), "|",
              '{0: <20}'.format('Tamanho'))
        # Exibe dados solicitados.
        print('{0: <15}'.format(str(processo.info['name'])[:15]), "|",
              '{0: <10}'.format(usuario), "|",
              '{0: <10}'.format(time.ctime(processo.info['create_time'])), "|",
              '{0: <10}'.format(f"{processo.info['memory_info'].rss / 1024} KB"))
