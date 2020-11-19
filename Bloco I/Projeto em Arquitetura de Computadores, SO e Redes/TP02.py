import pygame, sys
import psutil
import platform
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
TELA_S3 = (LARGURA_TELA, ALTURA_TELA // 3 + 50)

ESPESSURA_BARRA = 15


# Memória
def top_surface(memoria):
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
def middle_surface():
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
def bottom_surface():
    surface_03 = pygame.Surface(TELA_S3)
    surface_03.convert()
    surface_03.fill(ESCURO)
    TELA.blit(surface_03, (0, 180))


# FIM SURFACES

# Função que retorna as infos sobre a memória
def uso_memoria_fisica():
    mem = psutil.virtual_memory()
    return mem


def main():
    controle = 60
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Para fins de desenvolvimento (Posição na tela)
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
        if controle == 60:
            bottom_surface()
            middle_surface()
            top_surface(uso_memoria_fisica())
            controle = 0
        pygame.display.update()
        controle += 1
        CLOCK.tick(HZ)


if __name__ == '__main__':
    main()
