notas_candidatos = [["",0],["",0],["",0],["",0],["",0]]

#Função que recebe os dados sobre os candidatos (nome e nota) e
#retorna esses dados em forma de vetor, pos0= nome e pos1 = nota.
def candidatos(candidato):
    nome = input("Informe o nome do {}º participante: ".format(candidato+1))
    nota = -1
    while nota < 0 or nota>10: #Verifica se a nota é um valor válido.
        nota = float(input("Informe a nota do {}º participante: ".format(candidato+1)))
        if (nota < 0 or nota > 10):
            print(ValueError("Essa nota é inválida. Tente novamente."))
    return(nome, nota) #Retorna o nome e a nota.

#Função que irá adicionar os dados na matriz de acordo com a iteração.
def addMatriz(dados,i): #Var. dados referente a funcao candidatos.
    notas_candidatos[i][0] = dados[0]
    notas_candidatos[i][1] = dados[1]

#Função que irá verificar quem foi o candidato vencedor, fazendo uma
#iteração sobre as linhas da coluna 1, em que constam as notas.
def verificaVencedor(matriz):
    maiorNota = 0
    posicao = -1
    for i in range(0,5):
        if maiorNota < matriz[i][1]:
            maiorNota = matriz[i][1]
            posicao = i
    print("O(A) vencedor(a) foi {} com nota {}!".format(matriz[posicao][0], matriz[posicao][1]))

#iteração de 5 candidatos.
for i in range(0,5):
    addMatriz(candidatos(i),i)

#Função que irá chamar a função verificaVencedor, após a matriz estar preenchida.
verificaVencedor(notas_candidatos)

