import matplotlib.pyplot

def preparar_dados():
    arquivo = open('Files/planilha_pibs.csv', 'r', encoding='utf-8')
    dados_crus = arquivo.read()
    # Quebraremos o arquivo em linhas.
    linhas = dados_crus.splitlines()
    # Separaremos a primeira linha, que contém os anos.
    dados_crus_rotulos = linhas[0]
    # Quebaremos a linha em uma lista de rotulos.
    lista_rotulos = dados_crus_rotulos.split(",")
    dados_crus_paises = linhas[1:]
    pib_pais = []
    lista_rot_paises = []

    for ano in dados_crus_paises:
        ano = ano.split(',')
        ano[0] = ano[0].upper()
        pib_pais.append(ano)

    for pais in linhas:
        rot_pais = pais.split(',')
        lista_rot_paises.append(rot_pais[0].upper())

    lista_rot_paises.pop(0)

    return lista_rotulos, pib_pais, lista_rot_paises

rotulos, pib, paises = preparar_dados()

# Função para verificar se o país existe.
def verificar_pais(pais):
    if pais in paises:
        return True
    else:
        return False

def inputPais():
    # Input.
    input_pais = input("Informe um país: ").upper()
    # Verifica se o país é válido.
    while not verificar_pais(input_pais):
        print(Exception("País não disponível. Tente outro país."))
        input_pais = input("Informe um país: ").upper()
    return input_pais

#################################
# Resposta alternativa letra A. #
#################################

input_pais = inputPais()

input_ano = int(input("Informe um ano entre 2013 e 2020: "))
# Verifica se ano é válido.
while input_ano < 2013 or input_ano > 2020:
    print(Exception("Valor inválido."))
    input_ano = int(input("Informe um ano entre 2013 e 2020: "))


print("\nResposta alternativa A:\n")

def alternativaA(pib):
    valorPIB = ''
    for pib in pib:
        if input_pais == pib[0]:
            # verifica na tabela de pib, a posição do ano, e retorna com o país encontrado.
            valorPIB = pib[rotulos.index(str(input_ano))]

    print("PIB {} em 2020: US${} trilhões.".format(input_pais.capitalize(), valorPIB))

alternativaA(pib)

#################################
# Resposta alternativa letra B. #
#################################
print("\nResposta alternativa B:\n")
def alternativaB():
    for paises in pib:
        pais = paises[0]
        variacao = (float(paises[-1]) / float(paises[1]) - 1) * 100
        print("{:<20} Variação de {:.2f}% entre {} e {}.".format(pais.capitalize(), variacao, rotulos[1], rotulos[-1]))

alternativaB()

#################################
# Resposta alternativa letra C. #
#################################
print("\nResposta alternativa C:\n")

local = inputPais()

def grafico_valor(local, pib):
    vetor_valores = ""
    for index in pib:
        if local == index[0]:
            vetor_valores = index
            continue
    vetor_valores.pop(0)
    vetor_valores = [float(i) for i in vetor_valores]
    matplotlib.pyplot.title('Evolução do PIB - {}'.format(local))
    matplotlib.pyplot.ylabel('Valor em trilhões US$')
    rotulos.pop(0)
    matplotlib.pyplot.plot(rotulos, vetor_valores, 'r-o')
    matplotlib.pyplot.show()

grafico_valor(local, pib)