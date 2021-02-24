# Q19 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há
# na partição do sistema (onde o sistema está instalado).

# Importa o módulo psutil.
import os
import psutil

# Obtém o drive onde o sistema está instalado.
system = os.environ['SYSTEMDRIVE']

print("Espaço livre no Disco ", system)
# Exibe a quantidade de espaço livre da tupla nomeada: sdiskusage(total, used, free, percent)
# E converte para GB.
print(f"{round(psutil.disk_usage(system).free//1024//1024/1000, 2)} GB")
