"""
Q.2 Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
"""

# input do valor máximo
n = int(input("Digite o número: "))


# Função para somar números pares
def num_pares(num_max):
    soma_pares = 0
    for numero in range(1,num_max+1):
        if numero % 2 == 0:
            soma_pares += numero
    return soma_pares


soma_numeros = num_pares(n)
# Mostra o valor da soma em tela
print("Valor total: {}".format(soma_numeros))





