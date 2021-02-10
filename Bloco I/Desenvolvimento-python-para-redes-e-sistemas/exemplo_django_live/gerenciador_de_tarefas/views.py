from django.shortcuts import render
import os
import psutil
from gerenciador_de_tarefas.tools import timestamp_converter


class InfoArquivos():
    def __init__(self, nome, tamanho, atime, mtime):
        self.nome = nome
        self.tamanho = tamanho
        self.atime = atime
        self.mtime = mtime


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
            tamanho = f"{arquivo_stat.st_size // 1024} KB"
            info = InfoArquivos(arquivo, tamanho, timestamp_converter(os.stat(caminho_arquivo).st_atime),
                                timestamp_converter(os.stat(caminho_arquivo).st_mtime))
            lista.append(info)
    return lista


def arquivos(request):
    pasta = os.path.expanduser('~/Downloads')
    context = {"lista": get_arquivos(pasta), "pasta": pasta}
    return render(request, 'lista_arquivos.html', context)


def processos(request):
    l_process = []
    for item in psutil.process_iter():
        l_process.append(item.as_dict(attrs=['pid', 'name', 'status', 'cpu_times', 'memory_info']))
    context = {"processos": l_process}
    return render(request, 'lista_processos.html', context)


def detalhar(request, pid):
    context = {"process": psutil.Process(pid)}
    return render(request, 'processo.html', context)
