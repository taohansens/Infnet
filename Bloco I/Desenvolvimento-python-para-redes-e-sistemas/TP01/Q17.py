# Q17 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o
# percentual do uso de CPU do computador.

# Importa o módulo psutil e time.
import time
import psutil

cpu = psutil.cpu_percent(interval=1, percpu=False)
# Qtd de nucleos, incluindo threads.
qtd_nucleos = psutil.cpu_count()
print(f"Núcleos: {qtd_nucleos}")
# Laço de repetição
while True:
    # armazena a informação do uso da CPU em % (percpu=False).
    uso_cpu = psutil.cpu_percent(interval=0.1)
    print(f"{uso_cpu} %")
    # a cada um segundo.
    time.sleep(1)
