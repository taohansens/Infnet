# Q05 Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente
# um arquivo ou não.

# Importando módulo os.
import os


def verifica_path(arquivo):
    # Fazendo a verificação se existe no diretório:
    if os.path.exists(arquivo):
        print('Existe')
        # Fazendo a verificação se é arquivo ou pasta.
        if os.path.isfile(arquivo):
            print('E é um arquivo.')
        else:
            print('E é um diretório.')

    # Em caso de não existir, os.path.exists = False.
    else:
        print('Não existe')


# Utilizando como exemplo o próprio diretório do repositório, o arquivo a ser verificado será o Q01.py, que existe.
# A pasta TP01, e um arquivo inexistente.
testes = ['Q01.py', '../TP01', '000.py']

# Loop sobre os itens da lista
for teste in testes:
    print(f"Verificacão de: '{teste}'")
    # Função recebendo a variável teste da iteração, que contém o que será testado.
    verifica_path(teste)
