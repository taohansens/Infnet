# Q11 Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’,
# de bloco de notas (notepad) para abri-lo

import os
import platform


# Cria função que receberá o caminho abs.
def abrir_notepad(nome_do_arquivo):
    # Verifica se o sistema é Windows.
    if platform.system() == "Windows":
        # Se sim, abrirá o notepad com o arquivo.
        os.system(f"notepad.exe {nome_do_arquivo}")
    else:
        print("Seu sistema não é Windows. Você sabe usar o terminal :D.")


# Input
nome_arquivo = input("Digite o nome do arquivo com .txt: ")
# No caso de não existir o arquivo
while not os.path.exists(nome_arquivo):
    # Criará um arquivo com o nome digitado.
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines('')

# Obtém o caminho abs do arquivo.
nome_arquivo = os.path.realpath(nome_arquivo)

abrir_notepad(nome_arquivo)
