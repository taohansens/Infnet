"""
Q6. Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada.
Indique quais frases apresentam a palavra “eu”. (código)
"""

# Cria a lista para armazanar as frases
lista_frases = []

# Variável para indicar a qtd de frases.
cont = 0
# Iniciliza a variável frase como uma string vazia
frase = ""


# Verificar frases que possuem "eu".
def verifica_eu(vetor):
    # se não existir frase com "eu" continuará False.
    existe = False
    for ver_frase in vetor:
        # verifica a existência da string "eu" na frase // convertido para lower, para não haver difirenças.
        if "eu" in ver_frase.lower():
            # se existir frase com "eu" se tornará True.
            existe = True
            # imprime a frase encontrada
            print("Frase encontrada: ", ver_frase)
    # se não existir nenhuma frase, mostrará a mensagem abaixo.
    if not existe:
        print("Não existe 'Eu' em nenhuma frase")


# Interromper o laço de repetição quando aluno == sair.
while frase != "Sair":
    # faz a contagem para exibir no GUI
    cont += 1
    frase = input("Digite a frase ({}) ou Sair para interromper: ".format(cont))
    if frase == "Sair":
        break
    # adiciona a frase ao vetor lista_frases e inicia o loop novamente, até digitar Sair.
    lista_frases.append(frase)

# Função que verificará se existe 'eu' na frase, passando o vetor lista_frases.
verifica_eu(lista_frases)
