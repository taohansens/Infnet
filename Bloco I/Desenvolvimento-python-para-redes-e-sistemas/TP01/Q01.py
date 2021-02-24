# Q01 Escreva um programa usando o módulo ‘os’ de Python que imprima o nome de usuário.

# Importando módulo os.
import os

# Exibindo no terminal o nome de usuário.
print(os.getlogin())

# ou utilizando a variável de ambiente 'username'
print(os.getenv('username'))
