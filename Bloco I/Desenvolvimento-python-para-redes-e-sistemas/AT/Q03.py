import os
from psutil._common import bytes2human


# Retorna o dicionário ordenado em bytes com o arquivo (key), e tamanho (value)
def tamanho_arquivos(diretorio):
    dict_files = {}
    arquivos_diretorio = os.listdir(diretorio)
    for arquivo in arquivos_diretorio:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_arquivo):
            arquivo_stat = os.stat(caminho_arquivo)
            dict_files[arquivo] = arquivo_stat.st_size
            continue
    return dict(sorted(dict_files.items(), key=lambda item: item[1], reverse=True))


# Grava o dicionário em um arquivo de texto.
def gravar_texto(dados):
    FORMAT = "%-25s %10s"
    TOP = "%-25s %10s" % ("NOME", "TAMANHO")
    with open("diretorios.txt", "w", encoding="utf-8") as file:
        file.write(TOP + "\n")
        for k, v in dados.items():
            linha = FORMAT % (k, bytes2human(v))
            file.write(linha + "\n")


def main():
    pasta = input("Para gerar o relatório, digite o diretório: ")
    if os.path.exists(pasta):
        gravar_texto(tamanho_arquivos(pasta))



if __name__ == "__main__":
    main()
