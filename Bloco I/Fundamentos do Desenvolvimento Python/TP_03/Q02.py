"""
Q.2 Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)
"""

# Cria vetor vazio
vetor = []

# Quantidade de números que desejo adicionar a lista
qtd_de_numeros = 5

# Iteração de qtd_de_numeros adicionando-os na lista.
for x in range(qtd_de_numeros):
    numero = int(input("Digite o número {:g}/{:g} da lista: ".format(x+1, qtd_de_numeros)))
    vetor.append(numero)

# Mostrando o vetor
print(vetor)
