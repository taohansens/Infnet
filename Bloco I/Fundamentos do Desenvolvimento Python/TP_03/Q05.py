"""
Q.5 Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o
código de saída “Sair”. O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média
(a média aritmética das alturas de todos os alunos lidos).
"""

# Cria a lista para armazanar os alunos e alturas
lista_alunos = []

# Variável para indicar a qtd de alunos.
cont = 0
# Iniciliza a variável aluno como uma string vazia
aluno = ""


# Função para calular a média da lista de alunos
def media_altura_alunos(vetor_alunos):
    qtd_alunos = len(vetor_alunos)
    # inicializa variável que terá a soma de todas as alturas.
    soma_altura = 0
    # faz a iteração de todos os alunos no vetor de alunos.
    for alun in vetor_alunos:
        # pessoa[1] corresponde a posição na tupla que contém a altura do aluno.
        soma_altura += alun[1]
    media = soma_altura / qtd_alunos
    return media


# Função para mostrar alunos com altura maior que a média
def alunos_superior_media(vetor_alunos):
    # calcula a média com a função media_altura_alunos.
    media_altura = media_altura_alunos(vetor_alunos)
    qtd = 0
    print("Média da turma ({:.2f}m) - Alunos com altura superior a média: ".format(media_altura))
    for alunos in lista_alunos:
        if alunos[1] > media_altura:
            # soma ao qtd +1 se houver aluno
            qtd += 1
            print("{} possui {}m de altura.".format(alunos[0].upper(), alunos[1]))
    # se todos alunos tiverem a mesma altura
    if qtd == 0:
        print("Não existe aluno com altura superior a média.")


# Interromper o laço de repetição quando aluno == sair.
while aluno != "Sair":
    # faz a contagem para exibir no GUI
    cont += 1
    aluno = input("Digite o nome do aluno ({}) ou Sair para interromper: ".format(cont))
    if aluno == "Sair":
        break
    altura = float(input("Digite a altura de {:s} em metros: ".format(aluno)))
    # Adiciona uma tupla com aluno na posição 0 e altura na posição [1]
    lista_alunos.append((aluno, altura))

# Mostra apenas os alunos que possuem altura maior que a média.
alunos_superior_media(lista_alunos)


