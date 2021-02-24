# Q20 Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
# o nome do dispositivo, o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
# o total de armazenamento em GB e o armazenamento disponível em GB.

# Importa o módulo Psutil
import os
import psutil

# Obtém a partição corente
caminho = os.path.abspath('.')
particao_atual, caminho = os.path.splitdrive(caminho)
particao_atual = particao_atual + "\\"

print('{0: <8}'.format('Device'), "|",
      '{0: <8}'.format('Type'), "|",
      '{0: <10}'.format('Total GB'), "|",
      '{0: <10}'.format('Free GB'))

device = ""
tipo = ""
# Verifica apenas a partição.
for part in psutil.disk_partitions(caminho):
    if part.device == particao_atual:
        device = part.device
        tipo = part.fstype

# Obtém as informações de espaço do disco.
espaco = psutil.disk_usage(caminho)

# mostra na tela os valores em GB.
print('{0: <10}'.format(device),
      '{0: <10}'.format(tipo),
      '{0: <10} '.format(espaco.total//1024//1024/1000), "|",
      '{0: <10}'.format(espaco.free//1024//1024/1000))

