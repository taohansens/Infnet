"""
Q.4 Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)
"""

# Cria vetor vazio
vetor = []

# Ler tamanho do vetor e armazenar na variável t.
t = int(input("Digite a quantidade de números que deseja adicionar: "))


# Iteração de qtd_de_numeros adicionando-os na lista.
for x in range(t):
    numero = int(input("Digite o número {:g}/{:g} da lista: ".format(x+1, t)))
    vetor.append(numero)

# Verifica quantos numeros "zeros" existem no vetor.
qtd_zeros = 0
for numero in vetor:
    if numero == 0:
        qtd_zeros += 1

# mostra a quantidade de zeros.
print("Quantidade de zeros na lista: ", qtd_zeros)
