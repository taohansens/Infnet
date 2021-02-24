# Q18 Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto
# de memória de paginação (swap) existem no computador.

# Importa o módulo psutil.
import psutil

# Obtém os dados e formata de bytes para GB.
memoria_principal = round(psutil.virtual_memory().total//1024//1024/1000, 2)
swap = round(psutil.swap_memory().free//1024//1024/1000, 2)

print("Memória Principal: {} GB".format(memoria_principal))
print("Memória Virtual: {} GB".format(swap))
