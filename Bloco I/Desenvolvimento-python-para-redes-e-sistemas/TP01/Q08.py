# Q08 Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.

# Importando módulo os.
import os


# Cria função que irá receber o diretório para listar os arquivos
def tamanho_arquivos(diretorio):
    # Verifica se a pasta existe.
    if os.path.exists(diretorio):
        # Armazena em uma lista o nome dos arquivos disponíveis na pasta.
        arquivos_diretorio = os.listdir(diretorio)
        # Formatação no console, mostrando o caminho do diretório.
        print("Diretório: ", os.path.abspath(diretorio))
        print('{0: <28}'.format("Arquivo"), "Tamanho")
        # Percorre a lista de nome de arquivos.
        for arquivo in arquivos_diretorio:
            # Cria a string, unindo o caminho do diretorio + nome do arquivo em cada iteração.
            caminho_arquivo = os.path.join(diretorio, arquivo)
            # Verifica se o caminho é de um arquivo.
            if os.path.isfile(caminho_arquivo):
                arquivo_stat = os.stat(caminho_arquivo)
                # Mostra no console o nome do arquivo (limitado a 25 char, usando o slice) e
                # arredonda o tamanho do arquivo para duas casas decimais usando o round.
                print('{0: <25}'.format(arquivo[:25]), "|",
                      '{0: <10}'.format(f"{round(arquivo_stat.st_size / 1024, 2)} KB"))
            else:
                # Se for diretório, não exibir, continuar a iteração dos nomes dos arquivos.
                continue
    else:
        # No caso do diretório não existir.
        return "Diretório não existe"


# Usando como exemplo o diretório do repositório.
pasta = "."

tamanho_arquivos(pasta)
