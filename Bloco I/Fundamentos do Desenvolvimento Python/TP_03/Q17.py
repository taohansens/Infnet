"""
Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação.
Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
"""

import pygame, sys
from pygame.locals import *
# CONSTANTES
# FPS
FPS = 60

# DISPLAY
LARGURA_TELA = 800
ALTURA_TELA = 600

def main():
    pygame.init()
    global DISPLAYSURF

    # Clock
    FPSCLOCK = pygame.time.Clock()
    # Display
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Pong")

    terminou = False
    while not terminou:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    # Saindo do loop, encerrando janela e finalizando o pygame
    pygame.display.quit()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()