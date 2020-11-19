import pygame, sys
from pygame.locals import *

pygame.init()

# Iniciando a janela principal
LARGURA_TELA = 500
ALTURA_TELA = 500
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Gerenciador de Recursos")

# CORES
CINZA = (236, 240, 241)
ESCURO = (52, 73, 94)
VERMELHO = (231, 76, 60)
AZUL = (52, 152, 219)
BRANCO = (255, 255, 255)

# Surface 01
Surface_01 = pygame.Surface((LARGURA_TELA, ALTURA_TELA // 3 - 10))
Surface_01_box = pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA // 3 - 10)
Surface_01 = Surface_01.convert()
Surface_01.fill(CINZA)

# Surface 02
Surface_02 = pygame.Surface((LARGURA_TELA, ALTURA_TELA // 3 * 2))
Surface_02_box = pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA // 3 * 2)
Surface_02 = Surface_02.convert()
Surface_02.fill(AZUL)

# Surface 03
Surface_03 = pygame.Surface((LARGURA_TELA, ALTURA_TELA // 3 * 3))
Surface_03_box = pygame.Rect(0, 0, LARGURA_TELA, ALTURA_TELA // 3 * 3)
Surface_03 = Surface_03.convert()
Surface_03.fill(VERMELHO)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    TELA.blit(Surface_03, Surface_03_box)
    TELA.blit(Surface_02, Surface_02_box)
    TELA.blit(Surface_01, Surface_01_box)

    pygame.display.flip()
