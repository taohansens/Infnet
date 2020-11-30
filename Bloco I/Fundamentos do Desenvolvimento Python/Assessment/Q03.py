"""
Q3 - Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números
inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o
resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o
resultado de AB usando a função.
"""


# Função que calcula a pontência de um determinado número, realizando multiplicações sucessivas.
def potencia(a, b):
    result_potencia = a
    for pot in range(1, b):
        result_potencia *= a
    return result_potencia


# input número A
num_a = int(input("Digite o número A (Base): "))
# input número B
num_b = int(input("Digite o número B (Expoente): "))

print(potencia(num_a, num_b))
