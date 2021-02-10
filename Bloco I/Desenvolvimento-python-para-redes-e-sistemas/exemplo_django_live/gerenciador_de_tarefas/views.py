from django.shortcuts import render
import os
from datetime import datetime
from dateutil import tz
import time


class InfoArquivos():
    def __init__(self, nome, tamanho, atime, mtime):
        self.nome = nome
        self.tamanho = tamanho
        self.atime = atime
        self.mtime = mtime


def timestamp(namefile):
    atime = datetime.fromtimestamp(os.stat(namefile).st_atime, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    mtime = datetime.fromtimestamp(os.stat(namefile).st_mtime, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    return atime, mtime


def get_arquivos(pasta):
    if os.path.exists(pasta):
        caminho = pasta
    else:
        caminho = os.getcwd()

    lista_arquivos = os.listdir(caminho)

    lista = []

    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)
        if os.path.isfile(caminho_arquivo):
            arquivo_stat = os.stat(caminho_arquivo)
            timestamp_GMT = timestamp(caminho_arquivo)
            tamanho = f"{arquivo_stat.st_size // 1024} KB"
            info = InfoArquivos(arquivo, tamanho, timestamp_GMT[0], timestamp_GMT[1])
            lista.append(info)
    return lista


def arquivos(request):
    pasta = os.path.expanduser('~/Downloads')

    context = {"lista": get_arquivos(pasta), "pasta": pasta}

    return render(request, 'lista_arquivos.html', context)
