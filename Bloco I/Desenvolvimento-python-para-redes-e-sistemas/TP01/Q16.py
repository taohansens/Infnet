# Q16 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.

# Importa o módulo psutil.
import psutil

cpu = psutil.cpu_times_percent(interval=0.1, percpu=True)
# Qtd de nucleos, incluindo threads.
qtd_nucleos = psutil.cpu_count()
print(f"Núcleos: {qtd_nucleos}")
# Formatação no console (Titulo)
print('{}'.format('Núcleo nº'), "|",
      '{0: <5}'.format('User'), "|",
      '{0: <5}'.format('System'), "|",
      '{0: <5}'.format('Interrupt'), "|",
      '{0: <5}'.format('DPC'))

# Contador de núcleos para exibição na tela.
contador = 1
# Executar 10x
for i in range(10):
    # Exibição de cada núcleo no console. (tupla)
    for nucleo in cpu:
        print('{0: <10}'.format(f"{contador}"), "|",
              '{0: <5}'.format(f"{nucleo[0]}"), "|",
              '{0: <5}'.format(f"{nucleo[1]}"), "|",
              '{0: <10}'.format(f"{nucleo[2]}"), "|",
              '{0: <5}'.format(f"{nucleo[3]}"))
        if contador < qtd_nucleos:
            contador += 1
        else:
            contador = 1
    print("Prox. execução " + "=="*30)
