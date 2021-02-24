# Q05 Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.

# Importando módulo os.
import os


def separa_extensao(arquivo):
    # Fazendo a verificação se existe no diretório:
    if os.path.exists(arquivo):
        # Fazendo a verificação se é arquivo ou pasta.
        if os.path.isfile(arquivo):
            # Se for arquivo, irá separar e retornar a extensão em uma string.
            nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
            return extensao_arquivo
        else:
            print('E é um diretório.')

    # Em caso de não existir, os.path.exists = False.
    else:
        print('Não existe')


# Utilizando como exemplo o próprio diretório do repositório, o arquivo a ser verificado será o Q01.py.
teste = 'Q01.py'

print(f"Verificacão de: '{teste}'")
# Que apresentará a extensão .py.
print(f"Extensão: {separa_extensao(teste)}")
