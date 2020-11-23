"""
Q.3 Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura.
"""

# Cria vetor vazio,
vetor = []

# Quantidade de palavras a serem adicionadas:
qtd_palavras = 10


# Função que inverterá a palavra
def inverte_palavra(word):
    return word[::-1]


# Iteração de qtd_de_palavras adicionando-as na lista.
for x in range(qtd_palavras):
    palavra = input("Escrava a palavra {:g}/{:g} da lista: ".format(x+1, qtd_palavras))
    # Inverte a palavra com a função inverte_palavra e a adiciona na lista
    vetor.append(inverte_palavra(palavra))

# Mostra o vetor com as palavras já invertidas
print(vetor)
