# Importação de bibliotecas
import platform
import re
import sys
from datetime import datetime

import cpuinfo
from urllib.request import urlopen

import psutil
import pygame
from dateutil.tz import tz
from pygame.locals import *

import os

# INICIA PYGAME
pygame.init()
CLOCK = pygame.time.Clock()
HZ = 60

# FONTES
pygame.font.init()
FONTE_TITLE = pygame.font.SysFont("segoe-ui-bold", 60)
FONTE_INFO = pygame.font.SysFont("segoe-ui", 18)
FONTE_INFO_BOLD = pygame.font.SysFont("segoe-ui-bold", 26)
FONTE_SUBINFO_BOLD = pygame.font.SysFont("segoe-ui-bold", 20)
FONTE_PERCENT = pygame.font.SysFont("segoe", 26)
FONTE_PERCENT_PROC = pygame.font.SysFont("segoe", 20)

# Iniciando a janela principal
LARGURA_TELA = 600
ALTURA_TELA = 600
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Gerenciador de Recursos")

# CORES
CINZA = (236, 240, 241)
ESCURO = (52, 73, 94)
VERMELHO = (231, 76, 60)
AZUL = (52, 152, 219)
BRANCO = (255, 255, 255)


# CONSTANTES COM O TAMANHO DA TELA
TAM_TELA = (LARGURA_TELA, 500)
TAM_SETA = (LARGURA_TELA, 100)

ESPESSURA_BARRA = 14

info_cpu = cpuinfo.get_cpu_info()


# ************************************************************ #
#                      Processador
# ************************************************************ #
def processador():
    uso_cpu = psutil.cpu_percent(percpu=True)
    surface_02 = pygame.Surface(TAM_TELA)
    surface_02.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 50

    # Textos Info processador
    # Título
    titulo = FONTE_TITLE.render("Uso do Processador", True, ESCURO)
    surface_02.blit(titulo, (40, 20))
    # Informações
    processor_name = "{}".format(info_cpu['brand_raw'])
    sistema_op = "SO: {} ({})".format(platform.system(), platform.platform())
    processor_cores = "Clock: {} GHz | Palavra: {} bits | Arch: {}".format(psutil.cpu_freq().current/1000, info_cpu['bits'], info_cpu['arch'])
    freq_info = "Frequência: {}Mhz / {}Mhz".format(psutil.cpu_freq().current, psutil.cpu_freq().max)
    processor_cores_obj = FONTE_INFO.render(processor_cores, True, ESCURO)
    sistema_op_obj = FONTE_INFO.render(sistema_op, True, ESCURO)
    processor_name_obj = FONTE_INFO.render(processor_name, True, ESCURO)
    freq_info_obj = FONTE_INFO.render(freq_info, True, ESCURO)
    surface_02.blit(processor_name_obj, (40, pos_altura_barra + 20))
    surface_02.blit(processor_cores_obj, (40, pos_altura_barra + 45))
    surface_02.blit(sistema_op_obj, (40, pos_altura_barra + 70))
    surface_02.blit(freq_info_obj, (40, pos_altura_barra + 92))

    qtd_nucleos = "{} threads | {} núcleos".format(psutil.cpu_count(),  psutil.cpu_count(logical=False))
    qtd_nucleos_obj = FONTE_INFO_BOLD.render(qtd_nucleos, True, ESCURO)
    surface_02.blit(qtd_nucleos_obj, (210, 175))

    # Laço sobre todas os núcleos.
    var_barra = 0
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    for i in uso_cpu:
        # texto da % de cada processador.
        perc_texto = "{}%".format(i)
        percentagem_uso = FONTE_PERCENT_PROC.render(perc_texto, True, ESCURO)
        surface_02.blit(percentagem_uso, (15, 200 + var_barra))

        pygame.draw.rect(surface_02, AZUL, (60, 200 + var_barra, pos_final_barra, ESPESSURA_BARRA))
        pos_final_barra_uso = pos_final_barra * (i / 100)
        pygame.draw.rect(surface_02, VERMELHO, (60, 200 + var_barra, pos_final_barra_uso, ESPESSURA_BARRA))
        var_barra += 25
    TELA.blit(surface_02, (0, 0))

# ************************************************************ #
#                      Memória RAM
# ************************************************************ #
def memoria_ram():
    memoria = psutil.virtual_memory()
    surface_01 = pygame.Surface(TAM_TELA)
    surface_01.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface_01, AZUL, (70, pos_altura_barra, pos_final_barra, ESPESSURA_BARRA))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (memoria.percent / 100)
    pygame.draw.rect(surface_01, VERMELHO, (70, pos_altura_barra, pos_final_barra_uso, ESPESSURA_BARRA))

    # Início Textos
    perc_texto = "{}%".format(memoria.percent)

    titulo = FONTE_TITLE.render("Uso Memória RAM", True, ESCURO)
    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_01.blit(titulo, (40, 20))
    surface_01.blit(percentagem_uso, (15, pos_altura_barra))

    # Memoria total
    memoria_total = "Memória física total: {:g} GB".format(round(memoria.total / (1024.0 ** 3), 0))
    memoria_total_obj = FONTE_INFO.render(memoria_total, True, ESCURO)
    surface_01.blit(memoria_total_obj, (pos_final_barra - 150, pos_altura_barra - 30))

    # Memoria Física total
    memoria_livre = "Memória em uso: {:.2f} GB | Memória livre: {:.2f} GB".format(memoria.used / (1024.0 ** 3),
                                                                                  memoria.free / (1024.0 ** 3))
    memoria_livre_obj = FONTE_INFO.render(memoria_livre, True, ESCURO)
    surface_01.blit(memoria_livre_obj, (LARGURA_TELA // 5, pos_altura_barra + 20))
    TELA.blit(surface_01, (0, 0))


# ************************************************************ #
#                      Disco
# ************************************************************ #
def disco():
    disk = verifica_discos()
    surface_03 = pygame.Surface(TAM_TELA)
    surface_03.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 110
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface_03, AZUL, (70, pos_altura_barra, pos_final_barra, ESPESSURA_BARRA))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (disk[5] / 100)
    pygame.draw.rect(surface_03, VERMELHO, (70, pos_altura_barra, pos_final_barra_uso, ESPESSURA_BARRA))

    # Início Textos
    perc_texto = "{}%".format(disk[5])

    titulo = FONTE_TITLE.render("Espaço Total em Disco", True, ESCURO)
    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_03.blit(titulo, (40, 20))
    surface_03.blit(percentagem_uso, (15, pos_altura_barra))

    # Espaço total

    qtd_total = "Encontrados: {:g}".format(round(disk[0]))
    qtd_total_obj = FONTE_INFO.render(qtd_total, True, ESCURO)
    mont_hds = "{}".format(disk[1])
    mont_hds_obj = FONTE_INFO.render(mont_hds, True, ESCURO)
    surface_03.blit(qtd_total_obj, (pos_final_barra - 50, pos_altura_barra + 20))
    surface_03.blit(mont_hds_obj, (pos_final_barra - 40, pos_altura_barra + 40))

    # Espaço livre/ocupado no hd
    espaco_livre = "Espaço livre: {:.2f} GB".format(disk[4] / (1024.0 ** 3))
    espaco_ocupado = "Espaço usado: {:.2f} GB".format(disk[3] / (1024.0 ** 3))
    espaco_livre_obj = FONTE_INFO.render(espaco_livre, True, ESCURO)
    espaco_ocupado_obj = FONTE_INFO.render(espaco_ocupado, True, ESCURO)
    surface_03.blit(espaco_livre_obj, (70, pos_altura_barra + 20))
    surface_03.blit(espaco_ocupado_obj, (70, pos_altura_barra + 40))
    TELA.blit(surface_03, (0, 0))


# ************************************************************ #
#                      Surface Rede
# ************************************************************ #
def rede(ip_pub):
    # Interface de rede terá que ser colocada manualmente, variação muito grande.
    dic_interfaces = psutil.net_if_addrs()
    if "Wi-Fi 6" in dic_interfaces:
        INTERFACE_REDE = "Wi-Fi 6"
    elif "Ethernet" in dic_interfaces:
        INTERFACE_REDE = "Ethernet"
    else:
        INTERFACE_REDE = "Wi-Fi 2"

    ip_rede = dic_interfaces[INTERFACE_REDE][1].address
    net_mask = dic_interfaces[INTERFACE_REDE][1].netmask
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_public = "IP Público: {}".format(ip_pub)
    ip_netmask = "Máscara de Sub-rede: {}".format(net_mask)
    ip_local_obj = FONTE_TITLE.render(ip_local, True, ESCURO)
    ip_netmask_obj = FONTE_INFO.render(ip_netmask, True, ESCURO)
    ip_pub_obj = FONTE_TITLE.render(ip_public, True, ESCURO)
    surface_04 = pygame.Surface(TAM_TELA)
    surface_04.fill(CINZA)
    titulo = FONTE_TITLE.render("Informações de Rede", True, ESCURO)
    surface_04.blit(titulo, (40, 20))
    surface_04.blit(ip_local_obj, (20, 200))
    surface_04.blit(ip_pub_obj, (20, 240))
    surface_04.blit(ip_netmask_obj, (20, 290))

    TELA.blit(surface_04, (0, 0))


# ************************************************************ #
#                      Surface Resumo
# ************************************************************ #
def resumo():
    surface_05 = pygame.Surface(TAM_TELA)
    surface_05.fill(CINZA)
    pos_altura_barra = 75

    # Título
    titulo = FONTE_TITLE.render("Resumo de Informações", True, ESCURO)
    surface_05.blit(titulo, (40, 20))

    # ************************************************************ #
    #                      Processador
    # ************************************************************ #
    titulo = FONTE_SUBINFO_BOLD.render("Processador", True, ESCURO)
    surface_05.blit(titulo, (40, 80))
    processor_name = "{}".format(info_cpu['brand_raw'])
    sistema_op = "SO: {} ({})".format(platform.system(), platform.platform())
    processor_cores = "Clock: {} GHz | Palavra: {} bits | Arch: {}".format(psutil.cpu_freq().current / 1000,
                                                                           info_cpu['bits'], info_cpu['arch'])
    freq_info = "Frequência: {}Mhz / {}Mhz".format(psutil.cpu_freq().current, psutil.cpu_freq().max)
    processor_cores_obj = FONTE_INFO.render(processor_cores, True, ESCURO)
    sistema_op_obj = FONTE_INFO.render(sistema_op, True, ESCURO)
    processor_name_obj = FONTE_INFO.render(processor_name, True, ESCURO)
    freq_info_obj = FONTE_INFO.render(freq_info, True, ESCURO)
    surface_05.blit(processor_name_obj, (40, pos_altura_barra + 20))
    surface_05.blit(processor_cores_obj, (40, pos_altura_barra + 45))
    surface_05.blit(sistema_op_obj, (40, pos_altura_barra + 70))
    surface_05.blit(freq_info_obj, (40, pos_altura_barra + 92))

    qtd_nucleos = "{} threads | {} núcleos".format(psutil.cpu_count(), psutil.cpu_count(logical=False))
    qtd_nucleos_obj = FONTE_INFO.render(qtd_nucleos, True, ESCURO)
    surface_05.blit(qtd_nucleos_obj, (410, 100))

    uso_cpu = psutil.cpu_percent(interval=0)

    perc_texto = "{}%".format(uso_cpu)
    titulo = FONTE_PERCENT.render("Uso do Processador", True, ESCURO)
    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_05.blit(titulo, (410, 85))
    surface_05.blit(percentagem_uso, (460, 130))

    # Desenha barra total (em azul)
    pygame.draw.rect(surface_05, AZUL, (430, 150, 100, ESPESSURA_BARRA))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = 100 * (uso_cpu / 100)
    pygame.draw.rect(surface_05, VERMELHO, (430, 150, pos_final_barra_uso, ESPESSURA_BARRA))

    # ************************************************************ #
    #                      Memória RAM
    # ************************************************************ #
    memoria = psutil.virtual_memory()
    titulo_memoria = FONTE_SUBINFO_BOLD.render("Memória", True, ESCURO)
    surface_05.blit(titulo_memoria, (40, 210))
    perc_texto = "{}%".format(memoria.percent)

    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_05.blit(percentagem_uso, (40, 230))

    pos_altura_barra = 230
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.2)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface_05, AZUL, (100, pos_altura_barra, pos_final_barra, 20))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (memoria.percent / 100)
    pygame.draw.rect(surface_05, VERMELHO, (100, pos_altura_barra, pos_final_barra_uso, 20))

    memoria_total = "Memória física total: {:g} GB".format(round(memoria.total / (1024.0 ** 3), 0))
    memoria_total_obj = FONTE_INFO.render(memoria_total, True, ESCURO)
    surface_05.blit(memoria_total_obj, (pos_final_barra - 150, pos_altura_barra - 30))

    # Memoria Física total
    memoria_livre = "Memória em uso: {:.2f} GB | Memória livre: {:.2f} GB".format(memoria.used / (1024.0 ** 3),
                                                                                  memoria.free / (1024.0 ** 3))
    memoria_livre_obj = FONTE_INFO.render(memoria_livre, True, ESCURO)
    surface_05.blit(memoria_livre_obj, (LARGURA_TELA // 5, pos_altura_barra + 20))

    # ************************************************************ #
    #                            Discos
    # ************************************************************ #
    disk = verifica_discos()
    # Posições em pixels
    pos_altura_barra = 320
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.2)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface_05, AZUL, (100, pos_altura_barra, pos_final_barra, 20))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (disk[5] / 100)
    pygame.draw.rect(surface_05, VERMELHO, (100, pos_altura_barra, pos_final_barra_uso, 20))

    # Início Textos
    perc_texto = "{}%".format(disk[5])

    titulo = FONTE_SUBINFO_BOLD.render("Espaço em Disco", True, ESCURO)
    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_05.blit(titulo, (40, 300))
    surface_05.blit(percentagem_uso, (40, pos_altura_barra))

    # Espaço total
    qtd_total = "Encontrados: {:g}".format(round(disk[0]))
    qtd_total_obj = FONTE_INFO.render(qtd_total, True, ESCURO)
    mont_hds = "{}".format(disk[1])
    mont_hds_obj = FONTE_INFO.render(mont_hds, True, ESCURO)
    surface_05.blit(qtd_total_obj, (pos_final_barra - 50, pos_altura_barra + 20))
    surface_05.blit(mont_hds_obj, (pos_final_barra - 40, pos_altura_barra + 40))

    # Espaço livre/ocupado no hd
    espaco_livre = "Espaço livre: {:.2f} GB".format(disk[4] / (1024.0 ** 3))
    espaco_ocupado = "Espaço usado: {:.2f} GB".format(disk[3] / (1024.0 ** 3))
    espaco_livre_obj = FONTE_INFO.render(espaco_livre, True, ESCURO)
    espaco_ocupado_obj = FONTE_INFO.render(espaco_ocupado, True, ESCURO)
    surface_05.blit(espaco_livre_obj, (70, pos_altura_barra + 20))
    surface_05.blit(espaco_ocupado_obj, (70, pos_altura_barra + 40))

    # ************************************************************ #
    #                   Informações de REDE.
    # ************************************************************ #
    dic_interfaces = psutil.net_if_addrs()
    if "Wi-Fi 6" in dic_interfaces:
        INTERFACE_REDE = "Wi-Fi 6"
    elif "Ethernet" in dic_interfaces:
        INTERFACE_REDE = "Ethernet"
    else:
        INTERFACE_REDE = "Wi-Fi"
    ip_rede = dic_interfaces[INTERFACE_REDE][1].address
    net_mask = dic_interfaces[INTERFACE_REDE][1].netmask
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_public = "IP Público: {}".format(ip_publico())
    ip_netmask = "Máscara de Sub-rede: {}".format(net_mask)
    ip_local_obj = FONTE_INFO.render(ip_local, True, ESCURO)
    ip_netmask_obj = FONTE_INFO.render(ip_netmask, True, ESCURO)
    ip_pub_obj = FONTE_INFO.render(ip_public, True, ESCURO)
    titulo = FONTE_SUBINFO_BOLD.render("Informações de Rede", True, ESCURO)
    surface_05.blit(titulo, (40, 400))
    surface_05.blit(ip_local_obj, (40, 420))
    surface_05.blit(ip_pub_obj, (40, 440))
    surface_05.blit(ip_netmask_obj, (40, 460))
    # ************************************************************ #

    TELA.blit(surface_05, (0,0))


# Verifica todos os discos do usuario:
#   RETORNOS POR POSIÇÃO:
#   qtd_discos[0] [int]
#   string_com_discos[1] [str],
#   espaco_total[2] [int],
#   espaco_usado[3] [int],
#   espaco_livre[4] [int]
#   (TODAS UNIDADES EM BYTES), e a
#   percentagem de uso [5] [int]
def verifica_discos():
    # verifica a quantidade de discos
    qtd_discos = len(psutil.disk_partitions())
    discos = []
    espaco_total = 0
    espaco_usado = 0
    espaco_livre = 0

    # Faz a iteração sobre os retornos do disk_partitions e disk_usage.
    for partition in psutil.disk_partitions():
        discos.append(partition[1])
        espaco_total += psutil.disk_usage(partition[1])[0]
        espaco_usado += psutil.disk_usage(partition[1])[1]
        espaco_livre += psutil.disk_usage(partition[1])[2]

    string_discos = ""
    for i in range(len(discos)):
        string_discos += discos[i]+" "

    # Calcula a porcentagem do uso total.
    percent_usado = round(espaco_usado / espaco_total * 100, 1)
    return qtd_discos, string_discos, espaco_total, espaco_usado, espaco_livre, percent_usado


def timestamp_converter(st_time):
    time = datetime.fromtimestamp(st_time, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    return time


def listagem_diretorio(diretorio):
    class InfoArquivos():
        def __init__(self, nome, tamanho, atime, mtime):
            self.nome = nome
            self.tamanho = tamanho
            self.atime = atime
            self.mtime = mtime

    lista_arquivos = []
    lista_diretorios = []

    if os.path.exists(diretorio):
        l_arquivos = os.listdir(diretorio)
        for arquivo in l_arquivos:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            arquivo_stat = os.stat(caminho_arquivo)
            tamanho = f"{arquivo_stat.st_size // 1024} KB"
            instFile = InfoArquivos(arquivo, tamanho, timestamp_converter(os.stat(caminho_arquivo).st_atime),
                                timestamp_converter(os.stat(caminho_arquivo).st_mtime))
            if os.path.isfile(caminho_arquivo):
                lista_arquivos.append(instFile)
            elif os.path.isdir(caminho_arquivo):
                lista_diretorios.append(instFile)
            else:
                print('ERROR')

    return lista_arquivos, lista_diretorios


def arquivos():
    listagem_diretorio(os.environ['HOMEPATH'])
    surface_06 = pygame.Surface(TAM_TELA)
    surface_06.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 50

    # Textos Info processador
    # Título
    titulo = FONTE_TITLE.render("Listagem da pasta:", True, ESCURO)
    subtitulo = FONTE_SUBINFO_BOLD.render(os.environ['HOMEPATH'], True, ESCURO)

    surface_06.blit(titulo, (40, 20))
    # Informações
    processor_name = "{}".format(info_cpu['brand_raw'])
    sistema_op = "SO: {} ({})".format(platform.system(), platform.platform())
    processor_cores = "Clock: {} GHz | Palavra: {} bits | Arch: {}".format(psutil.cpu_freq().current/1000, info_cpu['bits'], info_cpu['arch'])
    freq_info = "Frequência: {}Mhz / {}Mhz".format(psutil.cpu_freq().current, psutil.cpu_freq().max)
    processor_cores_obj = FONTE_INFO.render(processor_cores, True, ESCURO)
    sistema_op_obj = FONTE_INFO.render(sistema_op, True, ESCURO)
    processor_name_obj = FONTE_INFO.render(processor_name, True, ESCURO)
    freq_info_obj = FONTE_INFO.render(freq_info, True, ESCURO)
    surface_06.blit(processor_name_obj, (40, pos_altura_barra + 20))
    surface_06.blit(processor_cores_obj, (40, pos_altura_barra + 45))
    surface_06.blit(sistema_op_obj, (40, pos_altura_barra + 70))
    surface_06.blit(freq_info_obj, (40, pos_altura_barra + 92))

    qtd_nucleos = "{} threads | {} núcleos".format(psutil.cpu_count(),  psutil.cpu_count(logical=False))
    qtd_nucleos_obj = FONTE_INFO_BOLD.render(qtd_nucleos, True, ESCURO)
    surface_06.blit(qtd_nucleos_obj, (210, 175))

    # Laço sobre todas os núcleos.
    var_barra = 0
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    for i in range(1):
        # texto da % de cada processador.
        perc_texto = "{}%".format(i)
        percentagem_uso = FONTE_PERCENT_PROC.render(perc_texto, True, ESCURO)
        surface_06.blit(percentagem_uso, (15, 200 + var_barra))

        pygame.draw.rect(surface_06, AZUL, (60, 200 + var_barra, pos_final_barra, ESPESSURA_BARRA))
        pos_final_barra_uso = pos_final_barra * (i / 100)
        pygame.draw.rect(surface_06, VERMELHO, (60, 200 + var_barra, pos_final_barra_uso, ESPESSURA_BARRA))
        var_barra += 25
    TELA.blit(surface_06, (0, 0))


def controle_setas():
    surface_seta = pygame.Surface(TAM_TELA)
    surface_seta.fill(CINZA)
    image = pygame.image.load(r'resources/seta-direita.png')
    imagered = pygame.transform.smoothscale(image, (70, 70))
    surface_seta.blit(imagered, (340, 10))
    surface_seta.blit(pygame.transform.rotate(imagered, 180), (180, 10))
    TELA.blit(surface_seta, (0, 500))


def colisao_setas(mouse):
    # Posições das setas esquerda e direita
    # Posição no eixo x
    if 510 <= mouse[1] <= 580:
        if 180 <= mouse[0] <= 240:
            return 1
        if 350 <= mouse[0] <= 405:
            return 2


# Verifica o IP público que acessou a página do dyndns.
def ip_publico():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)


# Variável inicializada vazia (IP_Externo)
ip_net = ""


def main():
    controle = 60
    pagina = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if colisao_setas(pos) == 1:
                    if pagina > 0:
                        pagina -= 1
                if colisao_setas(pos) == 2:
                    if pagina < 7:
                        pagina += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if pagina > 0:
                        pagina -= 1
                if event.key == pygame.K_RIGHT:
                    if pagina < 7:
                        pagina += 1
                if event.key == pygame.K_SPACE:
                    pagina = 4

        if controle == 60:
            controle_setas()
            if pagina == 0:
                processador()
            if pagina == 1:
                memoria_ram()
            if pagina == 2:
                disco()
            if pagina == 3:
                rede(ip_publico())
            if pagina == 4:
                resumo()
            if pagina == 5:
                arquivos()
            if pagina == 6:
                resumo()
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
