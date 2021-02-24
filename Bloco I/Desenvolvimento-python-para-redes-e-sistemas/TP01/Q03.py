# Q03 Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo
# e também seu GID (identificador de grupo) caso seja sistema do tipo Linux.

# Importando módulo os.
import os

# Mostrando o PID do próprio processo.
print(f"PID {os.getpid()}")

# Mostrando o GID do processo se sistema for Linux.
try:
    print(f"GID {os.getgid()}")
except:
    print("GID NÃO DISPONÍVEL")
