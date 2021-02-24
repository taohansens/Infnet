# Q09 Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.

# Importando módulo os.
import os
# Importando módulo datetime e python-dateutil
from datetime import datetime
from dateutil import tz


# Criada função para conversão do timeStamp.
# Recebe valor de os.stat('file').st_mtime e st_atime e retorna a String formatada.
def timestamp_converter(st_time):
    time = datetime.fromtimestamp(st_time, tz=tz.tzlocal()).strftime('%d/%m/%Y às %H:%M')
    return time


# Reaproveitando código da Q08.
def tamanho_arquivos(diretorio):
    # Verifica se a pasta existe.
    if os.path.exists(diretorio):
        # Armazena em uma lista o nome dos arquivos disponíveis na pasta.
        arquivos_diretorio = os.listdir(diretorio)
        # Formatação no console, mostrando o caminho do diretório.
        print("Diretório: ", os.path.abspath(diretorio))
        print('{0: <27}'.format("Arquivo"), "Data de Modificação     Data de Acesso")
        # Percorre a lista de nome de arquivos.
        for arquivo in arquivos_diretorio:
            # Cria a string, unindo o caminho do diretorio + nome do arquivo em cada iteração.
            caminho_arquivo = os.path.join(diretorio, arquivo)
            # Verifica se o caminho é de um arquivo.
            if os.path.isfile(caminho_arquivo):
                arquivo_stat = os.stat(caminho_arquivo)
                # Mostra no console o nome do arquivo (limitado a 25 char, usando o slice) e
                # data de modificação e de acesso.
                print('{0: <25}'.format(arquivo[:25]), "|",
                      '{0: <10}'.format(f"{timestamp_converter(arquivo_stat.st_mtime)}"), "|",
                      '{0: <10}'.format(f"{timestamp_converter(arquivo_stat.st_atime)}"), "|")
            else:
                # Se for diretório, não exibir, continuar a iteração dos nomes dos arquivos.
                continue
    else:
        # No caso do diretório não existir.
        return "Diretório não existe"


# Usando como exemplo o diretório do repositório.
pasta = "."

tamanho_arquivos(pasta)
