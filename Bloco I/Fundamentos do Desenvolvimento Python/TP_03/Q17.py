"""
Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação.
Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
"""

import pygame, sys
from pygame.locals import *

# CONSTANTES
# FPS
FPS = 120

# DISPLAY
LARGURA_TELA = 800
ALTURA_TELA = 600

# GAME
LARGURA_LINHA = 10
PALETA_TAMANHO = 50
PALETAOFFSET = 20

# CORES
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


# Função para desenhar o fundo do jogo
def desenha_arena():
    DISPLAYSURF.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(DISPLAYSURF, BRANCO, ((0, 0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA * 2)
    # Desenha a linha no centro
    pygame.draw.line(DISPLAYSURF, BRANCO, ((LARGURA_TELA // 2), 0), ((LARGURA_TELA // 2), ALTURA_TELA), (LARGURA_LINHA // 4))


# Função para desenhar a paleta
def desenha_paleta(paleta):
    # Impede da paleta ir além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    # Impede da paleta ir além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    # Desenha a paleta
    pygame.draw.rect(DISPLAYSURF, BRANCO, paleta)


# Função para desenhar a bola
def desenha_bola(bola):
    pygame.draw.rect(DISPLAYSURF, BRANCO, bola)


# Função para atualizar posição da bola
def movimento_bola(bola, eixo_x, eixo_y):
    bola.x += eixo_x
    bola.y += eixo_y
    return bola


# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verifica_colisao(bola, bolaDirX, bolaDirY):
    if bola.top == LARGURA_LINHA or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == LARGURA_LINHA or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY


def main():
    pygame.init()
    global DISPLAYSURF

    # Clock
    FPSCLOCK = pygame.time.Clock()
    # Display
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Pong")

    # Posições iniciais
    bolaX = LARGURA_TELA // 2 - LARGURA_LINHA // 2
    bolaY = ALTURA_TELA // 2 - LARGURA_LINHA // 2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2

    # Altera posição da bola
    bolaDirX = -1
    bolaDirY = -1

    # Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,
                          PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    # Desenhando as posições iniciais da arena
    desenha_arena()
    desenha_paleta(paleta1)
    desenha_paleta(paleta2)
    desenha_bola(bola)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # encerrando janela e finalizando o pygame
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        desenha_arena()
        desenha_paleta(paleta1)
        desenha_paleta(paleta2)
        desenha_bola(bola)
        bola = movimento_bola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verifica_colisao(bola, bolaDirX, bolaDirY)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
