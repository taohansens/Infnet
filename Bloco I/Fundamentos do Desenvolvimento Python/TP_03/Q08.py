"""
Q.8 Faça uma funçãoum programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene
os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios, simulando os lançamentos dos dados. (código)
"""
from random import choice

# Utilizando POO.


# Cria vetor vazio para armazenar os lancamentos.
lancamentos = []


# Cria objeto Dado com uma lista com seus lados e uma lista com a qtd de lançamentos.
class Dado:
    def __init__(self):
        self.lado = [1, 2, 3, 4, 5, 6]
        self.qtd = [0, 0, 0, 0, 0, 0]

    def lancar(self):
        # lado escolhido
        lado_mostrado = choice(self.lado)
        # soma +1 na lista de qtd no index correspondente do lado.
        self.qtd[(self.lado.index(lado_mostrado))] += 1
        return lado_mostrado


# Cria um objeto dado.
dado = Dado()
print("Lista de lançamentos: ")
# Lança o dado 100 vezes
for vez in range(100):
    # Chama a função lançar que já efetua a soma no próprio objeto dado.
    dado.lancar()

# Mostra a quantidade de vezes que cada lado foi sorteado.
for lado in dado.qtd:
    print("Lado {} foi sorteado {} vezes."
          .format((dado.lado[dado.qtd.index(lado)]), lado))
    # Verifica qual foi o lado do dado em virtude do index da posição na lista da qtd.
