# https://docs.python.org/3/library/os.html
import os

# Para timestamp
from datetime import datetime
from dateutil import tz
import time

# breakline
br = '\n===================='

# Name System
print(os.name)

# User
print(os.getlogin(), br)

# Env Var
print(os.environ)
print(os.environ['HOMEDRIVE'])
print(os.environ['HOMEPATH'], br)

# current Dir.
print(os.getcwd(), br)

# PID
print(os.getpid(), br)


# Manipulando diretórios
# Criar (Se já existir: FileExistsError)
try:
    os.mkdir('nova Pasta')
except FileExistsError:
    print("Pasta já criada")

# Renomear
try:
    os.rename('nova Pasta', 'nova Pasta Renomeada')
except FileExistsError:
    print("Pasta já renomeada")

# Excluir
try:
    os.rmdir("nova Pasta Renomeada")
except FileNotFoundError:
    print("Pasta não encontrada")


# Listando diretórios
print(os.listdir('../'))

# Listando arquivos por formato (Exemplo)
lista_arquivos = ''
try:
    lista_arquivos = os.listdir('../Fundamentos do Desenvolvimento Python/Assessment/')
except FileNotFoundError:
    print("Repositório não disponível localmente")

for arquivo in lista_arquivos:
    # determinado formato
    if '.gif' in arquivo:
        print(arquivo)
print(br)

# Verificar se é arquivo ou pasta:
print(os.path.isfile('os-library.py'), br)

# Os.STAT
print(os.stat('os-library.py'), br)
# apenas tamanho do arquivo em KB
print(f"{os.stat('os-library.py').st_size//1024} KB")

# timestamp em formato de data utilizando datetime
print(datetime.fromtimestamp(os.stat('os-library.py').st_mtime, tz=tz.tzlocal())
      .strftime('%d/%m/%Y-%H:%M'), br)


# função para timestamp
def timestamp(file):
    atime = datetime.fromtimestamp(os.stat(file).st_atime, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    mtime = datetime.fromtimestamp(os.stat(file).st_mtime, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    return atime, mtime


# Calculando tempo de execução
inicio_exec = datetime.now()

# Imprimindo lista de arquivos da pasta downloads
my_folder = '../../../../Downloads'
l_arquivos = os.listdir(my_folder)
if os.path.exists(my_folder):
    for arquivo in l_arquivos:
        # time.sleep(1)
        caminho_arquivo = os.path.join(my_folder, arquivo)
        if os.path.isfile(caminho_arquivo):
            arquivo_stat = os.stat(caminho_arquivo)
            timestamp_GMT = timestamp(caminho_arquivo)
            # print(arquivo, f"{arquivo_stat.st_size//1024}KB", arquivo_stat.st_uid, time[0], time[1])
            print('{0: <30}'.format(arquivo), "|",
                  '{0: <20}'.format(f"{arquivo_stat.st_size//1024}KB"), "|",
                  '{0: <20}'.format(timestamp_GMT[0]), "|",
                  '{0: <20}'.format(timestamp_GMT[1]))

print(br)

# Calculando tempo de execução
fim_exec = datetime.now()
tempo_exec = fim_exec - inicio_exec
print(f"Tempo de execução: {tempo_exec}")

print(br)



