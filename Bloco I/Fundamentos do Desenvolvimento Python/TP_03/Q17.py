"""
Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação.
Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
"""

import pygame, sys
from pygame.locals import *

# Provável Menu
# SE jogador == 0, será bot x bot.
# SE jogador == 1, será player x bot.
# SE jogador == 2, player x player.
JOGADOR = 2

# CONSTANTES
# FPS
FPS = 300

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


# Verifica a colisão da bola com a paleta1 ou paleta2
def verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else:
        return 1


def paleta_bot(bola, bolaDirX, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -=1
    return paleta2



def paleta_double_bot(bola, bolaDirX, paleta1, paleta2):
    # Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    if bolaDirX == -1:
        if paleta1.centery < bola.centery:
            paleta1.y += 1
        else:
            paleta1.y -= 1
    return paleta1, paleta2


# Verifica se um jogador fez ponto e retorna o novo valor do placar
def verifica_placar(paleta1, bola, placar, bolaDirX):
    if bola.left == LARGURA_LINHA:
        return 0


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

    # Placar
    placar_player = 0
    placar_bot = 0

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
            elif JOGADOR == 1 or JOGADOR == 2:
                if event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    # Se apenas um jogador, controlará a paleta esquerda;
                    if JOGADOR == 1:
                        paleta1.y = mouseY
                    # Controlar as duas paletas, a depender da posição do mouse na mesa.
                    # Se estiver mais para esquerda, controlará a paleta esquerda, se não, a paleta direita.
                    if JOGADOR == 2:
                        if mouseX < LARGURA_TELA/2:
                            paleta1.y = mouseY
                        if mouseX > LARGURA_TELA / 2:
                            paleta2.y = mouseY

        desenha_arena()
        desenha_paleta(paleta1)
        desenha_paleta(paleta2)
        desenha_bola(bola)
        bola = movimento_bola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verifica_colisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verifica_colisao_paletas(bola, paleta1, paleta2, bolaDirX)

        if JOGADOR == 0:
            paleta1, paleta2 = paleta_double_bot(bola, bolaDirX, paleta1, paleta2)
        if JOGADOR == 1:
            paleta2 = paleta_bot(bola, bolaDirX, paleta2)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
