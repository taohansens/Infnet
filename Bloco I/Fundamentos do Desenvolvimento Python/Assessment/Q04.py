"""
Q04. Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa.
Imprima o vetor no final. Use listas. Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].
"""

# Cria vetor vazio
vetor = []

# Quantidade de numeros que desejo adicionar a lista
qtd_de_numeros = 5

# Iteração de qtd_de_numeros adicionando-os na lista.
for x in range(qtd_de_numeros):
    numero = int(input("Digite o número {:g}/{:g} da lista: ".format(x+1, qtd_de_numeros)))
    vetor.append(numero)

# reverse = True
vetor_original = vetor.copy()
vetor.reverse()

print("Vetor original: {}"
      "\n"
      "Vetor invertido: {}".format(vetor_original, vetor))
