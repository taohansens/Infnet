# Q07 Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo.
# A impressão não deve conter o nome do arquivo, apenas o caminho.

# Importando módulo os.
import os


def retona_caminho(arquivo):
    # Fazendo a verificação se existe no diretório:
    if os.path.exists(arquivo):
        # Fazendo a verificação se é arquivo ou pasta.
        if os.path.isfile(arquivo):
            nome_arquivo = os.path.basename(arquivo)
            # Se for arquivo, irá obter o caminho absoluto, remover o nome do arquivo e retornar como string.
            caminho_absoluto = os.path.abspath(arquivo)
            diretorio = caminho_absoluto.replace(nome_arquivo, "")
            return diretorio
        else:
            print('E é um diretório.')

    # Em caso de não existir, os.path.exists = False.
    else:
        print('Não existe')


# Utilizando como exemplo o próprio diretório do repositório, o arquivo a ser verificado será o Q01.py.
file = 'Q01.py'

print(f"Caminho do arquivo: '{file}'")
# Que apresentará o caminho absoluto sem o nome do arquivo.
print(retona_caminho(file))
