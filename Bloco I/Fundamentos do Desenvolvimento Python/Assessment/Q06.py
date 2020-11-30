"""
Q06. Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente
os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
"""

# tupla com valores
tupla = (15, 10, 54, 66, 45, 8, 77, 53, 17, 11)

# vetores vazios
num_impares = []
num_pos_pares = []

for pos in range(len(tupla)):
    # Verifica se o número é ímpar
    if tupla[pos] % 2 != 0:
        num_impares.append(tupla[pos])
    # Verifica se o número está em uma posição par.
    if pos % 2 == 0:
        num_pos_pares.append(tupla[pos])

# Converte para tupla
tuple_pos_pares = tuple(num_pos_pares)

# Lista com os números ímpares
print(num_impares)
# Tupla com os números das posições pares
print(tuple_pos_pares)
