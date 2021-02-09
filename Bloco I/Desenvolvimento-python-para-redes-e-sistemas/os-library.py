# https://docs.python.org/3/library/os.html

import os

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
    if '.gif' in arquivo:
        print(arquivo)


# Verificar se é arquivo ou pasta:
# os.path.isfile()



