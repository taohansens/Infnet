"""
Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação.
Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
"""

import pygame, sys
from pygame.locals import *
# CONSTANTES
# FPS
FPS = 60
FPSCLOCK = pygame.time.Clock()

# DISPLAY
LARGURA_TELA = 800
ALTURA_TELA = 600


pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

terminou = False
while not terminou:
    # Atualiza o desenho na tela
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    FPSCLOCK.tick(FPS)

# Finaliza a janela
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
sys.exit()