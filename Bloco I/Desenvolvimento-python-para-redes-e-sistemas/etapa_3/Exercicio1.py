import os


def procura_arquivo(filename, filedir):
    dir = []
    try:
        dir = os.listdir(filedir)
    except:
        pass
    for arquivo in dir:
        if os.path.isfile(arquivo) and arquivo == filename:
            return True
    return False


rodando = True
while rodando:
    nome_arquivo = input("Digite o nome do arquivo: ")
    nome_diretorio = input("Digite o nome do diretorório: ")
    if procura_arquivo(nome_arquivo, nome_diretorio):
        print(f"'{nome_arquivo}' foi encontrado no diretório")
    else:
        print(f"Oops... '{nome_arquivo}' não encontrado.\n")
    print("=" * 10)
    try:
        escolha = int(input("Deseja fazer outra busca?\n1- Sim\n2- Não\n# "))
    except:
        escolha = False
        continue
    if escolha != 1:
        rodando = False
