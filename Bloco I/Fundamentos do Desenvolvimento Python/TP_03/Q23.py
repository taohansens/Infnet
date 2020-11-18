"""
Q.23
(Desafio) Usando a biblioteca Pygame, escreva um programa que implemente o jogo da velha para dois jogadores
(ambos usuários). (código e printscreen)
"""
import pygame, sys
from pygame.locals import *
FPS = 60

# DISPLAY
LARGURA_TELA = 800
ALTURA_TELA = 600
LARGURA_LINHA = 10

# CORES
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

def desenhar_tabuleiro():
    DISPLAYSURF.fill(BRANCO)
    pygame.draw.rect(DISPLAYSURF, PRETO, ((0, 0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA * 2)
    # Desenha linhas
    # lARGURA = 444
    #ALTURA = 90
    pygame.draw.line(DISPLAYSURF, PRETO, ((LARGURA_TELA // 3), ALTURA_TELA*0.15), ((LARGURA_TELA // 3), ALTURA_TELA - ALTURA_TELA*0.15),
                     LARGURA_LINHA)
    pygame.draw.line(DISPLAYSURF, PRETO, ((LARGURA_TELA // 1.8), ALTURA_TELA * 0.15),
                     ((LARGURA_TELA // 1.8), ALTURA_TELA - ALTURA_TELA * 0.15), LARGURA_LINHA)
    # Desenha colunas
    pygame.draw.line(DISPLAYSURF, PRETO, ((LARGURA_TELA // 10), ALTURA_TELA * 0.37), ((LARGURA_TELA - LARGURA_TELA * 0.2), ALTURA_TELA * 0.37),
                     LARGURA_LINHA)
    pygame.draw.line(DISPLAYSURF, PRETO, ((LARGURA_TELA // 10), ALTURA_TELA * 0.64),
                     ((LARGURA_TELA - LARGURA_TELA * 0.2), ALTURA_TELA * 0.64),
                     LARGURA_LINHA)


def main():
    pygame.init()
    global DISPLAYSURF
    # Informações sobre a fonte do placar
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 48
    BASICFONT = pygame.font.SysFont('unispacebold', BASICFONTSIZE)
    # Clock
    FPSCLOCK = pygame.time.Clock()
    # Display
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Jogo da Velha")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # encerrando janela e finalizando o pygame
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        desenhar_tabuleiro()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
