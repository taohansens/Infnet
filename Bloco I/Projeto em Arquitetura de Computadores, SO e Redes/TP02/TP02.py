# Importação de bibliotecas
import platform
import psutil
import re
from urllib.request import urlopen

import pygame
import sys
from pygame.locals import *

# INICIA PYGAME
pygame.init()
CLOCK = pygame.time.Clock()
HZ = 60
# FONTES
pygame.font.init()
FONTE_TITLE = pygame.font.SysFont("segoe-ui", 32)
FONTE_INFO = pygame.font.SysFont("segoe-ui", 18)
FONTE_PERCENT = pygame.font.SysFont("segoe", 26)

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
TELA_S1 = (LARGURA_TELA, ALTURA_TELA // 3 - 90)
TELA_S2 = (LARGURA_TELA, ALTURA_TELA // 3 - 20)
TELA_S3 = (LARGURA_TELA, ALTURA_TELA // 3 - 50)
TELA_S4 = (LARGURA_TELA, ALTURA_TELA // 2 + 100)

ESPESSURA_BARRA = 15


# Memória
def memoria(memoria):
    surface_01 = pygame.Surface(TELA_S1)
    surface_01.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 60
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
    surface_01.blit(titulo, (70, pos_altura_barra - 50))
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


# Processador
def processador():
    uso_cpu = psutil.cpu_percent(interval=0)
    surface_02 = pygame.Surface(TELA_S2)
    surface_02.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 60
    pos_final_barra = int(LARGURA_TELA - LARGURA_TELA * 0.15)
    # Desenha barra total (em azul)
    pygame.draw.rect(surface_02, AZUL, (70, pos_altura_barra, pos_final_barra, ESPESSURA_BARRA))
    # Barra de uso (em vermelho)
    pos_final_barra_uso = pos_final_barra * (uso_cpu / 100)
    pygame.draw.rect(surface_02, VERMELHO, (70, pos_altura_barra, pos_final_barra_uso, ESPESSURA_BARRA))

    # Início Textos
    perc_texto = "{}%".format(uso_cpu)
    titulo = FONTE_TITLE.render("Uso do Processador", True, ESCURO)
    percentagem_uso = FONTE_PERCENT.render(perc_texto, True, ESCURO)
    surface_02.blit(titulo, (70, pos_altura_barra - 50))
    surface_02.blit(percentagem_uso, (15, pos_altura_barra))

    # Info processador
    processor_name = "{}".format(platform.processor())
    sistema_op = "SO: {} ({})".format(platform.system(), platform.platform())
    processor_cores = "Clock: {} GHz, {} núcleos, Arquitetura ({})".format(psutil.cpu_freq().current/1000, psutil.cpu_count(), platform.architecture()[0])
    processor_cores_obj = FONTE_INFO.render(processor_cores, True, ESCURO)
    sistema_op_obj = FONTE_INFO.render(sistema_op, True, ESCURO)
    processor_name_obj = FONTE_INFO.render(processor_name, True, ESCURO)
    surface_02.blit(processor_name_obj, (70, pos_altura_barra + 20))
    surface_02.blit(processor_cores_obj, (70, pos_altura_barra + 45))
    surface_02.blit(sistema_op_obj, (70, pos_altura_barra + 70))
    TELA.blit(surface_02, (0, 110))


# Disco
def disco():
    disk = verifica_discos()
    surface_03 = pygame.Surface(TELA_S3)
    surface_03.fill(CINZA)
    # Posições em pixels
    pos_altura_barra = 60
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
    surface_03.blit(titulo, (70, pos_altura_barra - 50))
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
    TELA.blit(surface_03, (0, 270))


# Rede
def rede(ip_pub):
    # Interface de rede terá que ser colocada manualmente, variação muito grande.
    INTERFACE_REDE = "Wi-Fi"

    dic_interfaces = psutil.net_if_addrs()
    ip_rede = dic_interfaces[INTERFACE_REDE][1].address
    net_mask = dic_interfaces[INTERFACE_REDE][1].netmask
    ip_local = "IPv4 Local: {}".format(ip_rede)
    ip_public = "IP Público: {}".format(ip_pub)
    ip_netmask = "Máscara de Sub-rede: {}".format(net_mask)
    ip_local_obj = FONTE_TITLE.render(ip_local, True, ESCURO)
    ip_netmask_obj = FONTE_INFO.render(ip_netmask, True, ESCURO)
    ip_pub_obj = FONTE_TITLE.render(ip_public, True, ESCURO)
    surface_04 = pygame.Surface(TELA_S4)
    surface_04.fill(CINZA)
    surface_04.blit(ip_local_obj, (70, 160))
    surface_04.blit(ip_pub_obj, (70, 200))
    surface_04.blit(ip_netmask_obj, (70, 250))

    TELA.blit(surface_04, (0, 270))
# FIM SURFACES


# Função que retorna as infos sobre a memória
def uso_memoria_fisica():
    mem = psutil.virtual_memory()
    return mem


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


# Verifica o IP público que acessou a página do dyndns.
def ip_publico():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)


# Variável inicializada vazia (IP_Externo)
ip_net = ""


def main():
    controle = 60
    ip_net = ip_publico()
    if ip_net != "":
        ip_rede = ip_net
    else:
        ip_rede = 'Sem conexão.'
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if controle == 60:
            rede(ip_rede)
            disco()
            processador()
            memoria(uso_memoria_fisica())
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
